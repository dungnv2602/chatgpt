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
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T07:06:21Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | cancelled |
| Jobs | 2 |
| Steps | 17 |
| Issues | 1 |
| Annotations | 3 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

cancelled

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137537024744 | Reject superseded runs and find lint baseline | completed | success | 4 | logs/job-137537024744.log |
| 137537068649 | Lint changed Markdown files and publish detailed evidence | completed | cancelled | 13 | logs/job-137537068649.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| cancelled | 137537068649 | 2 | Check out current commit | Blocking | high | Lint changed Markdown files and publish detailed evidence	Check out current commit	2026-11-23T07:01:24.8317569Z ##[error]The operation was canceled. |

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
| 137537024744 | Reject superseded runs and find lint baseline | logs/job-137537024744.log | 12713 | False |  |
| 137537068649 | Lint changed Markdown files and publish detailed evidence | logs/job-137537068649.log | 20251 | False | Lint changed Markdown files and publish detailed evidence	Check out current commit	2026-11-23T07:01:24.8317569Z ##[error]The operation was canceled., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T07:01:24.8895706Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.