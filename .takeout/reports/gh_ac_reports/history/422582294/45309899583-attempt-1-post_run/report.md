# Process Image Takeout and Create WebP Derivatives — run 45309899583

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Process Image Takeout and Create WebP Derivatives |
| Workflow path | .github/workflows/convert-images-to-webp.yml |
| Run / attempt | 45309899583 / 1 |
| Run number | 66 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45309899583 |
| Branch | gpt |
| Commit | f99a9ac832c48a9117cd001960039f45b3b0d0be |
| Event | workflow_dispatch |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T02:06:14Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-24T06:17:01Z |

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
| 138162718767 | process-image-takeout | completed | failure | 11 | logs/job-138162718767.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| checkout_or_action_download | 138162718767 | 5 | Test takeout processor | Blocking | medium | process-image-takeout	UNKNOWN STEP	2026-11-24T02:06:42.2149202Z Traceback (most recent call last): |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138162718767 | failure | .github | 84 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138162718767 | process-image-takeout | logs/job-138162718767.log | 46301 | False | process-image-takeout	UNKNOWN STEP	2026-11-24T02:06:42.2149202Z Traceback (most recent call last):, process-image-takeout	UNKNOWN STEP	2026-11-24T02:06:42.2203008Z FAILED (failures=1), process-image-takeout	UNKNOWN STEP	2026-11-24T02:06:42.2287738Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.