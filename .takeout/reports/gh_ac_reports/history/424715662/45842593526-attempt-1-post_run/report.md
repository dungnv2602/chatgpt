# STE Lint Changed Documentation — run 45842593526

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45842593526 / 1 |
| Run number | 813 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45842593526 |
| Branch | gpt |
| Commit | 72e52a26c059d2b3795246916fba9d1a48c1e947 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-26T14:47:49Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-26T14:51:33Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | publication_or_push |
| Jobs | 2 |
| Steps | 17 |
| Issues | 1 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

publication_or_push

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests may bypass retry timing for one exact completed run, but they cannot override the error-only retention rule. Successful and cancellation-only runs are never retained.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 139987878493 | Find lint baseline and select execution mode | completed | success | 3 | logs/job-139987878493.log |
| 139987942965 | Lint changed Markdown files and publish detailed evidence | completed | failure | 14 | logs/job-139987942965.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| publication_or_push | 139987942965 | 10 | Generate and publish changed-document lint evidence | Blocking | high | 2026-11-26T14:48:40.0530488Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 139987942965 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 139987942965 | failure | .github | 120 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 139987878493 | Find lint baseline and select execution mode | logs/job-139987878493.log | 11646 | False | Find lint baseline and select execution mode	Find the latest complete lint baseline	2026-11-26T14:47:52.6563323Z ^[[36;1m  ($report.status == "Passed" or $report.status == "Failed") and^[[0m |
| 139987942965 | Lint changed Markdown files and publish detailed evidence | logs/job-139987942965.log | 73570 | False | Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-26T14:48:32.0028275Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-26T14:48:32.0033890Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Run STE linter on changed Markdown files	2026-11-26T14:48:39.8205467Z ^[[36;1m    failed=1^[[0m, Lint changed Markdown files and publish detailed evidence	Run STE linter on changed Markdown files	2026-11-26T14:48:39.8206494Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Run STE linter on changed Markdown files	2026-11-26T14:48:39.8207663Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-26T14:48:40.0530488Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-26T14:48:40.0538166Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-26T14:48:40.0542321Z ^[[36;1mif [[ "$TOOLING_FAILED" == "1" \|\| "$FULL_FAILED" == "1" \|\| "$CHANGED_FAILED" == "1" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-26T14:48:40.0542998Z ^[[36;1mif [[ "$ANCHOR_OUTCOME" != "skipped" && "$ANCHOR_EXIT" != "0" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-26T14:48:41.1275103Z error: failed to push some refs to 'https://github.com/dungnv2602/chatgpt', Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-26T14:48:41.1296608Z ##[error]Process completed with exit code 1., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-26T14:48:41.1360508Z ^[[36;1m  echo "::error::Changed-document lint failed. See .takeout/reports/lint_reports/on_changed/latest-lint-report.md."^[[0m |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/.takeout/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.