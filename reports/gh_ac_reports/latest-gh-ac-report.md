# STE Lint Changed Documentation — run 45170908599

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45170908599 / 1 |
| Run number | 523 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45170908599 |
| Branch | gpt |
| Commit | 1e9dd3d901f1b4749064f6781340fef690e948aa |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T12:04:51Z |
| Status at capture | in_progress |
| Observed conclusion | Not yet available |
| Projected conclusion | failure |
| Reporter job | in_progress / Pending |
| Capture stage | pre_finalizer |
| Completeness | Incomplete |
| Captured (UTC) | 2026-11-23T12:08:03Z |

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

The run conclusion records the workflow outcome. A cancelled run remains in history. Cancellation alone does not create an actionable issue. The generator also excludes known downstream status-propagation steps after cancellation.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137679955104 | Reject superseded runs and find lint baseline | completed | success | 4 | logs/job-137679955104.log |
| 137680057707 | Lint changed Markdown files and publish detailed evidence | completed | failure | 14 | logs/job-137680057707.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 137680057707 | 11 | Preserve lint failure as workflow conclusion | Blocking | medium | Step conclusion: failure |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137680057707 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137680057707 | failure | .github | 21 |  | Process completed with exit code 1. |
| 137680057707 | failure | .github | 20 |  | Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137679955104 | Reject superseded runs and find lint baseline | logs/job-137679955104.log | 82 | False |  |
| 137680057707 | Lint changed Markdown files and publish detailed evidence | logs/job-137680057707.log | 82 | False |  |

## Evidence coverage

One or more evidence sources were unavailable. This report is Incomplete.

| Source | HTTP status | Limitation |
| --- | --- | --- |
| job_log | Not recorded | run 45170908599 is still in progress; logs will be available when it is complete  |
| job_log | Not recorded | run 45170908599 is still in progress; logs will be available when it is complete  |

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.