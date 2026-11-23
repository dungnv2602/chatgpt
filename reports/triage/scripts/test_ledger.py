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

class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        triage = self.root / "reports" / "triage"
        triage.mkdir(parents=True)
        shutil.copyfile(SCHEMA_SOURCE, triage / "ledger-schema.json")
        self.write_ledger()

    def tearDown(self):
        self.temp.cleanup()

    def write_ledger(self, version="1.1.0", findings=None):
        payload = {"schema_version": version, "updated_at_utc": None, "findings": findings or []}
        if version == "1.1.0":
            payload["ingestion_state"] = {"bootstrap_at_utc":"2026-11-23T07:00:00Z","processed_reports":[]}
        path = self.root / "reports" / "triage" / "ledger.json"
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        return path

    def add_lint(self, scope, run_id, timestamp, fingerprint="a1b2c3d4e5f6", status="Failed"):
        folder = self.root / "reports" / "lint_reports" / scope
        history = folder / "history" / (run_id + "-attempt-1")
        history.mkdir(parents=True, exist_ok=True)
        report_path = history / "report.json"
        report = {
            "schema_version":"1.1.0","scope":scope,"run_id":run_id,"attempt":1,
            "run_url":"https://example.invalid/actions/runs/" + run_id,
            "generated_at_utc":timestamp,"status":status,
            "findings":[{
                "file":"docs/example.md","line":5,"col":2,"rule":"semicolon","level":"advisory-free",
                "message":"Split this sentence.","fingerprint":fingerprint,"comparison":"new",
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
        self.assertEqual(len(finding["evidence"]),2)
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

    def test_cancelled_source_run_never_creates_findings(self):
        issue = {
            "category":"validation_or_test","job_name":"Build","step_name":"Unit tests",
            "blocking":True,"confidence":"high","message":"A stale report marked a cancelled run as a test failure.",
        }
        self.add_actions("203","2026-11-23T07:35:00Z",[issue],conclusion="cancelled")
        result = LEDGER.ingest(self.root)
        self.assertEqual(result["total_findings"],0)
        self.assertEqual(result["reports_processed"],1)
        self.assertEqual(self.read_ledger()["findings"],[])

    def test_actions_repeat_observation_increments_once_per_run(self):
        issue = {"category":"validation_or_test","job_name":"Build","step_name":"Unit tests","blocking":True,"confidence":"medium","message":"Assertion mismatch"}
        self.add_actions("201","2026-11-23T07:30:00Z",[issue])
        LEDGER.ingest(self.root)
        self.add_actions("202","2026-11-23T07:40:00Z",[issue])
        LEDGER.ingest(self.root)
        finding = self.read_ledger()["findings"][0]
        self.assertEqual(finding["occurrence_count"],2)
        self.assertEqual(len(finding["evidence"]),2)

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
        self.assertEqual(migrated["schema_version"],"1.1.0")
        self.assertIn(path,migrated["ingestion_state"]["processed_reports"])
        self.assertEqual(migrated["findings"],[])
        self.assertEqual(result["reports_processed"],0)
        self.assertTrue(migrated["updated_at_utc"])

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
        self.assertIn("git add -A -- reports/gh_ac_reports/ reports/triage/", action)
        self.assertIn("- 'reports/triage/ledger.json'", sweep)
        self.assertIn("Ingest centralized CI issues", sweep)

    def test_atomic_write_replaces_file_without_temp_remnants(self):
        path = self.root / "reports" / "triage" / "ledger.json"
        LEDGER.atomic_write(path,{"schema_version":"test"})
        self.assertEqual(json.loads(path.read_text())["schema_version"],"test")
        self.assertEqual(list(path.parent.glob("ledger.json.*.tmp")),[])

if __name__ == "__main__":
    unittest.main()
