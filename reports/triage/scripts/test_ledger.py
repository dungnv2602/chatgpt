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
TASK_TEMPLATE_SOURCE = SCRIPT.parents[3] / "workspace" / "TASK_TEMPLATE.md"
TASK_BOARD_SOURCE = SCRIPT.parents[3] / "workspace" / "task_board.md"

class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        triage = self.root / "reports" / "triage"
        triage.mkdir(parents=True)
        shutil.copyfile(SCHEMA_SOURCE, triage / "ledger-schema.json")
        workspace = self.root / "workspace"
        (workspace / "tasks").mkdir(parents=True)
        shutil.copyfile(TASK_TEMPLATE_SOURCE, workspace / "TASK_TEMPLATE.md")
        shutil.copyfile(TASK_BOARD_SOURCE, workspace / "task_board.md")
        self.write_ledger()

    def tearDown(self):
        self.temp.cleanup()

    def write_ledger(self, version="1.3.0", findings=None):
        payload = {"schema_version": version, "updated_at_utc": None, "findings": findings or []}
        if version in ("1.1.0", "1.2.0", "1.3.0"):
            payload["ingestion_state"] = {"bootstrap_at_utc":"2026-11-23T07:00:00Z","processed_reports":[]}
        path = self.root / "reports" / "triage" / "ledger.json"
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        return path

    def add_lint(self, scope, run_id, timestamp, fingerprint="a1b2c3d4e5f6", status="Failed",
                 level="advisory-free", file_path="docs/example.md", rule="semicolon",
                 message="Split this sentence."):
        folder = self.root / "reports" / "lint_reports" / scope
        history = folder / "history" / (run_id + "-attempt-1")
        history.mkdir(parents=True, exist_ok=True)
        report_path = history / "report.json"
        report = {
            "schema_version":"1.1.0","scope":scope,"run_id":run_id,"attempt":1,
            "run_url":"https://example.invalid/actions/runs/" + run_id,
            "generated_at_utc":timestamp,"status":status,
            "findings":[{
                "file":file_path,"line":5,"col":2,"rule":rule,"level":level,
                "message":message,"fingerprint":fingerprint,"comparison":"new",
            }],
        }
        report_path.write_text(json.dumps(report), encoding="utf-8")
        index_path = folder / "index.json"
        rows = json.loads(index_path.read_text())["runs"] if index_path.exists() else []
        rows.append({"run_id":run_id,"attempt":1,"generated_at_utc":timestamp})
        index_path.write_text(json.dumps({"schema_version":"1.1.0","runs":rows}), encoding="utf-8")
        return report_path.relative_to(self.root).as_posix()

    def add_actions(self, run_id, timestamp, issues, stage="post_run", completeness="Complete", conclusion="failure"):
        history = self.root / "reports" / "gh_ac_reports" / "history" / "55" / (run_id + "-attempt-1-" + stage)
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
        index_path = self.root / "reports" / "gh_ac_reports" / "index.json"
        rows = json.loads(index_path.read_text())["runs"] if index_path.exists() else []
        rows.append({
            "run_id":run_id,"attempt":1,"workflow_id":55,"capture_stage":stage,
            "captured_at_utc":timestamp,"history_path":history.relative_to(index_path.parent).as_posix(),
        })
        index_path.write_text(json.dumps({"schema_version":"1.0.0","runs":rows}), encoding="utf-8")
        return report_path.relative_to(self.root).as_posix()

    def read_ledger(self):
        return json.loads((self.root / "reports" / "triage" / "ledger.json").read_text())

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
        self.assertIn(f"| {finding['task_refs'][0]} |", (self.root / "workspace" / "task_board.md").read_text(encoding="utf-8"))
        second = LEDGER.ingest(self.root, now="2026-11-23T07:13:00Z")
        self.assertFalse(second["changed"])
        self.assertEqual(self.read_ledger()["findings"][0]["occurrence_count"],1)

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
        report_path = "reports/gh_ac_reports/history/55/900-attempt-1-post_run/report.json"
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

    def test_untrusted_diagnostic_text_is_escaped_in_worker_task(self):
        self.add_lint("on_changed", "213", "2026-11-23T07:55:00Z",
                      message="<script>alert(1)</script> [follow](javascript:run())")
        LEDGER.ingest(self.root, now="2026-11-23T07:56:00Z")
        task = next((self.root / "workspace" / "tasks").glob("*.md")).read_text(encoding="utf-8")
        self.assertIn("\\<script\\>", task)
        self.assertIn("\\[follow\\]", task)
        self.assertIn("untrusted evidence", task)

    def test_low_severity_findings_remain_ledger_only(self):
        self.add_lint("on_changed", "212", "2026-11-23T07:50:00Z", level="advisory")
        result = LEDGER.ingest(self.root, now="2026-11-23T07:51:00Z")
        finding = self.read_ledger()["findings"][0]
        self.assertEqual(finding["severity"], "low")
        self.assertEqual(finding["task_refs"], [])
        self.assertEqual(result["tasks_created"], 0)
        self.assertEqual(list((self.root / "workspace" / "tasks").glob("*.md")), [])

    def test_resolved_finding_reopens_and_preserves_resolution_history(self):
        self.add_lint("on_changed","300","2026-11-23T07:10:00Z")
        LEDGER.ingest(self.root)
        path = self.root / "reports" / "triage" / "ledger.json"
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
        self.assertEqual(migrated["schema_version"],"1.3.0")
        self.assertEqual(migrated["findings"],[])
        self.assertIn(path,migrated["ingestion_state"]["processed_reports"])
        self.assertEqual(migrated["findings"],[])
        self.assertEqual(result["reports_processed"],0)
        self.assertTrue(migrated["updated_at_utc"])

    def test_migrate_1_1_creates_proposed_task_for_unlinked_actionable_finding(self):
        finding = {
            "finding_id":"lint-a1b2c3d4e5f6","source_family":"lint","category":"rule","title":"A finding",
            "status":"planned","severity":"medium","owner":None,
            "first_seen_utc":"2026-11-23T07:00:00Z","last_seen_utc":"2026-11-23T07:00:00Z",
            "occurrence_count":1,"evidence":[{"report_path":"reports/lint_reports/on_repo/history/1-attempt-1/report.json",
                "observed_at_utc":"2026-11-23T07:00:00Z","observation_id":"lint:1:1",
                "note":"on_repo · docs/example.md:5:2"}],"resolution":None,"resolution_history":[],
            "duplicate_of":None,"accepted_risk":None,
        }
        second = dict(finding)
        second.update({"finding_id":"lint-b2c3d4e5f6a7","title":"Second finding"})
        second["evidence"] = [{"report_path":"reports/lint_reports/on_changed/history/2-attempt-1/report.json",
            "observed_at_utc":"2026-11-23T07:00:00Z","observation_id":"lint:2:1",
            "note":"on_changed · docs/example.md:8:1"}]
        self.write_ledger(version="1.1.0", findings=[finding, second])
        LEDGER.ingest(self.root)
        migrated = self.read_ledger()
        self.assertEqual(migrated["schema_version"],"1.3.0")
        self.assertEqual(len(migrated["findings"][0]["task_refs"]), 1)
        self.assertEqual(migrated["findings"][0]["task_refs"], migrated["findings"][1]["task_refs"])
        self.assertEqual(migrated["findings"][0]["task_group"], migrated["findings"][1]["task_group"])
        task_files = list((self.root / "workspace" / "tasks").glob("*.md"))
        self.assertEqual(len(task_files), 1)
        task_text = task_files[0].read_text(encoding="utf-8")
        self.assertIn("- **Status:** Proposed", task_text)
        self.assertIn("lint-a1b2c3d4e5f6", task_text)
        self.assertIn("lint-b2c3d4e5f6a7", task_text)

    def test_malformed_index_fails_closed_without_changing_ledger(self):
        index = self.root / "reports" / "lint_reports" / "on_changed" / "index.json"
        index.parent.mkdir(parents=True,exist_ok=True)
        index.write_text("{broken",encoding="utf-8")
        path = self.root / "reports" / "triage" / "ledger.json"
        before = path.read_bytes()
        with self.assertRaises(LEDGER.LedgerError):
            LEDGER.ingest(self.root)
        self.assertEqual(path.read_bytes(),before)

    def test_unsafe_actions_history_path_is_rejected(self):
        index = self.root / "reports" / "gh_ac_reports" / "index.json"
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
        root = SCRIPT.parents[3]
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
        action = (root / "reports/gh_ac_reports/actions/capture/action.yml").read_text(encoding="utf-8")
        sweep = (root / ".github/workflows/gh-actions-diagnostics.yml").read_text(encoding="utf-8")
        self.assertIn("Update central CI issue ledger", action)
        publish_paths = "git add -A -- reports/gh_ac_reports/ reports/triage/ workspace/tasks/ workspace/task_board.md"
        self.assertIn(publish_paths, action)
        self.assertIn(publish_paths, sweep)
        self.assertIn("- 'reports/triage/ledger.json'", sweep)
        self.assertIn("- 'workspace/tasks/**'", sweep)
        self.assertIn("- 'workspace/task_board.md'", sweep)
        self.assertIn("Ingest centralized CI issues", sweep)

    def test_atomic_write_replaces_file_without_temp_remnants(self):
        path = self.root / "reports" / "triage" / "ledger.json"
        LEDGER.atomic_write(path,{"schema_version":"test"})
        self.assertEqual(json.loads(path.read_text())["schema_version"],"test")
        self.assertEqual(list(path.parent.glob("ledger.json.*.tmp")),[])

if __name__ == "__main__":
    unittest.main()
