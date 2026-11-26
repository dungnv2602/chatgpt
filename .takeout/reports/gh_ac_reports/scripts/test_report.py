#!/usr/bin/env python3
"""Regression tests for GitHub Actions diagnostic reports."""
import hashlib
import importlib.util
import json
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

SCRIPT = Path(__file__).with_name("report.py")
SPEC = importlib.util.spec_from_file_location("gh_ac_report", SCRIPT)
REPORT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(REPORT)


def make_run(conclusion="failure", status="completed", run_id=100, created="2026-11-23T06:00:00Z"):
    return {
        "id": run_id, "run_number": run_id, "run_attempt": 1, "workflow_id": 55,
        "name": "Example workflow", "path": ".github/workflows/example.yml",
        "html_url": "https://github.com/example/repo/actions/runs/" + str(run_id),
        "event": "push", "head_branch": "gpt", "head_sha": "abc123",
        "status": status, "conclusion": conclusion, "created_at": created,
        "run_started_at": created, "updated_at": created, "actor": {"login": "tester"},
    }


def make_job(conclusion="failure", step_conclusion="failure", name="Run unit tests", job_id=200):
    return {
        "id": job_id, "name": "Build and test", "status": "completed", "conclusion": conclusion,
        "started_at": "2026-11-23T06:00:01Z", "completed_at": "2026-11-23T06:00:10Z",
        "runner_name": "GitHub Actions", "runner_id": 123, "steps": [
            {"number": 1, "name": "Set up job", "status": "completed", "conclusion": "success"},
            {"number": 2, "name": name, "status": "completed", "conclusion": step_conclusion},
        ],
    }


def build(run, jobs, logs=None, stage="post_run", jobs_available=True):
    logs = logs or {}
    return REPORT.classify(run, [
        {"id": str(job["id"]), "name": job["name"], "status": job.get("status", "completed"),
         "conclusion": job["conclusion"], "steps": job["steps"]} for job in jobs
    ], logs, jobs_available=jobs_available)


