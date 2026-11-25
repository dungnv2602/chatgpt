# Validate Document Standards — run 45399711310

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45399711310 / 1 |
| Run number | 298 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45399711310 |
| Branch | gpt |
| Commit | d66901394de689223394f990047705d42108cef0 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T13:04:39Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-24T13:27:01Z |

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
| 138464780986 | validate-document-standards | completed | failure | 8 | logs/job-138464780986.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 138464780986 | 5 | Validate the document type catalog | Blocking | medium | 2026-11-24T13:04:52.2485016Z ERROR: Line 130: Embedded contract coverage must name its owner and live record. |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138464780986 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138464780986 | failure | .github | 19 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138464780986 | validate-document-standards | logs/job-138464780986.log | 35342 | False | validate-document-standards	Validate the document type catalog	2026-11-24T13:04:52.2485016Z ERROR: Line 130: Embedded contract coverage must name its owner and live record., validate-document-standards	Validate the document type catalog	2026-11-24T13:04:52.2486608Z ERROR: Line 132: invalid coverage template location for 'workspace/analysis/ANALYSIS_TEMPLATE.md': template must be in its owning skill's assets/ directory, novels/templates/, or the shared workspace root., validate-document-standards	Validate the document type catalog	2026-11-24T13:04:52.2487904Z ERROR: Line 133: Embedded contract coverage must name its owner and live record., validate-document-standards	Validate the document type catalog	2026-11-24T13:04:52.2489129Z ERROR: Line 135: invalid coverage template location for 'workspace/draft/DRAFT_TEMPLATE.md': template must be in its owning skill's assets/ directory, novels/templates/, or the shared workspace root., validate-document-standards	Validate the document type catalog	2026-11-24T13:04:52.2490542Z ERROR: Line 136: Embedded contract coverage must name its owner and live record., validate-document-standards	Validate the document type catalog	2026-11-24T13:04:52.2491714Z ERROR: Line 138: invalid coverage template location for 'workspace/adr/ADR_TEMPLATE.md': template must be in its owning skill's assets/ directory, novels/templates/, or the shared workspace root., validate-document-standards	Validate the document type catalog	2026-11-24T13:04:52.2492751Z Catalog validation failed: 6 error(s), 18 document type(s), 28 reference(s)., validate-document-standards	Validate the document type catalog	2026-11-24T13:04:52.2551674Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.