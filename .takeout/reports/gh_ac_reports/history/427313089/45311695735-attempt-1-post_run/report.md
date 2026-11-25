# Validate Document Standards — run 45311695735

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45311695735 / 1 |
| Run number | 243 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45311695735 |
| Branch | gpt |
| Commit | ff1f6341c07bb468b5b387dbf50c5266cbdfcafe |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T02:20:52Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-24T06:17:12Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
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
| 138168722995 | validate-document-standards | completed | failure | 8 | logs/job-138168722995.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| checkout_or_action_download | 138168722995 | 5 | Validate the document type catalog | Blocking | medium | validate-document-standards	UNKNOWN STEP	2026-11-24T02:21:05.5600706Z ERROR: 1 Markdown file(s) are not covered by the catalog: images/takeout/history/2026-11-20-001/attempt-001/verification-report.md. |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138168722995 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138168722995 | failure | .github | 14 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138168722995 | validate-document-standards | logs/job-138168722995.log | 31814 | False | validate-document-standards	UNKNOWN STEP	2026-11-24T02:21:05.5600706Z ERROR: 1 Markdown file(s) are not covered by the catalog: images/takeout/history/2026-11-20-001/attempt-001/verification-report.md., validate-document-standards	UNKNOWN STEP	2026-11-24T02:21:05.5602278Z Catalog validation failed: 1 error(s), 33 document type(s), 73 reference(s)., validate-document-standards	UNKNOWN STEP	2026-11-24T02:21:05.5676521Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.