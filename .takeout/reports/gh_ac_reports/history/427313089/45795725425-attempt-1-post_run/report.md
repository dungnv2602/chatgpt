# Validate Document Standards — run 45795725425

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45795725425 / 1 |
| Run number | 603 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45795725425 |
| Branch | gpt |
| Commit | 6340fa673a4f927692a0a94b03204b0bff6cf71d |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-26T09:50:36Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-26T10:14:49Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | publication_or_push |
| Jobs | 1 |
| Steps | 9 |
| Issues | 1 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

publication_or_push

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 139825848472 | validate-document-standards | completed | failure | 9 | logs/job-139825848472.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| publication_or_push | 139825848472 | 4 | Run CI Ledger regression tests | Blocking | high | 2026-11-26T09:50:59.0007701Z Traceback (most recent call last): |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 139825848472 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 139825848472 | failure | .github | 138 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 139825848472 | validate-document-standards | logs/job-139825848472.log | 66858 | False | validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:50:59.0007701Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:50:59.0028193Z AssertionError: 'python3 .takeout/reports/gh_ac_reports/scripts/report.py' not found in 'name: Capture GitHub Actions diagnostics\ndescription: Validate diagnostic tools, capture source-workflow failures, update the issue ledger, create grouped Worker tasks for new actionable findings, and publish evidence.\nruns:\n  using: composite\n  steps:\n    - name: Set up Python\n      uses: actions/setup-python@v5\n , validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:50:59.0038493Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:50:59.0076218Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:50:59.0115514Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:50:59.0122415Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:50:59.0158448Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:50:59.0194955Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:50:59.0199190Z Traceback (most recent call last):, validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:50:59.0202114Z FAILED (failures=8), validate-document-standards	Run CI Ledger regression tests	2026-11-26T09:50:59.0214639Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.