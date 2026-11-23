# STE Lint Full Technical Documentation — run 45127306049

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Full Technical Documentation |
| Workflow path | .github/workflows/ste-lint-full-docs.yml |
| Run / attempt | 45127306049 / 1 |
| Run number | 167 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45127306049 |
| Branch | gpt |
| Commit | 7f203e5cbb3ab5615714a454ff16d1984a536e8d |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T06:54:22Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Incomplete |
| Captured (UTC) | 2026-11-23T08:38:02Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | cancelled |
| Jobs | 2 |
| Steps | 3 |
| Issues | 2 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 1 |

## Failure classification

cancelled

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137534503885 | Validate target branch and reject superseded push runs | completed | cancelled | 3 | logs/job-137534503885.log |
| 137534535789 | Full audit and publish detailed evidence | completed | cancelled | 0 | logs/job-137534535789.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| cancelled | 137534503885 | — | Validate target branch and reject superseded push runs | Blocking | high | Validate target branch and reject superseded push runs	UNKNOWN STEP	2026-11-23T06:54:25.7160955Z ^[[36;1m  echo "::error::Select the gpt branch when manually dispatching this workflow."^[[0m |
| cancelled | 137534535789 | — | Full audit and publish detailed evidence | Blocking | high | Job conclusion: cancelled |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137534503885 | failure | .github | 1 |  | Canceling since a higher priority waiting request for STE Lint Full Technical Documentation-refs/heads/gpt exists |
| 137534503885 | warning | .github | 35 |  | Could not identify the latest push run. Continue with validation. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137534503885 | Validate target branch and reject superseded push runs | logs/job-137534503885.log | 9236 | False | Validate target branch and reject superseded push runs	UNKNOWN STEP	2026-11-23T06:54:25.7160955Z ^[[36;1m  echo "::error::Select the gpt branch when manually dispatching this workflow."^[[0m |
| 137534535789 | Full audit and publish detailed evidence | logs/job-137534535789.log | 29 | False |  |

## Evidence coverage

One or more evidence sources were unavailable. This report is Incomplete.

| Source | HTTP status | Limitation |
| --- | --- | --- |
| job_log | Not recorded | log not found: 137534535789  |

## Related lint evidence

[Repository-wide lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_repo/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.