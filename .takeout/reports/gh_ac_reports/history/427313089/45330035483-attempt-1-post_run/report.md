# Validate Document Standards — run 45330035483

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45330035483 / 1 |
| Run number | 248 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45330035483 |
| Branch | gpt |
| Commit | 1a4926f94355ac468f697dd4f7bd2c2734f089ca |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T04:58:27Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-24T06:17:43Z |

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
| 138228782779 | validate-document-standards | completed | failure | 8 | logs/job-138228782779.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| checkout_or_action_download | 138228782779 | 5 | Validate the document type catalog | Blocking | medium | validate-document-standards	UNKNOWN STEP	2026-11-24T04:58:42.0512454Z ERROR: 3 Markdown file(s) are not covered by the catalog: images/takeout/history/2026-11-20-001/attempt-001/verification-report.md, images/takeout/history/2026-11-20-001/attempt-002/verification-report.md, images/takeout/history/2026-11-20-001/attempt-003/verification-report.md. |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138228782779 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138228782779 | failure | .github | 14 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138228782779 | validate-document-standards | logs/job-138228782779.log | 31962 | False | validate-document-standards	UNKNOWN STEP	2026-11-24T04:58:42.0512454Z ERROR: 3 Markdown file(s) are not covered by the catalog: images/takeout/history/2026-11-20-001/attempt-001/verification-report.md, images/takeout/history/2026-11-20-001/attempt-002/verification-report.md, images/takeout/history/2026-11-20-001/attempt-003/verification-report.md., validate-document-standards	UNKNOWN STEP	2026-11-24T04:58:42.0514486Z Catalog validation failed: 1 error(s), 33 document type(s), 73 reference(s)., validate-document-standards	UNKNOWN STEP	2026-11-24T04:58:42.0563991Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.