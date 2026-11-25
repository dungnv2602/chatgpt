# STE Lint Full Technical Documentation — run 45301729199

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Full Technical Documentation |
| Workflow path | .github/workflows/ste-lint-full-docs.yml |
| Run / attempt | 45301729199 / 1 |
| Run number | 179 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45301729199 |
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
| Captured (UTC) | 2026-11-24T06:16:23Z |

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
| 138135641231 | Validate target branch and reject superseded push runs | completed | success | 3 | logs/job-138135641231.log |
| 138135678685 | Full audit and publish detailed evidence | completed | failure | 9 | logs/job-138135678685.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| publication_or_push | 138135678685 | 6 | Set workflow result from audit and tooling outcomes | Blocking | high | Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:14.7382581Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138135641231 | warning | .github | 35 |  | Could not identify the latest push run. Continue with validation. |
| 138135678685 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138135678685 | failure | .github | 20 |  | Process completed with exit code 1. |
| 138135678685 | failure | .github | 19 |  | The full audit found lint or validation failures. See reports/lint_reports/on_repo/latest-lint-report.md. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138135641231 | Validate target branch and reject superseded push runs | logs/job-138135641231.log | 9236 | False | Validate target branch and reject superseded push runs	UNKNOWN STEP	2026-11-24T01:00:48.3836697Z ^[[36;1m  echo "::error::Select the gpt branch when manually dispatching this workflow."^[[0m |
| 138135678685 | Full audit and publish detailed evidence | logs/job-138135678685.log | 45703 | False | Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:14.7382581Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:14.7390034Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:22.2050271Z ^[[36;1m    failed=1^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:22.2051077Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:22.2061485Z ^[[36;1m        "status": "Passed" if code == 0 else "Failed",^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:22.2064725Z ^[[36;1m    "status": "Passed" if anchor_code == 0 else "Failed",^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:22.2068132Z ^[[36;1mif [[ "$failed" -ne 0 \|\| "$anchor_status" -ne 0 \|\| "$TOOLING_FAILED" == "1" ]]; then^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:22.2068541Z ^[[36;1m  report_status="Failed"^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:22.2068796Z ^[[36;1m  failed=1^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:22.2076205Z ^[[36;1m  echo "::error::The shared lint report generator failed with exit $generator_status."^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:22.2076634Z ^[[36;1m  failed=1^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:22.2081174Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:31.0516410Z ^[[36;1m  echo "::error::The full audit found lint or validation failures. See reports/lint_reports/on_repo/latest-lint-report.md."^[[0m, Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:31.0650021Z ##[error]The full audit found lint or validation failures. See reports/lint_reports/on_repo/latest-lint-report.md., Full audit and publish detailed evidence	UNKNOWN STEP	2026-11-24T01:01:31.0660055Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Repository-wide lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_repo/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.