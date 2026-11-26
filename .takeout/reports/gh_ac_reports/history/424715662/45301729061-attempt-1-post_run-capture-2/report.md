# STE Lint Changed Documentation — run 45301729061

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45301729061 / 1 |
| Run number | 572 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45301729061 |
| Branch | gpt |
| Commit | 4afaa2c2211858b0455eaf29c523b32eb16e012c |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T01:00:45Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-26T05:10:16Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | publication_or_push |
| Jobs | 2 |
| Steps | 18 |
| Issues | 1 |
| Annotations | 4 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

publication_or_push

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 138135640537 | Reject superseded runs and find lint baseline | completed | success | 4 | logs/job-138135640537.log |
| 138135699767 | Lint changed Markdown files and publish detailed evidence | completed | failure | 14 | logs/job-138135699767.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| publication_or_push | 138135699767 | 11 | Preserve lint failure as workflow conclusion | Blocking | high | Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:42.3489393Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138135640537 | warning | .github | 45 |  | No complete tooling-valid lint baseline exists. Run one full audit. |
| 138135699767 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138135699767 | failure | .github | 21 |  | Process completed with exit code 1. |
| 138135699767 | failure | .github | 20 |  | Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138135640537 | Reject superseded runs and find lint baseline | logs/job-138135640537.log | 14042 | False | Reject superseded runs and find lint baseline	UNKNOWN STEP	2026-11-24T01:00:50.8302015Z ^[[36;1m  ($report.status == "Passed" or $report.status == "Failed") and^[[0m |
| 138135699767 | Lint changed Markdown files and publish detailed evidence | logs/job-138135699767.log | 55086 | False | Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:42.3489393Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:42.3498118Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:48.3705901Z ^[[36;1m    failed=1^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:48.3707088Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:48.3708337Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:54.3275214Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:54.3281204Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:54.3284676Z ^[[36;1mif [[ "$TOOLING_FAILED" == "1" \|\| "$FULL_FAILED" == "1" \|\| "$CHANGED_FAILED" == "1" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:54.3285284Z ^[[36;1mif [[ "$ANCHOR_OUTCOME" != "skipped" && "$ANCHOR_EXIT" != "0" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:56.2157476Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:56.2248306Z ##[error]Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md., Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:56.2256791Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/.takeout/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.