class ClassificationTests(unittest.TestCase):
    def test_failed_test_step(self):
        result = build(make_run(), [make_job()], {"200": "FAILED: assertion did not match"})
        self.assertEqual(result["state"], "failure")
        self.assertEqual(result["primary_category"], "validation_or_test")
        self.assertTrue(result["issues"][0]["blocking"])

    def test_failed_step_uses_only_its_own_log_lines(self):
        log = (
            "Build and test\tPublish report\t2026-11-23T06:00:00Z git push origin gpt\n"
            "Build and test\tRun unit tests\t2026-11-23T06:00:01Z FAILED: assertion mismatch"
        )
        step_text = REPORT.step_log_text(log, "Run unit tests")
        category, confidence = REPORT.classify_text(step_text, "Build and test", "Run unit tests")
        self.assertEqual(category, "validation_or_test")
        self.assertEqual(confidence, "medium")
        self.assertNotIn("git push", step_text)

    def test_unittest_assertion_beats_embedded_publication_keywords(self):
        log = (
            "FAIL: test_all_ledger_publishers_share_serialized_writer_group "
            "(test_ledger.LedgerTests) ... FAIL\n"
            "AssertionError: expected command not found in 'git push origin gpt'\n"
            "FAILED (failures=1)"
        )
        category, confidence = REPORT.classify_text(
            log, "validate-document-standards", "Run CI Ledger regression tests"
        )
        self.assertEqual(category, "validation_or_test")
        self.assertEqual(confidence, "medium")

    def test_structured_unknown_step_does_not_leak_checkout_log_lines(self):
        log = (
            "validate-document-standards\tUNKNOWN STEP\tERROR: test_fixture_case ... ERROR\n"
            "validate-document-standards\tCheck out gpt\tcheckout completed"
        )
        step_text = REPORT.step_log_text(log, "Run CI Ledger regression tests")
        self.assertEqual(step_text, "")
        result = build(
            make_run("cancelled"),
            [make_job("failure", "failure", name="Run CI Ledger regression tests")],
            {"200": log},
        )
        self.assertEqual(result["state"], "cancelled")
        self.assertEqual(result["issues"][0]["category"], "validation_or_test")

    def test_unstructured_log_remains_available_when_step_label_is_absent(self):
        log = "ERROR: failed operation"
        self.assertEqual(REPORT.step_log_text(log, "Run unit tests"), log)

    def test_genuine_push_failure_remains_publication_error(self):
        category, confidence = REPORT.classify_text(
            "remote rejected: protected branch; git push failed",
            "Publish diagnostic evidence", "Publish evidence",
        )
        self.assertEqual(category, "publication_or_push")
        self.assertEqual(confidence, "high")

    def test_cancelled_is_not_failure(self):
        result = build(make_run("cancelled"), [make_job("cancelled", "cancelled")])
        self.assertEqual(result["state"], "cancelled")
        self.assertIsNone(result["primary_category"])
        self.assertEqual(result["categories"], [])
        self.assertEqual(result["issues"], [])

    def test_cancelled_run_ignores_downstream_status_propagation(self):
        job = make_job("cancelled", "cancelled", name="Run full technical-document lint")
        job["steps"].append({
            "number": 3, "name": "Preserve lint failure as workflow conclusion",
            "status": "completed", "conclusion": "failure",
        })
        log = (
            "Build and test\tPreserve lint failure as workflow conclusion\t"
            "2026-11-23T06:00:11Z ##[error]Changed-document lint failed."
        )
        result = build(make_run("cancelled"), [job], {"200": log})
        self.assertEqual(result["state"], "cancelled")
        self.assertEqual(result["issues"], [])
        self.assertIsNone(result["primary_category"])

    def test_independent_failure_before_cancellation_remains_actionable(self):
        job = make_job("cancelled", "failure", name="Run unit tests")
        job["steps"].append({
            "number": 3, "name": "Cancel remaining work",
            "status": "completed", "conclusion": "cancelled",
        })
        log = "Build and test\tRun unit tests\t2026-11-23T06:00:02Z FAILED: assertion mismatch"
        result = build(make_run("cancelled"), [job], {"200": log})
        self.assertEqual(result["state"], "cancelled")
        self.assertEqual(len(result["issues"]), 1)
        self.assertEqual(result["issues"][0]["category"], "validation_or_test")

    def test_pre_finalizer_projects_cancellation_without_actionable_issues(self):
        run = make_run(None, "in_progress")
        job = make_job("cancelled", "cancelled", name="Run unit tests")
        job["steps"].append({
            "number": 3, "name": "Preserve lint failure as workflow conclusion",
            "status": "completed", "conclusion": "failure",
        })
        result = build(run, [job])
        self.assertEqual(result["state"], "in_progress")
        self.assertEqual(result["projected_conclusion"], "cancelled")
        self.assertEqual(result["issues"], [])

    def test_failed_run_without_jobs_is_low_confidence_startup(self):
        result = build(make_run(), [])
        self.assertEqual(result["primary_category"], "workflow_startup_or_configuration_failure")
        self.assertEqual(result["issues"][0]["confidence"], "low")

    def test_unavailable_jobs_endpoint_is_not_called_a_startup_failure(self):
        result = build(make_run(), [], jobs_available=False)
        self.assertEqual(result["primary_category"], "workflow_level_failure_unattributed")
        self.assertEqual(result["issues"][0]["confidence"], "low")

    def test_continue_on_error_step_is_nonblocking(self):
        result = build(make_run("success"), [make_job("success", "failure")], {"200": "Process completed with exit code 1"})
        self.assertEqual(result["state"], "success_with_non_blocking_step_failures")
        self.assertFalse(result["issues"][0]["blocking"])

    def test_pre_finalizer_projects_but_does_not_invent_conclusion(self):
        run = make_run(None, "in_progress")
        result = build(run, [make_job()])
        self.assertIsNone(result["observed_conclusion"])
        self.assertEqual(result["projected_conclusion"], "failure")

    def test_log_redaction(self):
        value = "Authorization: Bearer abcdef123456 password=hunter2\n::error::request failed"
        cleaned = REPORT.redact(value)
        self.assertNotIn("abcdef123456", cleaned)
        self.assertNotIn("hunter2", cleaned)
        self.assertTrue(REPORT.markers(cleaned))


