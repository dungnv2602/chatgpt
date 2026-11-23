# STE Lint Changed Documentation — run 45222817261

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45222817261 / 1 |
| Run number | 565 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45222817261 |
| Branch | gpt |
| Commit | c07921efe1a22db2237caa647d828e66fdd0236d |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T17:00:22Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T23:00:31Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | publication_or_push |
| Jobs | 2 |
| Steps | 18 |
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
| 137861341867 | Reject superseded runs and find lint baseline | completed | success | 4 | logs/job-137861341867.log |
| 137861452009 | Lint changed Markdown files and publish detailed evidence | completed | failure | 14 | logs/job-137861452009.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| publication_or_push | 137861452009 | 11 | Preserve lint failure as workflow conclusion | Blocking | high | Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T17:00:43.6848587Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137861452009 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137861452009 | failure | .github | 21 |  | Process completed with exit code 1. |
| 137861452009 | failure | .github | 20 |  | Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137861341867 | Reject superseded runs and find lint baseline | logs/job-137861341867.log | 11369 | False |  |
| 137861452009 | Lint changed Markdown files and publish detailed evidence | logs/job-137861452009.log | 54461 | False | Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T17:00:43.6848587Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T17:00:43.6852736Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T17:00:48.4708681Z ^[[36;1m    failed=1^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T17:00:48.4709054Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T17:00:48.4709446Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T17:00:52.5094586Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T17:00:52.5097644Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T17:00:52.5099525Z ^[[36;1mif [[ "$TOOLING_FAILED" == "1" \|\| "$FULL_FAILED" == "1" \|\| "$CHANGED_FAILED" == "1" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T17:00:52.5099847Z ^[[36;1mif [[ "$ANCHOR_OUTCOME" != "skipped" && "$ANCHOR_EXIT" != "0" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T17:00:55.1372385Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T17:00:55.1455291Z ##[error]Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md., Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T17:00:55.1461365Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.