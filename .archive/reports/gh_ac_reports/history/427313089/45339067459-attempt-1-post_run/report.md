# Validate Document Standards — run 45339067459

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45339067459 / 1 |
| Run number | 266 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45339067459 |
| Branch | gpt |
| Commit | 667b1be4b3b1f369cc4898956327674f0a923003 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T06:15:11Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-24T06:30:19Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | validation_or_test |
| Jobs | 1 |
| Steps | 8 |
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
| 138258048097 | validate-document-standards | completed | failure | 8 | logs/job-138258048097.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 138258048097 | 5 | Validate the document type catalog | Blocking | medium | 2026-11-24T06:15:27.8163354Z ERROR: Line 55: referenced file does not exist: images/takeout/history/&lt;batch&gt;/&lt;attempt&gt;/verification-report.md. |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138258048097 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138258048097 | failure | .github | 14 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138258048097 | validate-document-standards | logs/job-138258048097.log | 34150 | False | validate-document-standards	Validate the document type catalog	2026-11-24T06:15:27.8163354Z ERROR: Line 55: referenced file does not exist: images/takeout/history/&lt;batch&gt;/&lt;attempt&gt;/verification-report.md., validate-document-standards	Validate the document type catalog	2026-11-24T06:15:27.8164650Z Catalog validation failed: 1 error(s), 33 document type(s), 74 reference(s)., validate-document-standards	Validate the document type catalog	2026-11-24T06:15:27.8226576Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.