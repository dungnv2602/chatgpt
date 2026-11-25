# STE Lint Changed Documentation — run 45534135323

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45534135323 / 1 |
| Run number | 695 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45534135323 |
| Branch | gpt |
| Commit | 1b0d7bb58e734e64a7c3b1c778749f44cb097ac5 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-25T02:36:12Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-25T06:28:57Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | publication_or_push |
| Jobs | 2 |
| Steps | 17 |
| Issues | 1 |
| Annotations | 3 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

publication_or_push

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 138936937834 | Find lint baseline and select execution mode | completed | success | 3 | logs/job-138936937834.log |
| 138936969787 | Lint changed Markdown files and publish detailed evidence | completed | failure | 14 | logs/job-138936969787.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| publication_or_push | 138936969787 | 11 | Preserve lint failure as workflow conclusion | Blocking | high | Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-25T02:39:19.4060749Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138936969787 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138936969787 | failure | .github | 21 |  | Process completed with exit code 1. |
| 138936969787 | failure | .github | 20 |  | Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138936937834 | Find lint baseline and select execution mode | logs/job-138936937834.log | 10523 | False | Find lint baseline and select execution mode	UNKNOWN STEP	2026-11-25T02:37:31.2106208Z ^[[36;1m  ($report.status == "Passed" or $report.status == "Failed") and^[[0m |
| 138936969787 | Lint changed Markdown files and publish detailed evidence | logs/job-138936969787.log | 68663 | False | Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-25T02:39:19.4060749Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-25T02:39:19.4065970Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-25T02:39:24.0698763Z ^[[36;1m    failed=1^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-25T02:39:24.0699815Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-25T02:39:24.0700664Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-25T02:39:24.7921075Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-25T02:39:24.7928480Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-25T02:39:24.7932615Z ^[[36;1mif [[ "$TOOLING_FAILED" == "1" \|\| "$FULL_FAILED" == "1" \|\| "$CHANGED_FAILED" == "1" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-25T02:39:24.7933244Z ^[[36;1mif [[ "$ANCHOR_OUTCOME" != "skipped" && "$ANCHOR_EXIT" != "0" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-25T02:39:27.6683698Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-25T02:39:27.6776160Z ##[error]Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md., Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-25T02:39:27.6785344Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.