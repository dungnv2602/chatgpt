# Validate Document Standards — run 45457882610

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45457882610 / 1 |
| Run number | 362 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45457882610 |
| Branch | gpt |
| Commit | ae1ae3420409c2031ad8aa34f75121dead98b4a6 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T18:17:21Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-24T18:33:31Z |

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
| 138674011068 | validate-document-standards | completed | failure | 9 | logs/job-138674011068.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 138674011068 | 6 | Validate the document type catalog | Blocking | medium | 2026-11-24T18:20:26.1370225Z ERROR: Line 140: Markdown coverage pattern matches no in-scope document: 'workspace/adr/????-*.md'. |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138674011068 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138674011068 | failure | .github | 14 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138674011068 | validate-document-standards | logs/job-138674011068.log | 45088 | False | validate-document-standards	Validate the document type catalog	2026-11-24T18:20:26.1370225Z ERROR: Line 140: Markdown coverage pattern matches no in-scope document: 'workspace/adr/????-*.md'., validate-document-standards	Validate the document type catalog	2026-11-24T18:20:26.1417475Z Catalog validation failed: 1 error(s), 18 document type(s), 28 reference(s)., validate-document-standards	Validate the document type catalog	2026-11-24T18:20:26.1426735Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.