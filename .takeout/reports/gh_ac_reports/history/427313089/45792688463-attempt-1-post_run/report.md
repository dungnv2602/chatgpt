# Validate Document Standards — run 45792688463

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45792688463 / 1 |
| Run number | 583 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45792688463 |
| Branch | gpt |
| Commit | 73b40460947e9f651d52da893ed1fc870df8fdb6 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-26T09:31:01Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-26T10:13:37Z |

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
| 139815417727 | validate-document-standards | completed | failure | 9 | logs/job-139815417727.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 139815417727 | 4 | Run CI Ledger regression tests | Blocking | medium | 2026-11-26T09:31:10.5437451Z Traceback (most recent call last): |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 139815417727 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 139815417727 | failure | .github | 111 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 139815417727 | validate-document-standards | logs/job-139815417727.log | 64600 | False | validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:31:10.5437451Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:31:10.5507000Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:31:10.5575417Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:31:10.5622110Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:31:10.5658191Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:31:10.5694478Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:31:10.5697500Z FAILED (failures=6), validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:31:10.5710855Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.