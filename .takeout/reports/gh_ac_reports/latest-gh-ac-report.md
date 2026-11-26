# Validate Document Standards — run 45831497498

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45831497498 / 1 |
| Run number | 627 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45831497498 |
| Branch | gpt |
| Commit | 7d1e9ab7a1b57cf16cf9770426419132ab052e1b |
| Event | workflow_dispatch |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-26T13:40:51Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-26T13:42:49Z |

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

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests may bypass retry timing for one exact completed run, but they cannot override the error-only retention rule. Successful and cancellation-only runs are never retained.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 139949149577 | validate-document-standards | completed | failure | 9 | logs/job-139949149577.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 139949149577 | 6 | Validate the document type catalog | Blocking | medium | 2026-11-26T13:41:03.3798268Z ERROR: Line 148: unsafe or excluded Markdown coverage pattern ' .archive/adr/*.md'. |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 139949149577 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 139949149577 | failure | .github | 15 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 139949149577 | validate-document-standards | logs/job-139949149577.log | 48023 | False | validate-document-standards	Validate the document type catalog	2026-11-26T13:41:03.3798268Z ERROR: Line 148: unsafe or excluded Markdown coverage pattern ' .archive/adr/*.md'., validate-document-standards	Validate the document type catalog	2026-11-26T13:41:03.3799546Z ERROR: Line 149: unsafe or excluded Markdown coverage pattern ' .archive/task/*.md'., validate-document-standards	Validate the document type catalog	2026-11-26T13:41:03.3800573Z Catalog validation failed: 2 error(s), 18 document type(s), 28 reference(s)., validate-document-standards	Validate the document type catalog	2026-11-26T13:41:03.3857460Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.