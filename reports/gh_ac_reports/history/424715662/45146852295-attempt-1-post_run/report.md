# STE Lint Changed Documentation — run 45146852295

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45146852295 / 1 |
| Run number | 447 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45146852295 |
| Branch | gpt |
| Commit | 74d8bf054c149c1858242a93d90293a3dd9bcd20 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T09:25:15Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T09:27:04Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | validation_or_test |
| Jobs | 2 |
| Steps | 18 |
| Issues | 2 |
| Annotations | 5 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

validation_or_test, cancelled

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137598152285 | Reject superseded runs and find lint baseline | completed | success | 4 | logs/job-137598152285.log |
| 137598231454 | Lint changed Markdown files and publish detailed evidence | completed | cancelled | 14 | logs/job-137598231454.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| cancelled | 137598231454 | 7 | Run full technical-document lint | Blocking | high | Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-23T09:25:34.3521024Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m |
| validation_or_test | 137598231454 | 11 | Preserve lint failure as workflow conclusion | Blocking | medium | 2026-11-23T09:25:49.7110899Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137598231454 | failure | .github | 1 |  | Canceling since a higher priority waiting request for STE Lint Changed Documentation-refs/heads/gpt exists |
| 137598231454 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137598231454 | failure | .github | 21 |  | Process completed with exit code 1. |
| 137598231454 | failure | .github | 20 |  | Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md. |
| 137598231454 | failure | .github | 48 |  | The operation was canceled. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137598152285 | Reject superseded runs and find lint baseline | logs/job-137598152285.log | 12721 | False |  |
| 137598231454 | Lint changed Markdown files and publish detailed evidence | logs/job-137598231454.log | 41778 | False | Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-23T09:25:34.3521024Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-23T09:25:34.3531363Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T09:25:42.7703380Z ^[[36;1m    failed=1^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T09:25:42.7704528Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T09:25:42.7706081Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T09:25:49.7033383Z ##[error]The operation was canceled., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T09:25:49.7110899Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m, Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T09:25:49.7213449Z ##[error]Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T09:25:49.7216515Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.