# Validate Document Standards — run 45291556980

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45291556980 / 1 |
| Run number | 229 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45291556980 |
| Branch | gpt |
| Commit | 59df9eab2f568605ab94d84fefec5b787f477448 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T23:45:36Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-26T05:09:52Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | checkout_or_action_download |
| Jobs | 1 |
| Steps | 8 |
| Issues | 1 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

checkout_or_action_download

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 138101305032 | validate-document-standards | completed | failure | 8 | logs/job-138101305032.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| checkout_or_action_download | 138101305032 | 5 | Validate the document type catalog | Blocking | medium | validate-document-standards	UNKNOWN STEP	2026-11-23T23:45:49.4870036Z ERROR: Line 106: Markdown coverage pattern matches no in-scope document: 'reports/lint_reports/latest-lint-report.md'. |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138101305032 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138101305032 | failure | .github | 16 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138101305032 | validate-document-standards | logs/job-138101305032.log | 31415 | False | validate-document-standards	UNKNOWN STEP	2026-11-23T23:45:49.4870036Z ERROR: Line 106: Markdown coverage pattern matches no in-scope document: 'reports/lint_reports/latest-lint-report.md'., validate-document-standards	UNKNOWN STEP	2026-11-23T23:45:49.4871213Z ERROR: Line 108: Markdown coverage pattern matches no in-scope document: 'reports/lint_reports/on_*/latest-lint-report.md'., validate-document-standards	UNKNOWN STEP	2026-11-23T23:45:49.4872378Z ERROR: Line 109: Markdown coverage pattern matches no in-scope document: 'reports/lint_reports/on_*/history/**/*.md'., validate-document-standards	UNKNOWN STEP	2026-11-23T23:45:49.4873508Z Catalog validation failed: 3 error(s), 33 document type(s), 73 reference(s)., validate-document-standards	UNKNOWN STEP	2026-11-23T23:45:49.4924295Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.