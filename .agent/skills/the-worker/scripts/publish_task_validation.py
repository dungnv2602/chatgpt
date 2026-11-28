"""Atomically publish ADR-0008 attempt status and review records."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any

from build_task_validation_contract import TaskContractError, extract_task_id


OUTCOMES = {
    "success",
    "check_failure",
    "coverage_failure",
    "infrastructure_failure",
    "capture_failure",
    "cancelled",
    "superseded",
}
REVIEW_TEMPLATE = Path(".agent/skills/the-worker/assets/task-validation/task-validation-review-template.md")
INDEX_PATH = Path("workspace/task-validation/status-index.json")
REVIEW_ROOT = Path("workspace/task-validation/reviews")
MAX_PUSH_ATTEMPTS = 5


class PublisherError(ValueError):
    """Raised when an attempt cannot be safely published."""


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise PublisherError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def run_git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
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
        raise PublisherError(f"git operation timed out: {' '.join(args[:2])}") from exc
    if check and result.returncode != 0:
        raise PublisherError(f"git {' '.join(args[:2])} failed: {result.stderr[-2000:]}")
    return result


def ensure_source_commit(root: Path, source_sha: str) -> None:
    probe = run_git(root, "cat-file", "-e", f"{source_sha}^{{commit}}", check=False)
    if probe.returncode == 0:
        return
    run_git(root, "fetch", "origin", source_sha, "--depth=1")
    run_git(root, "cat-file", "-e", f"{source_sha}^{{commit}}")


def source_task_id(root: Path, source_sha: str) -> str | None:
    message = run_git(root, "show", "-s", "--format=%B", source_sha).stdout
    try:
        task_id = extract_task_id(message)
    except TaskContractError:
        return None
    paths = run_git(root, "ls-tree", "-r", "--name-only", source_sha, "workspace/tasks").stdout.splitlines()
    matches = []
    for relative in paths:
        if not (relative.endswith("/task.md") or "/subtasks/" in relative and relative.endswith(".md")):
            continue
        if not relative.startswith("workspace/tasks/"):
            continue
        record = run_git(root, "show", f"{source_sha}:{relative}").stdout
        if re.search(rf"^- \*\*ID:\*\* {re.escape(task_id)}$", record, re.MULTILINE):
            matches.append(relative)
    return task_id if len(matches) == 1 else None


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise PublisherError(f"Cannot read JSON input {path}: {exc}") from exc


def validate_aggregate(
    aggregate: Any,
    source_sha: str,
    policy_blob_sha: str,
    run_id: int,
    attempt: int,
) -> tuple[str, str | None, str]:
    if not isinstance(aggregate, dict):
        raise PublisherError("Aggregate must be a JSON object")
    if not isinstance(aggregate.get("source_sha"), str) or aggregate.get("source_sha") != source_sha:
        raise PublisherError("Aggregate source SHA does not match the source event")
    if not isinstance(aggregate.get("policy_blob_sha"), str) or aggregate.get("policy_blob_sha") != policy_blob_sha:
        raise PublisherError("Aggregate policy blob SHA does not match the protected policy")
    aggregate_run_id = aggregate.get("coordinator_run_id")
    aggregate_attempt = aggregate.get("attempt")
    if (
        not isinstance(aggregate_run_id, int) or isinstance(aggregate_run_id, bool)
        or not isinstance(aggregate_attempt, int) or isinstance(aggregate_attempt, bool)
        or aggregate_run_id != run_id or aggregate_attempt != attempt
    ):
        raise PublisherError("Aggregate run ID or attempt does not match the coordinator event")
    outcome = aggregate.get("outcome")
    if not isinstance(outcome, str) or outcome not in OUTCOMES:
        raise PublisherError("Aggregate has an unknown terminal outcome")
    check_set_id = aggregate.get("check_set_id")
    if check_set_id is not None and (
        not isinstance(check_set_id, str) or not re.fullmatch(r"[0-9a-f]{64}", check_set_id)
    ):
        raise PublisherError("Aggregate check-set identity is malformed")
    if check_set_id is None and outcome not in {
        "capture_failure", "infrastructure_failure", "cancelled", "superseded"
    }:
        raise PublisherError("A terminal result requires a check-set identity")
    completed_at = aggregate.get("completed_at")
    if not isinstance(completed_at, str):
        raise PublisherError("Aggregate completion timestamp is missing")
    try:
        parsed_completed_at = datetime.fromisoformat(completed_at.replace("Z", "+00:00"))
        if parsed_completed_at.tzinfo is None:
            raise ValueError("timezone is required")
    except ValueError as exc:
        raise PublisherError("Aggregate completion timestamp is invalid") from exc
    statuses = aggregate.get("statuses")
    expected_checks = aggregate.get("expected_checks")
    if outcome == "success" and (
        not isinstance(expected_checks, list)
        or not expected_checks
        or not all(isinstance(item, str) for item in expected_checks)
        or not isinstance(statuses, dict)
        or set(statuses) != set(expected_checks)
        or any(value != "success" for value in statuses.values())
    ):
        raise PublisherError("Successful aggregate does not contain a complete all-success check set")
    return outcome, check_set_id, completed_at


def validate_index(index: Any) -> dict[str, Any]:
    if not isinstance(index, dict) or set(index) != {"schema_version", "closed_through", "attempts"}:
        raise PublisherError("Status index has an invalid top-level shape")
    if index.get("schema_version") != 1:
        raise PublisherError("Unsupported status-index schema version")
    checkpoint = index.get("closed_through")
    if (
        not isinstance(checkpoint, dict)
        or set(checkpoint) != {"run_id", "attempt"}
        or not isinstance(checkpoint.get("run_id"), int)
        or isinstance(checkpoint.get("run_id"), bool)
        or checkpoint["run_id"] < 0
        or not isinstance(checkpoint.get("attempt"), int)
        or isinstance(checkpoint.get("attempt"), bool)
        or checkpoint["attempt"] < 0
    ):
        raise PublisherError("Status-index checkpoint is malformed")
    attempts = index.get("attempts")
    if not isinstance(attempts, list):
        raise PublisherError("Status-index attempts must be an array")
    seen: set[tuple[int, int]] = set()
    previous = (0, 0)
    required = {
        "source_task_id",
        "source_sha",
        "coordinator_run_id",
        "attempt",
        "check_set_id",
        "policy_revision",
        "completed_at",
        "outcome",
        "actions_url",
        "recovery",
    }
    for record in attempts:
        if not isinstance(record, dict) or set(record) != required:
            raise PublisherError("Status-index attempt record has an invalid shape")
        run_id = record.get("coordinator_run_id")
        attempt = record.get("attempt")
        if (
            not isinstance(run_id, int) or isinstance(run_id, bool) or run_id < 1
            or not isinstance(attempt, int) or isinstance(attempt, bool) or attempt < 1
        ):
            raise PublisherError("Status-index attempt key is invalid")
        key = (run_id, attempt)
        if key in seen or key < previous:
            raise PublisherError("Status-index attempts must be unique and sorted")
        seen.add(key)
        previous = key
        source_task = record.get("source_task_id")
        if source_task is not None and (
            not isinstance(source_task, str)
            or not re.fullmatch(r"[0-9]{8}-[0-9]{6}(?:-[0-9]{2,})?", source_task)
        ):
            raise PublisherError("Status-index source Task-ID is malformed")
        source_value = record.get("source_sha")
        if not isinstance(source_value, str) or not re.fullmatch(r"[0-9a-f]{40}", source_value):
            raise PublisherError("Status-index source SHA is malformed")
        policy_value = record.get("policy_revision")
        if not isinstance(policy_value, str) or not re.fullmatch(r"[0-9a-f]{40}", policy_value):
            raise PublisherError("Status-index policy revision is malformed")
        check_set_id = record.get("check_set_id")
        if check_set_id is not None and (
            not isinstance(check_set_id, str) or not re.fullmatch(r"[0-9a-f]{64}", check_set_id)
        ):
            raise PublisherError("Status-index check-set identity is malformed")
        if not isinstance(record.get("outcome"), str) or record["outcome"] not in OUTCOMES:
            raise PublisherError("Status-index outcome is invalid")
        if check_set_id is None and record["outcome"] not in {
            "capture_failure", "infrastructure_failure", "cancelled", "superseded"
        }:
            raise PublisherError("Status-index outcome requires a check-set identity")
        try:
            completed_at = record.get("completed_at")
            if not isinstance(completed_at, str):
                raise ValueError("completion timestamp must be a string")
            completed = datetime.fromisoformat(completed_at.replace("Z", "+00:00"))
            if completed.tzinfo is None:
                raise ValueError("timezone is required")
            actions_url = record.get("actions_url", "")
            if actions_url != f"https://github.com/dungnv2602/chatgpt/actions/runs/{run_id}":
                raise ValueError("Actions URL does not match run ID")
        except ValueError as exc:
            raise PublisherError("Status-index completion metadata is invalid") from exc
        recovery = record.get("recovery")
        if (
            not isinstance(recovery, dict)
            or set(recovery) != {"reconciled_at", "retry_count", "last_retry_at"}
            or not isinstance(recovery.get("retry_count"), int)
            or isinstance(recovery.get("retry_count"), bool)
            or recovery["retry_count"] < 0
        ):
            raise PublisherError("Status-index recovery metadata is malformed")
        if record["outcome"] in {"cancelled", "superseded"} and recovery["reconciled_at"] is None:
            raise PublisherError("Cancelled and superseded attempts must be reconciled immediately")
        for field in ("reconciled_at", "last_retry_at"):
            value = recovery[field]
            if value is not None:
                try:
                    parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
                    if parsed.tzinfo is None:
                        raise ValueError("timezone is required")
                except ValueError as exc:
                    raise PublisherError("Status-index recovery timestamp is malformed") from exc
        if key <= (checkpoint["run_id"], checkpoint["attempt"]) and recovery["reconciled_at"] is None:
            raise PublisherError("Checkpoint cannot pass an unresolved attempt")
    return index


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def record_for(
    source_task: str | None,
    source_sha: str,
    policy_blob_sha: str,
    run_id: int,
    attempt: int,
    actions_url: str,
    completed_at: str,
    outcome: str,
    check_set_id: str | None,
) -> dict[str, Any]:
    ignored = outcome in {"cancelled", "superseded"}
    return {
        "source_task_id": source_task,
        "source_sha": source_sha,
        "coordinator_run_id": run_id,
        "attempt": attempt,
        "check_set_id": check_set_id,
        "policy_revision": policy_blob_sha,
        "completed_at": completed_at,
        "outcome": outcome,
        "actions_url": actions_url,
        "recovery": {
            "reconciled_at": completed_at if ignored else None,
            "retry_count": 0,
            "last_retry_at": None,
        },
    }


def render_review(record: dict[str, Any], template: str) -> str:
    values = {
        "source_task_id": record["source_task_id"] or "Unattributed",
        "source_sha": record["source_sha"],
        "coordinator_run_id": str(record["coordinator_run_id"]),
        "attempt": str(record["attempt"]),
        "check_set_id": record["check_set_id"] or "Unavailable",
        "policy_revision": record["policy_revision"],
        "completed_at": record["completed_at"],
        "outcome": record["outcome"],
        "actions_url": record["actions_url"],
    }
    for key, value in values.items():
        template = template.replace("{{" + key + "}}", value)
    if re.search(r"\{\{[a-z_]+\}\}", template):
        raise PublisherError("Review template contains unresolved placeholders")
    return template


def publish_attempt(
    root: Path,
    aggregate: dict[str, Any],
    source_sha: str,
    policy_blob_sha: str,
    run_id: int,
    attempt: int,
    actions_url: str,
    completed_at: str,
) -> bool:
    outcome, check_set_id, aggregate_completed_at = validate_aggregate(aggregate, source_sha, policy_blob_sha, run_id, attempt)
    if completed_at != aggregate_completed_at:
        raise PublisherError("Publisher timestamp does not match the aggregate timestamp")
    task_id = source_task_id(root, source_sha)
    record = record_for(
        task_id, source_sha, policy_blob_sha, run_id, attempt,
        actions_url, completed_at, outcome, check_set_id,
    )

    index_file = root / INDEX_PATH
    if not index_file.exists():
        raise PublisherError("Canonical task-validation status index is missing")
    index = validate_index(read_json(index_file))

    checkpoint = index["closed_through"]
    if (run_id, attempt) <= (checkpoint["run_id"], checkpoint["attempt"]):
        return False

    existing = next(
        (
            item for item in index["attempts"]
            if item["coordinator_run_id"] == run_id and item["attempt"] == attempt
        ),
        None,
    )
    review_dir = root / REVIEW_ROOT / f"{run_id}-{attempt}"
    review_file = review_dir / "review.md"
    ignored = outcome in {"cancelled", "superseded"}

    if ignored:
        review_content = None
    else:
        template = (root / REVIEW_TEMPLATE).read_text(encoding="utf-8")
        review_content = render_review(record, template)

    if existing is not None:
        comparable = {key: value for key, value in existing.items() if key != "recovery"}
        candidate = {key: value for key, value in record.items() if key != "recovery"}
        if comparable != candidate:
            raise PublisherError(f"Conflicting duplicate publication for {run_id}/{attempt}")
        if ignored:
            if review_dir.exists():
                raise PublisherError("Cancelled or superseded attempt unexpectedly has a review folder")
            return False
        if existing["recovery"]["reconciled_at"] is not None:
            return False
        if review_file.exists():
            if review_file.read_text(encoding="utf-8") != review_content:
                raise PublisherError("Existing review folder conflicts with the attempt record")
            return False
        atomic_write(review_file, review_content or "")
        return True

    if review_dir.exists():
        if ignored or not review_file.exists() or review_file.read_text(encoding="utf-8") != review_content:
            raise PublisherError("Orphaned review folder conflicts with this attempt")
    elif not ignored:
        atomic_write(review_file, review_content or "")

    index["attempts"].append(record)
    index["attempts"].sort(key=lambda item: (item["coordinator_run_id"], item["attempt"]))
    atomic_write(index_file, json.dumps(index, ensure_ascii=False, indent=2) + "\n")
    return True


def publish_with_retry(
    root: Path,
    aggregate_path: Path,
    source_sha: str,
    policy_blob_sha: str,
    run_id: int,
    attempt: int,
    actions_url: str,
    branch: str,
) -> str:
    if not re.fullmatch(r"[0-9a-f]{40}", source_sha):
        raise PublisherError("source_sha must be a full lowercase 40-character SHA")
    if not re.fullmatch(r"[0-9a-f]{40}", policy_blob_sha):
        raise PublisherError("policy_blob_sha must be a full lowercase 40-character SHA")
    if branch != "gpt":
        raise PublisherError("Publisher may write only to the authorized gpt branch")
    if not isinstance(run_id, int) or run_id < 1 or not isinstance(attempt, int) or attempt < 1:
        raise PublisherError("Coordinator run ID and attempt must be positive integers")
    expected_url = f"https://github.com/dungnv2602/chatgpt/actions/runs/{run_id}"
    if actions_url != expected_url:
        raise PublisherError("Actions URL does not match the repository and run ID")

    aggregate = read_json(aggregate_path)
    outcome, check_set_id, completed_at = validate_aggregate(
        aggregate, source_sha, policy_blob_sha, run_id, attempt
    )
    ensure_source_commit(root, source_sha)
    policy_content = run_git(
        root,
        "show",
        f"{source_sha}:.agent/skills/the-worker/assets/task-validation/task-validation-policy.json",
    ).stdout.encode("utf-8")
    actual_policy_blob_sha = hashlib.sha1(
        f"blob {len(policy_content)}\0".encode("ascii") + policy_content
    ).hexdigest()
    if actual_policy_blob_sha != policy_blob_sha:
        raise PublisherError("Source commit policy blob does not match the aggregate policy revision")

    for push_attempt in range(1, MAX_PUSH_ATTEMPTS + 1):
        run_git(root, "fetch", "origin", branch, "--depth=1")
        run_git(root, "reset", "--hard", "FETCH_HEAD")
        changed = publish_attempt(
            root, aggregate, source_sha, policy_blob_sha, run_id, attempt, actions_url, completed_at
        )
        if not changed:
            return "already_published"

        run_git(root, "config", "user.name", "github-actions[bot]")
        run_git(root, "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
        run_git(root, "add", "--", INDEX_PATH.as_posix())
        review_path = REVIEW_ROOT / f"{run_id}-{attempt}"
        if (root / review_path).exists():
            run_git(root, "add", "--", review_path.as_posix())
        commit = run_git(
            root,
            "commit",
            "-m",
            f"Publish task validation attempt {run_id}/{attempt}",
            check=False,
        )
        if commit.returncode != 0:
            if "nothing to commit" in commit.stdout.lower():
                return "already_published"
            raise PublisherError(f"Cannot create publisher commit: {commit.stderr[-2000:]}")

        push = run_git(root, "push", "origin", f"HEAD:refs/heads/{branch}", check=False)
        if push.returncode == 0:
            return "published"
        if "non-fast-forward" not in push.stderr.lower() and "[rejected]" not in push.stderr.lower():
            raise PublisherError(f"Publisher push failed: {push.stderr[-2000:]}")
    raise PublisherError(f"Concurrent publisher retries exhausted after {MAX_PUSH_ATTEMPTS} attempts")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--aggregate-json", type=Path, required=True)
    parser.add_argument("--source-sha", required=True)
    parser.add_argument("--policy-blob-sha", required=True)
    parser.add_argument("--coordinator-run-id", type=int, required=True)
    parser.add_argument("--attempt", type=int, required=True)
    parser.add_argument("--actions-url", required=True)
    parser.add_argument("--branch", default="gpt")
    args = parser.parse_args()

    try:
        root = args.root.resolve(strict=True)
        result = publish_with_retry(
            root,
            args.aggregate_json.resolve(strict=True),
            args.source_sha,
            args.policy_blob_sha,
            args.coordinator_run_id,
            args.attempt,
            args.actions_url,
            args.branch,
        )
        print(json.dumps({"outcome": "success", "publication": result}))
        return 0
    except (PublisherError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(json.dumps({"outcome": "capture_failure", "error": str(exc)}))
        return 1


if __name__ == "__main__":
    sys.exit(main())