class CapturePolicyTests(unittest.TestCase):
    def test_failed_conclusion_without_independent_issue_is_not_reportable(self):
        report = {"classification": {
            "observed_conclusion": "failure", "projected_conclusion": None, "issues": []
        }}
        self.assertFalse(REPORT.report_is_actionable(report))

    def test_retention_uses_shared_independent_error_predicate_and_keeps_incomplete_retries(self):
        report = {
            "source_run":{"status":"completed"},
            "capture":{"stage":"post_run","completeness":"Incomplete"},
            "classification":{"issues":[{
                "category":"validation_or_test","job_name":"Build","step_name":"Run tests",
                "message":"ERROR: assertion mismatch",
            }]},
        }
        self.assertTrue(REPORT.report_is_retained(report))
        report["classification"]["issues"][0]["step_name"] = "Set workflow result from audit and tooling outcomes"
        self.assertFalse(REPORT.report_is_retained(report))
        report["classification"]["issues"][0].update({
            "category":"cancelled","step_name":"Cancel remaining work","message":"Run cancelled.",
        })
        self.assertFalse(REPORT.report_is_retained(report))

    def test_capture_never_writes_an_in_progress_run(self):
        with tempfile.TemporaryDirectory() as temp:
            with patch.object(REPORT, "api_get", return_value={"run_attempt": 1, "status": "in_progress"}), \
                 patch.object(REPORT, "fetch_evidence") as fetch, \
                 patch.object(REPORT, "write_report") as writer:
                result = REPORT.capture_one("owner/repository", Path(temp), "100", "post_run", force=True)
            self.assertIsNone(result)
            fetch.assert_not_called()
            writer.assert_not_called()

    def test_manual_force_does_not_retain_success_without_errors(self):
        with tempfile.TemporaryDirectory() as temp:
            report = {"classification": {
                "observed_conclusion": "success", "projected_conclusion": None, "issues": []
            }}
            with patch.object(REPORT, "api_get", return_value={"run_attempt": 1, "status": "completed"}), \
                 patch.object(REPORT, "fetch_evidence", return_value=(report, {})), \
                 patch.object(REPORT, "write_report") as writer:
                result = REPORT.capture_one("owner/repository", Path(temp), "100", "post_run", force=True)
            self.assertIsNone(result)
            writer.assert_not_called()


    def test_ordinary_success_is_not_reportable(self):
        result = build(make_run("success"), [make_job("success", "success")])
        self.assertFalse(REPORT.report_is_actionable({"classification": result}))

    def test_success_with_nonblocking_step_failure_is_reportable(self):
        result = build(make_run("success"), [make_job("success", "failure")],
                       {"200": "Process completed with exit code 1"})
        self.assertEqual(result["state"], "success_with_non_blocking_step_failures")
        self.assertTrue(REPORT.report_is_actionable({"classification": result}))

    def test_cancelled_only_run_is_not_reportable(self):
        result = build(make_run("cancelled"), [make_job("cancelled", "cancelled")])
        self.assertFalse(REPORT.report_is_actionable({"classification": result}))

    def test_cancelled_run_with_independent_failure_is_reportable(self):
        job = make_job("cancelled", "failure", name="Run unit tests")
        job["steps"].append({
            "number": 3, "name": "Cancel remaining work",
            "status": "completed", "conclusion": "cancelled",
        })
        result = build(make_run("cancelled"), [job], {"200": "ERROR: assertion mismatch"})
        self.assertTrue(REPORT.report_is_actionable({"classification": result}))

    def test_workflow_level_timeout_is_actionable_without_job_evidence(self):
        result = build(make_run("timed_out"), [])
        self.assertEqual(result["primary_category"], "timeout")
        self.assertEqual(len(result["issues"]), 1)
        self.assertTrue(REPORT.report_is_actionable({"classification": result}))

    def test_capture_skips_ordinary_success(self):
        with tempfile.TemporaryDirectory() as temp:
            report = {"classification": {"observed_conclusion": "success", "projected_conclusion": None, "issues": []}}
            with patch.object(REPORT, "api_get", return_value={"run_attempt": 1}), \
                 patch.object(REPORT, "fetch_evidence", return_value=(report, {})), \
                 patch.object(REPORT, "write_report") as writer:
                result = REPORT.capture_one("owner/repository", Path(temp), "100", "post_run")
            self.assertIsNone(result)
            writer.assert_not_called()

    def test_sweep_retires_completed_ordinary_success_without_indexing_it(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with patch.object(REPORT, "collect_runs_since", return_value=[make_run("success")]), \
                 patch.object(REPORT, "capture_one", return_value=None):
                REPORT.run_sweep("owner/repository", root)
            index = REPORT.load_index(root)
            self.assertEqual(index["runs"], [])
            self.assertEqual(index["pending_run_ids"], [])


class HistoricalRetentionTests(unittest.TestCase):
    def test_prune_migrates_retained_history_and_removes_only_derived_views(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            cases = [
                ("100", "pre_finalizer", "in_progress", "failure", False),
                ("101", "post_run", "completed", "success", False),
                ("102", "post_run", "completed", "cancelled", False),
                ("103", "post_run", "completed", "failure", True),
                ("104", "post_run", "completed", "cancelled", True),
            ]
            canonical_before = {}
            for position, (run_id, stage, status, conclusion, has_issue) in enumerate(cases):
                folder = root / "history" / "55" / (run_id + "-attempt-1-" + stage)
                (folder / "logs").mkdir(parents=True)
                report = {
                    "schema_version": "1.0.0",
                    "source_run": {
                        "id": run_id, "number": int(run_id), "attempt": 1, "workflow_id": 55,
                        "workflow_name": "Example", "workflow_path": ".github/workflows/example.yml",
                        "run_url": "https://example.invalid/" + run_id, "status": status,
                        "conclusion": conclusion, "created_at": "2026-11-23T06:%02d:00Z" % position,
                    },
                    "capture": {
                        "stage": stage, "captured_at_utc": "2026-11-23T07:%02d:00Z" % position,
                        "completeness": "Complete" if status == "completed" else "Incomplete",
                    },
                    "classification": {
                        "state": conclusion, "projected_conclusion": "failure" if stage == "pre_finalizer" else None,
                        "primary_category": "validation_or_test" if has_issue else None,
                        "issues": ([{
                            "category": "validation_or_test", "job_name": "Build",
                            "step_name": "Run unit tests", "message": "ERROR: assertion mismatch",
                        }] if has_issue else []),
                    },
                    "history_path": "history/55/" + folder.name,
                }
                report_bytes = (json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
                log_bytes = ("immutable log " + run_id + "\n").encode("utf-8")
                (folder / "report.json").write_bytes(report_bytes)
                (folder / "report.md").write_text("# " + run_id, encoding="utf-8")
                (folder / "logs" / "job-1.log").write_bytes(log_bytes)
                canonical_before[run_id] = (report_bytes, log_bytes)
            REPORT.save_json(root / "index.json", {
                "schema_version": "1.0.0", "pending_run_ids": ["100"], "runs": [],
                "latest_report": None, "exhausted_run_ids": [],
            })
            (root / "latest-gh-ac-report.md").write_text("derived", encoding="utf-8")
            (root / "latest-gh-ac-report.json").write_text("derived", encoding="utf-8")
            REPORT.save_json(root / "by_workflow" / "55" / "index.json", {"runs": []})

            result = REPORT.prune_invalid_history(root)
            index = REPORT.load_index(root)
            self.assertEqual(result, {"removed": 3, "retained": 2, "migrated_markdown": 2})
            self.assertEqual({item["run_id"] for item in index["runs"]}, {"103", "104"})
            self.assertEqual(index["pending_run_ids"], ["100"])
            self.assertEqual(index["latest_report"]["run_id"], "104")
            self.assertFalse((root / "history/55/100-attempt-1-pre_finalizer").exists())
            self.assertFalse((root / "history/55/101-attempt-1-post_run").exists())
            self.assertFalse((root / "history/55/102-attempt-1-post_run").exists())
            self.assertFalse((root / "latest-gh-ac-report.md").exists())
            self.assertFalse((root / "latest-gh-ac-report.json").exists())
            self.assertFalse((root / "by_workflow").exists())
            for run_id in ("103", "104"):
                folder = root / "history" / "55" / (run_id + "-attempt-1-post_run")
                self.assertEqual((folder / "report.json").read_bytes(), canonical_before[run_id][0])
                self.assertEqual((folder / "logs" / "job-1.log").read_bytes(), canonical_before[run_id][1])
                self.assertFalse((folder / "report.md").exists())
                manifest = json.loads((folder / "integrity.json").read_text(encoding="utf-8"))
                self.assertEqual(set(manifest["files"]), {"report.json", "logs/job-1.log"})
                for relative, digest in manifest["files"].items():
                    self.assertEqual(hashlib.sha256((folder / relative).read_bytes()).hexdigest(), digest)


class OnDemandRenderingTests(unittest.TestCase):
    def test_render_report_produces_markdown_from_canonical_json(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            history_path = "history/55/100-attempt-1-post_run"
            folder = root / history_path
            folder.mkdir(parents=True)
            report = {
                "history_path": history_path,
                "source_run": {
                    "workflow_name": "Example workflow", "workflow_path": ".github/workflows/example.yml",
                    "id": "100", "attempt": 1, "number": 100, "run_url": "https://example.invalid/100",
                    "branch": "gpt", "head_sha": "abc123", "event": "push", "actor": "tester",
                    "created_at": "2026-11-23T06:00:00Z", "status": "completed", "conclusion": "failure",
                },
                "capture": {
                    "reporter_job": None, "stage": "post_run", "completeness": "Complete",
                    "captured_at_utc": "2026-11-23T06:01:00Z",
                },
                "classification": {
                    "projected_conclusion": None, "state": "failure",
                    "primary_category": "validation_or_test", "categories": ["validation_or_test"],
                    "issues": [],
                },
                "jobs": [], "annotations": [], "artifacts": [], "capture_errors": [],
            }
            (folder / "report.json").write_text(json.dumps(report), encoding="utf-8")
            rendered = REPORT.render_report(root, history_path)
            self.assertIn("Example workflow", rendered)
            self.assertIn("validation_or_test", rendered)
            self.assertFalse((folder / "report.md").exists())

    def test_render_report_rejects_missing_invalid_and_traversal_paths(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with self.assertRaises(FileNotFoundError):
                REPORT.render_report(root, "history/55/missing")
            folder = root / "history" / "55" / "broken"
            folder.mkdir(parents=True)
            (folder / "report.json").write_text("{invalid", encoding="utf-8")
            with self.assertRaises(json.JSONDecodeError):
                REPORT.render_report(root, "history/55/broken")
            with self.assertRaises(ValueError):
                REPORT.render_report(root, "../outside")


class RetryPolicyTests(unittest.TestCase):
    def test_incomplete_capture_uses_backoff_and_bounded_attempts(self):
        index = {"runs":[{
            "run_id":"100","attempt":1,"capture_stage":"post_run",
            "report_status":"Incomplete","captured_at_utc":"2026-11-23T06:00:00Z",
        }]}
        self.assertFalse(REPORT.incomplete_retry_allowed(
            index, "100", 1, "post_run", now="2026-11-23T06:30:00Z"
        ))
        self.assertTrue(REPORT.incomplete_retry_allowed(
            index, "100", 1, "post_run", now="2026-11-23T07:00:00Z"
        ))
        index["runs"] *= 3
        self.assertFalse(REPORT.incomplete_retry_allowed(
            index, "100", 1, "post_run", now="2026-11-23T12:00:00Z"
        ))

    def test_force_request_does_not_duplicate_a_complete_capture(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            index = {
                "schema_version":"1.0.0","pending_run_ids":[],"exhausted_run_ids":[],
                "runs":[{
                    "run_id":"100","attempt":1,"capture_stage":"post_run",
                    "report_status":"Complete","captured_at_utc":"2026-11-23T06:00:00Z",
                }],
            }
            (root / "index.json").write_text(json.dumps(index), encoding="utf-8")
            with patch.object(REPORT, "api_get", return_value={"run_attempt":1}), \
                 patch.object(REPORT, "fetch_evidence") as fetch:
                result = REPORT.capture_one("owner/repository", root, "100", "post_run", force=True)
            self.assertIsNone(result)
            fetch.assert_not_called()

    def test_manual_request_is_consumed_after_incomplete_capture(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            pending = root / "requests" / "pending"
            pending.mkdir(parents=True)
            (pending / "request-100.json").write_text(json.dumps({"run_id":"100"}), encoding="utf-8")
            history = root / "history" / "55" / "100-attempt-1-post_run"
            history.mkdir(parents=True)
            incomplete_report = {
                "source_run": {
                    "id":"100","number":100,"attempt":1,"workflow_id":55,
                    "workflow_name":"Example","run_url":"https://example.invalid/100",
                    "status":"completed","conclusion":"failure",
                    "created_at":"2026-11-23T06:00:00Z",
                },
                "capture":{
                    "stage":"post_run","captured_at_utc":"2026-11-23T06:01:00Z",
                    "completeness":"Incomplete",
                },
                "classification":{
                    "projected_conclusion":None,"primary_category":"validation_or_test",
                    "issues":[{
                        "category":"validation_or_test","job_name":"Build",
                        "step_name":"Run unit tests","message":"ERROR: assertion mismatch",
                    }],
                },
                "history_path":"history/55/100-attempt-1-post_run",
            }
            (history / "report.json").write_text(json.dumps(incomplete_report), encoding="utf-8")
            (history / "report.md").write_text("# Incomplete evidence", encoding="utf-8")
            index = {
                "schema_version":"1.0.0","sweep_watermark_utc":"2026-11-23T06:00:00Z",
                "pending_run_ids":[],"exhausted_run_ids":[],
                "runs":[{
                    "run_id":"100","attempt":1,"capture_stage":"post_run",
                    "report_status":"Incomplete","captured_at_utc":"2026-11-23T06:00:00Z",
                    "history_path":"history/55/100-attempt-1-post_run",
                }],
            }
            (root / "index.json").write_text(json.dumps(index), encoding="utf-8")
            metadata = {"run_attempt":1,"status":"completed"}
            with patch.object(REPORT, "collect_runs_since", return_value=[]), \
                 patch.object(REPORT, "api_get", return_value=metadata), \
                 patch.object(REPORT, "capture_one", return_value=None):
                REPORT.run_sweep("owner/repository", root)
            done = root / "requests" / "processed" / "request-100.json"
            self.assertTrue(done.is_file())
            result = json.loads(done.read_text(encoding="utf-8"))
            self.assertEqual(result["status"], "Incomplete")
            self.assertEqual(result["report_path"], "history/55/100-attempt-1-post_run")
            self.assertFalse((pending / "request-100.json").exists())
            updated = REPORT.load_index(root)
            self.assertEqual(updated["pending_run_ids"], ["100"])


class RenderedPathTests(unittest.TestCase):
    def test_lint_report_links_use_reconstructed_takeout_root(self):
        report = {
            "source_run": {
                "workflow_name":"Example lint workflow",
                "workflow_path":".github/workflows/ste-lint-changed.yml",
                "id":"100","attempt":1,"number":100,
                "run_url":"https://example.invalid/actions/runs/100",
                "branch":"gpt","head_sha":"abc123","event":"push","actor":"tester",
                "created_at":"2026-11-23T06:00:00Z","status":"completed","conclusion":"failure",
            },
            "capture":{
                "stage":"post_run","completeness":"Complete",
                "captured_at_utc":"2026-11-23T06:01:00Z","reporter_job":None,
            },
            "classification":{
                "state":"failure","primary_category":"validation_or_test",
                "projected_conclusion":"failure","categories":["validation_or_test"],"issues":[],
            },
            "jobs":[],"annotations":[],"artifacts":[],"capture_errors":[],
        }
        expected = {
            ".github/workflows/ste-lint-changed.yml":
                "https://github.com/dungnv2602/chatgpt/blob/gpt/.takeout/reports/lint_reports/on_changed/latest-lint-report.md",
            ".github/workflows/ste-lint-full-docs.yml":
                "https://github.com/dungnv2602/chatgpt/blob/gpt/.takeout/reports/lint_reports/on_repo/latest-lint-report.md",
        }
        for workflow_path, link in expected.items():
            report["source_run"]["workflow_path"] = workflow_path
            rendered = REPORT.render_markdown(report)
            self.assertIn(link, rendered)
            self.assertNotIn("blob/gpt/reports/lint_reports/", rendered)


class RunSweepPaginationTests(unittest.TestCase):
    def test_run_sweep_page_urls_replace_page_parameter(self):
        first_runs = [{"id": i} for i in range(100)]
        second_runs = [{"id": 100}]
        responses = [
            {"workflow_runs": first_runs, "total_count": 101},
            {"workflow_runs": second_runs, "total_count": 101},
        ]
        with patch.object(REPORT, "api_get", side_effect=responses) as mocked_api:
            errors = []
            result = REPORT.collect_runs_between(
                "owner/repository", "2026-11-23T06:00:00Z", "2026-11-23T07:00:00Z", errors
            )
        self.assertEqual(len(result), 101)
        self.assertEqual(errors, [])
        urls = [call.args[1] for call in mocked_api.call_args_list]
        from urllib.parse import parse_qs, urlparse
        queries = [parse_qs(urlparse(url).query) for url in urls]
        self.assertEqual(queries[0].get("page"), ["1"])
        self.assertEqual(queries[1].get("page"), ["2"])
        self.assertEqual(len(queries[0].get("page", [])), 1)
        self.assertEqual(len(queries[1].get("page", [])), 1)


class AnnotationPaginationTests(unittest.TestCase):
    @patch.object(REPORT, "api_get", return_value=[{"path": "docs/example.md", "message": "A check annotation"}])
    def test_annotations_endpoint_accepts_top_level_array(self, mocked_api):
        errors = []
        items = REPORT.direct_pages("owner/repository", "/repos/owner/repository/check-runs/42/annotations", errors, "annotations")
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["path"], "docs/example.md")
        self.assertEqual(errors, [])
        mocked_api.assert_called_once()


class SchemaTests(unittest.TestCase):
    def test_schema_rejects_invalid_capture_stage(self):
        schema = json.loads(REPORT.SCHEMA_PATH.read_text(encoding="utf-8"))
        with self.assertRaises(ValueError):
            REPORT.validate_schema({"stage": "after_completion"}, schema["properties"]["capture"])


class StorageTests(unittest.TestCase):
    def test_integrity_and_immutable_history(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            report = {
                "schema_version": "1.0.0",
                "source_run": {"id":"100","number":100,"attempt":1,"workflow_id":55,"workflow_name":"Example",
                               "workflow_path":".github/workflows/example.yml","run_url":"https://example.invalid",
                               "event":"push","branch":"gpt","head_sha":"abc123","status":"completed",
                               "conclusion":"failure","created_at":"2026-11-23T06:00:00Z","actor":None,
                               "triggering_actor":None,"run_started_at":None,"updated_at":None,"head_commit_message":None},
                "capture":{"stage":"post_run","captured_at_utc":"2026-11-23T06:01:00Z","completeness":"Complete","reporter_job":None},
                "classification":{"state":"failure","observed_conclusion":"failure","projected_conclusion":None,
                                  "primary_category":"validation_or_test","categories":["validation_or_test"],
                                  "issues":[{"category":"validation_or_test","job_id":"200","job_name":"Build",
                                             "step_number":2,"step_name":"Tests","blocking":True,"confidence":"medium",
                                             "message":"Tests failed."}]},
                "jobs":[{"id":"200","name":"Build","status":"completed","conclusion":"failure",
                         "steps":[],"log_capture":{"available":True,"truncated":False,"bytes":6,
                         "path":"logs/job-200.log","marker_lines":[]}}],
                "check_runs":[],"annotations":[],"artifacts":[],"capture_errors":[],"history_path":"",
            }
            first = REPORT.write_report(root, report, {"logs/job-200.log":"FAILED"})
            before = (first / "report.json").read_bytes()
            integrity = json.loads((first / "integrity.json").read_text(encoding="utf-8"))
            self.assertEqual(integrity["files"]["report.json"], hashlib.sha256(before).hexdigest())
            self.assertEqual(integrity["files"]["logs/job-200.log"],
                             hashlib.sha256((first / "logs/job-200.log").read_bytes()).hexdigest())
            self.assertEqual(set(integrity["files"]), {"report.json", "logs/job-200.log"})
            self.assertFalse((first / "report.md").exists())
            second = REPORT.write_report(root, dict(report), {"logs/job-200.log":"OTHER"})
            self.assertNotEqual(first, second)
            self.assertEqual((first / "report.json").read_bytes(), before)

    def test_latest_pointer_and_stage_precedence(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            base = {
                "schema_version":"1.0.0",
                "source_run":{"id":"300","number":300,"attempt":1,"workflow_id":55,"workflow_name":"Example",
                              "workflow_path":".github/workflows/example.yml","run_url":"https://example.invalid",
                              "event":"push","branch":"gpt","head_sha":"abc123","status":"completed",
                              "conclusion":"success","created_at":"2026-11-23T07:00:00Z"},
                "capture":{"stage":"post_run","captured_at_utc":"2026-11-23T07:01:00Z","completeness":"Complete","reporter_job":None},
                "classification":{"state":"success","observed_conclusion":"success","projected_conclusion":None,
                                  "primary_category":None,"categories":[],"issues":[]},
                "jobs":[],"check_runs":[],"annotations":[],"artifacts":[],"capture_errors":[],"history_path":"",
            }
            REPORT.write_report(root, base, {})
            older = json.loads(json.dumps(base))
            older["source_run"]["id"]="200"
            older["source_run"]["number"]=200
            older["source_run"]["created_at"]="2026-11-23T06:00:00Z"
            REPORT.write_report(root, older, {})
            latest = REPORT.load_index(root)["latest_report"]
            self.assertEqual(latest["run_id"], "300")
            self.assertFalse((root / "latest-gh-ac-report.json").exists())
            self.assertFalse((root / "by_workflow").exists())
            pre = json.loads(json.dumps(base))
            pre["capture"]["stage"]="pre_finalizer"
            pre["capture"]["captured_at_utc"]="2026-11-23T07:02:00Z"
            REPORT.write_report(root, pre, {})
            latest = REPORT.load_index(root)["latest_report"]
            self.assertEqual(latest["capture_stage"], "post_run")

    def test_completed_pending_run_gets_post_run_capture_and_clears_pending(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            pre = {
                "schema_version":"1.0.0",
                "source_run":{"id":"100","number":100,"attempt":1,"workflow_id":55,"workflow_name":"Example",
                              "workflow_path":".github/workflows/example.yml","run_url":"https://example.invalid",
                              "event":"push","branch":"gpt","head_sha":"abc123","status":"in_progress",
                              "conclusion":None,"created_at":"2026-11-23T06:00:00Z","actor":None,
                              "triggering_actor":None,"run_started_at":None,"updated_at":None,"head_commit_message":None},
                "capture":{"stage":"pre_finalizer","captured_at_utc":"2026-11-23T06:01:00Z","completeness":"Incomplete","reporter_job":None},
                "classification":{"state":"in_progress","observed_conclusion":None,"projected_conclusion":"failure",
                                  "primary_category":"validation_or_test","categories":["validation_or_test"],
                                  "issues":[{"category":"validation_or_test","job_id":"200","job_name":"Build",
                                             "step_number":2,"step_name":"Tests","blocking":True,"confidence":"medium",
                                             "message":"Tests failed."}]},
                "jobs":[{"id":"200","name":"Build","status":"completed","conclusion":"failure",
                         "steps":[],"log_capture":{"available":False,"truncated":False,"bytes":0,
                         "path":None,"marker_lines":[]}}],
                "check_runs":[],"annotations":[],"artifacts":[],
                "capture_errors":[{"source":"job_log","message":"Run is still in progress."}],"history_path":"",
            }
            REPORT.save_json(root / "index.json", {
                "schema_version":"1.0.0","sweep_watermark_utc":"2026-11-23T06:00:00Z",
                "pending_run_ids":["100"],"exhausted_run_ids":[],"runs":[],"latest_report":None,
            })

            post = json.loads(json.dumps(pre))
            post["source_run"]["status"] = "completed"
            post["source_run"]["conclusion"] = "failure"
            post["capture"] = {
                "stage":"post_run","captured_at_utc":"2026-11-23T06:05:00Z",
                "completeness":"Complete","reporter_job":None,
            }
            post["classification"] = {
                "state":"failure","observed_conclusion":"failure","projected_conclusion":None,
                "primary_category":"validation_or_test","categories":["validation_or_test"],
                "issues":pre["classification"]["issues"],
            }
            post["jobs"][0]["log_capture"] = {
                "available":True,"truncated":False,"bytes":6,
                "path":"logs/job-200.log","marker_lines":["FAILED: tests"],
            }
            post["capture_errors"] = []

            with patch.object(REPORT, "collect_runs_since", return_value=[]), \
                 patch.object(REPORT, "api_get", side_effect=[
                     make_run("failure"),
                     {"run_attempt":1,"status":"completed"},
                     make_run("failure"),
                 ]), \
                 patch.object(REPORT, "fetch_evidence", return_value=(post, {"logs/job-200.log":"FAILED"})):
                REPORT.run_sweep("owner/repository", root)

            index = REPORT.load_index(root)
            self.assertEqual(index["pending_run_ids"], [])
            self.assertEqual(len(index["runs"]), 1)
            self.assertEqual({item["capture_stage"] for item in index["runs"]}, {"post_run"})
            latest = REPORT.load_index(root)["latest_report"]
            self.assertEqual(latest["capture_stage"], "post_run")


if __name__ == "__main__":
    unittest.main()
