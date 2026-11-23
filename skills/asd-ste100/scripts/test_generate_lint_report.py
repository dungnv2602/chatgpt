#!/usr/bin/env python3
"""Hosted regression tests for the lint evidence report generator."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("generate_lint_report.py")

class ReportGeneratorTests(unittest.TestCase):
    def run_report(self, root, run_id, attempt, records, previous=""):
        records_dir = root / ("records-" + run_id + "-" + str(attempt))
        records_dir.mkdir()
        for name, value in records.items():
            (records_dir / (name + ".json")).write_text(json.dumps(value), encoding="utf-8")
        output = root / "on_changed" / "history" / (run_id + "-attempt-" + str(attempt))
        command = [
            sys.executable, str(SCRIPT), "--scope", "on_changed",
            "--records-dir", str(records_dir), "--output-dir", str(output),
            "--run-id", run_id, "--run-number", "1",
            "--run-url", "https://example.invalid/run/" + run_id,
            "--attempt", str(attempt), "--branch", "gpt", "--commit", "abc123",
            "--event", "push", "--mode", "incremental", "--baseline", "base123",
            "--status", "Passed",
        ]
        if previous:
            command += ["--previous-report", previous]
        subprocess.run(command, check=True, capture_output=True, text=True)
        return output

    def test_structured_findings_fingerprints_and_latest_pointer(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            finding = {"rule": "semicolon", "match": ";", "message": "Split sentence.", "line": 3, "col": 8, "level": "advisory-free"}
            record = {"path": "docs/a.md", "exit_code": 0, "violations": [finding], "count": 1, "hard_count": 1, "words": 20}
            first = self.run_report(root, "100", 1, {"a": record})
            report = json.loads((first / "report.json").read_text(encoding="utf-8"))
            self.assertEqual(report["files_evaluated"], 1)
            self.assertEqual(report["total_findings"], 1)
            self.assertTrue(report["findings"][0]["fingerprint"])
            self.assertEqual(report["findings"][0]["comparison"], "new")
            latest = root / "on_changed" / "latest-lint-report.json"
            self.assertEqual(json.loads(latest.read_text(encoding="utf-8"))["run_id"], "100")

    def test_baseline_comparison_and_attempt_history(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            first_record = {"path": "docs/a.md", "exit_code": 0, "violations": [
                {"rule": "semicolon", "match": ";", "message": "Split sentence.", "line": 3, "col": 8}
            ], "count": 1, "hard_count": 1, "words": 20}
            first = self.run_report(root, "200", 1, {"a": first_record})
            previous = str(first / "report.json")
            second_record = {"path": "docs/a.md", "exit_code": 0, "violations": [
                {"rule": "semicolon", "match": ";", "message": "Split sentence.", "line": 9, "col": 8},
                {"rule": "long-sentence", "match": "26 words", "message": "Split it.", "line": 12, "col": 1}
            ], "count": 2, "hard_count": 2, "words": 30}
            second = self.run_report(root, "201", 1, {"a": second_record}, previous)
            report = json.loads((second / "report.json").read_text(encoding="utf-8"))
            self.assertEqual(report["recurring_findings"], 1)
            self.assertEqual(report["new_findings"], 1)
            self.assertEqual(report["resolved_findings"], 0)
            index = json.loads((root / "on_changed" / "index.json").read_text(encoding="utf-8"))
            self.assertEqual(len(index["runs"]), 2)
            self.assertTrue((root / "on_changed" / "latest-lint-report.md").is_file())

if __name__ == "__main__":
    unittest.main()
