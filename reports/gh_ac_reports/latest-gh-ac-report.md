# Process Image Takeout and Create WebP Derivatives — run 45305320198

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Process Image Takeout and Create WebP Derivatives |
| Workflow path | .github/workflows/convert-images-to-webp.yml |
| Run / attempt | 45305320198 / 1 |
| Run number | 64 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45305320198 |
| Branch | gpt |
| Commit | 42be44a4e0999c5cf55181cafe3c32600659a6c4 |
| Event | workflow_dispatch |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T01:28:41Z |
| Status at capture | in_progress |
| Observed conclusion | Not yet available |
| Projected conclusion | failure |
| Reporter job | in_progress / Pending |
| Capture stage | pre_finalizer |
| Completeness | Incomplete |
| Captured (UTC) | 2026-11-24T01:29:26Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | in_progress |
| Primary category | validation_or_test |
| Jobs | 1 |
| Steps | 11 |
| Issues | 1 |
| Annotations | 1 |
| Artifacts | 0 |
| Capture errors | 1 |

## Failure classification

validation_or_test The parent run is still in progress. The projected conclusion is provisional.

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 138147636006 | process-image-takeout | completed | failure | 11 | logs/job-138147636006.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 138147636006 | 5 | Test takeout processor | Blocking | medium | Step conclusion: failure |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138147636006 | failure | .github | 203 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138147636006 | process-image-takeout | logs/job-138147636006.log | 82 | False |  |

## Evidence coverage

One or more evidence sources were unavailable. This report is Incomplete.

| Source | HTTP status | Limitation |
| --- | --- | --- |
| job_log | Not recorded | run 45305320198 is still in progress; logs will be available when it is complete  |

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.