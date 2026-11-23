#!/usr/bin/env python3
"""Build machine-readable and human-readable lint evidence from per-file JSON."""
import argparse, hashlib, json, platform, sys
from pathlib import Path
from datetime import datetime, timezone

p = argparse.ArgumentParser()
for name in ("scope", "records_dir", "output_dir", "run_id", "run_number", "run_url", "attempt", "branch", "commit", "event", "mode", "status"):
    p.add_argument("--" + name.replace("_", "-"), required=True)
p.add_argument("--baseline", default="")
p.add_argument("--previous-report", default="")
p.add_argument("--linter-source-sha", default="")
a = p.parse_args()
records = []
for file in sorted(Path(a.records_dir).glob("*.json")):
    try:
        item = json.loads(file.read_text(encoding="utf-8"))
    except Exception as exc:
        item = {"path": file.stem, "exit_code": 2, "capture_error": str(exc), "violations": []}
    item.setdefault("path", file.stem)
    records.append(item)
findings = []
for record in records:
    for original in record.get("violations", []):
        finding = dict(original)
        finding["file"] = record["path"]
        identity = {key: finding.get(key) for key in ("rule", "match", "message")}
        finding["fingerprint"] = hashlib.sha256(json.dumps([finding["file"], identity], sort_keys=True).encode()).hexdigest()[:20]
        findings.append(finding)
by_rule = {}
for finding in findings:
    rule = str(finding.get("rule", "unknown"))
    by_rule[rule] = by_rule.get(rule, 0) + 1
hard = sum(int(record.get("hard_count", 0)) for record in records)
previous_findings = []
if a.previous_report and Path(a.previous_report).is_file():
    try:
        previous_findings = json.loads(Path(a.previous_report).read_text(encoding="utf-8")).get("findings", [])
    except (OSError, ValueError):
        previous_findings = []
previous_ids = {item.get("fingerprint") for item in previous_findings}
current_ids = {item.get("fingerprint") for item in findings}
for item in findings:
    item["comparison"] = "recurring" if item.get("fingerprint") in previous_ids else "new"
resolved = [item for item in previous_findings if item.get("fingerprint") not in current_ids]
failed = [record["path"] for record in records if int(record.get("exit_code", 0)) != 0]
generated = datetime.now(timezone.utc).isoformat()
data = {
    "schema_version": "1.0.0", "scope": a.scope, "run_id": a.run_id,
    "run_number": int(a.run_number), "run_url": a.run_url, "attempt": int(a.attempt),
    "branch": a.branch, "commit_sha": a.commit, "event": a.event,
    "workflow": __import__("os").environ.get("GITHUB_WORKFLOW"),
    "runner_os": __import__("os").environ.get("RUNNER_OS"),
    "execution_mode": a.mode, "baseline_sha": a.baseline or None,
    "generated_at_utc": generated, "status": a.status,
    "linter_source_sha": a.linter_source_sha or None,
    "runtime": {"python": sys.version, "platform": platform.platform()},
    "files_evaluated": [record["path"] for record in records], "files_evaluated_count": len(records), "files_failed": len(failed),
    "total_findings": len(findings), "hard_findings": hard,
    "findings_by_rule": by_rule, "failed_files": failed,
    "records": records, "findings": findings,
    "new_findings": sum(1 for item in findings if item["comparison"] == "new"),
    "recurring_findings": sum(1 for item in findings if item["comparison"] == "recurring"),
    "resolved_findings": resolved
}
out = Path(a.output_dir)
out.mkdir(parents=True, exist_ok=True)
(out / "report.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
lines = [
    "# " + a.scope.replace("_", " ").title() + " Lint Report", "",
    "- **Status:** " + a.status,
    "- **Run:** [#" + a.run_number + "](" + a.run_url + ")",
    "- **Run ID / attempt:** " + a.run_id + " / " + a.attempt,
    "- **Branch / commit:** " + a.branch + " / " + a.commit,
    "- **Trigger:** " + a.event, "- **Execution mode:** " + a.mode,
    "- **Baseline SHA:** " + (a.baseline or "not applicable"),
    "- **Generated (UTC):** " + generated, "",
    "## Coverage", "",
    "- Files evaluated: " + str(len(records)),
    "- Files with execution failures: " + str(len(failed)),
    "- Findings: " + str(len(findings)) + " (hard: " + str(hard) + ")", "",
    "## Findings by rule", ""
]
lines += ["- " + key + ": " + str(value) for key, value in sorted(by_rule.items())] or ["No findings."]
lines += ["", "## Per-file results", ""]
for record in records:
    lines += ["### " + record["path"], "",
              "- Exit code: " + str(record.get("exit_code", "not recorded")),
              "- Findings: " + str(record.get("count", len(record.get("violations", [])))),
              "- Hard findings: " + str(record.get("hard_count", "not recorded")), ""]
    for finding in record.get("violations", []):
        lines.append("- " + str(finding.get("level", "level unknown")) + " " +
                     str(finding.get("rule", "unknown")) + " at " +
                     str(finding.get("line", "?")) + ":" + str(finding.get("col", "?")) +
                     ": " + str(finding.get("message", "")) + " Match: " +
                     str(finding.get("match", "")))
    lines.append("")
lines += ["## Baseline comparison", "",
    "- New findings: " + str(data["new_findings"]),
    "- Recurring findings: " + str(data["recurring_findings"]),
    "- Resolved findings: " + str(len(resolved)), "",
    "## Structured evidence", "", "The complete original per-file JSON payloads and normalized findings are in report.json.", ""]
(out / "report.md").write_text("\n".join(lines), encoding="utf-8")
scope_root = out.parent.parent
index_path = scope_root / "index.json"
index = json.loads(index_path.read_text(encoding="utf-8")) if index_path.exists() else {"schema_version": "1.0.0", "runs": []}
entry = {key: data[key] for key in ("run_id", "run_number", "run_url", "attempt", "commit_sha", "generated_at_utc", "status", "files_evaluated_count", "total_findings")}
index["runs"] = [row for row in index["runs"] if (row.get("run_id"), row.get("attempt", 1)) != (a.run_id, int(a.attempt))] + [entry]
index["runs"].sort(key=lambda row: (row["generated_at_utc"], row["run_id"]))
index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(scope_root / "latest-lint-report.md").write_text((out / "report.md").read_text(encoding="utf-8"), encoding="utf-8")
(scope_root / "latest-lint-report.json").write_text((out / "report.json").read_text(encoding="utf-8"), encoding="utf-8")
integrity = {"algorithm": "SHA-256", "files": {name: hashlib.sha256((out / name).read_bytes()).hexdigest() for name in ("report.md", "report.json")}}
(out / "integrity.json").write_text(json.dumps(integrity, indent=2) + "\\n", encoding="utf-8")
