#!/usr/bin/env python3
"""Generate detailed Markdown and structured JSON lint evidence for both scopes."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ASSET_DIR = Path(__file__).resolve().parents[1] / "assets"
REPORT_TEMPLATE_PATH = ASSET_DIR / "lint-report-template.md"
REPORT_SCHEMA_PATH = ASSET_DIR / "lint-report-schema.json"
SCHEMA_VERSION = "1.2.0"
VALID_SCOPES = {"on_changed", "on_repo"}
VALID_STATUSES = {"Passed", "Failed", "Incomplete", "Cancelled", "Superseded"}


def _matches_type(value, expected):
    types = expected if isinstance(expected, list) else [expected]
    for kind in types:
        if kind == "object" and isinstance(value, dict):
            return True
        if kind == "array" and isinstance(value, list):
            return True
        if kind == "string" and isinstance(value, str):
            return True
        if kind == "integer" and isinstance(value, int) and not isinstance(value, bool):
            return True
        if kind == "number" and isinstance(value, (int, float)) and not isinstance(value, bool):
            return True
        if kind == "null" and value is None:
            return True
    return False


def validate_schema(value, schema, path="$"):
    if "const" in schema and value != schema["const"]:
        raise ValueError(path + " must equal " + repr(schema["const"]))
    if "enum" in schema and value not in schema["enum"]:
        raise ValueError(path + " must be one of " + repr(schema["enum"]))
    if "type" in schema and not _matches_type(value, schema["type"]):
        raise ValueError(path + " has an invalid type")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                raise ValueError(path + " is missing required field " + key)
        properties = schema.get("properties", {})
        extra = schema.get("additionalProperties", True)
        for key, item in value.items():
            child_path = path + "." + key
            if key in properties:
                validate_schema(item, properties[key], child_path)
            elif extra is False:
                raise ValueError(child_path + " is not allowed")
            elif isinstance(extra, dict):
                validate_schema(item, extra, child_path)
    if isinstance(value, list) and "items" in schema:
        for index, item in enumerate(value):
            validate_schema(item, schema["items"], path + "[" + str(index) + "]")


def safe_int(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def load_records(records_dir):
    records = []
    for file in sorted(Path(records_dir).glob("*.json")):
        try:
            item = json.loads(file.read_text(encoding="utf-8"))
            if not isinstance(item, dict):
                raise ValueError("Per-file linter output must be a JSON object")
        except Exception as exc:
            item = {"path": file.stem, "exit_code": 2, "capture_error": str(exc), "violations": []}
        item.setdefault("path", file.stem)
        item.setdefault("exit_code", 0)
        if not isinstance(item.get("violations"), list):
            item["capture_error"] = "The violations field is not an array"
            item["violations"] = []
            item["exit_code"] = max(2, safe_int(item.get("exit_code"), 0))
        records.append(item)
    return records


def load_checks(checks_file):
    if not checks_file:
        return []
    try:
        payload = json.loads(Path(checks_file).read_text(encoding="utf-8"))
        checks = payload.get("checks", []) if isinstance(payload, dict) else payload
        if not isinstance(checks, list):
            raise ValueError("Check evidence must be an array")
    except Exception as exc:
        return [{"name": "Load validation check evidence", "status": "Failed", "exit_code": 2, "output": str(exc)}]
    normalized = []
    for item in checks:
        if not isinstance(item, dict):
            normalized.append({"name": "Unknown check", "status": "Failed", "exit_code": 2, "output": "The check record is not an object"})
            continue
        check = dict(item)
        check.setdefault("name", "Unnamed check")
        check.setdefault("status", "Unknown")
        check.setdefault("exit_code", None)
        check.setdefault("output", "")
        if check["status"] in ("success", "passed", "PASS"):
            check["status"] = "Passed"
        elif check["status"] in ("failure", "failed", "FAIL"):
            check["status"] = "Failed"
        elif check["status"] in ("skipped", "Skipped"):
            check["status"] = "Skipped"
        elif check["status"] not in ("Passed", "Failed", "Skipped", "Unknown"):
            check["status"] = "Unknown"
        normalized.append(check)
    return normalized


def finding_fingerprint(file_path, finding):
    identity = {key: finding.get(key) for key in ("rule", "match", "message")}
    raw = json.dumps([file_path, identity], sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:24]


def inline(value):
    value = str(value if value is not None else "Unknown")
    return value.replace("\r", " ").replace("\n", " ").replace("|", "\\|").strip()


def fence(text):
    text = str(text or "No output captured.")
    longest = max((len(match.group(0)) for match in re.finditer(r"~+", text)), default=0)
    marker = "~" * max(3, longest + 1)
    return marker + "text\n" + text.rstrip("\n") + "\n" + marker


def format_finding(finding, comparison=None):
    location = "{}:{}:{}".format(
        inline(finding.get("file", "Unknown")),
        inline(finding.get("line", "?")),
        inline(finding.get("col", finding.get("column", "?"))),
    )
    label = comparison or finding.get("comparison", "unclassified")
    return [
        "- **{}** · {} · **{}** · fingerprint: {}".format(
            inline(finding.get("rule", "unknown")), location,
            inline(label), inline(finding.get("fingerprint", "Unknown")),
        ),
        "  - **Level:** " + inline(finding.get("level", "Unknown")),
        "  - **Message:** " + inline(finding.get("message", "No message recorded")),
        "  - **Matched text:** " + inline(finding.get("match", "Not recorded")),
    ]


def build_markdown(data):
    template = REPORT_TEMPLATE_PATH.read_text(encoding="utf-8")
    files_text = "\n".join("- " + inline(path) for path in data["files_evaluated"])
    if not files_text:
        files_text = "No Markdown files were evaluated in this run."

    rows = [
        "| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for record in data["records"]:
        exit_code = safe_int(record.get("exit_code"), 0)
        rows.append("| {} | {} | {} | {} | {} | {} | {} | {} |".format(
            inline(record.get("path", "Unknown")),
            "PASS" if exit_code == 0 else "FAIL",
            safe_int(record.get("count"), len(record.get("violations", []))),
            safe_int(record.get("hard_count"), 0),
            safe_int(record.get("baseline"), 0),
            safe_int(record.get("words"), 0),
            inline(record.get("per_100_words", 0)),
            exit_code,
        ))
    rule_rows = ["| Rule | Findings |", "|---|---:|"]
    for rule, count in sorted(data["findings_by_rule"].items(), key=lambda item: (-item[1], item[0])):
        rule_rows.append("| {} | {} |".format(inline(rule), count))

    check_blocks = []
    for check in data["checks"]:
        check_blocks.extend([
            "### " + inline(check.get("name", "Unnamed check")), "",
            "- **Result:** " + inline(check.get("status", "Unknown")),
            "- **Exit code:** " + inline(check.get("exit_code")), "",
            fence(check.get("output", "")), "",
        ])
    if not check_blocks:
        check_blocks = ["No separate workflow checks were recorded."]

    per_file = []
    for record in data["records"]:
        path = record.get("path", "Unknown")
        exit_code = safe_int(record.get("exit_code"), 0)
        matched = [finding for finding in data["findings"] if finding.get("file") == path]
        per_file.extend([
            "### " + inline(path), "",
            "- **Result:** " + ("PASS" if exit_code == 0 else "FAIL"),
            "- **Exit code:** " + str(exit_code),
            "- **Findings:** " + str(safe_int(record.get("count"), len(record.get("violations", [])))),
            "- **Hard findings:** " + str(safe_int(record.get("hard_count"), 0)),
            "- **Baseline:** " + str(safe_int(record.get("baseline"), 0)),
            "- **Words:** " + str(safe_int(record.get("words"), 0)),
            "- **Findings per 100 words:** " + inline(record.get("per_100_words", 0)),
        ])
        if record.get("capture_error"):
            per_file.extend(["", "**Capture error:**", "", fence(record["capture_error"])])
        if matched:
            per_file.extend(["", "#### Complete diagnostics", ""])
            for finding in matched:
                per_file.extend(format_finding(finding))
                per_file.append("")
        else:
            per_file.extend(["", "No STE findings were recorded for this file.", ""])
        per_file.append("")

    comparison = []
    for title, label, items in (
        ("New findings", "new", [f for f in data["findings"] if f["comparison"] == "new"]),
        ("Recurring findings", "recurring", [f for f in data["findings"] if f["comparison"] == "recurring"]),
        ("Resolved findings", "resolved", data["resolved_findings"]),
    ):
        comparison.extend(["### " + title, ""])
        for item in items:
            comparison.extend(format_finding(item, label))
        if not items:
            comparison.append("None.")
        comparison.append("")

    values = {
        "scope_title": data["scope"].replace("_", " ").title(),
        "source_task_id": data.get("source_task_id") or "Unassigned",
        "schema_version": data["schema_version"], "status": data["status"],
        "run_number": data["run_number"], "run_url": data["run_url"],
        "run_id": data["run_id"], "attempt": data["attempt"],
        "workflow": data["workflow"] or "Unknown", "branch": data["branch"],
        "commit": data["commit_sha"], "event": data["event"],
        "mode": data["execution_mode"], "baseline_sha": data["baseline_sha"] or "Not applicable",
        "linter_source_sha": data["linter_source_sha"] or "Unknown",
        "generated_at": data["generated_at_utc"], "runner_os": data["runner_os"] or "Unknown",
        "python_version": data["runtime"]["python"].split()[0],
        "platform": data["runtime"]["platform"],
        "files_evaluated": data["files_evaluated_count"],
        "files_failed": data["files_failed"], "files_with_findings": data["files_with_findings"],
        "total_findings": data["total_findings"], "hard_findings": data["hard_findings"],
        "advisory_findings": data["advisory_findings"], "new_findings": data["new_findings"],
        "recurring_findings": data["recurring_findings"],
        "resolved_findings": len(data["resolved_findings"]),
        "failed_checks": len(data["failed_checks"]),
        "files_list": files_text, "file_summary": "\n".join(rows),
        "rule_summary": "\n".join(rule_rows) if data["findings_by_rule"] else "No findings.",
        "checks": "\n".join(check_blocks).rstrip(),
        "baseline_comparison": "\n".join(comparison).rstrip(),
        "per_file_results": "\n".join(per_file).rstrip() or "No per-file records were captured.",
    }
    return template.format_map(values)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in (
        "scope", "records-dir", "output-dir", "run-id", "run-number",
        "run-url", "attempt", "branch", "commit", "event", "mode", "status",
    ):
        parser.add_argument("--" + name, required=True)
    parser.add_argument("--baseline", default="")
    parser.add_argument("--previous-report", default="")
    parser.add_argument("--linter-source-sha", default="")
    parser.add_argument("--checks-file", default="")
    parser.add_argument("--task-id", default="")
    args = parser.parse_args()

    if args.scope not in VALID_SCOPES:
        parser.error("--scope must be one of " + ", ".join(sorted(VALID_SCOPES)))
    if args.status not in VALID_STATUSES:
        parser.error("--status must be one of " + ", ".join(sorted(VALID_STATUSES)))

    records = load_records(args.records_dir)
    checks = load_checks(args.checks_file)
    findings = []
    for record in records:
        for original in record.get("violations", []):
            if not isinstance(original, dict):
                continue
            finding = dict(original)
            finding["file"] = str(record["path"])
            finding["fingerprint"] = finding_fingerprint(finding["file"], finding)
            findings.append(finding)

    previous_findings = []
    if args.previous_report and Path(args.previous_report).is_file():
        try:
            previous = json.loads(Path(args.previous_report).read_text(encoding="utf-8"))
            if isinstance(previous, dict) and isinstance(previous.get("findings"), list):
                previous_findings = previous["findings"]
        except (OSError, ValueError):
            previous_findings = []
    previous_ids = {
        item.get("fingerprint") for item in previous_findings
        if isinstance(item, dict) and item.get("fingerprint")
    }
    current_ids = {item["fingerprint"] for item in findings}
    for item in findings:
        item["comparison"] = "recurring" if item["fingerprint"] in previous_ids else "new"
    resolved = [
        {**item, "comparison": "resolved"}
        for item in previous_findings
        if isinstance(item, dict) and item.get("fingerprint") not in current_ids
    ]

    hard = sum(1 for item in findings if item.get("level") in ("advisory-free", "hard"))
    by_rule = {}
    for finding in findings:
        rule = str(finding.get("rule", "unknown"))
        by_rule[rule] = by_rule.get(rule, 0) + 1
    failed_files = [
        str(record["path"]) for record in records
        if safe_int(record.get("exit_code"), 0) != 0
    ]
    failed_checks = [
        str(check.get("name", "Unnamed check")) for check in checks
        if check.get("status") == "Failed" or (
            check.get("exit_code") is not None and safe_int(check.get("exit_code"), 0) != 0
        )
    ]
    status = args.status
    if status == "Passed" and (failed_files or failed_checks):
        status = "Failed"

    generated = datetime.now(timezone.utc).isoformat()
    run_number = safe_int(args.run_number)
    attempt = safe_int(args.attempt, 1)
    data = {
        "schema_version": SCHEMA_VERSION, "scope": args.scope,
        "source_task_id": (args.task_id.strip() or None) if args.event == "push" else None,
        "run_id": args.run_id, "run_number": run_number, "run_url": args.run_url,
        "attempt": attempt, "branch": args.branch, "commit_sha": args.commit,
        "event": args.event, "workflow": os.environ.get("GITHUB_WORKFLOW"),
        "runner_os": os.environ.get("RUNNER_OS"), "execution_mode": args.mode,
        "baseline_sha": args.baseline or None, "generated_at_utc": generated,
        "status": status, "linter_source_sha": args.linter_source_sha or None,
        "runtime": {"python": sys.version, "platform": platform.platform()},
        "files_evaluated": [str(record["path"]) for record in records],
        "files_evaluated_count": len(records), "files_failed": len(failed_files),
        "failed_files": failed_files, "files_with_findings": len({f["file"] for f in findings}),
        "total_findings": len(findings), "hard_findings": hard,
        "advisory_findings": len(findings) - hard, "findings_by_rule": by_rule,
        "records": records, "findings": findings,
        "new_findings": sum(1 for f in findings if f["comparison"] == "new"),
        "recurring_findings": sum(1 for f in findings if f["comparison"] == "recurring"),
        "resolved_findings": resolved, "checks": checks, "failed_checks": failed_checks,
    }

    schema = json.loads(REPORT_SCHEMA_PATH.read_text(encoding="utf-8"))
    validate_schema(data, schema)
    output = Path(args.output_dir)
    if output.parent.name != "history" or output.parent.parent.name != args.scope:
        parser.error("--output-dir must be <scope>/history/<run-id>-attempt-<attempt>")
    scope_root = output.parent.parent
    output.mkdir(parents=True, exist_ok=True)
    markdown = build_markdown(data)
    report_json = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    (output / "report.md").write_text(markdown, encoding="utf-8")
    (output / "report.json").write_text(report_json, encoding="utf-8")

    index_path = Path(__file__).resolve().parents[4] / ".takeout" / "reports" / "index.json"
    try:
        index = json.loads(index_path.read_text(encoding="utf-8"))
        if not isinstance(index, dict) or not isinstance(index.get("runs"), list):
            raise ValueError("Invalid report index")
    except FileNotFoundError:
        index = {"schema_version": SCHEMA_VERSION, "runs": []}
    except (OSError, ValueError) as exc:
        raise SystemExit("Cannot read report index: " + str(exc))
    entry = {
        "family": "lint",
        key: data[key] for key in (
            "scope", "run_id", "run_number", "run_url", "attempt", "commit_sha",
            "generated_at_utc", "status", "execution_mode", "files_evaluated_count",
            "files_failed", "files_with_findings", "total_findings", "hard_findings",
            "advisory_findings", "new_findings", "recurring_findings",
        )
    }
    entry["resolved_findings_count"] = len(resolved)
    index["schema_version"] = SCHEMA_VERSION
    index["runs"] = [
        row for row in index["runs"]
        if (row.get("run_id"), row.get("attempt", 1)) != (args.run_id, attempt)
    ]
    index["runs"].append(entry)
    index["runs"].sort(
        key=lambda row: (
            safe_int(row.get("run_number")), safe_int(row.get("attempt"), 1),
            str(row.get("generated_at_utc", "")),
        ),
        reverse=True,
    )
    index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    latest_json = scope_root / "latest-lint-report.json"
    latest_markdown = scope_root / "latest-lint-report.md"
    replace_latest = True
    if latest_json.is_file():
        try:
            old_latest = json.loads(latest_json.read_text(encoding="utf-8"))
            replace_latest = (run_number, attempt) >= (
                safe_int(old_latest.get("run_number")),
                safe_int(old_latest.get("attempt"), 1),
            )
        except (OSError, ValueError, AttributeError):
            replace_latest = True
    if replace_latest:
        latest_json.write_text(report_json, encoding="utf-8")
        latest_markdown.write_text(markdown, encoding="utf-8")

    integrity = {
        "algorithm": "SHA-256", "schema_version": SCHEMA_VERSION,
        "files": {
            name: hashlib.sha256((output / name).read_bytes()).hexdigest()
            for name in ("report.md", "report.json")
        },
    }
    (output / "integrity.json").write_text(
        json.dumps(integrity, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
