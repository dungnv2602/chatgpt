# STE Lint Full Technical Documentation — run 45128438340

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Full Technical Documentation |
| Workflow path | .github/workflows/ste-lint-full-docs.yml |
| Run / attempt | 45128438340 / 1 |
| Run number | 173 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45128438340 |
| Branch | gpt |
| Commit | 6133f83778ce3d6241ce5e53faf443292a3140d1 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T07:04:09Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Incomplete |
| Captured (UTC) | 2026-11-23T11:42:57Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | None |
| Jobs | 2 |
| Steps | 3 |
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
| 137538097907 | Validate target branch and reject superseded push runs | completed | cancelled | 3 | logs/job-137538097907.log |
| 137538141103 | Full audit and publish detailed evidence | completed | cancelled | 0 | logs/job-137538141103.log |

## Actionable step outcomes

No records were captured.

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137538097907 | failure | .github | 1 |  | Canceling since a higher priority waiting request for STE Lint Full Technical Documentation-refs/heads/gpt exists |
| 137538097907 | failure | .github | 35 |  | The operation was canceled. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137538097907 | Validate target branch and reject superseded push runs | logs/job-137538097907.log | 9073 | False | Validate target branch and reject superseded push runs	UNKNOWN STEP	2026-11-23T07:04:11.9704126Z ^[[36;1m  echo "::error::Select the gpt branch when manually dispatching this workflow."^[[0m, Validate target branch and reject superseded push runs	UNKNOWN STEP	2026-11-23T07:04:15.3395931Z ##[error]The operation was canceled. |
| 137538141103 | Full audit and publish detailed evidence | logs/job-137538141103.log | 29 | False |  |

## Evidence coverage

One or more evidence sources were unavailable. This report is Incomplete.

| Source | HTTP status | Limitation |
| --- | --- | --- |
| job_log | Not recorded | log not found: 137538141103  |

## Related lint evidence

[Repository-wide lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_repo/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.