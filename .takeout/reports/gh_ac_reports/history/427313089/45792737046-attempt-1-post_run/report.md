# Validate Document Standards — run 45792737046

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45792737046 / 1 |
| Run number | 584 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45792737046 |
| Branch | gpt |
| Commit | a366786103f62c68a68fd4dccea812ed39407001 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-26T09:31:20Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-26T10:13:42Z |

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
| 139815764864 | validate-document-standards | completed | failure | 9 | logs/job-139815764864.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 139815764864 | 4 | Run CI Ledger regression tests | Blocking | medium | 2026-11-26T09:31:50.5841553Z Traceback (most recent call last): |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 139815764864 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 139815764864 | failure | .github | 111 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 139815764864 | validate-document-standards | logs/job-139815764864.log | 64597 | False | validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:31:50.5841553Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:31:50.5880004Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:31:50.5912799Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:31:50.5944553Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:31:50.5975585Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:31:50.6006905Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:31:50.6008890Z FAILED (failures=6), validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:31:50.6023806Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.