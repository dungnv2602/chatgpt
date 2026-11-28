from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from datetime import datetime, timedelta, timezone
from pathlib import Path

import recover_task_validation as recovery
import publish_task_validation as publisher


class RecoveryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.index_path = self.root / publisher.INDEX_PATH
        self.index_path.parent.mkdir(parents=True)
        self.index_path.write_text(
            json.dumps({"schema_version": 1, "closed_through": {"run_id": 0, "attempt": 0}, "attempts": []}),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def record(self, run_id: int, attempt: int, reconciled_at: str | None) -> dict:
        return {
            "source_task_id": None,
            "source_sha": "a" * 40,
            "coordinator_run_id": run_id,
            "attempt": attempt,
            "check_set_id": "c" * 64,
            "policy_revision": "b" * 40,
            "completed_at": "2026-11-20T12:00:00Z",
            "outcome": "check_failure",
            "actions_url": f"https://github.com/dungnv2602/chatgpt/actions/runs/{run_id}",
            "recovery": {
                "reconciled_at": reconciled_at,
                "retry_count": 0,
                "last_retry_at": None,
            },
        }

    def write_index(self, records: list[dict], checkpoint: tuple[int, int] = (0, 0)) -> None:
        self.index_path.write_text(
            json.dumps({
                "schema_version": 1,
                "closed_through": {"run_id": checkpoint[0], "attempt": checkpoint[1]},
                "attempts": records,
            }),
            encoding="utf-8",
        )

    def test_attempt_kind_ignores_gated_or_duplicate_dispatch(self) -> None:
        jobs = [
            {"name": "Check protected policy and duplicate source SHA", "status": "completed", "conclusion": "success"},
            {"name": "Run exact-SHA coordinator", "status": "completed", "conclusion": "skipped"},
        ]
        self.assertEqual(recovery.attempt_kind(jobs)[0], "ignored")

    def test_attempt_kind_captures_policy_gate_failure(self) -> None:
        jobs = [
            {"name": "Check protected policy and duplicate source SHA", "status": "completed", "conclusion": "failure"},
        ]
        self.assertEqual(recovery.attempt_kind(jobs)[0], "policy_failure")

    def test_attempt_kind_waits_for_running_coordinator(self) -> None:
        jobs = [
            {"name": "Aggregate complete check set", "status": "in_progress", "conclusion": None},
        ]
        self.assertEqual(recovery.attempt_kind(jobs)[0], "pending")

    def test_attempt_kind_recognizes_cancelled_coordinator(self) -> None:
        jobs = [
            {"name": "Changed-document lint", "status": "completed", "conclusion": "cancelled"},
        ]
        self.assertEqual(recovery.attempt_kind(jobs)[0], "cancelled")

    def test_aggregate_artifact_proves_coordinator_started(self) -> None:
        self.assertEqual(recovery.attempt_kind([], artifact_present=True)[0], "started")

    def test_dispatcher_policy_gate_running_counts_as_pending(self) -> None:
        jobs = [
            {"name": "Check protected policy and duplicate source SHA", "status": "in_progress", "conclusion": None},
        ]
        self.assertEqual(recovery.attempt_kind(jobs, run_status="in_progress")[0], "pending")

    def test_source_sha_is_read_from_workflow_dispatch_run_name(self) -> None:
        source_sha = "a" * 40
        run = {
            "event": "workflow_dispatch",
            "display_title": f"ADR-0008 task validation {source_sha}",
            "head_sha": "b" * 40,
        }
        self.assertEqual(recovery.source_sha_for_run(run), source_sha)

    def test_source_sha_uses_push_head_sha(self) -> None:
        source_sha = "a" * 40
        self.assertEqual(
            recovery.source_sha_for_run({"event": "push", "head_sha": source_sha}),
            source_sha,
        )

    def test_validation_lifecycle_parser_reads_awaiting_state(self) -> None:
        block = {
            "state": "awaiting_ci",
            "source_sha": "a" * 40,
            "policy_revision": "b" * 40,
            "coordinator_run_id": None,
            "attempt": None,
            "outcome": None,
            "reconciled_at": None,
        }
        fence = chr(96) * 3
        content = "## Validation Lifecycle\n\n" + fence + "json\n" + json.dumps(block) + "\n" + fence
        self.assertEqual(recovery.read_validation_lifecycle(content), block)

    def test_review_required_lifecycle_rejects_success_outcome(self) -> None:
        block = {
            "state": "review_required",
            "source_sha": "a" * 40,
            "policy_revision": "b" * 40,
            "coordinator_run_id": 10,
            "attempt": 1,
            "outcome": "success",
            "reconciled_at": None,
        }
        fence = chr(96) * 3
        content = "## Validation Lifecycle\n" + fence + "json\n" + json.dumps(block) + "\n" + fence
        with self.assertRaises(recovery.RecoveryError):
            recovery.read_validation_lifecycle(content)

    def test_awaiting_ci_task_discovery_uses_task_record_metadata(self) -> None:
        source_sha = "a" * 40
        block = {
            "state": "awaiting_ci",
            "source_sha": source_sha,
            "policy_revision": "b" * 40,
            "coordinator_run_id": None,
            "attempt": None,
            "outcome": None,
            "reconciled_at": None,
        }
        content = "- **ID:** 20261128-230000-04\n\n## Validation Lifecycle\n\n" + chr(96) * 3 + "json\n" + json.dumps(block) + "\n" + chr(96) * 3 + "\n"
        def fake_git(_root, *args, **_kwargs):
            output = "workspace/tasks/20261128-230000/subtasks/04-worker-migration.md\n" if args[:4] == ("ls-tree", "-r", "--name-only", "HEAD") else content
            return subprocess.CompletedProcess(args, 0, stdout=output, stderr="")
        with patch.object(recovery, "git", side_effect=fake_git):
            tasks = recovery.awaiting_ci_tasks(self.root)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["task_id"], "20261128-230000-04")
        self.assertEqual(tasks[0]["source_sha"], source_sha)

    def test_duplicate_awaiting_ci_source_sha_fails_closed(self) -> None:
        source_sha = "a" * 40
        block = {
            "state": "awaiting_ci",
            "source_sha": source_sha,
            "policy_revision": "b" * 40,
            "coordinator_run_id": None,
            "attempt": None,
            "outcome": None,
            "reconciled_at": None,
        }
        content = "- **ID:** 20261128-230000-04\n## Validation Lifecycle\n" + chr(96) * 3 + "json\n" + json.dumps(block) + "\n" + chr(96) * 3
        paths = [
            "workspace/tasks/20261128-230000/subtasks/04-worker-migration.md",
            "workspace/tasks/20261128-230000/subtasks/05-confirmation-retirement.md",
        ]
        def fake_git(_root, *args, **_kwargs):
            output = "\n".join(paths) if args[:4] == ("ls-tree", "-r", "--name-only", "HEAD") else content
            return subprocess.CompletedProcess(args, 0, stdout=output, stderr="")
        with patch.object(recovery, "git", side_effect=fake_git):
            with self.assertRaises(recovery.RecoveryError):
                recovery.awaiting_ci_tasks(self.root)

    def test_source_commit_policy_binds_validation_but_dispatch_gate_uses_current_policy(self) -> None:
        source_policy = {
            "coordinator": {"activation_status": "enabled"},
            "protection": {"enforcement_status": "verified"},
            "recovery": {"workflow_dispatch_activation_status": "external-prerequisite"},
        }
        current_policy = {
            "coordinator": {"activation_status": "enabled"},
            "protection": {"enforcement_status": "verified"},
            "recovery": {"workflow_dispatch_activation_status": "verified"},
        }
        policy_path = self.root / recovery.POLICY_PATH
        policy_path.parent.mkdir(parents=True)
        policy_path.write_text(json.dumps(current_policy), encoding="utf-8")
        def fake_git(_root, *args, **_kwargs):
            return subprocess.CompletedProcess(args, 0, stdout=json.dumps(source_policy), stderr="")
        with patch.object(recovery, "policy_blob_sha", return_value="b" * 40), patch.object(
            recovery, "git", side_effect=fake_git
        ):
            self.assertTrue(recovery.source_policy_allows_dispatch(self.root, "a" * 40, "b" * 40))
        current_policy["recovery"]["workflow_dispatch_activation_status"] = "external-prerequisite"
        policy_path.write_text(json.dumps(current_policy), encoding="utf-8")
        with patch.object(recovery, "policy_blob_sha", return_value="b" * 40), patch.object(
            recovery, "git", side_effect=fake_git
        ):
            self.assertFalse(recovery.source_policy_allows_dispatch(self.root, "a" * 40, "b" * 40))

    def test_source_commit_without_coordinator_activation_cannot_be_dispatched(self) -> None:
        source_policy = {
            "coordinator": {"activation_status": "staged"},
            "protection": {"enforcement_status": "verified"},
            "recovery": {"workflow_dispatch_activation_status": "verified"},
        }
        current_policy = {
            "coordinator": {"activation_status": "enabled"},
            "protection": {"enforcement_status": "verified"},
            "recovery": {"workflow_dispatch_activation_status": "verified"},
        }
        policy_path = self.root / recovery.POLICY_PATH
        policy_path.parent.mkdir(parents=True, exist_ok=True)
        policy_path.write_text(json.dumps(current_policy), encoding="utf-8")
        def fake_git(_root, *args, **_kwargs):
            return subprocess.CompletedProcess(args, 0, stdout=json.dumps(source_policy), stderr="")
        with patch.object(recovery, "policy_blob_sha", return_value="b" * 40), patch.object(
            recovery, "git", side_effect=fake_git
        ):
            self.assertFalse(recovery.source_policy_allows_dispatch(self.root, "a" * 40, "b" * 40))

    def test_missing_dispatch_is_started_only_when_source_policy_is_enabled(self) -> None:
        source_sha = "a" * 40
        task = {
            "task_id": "20261128-230000-04",
            "path": "workspace/tasks/20261128-230000/subtasks/04-worker-migration.md",
            "source_sha": source_sha,
            "policy_revision": "b" * 40,
        }
        class FakeAPI:
            def __init__(self):
                self.calls = []
            def post_json(self, path, payload):
                self.calls.append((path, payload))
        api = FakeAPI()
        with patch.object(recovery, "awaiting_ci_tasks", return_value=[task]), patch.object(
            recovery, "source_policy_allows_dispatch", return_value=True
        ):
            result = recovery.dispatch_missing_attempts(self.root, api, "dungnv2602/chatgpt", set(), set())
        self.assertEqual(result, (1, 1, 0))
        self.assertEqual(api.calls[0][1], {"ref": "gpt", "inputs": {"source_sha": source_sha}})

    def test_missing_dispatch_stays_staged_without_verified_policy(self) -> None:
        task = {
            "task_id": "20261128-230000-04",
            "path": "workspace/tasks/20261128-230000/subtasks/04-worker-migration.md",
            "source_sha": "a" * 40,
            "policy_revision": "b" * 40,
        }
        class FakeAPI:
            def post_json(self, *_args, **_kwargs):
                self.fail("staged policy must not dispatch")
        with patch.object(recovery, "awaiting_ci_tasks", return_value=[task]), patch.object(
            recovery, "source_policy_allows_dispatch", return_value=False
        ):
            result = recovery.dispatch_missing_attempts(self.root, FakeAPI(), "dungnv2602/chatgpt", set(), set())
        self.assertEqual(result, (1, 0, 1))

    def test_existing_index_or_running_attempt_prevents_duplicate_dispatch(self) -> None:
        task = {
            "task_id": "20261128-230000-04",
            "path": "workspace/tasks/20261128-230000/subtasks/04-worker-migration.md",
            "source_sha": "a" * 40,
            "policy_revision": "b" * 40,
        }
        class FakeAPI:
            def post_json(self, *_args, **_kwargs):
                self.fail("existing attempt must not dispatch")
        with patch.object(recovery, "awaiting_ci_tasks", return_value=[task]), patch.object(
            recovery, "source_policy_allows_dispatch", return_value=True
        ):
            indexed = recovery.dispatch_missing_attempts(self.root, FakeAPI(), "dungnv2602/chatgpt", set(), {"a" * 40})
            active = recovery.dispatch_missing_attempts(self.root, FakeAPI(), "dungnv2602/chatgpt", {"a" * 40}, set())
        self.assertEqual(indexed, (1, 0, 0))
        self.assertEqual(active, (1, 0, 0))

    def test_run_cancelled_before_coordinator_jobs_is_captured(self) -> None:
        jobs = [
            {"name": "Check protected policy and duplicate source SHA", "status": "completed", "conclusion": "success"},
        ]
        kind, _ = recovery.attempt_kind(
            jobs,
            run_status="completed",
            run_conclusion="cancelled",
        )
        self.assertEqual(kind, "cancelled")

    def test_failed_dispatch_without_coordinator_is_capture_failure_candidate(self) -> None:
        kind, _ = recovery.attempt_kind(
            [],
            run_status="completed",
            run_conclusion="failure",
        )
        self.assertEqual(kind, "policy_failure")

    def test_fallback_record_contains_only_compact_status_metadata(self) -> None:
        result = recovery.fallback_aggregate(
            "a" * 40,
            "b" * 40,
            10,
            2,
            "capture_failure",
            "2026-11-28T12:00:00Z",
        )
        self.assertEqual(
            set(result),
            {
                "source_sha", "policy_blob_sha", "coordinator_run_id", "attempt",
                "check_set_id", "expected_checks", "statuses", "outcome", "completed_at",
            },
        )
        self.assertNotIn("logs", result)
        self.assertNotIn("diagnostics", result)

    def test_checkpoint_stops_before_first_unresolved_attempt(self) -> None:
        reconciled = "2026-11-28T12:00:00Z"
        records = [
            self.record(1, 1, reconciled),
            self.record(2, 1, None),
            self.record(3, 1, reconciled),
        ]
        self.write_index(records)
        changed = recovery.checkpoint_and_prune(
            self.root,
            [(1, 1, "completed"), (2, 1, "unresolved"), (3, 1, "completed")],
            datetime(2026, 11, 28, 13, 0, tzinfo=timezone.utc),
        )
        self.assertTrue(changed)
        index = publisher.validate_index(publisher.read_json(self.index_path))
        self.assertEqual(index["closed_through"], {"run_id": 1, "attempt": 1})
        self.assertEqual(len(index["attempts"]), 3)

    def test_metadata_publication_is_excluded_from_source_validation_triggers(self) -> None:
        root = Path(__file__).resolve().parents[4]
        dispatcher = (root / ".github/workflows/task-validation-dispatch.yml").read_text(encoding="utf-8")
        changed_lint = (root / ".github/workflows/ste-lint-changed.yml").read_text(encoding="utf-8")
        standards = (root / ".github/workflows/validate-document-standards.yml").read_text(encoding="utf-8")
        recovery_workflow = (root / ".github/workflows/task-validation-recovery.yml").read_text(encoding="utf-8")
        legacy_diagnostics = (root / ".github/workflows/gh-actions-diagnostics.yml").read_text(encoding="utf-8")
        self.assertIn('"workspace/task-validation/**"', dispatcher)
        self.assertIn("'workspace/task-validation/**'", legacy_diagnostics)
        self.assertIn("'!workspace/task-validation/**'", changed_lint)
        self.assertIn("'!workspace/task-validation/reviews/**'", standards)
        self.assertIn("'!workspace/task-validation/status-index.json'", standards)
        self.assertNotIn('"workspace/task-validation/status-index.json"', recovery_workflow.split("paths:", 1)[1].split("schedule:", 1)[0])
        self.assertNotIn('"workspace/task-validation/reviews/**"', recovery_workflow.split("paths:", 1)[1].split("schedule:", 1)[0])

    def test_retention_prunes_only_reconciled_attempts_after_three_days(self) -> None:
        old = "2026-11-20T12:00:00Z"
        records = [
            self.record(1, 1, old),
            self.record(2, 1, old),
            self.record(3, 1, None),
        ]
        self.write_index(records)
        for key in ("1-1", "2-1", "3-1"):
            folder = self.root / publisher.REVIEW_ROOT / key
            folder.mkdir(parents=True)
            (folder / "review.md").write_text("review", encoding="utf-8")
        changed = recovery.checkpoint_and_prune(
            self.root,
            [(1, 1, "completed"), (2, 1, "completed"), (3, 1, "unresolved")],
            datetime(2026, 11, 28, 13, 0, tzinfo=timezone.utc),
        )
        self.assertTrue(changed)
        index = publisher.validate_index(publisher.read_json(self.index_path))
        self.assertEqual(index["closed_through"], {"run_id": 2, "attempt": 1})
        self.assertEqual(
            [(item["coordinator_run_id"], item["attempt"]) for item in index["attempts"]],
            [(3, 1)],
        )
        self.assertFalse((self.root / publisher.REVIEW_ROOT / "1-1").exists())
        self.assertFalse((self.root / publisher.REVIEW_ROOT / "2-1").exists())
        self.assertTrue((self.root / publisher.REVIEW_ROOT / "3-1").exists())


if __name__ == "__main__":
    unittest.main()
