"""Regression tests for task-trailer contract resolution."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_task_validation_contract as builder


class BuildTaskValidationContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.task_id = "20261128-230000-02"
        self.task_path = self.root / "workspace/tasks/20261128-230000/subtasks/02-verifier.md"
        self.task_path.parent.mkdir(parents=True)
        self.task_path.write_text(
            "- **ID:** 20261128-230000-02\n\n"
            "## Validation Contract\n\n"
            "```json\n"
            '{"contract_revision":"1","checks":[]}\n'
            "```\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_builds_contract_bound_to_source_sha(self) -> None:
        source_sha = "a" * 40
        contract, task_id = builder.build_contract(
            self.root, source_sha, "Implement verifier\n\nTask-ID: 20261128-230000-02\n"
        )
        self.assertEqual(task_id, self.task_id)
        self.assertEqual(contract["source_sha"], source_sha)
        self.assertEqual(contract["schema_version"], 1)
        self.assertEqual(contract["checks"], [])

    def test_rejects_missing_task_id_trailer(self) -> None:
        with self.assertRaises(builder.TaskContractError):
            builder.extract_task_id("Implement verifier\n")

    def test_rejects_duplicate_task_id_trailers(self) -> None:
        message = "Task-ID: 20261128-230000-02\nTask-ID: 20261128-230000-02\n"
        with self.assertRaises(builder.TaskContractError):
            builder.extract_task_id(message)

    def test_rejects_malformed_task_id(self) -> None:
        with self.assertRaises(builder.TaskContractError):
            builder.extract_task_id("Task-ID: ../task\n")

    def test_rejects_missing_task_record(self) -> None:
        with self.assertRaises(builder.TaskContractError):
            builder.build_contract(self.root, "a" * 40, "Task-ID: 20261128-230000-03\n")

    def test_rejects_missing_contract_block(self) -> None:
        self.task_path.write_text("- **ID:** 20261128-230000-02\n", encoding="utf-8")
        with self.assertRaises(builder.TaskContractError):
            builder.build_contract(self.root, "a" * 40, "Task-ID: 20261128-230000-02\n")

    def test_rejects_invalid_contract_json(self) -> None:
        self.task_path.write_text(
            "- **ID:** 20261128-230000-02\n\n## Validation Contract\n"
            "```json\n{invalid}\n```\n",
            encoding="utf-8",
        )
        with self.assertRaises(builder.TaskContractError):
            builder.build_contract(self.root, "a" * 40, "Task-ID: 20261128-230000-02\n")

    def test_rejects_unknown_contract_fields(self) -> None:
        self.task_path.write_text(
            "- **ID:** 20261128-230000-02\n\n## Validation Contract\n"
            "```json\n"
            '{"contract_revision":"1","checks":[],"shell":"unsafe"}\n'
            "```\n",
            encoding="utf-8",
        )
        with self.assertRaises(builder.TaskContractError):
            builder.build_contract(self.root, "a" * 40, "Task-ID: 20261128-230000-02\n")

    def test_rejects_invalid_source_sha(self) -> None:
        with self.assertRaises(builder.TaskContractError):
            builder.build_contract(self.root, "not-a-sha", "Task-ID: 20261128-230000-02\n")


if __name__ == "__main__":
    unittest.main()
