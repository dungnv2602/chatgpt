# STE Lint Full Technical Documentation — run 45773614372

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Full Technical Documentation |
| Workflow path | .github/workflows/ste-lint-full-docs.yml |
| Run / attempt | 45773614372 / 1 |
| Run number | 206 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45773614372 |
| Branch | gpt |
| Commit | f7d38e70535b3918f978e1fd769f7e42d9fd1692 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-26T07:12:35Z |
| Status at capture | in_progress |
| Observed conclusion | Not yet available |
| Projected conclusion | failure |
| Reporter job | in_progress / Pending |
| Capture stage | pre_finalizer |
| Completeness | Incomplete |
| Captured (UTC) | 2026-11-26T07:15:39Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | in_progress |
| Primary category | step_or_job_failure |
| Jobs | 2 |
| Steps | 12 |
| Issues | 1 |
| Annotations | 4 |
| Artifacts | 0 |
| Capture errors | 2 |

## Failure classification

step_or_job_failure The parent run is still in progress. The projected conclusion is provisional.

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 139751876182 | Validate target branch and reject superseded push runs | completed | success | 3 | logs/job-139751876182.log |
| 139751914227 | Full audit and publish detailed evidence | completed | failure | 9 | logs/job-139751914227.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| step_or_job_failure | 139751914227 | 6 | Set workflow result from audit and tooling outcomes | Blocking | low | Step conclusion: failure |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 139751876182 | warning | .github | 35 |  | Could not identify the latest push run. Continue with validation. |
| 139751914227 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 139751914227 | failure | .github | 20 |  | Process completed with exit code 1. |
| 139751914227 | failure | .github | 19 |  | The full audit found lint or validation failures. See .takeout/reports/lint_reports/on_repo/latest-lint-report.md. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 139751876182 | Validate target branch and reject superseded push runs | logs/job-139751876182.log | 82 | False |  |
| 139751914227 | Full audit and publish detailed evidence | logs/job-139751914227.log | 82 | False |  |

## Evidence coverage

One or more evidence sources were unavailable. This report is Incomplete.

| Source | HTTP status | Limitation |
| --- | --- | --- |
| job_log | Not recorded | run 45773614372 is still in progress; logs will be available when it is complete  |
| job_log | Not recorded | run 45773614372 is still in progress; logs will be available when it is complete  |

## Related lint evidence

[Repository-wide lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/.takeout/reports/lint_reports/on_repo/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.