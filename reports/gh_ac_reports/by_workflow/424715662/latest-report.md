# STE Lint Changed Documentation — run 45128076770

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45128076770 / 1 |
| Run number | 441 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45128076770 |
| Branch | gpt |
| Commit | 3cc93083c3e6a655038f9c5f22a970ac4ff9e731 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T07:00:57Z |
| Status at capture | in_progress |
| Observed conclusion | Not yet available |
| Projected conclusion | cancelled |
| Reporter job | in_progress / Pending |
| Capture stage | pre_finalizer |
| Completeness | Incomplete |
| Captured (UTC) | 2026-11-23T07:01:44Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | in_progress |
| Primary category | cancelled |
| Jobs | 2 |
| Steps | 17 |
| Issues | 1 |
| Annotations | 3 |
| Artifacts | 0 |
| Capture errors | 2 |

## Failure classification

cancelled The parent run is still in progress. The projected conclusion is provisional.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137537024744 | Reject superseded runs and find lint baseline | completed | success | 4 | logs/job-137537024744.log |
| 137537068649 | Lint changed Markdown files and publish detailed evidence | completed | cancelled | 13 | logs/job-137537068649.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| cancelled | 137537068649 | 2 | Check out current commit | Blocking | high | Step conclusion: cancelled |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137537068649 | failure | .github | 1 |  | Canceling since a higher priority waiting request for STE Lint Changed Documentation-refs/heads/gpt exists |
| 137537068649 | warning | .github | 4 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137537068649 | failure | .github | 60 |  | The operation was canceled. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137537024744 | Reject superseded runs and find lint baseline | logs/job-137537024744.log | 82 | False |  |
| 137537068649 | Lint changed Markdown files and publish detailed evidence | logs/job-137537068649.log | 82 | False |  |

## Evidence coverage

One or more evidence sources were unavailable. This report is Incomplete.

| Source | HTTP status | Limitation |
| --- | --- | --- |
| job_log | Not recorded | run 45128076770 is still in progress; logs will be available when it is complete  |
| job_log | Not recorded | run 45128076770 is still in progress; logs will be available when it is complete  |

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.