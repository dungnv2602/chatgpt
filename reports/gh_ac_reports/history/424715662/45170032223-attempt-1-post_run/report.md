# STE Lint Changed Documentation — run 45170032223

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45170032223 / 1 |
| Run number | 494 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45170032223 |
| Branch | gpt |
| Commit | adf9807dca79b4be299909db1d6b4004e28a20d3 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T11:59:06Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / cancelled |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T12:02:49Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | None |
| Jobs | 2 |
| Steps | 5 |
| Issues | 0 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

No failure category identified.

The run conclusion records the workflow outcome. A cancelled run remains in history. Cancellation alone does not create an actionable issue. The generator also excludes known downstream status-propagation steps after cancellation.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137676866887 | Reject superseded runs and find lint baseline | completed | success | 4 | logs/job-137676866887.log |
| 137676950705 | Lint changed Markdown files and publish detailed evidence | completed | cancelled | 1 | logs/job-137676950705.log |

## Actionable step outcomes

No records were captured.

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137676950705 | failure | .github | 1 |  | Canceling since a higher priority waiting request for STE Lint Changed Documentation-refs/heads/gpt exists |
| 137676950705 | failure | .github | 32 |  | The operation was canceled. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137676866887 | Reject superseded runs and find lint baseline | logs/job-137676866887.log | 12714 | False |  |
| 137676950705 | Lint changed Markdown files and publish detailed evidence | logs/job-137676950705.log | 4113 | False | Lint changed Markdown files and publish detailed evidence	Set up job	2026-11-23T11:59:19.5950225Z ##[error]The operation was canceled. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.