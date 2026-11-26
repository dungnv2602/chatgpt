# Validate Document Standards — run 45798838831

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45798838831 / 1 |
| Run number | 608 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45798838831 |
| Branch | gpt |
| Commit | 01c2cff6f33f7b75ae42d984b448312b806e0d9f |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-26T10:10:30Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-26T10:15:11Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | validation_or_test |
| Jobs | 1 |
| Steps | 9 |
| Issues | 1 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

validation_or_test

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 139837019100 | validate-document-standards | completed | failure | 9 | logs/job-139837019100.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 139837019100 | 4 | Run CI Ledger regression tests | Blocking | medium | 2026-11-26T10:11:46.8637725Z test_processed_actions_paths_are_pruned_when_removed_from_active_history (test_ledger.LedgerTests.test_processed_actions_paths_are_pruned_when_removed_from_active_history) ... ERROR |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 139837019100 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 139837019100 | failure | .github | 72 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 139837019100 | validate-document-standards | logs/job-139837019100.log | 36049 | False | validate-document-standards	Run CI Ledger regression tests	2026-11-26T10:11:46.8637725Z test_processed_actions_paths_are_pruned_when_removed_from_active_history (test_ledger.LedgerTests.test_processed_actions_paths_are_pruned_when_removed_from_active_history) ... ERROR, validate-document-standards	Run CI Ledger regression tests	2026-11-26T10:11:46.9105436Z ERROR: test_processed_actions_paths_are_pruned_when_removed_from_active_history (test_ledger.LedgerTests.test_processed_actions_paths_are_pruned_when_removed_from_active_history), validate-document-standards	Run CI Ledger regression tests	2026-11-26T10:11:46.9107470Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T10:11:46.9122699Z FAILED (errors=1), validate-document-standards	Run CI Ledger regression tests	2026-11-26T10:11:46.9242022Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.