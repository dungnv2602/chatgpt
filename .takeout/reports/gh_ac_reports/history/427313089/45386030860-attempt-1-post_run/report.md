# Validate Document Standards — run 45386030860

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45386030860 / 1 |
| Run number | 285 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45386030860 |
| Branch | gpt |
| Commit | 31bb58dfe0d7acd5914b7b34ee8b41464f0658ee |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T11:38:27Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-24T12:59:04Z |

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
| 138417273800 | validate-document-standards | completed | failure | 8 | logs/job-138417273800.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| checkout_or_action_download | 138417273800 | 5 | Validate the document type catalog | Blocking | medium | validate-document-standards	UNKNOWN STEP	2026-11-24T11:39:07.3692744Z ERROR: Line 129: Embedded contract coverage must name its owner and live record. |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138417273800 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138417273800 | failure | .github | 17 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138417273800 | validate-document-standards | logs/job-138417273800.log | 32931 | False | validate-document-standards	UNKNOWN STEP	2026-11-24T11:39:07.3692744Z ERROR: Line 129: Embedded contract coverage must name its owner and live record., validate-document-standards	UNKNOWN STEP	2026-11-24T11:39:07.3693793Z ERROR: Line 131: invalid coverage template location for 'workspace/draft/DRAFT_TEMPLATE.md': template must be in its owning skill's assets/ directory, novels/templates/, or the shared workspace root., validate-document-standards	UNKNOWN STEP	2026-11-24T11:39:07.3694506Z ERROR: Line 132: Embedded contract coverage must name its owner and live record., validate-document-standards	UNKNOWN STEP	2026-11-24T11:39:07.3695189Z ERROR: Line 134: invalid coverage template location for 'workspace/adr/ADR_TEMPLATE.md': template must be in its owning skill's assets/ directory, novels/templates/, or the shared workspace root., validate-document-standards	UNKNOWN STEP	2026-11-24T11:39:07.3695843Z Catalog validation failed: 4 error(s), 18 document type(s), 28 reference(s)., validate-document-standards	UNKNOWN STEP	2026-11-24T11:39:07.3737960Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.