# STE Lint Full Technical Documentation — run 45330655561

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Full Technical Documentation |
| Workflow path | .github/workflows/ste-lint-full-docs.yml |
| Run / attempt | 45330655561 / 1 |
| Run number | 181 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45330655561 |
| Branch | gpt |
| Commit | 5fa4f4159d0df5972e2dd6fe130c7073ce8981e2 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T05:03:52Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-24T06:18:33Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | publication_or_push |
| Jobs | 2 |
| Steps | 12 |
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
| 138230792720 | Validate target branch and reject superseded push runs | completed | success | 3 | logs/job-138230792720.log |
| 138230824621 | Full audit and publish detailed evidence | completed | failure | 9 | logs/job-138230824621.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| publication_or_push | 138230824621 | 6 | Set workflow result from audit and tooling outcomes | Blocking | high | Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T05:05:53.9035292Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138230792720 | warning | .github | 35 |  | Could not identify the latest push run. Continue with validation. |
| 138230824621 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138230824621 | failure | .github | 20 |  | Process completed with exit code 1. |
| 138230824621 | failure | .github | 19 |  | The full audit found lint or validation failures. See reports/lint_reports/on_repo/latest-lint-report.md. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138230792720 | Validate target branch and reject superseded push runs | logs/job-138230792720.log | 9236 | False | Validate target branch and reject superseded push runs	UNKNOWN STEP	2026-11-24T05:03:55.6652164Z ^[[36;1m  echo "::error::Select the gpt branch when manually dispatching this workflow."^[[0m |
| 138230824621 | Full audit and publish detailed evidence | logs/job-138230824621.log | 51079 | False | Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T05:05:53.9035292Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T05:05:53.9043159Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T05:05:58.9789470Z ^[[36;1m    failed=1^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T05:05:58.9790450Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T05:05:58.9803456Z ^[[36;1m        "status": "Passed" if code == 0 else "Failed",^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T05:05:58.9807345Z ^[[36;1m    "status": "Passed" if anchor_code == 0 else "Failed",^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T05:05:58.9811641Z ^[[36;1mif [[ "$failed" -ne 0 \|\| "$anchor_status" -ne 0 \|\| "$TOOLING_FAILED" == "1" ]]; then^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T05:05:58.9812119Z ^[[36;1m  report_status="Failed"^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T05:05:58.9812426Z ^[[36;1m  failed=1^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T05:05:58.9821292Z ^[[36;1m  echo "::error::The shared lint report generator failed with exit $generator_status."^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T05:05:58.9821786Z ^[[36;1m  failed=1^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T05:05:58.9827465Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T05:06:07.4118239Z ^[[36;1m  echo "::error::The full audit found lint or validation failures. See reports/lint_reports/on_repo/latest-lint-report.md."^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T05:06:07.4211137Z ##[error]The full audit found lint or validation failures. See reports/lint_reports/on_repo/latest-lint-report.md., Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T05:06:07.4219456Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Repository-wide lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_repo/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.