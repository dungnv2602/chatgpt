#!/usr/bin/env python3
"""Ingest immutable lint and GitHub Actions reports into the central issue ledger."""
from __future__ import annotations
import argparse, copy, hashlib, json, re, tempfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

SCHEMA_VERSION = "1.1.0"
IGNORED_CATEGORIES = {"cancelled", "skipped", "neutral", "queued", "in_progress", "unavailable", "unknown", "not_available"}
IGNORED_LINT_STATUSES = {"Incomplete", "Cancelled", "Superseded"}

class LedgerError(ValueError):
    """Raised when a ledger or source index cannot be processed safely."""

def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

def parse_time(value):
    if not isinstance(value, str) or not value.strip():
        raise LedgerError("A source report has no valid UTC timestamp")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise LedgerError("Invalid timestamp: " + value) from exc
    if parsed.tzinfo is None:
        raise LedgerError("Timestamp must include a timezone: " + value)
    return parsed.astimezone(timezone.utc)

def validate_schema(value, schema, path="$"):
    expected = schema.get("type")
    if expected:
        kinds = expected if isinstance(expected, list) else [expected]
        checks = {
            "object": lambda item: isinstance(item, dict),
            "array": lambda item: isinstance(item, list),
            "string": lambda item: isinstance(item, str),
            "integer": lambda item: isinstance(item, int) and not isinstance(item, bool),
            "number": lambda item: isinstance(item, (int, float)) and not isinstance(item, bool),
            "boolean": lambda item: isinstance(item, bool),
            "null": lambda item: item is None,
        }
        if not any(checks[kind](value) for kind in kinds):
            raise LedgerError(path + " has an invalid type")
    if "const" in schema and value != schema["const"]:
        raise LedgerError(path + " must equal " + repr(schema["const"]))
    if "enum" in schema and value not in schema["enum"]:
        raise LedgerError(path + " has an unsupported value")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            raise LedgerError(path + " is shorter than minLength")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            raise LedgerError(path + " does not match its required pattern")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if value < schema.get("minimum", float("-inf")):
            raise LedgerError(path + " is below its minimum")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                raise LedgerError(path + " is missing " + key)
        properties = schema.get("properties", {})
        extra = schema.get("additionalProperties", True)
        for key, item in value.items():
            child = path + "." + key
            if key in properties:
                validate_schema(item, properties[key], child)
            elif extra is False:
                raise LedgerError(child + " is not allowed")
            elif isinstance(extra, dict):
                validate_schema(item, extra, child)
    if isinstance(value, list):
        if schema.get("uniqueItems") and len(value) != len(set(value)):
            raise LedgerError(path + " must contain unique items")
        if "items" in schema:
            for index, item in enumerate(value):
                validate_schema(item, schema["items"], path + "[" + str(index) + "]")

def safe_relative_path(value, prefix):
    if not isinstance(value, str) or not value:
        raise LedgerError("An index contains an empty report path")
    candidate = PurePosixPath(value)
    if candidate.is_absolute() or ".." in candidate.parts or not value.startswith(prefix):
        raise LedgerError("Unsafe report path in index: " + value)
    return value

def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise LedgerError("Cannot read JSON file " + str(path) + ": " + str(exc)) from exc

def indexed_reports(root):
    """Resolve report files only through the published family indexes."""
    found = []
    for scope in ("on_changed", "on_repo"):
        index_path = root / "reports" / "lint_reports" / scope / "index.json"
        if not index_path.is_file():
            continue
        index = read_json(index_path)
        if not isinstance(index, dict) or not isinstance(index.get("runs"), list):
            raise LedgerError("Invalid lint report index: " + str(index_path))
        for row in index["runs"]:
            if not isinstance(row, dict) or not row.get("run_id"):
                raise LedgerError("Invalid run entry in " + str(index_path))
            run_id = str(row["run_id"])
            attempt = row.get("attempt", 1)
            if not isinstance(attempt, int) or attempt < 1:
                raise LedgerError("Invalid attempt in " + str(index_path))
            base = root / "reports" / "lint_reports" / scope / "history"
            candidates = [base / (run_id + "-attempt-" + str(attempt)) / "report.json", base / run_id / "report.json"]
            report_path = next((item for item in candidates if item.is_file()), None)
            if report_path is not None:
                found.append(("lint", report_path.relative_to(root).as_posix(), row))
    gh_index_path = root / "reports" / "gh_ac_reports" / "index.json"
    if gh_index_path.is_file():
        index = read_json(gh_index_path)
        if not isinstance(index, dict) or not isinstance(index.get("runs"), list):
            raise LedgerError("Invalid GitHub Actions report index")
        for row in index["runs"]:
            if not isinstance(row, dict):
                raise LedgerError("Invalid GitHub Actions report index entry")
            history = row.get("history_path")
            if not history:
                continue
            history = safe_relative_path(history, "history/")
            report_path = root / "reports" / "gh_ac_reports" / Path(*PurePosixPath(history).parts) / "report.json"
            if report_path.is_file():
                found.append(("github_actions", report_path.relative_to(root).as_posix(), row))
    unique = {path: (family, path, row) for family, path, row in found}
    return sorted(unique.values(), key=lambda item: (item[2].get("generated_at_utc") or item[2].get("captured_at_utc") or "", item[1]))

