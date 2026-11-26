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
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Incomplete |
| Captured (UTC) | 2026-11-26T05:10:38Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | permission_or_authentication |
| Jobs | 1 |
| Steps | 11 |
| Issues | 1 |
| Annotations | 1 |
| Artifacts | 0 |
| Capture errors | 1 |

## Failure classification

permission_or_authentication

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 138147636006 | process-image-takeout | completed | failure | 11 | logs/job-138147636006.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| permission_or_authentication | 138147636006 | 5 | Test takeout processor | Blocking | high | failed to get run: HTTP 403: API rate limit exceeded for installation. If you reach out to GitHub Support for help, please include the request ID 3044:1C8C72:242AC9D:716E1BF:6B07BF4E and timestamp 2026-11-26 05:10:38 UTC. For more on scraping GitHub and how it may affect your rights, please review our Terms of Service (https://docs.github.com/en/site-policy/github-terms/github-terms-of-service) (https://api.github.com/repos/dungnv2602/chatgpt/actions/runs/45305320198?exclude_pull_requests=true) |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138147636006 | failure | .github | 203 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138147636006 | process-image-takeout | logs/job-138147636006.log | 501 | False | failed to get run: HTTP 403: API rate limit exceeded for installation. If you reach out to GitHub Support for help, please include the request ID 3044:1C8C72:242AC9D:716E1BF:6B07BF4E and timestamp 2026-11-26 05:10:38 UTC. For more on scraping GitHub and how it may affect your rights, please review our Terms of Service (https://docs.github.com/en/site-policy/github-terms/github-terms-of-service) (https://api.github.com/repos/dungnv2602/chatgpt/actions/runs/45305320198?exclude_pull_requests=true) |

## Evidence coverage

One or more evidence sources were unavailable. This report is Incomplete.

| Source | HTTP status | Limitation |
| --- | --- | --- |
| job_log | Not recorded | failed to get run: HTTP 403: API rate limit exceeded for installation. If you reach out to GitHub Support for help, please include the request ID 3044:1C8C72:242AC9D:716E1BF:6B07BF4E and timestamp 2026-11-26 05:10:38 UTC. For more on scraping GitHub and how it may affect your rights, please review our Terms of Service (https://docs.github.com/en/site-policy/github-terms/github-terms-of-service) (https://api.github.com/repos/dungnv2602/chatgpt/actions/runs/45305320198?exclude_pull_requests=true)  |

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.