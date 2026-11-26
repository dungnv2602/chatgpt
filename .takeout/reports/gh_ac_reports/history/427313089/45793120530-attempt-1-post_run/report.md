# Validate Document Standards — run 45793120530

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45793120530 / 1 |
| Run number | 585 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45793120530 |
| Branch | gpt |
| Commit | 46327b632172b4bba5616db254c6c06b1ecc6f32 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-26T09:33:48Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-26T10:13:46Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
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
| 139816877756 | validate-document-standards | completed | failure | 9 | logs/job-139816877756.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 139816877756 | 4 | Run CI Ledger regression tests | Blocking | medium | 2026-11-26T09:33:57.3341242Z Traceback (most recent call last): |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 139816877756 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 139816877756 | failure | .github | 111 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 139816877756 | validate-document-standards | logs/job-139816877756.log | 64938 | False | validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:33:57.3341242Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:33:57.3413017Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:33:57.3479401Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:33:57.3517130Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:33:57.3553390Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:33:57.3589711Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:33:57.3592872Z FAILED (failures=6), validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:33:57.3604357Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.