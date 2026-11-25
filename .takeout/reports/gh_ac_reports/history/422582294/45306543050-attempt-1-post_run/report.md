# Process Image Takeout and Create WebP Derivatives — run 45306543050

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Process Image Takeout and Create WebP Derivatives |
| Workflow path | .github/workflows/convert-images-to-webp.yml |
| Run / attempt | 45306543050 / 1 |
| Run number | 65 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45306543050 |
| Branch | gpt |
| Commit | 709ae66e59d4161b69f99f9d4b299d1f36021406 |
| Event | workflow_dispatch |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T01:38:35Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-24T06:16:42Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | checkout_or_action_download |
| Jobs | 1 |
| Steps | 11 |
| Issues | 1 |
| Annotations | 1 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

checkout_or_action_download

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 138151666516 | process-image-takeout | completed | failure | 11 | logs/job-138151666516.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| checkout_or_action_download | 138151666516 | 5 | Test takeout processor | Blocking | medium | process-image-takeout	UNKNOWN STEP	2026-11-24T01:39:00.1205370Z Traceback (most recent call last): |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138151666516 | failure | .github | 67 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138151666516 | process-image-takeout | logs/job-138151666516.log | 44219 | False | process-image-takeout	UNKNOWN STEP	2026-11-24T01:39:00.1205370Z Traceback (most recent call last):, process-image-takeout	UNKNOWN STEP	2026-11-24T01:39:00.1220776Z FAILED (failures=1), process-image-takeout	UNKNOWN STEP	2026-11-24T01:39:00.1333484Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.