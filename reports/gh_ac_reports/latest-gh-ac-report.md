# STE Lint Changed Documentation — run 45416735141

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45416735141 / 1 |
| Run number | 635 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45416735141 |
| Branch | gpt |
| Commit | 725896a79c8a9c3decef0f8d507cc9cacdaed4fc |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T14:40:30Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-24T15:07:17Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | publication_or_push |
| Jobs | 2 |
| Steps | 17 |
| Issues | 2 |
| Annotations | 4 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

publication_or_push, validation_or_test

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 138525836328 | Find lint baseline and select execution mode | completed | success | 3 | logs/job-138525836328.log |
| 138525943599 | Lint changed Markdown files and publish detailed evidence | completed | failure | 14 | logs/job-138525943599.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| publication_or_push | 138525943599 | 10 | Generate and publish changed-document lint evidence | Blocking | high | 2026-11-24T14:42:42.1239741Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m |
| validation_or_test | 138525943599 | 11 | Preserve lint failure as workflow conclusion | Blocking | medium | 2026-11-24T14:42:43.2583374Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138525943599 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138525943599 | failure | .github | 21 |  | Process completed with exit code 1. |
| 138525943599 | failure | .github | 20 |  | Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md. |
| 138525943599 | failure | .github | 124 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138525836328 | Find lint baseline and select execution mode | logs/job-138525836328.log | 11634 | False | Find lint baseline and select execution mode	Find the latest complete lint baseline	2026-11-24T14:42:00.9852585Z ^[[36;1m  ($report.status == "Passed" or $report.status == "Failed") and^[[0m |
| 138525943599 | Lint changed Markdown files and publish detailed evidence | logs/job-138525943599.log | 69938 | False | Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-24T14:42:36.2608860Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-24T14:42:36.2613723Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Run STE linter on changed Markdown files	2026-11-24T14:42:41.8862893Z ^[[36;1m    failed=1^[[0m, Lint changed Markdown files and publish detailed evidence	Run STE linter on changed Markdown files	2026-11-24T14:42:41.8864086Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Run STE linter on changed Markdown files	2026-11-24T14:42:41.8864705Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T14:42:42.1239741Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T14:42:42.1246175Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T14:42:42.1272527Z ^[[36;1mif [[ "$TOOLING_FAILED" == "1" \|\| "$FULL_FAILED" == "1" \|\| "$CHANGED_FAILED" == "1" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T14:42:42.1273451Z ^[[36;1mif [[ "$ANCHOR_OUTCOME" != "skipped" && "$ANCHOR_EXIT" != "0" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T14:42:43.2493781Z error: could not apply 772b58c... Publish changed-document lint evidence, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T14:42:43.2522730Z ##[error]Process completed with exit code 1., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-24T14:42:43.2583374Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m, Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-24T14:42:43.2695851Z ##[error]Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-24T14:42:43.2697837Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.