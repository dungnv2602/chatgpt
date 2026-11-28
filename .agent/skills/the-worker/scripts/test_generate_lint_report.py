#!/usr/bin/env python3
"""Hosted regression tests for the shared STE lint evidence generator."""
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("generate_lint_report.py")
ASSET_DIR = SCRIPT.parents[1] / "assets"
REPORT_TEMPLATE = ASSET_DIR / "lint-report-template.md"
REPORT_SCHEMA = ASSET_DIR / "lint-report-schema.json"


class ReportGeneratorTests(unittest.TestCase):
    def run_report(self, root, scope, run_id, run_number, attempt, records,
                   previous="", checks=None, status="Passed", task_id="", event="push"):
        records_dir = root / ("records-" + run_id + "-" + str(attempt))
        records_dir.mkdir()
        for name, value in records.items():
            (records_dir / (name + ".json")).write_text(json.dumps(value), encoding="utf-8")
        output = root / ".takeout" / "reports" / "history" / (run_id + "-attempt-" + str(attempt))
        checks_file = root / ("checks-" + run_id + ".json")
        checks_file.write_text(json.dumps(checks or []), encoding="utf-8")
        command = [
            sys.executable, str(SCRIPT), "--scope", scope,
            "--records-dir", str(records_dir), "--output-dir", str(output),
            "--run-id", run_id, "--run-number", str(run_number),
            "--run-url", "https://example.invalid/run/" + run_id,
            "--attempt", str(attempt), "--branch", "gpt", "--commit", "abc123",
            "--event", event, "--mode",
            "repository-wide" if scope == "on_repo" else "incremental",
            "--baseline", "" if scope == "on_repo" else "base123",
            "--status", status, "--checks-file", str(checks_file),
        ]
        if task_id:
            command += ["--task-id", task_id]
        if previous:
            command += ["--previous-report", previous]
        env = dict(os.environ)
        env["GITHUB_WORKFLOW"] = "Test lint report"
        env["RUNNER_OS"] = "Linux"
        subprocess.run(command, check=True, capture_output=True, text=True, env=env)
        return output

    def test_changed_scope_details_schema_and_integrity(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            record = {
                "path": "docs/a.md", "exit_code": 0,
                "violations": [
                    {"rule":"semicolon","match":";","message":"Split the sentence.",
                     "line":3,"col":8,"level":"advisory-free"},
                    {"rule":"passive-voice","match":"is used","message":"Name the actor.",
                     "line":7,"col":2,"level":"advisory"},
                ],
                "count":2,"hard_count":1,"baseline":0,"words":40,"per_100_words":5.0,
            }
            checks = [{
                "name":"Markdown link check","status":"Passed","exit_code":0,
                "output":"Scanned 1 file and 2 links.",
            }]
            first = self.run_report(root,"on_changed","100",10,1,{"a":record},checks=checks)
            report = json.loads((first/"report.json").read_text(encoding="utf-8"))
            schema = json.loads(REPORT_SCHEMA.read_text(encoding="utf-8"))
            self.assertTrue(REPORT_TEMPLATE.is_file())
            self.assertIn("on_changed",schema["properties"]["scope"]["enum"])
            self.assertIn("on_repo",schema["properties"]["scope"]["enum"])
            self.assertEqual(report["schema_version"],"1.2.0")
            self.assertEqual(report["scope"],"on_changed")
            self.assertEqual(report["files_evaluated"],["docs/a.md"])
            self.assertEqual(report["files_evaluated_count"],1)
            self.assertEqual(report["files_with_findings"],1)
            self.assertEqual(report["total_findings"],2)
            self.assertEqual(report["hard_findings"],1)
            self.assertEqual(report["advisory_findings"],1)
            self.assertEqual(report["checks"][0]["output"],checks[0]["output"])
            self.assertEqual(report["findings"][0]["comparison"],"new")
            self.assertTrue(report["findings"][0]["fingerprint"])
            integrity=json.loads((first/"integrity.json").read_text(encoding="utf-8"))
            self.assertEqual(integrity["files"]["report.json"],
                             hashlib.sha256((first/"report.json").read_bytes()).hexdigest())
            self.assertTrue((first/"report.json").is_file())
            index=json.loads((root/".takeout"/"reports"/"index.json").read_text(encoding="utf-8"))
            self.assertEqual(index["runs"][0]["total_findings"],2)
            self.assertEqual(index["runs"][0]["files_evaluated_count"],1)

    def test_full_scope_and_execution_failures_are_captured(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            record={
                "path":"skills/example.md","exit_code":1,
                "violations":[{
                    "rule":"long-sentence","match":"26 words","message":"Split the sentence.",
                    "line":4,"col":1,"level":"advisory-free",
                }],
                "count":1,"hard_count":1,"baseline":0,"words":75,"per_100_words":1.3,
            }
            checks=[{"name":"Anchor check","status":"Failed","exit_code":1,
                     "output":"One unresolved local link."}]
            output=self.run_report(root,"on_repo","200",20,1,{"one":record},
                                   checks=checks,status="Failed")
            report=json.loads((output/"report.json").read_text(encoding="utf-8"))
            self.assertEqual(report["scope"],"on_repo")
            self.assertEqual(report["status"],"Failed")
            self.assertEqual(report["files_failed"],1)
            self.assertEqual(report["failed_files"],["skills/example.md"])
            self.assertEqual(report["failed_checks"],["Anchor check"])
            self.assertEqual(report["records"][0]["words"],75)

    def test_baseline_new_recurring_and_resolved_findings(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            recurring={"rule":"semicolon","match":";","message":"Split the sentence.",
                       "line":3,"col":8,"level":"advisory-free"}
            previous_dir=self.run_report(root,"on_changed","300",30,1,{
                "a":{"path":"docs/a.md","exit_code":0,"violations":[recurring],
                     "count":1,"hard_count":1,"baseline":0,"words":20},
                "old":{"path":"docs/old.md","exit_code":0,"violations":[{
                    "rule":"passive-voice","match":"is used","message":"Name the actor.",
                    "line":2,"col":1,"level":"advisory",
                }],"count":1,"hard_count":0,"baseline":0,"words":20},
            })
            second=self.run_report(root,"on_changed","301",31,1,{"a":{
                "path":"docs/a.md","exit_code":0,"violations":[recurring,{
                    "rule":"long-sentence","match":"26 words","message":"Split it.",
                    "line":12,"col":1,"level":"advisory-free",
                }],"count":2,"hard_count":2,"baseline":0,"words":30,
            }},previous=str(previous_dir/"report.json"))
            report=json.loads((second/"report.json").read_text(encoding="utf-8"))
            self.assertEqual(report["recurring_findings"],1)
            self.assertEqual(report["new_findings"],1)
            self.assertEqual(len(report["resolved_findings"]),1)
            self.assertEqual(report["resolved_findings"][0]["comparison"],"resolved")

    def test_older_run_cannot_replace_newer_latest_pointer(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            self.run_report(root,"on_repo","newer",50,1,{})
            older=self.run_report(root,"on_repo","older",49,1,{})
            index=json.loads((root/".takeout"/"reports"/"index.json").read_text(encoding="utf-8"))
            self.assertEqual({row["run_id"] for row in index["runs"]},{"newer","older"})
            self.assertEqual(index["runs"][0]["run_id"],"newer")
            self.assertTrue((older/"integrity.json").is_file())


    def test_source_task_id_is_recorded_for_push_commit(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            record = {"path": "docs/a.md", "exit_code": 0, "violations": [], "count": 0}
            output = self.run_report(
                root, "on_repo", "901", 901, 1, {"a": record},
                status="Passed", task_id="20261127-090000", event="push",
            )
            report = json.loads((output / "report.json").read_text(encoding="utf-8"))
            self.assertEqual(report["source_task_id"], "20261127-090000")

    def test_scheduled_report_does_not_claim_a_task(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            record = {"path": "docs/a.md", "exit_code": 0, "violations": [], "count": 0}
            output = self.run_report(
                root, "on_repo", "902", 902, 1, {"a": record},
                status="Passed", task_id="20261127-090000", event="schedule",
            )
            report = json.loads((output / "report.json").read_text(encoding="utf-8"))
            self.assertIsNone(report["source_task_id"])


if __name__=="__main__":
    unittest.main()
