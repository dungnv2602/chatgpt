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
            "mandatory_checks": [
                {"id": "lint"},
                {"id": "document-standards"},
            ]
        }
        self.source_sha = "a" * 40
        self.policy_sha = "b" * 40
        self.run_id = "12345"
        self.attempt = 1
        self.expected, self.check_set_id = aggregate.canonical_check_set(self.policy, [])

    def records(self, statuses=None):
        statuses = statuses or {}
        return [
            {
                "check_id": check_id,
                "status": statuses.get(check_id, "success"),
                "source_sha": self.source_sha,
                "policy_blob_sha": self.policy_sha,
                "check_set_id": self.check_set_id,
                "coordinator_run_id": self.run_id,
                "attempt": self.attempt,
            }
            for check_id in self.expected
        ]

    def classify(self, records=None, task_check_ids=None):
        return aggregate.classify_attempt(
            self.policy,
            self.records() if records is None else records,
            self.source_sha,
            self.policy_sha,
            self.run_id,
            self.attempt,
            [] if task_check_ids is None else task_check_ids,
        )

    def test_all_exact_matching_successes_pass(self) -> None:
        self.assertEqual(self.classify()["outcome"], "success")

    def test_missing_result_is_coverage_failure(self) -> None:
        self.assertEqual(self.classify(self.records()[:1])["outcome"], "coverage_failure")

    def test_skipped_result_is_coverage_failure(self) -> None:
        self.assertEqual(self.classify(self.records({"lint": "skipped"}))["outcome"], "coverage_failure")

    def test_pending_and_partial_results_are_not_success(self) -> None:
        for status in ("pending", "partial", "neutral"):
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
        expected, identity = aggregate.canonical_check_set(self.policy, ["task-extra"])
        records = self.records()
        for record in records:
            record["check_set_id"] = identity
        records.append({
            "check_id": "task-extra",
            "status": "success",
            "source_sha": self.source_sha,
            "policy_blob_sha": self.policy_sha,
            "check_set_id": identity,
            "coordinator_run_id": self.run_id,
            "attempt": self.attempt,
        })
        result = aggregate.classify_attempt(
            self.policy, records, self.source_sha, self.policy_sha,
            self.run_id, self.attempt, ["task-extra"],
        )
        self.assertEqual(result["expected_checks"], expected)
        self.assertEqual(result["outcome"], "success")

    def test_task_checks_cannot_override_mandatory_ids(self) -> None:
        with self.assertRaises(aggregate.AggregateError):
            aggregate.canonical_check_set(self.policy, ["lint"])


if __name__ == "__main__":
    unittest.main()