def bootstrap_state(root, timestamp=None):
    paths = [path for _, path, _ in indexed_reports(root)]
    return {"bootstrap_at_utc": timestamp or utc_now(), "processed_reports": sorted(set(paths))}

def migrate_ledger(ledger, root):
    version = ledger.get("schema_version")
    if version not in ("1.0.0", SCHEMA_VERSION):
        raise LedgerError("Unsupported ledger schema version: " + str(version))
    if not isinstance(ledger.get("findings"), list):
        raise LedgerError("The ledger findings field must be an array")
    if version == "1.0.0":
        ledger["schema_version"] = SCHEMA_VERSION
    for finding in ledger["findings"]:
        if not isinstance(finding, dict):
            raise LedgerError("Every ledger finding must be an object")
        finding.setdefault("resolution_history", [])
        finding.setdefault("duplicate_of", None)
        finding.setdefault("accepted_risk", None)
    if not isinstance(ledger.get("ingestion_state"), dict):
        ledger["ingestion_state"] = bootstrap_state(root)
    state = ledger["ingestion_state"]
    state.setdefault("bootstrap_at_utc", utc_now())
    state.setdefault("processed_reports", [])
    if not isinstance(state["processed_reports"], list) or not all(isinstance(item, str) for item in state["processed_reports"]):
        raise LedgerError("ingestion_state.processed_reports must be an array of paths")
    state["processed_reports"] = sorted(set(state["processed_reports"]))
    return ledger

def normalize_signature(message):
    value = str(message or "").strip().lower()
    value = re.sub(r"\b[0-9a-f]{7,40}\b", "<sha>", value)
    value = re.sub(r"\b\d{7,}\b", "<id>", value)
    value = re.sub(r"\b\d{4}-\d\d-\d\d[t ][0-9:.+-]+z?\b", "<timestamp>", value)
    value = re.sub(r"\s+", " ", value).strip()
    if value in ("step conclusion: failure", "job conclusion: failure", "step conclusion: timed_out"):
        return ""
    return value

def lint_severity(level):
    if level in ("advisory-free", "hard"):
        return "medium"
    if level == "advisory":
        return "low"
    return "informational"

def actions_severity(issue):
    confidence = issue.get("confidence")
    if confidence == "high":
        return "high" if issue.get("blocking") else "medium"
    if confidence == "medium":
        return "medium"
    return "low"

def evidence_record(report_path, observed_at, run_url, observation_id, note):
    return {"report_path": report_path, "run_url": run_url or None, "observed_at_utc": observed_at,
            "note": note or None, "observation_id": observation_id}

def lint_observations(report, report_path):
    if report.get("status") in IGNORED_LINT_STATUSES:
        return []
    findings = report.get("findings")
    if not isinstance(findings, list):
        raise LedgerError("Lint report findings must be an array: " + report_path)
    observed_at = report.get("generated_at_utc")
    parse_time(observed_at)
    run_id, attempt = str(report.get("run_id", "")), report.get("attempt", 1)
    if not run_id or not isinstance(attempt, int):
        raise LedgerError("Lint report has invalid run identity: " + report_path)
    observation_id = "lint:" + run_id + ":" + str(attempt)
    scope = report.get("scope") or "unknown"
    result = {}
    for item in findings:
        if not isinstance(item, dict):
            raise LedgerError("Lint finding must be an object: " + report_path)
        fingerprint = item.get("fingerprint")
        if not isinstance(fingerprint, str) or len(fingerprint) < 8:
            raise LedgerError("Lint finding has no stable fingerprint: " + report_path)
        rule = str(item.get("rule") or "unknown")
        file_path = str(item.get("file") or "Unknown")
        message = str(item.get("message") or "No diagnostic message")
        identity = "lint-" + fingerprint
        note = scope + " · " + file_path
        if item.get("line") is not None:
            note += ":" + str(item["line"])
            if item.get("col") is not None:
                note += ":" + str(item["col"])
        result[identity] = {
            "finding_id": identity, "source_family": "lint", "category": rule,
            "title": (rule + ": " + message)[:240], "severity": lint_severity(item.get("level")),
            "evidence": evidence_record(report_path, observed_at, report.get("run_url"), observation_id, note),
        }
    return list(result.values())

