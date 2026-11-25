# Validate Document Standards — run 45382651641

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45382651641 / 1 |
| Run number | 283 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45382651641 |
| Branch | gpt |
| Commit | 8adc48d1be4d4d659fba028d7cea8e76ddd9c9d9 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T11:16:23Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-24T11:19:01Z |

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
| 138405362346 | validate-document-standards | completed | failure | 8 | logs/job-138405362346.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 138405362346 | 5 | Validate the document type catalog | Blocking | medium | 2026-11-24T11:16:35.5153185Z ERROR: Line 129: Embedded contract coverage must name its owner and live record. |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138405362346 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138405362346 | failure | .github | 17 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138405362346 | validate-document-standards | logs/job-138405362346.log | 34879 | False | validate-document-standards	Validate the document type catalog	2026-11-24T11:16:35.5153185Z ERROR: Line 129: Embedded contract coverage must name its owner and live record., validate-document-standards	Validate the document type catalog	2026-11-24T11:16:35.5153792Z ERROR: Line 131: invalid coverage template location for 'workspace/draft/DRAFT_TEMPLATE.md': template must be in its owning skill's assets/ directory, novels/templates/, or the shared workspace root., validate-document-standards	Validate the document type catalog	2026-11-24T11:16:35.5154381Z ERROR: Line 132: Embedded contract coverage must name its owner and live record., validate-document-standards	Validate the document type catalog	2026-11-24T11:16:35.5154877Z ERROR: Line 134: invalid coverage template location for 'workspace/adr/ADR_TEMPLATE.md': template must be in its owning skill's assets/ directory, novels/templates/, or the shared workspace root., validate-document-standards	Validate the document type catalog	2026-11-24T11:16:35.5155358Z Catalog validation failed: 4 error(s), 18 document type(s), 28 reference(s)., validate-document-standards	Validate the document type catalog	2026-11-24T11:16:35.5211186Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.