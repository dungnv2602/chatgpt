from __future__ import annotations

import json
import tempfile
import unittest
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