def actions_observations(report, report_path):
    capture, source = report.get("capture") or {}, report.get("source_run") or {}
    if capture.get("stage") != "post_run" or capture.get("completeness") != "Complete":
        return []
    if source.get("status") != "completed":
        return []
    issues = (report.get("classification") or {}).get("issues")
    if not isinstance(issues, list):
        raise LedgerError("GitHub Actions classification issues must be an array: " + report_path)
    workflow_id = source.get("workflow_id")
    workflow_path = str(source.get("workflow_path") or "")
    workflow_name = str(source.get("workflow_name") or "Unknown workflow")
    run_id, attempt = str(source.get("id") or ""), source.get("attempt", 1)
    if not workflow_id or not workflow_path or not run_id or not isinstance(attempt, int):
        raise LedgerError("GitHub Actions report has invalid workflow identity: " + report_path)
    observed_at = capture.get("captured_at_utc")
    parse_time(observed_at)
    observation_id = "github_actions:" + str(workflow_id) + ":" + run_id + ":" + str(attempt)
    result = {}
    for issue in issues:
        if not isinstance(issue, dict):
            raise LedgerError("GitHub Actions issue must be an object: " + report_path)
        category = str(issue.get("category") or "unknown").strip().lower()
        if category in IGNORED_CATEGORIES:
            continue
        job_name, step_name = str(issue.get("job_name") or "").strip(), str(issue.get("step_name") or "").strip()
        signature = normalize_signature(issue.get("message"))
        if category.startswith("workflow_") and not job_name and not step_name:
            continue
        if not job_name and not step_name and (not signature or issue.get("confidence") == "low"):
            continue
        identity_data = [str(workflow_id), workflow_path, job_name, step_name, category, signature]
        identity_json = json.dumps(identity_data, ensure_ascii=False, separators=(",", ":"))
        identity = "gha-" + hashlib.sha256(identity_json.encode("utf-8")).hexdigest()[:24]
        location = " / ".join(part for part in (job_name, step_name) if part)
        title = workflow_name + " / " + (location or "workflow") + ": " + category
        if signature:
            title += " — " + signature
        result[identity] = {
            "finding_id": identity, "source_family": "github_actions", "category": category,
            "title": title[:240], "severity": actions_severity(issue),
            "evidence": evidence_record(report_path, observed_at, source.get("run_url"), observation_id, location),
        }
    return list(result.values())

def upsert_finding(ledger, observation):
    existing = next((item for item in ledger["findings"] if item["finding_id"] == observation["finding_id"]), None)
    evidence = observation["evidence"]
    if existing is None:
        ledger["findings"].append({
            "finding_id": observation["finding_id"], "source_family": observation["source_family"],
            "category": observation["category"], "title": observation["title"], "status": "open",
            "severity": observation["severity"], "owner": None, "first_seen_utc": evidence["observed_at_utc"],
            "last_seen_utc": evidence["observed_at_utc"], "occurrence_count": 1, "evidence": [evidence],
            "resolution": None, "resolution_history": [], "duplicate_of": None, "accepted_risk": None,
        })
        return "created"
    before = json.dumps(existing, sort_keys=True, ensure_ascii=False)
    evidence_rows = existing.setdefault("evidence", [])
    known_paths = {row.get("report_path") for row in evidence_rows if isinstance(row, dict)}
    known_observations = {row.get("observation_id") or row.get("report_path") for row in evidence_rows if isinstance(row, dict)}
    observation_key = evidence.get("observation_id") or evidence["report_path"]
    if evidence["report_path"] not in known_paths:
        evidence_rows.append(evidence)
    if observation_key not in known_observations and existing.get("status") == "resolved":
        resolution = existing.get("resolution")
        if resolution:
            existing.setdefault("resolution_history", []).append(copy.deepcopy(resolution))
        existing["resolution"] = None
        existing["status"] = "open"
    valid_times = [row.get("observed_at_utc") for row in evidence_rows if isinstance(row, dict) and isinstance(row.get("observed_at_utc"), str)]
    if valid_times:
        existing["first_seen_utc"] = min(valid_times, key=parse_time)
        existing["last_seen_utc"] = max(valid_times, key=parse_time)
    occurrence_keys = {row.get("observation_id") or row.get("report_path") for row in evidence_rows if isinstance(row, dict)}
    existing["occurrence_count"] = len(occurrence_keys)
    return "updated" if before != json.dumps(existing, sort_keys=True, ensure_ascii=False) else "unchanged"

