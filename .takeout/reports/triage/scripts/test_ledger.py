#!/usr/bin/env python3
"""Hosted regression tests for the central CI issue ledger."""
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
TASK_BOARD_SOURCE = SCRIPT.parents[4] / "workspace" / "task_board.md"

class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        triage = self.root / ".takeout" / "reports" / "triage"
        triage.mkdir(parents=True)
        shutil.copyfile(SCHEMA_SOURCE, triage / "ledger-schema.json")
        workspace = self.root / "workspace"
        (workspace / "tasks").mkdir(parents=True)
        shutil.copyfile(TASK_TEMPLATE_SOURCE, workspace / "TASK_TEMPLATE.md")
        board_copy = workspace / "task_board.md"
        shutil.copyfile(TASK_BOARD_SOURCE, board_copy)
        board_text = board_copy.read_text(encoding="utf-8")
        if "\\n" in board_text:
            board_copy.write_text(board_text.replace("\\n", "\n"), encoding="utf-8")
        self.write_ledger()

    def tearDown(self):
        self.temp.cleanup()

    def write_ledger(self, version="1.5.0", findings=None):
        payload = {"schema_version": version, "updated_at_utc": None, "findings": findings or []}
        if version in ("1.1.0", "1.2.0", "1.3.0", "1.4.0", "1.5.0"):
            payload["ingestion_state"] = {
                "bootstrap_at_utc":"2026-11-23T07:00:00Z","processed_reports":[],
                "lint_baseline_scopes":{"on_changed":True,"on_repo":True},
            }
        path = self.root / ".takeout" / "reports" / "triage" / "ledger.json"
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        return path

    def add_lint(self, scope, run_id, timestamp, fingerprint="a1b2c3d4e5f6", status="Failed",
                 level="advisory-free", file_path="docs/example.md", rule="semicolon",
                 message="Split this sentence.", comparison="new", execution_mode="full-audit-fallback"):
        folder = self.root / ".takeout" / "reports" / "lint_reports" / scope
        history = folder / "history" / (run_id + "-attempt-1")
        history.mkdir(parents=True, exist_ok=True)
        report_path = history / "report.json"
        report = {
            "schema_version":"1.1.0","scope":scope,"run_id":run_id,"attempt":1,
            "run_url":"https://example.invalid/actions/runs/" + run_id,
            "generated_at_utc":timestamp,"status":status,"execution_mode":execution_mode,
            "commit_sha":"a"*40,"files_evaluated_count":1,
            "checks":[
                {"name":"Wrapper shell syntax","status":"Passed"},
                {"name":"Python report tooling compilation","status":"Passed"},
                {"name":"Lint report regression tests","status":"Passed"},
                {"name":"Markdown anchor regression tests","status":"Passed"},
                {"name":"STE linter self-test","status":"Passed"},
                {"name":"Markdown links and heading anchors","status":"Passed"},
            ],
            "findings":[{
                "file":file_path,"line":5,"col":2,"rule":rule,"level":level,
                "message":message,"fingerprint":fingerprint,"comparison":comparison,
            }],
        }
        report_path.write_text(json.dumps(report), encoding="utf-8")
        index_path = folder / "index.json"
        rows = json.loads(index_path.read_text())["runs"] if index_path.exists() else []
        rows.append({"run_id":run_id,"attempt":1,"generated_at_utc":timestamp})
        index_path.write_text(json.dumps({"schema_version":"1.1.0","runs":rows}), encoding="utf-8")
        return report_path.relative_to(self.root).as_posix()

    def add_actions(self, run_id, timestamp, issues, stage="post_run", completeness="Complete", conclusion="failure"):
        history = self.root / ".takeout" / "reports" / "gh_ac_reports" / "history" / "55" / (run_id + "-attempt-1-" + stage)
        history.mkdir(parents=True, exist_ok=True)
        report_path = history / "report.json"
        report = {
            "schema_version":"1.0.0",
            "source_run":{
                "id":run_id,"number":int(run_id),"attempt":1,"workflow_id":55,
                "workflow_name":"Example CI","workflow_path":".github/workflows/example.yml",
                "run_url":"https://example.invalid/actions/runs/" + run_id,"status":"completed","conclusion":conclusion,
            },
            "capture":{"stage":stage,"captured_at_utc":timestamp,"completeness":completeness,"reporter_job":None},
            "classification":{"issues":issues},
        }
        report_path.write_text(json.dumps(report), encoding="utf-8")
        index_path = self.root / ".takeout" / "reports" / "gh_ac_reports" / "index.json"
        rows = json.loads(index_path.read_text())["runs"] if index_path.exists() else []
        rows.append({
            "run_id":run_id,"attempt":1,"workflow_id":55,"capture_stage":stage,
            "captured_at_utc":timestamp,"history_path":history.relative_to(index_path.parent).as_posix(),
        })
        index_path.write_text(json.dumps({"schema_version":"1.0.0","runs":rows}), encoding="utf-8")
        return report_path.relative_to(self.root).as_posix()

    def read_ledger(self):
        return json.loads((self.root / ".takeout" / "reports" / "triage" / "ledger.json").read_text())

    def test_missing_ledger_fails_closed_without_automatic_reset(self):
        path = self.root / ".takeout" / "reports" / "triage" / "ledger.json"
        path.unlink()
        with self.assertRaisesRegex(LEDGER.LedgerError, "explicit user authorization"):
            LEDGER.ingest(self.root)
        self.assertFalse(path.exists())

    def test_legacy_report_paths_migrate_to_repository_relative_roots(self):
        finding = {
            "finding_id":"lint-a1b2c3d4e5f6","source_family":"lint","category":"semicolon","title":"A finding",
            "status":"open","severity":"low","first_seen_utc":"2026-11-23T07:00:00Z",
            "last_seen_utc":"2026-11-23T07:00:00Z","occurrence_count":1,
            "evidence":[
                {"report_path":"reports/lint_reports/on_repo/history/1-attempt-1/report.json",
                 "observed_at_utc":"2026-11-23T07:00:00Z","observation_id":"lint:1:1"},
                {"report_path":"archive/reports/triage/old-report.json",
                 "observed_at_utc":"2026-11-23T07:01:00Z","observation_id":"lint:1:2"},
            ],
        }
        legacy = {
            "schema_version":"1.4.0","updated_at_utc":None,"findings":[finding],
            "ingestion_state":{
                "bootstrap_at_utc":"2026-11-23T07:00:00Z",
                "processed_reports":["reports/lint_reports/on_repo/history/1-attempt-1/report.json"],
                "lint_baseline_scopes":{"on_changed":True,"on_repo":True},
            },
        }
        migrated = LEDGER.migrate_ledger(legacy, self.root)
        self.assertEqual(migrated["schema_version"],"1.5.0")
        self.assertEqual(
            [item["report_path"] for item in migrated["findings"][0]["evidence"]],
            [".takeout/reports/lint_reports/on_repo/history/1-attempt-1/report.json",
             ".archive/reports/triage/old-report.json"],
        )
        self.assertEqual(
            migrated["ingestion_state"]["processed_reports"],
            [".takeout/reports/lint_reports/on_repo/history/1-attempt-1/report.json"],
        )

    def test_lint_fingerprint_deduplicates_across_scopes_and_is_idempotent(self):
        self.add_lint("on_changed","100","2026-11-23T07:10:00Z")
        self.add_lint("on_repo","100","2026-11-23T07:11:00Z")
        first = LEDGER.ingest(self.root, now="2026-11-23T07:12:00Z")
        finding = self.read_ledger()["findings"][0]
        self.assertEqual(first["findings_created"],1)
        self.assertEqual(finding["finding_id"],"lint-a1b2c3d4e5f6")
        self.assertEqual(finding["occurrence_count"],1)
        self.assertEqual(len(finding["task_refs"]), 1)
        self.assertEqual(len(finding["evidence"]),2)
        task_files = list((self.root / "workspace" / "tasks").glob("*.md"))
        self.assertEqual(len(task_files), 1)
        self.assertIn("- **Status:** Proposed", task_files[0].read_text(encoding="utf-8"))
        self.assertIn(finding["finding_id"], task_files[0].read_text(encoding="utf-8"))
        self.assertIn("[report](../../.takeout/reports/lint_reports/on_changed/history/100-attempt-1/report.json)", task_files[0].read_text(encoding="utf-8"))
        self.assertIn("../../.takeout/reports/triage/ledger.json", task_files[0].read_text(encoding="utf-8"))
        self.assertIn("- **Template version:** 1.3", task_files[0].read_text(encoding="utf-8"))
        self.assertIn("- **Governing ADR(s):** Pending — Worker review required before approval", task_files[0].read_text(encoding="utf-8"))
        self.assertIn("1. Inspect every linked report and exact diagnostic before proposing a fix.", task_files[0].read_text(encoding="utf-8"))
        self.assertNotIn("[List agreed requirements and acceptance criteria.", task_files[0].read_text(encoding="utf-8"))
        self.assertIn("- **Standing instruction:**", task_files[0].read_text(encoding="utf-8"))
        self.assertIn("- **Standing approval:** CI Ledger-generated remediation is approved under the user's permanent P0 instruction.", task_files[0].read_text(encoding="utf-8"))
        self.assertNotIn("[Record approved decisions and concise rationale.", task_files[0].read_text(encoding="utf-8"))
        self.assertNotIn("[Preserve relevant user clarifications", task_files[0].read_text(encoding="utf-8"))
        self.assertIn(f"| {finding['task_refs'][0]} |", (self.root / "workspace" / "task_board.md").read_text(encoding="utf-8"))
        self.assertIn("| Pending user approval | Pending |", (self.root / "workspace" / "task_board.md").read_text(encoding="utf-8"))
        second = LEDGER.ingest(self.root, now="2026-11-23T07:13:00Z")
        self.assertFalse(second["changed"])
        self.assertEqual(self.read_ledger()["findings"][0]["occurrence_count"],1)

    def test_task_board_rows_stay_inside_their_status_section(self):
        self.add_lint("on_changed", "109", "2026-11-23T07:09:00Z", level="advisory")
        LEDGER.ingest(self.root, now="2026-11-23T07:10:00Z")
        board = (self.root / "workspace" / "task_board.md").read_text(encoding="utf-8")
        proposed_start = board.index("## Proposed")
        paused_start = board.index("## Paused", proposed_start)
        historical_start = board.index("## Historical", paused_start)
        proposed_section = board[proposed_start:paused_start]
        historical_section = board[historical_start:]
        self.assertIn("| 20261123-071000 |", proposed_section)
        self.assertNotIn("| 20261123-071000 |", historical_section)

    def test_task_board_renderer_fails_closed_when_status_table_is_missing(self):
        board_path = self.root / "workspace" / "task_board.md"
        board = board_path.read_text(encoding="utf-8")
        proposed_start = board.index("## Proposed\n") + len("## Proposed\n")
        ready_start = board.index("## Ready\n", proposed_start)
        board = board[:proposed_start] + board[ready_start:]
        board_path.write_text(board, encoding="utf-8")
        task_path = self.root / "workspace" / "tasks" / "test-proposed-task.md"
        task_content = (
            "# Task: Proposed renderer test\n\n"
            "- **ID:** test-proposed-task\n"
            "- **Priority:** P3\n"
            "- **Status:** Proposed\n"
            "- **Origin:** Assistant\n"
            "- **Updated:** 2026-11-24 08:10 UTC\n"
        )
        task_path.write_text(task_content, encoding="utf-8")
        with self.assertRaises(LEDGER.LedgerError):
            LEDGER.upsert_task_board_row(
                self.root, {"id": "test-proposed-task", "path": task_path, "content": task_content}
            )
        self.assertNotIn("| test-proposed-task |", board_path.read_text(encoding="utf-8"))

    def test_new_task_record_is_rolled_back_when_board_publication_fails(self):
        board_path = self.root / "workspace" / "task_board.md"
        board = board_path.read_text(encoding="utf-8")
        proposed_start = board.index("## Proposed\n") + len("## Proposed\n")
        ready_start = board.index("## Ready\n", proposed_start)
        board = board[:proposed_start] + board[ready_start:]
        board_path.write_text(board, encoding="utf-8")
        finding = {
            "finding_id": "test-finding", "source_family": "lint", "category": "test",
            "severity": "medium", "status": "open", "task_group": "ci-0123456789abcdef",
            "evidence": [{"note": "docs/example.md"}], "task_refs": [],
        }
        with self.assertRaises(LEDGER.LedgerError):
            LEDGER.create_or_update_worker_task(
                self.root, finding["task_group"], [finding], "2026-11-26T08:12:00Z", {}
            )
        self.assertEqual(list((self.root / "workspace" / "tasks").glob("*.md")), [])
        self.assertNotIn("test-finding", board_path.read_text(encoding="utf-8"))

    def test_all_lint_severities_create_and_reuse_grouped_tasks(self):
        self.add_lint("on_changed", "110", "2026-11-23T07:10:00Z",
                      fingerprint="a1b2c3d4e5f6", level="advisory",
                      file_path="docs/advisory.md", rule="passive-voice")
        first = LEDGER.ingest(self.root, now="2026-11-23T07:11:00Z")
        self.assertEqual(first["tasks_created"], 1)
        first_finding = self.read_ledger()["findings"][0]
        self.assertEqual(first_finding["severity"], "low")
        task_id = first_finding["task_refs"][0]

        self.add_lint("on_changed", "111", "2026-11-23T07:12:00Z",
                      fingerprint="b2c3d4e5f6a7", level="unknown",
                      file_path="docs/advisory.md", rule="passive-voice")
        second = LEDGER.ingest(self.root, now="2026-11-23T07:13:00Z")
        findings = self.read_ledger()["findings"]
        self.assertEqual(second["tasks_created"], 0)
        self.assertEqual(second["tasks_updated"], 1)
        self.assertEqual(len(findings), 2)
        self.assertTrue(all(item["task_refs"] == [task_id] for item in findings))
        self.assertEqual({item["severity"] for item in findings}, {"low", "informational"})
        task_files = list((self.root / "workspace" / "tasks").glob("*.md"))
        self.assertEqual(len(task_files), 1)
        task_text = task_files[0].read_text(encoding="utf-8")
        self.assertIn("- **Priority:** P3", task_text)
        self.assertIn("lint-a1b2c3d4e5f6", task_text)
        self.assertIn("lint-b2c3d4e5f6a7", task_text)

    def test_low_confidence_actions_findings_remain_ledger_only(self):
        issue = {
            "category": "step_failure", "job_name": "build", "step_name": "optional check",
            "confidence": "low", "blocking": False,
            "diagnostic": "Optional check failed with a classified diagnostic.",
        }
        self.add_actions("112", "2026-11-23T07:20:00Z", [issue])
        result = LEDGER.ingest(self.root, now="2026-11-23T07:21:00Z")
        findings = self.read_ledger()["findings"]
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["source_family"], "github_actions")
        self.assertEqual(findings[0]["severity"], "low")
        self.assertEqual(findings[0]["task_refs"], [])
        self.assertEqual(result["tasks_created"], 0)

    def test_lint_new_run_increments_occurrence_and_tracks_dates(self):
        self.add_lint("on_changed","100","2026-11-23T07:10:00Z")
        LEDGER.ingest(self.root)
        self.add_lint("on_changed","101","2026-11-23T07:20:00Z")
        LEDGER.ingest(self.root)
        finding = self.read_ledger()["findings"][0]
        self.assertEqual(finding["occurrence_count"],2)
        self.assertEqual(len(list((self.root / "workspace" / "tasks").glob("*.md"))), 1)
        self.assertEqual(finding["first_seen_utc"],"2026-11-23T07:10:00Z")
        self.assertEqual(finding["last_seen_utc"],"2026-11-23T07:20:00Z")

    def test_runner_command_echo_uses_actual_step_log_signature(self):
        report_path = ".takeout/reports/gh_ac_reports/history/55/900-attempt-1-post_run/report.json"
        report_dir = self.root / Path(report_path).parent
        log_dir = report_dir / "logs"
        log_dir.mkdir(parents=True)
        log_path = log_dir / "job-901.log"
        log_path.write_text(
            "Build\tPublish\t2026-11-23T07:00:00Z\t^[[36;1m git push origin gpt\n"
            "Build\tPublish\t2026-11-23T07:00:01Z\t! [remote rejected] HEAD -> gpt (cannot lock ref abcdef1234567)\n"
            "Build\tPublish\t2026-11-23T07:00:02Z\terror: failed to push some refs\n",
            encoding="utf-8",
        )
        report = {"jobs":[{"id":"901","name":"Build","log_capture":{"path":"logs/job-901.log"}}]}
        issue = {"job_id":"901","job_name":"Build","step_name":"Publish",
                 "message":"2026-11-23T07:00:00Z ^[[36;1m git push origin gpt"}
        signature = LEDGER.diagnostic_signature(report, report_path, self.root, issue)
        self.assertIn("remote rejected", signature)
        self.assertIn("failed to push some refs", signature)
        self.assertNotIn("^[[", signature)
        self.assertNotIn("abcdef1234567", LEDGER.normalize_signature(signature))

    def test_actions_identity_uses_workflow_job_step_and_signature(self):
        issues = [
            {"category":"validation_or_test","job_name":"Build","step_name":"Unit tests","blocking":True,"confidence":"high","message":"ERROR: mismatch abcdef1234567\n"},
            {"category":"validation_or_test","job_name":"Build","step_name":"Unit tests","blocking":True,"confidence":"high","message":" error:   mismatch 7654321 "},
            {"category":"validation_or_test","job_name":"Build","step_name":"Publish","blocking":True,"confidence":"high","message":"ERROR: mismatch abcdef1234567"},
            {"category":"validation_or_test","job_name":"Build","step_name":"Unit tests","blocking":True,"confidence":"high","message":"ERROR: different assertion"},
        ]
        self.add_actions("200","2026-11-23T07:30:00Z",issues)
        result = LEDGER.ingest(self.root)
        findings = self.read_ledger()["findings"]
        self.assertEqual(result["findings_created"],3)
        self.assertEqual(len(findings),3)
        self.assertTrue(all(item["source_family"] == "github_actions" for item in findings))
        self.assertEqual(result["tasks_created"], 2)
        refs = [item["task_refs"][0] for item in findings]
        unit_test_refs = [item["task_refs"][0] for item in findings if "Unit tests" in item["evidence"][0]["note"]]
        self.assertEqual(len(set(unit_test_refs)), 1)
        self.assertEqual(len(set(refs)), 2)
        self.assertEqual(len(list((self.root / "workspace" / "tasks").glob("*.md"))), 2)

    def test_cancelled_run_keeps_independent_failure_and_ignores_cancellation_propagation(self):
        issues = [
            {"category":"cancelled","job_name":"Build","step_name":"Cancel remaining work",
             "blocking":False,"confidence":"high","message":"Run cancelled."},
            {"category":"validation_or_test","job_name":"Build",
             "step_name":"Preserve lint failure as workflow conclusion",
             "blocking":True,"confidence":"medium","message":"Changed-document lint failed."},
            {"category":"validation_or_test","job_name":"Build","step_name":"Run unit tests",
             "blocking":True,"confidence":"high","message":"ERROR: assertion mismatch"},
        ]
        self.add_actions("203","2026-11-23T07:35:00Z",issues,conclusion="cancelled")
        result = LEDGER.ingest(self.root)
        findings = self.read_ledger()["findings"]
        self.assertEqual(result["total_findings"],1)
        self.assertEqual(result["reports_processed"],1)
        self.assertEqual(findings[0]["category"],"validation_or_test")
        self.assertEqual(findings[0]["occurrence_count"],1)

    def test_cancelled_only_report_creates_no_findings(self):
        issue = {"category":"cancelled","job_name":"Build","step_name":"Cancel remaining work",
                 "blocking":False,"confidence":"high","message":"Run cancelled."}
        self.add_actions("204","2026-11-23T07:36:00Z",[issue],conclusion="cancelled")
        result = LEDGER.ingest(self.root)
        self.assertEqual(result["total_findings"],0)

    def test_actions_repeat_observation_increments_once_per_run(self):
        issue = {"category":"validation_or_test","job_name":"Build","step_name":"Unit tests","blocking":True,"confidence":"medium","message":"Assertion mismatch"}
        self.add_actions("201","2026-11-23T07:30:00Z",[issue])
        LEDGER.ingest(self.root)
        self.add_actions("202","2026-11-23T07:40:00Z",[issue])
        LEDGER.ingest(self.root)
        finding = self.read_ledger()["findings"][0]
        self.assertEqual(finding["occurrence_count"],2)
        self.assertEqual(len(finding["evidence"]),2)
        self.assertEqual(len(finding["task_refs"]), 1)
        self.assertEqual(len(list((self.root / "workspace" / "tasks").glob("*.md"))), 1)
        task_text = next((self.root / "workspace" / "tasks").glob("*.md")).read_text(encoding="utf-8")
        self.assertIn("201-attempt-1-post_run/report.json", task_text)
        self.assertIn("202-attempt-1-post_run/report.json", task_text)

    def test_related_findings_reuse_one_active_task_across_ingestion_events(self):
        self.add_lint("on_changed", "210", "2026-11-23T07:30:00Z", fingerprint="aaaaaaaa1111")
        first = LEDGER.ingest(self.root, now="2026-11-23T07:31:00Z")
        self.assertEqual(first["tasks_created"], 1)
        first_ref = self.read_ledger()["findings"][0]["task_refs"][0]
        self.add_lint("on_changed", "211", "2026-11-23T07:40:00Z", fingerprint="bbbbbbbb2222")
        second = LEDGER.ingest(self.root, now="2026-11-23T07:41:00Z")
        findings = self.read_ledger()["findings"]
        self.assertEqual(second["tasks_created"], 0)
        self.assertEqual(second["tasks_updated"], 1)
        self.assertEqual({item["task_refs"][0] for item in findings}, {first_ref})
        self.assertEqual(len(list((self.root / "workspace" / "tasks").glob("*.md"))), 1)
        task_text = next((self.root / "workspace" / "tasks").glob("*.md")).read_text(encoding="utf-8")
        self.assertIn("lint-aaaaaaaa1111", task_text)
        self.assertIn("lint-bbbbbbbb2222", task_text)

    def test_later_high_severity_finding_promotes_active_group_priority(self):
        first_issue = {"category":"validation_or_test","job_name":"Build","step_name":"Unit tests",
                       "blocking":True,"confidence":"medium","message":"Assertion mismatch A"}
        self.add_actions("214","2026-11-23T07:57:00Z",[first_issue])
        LEDGER.ingest(self.root, now="2026-11-23T07:58:00Z")
        second_issue = {"category":"validation_or_test","job_name":"Build","step_name":"Unit tests",
                        "blocking":True,"confidence":"high","message":"Assertion mismatch B"}
        self.add_actions("215","2026-11-23T08:00:00Z",[second_issue])
        result = LEDGER.ingest(self.root, now="2026-11-23T08:01:00Z")
        task_files = list((self.root / "workspace" / "tasks").glob("*.md"))
        self.assertEqual(len(task_files), 1)
        task_text = task_files[0].read_text(encoding="utf-8")
        self.assertIn("- **Priority:** P1", task_text)
        self.assertEqual(result["tasks_updated"], 1)

    def test_untrusted_diagnostic_text_is_escaped_in_worker_task(self):
        self.add_lint("on_changed", "213", "2026-11-23T07:55:00Z",
                      message="<script>alert(1)</script> [follow](javascript:run())")
        LEDGER.ingest(self.root, now="2026-11-23T07:56:00Z")
        task = next((self.root / "workspace" / "tasks").glob("*.md")).read_text(encoding="utf-8")
        self.assertIn("\\<script\\>", task)
        self.assertIn("\\[follow\\]", task)
        self.assertIn("untrusted evidence", task)

    def test_low_severity_advisory_findings_create_p3_tasks(self):
        self.add_lint("on_changed", "212", "2026-11-23T07:50:00Z", level="advisory")
        result = LEDGER.ingest(self.root, now="2026-11-23T07:51:00Z")
        finding = self.read_ledger()["findings"][0]
        self.assertEqual(finding["severity"], "low")
        self.assertEqual(len(finding["task_refs"]), 1)
        self.assertEqual(result["tasks_created"], 1)
        task_files = list((self.root / "workspace" / "tasks").glob("*.md"))
        self.assertEqual(len(task_files), 1)
        task_text = task_files[0].read_text(encoding="utf-8")
        self.assertIn("- **Priority:** P3", task_text)
        self.assertIn("lint-", task_text)

    def test_resolved_finding_reopens_and_preserves_resolution_history(self):
        self.add_lint("on_changed","300","2026-11-23T07:10:00Z")
        LEDGER.ingest(self.root)
        path = self.root / ".takeout" / "reports" / "triage" / "ledger.json"
        ledger = json.loads(path.read_text())
        resolution = {
            "fix_commit":"abcdef1234567","resolved_at_utc":"2026-11-23T07:15:00Z",
            "validation":{"run_url":"https://example.invalid/actions/runs/9","conclusion":"success","validated_at_utc":"2026-11-23T07:14:00Z"},
            "note":"Verified the fix.",
        }
        ledger["findings"][0]["status"]="resolved"
        ledger["findings"][0]["resolution"]=resolution
        path.write_text(json.dumps(ledger),encoding="utf-8")
        self.add_lint("on_changed","301","2026-11-23T07:20:00Z")
        LEDGER.ingest(self.root)
        finding = self.read_ledger()["findings"][0]
        self.assertEqual(finding["status"],"open")
        self.assertIsNone(finding["resolution"])
        self.assertEqual(finding["resolution_history"],[resolution])
        self.assertEqual(finding["occurrence_count"],2)

    def test_curated_owner_severity_status_title_and_risk_are_preserved(self):
        finding = {
            "finding_id":"lint-a1b2c3d4e5f6","source_family":"lint","category":"old-rule","title":"Curated title",
            "status":"accepted","severity":"critical","owner":"Platform",
            "first_seen_utc":"2026-11-23T07:00:00Z","last_seen_utc":"2026-11-23T07:00:00Z",
            "occurrence_count":1,"evidence":[{"report_path":"reports/old/report.json","observed_at_utc":"2026-11-23T07:00:00Z","observation_id":"lint:old:1"}],
            "resolution":None,"resolution_history":[],"duplicate_of":None,
            "accepted_risk":{"rationale":"Known legacy debt","accepted_by":"Team","accepted_at_utc":"2026-11-23T07:00:00Z"},
            "task_refs":["20261123-100738"],
        }
        self.write_ledger(findings=[finding])
        self.add_lint("on_changed","400","2026-11-23T07:20:00Z")
        LEDGER.ingest(self.root)
        updated = self.read_ledger()["findings"][0]
        self.assertEqual(updated["title"],"Curated title")
        self.assertEqual(updated["category"],"old-rule")
        self.assertEqual(updated["status"],"accepted")
        self.assertEqual(updated["severity"],"critical")
        self.assertEqual(updated["owner"],"Platform")
        self.assertEqual(updated["accepted_risk"],finding["accepted_risk"])
        self.assertEqual(updated["task_refs"],["20261123-100738"])
        self.assertEqual(updated["evidence"][0]["report_path"],".takeout/reports/old/report.json")

    def test_non_defect_actions_and_pre_finalizer_reports_are_ignored(self):
        issues = [
            {"category":"cancelled","job_name":"Build","step_name":"Tests","blocking":True,"confidence":"high","message":"Cancelled"},
            {"category":"skipped","job_name":"Build","step_name":"Tests","blocking":False,"confidence":"high","message":"Skipped"},
            {"category":"validation_or_test","job_name":None,"step_name":None,"blocking":True,"confidence":"low","message":"GitHub reported a failed run, but no failed job or step was available."},
            {"category":"validation_or_test","job_name":"Build","step_name":"Preserve lint failure as workflow conclusion","blocking":True,"confidence":"medium","message":"Changed-document lint failed."},
        ]
        self.add_actions("500","2026-11-23T07:30:00Z",issues,stage="pre_finalizer")
        self.add_actions("501","2026-11-23T07:31:00Z",issues,stage="post_run")
        result = LEDGER.ingest(self.root)
        self.assertEqual(result["total_findings"],0)
        self.assertEqual(result["reports_processed"],2)

    def test_incomplete_lint_report_is_not_imported(self):
        self.add_lint("on_changed","600","2026-11-23T07:10:00Z",status="Incomplete")
        LEDGER.ingest(self.root)
        self.assertEqual(self.read_ledger()["findings"],[])

    def test_malformed_report_is_not_marked_processed(self):
        path = self.add_lint("on_changed","700","2026-11-23T07:10:00Z")
        (self.root / path).write_text("{broken",encoding="utf-8")
        result = LEDGER.ingest(self.root)
        self.assertEqual(result["reports_processed"],0)
        self.assertTrue(result["warnings"])
        self.assertNotIn(path,self.read_ledger()["ingestion_state"]["processed_reports"])

    def test_bootstrap_migration_does_not_backfill_existing_reports(self):
        path = self.add_lint("on_changed","800","2026-11-23T07:10:00Z")
        self.write_ledger(version="1.0.0")
        result = LEDGER.ingest(self.root)
        migrated = self.read_ledger()
        self.assertEqual(migrated["schema_version"],"1.5.0")
        self.assertEqual(migrated["findings"],[])
        self.assertIn(path,migrated["ingestion_state"]["processed_reports"])
        self.assertEqual(migrated["findings"],[])
        self.assertEqual(result["reports_processed"],0)
        self.assertTrue(migrated["updated_at_utc"])

    def test_migrate_1_1_hands_off_unlinked_lint_findings_at_all_severities(self):
        finding = {
            "finding_id":"lint-a1b2c3d4e5f6","source_family":"lint","category":"semicolon","title":"A finding",
            "status":"open","severity":"low","owner":None,
            "first_seen_utc":"2026-11-23T07:00:00Z","last_seen_utc":"2026-11-23T07:00:00Z",
            "occurrence_count":1,"evidence":[{"report_path":"reports/lint_reports/on_repo/history/1-attempt-1/report.json",
                "observed_at_utc":"2026-11-23T07:00:00Z","observation_id":"lint:1:1",
                "note":"on_repo · docs/example.md:5:2"}],"resolution":None,"resolution_history":[],
            "duplicate_of":None,"accepted_risk":None,
        }
        second = dict(finding)
        second.update({"finding_id":"lint-b2c3d4e5f6a7","title":"Second finding","severity":"informational"})
        second["evidence"] = [{"report_path":"reports/lint_reports/on_changed/history/2-attempt-1/report.json",
            "observed_at_utc":"2026-11-23T07:00:00Z","observation_id":"lint:2:1",
            "note":"on_changed · docs/example.md:8:1"}]
        self.write_ledger(version="1.1.0", findings=[finding, second])
        LEDGER.ingest(self.root)
        migrated = self.read_ledger()
        self.assertEqual(migrated["schema_version"],"1.5.0")
        self.assertEqual(migrated["findings"][0]["task_group"], migrated["findings"][1]["task_group"])
        task_id = migrated["findings"][0]["task_refs"][0]
        self.assertEqual(migrated["findings"][1]["task_refs"], [task_id])
        task_files = list((self.root / "workspace" / "tasks").glob("*.md"))
        self.assertEqual(len(task_files), 1)
        task_text = task_files[0].read_text(encoding="utf-8")
        self.assertIn("lint-a1b2c3d4e5f6", task_text)
        self.assertIn("lint-b2c3d4e5f6a7", task_text)
        self.assertIn("- **Priority:** P3", task_text)

        self.add_lint("on_repo", "901", "2026-11-23T07:10:00Z", fingerprint="a1b2c3d4e5f6")
        LEDGER.ingest(self.root, now="2026-11-23T07:11:00Z")
        legacy = self.read_ledger()["findings"][0]
        self.assertEqual(legacy["task_refs"], [task_id])
        self.assertEqual(len(list((self.root / "workspace" / "tasks").glob("*.md"))), 1)

        self.add_lint("on_repo", "902", "2026-11-23T07:12:00Z", fingerprint="cccccccc3333")
        LEDGER.ingest(self.root, now="2026-11-23T07:13:00Z")
        migrated = self.read_ledger()
        new_finding = next(item for item in migrated["findings"] if item["finding_id"] == "lint-cccccccc3333")
        legacy_after = next(item for item in migrated["findings"] if item["finding_id"] == "lint-a1b2c3d4e5f6")
        self.assertEqual(new_finding["task_refs"], [task_id])
        self.assertEqual(legacy_after["task_refs"], [task_id])
        task_files = list((self.root / "workspace" / "tasks").glob("*.md"))
        self.assertEqual(len(task_files), 1)
        task_text = task_files[0].read_text(encoding="utf-8")
        self.assertIn("lint-cccccccc3333", task_text)
        self.assertIn("lint-a1b2c3d4e5f6", task_text)
        self.assertIn("lint-b2c3d4e5f6a7", task_text)

    def test_lint_baseline_requires_every_tooling_check_but_allows_lint_findings(self):
        path = self.add_lint("on_changed", "948", "2026-11-23T07:00:00Z", status="Failed")
        report = json.loads((self.root / path).read_text(encoding="utf-8"))
        self.assertTrue(LEDGER.lint_baseline_ready(report, "on_changed"))

        for name in LEDGER.LINT_BASELINE_CHECKS:
            candidate = json.loads(json.dumps(report))
            next(item for item in candidate["checks"] if item["name"] == name)["status"] = "Failed"
            self.assertFalse(LEDGER.lint_baseline_ready(candidate, "on_changed"), name)

        missing = json.loads(json.dumps(report))
        missing["checks"] = [
            item for item in missing["checks"]
            if item["name"] != LEDGER.LINT_BASELINE_CHECKS[0]
        ]
        self.assertFalse(LEDGER.lint_baseline_ready(missing, "on_changed"))

        anchor_failed = json.loads(json.dumps(report))
        next(item for item in anchor_failed["checks"]
             if item["name"] == "Markdown links and heading anchors")["status"] = "Failed"
        self.assertFalse(LEDGER.lint_baseline_ready(anchor_failed, "on_changed"))

    def test_first_full_lint_report_seeds_baseline_without_creating_findings(self):
        path = self.add_lint("on_changed", "950", "2026-11-23T07:10:00Z")
        ledger = self.read_ledger()
        ledger["ingestion_state"]["lint_baseline_scopes"]["on_changed"] = False
        (self.root / ".takeout" / "reports" / "triage" / "ledger.json").write_text(json.dumps(ledger), encoding="utf-8")
        result = LEDGER.ingest(self.root, now="2026-11-23T07:11:00Z")
        updated = self.read_ledger()
        self.assertTrue(updated["ingestion_state"]["lint_baseline_scopes"]["on_changed"])
        self.assertEqual(updated["findings"], [])
        self.assertEqual(result["findings_created"], 0)
        self.assertIn(path, updated["ingestion_state"]["processed_reports"])

    def test_invalid_lint_report_is_consumed_without_seeding_the_baseline(self):
        path = self.add_lint("on_changed", "949", "2026-11-23T07:05:00Z",
                             execution_mode="incremental")
        ledger = self.read_ledger()
        ledger["ingestion_state"]["lint_baseline_scopes"]["on_changed"] = False
        (self.root / ".takeout" / "reports" / "triage" / "ledger.json").write_text(json.dumps(ledger), encoding="utf-8")
        result = LEDGER.ingest(self.root, now="2026-11-23T07:06:00Z")
        updated = self.read_ledger()
        self.assertFalse(updated["ingestion_state"]["lint_baseline_scopes"]["on_changed"])
        self.assertEqual(updated["findings"], [])
        self.assertIn(path, updated["ingestion_state"]["processed_reports"])
        self.assertEqual(result["findings_created"], 0)
        self.assertEqual(len(result["warnings"]), 1)
        self.add_lint("on_changed", "950", "2026-11-23T07:10:00Z",
                      execution_mode="full-audit-fallback")
        LEDGER.ingest(self.root, now="2026-11-23T07:11:00Z")
        updated = self.read_ledger()
        self.assertTrue(updated["ingestion_state"]["lint_baseline_scopes"]["on_changed"])
        self.assertEqual(updated["findings"], [])

    def test_recurring_untracked_lint_baseline_findings_do_not_create_tasks(self):
        self.add_lint("on_changed", "951", "2026-11-23T07:10:00Z", comparison="recurring")
        LEDGER.ingest(self.root)
        self.assertEqual(self.read_ledger()["findings"], [])
        self.add_lint("on_changed", "952", "2026-11-23T07:20:00Z",
                      fingerprint="bbbbbbbb2222", comparison="new")
        result = LEDGER.ingest(self.root)
        findings = self.read_ledger()["findings"]
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["finding_id"], "lint-bbbbbbbb2222")
        self.assertEqual(result["tasks_created"], 1)

    def test_evidence_is_bounded_but_occurrence_count_keeps_growing(self):
        for position in range(8):
            minute = 10 + position
            self.add_lint("on_changed", str(960 + position),
                          "2026-11-23T07:%02d:00Z" % minute)
        LEDGER.ingest(self.root)
        finding = self.read_ledger()["findings"][0]
        self.assertEqual(finding["occurrence_count"], 8)
        self.assertEqual(len(finding["evidence"]), 5)
        self.assertIn("960-attempt-1/report.json", finding["evidence"][0]["report_path"])
        self.assertIn("967-attempt-1/report.json", finding["evidence"][-1]["report_path"])

    def test_terminal_finding_is_retired_after_linked_task_is_archived_done(self):
        finding_id = "lint-1234567890abcdef"
        task_id = "20261123-090000"
        archive_path = ".archive/task/20261123-090000-example.md"
        task_file = self.root / archive_path
        task_file.parent.mkdir(parents=True)
        task_file.write_text(
            "# Task: Example\n\n## Metadata\n\n"
            "- **ID:** " + task_id + "\n- **Status:** Done\n- **Archived:** Yes\n\n"
            "## 13. Ledger Findings\n\n"
            "| Finding ID | Severity | Diagnostic | Evidence |\n|---|---|---|---|\n"
            "| " + chr(96) + finding_id + chr(96) + " | medium | fixed | report |\n",
            encoding="utf-8",
        )
        index = self.root / ".github" / "archive-retention-index.json"
        index.parent.mkdir(parents=True)
        index.write_text(json.dumps({"schema_version":1,"unindexed_records":"preserve","records":[
            {"path":archive_path,"archived_at_utc":"2026-11-23T09:00:00Z"}
        ]}), encoding="utf-8")
        ledger = {"findings":[{"finding_id":finding_id,"status":"resolved","task_refs":[task_id]}]}
        retired = LEDGER.retire_completed_task_findings(self.root, ledger)
        self.assertEqual(retired, [finding_id])
        self.assertEqual(ledger["findings"], [])

    def test_grouped_task_waits_until_every_finding_is_terminal(self):
        task_id = "20261123-090002"
        archive_path = ".archive/task/20261123-090002-example.md"
        first = "lint-1234567890abcdef"
        second = "lint-fedcba0987654321"
        task_file = self.root / archive_path
        task_file.parent.mkdir(parents=True)
        task_file.write_text(
            "# Task: Example\n\n## Metadata\n\n"
            "- **ID:** " + task_id + "\n- **Status:** Done\n- **Archived:** Yes\n\n"
            "## 13. Ledger Findings\n\n"
            "| Finding ID | Severity | Diagnostic | Evidence |\n|---|---|---|---|\n"
            "| " + chr(96) + first + chr(96) + " | medium | fixed | report |\n"
            "| " + chr(96) + second + chr(96) + " | medium | still open | report |\n",
            encoding="utf-8",
        )
        index = self.root / ".github" / "archive-retention-index.json"
        index.parent.mkdir(parents=True)
        index.write_text(json.dumps({"schema_version":1,"unindexed_records":"preserve","records":[
            {"path":archive_path,"archived_at_utc":"2026-11-23T09:00:00Z"}
        ]}), encoding="utf-8")
        ledger = {"findings":[
            {"finding_id":first,"status":"resolved","task_refs":[task_id]},
            {"finding_id":second,"status":"open","task_refs":[task_id]},
        ]}
        self.assertEqual(LEDGER.retire_completed_task_findings(self.root, ledger), [])
        self.assertEqual(len(ledger["findings"]), 2)

    def test_open_or_cancelled_task_never_retires_a_finding(self):
        finding_id = "lint-1234567890abcdef"
        task_id = "20261123-090001"
        archive_path = ".archive/task/20261123-090001-example.md"
        task_file = self.root / archive_path
        task_file.parent.mkdir(parents=True)
        task_file.write_text(
            "# Task: Example\n\n## Metadata\n\n"
            "- **ID:** " + task_id + "\n- **Status:** Cancelled\n- **Archived:** Yes\n\n"
            "## 13. Ledger Findings\n\n"
            "| Finding ID | Severity | Diagnostic | Evidence |\n|---|---|---|---|\n"
            "| " + chr(96) + finding_id + chr(96) + " | medium | not fixed | report |\n",
            encoding="utf-8",
        )
        index = self.root / ".github" / "archive-retention-index.json"
        index.parent.mkdir(parents=True)
        index.write_text(json.dumps({"schema_version":1,"unindexed_records":"preserve","records":[
            {"path":archive_path,"archived_at_utc":"2026-11-23T09:00:00Z"}
        ]}), encoding="utf-8")
        ledger = {"findings":[{"finding_id":finding_id,"status":"open","task_refs":[task_id]}]}
        self.assertEqual(LEDGER.retire_completed_task_findings(self.root, ledger), [])
        self.assertEqual(len(ledger["findings"]), 1)

    def test_false_positive_requires_a_closure_note(self):
        finding = {"finding_id":"finding-1","status":"false_positive"}
        with self.assertRaises(LEDGER.LedgerError):
            LEDGER.validate_semantics({"findings":[finding]})
        finding["closure_note"] = "The report identified a false positive."
        LEDGER.validate_semantics({"findings":[finding]})

    def test_malformed_index_fails_closed_without_changing_ledger(self):
        index = self.root / ".takeout" / "reports" / "lint_reports" / "on_changed" / "index.json"
        index.parent.mkdir(parents=True,exist_ok=True)
        index.write_text("{broken",encoding="utf-8")
        path = self.root / ".takeout" / "reports" / "triage" / "ledger.json"
        before = path.read_bytes()
        with self.assertRaises(LEDGER.LedgerError):
            LEDGER.ingest(self.root)
        self.assertEqual(path.read_bytes(),before)

    def test_unsafe_actions_history_path_is_rejected(self):
        index = self.root / ".takeout" / "reports" / "gh_ac_reports" / "index.json"
        index.parent.mkdir(parents=True,exist_ok=True)
        index.write_text(json.dumps({"runs":[{"history_path":"history/../../outside"}]}),encoding="utf-8")
        with self.assertRaises(LEDGER.LedgerError):
            LEDGER.indexed_reports(self.root)

    def test_duplicate_status_requires_an_existing_target(self):
        with self.assertRaises(LEDGER.LedgerError):
            LEDGER.validate_semantics({"findings":[{"finding_id":"finding-1","status":"duplicate","duplicate_of":"missing"}]})
        LEDGER.validate_semantics({"findings":[
            {"finding_id":"finding-1","status":"open"},
            {"finding_id":"finding-2","status":"duplicate","duplicate_of":"finding-1"},
        ]})

    def test_resolved_status_requires_fix_and_successful_validation(self):
        finding = {
            "finding_id":"lint-a1b2c3d4e5f6","source_family":"lint","category":"rule","title":"A finding",
            "status":"resolved","severity":"low","first_seen_utc":"2026-11-23T07:00:00Z",
            "last_seen_utc":"2026-11-23T07:00:00Z","occurrence_count":1,"evidence":[],"resolution":None,
        }
        with self.assertRaises(LEDGER.LedgerError):
            LEDGER.validate_semantics({"findings":[finding]})

    def test_all_ledger_publishers_share_serialized_writer_group(self):
        root = SCRIPT.parents[4]
        workflows = (
            ".github/workflows/archive-retention.yml",
            ".github/workflows/convert-images-to-webp.yml",
            ".github/workflows/notification.yml",
            ".github/workflows/ste-lint-changed.yml",
            ".github/workflows/ste-lint-full-docs.yml",
            ".github/workflows/validate-document-standards.yml",
            ".github/workflows/gh-actions-diagnostics.yml",
        )
        group = "group: gh-ac-report-writer-${{ github.repository }}"
        for relative in workflows:
            content = (root / relative).read_text(encoding="utf-8")
            self.assertIn(group, content, relative)
            lines = content.splitlines()
            declarations = [
                index for index, line in enumerate(lines) if line.strip() == group
            ]
            self.assertTrue(declarations, relative)
            for index in declarations:
                indent = lines[index][:len(lines[index]) - len(lines[index].lstrip())]
                self.assertEqual(
                    lines[index + 1:index + 3],
                    [f"{indent}queue: max", f"{indent}cancel-in-progress: false"],
                    relative,
                )
        action = (root / ".takeout/reports/gh_ac_reports/actions/capture/action.yml").read_text(encoding="utf-8")
        sweep = (root / ".github/workflows/gh-actions-diagnostics.yml").read_text(encoding="utf-8")
        standards = (root / ".github/workflows/validate-document-standards.yml").read_text(encoding="utf-8")
        lint_changed = (root / ".github/workflows/ste-lint-changed.yml").read_text(encoding="utf-8")
        self.assertIn("Update central CI issue ledger", action)
        self.assertIn("python3 -m py_compile .takeout/reports/gh_ac_reports/scripts/report.py .takeout/reports/triage/scripts/ledger.py", action)
        self.assertIn("python3 .takeout/reports/gh_ac_reports/scripts/report.py", action)
        self.assertIn("python3 .takeout/reports/triage/scripts/ledger.py", action)
        self.assertNotIn("python3 reports/", action)
        self.assertNotIn("-s reports/", action)
        self.assertNotIn("continue-on-error: true", action)
        for relative in (".github/workflows/ste-lint-changed.yml", ".github/workflows/ste-lint-full-docs.yml", ".github/workflows/validate-document-standards.yml"):
            self.assertIn("    continue-on-error: true", (root / relative).read_text(encoding="utf-8"), relative)
        publish_paths = "git add -A -- .takeout/reports/gh_ac_reports/ .takeout/reports/triage/ workspace/tasks/ workspace/task_board.md"
        self.assertIn(publish_paths, action)
        self.assertIn(publish_paths, sweep)
        self.assertIn("- '.takeout/reports/triage/ledger.json'", sweep)
        self.assertIn("- 'workspace/tasks/**'", sweep)
        self.assertIn("- 'workspace/task_board.md'", sweep)
        self.assertIn("      - '!workspace/tasks/**'", standards)
        self.assertIn("      - '!workspace/task_board.md'", standards)
        self.assertIn("      - '!workspace/tasks/**'", lint_changed)
        self.assertIn("      - '!workspace/task_board.md'", lint_changed)
        self.assertIn("Ingest centralized CI issues", sweep)
        self.assertIn("      - name: Publish diagnostic backfill and Worker tasks\n        if: always()", sweep)
        ignored = sweep.split("paths-ignore:", 1)[1].split("concurrency:", 1)[0]
        self.assertIn(".archive/reports/**", ignored)
        self.assertNotIn(".github/archive-retention-index.json", ignored)
        self.assertNotIn(".archive/task/**", ignored)
        self.assertIn("      - '!workspace/discussion.md'", standards)
        self.assertLess(
            standards.index("      - 'workspace/**/*.md'"),
            standards.index("      - '!workspace/discussion.md'"),
        )
        retention = (root / ".github/workflows/archive-retention.yml").read_text(encoding="utf-8")
        self.assertIn("needs: [cleanup]", retention)
        self.assertIn(group, retention)
        for relative in (".github/workflows/ste-lint-changed.yml", ".github/workflows/ste-lint-full-docs.yml"):
            content = (root / relative).read_text(encoding="utf-8")
            self.assertIn(group, content, relative)
        self.assertIn("latest-lint-report.json", lint_changed)
        self.assertNotIn("last successful lint baseline", lint_changed)
        self.assertIn("lint_baseline_ready", (root / ".takeout/reports/triage/scripts/ledger.py").read_text(encoding="utf-8"))
        self.assertIn("retire_completed_task_findings", (root / ".takeout/reports/triage/scripts/ledger.py").read_text(encoding="utf-8"))
        self.assertIn("findings_retired", (root / ".takeout/reports/triage/scripts/ledger.py").read_text(encoding="utf-8"))

    def test_atomic_write_replaces_file_without_temp_remnants(self):
        path = self.root / ".takeout" / "reports" / "triage" / "ledger.json"
        LEDGER.atomic_write(path,{"schema_version":"test"})
        self.assertEqual(json.loads(path.read_text())["schema_version"],"test")
        self.assertEqual(list(path.parent.glob("ledger.json.*.tmp")),[])

if __name__ == "__main__":
    unittest.main()
