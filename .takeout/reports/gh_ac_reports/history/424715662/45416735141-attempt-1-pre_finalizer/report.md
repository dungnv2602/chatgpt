# STE Lint Changed Documentation — run 45416735141

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45416735141 / 1 |
| Run number | 635 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45416735141 |
| Branch | gpt |
| Commit | 725896a79c8a9c3decef0f8d507cc9cacdaed4fc |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T14:40:30Z |
| Status at capture | in_progress |
| Observed conclusion | Not yet available |
| Projected conclusion | failure |
| Reporter job | in_progress / Pending |
| Capture stage | pre_finalizer |
| Completeness | Incomplete |
| Captured (UTC) | 2026-11-24T14:43:02Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | in_progress |
| Primary category | validation_or_test |
| Jobs | 2 |
| Steps | 17 |
| Issues | 2 |
| Annotations | 4 |
| Artifacts | 0 |
| Capture errors | 2 |

## Failure classification

validation_or_test The parent run is still in progress. The projected conclusion is provisional.

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 138525836328 | Find lint baseline and select execution mode | completed | success | 3 | logs/job-138525836328.log |
| 138525943599 | Lint changed Markdown files and publish detailed evidence | completed | failure | 14 | logs/job-138525943599.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 138525943599 | 10 | Generate and publish changed-document lint evidence | Blocking | medium | Step conclusion: failure |
| validation_or_test | 138525943599 | 11 | Preserve lint failure as workflow conclusion | Blocking | medium | Step conclusion: failure |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138525943599 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138525943599 | failure | .github | 21 |  | Process completed with exit code 1. |
| 138525943599 | failure | .github | 20 |  | Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md. |
| 138525943599 | failure | .github | 124 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138525836328 | Find lint baseline and select execution mode | logs/job-138525836328.log | 82 | False |  |
| 138525943599 | Lint changed Markdown files and publish detailed evidence | logs/job-138525943599.log | 82 | False |  |

## Evidence coverage

One or more evidence sources were unavailable. This report is Incomplete.

| Source | HTTP status | Limitation |
| --- | --- | --- |
| job_log | Not recorded | run 45416735141 is still in progress; logs will be available when it is complete  |
| job_log | Not recorded | run 45416735141 is still in progress; logs will be available when it is complete  |

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.