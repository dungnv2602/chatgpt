# STE Lint Changed Documentation — run 45127427690

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45127427690 / 1 |
| Run number | 433 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45127427690 |
| Branch | gpt |
| Commit | 501deb3a96171ddd3bf601f72a3f126abb2149c9 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T06:55:25Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Incomplete |
| Captured (UTC) | 2026-11-23T09:21:21Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | cancelled |
| Jobs | 2 |
| Steps | 4 |
| Issues | 2 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 1 |

## Failure classification

cancelled

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137534891066 | Reject superseded runs and find lint baseline | completed | cancelled | 4 | logs/job-137534891066.log |
| 137534944936 | Lint changed Markdown files and publish detailed evidence | completed | cancelled | 0 | logs/job-137534944936.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| cancelled | 137534891066 | 2 | Cancel superseded run before checkout | Blocking | high | Reject superseded runs and find lint baseline	UNKNOWN STEP	2026-11-23T06:55:33.2921154Z ##[error]The operation was canceled. |
| cancelled | 137534944936 | — | Lint changed Markdown files and publish detailed evidence | Blocking | high | Job conclusion: cancelled |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137534891066 | failure | .github | 1 |  | Canceling since a higher priority waiting request for STE Lint Changed Documentation-refs/heads/gpt exists |
| 137534891066 | failure | .github | 27 |  | The operation was canceled. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137534891066 | Reject superseded runs and find lint baseline | logs/job-137534891066.log | 7390 | False | Reject superseded runs and find lint baseline	UNKNOWN STEP	2026-11-23T06:55:33.2921154Z ##[error]The operation was canceled. |
| 137534944936 | Lint changed Markdown files and publish detailed evidence | logs/job-137534944936.log | 29 | False |  |

## Evidence coverage

One or more evidence sources were unavailable. This report is Incomplete.

| Source | HTTP status | Limitation |
| --- | --- | --- |
| job_log | Not recorded | log not found: 137534944936  |

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.