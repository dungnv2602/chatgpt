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
            latest = json.loads((root / "latest-gh-ac-report.json").read_text(encoding="utf-8"))
            self.assertEqual(latest["source_run"]["id"], "300")
            pre = json.loads(json.dumps(base))
            pre["capture"]["stage"]="pre_finalizer"
            pre["capture"]["captured_at_utc"]="2026-11-23T07:02:00Z"
            REPORT.write_report(root, pre, {})
            latest = json.loads((root / "latest-gh-ac-report.json").read_text(encoding="utf-8"))
            self.assertEqual(latest["capture"]["stage"], "post_run")


if __name__ == "__main__":
    unittest.main()
