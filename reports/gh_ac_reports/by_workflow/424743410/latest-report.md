# STE Lint Full Technical Documentation — run 45343527317

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Full Technical Documentation |
| Workflow path | .github/workflows/ste-lint-full-docs.yml |
| Run / attempt | 45343527317 / 1 |
| Run number | 185 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45343527317 |
| Branch | gpt |
| Commit | f063afecb480325a871204c1e2ff50342c1df432 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T06:51:06Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-24T06:55:34Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | validation_or_test |
| Jobs | 2 |
| Steps | 12 |
| Issues | 1 |
| Annotations | 4 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

validation_or_test

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 138272520220 | Validate target branch and reject superseded push runs | completed | success | 3 | logs/job-138272520220.log |
| 138272561709 | Full audit and publish detailed evidence | completed | failure | 9 | logs/job-138272561709.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 138272561709 | 6 | Set workflow result from audit and tooling outcomes | Blocking | medium | 2026-11-24T06:52:18.2627282Z ^[[36;1m  echo "::error::The full audit found lint or validation failures. See reports/lint_reports/on_repo/latest-lint-report.md."^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138272520220 | warning | .github | 35 |  | Could not identify the latest push run. Continue with validation. |
| 138272561709 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138272561709 | failure | .github | 20 |  | Process completed with exit code 1. |
| 138272561709 | failure | .github | 19 |  | The full audit found lint or validation failures. See reports/lint_reports/on_repo/latest-lint-report.md. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138272520220 | Validate target branch and reject superseded push runs | logs/job-138272520220.log | 9983 | False | Validate target branch and reject superseded push runs	Validate branch and guard push runs	2026-11-24T06:51:10.7147886Z ^[[36;1m  echo "::error::Select the gpt branch when manually dispatching this workflow."^[[0m |
| 138272561709 | Full audit and publish detailed evidence | logs/job-138272561709.log | 54536 | False | Full audit and publish detailed evidence	Validate lint and report tooling	2026-11-24T06:52:06.7931906Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Full audit and publish detailed evidence	Validate lint and report tooling	2026-11-24T06:52:06.7937830Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:52:11.1077259Z ^[[36;1m    failed=1^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:52:11.1078099Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:52:11.1094239Z ^[[36;1m        "status": "Passed" if code == 0 else "Failed",^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:52:11.1098201Z ^[[36;1m    "status": "Passed" if anchor_code == 0 else "Failed",^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:52:11.1103678Z ^[[36;1mif [[ "$failed" -ne 0 \|\| "$anchor_status" -ne 0 \|\| "$TOOLING_FAILED" == "1" ]]; then^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:52:11.1104085Z ^[[36;1m  report_status="Failed"^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:52:11.1104436Z ^[[36;1m  failed=1^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:52:11.1114234Z ^[[36;1m  echo "::error::The shared lint report generator failed with exit $generator_status."^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:52:11.1114931Z ^[[36;1m  failed=1^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:52:11.1121445Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Full audit and publish detailed evidence	Set workflow result from audit and tooling outcomes	2026-11-24T06:52:18.2627282Z ^[[36;1m  echo "::error::The full audit found lint or validation failures. See reports/lint_reports/on_repo/latest-lint-report.md."^[[0m, Full audit and publish detailed evidence	Set workflow result from audit and tooling outcomes	2026-11-24T06:52:18.2704194Z ##[error]The full audit found lint or validation failures. See reports/lint_reports/on_repo/latest-lint-report.md., Full audit and publish detailed evidence	Set workflow result from audit and tooling outcomes	2026-11-24T06:52:18.2711403Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Repository-wide lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_repo/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.