def validate_semantics(ledger):
    finding_ids = {finding.get("finding_id") for finding in ledger["findings"] if isinstance(finding, dict)}
    for finding in ledger["findings"]:
        status = finding["status"]
        if status == "resolved":
            resolution = finding.get("resolution")
            if not isinstance(resolution, dict):
                raise LedgerError("Resolved finding requires resolution evidence: " + finding["finding_id"])
            commit, validation = resolution.get("fix_commit"), resolution.get("validation")
            if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-fA-F]{7,40}", commit):
                raise LedgerError("Resolved finding requires a valid fix commit: " + finding["finding_id"])
            if not isinstance(validation, dict) or validation.get("conclusion") != "success":
                raise LedgerError("Resolved finding requires successful validation evidence: " + finding["finding_id"])
            if not validation.get("run_url") or not validation.get("validated_at_utc"):
                raise LedgerError("Resolved finding requires a validation URL and timestamp: " + finding["finding_id"])
        if status == "accepted":
            risk = finding.get("accepted_risk")
            if not isinstance(risk, dict) or not risk.get("rationale") or not risk.get("accepted_by") or not risk.get("accepted_at_utc"):
                raise LedgerError("Accepted finding requires documented risk acceptance: " + finding["finding_id"])
        if status == "duplicate":
            duplicate_of = finding.get("duplicate_of")
            if not duplicate_of or duplicate_of == finding["finding_id"] or duplicate_of not in finding_ids:
                raise LedgerError("Duplicate finding requires an existing, different duplicate_of ID: " + finding["finding_id"])

def atomic_write(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    temp_name = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, prefix=path.name + ".", suffix=".tmp", delete=False) as handle:
            temp_name = handle.name
            handle.write(data)
            handle.flush()
        Path(temp_name).replace(path)
    finally:
        if temp_name and Path(temp_name).exists():
            Path(temp_name).unlink()

def ingest(root, now=None):
    root = Path(root).resolve()
    ledger_path, schema_path = root / "reports/triage/ledger.json", root / "reports/triage/ledger-schema.json"
    ledger = read_json(ledger_path)
    if not isinstance(ledger, dict):
        raise LedgerError("The ledger root must be an object")
    before_migration = json.dumps(ledger, sort_keys=True, ensure_ascii=False)
    ledger = migrate_ledger(ledger, root)
    migration_changed = before_migration != json.dumps(ledger, sort_keys=True, ensure_ascii=False)
    schema = read_json(schema_path)
    validate_schema(ledger, schema, "$ledger")
    validate_semantics(ledger)
    state, processed = ledger["ingestion_state"], set(ledger["ingestion_state"]["processed_reports"])
    counts = {"reports_processed": 0, "findings_created": 0, "findings_updated": 0, "findings_unchanged": 0}
    changed, warnings = migration_changed, []
    for family, report_path, _row in indexed_reports(root):
        if report_path in processed:
            continue
        try:
            report = read_json(root / report_path)
            if not isinstance(report, dict):
                raise LedgerError("Report root must be an object")
            observations = lint_observations(report, report_path) if family == "lint" else actions_observations(report, report_path)
        except (LedgerError, TypeError, KeyError) as exc:
            warnings.append(str(exc))
            continue
        for observation in observations:
            result = upsert_finding(ledger, observation)
            if result == "created":
                counts["findings_created"] += 1
                changed = True
            elif result == "updated":
                counts["findings_updated"] += 1
                changed = True
            else:
                counts["findings_unchanged"] += 1
        state["processed_reports"].append(report_path)
        processed.add(report_path)
        counts["reports_processed"] += 1
        changed = True
    state["processed_reports"] = sorted(processed)
    if changed:
        ledger["updated_at_utc"] = now or utc_now()
        validate_schema(ledger, schema, "$ledger")
        validate_semantics(ledger)
        atomic_write(ledger_path, ledger)
    return {**counts, "total_findings": len(ledger["findings"]), "warnings": warnings, "changed": changed}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("ingest",), default="ingest")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3])
    args = parser.parse_args()
    print(json.dumps(ingest(args.root), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
