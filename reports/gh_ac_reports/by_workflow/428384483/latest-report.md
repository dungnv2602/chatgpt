# Convert Unclassified Takeout Images to WebP — run 45282059449

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Convert Unclassified Takeout Images to WebP |
| Workflow path | .github/workflows/convert-unclassified-takeout.yml |
| Run / attempt | 45282059449 / 1 |
| Run number | 1 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45282059449 |
| Branch | gpt |
| Commit | da5d4730b200bc196072f51e4225733a26397f60 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T22:41:26Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | Not captured |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T23:00:58Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | publication_or_push |
| Jobs | 1 |
| Steps | 7 |
| Issues | 1 |
| Annotations | 1 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

publication_or_push

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 138068773958 | convert-unclassified | completed | failure | 7 | logs/job-138068773958.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| publication_or_push | 138068773958 | 5 | Commit WebP derivatives only | Blocking | high | 2026-11-23T22:44:31.4887460Z error: failed to push some refs to 'https://github.com/dungnv2602/chatgpt' |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138068773958 | failure | .github | 28 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138068773958 | convert-unclassified | logs/job-138068773958.log | 44645 | False | convert-unclassified	Commit WebP derivatives only	2026-11-23T22:44:31.4887460Z error: failed to push some refs to 'https://github.com/dungnv2602/chatgpt', convert-unclassified	Commit WebP derivatives only	2026-11-23T22:44:31.4911601Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.