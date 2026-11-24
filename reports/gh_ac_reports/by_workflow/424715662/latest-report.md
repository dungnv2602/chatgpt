# STE Lint Changed Documentation — run 45440436265

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45440436265 / 1 |
| Run number | 664 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45440436265 |
| Branch | gpt |
| Commit | 80e67808c0b97fbd4f1e69896c806b2145316d7c |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T16:43:30Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-24T16:54:24Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | validation_or_test |
| Jobs | 2 |
| Steps | 17 |
| Issues | 1 |
| Annotations | 3 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

validation_or_test

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 138609727465 | Find lint baseline and select execution mode | completed | success | 3 | logs/job-138609727465.log |
| 138609827560 | Lint changed Markdown files and publish detailed evidence | completed | failure | 14 | logs/job-138609827560.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 138609827560 | 11 | Preserve lint failure as workflow conclusion | Blocking | medium | 2026-11-24T16:44:31.6386257Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138609827560 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138609827560 | failure | .github | 21 |  | Process completed with exit code 1. |
| 138609827560 | failure | .github | 20 |  | Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138609727465 | Find lint baseline and select execution mode | logs/job-138609727465.log | 11637 | False | Find lint baseline and select execution mode	Find the latest complete lint baseline	2026-11-24T16:43:34.1242047Z ^[[36;1m  ($report.status == "Passed" or $report.status == "Failed") and^[[0m |
| 138609827560 | Lint changed Markdown files and publish detailed evidence | logs/job-138609827560.log | 67975 | False | Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-24T16:44:22.1630066Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-24T16:44:22.1637349Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Run STE linter on changed Markdown files	2026-11-24T16:44:28.2043307Z ^[[36;1m    failed=1^[[0m, Lint changed Markdown files and publish detailed evidence	Run STE linter on changed Markdown files	2026-11-24T16:44:28.2043960Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Run STE linter on changed Markdown files	2026-11-24T16:44:28.2044723Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T16:44:29.5282175Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T16:44:29.5307897Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T16:44:29.5311487Z ^[[36;1mif [[ "$TOOLING_FAILED" == "1" \|\| "$FULL_FAILED" == "1" \|\| "$CHANGED_FAILED" == "1" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T16:44:29.5312112Z ^[[36;1mif [[ "$ANCHOR_OUTCOME" != "skipped" && "$ANCHOR_EXIT" != "0" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-24T16:44:31.6386257Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m, Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-24T16:44:31.6493049Z ##[error]Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-24T16:44:31.6500926Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.