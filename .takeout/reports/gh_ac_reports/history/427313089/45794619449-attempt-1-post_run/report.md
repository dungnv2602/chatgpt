# Validate Document Standards — run 45794619449

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45794619449 / 1 |
| Run number | 590 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45794619449 |
| Branch | gpt |
| Commit | 3f6f505f904e81ec3f3b47796190e1f03ba879ff |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-26T09:43:30Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-26T10:14:10Z |

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
| 139822657635 | validate-document-standards | completed | failure | 9 | logs/job-139822657635.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 139822657635 | 4 | Run CI Ledger regression tests | Blocking | medium | 2026-11-26T09:45:01.8534221Z Traceback (most recent call last): |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 139822657635 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 139822657635 | failure | .github | 111 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 139822657635 | validate-document-standards | logs/job-139822657635.log | 65087 | False | validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:45:01.8534221Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:45:01.8564110Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:45:01.8590730Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:45:01.8616684Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:45:01.8642054Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:45:01.8666716Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:45:01.8669481Z FAILED (failures=6), validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:45:01.8679433Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.