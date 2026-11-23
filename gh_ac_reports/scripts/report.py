#!/usr/bin/env python3
"""Collect and generate detailed GitHub Actions diagnostic evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "assets" / "report-schema.json"
TEMPLATE_PATH = ROOT / "assets" / "report-template.md"
SCHEMA_VERSION = "1.0.0"
REPORT_WORKFLOW = ".github/workflows/gh-actions-diagnostics.yml"
REPORT_JOB = "Capture GH Actions diagnostics"
BOOTSTRAP_WATERMARK = "2026-11-23T05:49:04Z"
MAX_LOG_BYTES = 1_000_000
SECRET_PATTERNS = [
    (re.compile(r"(?i)(authorization\s*:\s*bearer\s+)[^\s]+"), r"\1[REDACTED]"),
    (re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"), "[REDACTED_TOKEN]"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "[REDACTED_AWS_KEY]"),
    (re.compile(r"(?i)(\b(?:password|passwd|secret|token)\b\s*[=:]\s*)[^\s,;]+"), r"\1[REDACTED]"),
]
MARKERS = re.compile(r"::error::|\b(?:ERROR|FATAL|FAILED)\b|Traceback|Process completed with exit code [1-9]", re.I)
FAILURES = {"failure", "timed_out", "action_required", "cancelled"}
CATEGORY_ORDER = [
    "workflow_startup_or_configuration_failure", "runner_initialization_failure",
    "permission_or_authentication", "publication_or_push", "artifact_transfer",
    "external_service_or_network", "checkout_or_action_download",
    "dependency_installation", "validation_or_test", "build_or_processing",
    "workflow_level_failure_unattributed", "step_or_job_failure", "timeout",
    "action_required", "cancelled",
]


def utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def timestamp(value):
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).timestamp()
    except (TypeError, ValueError):
        return 0.0


def redact(value):
    result = str(value or "")
    for pattern, replacement in SECRET_PATTERNS:
        result = pattern.sub(replacement, result)
    return result


def markers(value):
    output = []
    for line in str(value or "").splitlines():
        if MARKERS.search(line):
            item = redact(line.strip())[:500]
            if item and item not in output:
                output.append(item)
        if len(output) == 20:
            break
    return output



def validate_schema(value, schema, path="$"):
    expected = schema.get("type")
    if expected:
        allowed = expected if isinstance(expected, list) else [expected]
        checks = {
            "object": lambda item: isinstance(item, dict),
            "array": lambda item: isinstance(item, list),
            "string": lambda item: isinstance(item, str),
            "integer": lambda item: isinstance(item, int) and not isinstance(item, bool),
            "number": lambda item: isinstance(item, (int, float)) and not isinstance(item, bool),
            "null": lambda item: item is None,
        }
        if not any(checks[name](value) for name in allowed):
            raise ValueError(path + " has an invalid type")
    if "const" in schema and value != schema["const"]:
        raise ValueError(path + " must equal " + repr(schema["const"]))
    if "enum" in schema and value not in schema["enum"]:
        raise ValueError(path + " has an unsupported value")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                raise ValueError(path + " is missing " + key)
        properties = schema.get("properties", {})
        for key, item in value.items():
            if key in properties:
                validate_schema(item, properties[key], path + "." + key)
            elif schema.get("additionalProperties") is False:
                raise ValueError(path + "." + key + " is not allowed")
    if isinstance(value, list) and "items" in schema:
        for position, item in enumerate(value):
            validate_schema(item, schema["items"], path + "[" + str(position) + "]")


def api_get(repo, path, errors, source):
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        errors.append({"source": source, "message": "GitHub token is unavailable."})
        return None
    base = os.environ.get("GITHUB_API_URL", "https://api.github.com").rstrip("/")
    url = path if path.startswith("https://") else base + path
    request = Request(url, headers={
        "Authorization": "Bearer " + token,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "gh-ac-report-collector",
    })
    try:
        with urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        body = redact(exc.read().decode("utf-8", errors="replace"))
        errors.append({"source": source, "http_status": exc.code, "message": body[:1000]})
    except (URLError, TimeoutError, ValueError) as exc:
        errors.append({"source": source, "message": redact(exc)[:1000]})
    return None


def pages(repo, path, key, errors, source):
    output = []
    for page in range(1, 51):
        separator = "&" if "?" in path else "?"
        payload = api_get(repo, path + separator + urlencode({"per_page": 100, "page": page}), errors, source)
        if not isinstance(payload, dict) or not isinstance(payload.get(key), list):
            if isinstance(payload, dict):
                errors.append({"source": source, "message": "Expected array " + key + " was absent."})
            break
        batch = payload[key]
        output.extend(batch)
        if len(batch) < 100:
            break
    return output


def capture_log(repo, run_id, job_id):
    env = dict(os.environ)
    env["GH_TOKEN"] = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN", "")
    env["GH_REPO"] = repo
    env["CLICOLOR"] = "0"
    command = ["gh", "run", "view", str(run_id), "--job", str(job_id), "--log", "--repo", repo]
    try:
        result = subprocess.run(command, capture_output=True, text=True, env=env, timeout=120)
        value = redact(result.stdout + (("\n" + result.stderr) if result.stderr else ""))
        raw = value.encode("utf-8", errors="replace")
        truncated = len(raw) > MAX_LOG_BYTES
        if truncated:
            raw = raw[: MAX_LOG_BYTES * 3 // 4] + b"\n...[MIDDLE SECTION OMITTED]...\n" + raw[-MAX_LOG_BYTES // 4:]
            value = raw.decode("utf-8", errors="replace")
        return value, {
            "available": result.returncode == 0,
            "truncated": truncated,
            "bytes": len(value.encode("utf-8")),
            "error": None if result.returncode == 0 else redact(result.stderr or "gh run view failed.")[:1000],
        }
    except (OSError, subprocess.TimeoutExpired) as exc:
        return "", {"available": False, "truncated": False, "bytes": 0, "error": redact(exc)[:1000]}


def classify_text(text, job_name="", step_name=""):
    value = (job_name + " " + step_name + " " + text).lower()
    rules = [
        ("permission_or_authentication", ("resource not accessible by integration", "permission denied", "insufficient permission", "http 401", "http 403", "unauthorized", "forbidden")),
        ("publication_or_push", ("non-fast-forward", "remote rejected", "protected branch", "git push", "could not publish", "push failed")),
        ("artifact_transfer", ("upload-artifact", "download-artifact", "artifact upload", "artifact download")),
        ("checkout_or_action_download", ("checkout", "repository not found", "failed to download action", "action download")),
        ("runner_initialization_failure", ("no space left", "runner lost", "failed to start", "runner initialization", "job was not acquired")),
        ("external_service_or_network", ("smtp", "temporary failure in name resolution", "connection timed out", "connection refused", "http 502", "http 503", "service unavailable")),
        ("dependency_installation", ("pip install", "npm install", "apt-get", "unable to locate package", "setup python", "setup node")),
        ("validation_or_test", ("test", "lint", "validate", "verify", "assertionerror", "tests failed")),
        ("build_or_processing", ("build", "compile", "process", "convert", "generate")),
    ]
    for category, terms in rules:
        if any(term in value for term in terms):
            return category, "medium" if category not in ("permission_or_authentication", "publication_or_push", "artifact_transfer") else "high"
    return "step_or_job_failure", "low"


def normalize_step(step):
    return {key: step.get(key) for key in ("number", "name", "status", "conclusion", "started_at", "completed_at")}


def classify(run, jobs, logs):
    issues = []
    categories = set()
    for job in jobs:
        text = logs.get(str(job["id"]), "")
        failures = [step for step in job["steps"] if step.get("conclusion") in FAILURES]
        for step in failures:
            conclusion = step.get("conclusion")
            if conclusion == "cancelled":
                category, confidence = "cancelled", "high"
            elif conclusion == "timed_out":
                category, confidence = "timeout", "high"
            elif conclusion == "action_required":
                category, confidence = "action_required", "high"
            else:
                category, confidence = classify_text(text, job["name"], str(step.get("name") or ""))
            issues.append({
                "category": category, "job_id": job["id"], "job_name": job["name"],
                "step_number": step.get("number"), "step_name": step.get("name"),
                "blocking": job.get("conclusion") not in (None, "success", "neutral", "skipped"),
                "confidence": confidence,
                "message": next(iter(markers(text)), "Step conclusion: " + str(conclusion)),
            })
            categories.add(category)
        if job.get("conclusion") in FAILURES and not failures:
            conclusion = job.get("conclusion")
            if conclusion == "cancelled":
                category, confidence = "cancelled", "high"
            elif conclusion == "timed_out":
                category, confidence = "timeout", "high"
            elif conclusion == "action_required":
                category, confidence = "action_required", "high"
            else:
                category, confidence = classify_text(text, job["name"], "")
            issues.append({
                "category": category, "job_id": job["id"], "job_name": job["name"],
                "step_number": None, "step_name": None, "blocking": True,
                "confidence": confidence,
                "message": next(iter(markers(text)), "Job conclusion: " + str(conclusion)),
            })
            categories.add(category)

    conclusion = run.get("conclusion")
    if conclusion == "failure" and not issues:
        category = "workflow_startup_or_configuration_failure" if not jobs else "workflow_level_failure_unattributed"
        issues.append({
            "category": category, "job_id": None, "job_name": None,
            "step_number": None, "step_name": None, "blocking": True,
            "confidence": "low",
            "message": "GitHub reported a failed run, but no failed job or step was available.",
        })
        categories.add(category)
    if conclusion in ("cancelled", "timed_out", "action_required"):
        categories.add({"cancelled":"cancelled","timed_out":"timeout","action_required":"action_required"}[conclusion])

    if conclusion == "success":
        state = "success_with_non_blocking_step_failures" if issues else "success"
    elif conclusion in ("failure", "cancelled", "timed_out", "action_required", "skipped", "neutral"):
        state = conclusion
    elif run.get("status") in ("queued", "waiting", "pending"):
        state = "queued"
    elif run.get("status") == "in_progress":
        state = "in_progress"
    else:
        state = "unknown"

    projected = None
    if conclusion is None and jobs and all(job.get("status") == "completed" for job in jobs):
        outcomes = [job.get("conclusion") for job in jobs]
        if any(item in ("failure", "timed_out", "action_required") for item in outcomes):
            projected = "failure"
        elif "cancelled" in outcomes:
            projected = "cancelled"
        elif all(item == "skipped" for item in outcomes):
            projected = "skipped"
        else:
            projected = "success"
    order = {name: index for index, name in enumerate(CATEGORY_ORDER)}
    ordered = sorted(categories, key=lambda name: order.get(name, 999))
    return {
        "state": state, "observed_conclusion": conclusion, "projected_conclusion": projected,
        "primary_category": ordered[0] if ordered else None, "categories": ordered, "issues": issues,
    }


def fetch_evidence(repo, run_id, stage):
    errors = []
    run = api_get(repo, "/repos/" + repo + "/actions/runs/" + str(run_id), errors, "run_metadata")
    if not isinstance(run, dict):
        raise RuntimeError("Cannot retrieve workflow run " + str(run_id))
    jobs_path = "/repos/" + repo + "/actions/runs/" + str(run_id) + "/jobs?filter=latest"
    raw_jobs = pages(repo, jobs_path, "jobs", errors, "jobs")
    jobs_ok = not any(item.get("source") == "jobs" for item in errors)
    artifacts = pages(repo, "/repos/" + repo + "/actions/runs/" + str(run_id) + "/artifacts", "artifacts", errors, "artifacts")
    check_runs, annotations, logs, log_info = [], [], {}, {}

    reporter_job = None
    normalized_jobs = []
    for raw in raw_jobs:
        if stage == "pre_finalizer" and raw.get("name") == REPORT_JOB:
            reporter_job = {"id": str(raw.get("id")), "name": raw.get("name"), "status": raw.get("status"), "conclusion": raw.get("conclusion")}
            continue
        job_id = str(raw.get("id"))
        check_url = raw.get("check_run_url")
        match = re.search(r"/check-runs/(\d+)", check_url or "")
        if match:
            check_id = match.group(1)
            check = api_get(repo, "/repos/" + repo + "/check-runs/" + check_id, errors, "check_run")
            if isinstance(check, dict):
                check_runs.append({
                    "id": str(check.get("id")), "name": check.get("name"), "status": check.get("status"),
                    "conclusion": check.get("conclusion"), "started_at": check.get("started_at"),
                    "completed_at": check.get("completed_at"), "details_url": check.get("details_url"),
                    "app": (check.get("app") or {}).get("name"),
                    "annotations_count": (check.get("output") or {}).get("annotations_count", 0),
                })
                if int((check.get("output") or {}).get("annotations_count") or 0):
                    items = pages(repo, "/repos/" + repo + "/check-runs/" + check_id + "/annotations", "annotations", errors, "annotations")
                    for item in items:
                        annotations.append({
                            "check_run_id": check_id, "job_id": job_id, "path": item.get("path"),
                            "start_line": item.get("start_line"), "end_line": item.get("end_line"),
                            "level": item.get("annotation_level"), "title": redact(item.get("title")),
                            "message": redact(item.get("message")), "raw_details": redact(item.get("raw_details")),
                        })
        info = {"available": False, "truncated": False, "bytes": 0, "error": None}
        if raw.get("status") == "completed" and raw.get("conclusion") != "skipped":
            log, info = capture_log(repo, run_id, job_id)
            if info["available"] or log:
                logs[job_id] = log
            if info["error"]:
                errors.append({"source": "job_log", "job_id": job_id, "message": info["error"]})
        normalized_jobs.append({
            "id": job_id, "name": raw.get("name"), "status": raw.get("status"),
            "conclusion": raw.get("conclusion"), "started_at": raw.get("started_at"),
            "completed_at": raw.get("completed_at"), "runner_name": raw.get("runner_name"),
            "runner_id": raw.get("runner_id"), "runner_group_name": raw.get("runner_group_name"),
            "runner_group_id": raw.get("runner_group_id"),
            "steps": [normalize_step(item) for item in raw.get("steps", [])],
            "log_capture": {
                "available": info["available"], "truncated": info["truncated"], "bytes": info["bytes"],
                "path": "logs/job-" + job_id + ".log" if job_id in logs else None,
                "error": info["error"], "marker_lines": markers(logs.get(job_id, "")),
            },
        })
    if not jobs_ok:
        errors.append({"source": "jobs", "message": "The jobs endpoint was not available."})

    source_run = {
        "id": str(run.get("id")), "number": int(run.get("run_number") or 0),
        "attempt": int(run.get("run_attempt") or 1), "workflow_id": int(run.get("workflow_id") or 0),
        "workflow_name": run.get("name") or "Unknown", "workflow_path": run.get("path") or "Unknown",
        "run_url": run.get("html_url") or "", "event": run.get("event") or "Unknown",
        "branch": run.get("head_branch"), "head_sha": run.get("head_sha") or "",
        "status": run.get("status") or "unknown", "conclusion": run.get("conclusion"),
        "created_at": run.get("created_at"), "run_started_at": run.get("run_started_at"),
        "updated_at": run.get("updated_at"), "actor": (run.get("actor") or {}).get("login"),
        "triggering_actor": (run.get("triggering_actor") or {}).get("login"),
        "head_commit_message": (run.get("head_commit") or {}).get("message"),
    }
    report = {
        "schema_version": SCHEMA_VERSION,
        "source_run": source_run,
        "capture": {
            "stage": stage, "captured_at_utc": utc_now(),
            "completeness": "Incomplete" if errors else "Complete", "reporter_job": reporter_job,
        },
        "classification": classify(run, normalized_jobs, logs),
        "jobs": normalized_jobs, "check_runs": check_runs, "annotations": annotations,
        "artifacts": artifacts, "capture_errors": errors, "history_path": "",
    }
    log_files = {"logs/job-" + job_id + ".log": value for job_id, value in logs.items()}
    return report, log_files


def md(value):
    text = str(value if value is not None else "Not recorded")
    return text.replace("|", "\\|").replace("\r", " ").replace("\n", " ").replace("<", "&lt;").replace(">", "&gt;")


def table(headers, rows):
    if not rows:
        return "No records were captured."
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    lines.extend("| " + " | ".join(md(value) for value in row) + " |" for row in rows)
    return "\n".join(lines)


def render_markdown(report):
    run, capture, classification = report["source_run"], report["capture"], report["classification"]
    identity = table(["Field", "Value"], [
        ["Workflow", run["workflow_name"]], ["Workflow path", run["workflow_path"]],
        ["Run / attempt", run["id"] + " / " + str(run["attempt"])], ["Run number", run["number"]],
        ["Run URL", run["run_url"]], ["Branch", run["branch"] or "Not recorded"],
        ["Commit", run["head_sha"]], ["Event", run["event"]], ["Actor", run["actor"] or "Not recorded"],
        ["Created (UTC)", run["created_at"]], ["Status at capture", run["status"]],
        ["Observed conclusion", run["conclusion"] or "Not yet available"],
        ["Projected conclusion", classification["projected_conclusion"] or "Not calculated"],
        ["Capture stage", capture["stage"]], ["Completeness", capture["completeness"]],
        ["Captured (UTC)", capture["captured_at_utc"]],
    ])
    summary = table(["Measure", "Result"], [
        ["State", classification["state"]], ["Primary category", classification["primary_category"] or "None"],
        ["Jobs", len(report["jobs"])], ["Steps", sum(len(job["steps"]) for job in report["jobs"])],
        ["Issues", len(classification["issues"])], ["Annotations", len(report["annotations"])],
        ["Artifacts", len(report["artifacts"])], ["Capture errors", len(report["capture_errors"])],
    ])
    categories = ", ".join(classification["categories"]) or "No failure category identified."
    if capture["stage"] == "pre_finalizer":
        categories += " The parent run is still in progress. The projected conclusion is provisional."
    jobs = table(["Job ID", "Job", "Status", "Conclusion", "Steps", "Log"], [
        [j["id"], j["name"], j["status"], j["conclusion"], len(j["steps"]), j["log_capture"]["path"]]
        for j in report["jobs"]
    ])
    issues = table(["Category", "Job", "Step", "Name", "Effect", "Confidence", "Evidence"], [
        [i["category"], i["job_id"] or "Run", i["step_number"] or "—",
         i["step_name"] or i["job_name"] or "Workflow", "Blocking" if i["blocking"] else "Non-blocking",
         i["confidence"], i["message"]] for i in classification["issues"]
    ])
    annotations = table(["Job", "Level", "Path", "Line", "Title", "Message"], [
        [a.get("job_id"), a.get("level"), a.get("path"), a.get("start_line"), a.get("title"), a.get("message")]
        for a in report["annotations"]
    ])
    artifacts = table(["ID", "Name", "Bytes", "Expired", "Created", "Expires"], [
        [a.get("id"), a.get("name"), a.get("size_in_bytes"), a.get("expired"), a.get("created_at"), a.get("expires_at")]
        for a in report["artifacts"]
    ])
    log_rows = [
        [j["id"], j["name"], j["log_capture"]["path"], j["log_capture"]["bytes"],
         j["log_capture"]["truncated"], ", ".join(j["log_capture"]["marker_lines"])]
        for j in report["jobs"] if j["log_capture"]["path"]
    ]
    logs = table(["Job", "Name", "File", "Bytes", "Truncated", "Markers"], log_rows)
    coverage = table(["Source", "HTTP status", "Limitation"], [
        [e.get("source"), e.get("http_status"), e.get("message")] for e in report["capture_errors"]
    ])
    if not report["capture_errors"]:
        coverage = "All requested evidence endpoints and completed-job log captures returned data."
    else:
        coverage = "One or more evidence sources were unavailable. This report is Incomplete.\n\n" + coverage
    path = run["workflow_path"].lower()
    if "ste-lint-changed" in path:
        lint = "[Changed-document lint report](../../../../lint_reports/on_changed/latest-lint-report.md)"
    elif "ste-lint-full-docs" in path:
        lint = "[Repository-wide lint report](../../../../lint_reports/on_repo/latest-lint-report.md)"
    else:
        lint = "No separate lint report applies to this workflow."
    values = {
        "title": run["workflow_name"] + " — run " + run["id"],
        "identity": identity, "summary": summary, "classification": categories,
        "jobs": jobs, "issues": issues, "annotations": annotations, "artifacts": artifacts,
        "logs": logs, "coverage": coverage, "lint_reference": lint,
    }
    return TEMPLATE_PATH.read_text(encoding="utf-8").format(**values)


def load_index(root):
    path = root / "index.json"
    if path.is_file():
        data = json.loads(path.read_text(encoding="utf-8"))
    else:
        data = {"schema_version": SCHEMA_VERSION, "sweep_watermark_utc": BOOTSTRAP_WATERMARK,
                "pending_run_ids": [], "runs": [], "latest_report": None}
    data.setdefault("pending_run_ids", [])
    data.setdefault("runs", [])
    data.setdefault("latest_report", None)
    return data


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sort_key(item):
    return (timestamp(item.get("created_at")), int(item.get("attempt") or 1),
            2 if item.get("capture_stage") == "post_run" else 1,
            timestamp(item.get("captured_at_utc")))


def index_record(report):
    run, capture = report["source_run"], report["capture"]
    return {
        "workflow_id": run["workflow_id"], "workflow_name": run["workflow_name"],
        "run_id": run["id"], "run_number": run["number"], "attempt": run["attempt"],
        "capture_stage": capture["stage"], "created_at": run["created_at"],
        "captured_at_utc": capture["captured_at_utc"], "source_status": run["status"],
        "source_conclusion": run["conclusion"], "projected_conclusion": report["classification"]["projected_conclusion"],
        "report_status": capture["completeness"], "primary_category": report["classification"]["primary_category"],
        "history_path": report["history_path"], "run_url": run["run_url"],
    }


def update_indexes(root, report):
    record = index_record(report)
    index = load_index(root)
    if not any(item.get("history_path") == record["history_path"] for item in index["runs"]):
        index["runs"].append(record)
    index["runs"].sort(key=sort_key, reverse=True)
    index["runs"] = index["runs"][:1000]
    latest = index["runs"][0] if index["runs"] else None
    old = index.get("latest_report")
    if latest and (old is None or sort_key(latest) > sort_key(old)):
        index["latest_report"] = latest
        source = root / latest["history_path"]
        shutil.copyfile(source / "report.md", root / "latest-gh-ac-report.md")
        shutil.copyfile(source / "report.json", root / "latest-gh-ac-report.json")
    pending = set(str(x) for x in index.get("pending_run_ids", []))
    run_id = report["source_run"]["id"]
    if report["source_run"]["status"] != "completed":
        pending.add(run_id)
    elif report["capture"]["stage"] == "post_run" and report["capture"]["completeness"] == "Complete":
        pending.discard(run_id)
    elif report["capture"]["stage"] == "post_run":
        pending.add(run_id)
    index["pending_run_ids"] = sorted(pending, key=lambda x: int(x), reverse=True)
    save_json(root / "index.json", index)

    wf_root = root / "by_workflow" / str(record["workflow_id"])
    wf_index_path = wf_root / "index.json"
    wf_index = json.loads(wf_index_path.read_text(encoding="utf-8")) if wf_index_path.is_file() else {
        "schema_version": SCHEMA_VERSION, "runs": [], "latest_report": None}
    if not any(item.get("history_path") == record["history_path"] for item in wf_index["runs"]):
        wf_index["runs"].append(record)
    wf_index["runs"].sort(key=sort_key, reverse=True)
    wf_index["runs"] = wf_index["runs"][:500]
    wf_latest = wf_index["runs"][0] if wf_index["runs"] else None
    previous = wf_index.get("latest_report")
    if wf_latest and (previous is None or sort_key(wf_latest) > sort_key(previous)):
        wf_index["latest_report"] = wf_latest
        source = root / wf_latest["history_path"]
        wf_root.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source / "report.md", wf_root / "latest-report.md")
        shutil.copyfile(source / "report.json", wf_root / "latest-report.json")
    save_json(wf_index_path, wf_index)


def write_report(root, report, log_files):
    run = report["source_run"]
    folder = str(run["id"]) + "-attempt-" + str(run["attempt"]) + "-" + report["capture"]["stage"]
    parent = root / "history" / str(run["workflow_id"])
    parent.mkdir(parents=True, exist_ok=True)
    target = parent / folder
    suffix = 2
    while target.exists():
        target = parent / (folder + "-capture-" + str(suffix))
        suffix += 1
    report["history_path"] = "history/" + str(run["workflow_id"]) + "/" + target.name
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validate_schema(report, schema)
    target.mkdir()
    for relative, value in log_files.items():
        path = target / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding="utf-8")
    (target / "report.md").write_text(render_markdown(report), encoding="utf-8")
    (target / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    hashes = {
        path.relative_to(target).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(target.rglob("*")) if path.is_file()
    }
    save_json(target / "integrity.json", {
        "schema_version": SCHEMA_VERSION, "captured_at_utc": report["capture"]["captured_at_utc"],
        "file_count": len(hashes), "files": hashes,
    })
    update_indexes(root, report)
    return target


def capture_one(repo, root, run_id, stage, force=False):
    index = load_index(root)
    metadata_errors = []
    metadata = api_get(repo, "/repos/" + repo + "/actions/runs/" + str(run_id), metadata_errors, "run_metadata")
    if not isinstance(metadata, dict):
        raise RuntimeError("Cannot retrieve workflow run " + str(run_id))
    attempt = int(metadata.get("run_attempt") or 1)
    if not force and any(
        str(item.get("run_id")) == str(run_id)
        and int(item.get("attempt") or 1) == attempt
        and item.get("capture_stage") == stage
        and item.get("report_status") == "Complete"
        for item in index["runs"]
    ):
        return None
    report, logs = fetch_evidence(repo, run_id, stage)
    return write_report(root, report, logs)



def collect_runs_between(repo, start_utc, end_utc, errors, depth=0):
    """Collect every matching run without silently crossing GitHub's 1,000-result search cap."""
    start_value, end_value = timestamp(start_utc), timestamp(end_utc)
    if end_value < start_value:
        return []
    query_range = str(start_utc) + ".." + str(end_utc)
    endpoint = "/repos/" + repo + "/actions/runs?" + urlencode({
        "created": query_range, "per_page": 100, "page": 1,
    })
    first = api_get(repo, endpoint, errors, "run_sweep")
    if not isinstance(first, dict) or not isinstance(first.get("workflow_runs"), list):
        errors.append({"source": "run_sweep", "message": "The run-list endpoint did not return workflow_runs."})
        return []
    output = list(first["workflow_runs"])
    total = int(first.get("total_count") or len(output))
    if len(output) < 100:
        return output
    for page in range(2, 11):
        separator = "&" if "?" in endpoint else "?"
        page_url = endpoint + separator + urlencode({"page": page})
        payload = api_get(repo, page_url, errors, "run_sweep")
        if not isinstance(payload, dict) or not isinstance(payload.get("workflow_runs"), list):
            errors.append({"source": "run_sweep", "message": "A workflow-run page could not be retrieved."})
            return output
        batch = payload["workflow_runs"]
        output.extend(batch)
        if len(batch) < 100:
            break
    unique = {str(item.get("id")): item for item in output if item.get("id") is not None}
    output = list(unique.values())
    if len(output) >= total:
        return output
    if depth >= 24 or end_value - start_value <= 1:
        errors.append({
            "source": "run_sweep",
            "message": "GitHub returned more than 1,000 workflow runs for a narrow time range. The sweep was not advanced to avoid silently missing runs.",
        })
        return output
    midpoint = (start_value + end_value) / 2
    midpoint_text = datetime.fromtimestamp(midpoint, timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    left = collect_runs_between(repo, start_utc, midpoint_text, errors, depth + 1)
    right = collect_runs_between(repo, midpoint_text, end_utc, errors, depth + 1)
    merged = {str(item.get("id")): item for item in left + right if item.get("id") is not None}
    return list(merged.values())


def collect_runs_since(repo, watermark, scan_started, errors):
    start = datetime.fromtimestamp(timestamp(watermark), timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    end = datetime.fromtimestamp(timestamp(scan_started), timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return collect_runs_between(repo, start, end, errors)


def run_sweep(repo, root):
    index = load_index(root)
    started = utc_now()
    watermark = index.get("sweep_watermark_utc") or BOOTSTRAP_WATERMARK
    errors = []
    runs = collect_runs_since(repo, watermark, started, errors)
    if errors:
        raise RuntimeError("Cannot enumerate workflow runs: " + "; ".join(x["message"] for x in errors))
    pending = set(str(x) for x in index.get("pending_run_ids", []))
    candidates = {}
    for run in runs:
        if str(run.get("path") or "").split("@", 1)[0] == REPORT_WORKFLOW:
            continue
        if timestamp(run.get("created_at")) > 0 and timestamp(run.get("created_at")) >= timestamp(watermark):
            candidates[str(run["id"])] = run
    for run_id in pending:
        more = []
        run = api_get(repo, "/repos/" + repo + "/actions/runs/" + run_id, more, "pending_run")
        if isinstance(run, dict):
            candidates[run_id] = run

    new_reports = 0
    for run_id, run in sorted(candidates.items(), key=lambda pair: timestamp(pair[1].get("created_at"))):
        if run.get("status") != "completed":
            pending.add(run_id)
            continue
        try:
            target = capture_one(repo, root, run_id, "post_run")
            if target is not None:
                new_reports += 1
            latest_errors = []
            refreshed = api_get(repo, "/repos/" + repo + "/actions/runs/" + run_id, latest_errors, "run_refresh")
            if refreshed and refreshed.get("status") == "completed":
                fresh_attempt = int(refreshed.get("run_attempt") or 1)
                refreshed_index = load_index(root)
                complete = any(str(item.get("run_id")) == run_id and int(item.get("attempt") or 1) == fresh_attempt
                               and item.get("capture_stage") == "post_run" and item.get("report_status") == "Complete"
                               for item in refreshed_index["runs"])
                if complete:
                    pending.discard(run_id)
                else:
                    pending.add(run_id)
            else:
                pending.add(run_id)
        except Exception as exc:
            pending.add(run_id)
            print("Capture failed for run " + run_id + ": " + redact(exc), file=sys.stderr)

    processed = 0
    for request_file in sorted((root / "requests" / "pending").glob("*.json")) if (root / "requests" / "pending").is_dir() else []:
        try:
            request = json.loads(request_file.read_text(encoding="utf-8"))
            run_id = str(request.get("run_id", ""))
            if not run_id.isdigit():
                raise ValueError("run_id must be a numeric string")
            metadata_errors = []
            metadata = api_get(repo, "/repos/" + repo + "/actions/runs/" + run_id, metadata_errors, "manual_request")
            if not isinstance(metadata, dict):
                raise RuntimeError("Requested run metadata was unavailable.")
            if metadata.get("status") != "completed":
                pending.add(run_id)
                continue
            capture_one(repo, root, run_id, "post_run", force=True)
            current_index = load_index(root)
            attempt = int(metadata.get("run_attempt") or 1)
            complete = any(
                str(item.get("run_id")) == run_id
                and int(item.get("attempt") or 1) == attempt
                and item.get("capture_stage") == "post_run"
                and item.get("report_status") == "Complete"
                for item in current_index["runs"]
            )
            if complete:
                done = root / "requests" / "processed" / request_file.name
                done.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(request_file), str(done))
                pending.discard(run_id)
                processed += 1
            else:
                pending.add(run_id)
        except Exception as exc:
            print("Backfill request remains pending: " + request_file.name + " " + redact(exc), file=sys.stderr)

    index = load_index(root)
    index["sweep_watermark_utc"] = started
    index["pending_run_ids"] = sorted(pending, key=lambda value: int(value), reverse=True)
    save_json(root / "index.json", index)
    print("Sweep complete. New reports: " + str(new_reports) + "; backfill requests: " + str(processed) +
          "; pending runs: " + str(len(pending)) + ".")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("current", "sweep"), required=True)
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY"))
    parser.add_argument("--run-id", default=os.environ.get("GITHUB_RUN_ID"))
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    if not args.repo or "/" not in args.repo:
        parser.error("GITHUB_REPOSITORY or --repo must be owner/repository")
    if args.mode == "current":
        if not args.run_id:
            parser.error("GITHUB_RUN_ID or --run-id is required.")
        target = capture_one(args.repo, args.root, args.run_id, "pre_finalizer")
        print("Pre-finalizer capture: " + ("already present" if target is None else str(target)))
    else:
        run_sweep(args.repo, args.root)


if __name__ == "__main__":
    main()
