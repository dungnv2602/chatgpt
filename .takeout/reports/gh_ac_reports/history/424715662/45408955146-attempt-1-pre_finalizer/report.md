# STE Lint Changed Documentation — run 45408955146

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45408955146 / 1 |
| Run number | 620 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45408955146 |
| Branch | gpt |
| Commit | b1aec86f3f13eb7ac5c2dd92e8a7ba1f0f150a00 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T13:58:21Z |
| Status at capture | in_progress |
| Observed conclusion | Not yet available |
| Projected conclusion | failure |
| Reporter job | in_progress / Pending |
| Capture stage | pre_finalizer |
| Completeness | Incomplete |
| Captured (UTC) | 2026-11-24T14:00:15Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | in_progress |
| Primary category | validation_or_test |
| Jobs | 2 |
| Steps | 17 |
| Issues | 1 |
| Annotations | 3 |
| Artifacts | 0 |
| Capture errors | 2 |

## Failure classification

validation_or_test The parent run is still in progress. The projected conclusion is provisional.

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 138497222019 | Find lint baseline and select execution mode | completed | success | 3 | logs/job-138497222019.log |
| 138497288841 | Lint changed Markdown files and publish detailed evidence | completed | failure | 14 | logs/job-138497288841.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 138497288841 | 11 | Preserve lint failure as workflow conclusion | Blocking | medium | Step conclusion: failure |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138497288841 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138497288841 | failure | .github | 21 |  | Process completed with exit code 1. |
| 138497288841 | failure | .github | 20 |  | Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138497222019 | Find lint baseline and select execution mode | logs/job-138497222019.log | 82 | False |  |
| 138497288841 | Lint changed Markdown files and publish detailed evidence | logs/job-138497288841.log | 82 | False |  |

## Evidence coverage

One or more evidence sources were unavailable. This report is Incomplete.

| Source | HTTP status | Limitation |
| --- | --- | --- |
| job_log | Not recorded | run 45408955146 is still in progress; logs will be available when it is complete  |
| job_log | Not recorded | run 45408955146 is still in progress; logs will be available when it is complete  |

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.