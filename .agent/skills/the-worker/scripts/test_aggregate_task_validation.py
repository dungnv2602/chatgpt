"""Regression tests for exact-SHA ADR-0008 result aggregation."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aggregate_task_validation as aggregate


class AggregateTaskValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.policy = {
            "policy_id": "chatgpt-task-validation",
            "repository": "dungnv2602/chatgpt",
            "coordinator": {"activation_status": "enabled"},
            "protection": {"enforcement_status": "verified"},
            "mandatory_checks": [
                {"id": "lint"},
                {"id": "document-standards"},
            ],
        }
        self.source_sha = "a" * 40
        self.policy_sha = "b" * 40
        self.run_id = "12345"
        self.attempt = 1
        self.task_contract = {
            "schema_version": 1,
            "source_sha": self.source_sha,
            "contract_revision": "1",
            "checks": [],
        }
        self.expected, self.check_set_id = aggregate.canonical_check_set(self.policy, self.task_contract)

    def records(self, statuses=None, expected=None, check_set_id=None):
        statuses = statuses or {}
        expected = self.expected if expected is None else expected
        check_set_id = self.check_set_id if check_set_id is None else check_set_id
        return [
            {
                "check_id": check_id,
                "status": statuses.get(check_id, "success"),
                "source_sha": self.source_sha,
                "policy_blob_sha": self.policy_sha,
                "check_set_id": check_set_id,
                "coordinator_run_id": self.run_id,
                "attempt": self.attempt,
            }
            for check_id in expected
        ]

    def classify(self, records=None, task_contract=None):
        return aggregate.classify_attempt(
            self.policy,
            self.records() if records is None else records,
            self.source_sha,
            self.policy_sha,
            self.run_id,
            self.attempt,
            self.task_contract if task_contract is None else task_contract,
        )

    def test_all_exact_matching_successes_pass(self) -> None:
        self.assertEqual(self.classify()["outcome"], "success")

    def test_missing_result_is_coverage_failure(self) -> None:
        self.assertEqual(self.classify(self.records()[:1])["outcome"], "coverage_failure")

    def test_skipped_result_is_coverage_failure(self) -> None:
        self.assertEqual(self.classify(self.records({"lint": "skipped"}))["outcome"], "coverage_failure")

    def test_pending_and_partial_results_are_not_success(self) -> None:
        for status in ("pending", "queued", "in_progress", "partial", "neutral"):
            with self.subTest(status=status):
                self.assertEqual(self.classify(self.records({"lint": status}))["outcome"], "coverage_failure")

    def test_failed_check_is_check_failure(self) -> None:
        self.assertEqual(self.classify(self.records({"lint": "failure"}))["outcome"], "check_failure")

    def test_cancelled_attempt_is_terminal_cancelled(self) -> None:
        self.assertEqual(self.classify(self.records({"lint": "cancelled"}))["outcome"], "cancelled")

    def test_superseded_attempt_is_terminal_superseded(self) -> None:
        self.assertEqual(self.classify(self.records({"lint": "superseded"}))["outcome"], "superseded")

    def test_infrastructure_and_capture_failures_are_distinct(self) -> None:
        self.assertEqual(self.classify(self.records({"lint": "infrastructure_failure"}))["outcome"], "infrastructure_failure")
        self.assertEqual(self.classify(self.records({"lint": "capture_failure"}))["outcome"], "capture_failure")

    def test_source_sha_mismatch_is_coverage_failure(self) -> None:
        records = self.records()
        records[0]["source_sha"] = "c" * 40
        self.assertEqual(self.classify(records)["outcome"], "coverage_failure")

    def test_policy_revision_mismatch_is_coverage_failure(self) -> None:
        records = self.records()
        records[0]["policy_blob_sha"] = "c" * 40
        self.assertEqual(self.classify(records)["outcome"], "coverage_failure")

    def test_check_set_mismatch_is_coverage_failure(self) -> None:
        records = self.records()
        records[0]["check_set_id"] = "wrong"
        self.assertEqual(self.classify(records)["outcome"], "coverage_failure")

    def test_coordinator_run_and_attempt_must_match(self) -> None:
        records = self.records()
        records[0]["coordinator_run_id"] = "other"
        self.assertEqual(self.classify(records)["outcome"], "coverage_failure")
        records = self.records()
        records[0]["attempt"] = 2
        self.assertEqual(self.classify(records)["outcome"], "coverage_failure")

    def test_duplicate_and_unexpected_records_are_coverage_failures(self) -> None:
        records = self.records()
        records.append(dict(records[0]))
        self.assertEqual(self.classify(records)["outcome"], "coverage_failure")
        records = self.records()
        records.append(dict(records[0], check_id="unexpected"))
        self.assertEqual(self.classify(records)["outcome"], "coverage_failure")

    def test_task_checks_extend_the_expected_set(self) -> None:
        task_contract = {
            **self.task_contract,
            "checks": [{
                "id": "task-extra",
                "adapter": "python-script",
                "entrypoint": "scripts/check.py",
                "args": ["--strict"],
                "timeout_minutes": 10,
            }],
        }
        expected, identity = aggregate.canonical_check_set(self.policy, task_contract)
        records = self.records(expected=expected, check_set_id=identity)
        result = self.classify(records, task_contract)
        self.assertEqual(expected, ["lint", "document-standards"])
        self.assertEqual(result["expected_checks"], expected)
        self.assertEqual(result["outcome"], "success")

    def test_task_check_arguments_change_check_set_identity(self) -> None:
        first = {
            **self.task_contract,
            "checks": [{
                "id": "task-extra",
                "adapter": "python-script",
                "entrypoint": "scripts/check.py",
                "args": ["--strict"],
                "timeout_minutes": 10,
            }],
        }
        second = {
            **first,
            "checks": [{
                "id": "task-extra",
                "adapter": "python-script",
                "entrypoint": "scripts/check.py",
                "args": ["--relaxed"],
                "timeout_minutes": 10,
            }],
        }
        self.assertNotEqual(
            aggregate.canonical_check_set(self.policy, first)[1],
            aggregate.canonical_check_set(self.policy, second)[1],
        )

    def test_contract_source_sha_must_match(self) -> None:
        contract = {**self.task_contract, "source_sha": "c" * 40}
        with self.assertRaises(aggregate.AggregateError):
            aggregate.classify_attempt(
                self.policy, self.records(), self.source_sha, self.policy_sha,
                self.run_id, self.attempt, contract,
            )

    def test_task_checks_cannot_override_mandatory_ids(self) -> None:
        contract = {
            **self.task_contract,
            "checks": [{
                "id": "lint",
                "adapter": "python-script",
                "entrypoint": "scripts/check.py",
            }],
        }
        with self.assertRaises(aggregate.AggregateError):
            aggregate.canonical_check_set(self.policy, contract)

    def test_unverified_policy_cannot_aggregate_success(self) -> None:
        policy = {**self.policy, "protection": {"enforcement_status": "external-prerequisite"}}
        with self.assertRaises(aggregate.AggregateError):
            aggregate.classify_attempt(
                policy, self.records(), self.source_sha, self.policy_sha,
                self.run_id, self.attempt, self.task_contract,
            )

    def test_staged_coordinator_cannot_aggregate_success(self) -> None:
        policy = {**self.policy, "coordinator": {"activation_status": "staged"}}
        with self.assertRaises(aggregate.AggregateError):
            aggregate.classify_attempt(
                policy, self.records(), self.source_sha, self.policy_sha,
                self.run_id, self.attempt, self.task_contract,
            )


if __name__ == "__main__":
    unittest.main()
