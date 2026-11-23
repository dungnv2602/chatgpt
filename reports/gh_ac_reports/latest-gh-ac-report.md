# STE Lint Changed Documentation — run 45157016400

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45157016400 / 1 |
| Run number | 456 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45157016400 |
| Branch | gpt |
| Commit | bf361fd04c45eb6634b09bce553251ad73758904 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T10:32:23Z |
| Status at capture | in_progress |
| Observed conclusion | Not yet available |
| Projected conclusion | cancelled |
| Reporter job | in_progress / Pending |
| Capture stage | pre_finalizer |
| Completeness | Incomplete |
| Captured (UTC) | 2026-11-23T10:33:18Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | in_progress |
| Primary category | None |
| Jobs | 2 |
| Steps | 5 |
| Issues | 0 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 2 |

## Failure classification

No failure category identified. The parent run is still in progress. The projected conclusion is provisional.

The run conclusion records the workflow outcome. A cancelled run remains in history. Cancellation alone does not create an actionable issue. The generator also excludes known downstream status-propagation steps after cancellation.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137632528243 | Reject superseded runs and find lint baseline | completed | success | 4 | logs/job-137632528243.log |
| 137632604720 | Lint changed Markdown files and publish detailed evidence | completed | cancelled | 1 | logs/job-137632604720.log |

## Actionable step outcomes

No records were captured.

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137632604720 | failure | .github | 1 |  | Canceling since a higher priority waiting request for STE Lint Changed Documentation-refs/heads/gpt exists |
| 137632604720 | failure | .github | 32 |  | The operation was canceled. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137632528243 | Reject superseded runs and find lint baseline | logs/job-137632528243.log | 82 | False |  |
| 137632604720 | Lint changed Markdown files and publish detailed evidence | logs/job-137632604720.log | 82 | False |  |

## Evidence coverage

One or more evidence sources were unavailable. This report is Incomplete.

| Source | HTTP status | Limitation |
| --- | --- | --- |
| job_log | Not recorded | run 45157016400 is still in progress; logs will be available when it is complete  |
| job_log | Not recorded | run 45157016400 is still in progress; logs will be available when it is complete  |

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.