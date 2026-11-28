from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import publish_task_validation as publisher


class PublisherTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.task_id = "20261128-230000"
        task = self.root / "workspace/tasks" / self.task_id / "task.md"
        task.parent.mkdir(parents=True)
        task.write_text(f"- **ID:** {self.task_id}\n- **Origin:** User\n", encoding="utf-8")
        (self.root / publisher.INDEX_PATH).parent.mkdir(parents=True)
        (self.root / publisher.INDEX_PATH).write_text(
            json.dumps({"schema_version": 1, "closed_through": {"run_id": 0, "attempt": 0}, "attempts": []}),
            encoding="utf-8",
        )
        template = self.root / publisher.REVIEW_TEMPLATE
        template.parent.mkdir(parents=True)
        template.write_text(
            "# Review\nTask {{source_task_id}} SHA {{source_sha}} Run {{coordinator_run_id}} "
            "Attempt {{attempt}} Check {{check_set_id}} Policy {{policy_revision}} "
            "Completed {{completed_at}} Outcome {{outcome}} Actions {{actions_url}}\n",
            encoding="utf-8",
        )
        self.git("init")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.invalid")
        self.git("add", ".")
        self.git("commit", "-m", "Add source task\n\nTask-ID: " + self.task_id)
        self.source_sha = self.git("rev-parse", "HEAD")
        self.policy_sha = "b" * 40
        self.check_set_id = "c" * 64
        self.completed_at = "2026-11-28T12:00:00Z"
        self.actions_url = "https://github.com/dungnv2602/chatgpt/actions/runs/123"
        self.aggregate = {
            "source_sha": self.source_sha,
            "policy_blob_sha": self.policy_sha,
            "coordinator_run_id": 123,
            "attempt": 1,
            "check_set_id": self.check_set_id,
            "expected_checks": ["lint"],
            "statuses": {"lint": "success"},
            "outcome": "success",
            "completed_at": self.completed_at,
        }

    def tearDown(self) -> None:
        self.temp.cleanup()

    def git(self, *args: str) -> str:
        result = subprocess.run(
            ["git", *args],
            cwd=self.root,
            shell=False,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()

    def publish(self, aggregate: dict | None = None, run_id: int = 123, attempt: int = 1) -> bool:
        return publisher.publish_attempt(
            self.root,
            aggregate or self.aggregate,
            self.source_sha,
            self.policy_sha,
            run_id,
            attempt,
            f"https://github.com/dungnv2602/chatgpt/actions/runs/{run_id}",
            self.completed_at,
        )

    def test_publishes_status_and_review_folder(self) -> None:
        self.assertTrue(self.publish())
        index = json.loads((self.root / publisher.INDEX_PATH).read_text(encoding="utf-8"))
        self.assertEqual(len(index["attempts"]), 1)
        self.assertEqual(index["attempts"][0]["source_task_id"], self.task_id)
        review = self.root / publisher.REVIEW_ROOT / "123-1" / "review.md"
        self.assertTrue(review.is_file())
        self.assertIn("Outcome success", review.read_text(encoding="utf-8"))

    def test_duplicate_publication_is_idempotent(self) -> None:
        self.assertTrue(self.publish())
        self.assertFalse(self.publish())
        index = json.loads((self.root / publisher.INDEX_PATH).read_text(encoding="utf-8"))
        self.assertEqual(len(index["attempts"]), 1)

    def test_conflicting_duplicate_is_rejected(self) -> None:
        self.assertTrue(self.publish())
        changed = dict(self.aggregate)
        changed["outcome"] = "check_failure"
        changed["statuses"] = {"lint": "failure"}
        with self.assertRaises(publisher.PublisherError):
            self.publish(changed)

    def test_cancelled_attempt_has_no_review_folder(self) -> None:
        cancelled = dict(self.aggregate)
        cancelled.update({
            "coordinator_run_id": 124,
            "outcome": "cancelled",
            "statuses": {"lint": "cancelled"},
        })
        self.assertTrue(self.publish(cancelled, run_id=124))
        self.assertFalse((self.root / publisher.REVIEW_ROOT / "124-1").exists())
        index = json.loads((self.root / publisher.INDEX_PATH).read_text(encoding="utf-8"))
        self.assertEqual(index["attempts"][-1]["outcome"], "cancelled")
        self.assertIsNotNone(index["attempts"][-1]["recovery"]["reconciled_at"])

    def test_cancelled_attempt_without_check_set_is_valid(self) -> None:
        cancelled = dict(self.aggregate)
        cancelled.update({
            "coordinator_run_id": 126,
            "check_set_id": None,
            "expected_checks": [],
            "statuses": {},
            "outcome": "cancelled",
        })
        self.assertTrue(self.publish(cancelled, run_id=126))
        index = publisher.validate_index(publisher.read_json(self.root / publisher.INDEX_PATH))
        self.assertIsNone(index["attempts"][-1]["check_set_id"])
        self.assertEqual(index["attempts"][-1]["outcome"], "cancelled")

    def test_superseded_attempt_has_no_review_folder(self) -> None:
        superseded = dict(self.aggregate)
        superseded.update({
            "coordinator_run_id": 125,
            "outcome": "superseded",
            "statuses": {"lint": "superseded"},
        })
        self.assertTrue(self.publish(superseded, run_id=125))
        self.assertFalse((self.root / publisher.REVIEW_ROOT / "125-1").exists())

    def test_delayed_attempt_below_checkpoint_is_ignored(self) -> None:
        index_path = self.root / publisher.INDEX_PATH
        index = json.loads(index_path.read_text(encoding="utf-8"))
        index["closed_through"] = {"run_id": 200, "attempt": 1}
        index_path.write_text(json.dumps(index), encoding="utf-8")
        self.assertFalse(self.publish())
        self.assertFalse((self.root / publisher.REVIEW_ROOT / "123-1").exists())

    def test_rejects_duplicate_json_keys(self) -> None:
        aggregate_path = self.root / "duplicate.json"
        aggregate_path.write_text('{"outcome":"success","outcome":"failure"}', encoding="utf-8")
        with self.assertRaises(publisher.PublisherError):
            publisher.read_json(aggregate_path)


if __name__ == "__main__":
    unittest.main()
