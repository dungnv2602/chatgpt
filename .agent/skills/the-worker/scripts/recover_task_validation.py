"""Reconcile missed ADR-0008 publications from workflow metadata and aggregate artifacts."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import publish_task_validation as publisher


API_VERSION = "2022-11-28"
POLICY_PATH = ".agent/skills/the-worker/assets/task-validation/task-validation-policy.json"
INDEX_PATH = publisher.INDEX_PATH
REVIEW_ROOT = publisher.REVIEW_ROOT
RETENTION_DAYS = 3
MAX_API_RETRIES = 5
MAX_PUSH_RETRIES = 5


class RecoveryError(RuntimeError):
    """Raised when the recovery sweep cannot safely reconcile its inputs."""


class GitHubAPI:
    def __init__(self, token: str, api_url: str = "https://api.github.com") -> None:
        if not token:
            raise RecoveryError("GITHUB_TOKEN is required for Actions metadata recovery")
        self.base = api_url.rstrip("/")
        self.token = token

    def request(self, path: str, *, binary: bool = False, allow_not_found: bool = False) -> bytes | None:
        url = self.base + path
        for attempt in range(1, MAX_API_RETRIES + 1):
            request = urllib.request.Request(
                url,
                headers={
                    "Accept": "application/vnd.github+json",
                    "Authorization": f"Bearer {self.token}",
                    "X-GitHub-Api-Version": API_VERSION,
                    "User-Agent": "chatgpt-task-validation-recovery",
                },
                method="GET",
            )
            try:
                with urllib.request.urlopen(request, timeout=30) as response:
                    return response.read()
            except urllib.error.HTTPError as exc:
                if exc.code == 404 and allow_not_found:
                    return None
                if exc.code not in {403, 429, 500, 502, 503, 504} or attempt == MAX_API_RETRIES:
                    raise RecoveryError(f"GitHub API request failed ({exc.code}) for {path}") from exc
                retry_after = exc.headers.get("Retry-After")
                delay = min(int(retry_after), 20) if retry_after and retry_after.isdigit() else min(2 ** attempt, 16)
                time.sleep(delay)
            except urllib.error.URLError as exc:
                if attempt == MAX_API_RETRIES:
                    raise RecoveryError(f"GitHub API request failed for {path}: {exc}") from exc
                time.sleep(min(2 ** attempt, 16))
        raise RecoveryError(f"GitHub API retry budget exhausted for {path}")

    def json(self, path: str, *, allow_not_found: bool = False) -> Any:
        payload = self.request(path, allow_not_found=allow_not_found)
        if payload is None:
            return None
        try:
            return json.loads(payload.decode("utf-8"))
        except (UnicodeError, json.JSONDecodeError) as exc:
            raise RecoveryError(f"GitHub API returned invalid JSON for {path}") from exc

    def pages(self, path: str, collection: str) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        page = 1
        while True:
            separator = "&" if "?" in path else "?"
            payload = self.json(f"{path}{separator}per_page=100&page={page}")
            items = payload.get(collection, [])
            if not isinstance(items, list):
                raise RecoveryError(f"GitHub API response has no {collection} array")
            result.extend(item for item in items if isinstance(item, dict))
            if len(items) < 100:
                return result
            page += 1


def git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=root,
            shell=False,
            capture_output=True,
            text=True,
            check=False,
            timeout=60,
        )
    except subprocess.TimeoutExpired as exc:
        raise RecoveryError(f"git operation timed out: {' '.join(args[:2])}") from exc
    if check and result.returncode != 0:
        raise RecoveryError(f"git {' '.join(args[:2])} failed: {result.stderr[-2000:]}")
    return result


def utc_datetime(value: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (AttributeError, ValueError) as exc:
        raise RecoveryError("Workflow attempt timestamp is invalid") from exc
    if parsed.tzinfo is None:
        raise RecoveryError("Workflow attempt timestamp must include a timezone")
    return parsed.astimezone(timezone.utc)


def policy_blob_sha(root: Path, source_sha: str) -> str:
    publisher.ensure_source_commit(root, source_sha)
    content = git(root, "show", f"{source_sha}:{POLICY_PATH}").stdout.encode("utf-8")
    return hashlib.sha1(f"blob {len(content)}\0".encode("ascii") + content).hexdigest()


def list_runs(api: GitHubAPI, repository: str, workflow_file: str) -> list[dict[str, Any]]:
    owner_repo = urllib.parse.quote(repository, safe="/")
    workflow = urllib.parse.quote(Path(workflow_file).name, safe="")
    return api.pages(
        f"/repos/{owner_repo}/actions/workflows/{workflow}/runs?branch=gpt",
        "workflow_runs",
    )


def get_attempt(api: GitHubAPI, repository: str, run_id: int, attempt: int, fallback: dict[str, Any]) -> dict[str, Any]:
    owner_repo = urllib.parse.quote(repository, safe="/")
    payload = api.json(
        f"/repos/{owner_repo}/actions/runs/{run_id}/attempts/{attempt}",
        allow_not_found=True,
    )
    return payload if isinstance(payload, dict) else fallback


def get_jobs(api: GitHubAPI, repository: str, run_id: int, attempt: int) -> list[dict[str, Any]]:
    owner_repo = urllib.parse.quote(repository, safe="/")
    return api.pages(
        f"/repos/{owner_repo}/actions/runs/{run_id}/attempts/{attempt}/jobs",
        "jobs",
    )


def get_artifact_payload(
    api: GitHubAPI,
    repository: str,
    run_id: int,
    attempt: int,
) -> dict[str, Any] | None:
    owner_repo = urllib.parse.quote(repository, safe="/")
    artifacts = api.pages(
        f"/repos/{owner_repo}/actions/runs/{run_id}/artifacts",
        "artifacts",
    )
    expected_name = f"task-validation-aggregate-{run_id}-{attempt}"
    artifact = next(
        (item for item in artifacts if item.get("name") == expected_name and not item.get("expired")),
        None,
    )
    if artifact is None:
        return None
    artifact_id = artifact.get("id")
    if not isinstance(artifact_id, int):
        raise RecoveryError("Aggregate artifact ID is malformed")
    archive = api.request(
        f"/repos/{owner_repo}/actions/artifacts/{artifact_id}/zip",
        binary=True,
    )
    if archive is None:
        return None
    try:
        with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
            names = [name for name in bundle.namelist() if Path(name).name == ".task-validation-aggregate.json"]
            if len(names) != 1:
                raise RecoveryError("Aggregate artifact must contain exactly one structured result")
            payload = json.loads(bundle.read(names[0]).decode("utf-8"), object_pairs_hook=publisher.unique_object)
    except (zipfile.BadZipFile, UnicodeError, json.JSONDecodeError) as exc:
        raise RecoveryError("Aggregate artifact is corrupt or invalid") from exc
    if not isinstance(payload, dict):
        raise RecoveryError("Aggregate artifact payload must be an object")
    return payload


def attempt_kind(
    jobs: list[dict[str, Any]],
) -> tuple[str, dict[str, Any] | None]:
    policy_job = next(
        (job for job in jobs if job.get("name") == "Check protected policy and duplicate source SHA"),
        None,
    )
    coordinator_job = next(
        (
            job for job in jobs
            if isinstance(job.get("name"), str)
            and job["name"].startswith("Run exact-SHA coordinator")
        ),
        None,
    )
    if coordinator_job is not None:
        if coordinator_job.get("conclusion") == "skipped":
            return "ignored", coordinator_job
        if coordinator_job.get("status") != "completed":
            return "pending", coordinator_job
        if coordinator_job.get("conclusion") == "cancelled":
            return "cancelled", coordinator_job
        return "started", coordinator_job
    if policy_job is not None and policy_job.get("conclusion") == "failure":
        return "policy_failure", policy_job
    return "ignored", None


def fallback_aggregate(
    source_sha: str,
    policy_sha: str,
    run_id: int,
    attempt: int,
    outcome: str,
    completed_at: str,
) -> dict[str, Any]:
    return {
        "source_sha": source_sha,
        "policy_blob_sha": policy_sha,
        "coordinator_run_id": run_id,
        "attempt": attempt,
        "check_set_id": None,
        "expected_checks": [],
        "statuses": {},
        "outcome": outcome,
        "completed_at": completed_at,
    }


def record_exists(index: dict[str, Any], run_id: int, attempt: int) -> bool:
    return any(
        record["coordinator_run_id"] == run_id and record["attempt"] == attempt
        for record in index["attempts"]
    )


def current_index(root: Path) -> dict[str, Any]:
    return publisher.validate_index(publisher.read_json(root / INDEX_PATH))


def process_attempt(
    root: Path,
    api: GitHubAPI,
    repository: str,
    run: dict[str, Any],
    attempt_number: int,
) -> tuple[str, tuple[int, int]]:
    run_id = run.get("id")
    if not isinstance(run_id, int):
        raise RecoveryError("Workflow run ID is malformed")
    details = get_attempt(api, repository, run_id, attempt_number, run)
    source_sha = details.get("head_sha") or run.get("head_sha")
    if not isinstance(source_sha, str) or not re.fullmatch(r"[0-9a-f]{40}", source_sha):
        raise RecoveryError(f"Run {run_id}/{attempt_number} has no exact source SHA")
    if details.get("head_branch", run.get("head_branch")) != "gpt":
        return "ignored", (run_id, attempt_number)

    jobs = get_jobs(api, repository, run_id, attempt_number)
    kind, coordinator_job = attempt_kind(jobs)
    if kind == "ignored":
        return kind, (run_id, attempt_number)
    if kind == "pending":
        return kind, (run_id, attempt_number)

    completed_at = details.get("updated_at") or run.get("updated_at")
    if not isinstance(completed_at, str):
        raise RecoveryError(f"Run {run_id}/{attempt_number} has no completion timestamp")
    aggregate = get_artifact_payload(api, repository, run_id, attempt_number)

    if aggregate is not None:
        outcome = aggregate.get("outcome")
        if outcome not in publisher.OUTCOMES:
            aggregate = None
        elif aggregate.get("source_sha") != source_sha:
            aggregate = None

    if aggregate is None:
        outcome = "cancelled" if kind == "cancelled" else "capture_failure"
        policy_sha = policy_blob_sha(root, source_sha)
        aggregate = fallback_aggregate(
            source_sha, policy_sha, run_id, attempt_number, outcome, completed_at
        )
    else:
        policy_sha = aggregate.get("policy_blob_sha")
        if not isinstance(policy_sha, str) or not re.fullmatch(r"[0-9a-f]{40}", policy_sha):
            policy_sha = policy_blob_sha(root, source_sha)
            aggregate = fallback_aggregate(
                source_sha, policy_sha, run_id, attempt_number, "capture_failure", completed_at
            )

    with tempfile.TemporaryDirectory(prefix="task-validation-recovery-") as temp_dir:
        aggregate_path = Path(temp_dir) / "aggregate.json"
        aggregate_path.write_text(json.dumps(aggregate, separators=(",", ":")) + "\n", encoding="utf-8")
        actions_url = f"https://github.com/{repository}/actions/runs/{run_id}"
        publisher.publish_with_retry(
            root,
            aggregate_path,
            source_sha,
            policy_sha,
            run_id,
            attempt_number,
            actions_url,
            "gpt",
        )
    return "published_or_present", (run_id, attempt_number)


def checkpoint_and_prune(root: Path, known_attempts: list[tuple[int, int, str]], now: datetime) -> bool:
    index = current_index(root)
    current = (index["closed_through"]["run_id"], index["closed_through"]["attempt"])
    record_map = {
        (item["coordinator_run_id"], item["attempt"]): item
        for item in index["attempts"]
    }
    candidate = current
    for run_id, attempt, state in sorted(known_attempts):
        key = (run_id, attempt)
        if key <= current:
            continue
        if state != "completed":
            break
        record = record_map.get(key)
        if record is None or record["recovery"]["reconciled_at"] is None:
            break
        candidate = key

    changed = candidate != current
    if changed:
        index["closed_through"] = {"run_id": candidate[0], "attempt": candidate[1]}

    retained: list[dict[str, Any]] = []
    removed = 0
    for record in index["attempts"]:
        key = (record["coordinator_run_id"], record["attempt"])
        reconciled_at = record["recovery"]["reconciled_at"]
        expired = False
        if key <= candidate and reconciled_at is not None:
            expired = now - utc_datetime(reconciled_at) >= timedelta(days=RETENTION_DAYS)
        if expired:
            review_dir = root / REVIEW_ROOT / f"{key[0]}-{key[1]}"
            if review_dir.exists():
                import shutil
                shutil.rmtree(review_dir)
            removed += 1
        else:
            retained.append(record)
    if removed:
        index["attempts"] = retained
        changed = True
    if changed:
        publisher.atomic_write(root / INDEX_PATH, json.dumps(index, ensure_ascii=False, indent=2) + "\n")
    return changed


def commit_checkpoint_with_retry(root: Path, known_attempts: list[tuple[int, int, str]]) -> str:
    for retry in range(1, MAX_PUSH_RETRIES + 1):
        git(root, "fetch", "origin", "gpt", "--depth=1")
        git(root, "reset", "--hard", "FETCH_HEAD")
        changed = checkpoint_and_prune(root, known_attempts, datetime.now(timezone.utc))
        if not changed:
            return "unchanged"
        git(root, "config", "user.name", "github-actions[bot]")
        git(root, "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
        git(root, "add", "--", INDEX_PATH.as_posix())
        git(root, "add", "-u", "--", REVIEW_ROOT.as_posix())
        commit = git(root, "commit", "-m", "Reconcile task validation checkpoint", check=False)
        if commit.returncode != 0:
            if "nothing to commit" in commit.stdout.lower():
                return "unchanged"
            raise RecoveryError(f"Cannot commit recovery checkpoint: {commit.stderr[-2000:]}")
        push = git(root, "push", "origin", "HEAD:refs/heads/gpt", check=False)
        if push.returncode == 0:
            return "updated"
        if "non-fast-forward" not in push.stderr.lower() and "[rejected]" not in push.stderr.lower():
            raise RecoveryError(f"Recovery checkpoint push failed: {push.stderr[-2000:]}")
    raise RecoveryError(f"Recovery checkpoint push retries exhausted after {MAX_PUSH_RETRIES} attempts")


def run_recovery(root: Path, repository: str, api: GitHubAPI) -> dict[str, Any]:
    policy = json.loads((root / POLICY_PATH).read_text(encoding="utf-8"))
    dispatcher = policy.get("coordinator", {}).get("dispatcher_workflow")
    if not isinstance(dispatcher, str):
        raise RecoveryError("Policy does not identify the dispatcher workflow")
    runs = list_runs(api, repository, dispatcher)
    known: list[tuple[int, int, str]] = []
    published = 0
    ignored = 0
    pending = 0

    for run in sorted(runs, key=lambda item: item.get("id", 0)):
        run_id = run.get("id")
        latest_attempt = run.get("run_attempt", 1)
        if not isinstance(run_id, int) or not isinstance(latest_attempt, int):
            continue
        for attempt_number in range(1, latest_attempt + 1):
            index = current_index(root)
            if record_exists(index, run_id, attempt_number):
                record = next(
                    item for item in index["attempts"]
                    if item["coordinator_run_id"] == run_id and item["attempt"] == attempt_number
                )
                state = "completed" if record["recovery"]["reconciled_at"] is not None else "unresolved"
                known.append((run_id, attempt_number, state))
                continue
            state, key = process_attempt(root, api, repository, run, attempt_number)
            if state == "ignored":
                ignored += 1
                continue
            if state == "pending":
                pending += 1
                known.append((key[0], key[1], "pending"))
                continue
            published += 1
            index = current_index(root)
            record = next(
                (
                    item for item in index["attempts"]
                    if item["coordinator_run_id"] == run_id and item["attempt"] == attempt_number
                ),
                None,
            )
            state_value = "completed" if record and record["recovery"]["reconciled_at"] is not None else "unresolved"
            known.append((run_id, attempt_number, state_value))

    checkpoint_result = commit_checkpoint_with_retry(root, known)
    return {
        "runs_seen": len(runs),
        "attempts_published_or_present": published,
        "ignored_dispatches": ignored,
        "pending_attempts": pending,
        "checkpoint": checkpoint_result,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--repository", default=os.environ.get("GITHUB_REPOSITORY", ""))
    parser.add_argument("--api-url", default=os.environ.get("GITHUB_API_URL", "https://api.github.com"))
    args = parser.parse_args()
    try:
        root = args.root.resolve(strict=True)
        token = os.environ.get("GITHUB_TOKEN", "")
        api = GitHubAPI(token, args.api_url)
        result = run_recovery(root, args.repository, api)
        print(json.dumps({"outcome": "success", **result}))
        return 0
    except (RecoveryError, publisher.PublisherError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(json.dumps({"outcome": "infrastructure_failure", "error": str(exc)}))
        return 1


if __name__ == "__main__":
    sys.exit(main())
