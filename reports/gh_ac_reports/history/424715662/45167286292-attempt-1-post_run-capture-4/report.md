# STE Lint Changed Documentation — run 45167286292

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45167286292 / 1 |
| Run number | 485 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45167286292 |
| Branch | gpt |
| Commit | 6376a06fb118cf406b2d542c3d349689a70b682b |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T11:40:23Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / cancelled |
| Capture stage | post_run |
| Completeness | Incomplete |
| Captured (UTC) | 2026-11-23T12:00:34Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | None |
| Jobs | 2 |
| Steps | 0 |
| Issues | 0 |
| Annotations | 1 |
| Artifacts | 0 |
| Capture errors | 2 |

## Failure classification

No failure category identified.

The run conclusion records the workflow outcome. A cancelled run remains in history. Cancellation alone does not create an actionable issue. The generator also excludes known downstream status-propagation steps after cancellation.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137667414570 | Reject superseded runs and find lint baseline | completed | cancelled | 0 | logs/job-137667414570.log |
| 137669953203 | Lint changed Markdown files and publish detailed evidence | completed | cancelled | 0 | logs/job-137669953203.log |

## Actionable step outcomes

No records were captured.

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137667414570 | failure | .github | 1 |  | Canceling since a higher priority waiting request for STE Lint Changed Documentation-refs/heads/gpt exists |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137667414570 | Reject superseded runs and find lint baseline | logs/job-137667414570.log | 29 | False |  |
| 137669953203 | Lint changed Markdown files and publish detailed evidence | logs/job-137669953203.log | 29 | False |  |

## Evidence coverage

One or more evidence sources were unavailable. This report is Incomplete.

| Source | HTTP status | Limitation |
| --- | --- | --- |
| job_log | Not recorded | log not found: 137667414570  |
| job_log | Not recorded | log not found: 137669953203  |

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.