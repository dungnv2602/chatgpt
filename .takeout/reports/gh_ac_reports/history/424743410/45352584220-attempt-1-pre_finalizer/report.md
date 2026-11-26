# STE Lint Full Technical Documentation — run 45352584220

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Full Technical Documentation |
| Workflow path | .github/workflows/ste-lint-full-docs.yml |
| Run / attempt | 45352584220 / 1 |
| Run number | 188 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45352584220 |
| Branch | gpt |
| Commit | 2efeafaa264ed9df16314b0f05da3d8890367091 |
| Event | workflow_dispatch |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T08:01:42Z |
| Status at capture | in_progress |
| Observed conclusion | Not yet available |
| Projected conclusion | failure |
| Reporter job | in_progress / Pending |
| Capture stage | pre_finalizer |
| Completeness | Incomplete |
| Captured (UTC) | 2026-11-24T08:02:32Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | in_progress |
| Primary category | step_or_job_failure |
| Jobs | 2 |
| Steps | 12 |
| Issues | 1 |
| Annotations | 3 |
| Artifacts | 0 |
| Capture errors | 2 |

## Failure classification

step_or_job_failure The parent run is still in progress. The projected conclusion is provisional.

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 138302431876 | Validate target branch and reject superseded push runs | completed | success | 3 | logs/job-138302431876.log |
| 138302465262 | Full audit and publish detailed evidence | completed | failure | 9 | logs/job-138302465262.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| step_or_job_failure | 138302465262 | 6 | Set workflow result from audit and tooling outcomes | Blocking | low | Step conclusion: failure |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138302465262 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138302465262 | failure | .github | 20 |  | Process completed with exit code 1. |
| 138302465262 | failure | .github | 19 |  | The full audit found lint or validation failures. See reports/lint_reports/on_repo/latest-lint-report.md. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138302431876 | Validate target branch and reject superseded push runs | logs/job-138302431876.log | 82 | False |  |
| 138302465262 | Full audit and publish detailed evidence | logs/job-138302465262.log | 82 | False |  |

## Evidence coverage

One or more evidence sources were unavailable. This report is Incomplete.

| Source | HTTP status | Limitation |
| --- | --- | --- |
| job_log | Not recorded | run 45352584220 is still in progress; logs will be available when it is complete  |
| job_log | Not recorded | run 45352584220 is still in progress; logs will be available when it is complete  |

## Related lint evidence

[Repository-wide lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_repo/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.