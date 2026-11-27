#!/usr/bin/env python3
"""Regression tests for CI finding attribution and genuine-parent remediation."""
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("ledger.py")
SPEC = importlib.util.spec_from_file_location("ci_issue_ledger", SCRIPT)
LEDGER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(LEDGER)
SCHEMA_SOURCE = SCRIPT.parents[1] / "ledger-schema.json"
TASK_TEMPLATE_SOURCE = SCRIPT.parents[4] / "workspace" / "TASK_TEMPLATE.md"
SUBTASK_TEMPLATE_SOURCE = SCRIPT.parents[4] / "workspace" / "SUBTASK_TEMPLATE.md"
TASK_BOARD_SOURCE = SCRIPT.parents[4] / "workspace" / "task_board.md"

NOW = "2026-11-27T10:00:00Z"
PARENT_ID = "20261127-090000"


class LedgerAttributionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        triage = self.root / ".takeout" / "reports" / "triage"
        triage.mkdir(parents=True)
        shutil.copyfile(SCHEMA_SOURCE, triage / "ledger-schema.json")
        workspace = self.root / "workspace"
        (workspace / "tasks").mkdir(parents=True)
        shutil.copyfile(TASK_TEMPLATE_SOURCE, workspace / "TASK_TEMPLATE.md")
        shutil.copyfile(SUBTASK_TEMPLATE_SOURCE, workspace / "SUBTASK_TEMPLATE.md")
        shutil.copyfile(TASK_BOARD_SOURCE, workspace / "task_board.md")
        self.add_parent(PARENT_ID)
        self.write_ledger()

    def tearDown(self):
        self.temp.cleanup()

    def add_parent(self, task_id, status="In Progress", origin="User", priority="P1", governing="None"):
        folder = self.root / "workspace" / "tasks" / task_id
        subtasks = folder / "subtasks"
        subtasks.mkdir(parents=True, exist_ok=True)
        (subtasks / "README.md").write_text(
            "# Subtasks — " + task_id + "\n\nParent: [task.md](../task.md)\n",
            encoding="utf-8",
        )
        content = (
            "# Task: Genuine user task\n\n## Metadata\n\n"
            "- **ID:** " + task_id + "\n"
            "- **Status:** " + status + "\n"
            "- **Origin:** " + origin + "\n"
            "- **Priority:** " + priority + "\n"
            "- **Governing ADR(s):** " + governing + "\n"
            "- **Updated:** 2026-11-27 09:00 UTC\n"
            "- **Approval:** Approved\n\n"
            "## 10. Ledger Findings\n\n"
            "| Finding ID | Severity | Diagnostic | Evidence |\n"
            "|---|---|---|---|\n"
        )
        (folder / "task.md").write_text(content, encoding="utf-8")
        return folder

    def add_child(self, parent_id, child_id, filename="01-user-follow-up.md", status="Done"):
        path = self.root / "workspace" / "tasks" / parent_id / "subtasks" / filename
        path.write_text(
            "# Subtask: User follow-up\n\n"
            "## Metadata\n\n"
            "- **ID:** " + child_id + "\n"
            "- **Parent Task ID:** " + parent_id + "\n"
            "- **Status:** " + status + "\n"
            "- **Origin:** User\n"
            "- **Priority:** P2\n"
            "- **Ledger group:** None\n",
            encoding="utf-8",
        )
        return path

    def write_ledger(self, version="1.8.0", findings=None, baselines=None):
        payload = {
            "schema_version": version,
            "updated_at_utc": None,
            "findings": findings or [],
            "ingestion_state": {
                "bootstrap_at_utc": "2026-11-27T00:00:00Z",
                "processed_reports": [],
                "lint_baseline_scopes": baselines or {"on_changed": True, "on_repo": True},
            },
        }
        path = self.root / ".takeout" / "reports" / "triage" / "ledger.json"
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        return path

    def read_ledger(self):
        path = self.root / ".takeout" / "reports" / "triage" / "ledger.json"
        return json.loads(path.read_text(encoding="utf-8"))

    def read_index(self, path):
        if path.is_file():
            return json.loads(path.read_text(encoding="utf-8"))
        return {"schema_version": "1.1.0", "runs": []}

    def add_lint(
        self, run_id, timestamp=NOW, source_task_id=PARENT_ID, findings=None,
        scope="on_repo", checks=None, status="Failed", execution_mode=None,
    ):
        scope_folder = self.root / ".takeout" / "reports" / "lint_reports" / scope
        history = scope_folder / "history" / (str(run_id) + "-attempt-1")
        history.mkdir(parents=True, exist_ok=True)
        default_findings = [{
            "file": "docs/example.md", "line": 5, "col": 2,
            "rule": "semicolon", "level": "hard", "message": "Split this sentence.",
            "fingerprint": "a1b2c3d4e5f6", "comparison": "new",
        }]
        report = {
            "schema_version": "1.1.0",
            "scope": scope,
            "source_task_id": source_task_id,
            "run_id": str(run_id),
            "attempt": 1,
            "run_url": "https://example.invalid/actions/runs/" + str(run_id),
            "generated_at_utc": timestamp,
            "status": status,
            "execution_mode": execution_mode or ("repository-wide" if scope == "on_repo" else "full-audit-fallback"),
            "commit_sha": "a" * 40,
            "findings": default_findings if findings is None else findings,
            "checks": checks if checks is not None else [
                {"name": name, "status": "Passed", "exit_code": 0, "output": ""}
                for name in LEDGER.LINT_TOOLING_CHECKS
            ],
        }
        (history / "report.json").write_text(json.dumps(report), encoding="utf-8")
        index_path = scope_folder / "index.json"
        index = self.read_index(index_path)
        index["runs"].append({
            "run_id": str(run_id), "attempt": 1, "generated_at_utc": timestamp,
            "status": status,
        })
        index_path.write_text(json.dumps(index, indent=2), encoding="utf-8")
        return history / "report.json"

    def add_actions(
        self, run_id, timestamp=NOW, issues=None, task_message=None,
        source_status="completed", completeness="Complete", stage="post_run",
        conclusion="failure", source_event="push",
    ):
        workflow_id = 55
        history_relative = "history/" + str(workflow_id) + "/" + str(run_id) + "-attempt-1-" + stage
        history = self.root / ".takeout" / "reports" / "gh_ac_reports" / history_relative
        history.mkdir(parents=True, exist_ok=True)
        report = {
            "schema_version": "1.0.0",
            "source_run": {
                "id": str(run_id), "number": int(run_id), "attempt": 1,
                "workflow_id": workflow_id, "workflow_name": "Example CI",
                "workflow_path": ".github/workflows/example.yml",
                "run_url": "https://example.invalid/actions/runs/" + str(run_id),
                "status": source_status, "conclusion": conclusion, "event": source_event,
                "head_sha": "b" * 40,
                "head_commit_message": task_message,
            },
            "capture": {
                "stage": stage, "captured_at_utc": timestamp,
                "completeness": completeness, "reporter_job": None,
            },
            "classification": {
                "issues": issues if issues is not None else [{
                    "category": "validation_or_test", "job_id": "901",
                    "job_name": "Build", "step_name": "Run checks",
                    "blocking": True, "confidence": "high",
                    "message": "ERROR: test assertion failed",
                }],
            },
        }
        (history / "report.json").write_text(json.dumps(report), encoding="utf-8")
        index_path = self.root / ".takeout" / "reports" / "gh_ac_reports" / "index.json"
        index = self.read_index(index_path)
        index["runs"].append({
            "run_id": str(run_id), "attempt": 1, "workflow_id": workflow_id,
            "capture_stage": stage, "source_status": source_status,
            "report_status": "Complete" if completeness == "Complete" else "Incomplete",
            "captured_at_utc": timestamp, "history_path": history_relative,
        })
        index_path.parent.mkdir(parents=True, exist_ok=True)
        index_path.write_text(json.dumps(index, indent=2), encoding="utf-8")
        return history / "report.json"

    def child_files(self, parent_id=PARENT_ID):
        folder = self.root / "workspace" / "tasks" / parent_id / "subtasks"
        return sorted(path for path in folder.glob("[0-9][0-9]-*.md"))

    def ingest(self):
        return LEDGER.ingest(self.root, now=NOW)

    def test_missing_ledger_fails_closed(self):
        path = self.root / ".takeout" / "reports" / "triage" / "ledger.json"
        path.unlink()
        with self.assertRaises(LEDGER.LedgerError):
            self.ingest()
        self.assertFalse(path.exists())

    def test_missing_task_marker_keeps_finding_unassigned(self):
        self.add_lint("100", source_task_id=None)
        result = self.ingest()
        finding = self.read_ledger()["findings"][0]
        self.assertEqual(result["findings_created"], 1)
        self.assertEqual(result["subtasks_created"], 0)
        self.assertEqual(finding["task_refs"], [])
        self.assertEqual(finding["subtask_refs"], [])
        self.assertEqual(finding["evidence"][-1]["attribution_status"], "missing_marker")
        self.assertEqual(self.child_files(), [])

    def test_parent_task_marker_creates_ci_child_under_genuine_parent(self):
        board_before = (self.root / "workspace" / "task_board.md").read_text(encoding="utf-8")
        result = self.ingest_after_lint("101")
        ledger = self.read_ledger()
        finding = ledger["findings"][0]
        parent_path = self.root / "workspace" / "tasks" / PARENT_ID / "task.md"
        parent_content = parent_path.read_text(encoding="utf-8")
        child_files = self.child_files()
        self.assertEqual(result["tasks_created"], 0)
        self.assertEqual(result["subtasks_created"], 1)
        self.assertEqual(finding["task_refs"], [PARENT_ID])
        self.assertEqual(finding["subtask_refs"], [PARENT_ID + "-01"])
        self.assertIn(finding["finding_id"], parent_content)
        self.assertEqual(LEDGER.task_metadata(parent_content, "Priority"), "P1")
        self.assertEqual(len(list((self.root / "workspace" / "tasks").glob("*/task.md"))), 1)
        self.assertEqual(len(child_files), 1)
        child = child_files[0].read_text(encoding="utf-8")
        self.assertEqual(LEDGER.task_metadata(child, "ID"), PARENT_ID + "-01")
        self.assertEqual(LEDGER.task_metadata(child, "Parent Task ID"), PARENT_ID)
        self.assertEqual(LEDGER.task_metadata(child, "Priority"), "P0")
        self.assertEqual(LEDGER.task_metadata(child, "Status"), "Ready")
        self.assertEqual(LEDGER.task_metadata(child, "Approval"), "Approved")
        self.assertEqual(LEDGER.task_metadata(child, "Approval scope/source"), "Standing authorization for CI remediation.")
        self.assertEqual(LEDGER.task_metadata(child, "Eligibility / deferral reason"), "Eligible — no dependencies or unresolved decision gate.")
        self.assertNotIn("[Exact scope and authorization source]", child)
        self.assertNotIn("[Eligible or exact reason]", child)
        self.assertIn("## 10. Ledger Findings", child)
        self.assertIn(finding["finding_id"], child)
        self.assertEqual((self.root / "workspace" / "task_board.md").read_text(encoding="utf-8"), board_before)

    def ingest_after_lint(self, run_id, **kwargs):
        self.add_lint(run_id, **kwargs)
        return self.ingest()

    def test_child_task_marker_resolves_to_its_genuine_parent(self):
        child_id = PARENT_ID + "-01"
        self.add_child(PARENT_ID, child_id)
        self.ingest_after_lint("102", source_task_id=child_id)
        finding = self.read_ledger()["findings"][0]
        self.assertEqual(finding["task_refs"], [PARENT_ID])
        self.assertEqual(finding["subtask_refs"], [PARENT_ID + "-02"])
        self.assertEqual(len(self.child_files()), 2)

    def test_unknown_or_inactive_parent_never_creates_synthetic_task(self):
        self.add_lint("103", source_task_id="20261127-090001", findings=[{
            "file": "docs/a.md", "rule": "rule_a", "level": "hard", "message": "A",
            "fingerprint": "aaaaaaaa1111", "comparison": "new",
        }])
        self.add_parent("20261127-090002", status="Done")
        self.add_lint("104", source_task_id="20261127-090002", findings=[{
            "file": "docs/b.md", "rule": "rule_b", "level": "hard", "message": "B",
            "fingerprint": "bbbbbbbb2222", "comparison": "new",
        }])
        self.add_parent("20261127-090003", origin="Assistant")
        self.add_lint("105", source_task_id="20261127-090003", findings=[{
            "file": "docs/c.md", "rule": "rule_c", "level": "hard", "message": "C",
            "fingerprint": "cccccccc3333", "comparison": "new",
        }])
        self.ingest()
        findings = self.read_ledger()["findings"]
        self.assertEqual(len(findings), 3)
        self.assertTrue(all(not item["task_refs"] and not item["subtask_refs"] for item in findings))
        self.assertEqual(len(list((self.root / "workspace" / "tasks").glob("*/task.md"))), 3)

    def test_actions_commit_trailer_creates_child_under_originating_parent(self):
        message = "Implement task change.\n\nTask-ID: " + PARENT_ID + "\n"
        self.add_actions("200", task_message=message)
        result = self.ingest()
        finding = self.read_ledger()["findings"][0]
        self.assertEqual(result["subtasks_created"], 1)
        self.assertEqual(finding["task_refs"], [PARENT_ID])
        self.assertEqual(finding["evidence"][-1]["source_task_id"], PARENT_ID)
        self.assertEqual(finding["evidence"][-1]["source_commit_sha"], "b" * 40)

    def test_ambiguous_actions_task_trailers_remain_unassigned(self):
        message = (
            "Two unrelated task markers.\n\nTask-ID: " + PARENT_ID
            + "\nTask-ID: 20261127-090001\n"
        )
        self.add_actions("201", task_message=message)
        self.ingest()
        finding = self.read_ledger()["findings"][0]
        self.assertEqual(finding["task_refs"], [])
        self.assertEqual(finding["evidence"][-1]["attribution_status"], "ambiguous_marker")
        self.assertEqual(self.child_files(), [])

    def test_two_finding_groups_create_sibling_children_under_one_parent(self):
        findings = [
            {"file": "docs/example.md", "line": 5, "col": 2, "rule": "semicolon",
             "level": "hard", "message": "Split this sentence.", "fingerprint": "111111111111", "comparison": "new"},
            {"file": "docs/example.md", "line": 8, "col": 2, "rule": "passive_voice",
             "level": "advisory", "message": "Use active voice.", "fingerprint": "222222222222", "comparison": "new"},
        ]
        result = self.ingest_after_lint("202", findings=findings)
        ledger = self.read_ledger()
        self.assertEqual(result["subtasks_created"], 2)
        self.assertEqual(len(self.child_files()), 2)
        self.assertEqual(len(ledger["findings"]), 2)
        self.assertTrue(all(item["task_refs"] == [PARENT_ID] for item in ledger["findings"]))
        self.assertEqual(len({item["subtask_refs"][0] for item in ledger["findings"]}), 2)

    def test_repeated_reports_reuse_same_child_and_bound_evidence(self):
        for number in range(210, 217):
            self.ingest_after_lint(str(number), timestamp=NOW.replace("10:00", "10:" + str(number - 210).zfill(2)))
        finding = self.read_ledger()["findings"][0]
        self.assertEqual(finding["occurrence_count"], 7)
        self.assertEqual(len(finding["evidence"]), 5)
        self.assertEqual(finding["subtask_refs"], [PARENT_ID + "-01"])
        self.assertEqual(len(self.child_files()), 1)

    def test_latest_unattributed_observation_does_not_reuse_old_parent(self):
        self.ingest_after_lint("220", source_task_id=PARENT_ID)
        self.ingest_after_lint("221", source_task_id=None)
        finding = self.read_ledger()["findings"][0]
        self.assertEqual(finding["task_refs"], [PARENT_ID])
        self.assertEqual(finding["subtask_refs"], [PARENT_ID + "-01"])
        self.assertEqual(finding["evidence"][-1]["attribution_status"], "missing_marker")
        self.assertEqual(len(self.child_files()), 1)

    def test_lint_tooling_failure_is_a_finding_but_unattributed(self):
        checks = [
            {"name": name, "status": ("Failed" if name == "Markdown links and heading anchors" else "Passed"),
             "exit_code": (1 if name == "Markdown links and heading anchors" else 0), "output": "check"}
            for name in LEDGER.LINT_TOOLING_CHECKS
        ]
        self.add_lint("230", source_task_id=None, checks=checks)
        self.ingest()
        findings = self.read_ledger()["findings"]
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["category"], "lint_tooling")
        self.assertEqual(findings[0]["task_refs"], [])
        self.assertEqual(self.child_files(), [])

    def test_first_full_lint_report_seeds_baseline_without_findings(self):
        self.write_ledger(baselines={"on_changed": True, "on_repo": False})
        self.add_lint("240", source_task_id=PARENT_ID, execution_mode="repository-wide")
        self.ingest()
        ledger = self.read_ledger()
        self.assertEqual(ledger["findings"], [])
        self.assertTrue(ledger["ingestion_state"]["lint_baseline_scopes"]["on_repo"])

    def test_migration_preserves_verified_user_links_and_demotes_synthetic_refs(self):
        self.add_child(PARENT_ID, PARENT_ID + "-01")
        old_synthetic_id = "20261127-080000"
        finding = {
            "finding_id": "lint-aaaaaaaaaaaaaaaaaaaaaaaa",
            "source_family": "lint", "category": "semicolon", "title": "Finding",
            "status": "open", "severity": "medium", "owner": None,
            "first_seen_utc": NOW, "last_seen_utc": NOW, "occurrence_count": 2,
            "evidence": [{"report_path": ".takeout/reports/lint_reports/on_repo/history/90-attempt-1/report.json",
                          "observed_at_utc": NOW, "observation_id": "lint:90:1"}],
            "resolution": None, "resolution_history": [], "duplicate_of": None,
            "accepted_risk": None, "task_refs": [PARENT_ID, old_synthetic_id],
            "subtask_refs": [PARENT_ID + "-01", old_synthetic_id + "-01"],
            "legacy_task_refs": [], "task_group": "ci-aaaaaaaaaaaaaaaa",
            "parent_group": "ci-bbbbbbbbbbbbbbbb",
        }
        self.write_ledger(version="1.7.0", findings=[finding])
        migrated = LEDGER.migrate_ledger(self.read_ledger(), self.root)
        result = migrated["findings"][0]
        self.assertEqual(migrated["schema_version"], "1.8.0")
        self.assertEqual(result["task_refs"], [PARENT_ID])
        self.assertEqual(result["subtask_refs"], [PARENT_ID + "-01"])
        self.assertEqual(set(result["legacy_task_refs"]), {old_synthetic_id, old_synthetic_id + "-01"})
        self.assertEqual(result["occurrence_count"], 2)
        self.assertEqual(result["evidence"][0]["attribution_status"], "historical_unattributed")

    def test_resolution_reopens_with_history_and_new_attribution(self):
        self.ingest_after_lint("250")
        ledger = self.read_ledger()
        finding = ledger["findings"][0]
        finding["status"] = "resolved"
        finding["resolution"] = {
            "fix_commit": "c" * 40, "resolved_at_utc": NOW,
            "note": "Committed remediation.",
        }
        observation = {
            "finding_id": finding["finding_id"], "evidence": {
                "report_path": ".takeout/reports/lint_reports/on_repo/history/251-attempt-1/report.json",
                "run_url": None, "observed_at_utc": "2026-11-27T10:05:00Z",
                "note": "recurrence", "observation_id": "lint:251:1",
                "source_task_id": PARENT_ID, "parent_task_id": PARENT_ID,
                "attribution_status": "linked", "source_commit_sha": "d" * 40,
            },
        }
        result = LEDGER.upsert_finding(ledger, observation)
        self.assertEqual(result, "reopened")
        self.assertIsNone(finding["resolution"])
        self.assertEqual(len(finding["resolution_history"]), 1)
        self.assertEqual(finding["occurrence_count"], 2)

    def test_task_attribution_parser_rejects_multiple_or_malformed_markers(self):
        self.assertEqual(LEDGER.source_task_id_from_message("Subject\n\nTask-ID: " + PARENT_ID), (PARENT_ID, "present"))
        self.assertEqual(LEDGER.source_task_id_from_message("Task-ID: bad"), (None, "invalid_marker"))
        self.assertEqual(LEDGER.source_task_id_from_message("Task-ID: " + PARENT_ID + "\nTask-ID: " + PARENT_ID), (None, "ambiguous_marker"))
        self.assertEqual(LEDGER.source_task_id_from_message("No task marker"), (None, "missing_marker"))

    def test_incomplete_actions_capture_is_not_ingested(self):
        self.add_actions("260", task_message="Task-ID: " + PARENT_ID, completeness="Incomplete")
        result = self.ingest()
        self.assertEqual(result["reports_processed"], 0)
        self.assertEqual(self.read_ledger()["findings"], [])

    def test_atomic_write_replaces_file_without_temp_remnants(self):
        target = self.root / "atomic.txt"
        LEDGER.atomic_write_text(target, "written\n")
        self.assertEqual(target.read_text(encoding="utf-8"), "written\n")
        self.assertEqual(list(self.root.glob(".atomic.txt.*")), [])


    def test_repeated_actions_observations_reuse_one_child(self):
        message = "Fix task.\n\nTask-ID: " + PARENT_ID
        self.add_actions("270", task_message=message)
        self.ingest()
        self.add_actions("271", timestamp="2026-11-27T10:05:00Z", task_message=message)
        self.ingest()
        finding = self.read_ledger()["findings"][0]
        self.assertEqual(finding["occurrence_count"], 2)
        self.assertEqual(len(finding["evidence"]), 2)
        self.assertEqual(finding["task_refs"], [PARENT_ID])
        self.assertEqual(finding["subtask_refs"], [PARENT_ID + "-01"])
        self.assertEqual(len(self.child_files()), 1)

    def test_lint_tooling_repeat_across_scopes_reuses_one_child(self):
        checks = [
            {"name": name, "status": ("Failed" if name == "Markdown links and heading anchors" else "Passed"),
             "exit_code": (1 if name == "Markdown links and heading anchors" else 0), "output": "check"}
            for name in LEDGER.LINT_TOOLING_CHECKS
        ]
        self.add_lint("280", scope="on_repo", checks=checks)
        self.ingest()
        self.add_lint("281", scope="on_changed", timestamp="2026-11-27T10:05:00Z", checks=checks)
        self.ingest()
        finding = self.read_ledger()["findings"][0]
        self.assertEqual(finding["category"], "lint_tooling")
        self.assertEqual(finding["occurrence_count"], 2)
        self.assertEqual(len(finding["subtask_refs"]), 1)
        self.assertEqual(len(self.child_files()), 1)

    def test_processed_report_is_idempotent(self):
        self.add_lint("290")
        first = self.ingest()
        second = self.ingest()
        self.assertEqual(first["subtasks_created"], 1)
        self.assertEqual(second["reports_processed"], 0)
        self.assertEqual(len(self.child_files()), 1)
        self.assertEqual(self.read_ledger()["findings"][0]["occurrence_count"], 1)

    def test_untracked_recurring_lint_finding_is_suppressed(self):
        finding = {
            "file": "docs/example.md", "line": 5, "col": 2, "rule": "semicolon",
            "level": "hard", "message": "Split this sentence.",
            "fingerprint": "dddddddd4444", "comparison": "recurring",
        }
        self.add_lint("291", findings=[finding])
        self.ingest()
        self.assertEqual(self.read_ledger()["findings"], [])
        self.assertEqual(self.child_files(), [])

    def test_unknown_flat_task_record_does_not_become_parent(self):
        flat_id = "20261127-080000"
        flat = self.root / "workspace" / "tasks" / (flat_id + ".md")
        flat.write_text("# Legacy flat task\n\n- **ID:** " + flat_id + "\n- **Origin:** User\n- **Status:** In Progress\n", encoding="utf-8")
        self.add_lint("292", source_task_id=flat_id)
        self.ingest()
        finding = self.read_ledger()["findings"][0]
        self.assertEqual(finding["task_refs"], [])
        self.assertEqual(finding["subtask_refs"], [])
        self.assertEqual(len(list((self.root / "workspace" / "tasks").glob("*/task.md"))), 1)

    def test_scheduled_actions_run_is_unattributed(self):
        self.add_actions("293", task_message="Task-ID: " + PARENT_ID, source_event="schedule")
        self.ingest()
        finding = self.read_ledger()["findings"][0]
        self.assertEqual(finding["task_refs"], [])
        self.assertEqual(finding["evidence"][-1]["attribution_status"], "unsupported_event")
        self.assertEqual(self.child_files(), [])

    def test_malformed_report_remains_unprocessed(self):
        report = self.add_lint("294")
        report.write_text("{ malformed json", encoding="utf-8")
        result = self.ingest()
        self.assertEqual(len(result["errors"]), 1)
        self.assertNotIn(
            ".takeout/reports/lint_reports/on_repo/history/294-attempt-1/report.json",
            self.read_ledger()["ingestion_state"]["processed_reports"],
        )
        self.assertEqual(self.read_ledger()["findings"], [])

    def test_missing_indexed_report_fails_closed(self):
        report = self.add_lint("295")
        report.unlink()
        with self.assertRaises(LEDGER.LedgerError):
            self.ingest()
        self.assertEqual(self.read_ledger()["findings"], [])

    def test_human_managed_finding_fields_survive_recurrence(self):
        self.ingest_after_lint("296")
        ledger = self.read_ledger()
        finding = ledger["findings"][0]
        finding["status"] = "accepted"
        finding["severity"] = "low"
        finding["owner"] = "Human owner"
        finding["accepted_risk"] = {
            "rationale": "Known risk.", "accepted_by": "User", "accepted_at_utc": NOW,
            "expires_at_utc": None,
        }
        observation = {
            "finding_id": finding["finding_id"],
            "evidence": {
                "report_path": ".takeout/reports/lint_reports/on_repo/history/297-attempt-1/report.json",
                "run_url": None, "observed_at_utc": "2026-11-27T10:05:00Z",
                "note": "recurrence", "observation_id": "lint:297:1",
                "source_task_id": PARENT_ID, "parent_task_id": PARENT_ID,
                "attribution_status": "linked", "source_commit_sha": "d" * 40,
            },
        }
        LEDGER.upsert_finding(ledger, observation)
        self.assertEqual(finding["status"], "accepted")
        self.assertEqual(finding["severity"], "low")
        self.assertEqual(finding["owner"], "Human owner")
        self.assertEqual(finding["accepted_risk"]["rationale"], "Known risk.")

    def test_resolved_finding_needs_commit_but_not_hosted_validation(self):
        self.ingest_after_lint("298")
        ledger = self.read_ledger()
        finding = ledger["findings"][0]
        finding["status"] = "resolved"
        finding["resolution"] = {"fix_commit": "e" * 40, "resolved_at_utc": NOW, "note": "Fixed."}
        LEDGER.validate_semantics(ledger)
        finding["resolution"].pop("fix_commit")
        with self.assertRaises(LEDGER.LedgerError):
            LEDGER.validate_semantics(ledger)

    def test_diagnostic_markdown_is_escaped_in_task_summary(self):
        malicious = {
            "file": "docs/example.md", "line": 5, "col": 2, "rule": "semicolon",
            "level": "hard", "message": "[open](https://attacker.invalid)",
            "fingerprint": "eeeeeeee5555", "comparison": "new",
        }
        self.ingest_after_lint("299", findings=[malicious])
        child = self.child_files()[0].read_text(encoding="utf-8")
        self.assertIn("\\[open\\]", child)
        self.assertNotIn("[open](", child)


if __name__ == "__main__":
    unittest.main()
