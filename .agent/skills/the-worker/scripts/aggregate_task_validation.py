#!/usr/bin/env python3
"""Classify one complete ADR-0008 validation attempt."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


class AggregateError(ValueError):
    """Raised when the expected manifest or result set is invalid."""


def read_object(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise AggregateError(f"Cannot read JSON object from {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise AggregateError(f"Expected a JSON object in {path}")
    return value


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def canonical_check_set(policy: dict[str, Any], task_check_ids: list[str]) -> tuple[list[str], str]:
    mandatory = policy.get("mandatory_checks")
    if not isinstance(mandatory, list) or not mandatory:
        raise AggregateError("Policy mandatory_checks must be a non-empty array")
    mandatory_ids = []
    for item in mandatory:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            raise AggregateError("Every mandatory check must have a string id")
        mandatory_ids.append(item["id"])
    if len(set(mandatory_ids)) != len(mandatory_ids):
        raise AggregateError("Policy contains duplicate mandatory check IDs")
    if len(set(task_check_ids)) != len(task_check_ids):
        raise AggregateError("Task contract contains duplicate check IDs")
    if set(mandatory_ids) & set(task_check_ids):
        raise AggregateError("Task checks cannot override mandatory check IDs")
    expected = mandatory_ids + sorted(task_check_ids)
    identity = hashlib.sha256(
        json.dumps(expected, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    ).hexdigest()
    return expected, identity


def classify_attempt(
    policy: dict[str, Any],
    records: list[dict[str, Any]],
    source_sha: str,
    policy_blob_sha: str,
    coordinator_run_id: str,
    attempt: int,
    task_check_ids: list[str],
) -> dict[str, Any]:
    expected, check_set_id = canonical_check_set(policy, task_check_ids)
    by_id: dict[str, dict[str, Any]] = {}
    duplicate_ids: set[str] = set()
    for record in records:
        if not isinstance(record, dict) or not isinstance(record.get("check_id"), str):
            raise AggregateError("Each check result must contain a string check_id")
        check_id = record["check_id"]
        if check_id in by_id:
            duplicate_ids.add(check_id)
        by_id[check_id] = record

    if duplicate_ids:
        return {
            "outcome": "coverage_failure",
            "reason": "Duplicate check result records",
            "duplicate_checks": sorted(duplicate_ids),
            "expected_checks": expected,
            "check_set_id": check_set_id,
        }

    unexpected = sorted(set(by_id) - set(expected))
    missing = sorted(set(expected) - set(by_id))
    if unexpected:
        return {
            "outcome": "coverage_failure",
            "reason": "Unexpected check result records",
            "unexpected_checks": unexpected,
            "missing_checks": missing,
            "expected_checks": expected,
            "check_set_id": check_set_id,
        }
    if missing:
        return {
            "outcome": "coverage_failure",
            "reason": "One or more expected checks have no result",
            "missing_checks": missing,
            "expected_checks": expected,
            "check_set_id": check_set_id,
        }

    for check_id, record in by_id.items():
        if record.get("source_sha") != source_sha:
            return {"outcome": "coverage_failure", "reason": f"Source SHA mismatch for {check_id}", "check_set_id": check_set_id}
        if record.get("policy_blob_sha") != policy_blob_sha:
            return {"outcome": "coverage_failure", "reason": f"Policy blob mismatch for {check_id}", "check_set_id": check_set_id}
        if record.get("check_set_id") != check_set_id:
            return {"outcome": "coverage_failure", "reason": f"Check-set identity mismatch for {check_id}", "check_set_id": check_set_id}
        if str(record.get("coordinator_run_id")) != str(coordinator_run_id):
            return {"outcome": "coverage_failure", "reason": f"Coordinator run mismatch for {check_id}", "check_set_id": check_set_id}
        if record.get("attempt") != attempt:
            return {"outcome": "coverage_failure", "reason": f"Attempt mismatch for {check_id}", "check_set_id": check_set_id}

    statuses = {check_id: by_id[check_id].get("status") for check_id in expected}
    if "superseded" in statuses.values():
        outcome = "superseded"
    elif "cancelled" in statuses.values():
        outcome = "cancelled"
    elif "capture_failure" in statuses.values():
        outcome = "capture_failure"
    elif "infrastructure_failure" in statuses.values():
        outcome = "infrastructure_failure"
    elif any(status in {"skipped", "pending", "partial", "neutral", None} for status in statuses.values()):
        outcome = "coverage_failure"
    elif any(status != "success" for status in statuses.values()):
        outcome = "check_failure"
    else:
        outcome = "success"

    return {
        "outcome": outcome,
        "expected_checks": expected,
        "check_set_id": check_set_id,
        "check_statuses": statuses,
        "source_sha": source_sha,
        "policy_blob_sha": policy_blob_sha,
        "coordinator_run_id": str(coordinator_run_id),
        "attempt": attempt,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", type=Path, required=True)
    parser.add_argument("--policy-blob-sha", required=True)
    parser.add_argument("--source-sha", required=True)
    parser.add_argument("--coordinator-run-id", required=True)
    parser.add_argument("--attempt", type=int, required=True)
    parser.add_argument("--task-check-ids", default="[]")
    parser.add_argument("--results", type=Path, required=True)
    args = parser.parse_args()

    try:
        if not re.fullmatch(r"[0-9a-f]{40}", args.source_sha):
            raise AggregateError("source SHA must be 40 lowercase hexadecimal characters")
        if not re.fullmatch(r"[0-9a-f]{40}", args.policy_blob_sha):
            raise AggregateError("policy blob SHA must be 40 lowercase hexadecimal characters")
        if not args.coordinator_run_id or args.attempt < 1:
            raise AggregateError("Coordinator run ID and positive attempt are required")
        policy = read_object(args.policy)
        if blob_sha(args.policy) != args.policy_blob_sha:
            raise AggregateError("Policy blob SHA does not match the supplied policy")
        task_check_ids = json.loads(args.task_check_ids)
        if not isinstance(task_check_ids, list) or any(not isinstance(value, str) for value in task_check_ids):
            raise AggregateError("task-check-ids must be a JSON array of strings")
        results_value = json.loads(args.results.read_text(encoding="utf-8"))
        if not isinstance(results_value, list):
            raise AggregateError("results must be a JSON array")
        result = classify_attempt(
            policy, results_value, args.source_sha, args.policy_blob_sha,
            args.coordinator_run_id, args.attempt, task_check_ids,
        )
        print(json.dumps(result, ensure_ascii=False))
        return 0 if result["outcome"] == "success" else 1
    except (AggregateError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(json.dumps({"outcome": "coverage_failure", "reason": str(exc)}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
