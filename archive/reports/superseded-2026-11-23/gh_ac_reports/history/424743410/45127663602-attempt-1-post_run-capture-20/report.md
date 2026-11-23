# STE Lint Full Technical Documentation — run 45127663602

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Full Technical Documentation |
| Workflow path | .github/workflows/ste-lint-full-docs.yml |
| Run / attempt | 45127663602 / 1 |
| Run number | 171 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45127663602 |
| Branch | gpt |
| Commit | e075856bc3e0b72286bcef236c82c30a9a5724a3 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T06:57:30Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Incomplete |
| Captured (UTC) | 2026-11-23T08:35:31Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | cancelled |
| Jobs | 2 |
| Steps | 3 |
| Issues | 1 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 1 |

## Failure classification

cancelled

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137535647848 | Validate target branch and reject superseded push runs | completed | success | 3 | logs/job-137535647848.log |
| 137535671579 | Full audit and publish detailed evidence | completed | cancelled | 0 | logs/job-137535671579.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| cancelled | 137535671579 | — | Full audit and publish detailed evidence | Blocking | high | Job conclusion: cancelled |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137535647848 | warning | .github | 35 |  | Could not identify the latest push run. Continue with validation. |
| 137535671579 | failure | .github | 1 |  | Canceling since a higher priority waiting request for STE Lint Full Technical Documentation-refs/heads/gpt exists |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137535647848 | Validate target branch and reject superseded push runs | logs/job-137535647848.log | 9234 | False | Validate target branch and reject superseded push runs	UNKNOWN STEP	2026-11-23T06:57:33.4189300Z ^[[36;1m  echo "::error::Select the gpt branch when manually dispatching this workflow."^[[0m |
| 137535671579 | Full audit and publish detailed evidence | logs/job-137535671579.log | 29 | False |  |

## Evidence coverage

One or more evidence sources were unavailable. This report is Incomplete.

| Source | HTTP status | Limitation |
| --- | --- | --- |
| job_log | Not recorded | log not found: 137535671579  |

## Related lint evidence

[Repository-wide lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_repo/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.