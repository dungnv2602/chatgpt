# STE Lint Changed Documentation — run 45159429441

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45159429441 / 1 |
| Run number | 472 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45159429441 |
| Branch | gpt |
| Commit | 0a1835a15518a039f8fcfe4f25789ab8a2a78098 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T10:48:25Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / cancelled |
| Capture stage | post_run |
| Completeness | Incomplete |
| Captured (UTC) | 2026-11-23T10:54:05Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | None |
| Jobs | 2 |
| Steps | 4 |
| Issues | 0 |
| Annotations | 1 |
| Artifacts | 0 |
| Capture errors | 1 |

## Failure classification

No failure category identified.

The run conclusion records the workflow outcome. A cancelled run remains in history. Cancellation alone does not create an actionable issue. The generator also excludes known downstream status-propagation steps after cancellation.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137640669725 | Reject superseded runs and find lint baseline | completed | cancelled | 4 | logs/job-137640669725.log |
| 137640733149 | Lint changed Markdown files and publish detailed evidence | completed | cancelled | 0 | logs/job-137640733149.log |

## Actionable step outcomes

No records were captured.

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137640669725 | failure | .github | 1 |  | The run was canceled by @github-actions[bot]. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137640669725 | Reject superseded runs and find lint baseline | logs/job-137640669725.log | 8036 | False |  |
| 137640733149 | Lint changed Markdown files and publish detailed evidence | logs/job-137640733149.log | 29 | False |  |

## Evidence coverage

One or more evidence sources were unavailable. This report is Incomplete.

| Source | HTTP status | Limitation |
| --- | --- | --- |
| job_log | Not recorded | log not found: 137640733149  |

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.