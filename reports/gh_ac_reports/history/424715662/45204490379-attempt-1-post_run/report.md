# STE Lint Changed Documentation — run 45204490379

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45204490379 / 1 |
| Run number | 558 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45204490379 |
| Branch | gpt |
| Commit | 17711a6e84ca8884ef4e421f2d8a7d81384510f7 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T15:22:26Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T22:59:35Z |

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
| 137796397643 | Reject superseded runs and find lint baseline | completed | success | 4 | logs/job-137796397643.log |
| 137796504213 | Lint changed Markdown files and publish detailed evidence | completed | failure | 14 | logs/job-137796504213.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| publication_or_push | 137796504213 | 11 | Preserve lint failure as workflow conclusion | Blocking | high | Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T15:22:47.2396125Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137796504213 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137796504213 | failure | .github | 21 |  | Process completed with exit code 1. |
| 137796504213 | failure | .github | 20 |  | Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137796397643 | Reject superseded runs and find lint baseline | logs/job-137796397643.log | 11370 | False |  |
| 137796504213 | Lint changed Markdown files and publish detailed evidence | logs/job-137796504213.log | 56213 | False | Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T15:22:47.2396125Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T15:22:47.2403616Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T15:22:56.5527101Z ^[[36;1m    failed=1^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T15:22:56.5528270Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T15:22:56.5529548Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T15:23:03.2141649Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T15:23:03.2147767Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T15:23:03.2151444Z ^[[36;1mif [[ "$TOOLING_FAILED" == "1" \|\| "$FULL_FAILED" == "1" \|\| "$CHANGED_FAILED" == "1" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T15:23:03.2152063Z ^[[36;1mif [[ "$ANCHOR_OUTCOME" != "skipped" && "$ANCHOR_EXIT" != "0" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T15:23:06.0324441Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m, Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T15:23:06.0436520Z ##[error]Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md., Lint changed Markdown files and publish detailed evidence	UNKNOWN STEP	2026-11-23T15:23:06.0445654Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.