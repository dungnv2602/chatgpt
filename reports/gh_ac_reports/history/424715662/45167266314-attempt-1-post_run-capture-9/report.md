# STE Lint Changed Documentation — run 45167266314

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45167266314 / 1 |
| Run number | 482 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45167266314 |
| Branch | gpt |
| Commit | 05b062aead329a7ddbdeb07061834a1b04ef3f49 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T11:40:16Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / cancelled |
| Capture stage | post_run |
| Completeness | Incomplete |
| Captured (UTC) | 2026-11-23T12:05:36Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | None |
| Jobs | 2 |
| Steps | 4 |
| Issues | 0 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 1 |

## Failure classification

No failure category identified.

The run conclusion records the workflow outcome. A cancelled run remains in history. Cancellation alone does not create an actionable issue. The generator also excludes known downstream status-propagation steps after cancellation.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137667342297 | Reject superseded runs and find lint baseline | completed | cancelled | 4 | logs/job-137667342297.log |
| 137667406060 | Lint changed Markdown files and publish detailed evidence | completed | cancelled | 0 | logs/job-137667406060.log |

## Actionable step outcomes

No records were captured.

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137667342297 | failure | .github | 1 |  | Canceling since a higher priority waiting request for STE Lint Changed Documentation-refs/heads/gpt exists |
| 137667342297 | failure | .github | 27 |  | The operation was canceled. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137667342297 | Reject superseded runs and find lint baseline | logs/job-137667342297.log | 8012 | False | Reject superseded runs and find lint baseline	Cancel superseded run before checkout	2026-11-23T11:40:21.9346287Z ##[error]The operation was canceled. |
| 137667406060 | Lint changed Markdown files and publish detailed evidence | logs/job-137667406060.log | 29 | False |  |

## Evidence coverage

One or more evidence sources were unavailable. This report is Incomplete.

| Source | HTTP status | Limitation |
| --- | --- | --- |
| job_log | Not recorded | log not found: 137667406060  |

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.