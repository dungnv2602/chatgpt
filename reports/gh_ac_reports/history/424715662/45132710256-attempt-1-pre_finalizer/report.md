# STE Lint Changed Documentation — run 45132710256

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45132710256 / 1 |
| Run number | 444 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45132710256 |
| Branch | gpt |
| Commit | 90be84e64a8c0d3bc80b65388c33df0fbbef9bc2 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T07:39:35Z |
| Status at capture | in_progress |
| Observed conclusion | Not yet available |
| Projected conclusion | failure |
| Reporter job | in_progress / Pending |
| Capture stage | pre_finalizer |
| Completeness | Incomplete |
| Captured (UTC) | 2026-11-23T07:40:39Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | in_progress |
| Primary category | validation_or_test |
| Jobs | 2 |
| Steps | 18 |
| Issues | 1 |
| Annotations | 3 |
| Artifacts | 0 |
| Capture errors | 2 |

## Failure classification

validation_or_test The parent run is still in progress. The projected conclusion is provisional.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137551655090 | Reject superseded runs and find lint baseline | completed | success | 4 | logs/job-137551655090.log |
| 137551706275 | Lint changed Markdown files and publish detailed evidence | completed | failure | 14 | logs/job-137551706275.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 137551706275 | 11 | Preserve lint failure as workflow conclusion | Blocking | medium | Step conclusion: failure |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137551706275 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137551706275 | failure | .github | 21 |  | Process completed with exit code 1. |
| 137551706275 | failure | .github | 20 |  | Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137551655090 | Reject superseded runs and find lint baseline | logs/job-137551655090.log | 82 | False |  |
| 137551706275 | Lint changed Markdown files and publish detailed evidence | logs/job-137551706275.log | 82 | False |  |

## Evidence coverage

One or more evidence sources were unavailable. This report is Incomplete.

| Source | HTTP status | Limitation |
| --- | --- | --- |
| job_log | Not recorded | run 45132710256 is still in progress; logs will be available when it is complete  |
| job_log | Not recorded | run 45132710256 is still in progress; logs will be available when it is complete  |

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.