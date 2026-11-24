# STE Lint Full Technical Documentation — run 45343010144

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Full Technical Documentation |
| Workflow path | .github/workflows/ste-lint-full-docs.yml |
| Run / attempt | 45343010144 / 1 |
| Run number | 184 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45343010144 |
| Branch | gpt |
| Commit | 3f27a3985619466e0df3c64b895163acb2ee33b7 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T06:46:56Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-24T06:49:27Z |

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
| 138270856853 | Validate target branch and reject superseded push runs | completed | success | 3 | logs/job-138270856853.log |
| 138270893658 | Full audit and publish detailed evidence | completed | failure | 9 | logs/job-138270893658.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 138270893658 | 6 | Set workflow result from audit and tooling outcomes | Blocking | medium | 2026-11-24T06:47:47.4979692Z ^[[36;1m  echo "::error::The full audit found lint or validation failures. See reports/lint_reports/on_repo/latest-lint-report.md."^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138270856853 | warning | .github | 35 |  | Could not identify the latest push run. Continue with validation. |
| 138270893658 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138270893658 | failure | .github | 20 |  | Process completed with exit code 1. |
| 138270893658 | failure | .github | 19 |  | The full audit found lint or validation failures. See reports/lint_reports/on_repo/latest-lint-report.md. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138270856853 | Validate target branch and reject superseded push runs | logs/job-138270856853.log | 9989 | False | Validate target branch and reject superseded push runs	Validate branch and guard push runs	2026-11-24T06:47:00.0999873Z ^[[36;1m  echo "::error::Select the gpt branch when manually dispatching this workflow."^[[0m |
| 138270893658 | Full audit and publish detailed evidence | logs/job-138270893658.log | 54536 | False | Full audit and publish detailed evidence	Validate lint and report tooling	2026-11-24T06:47:36.0426305Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Full audit and publish detailed evidence	Validate lint and report tooling	2026-11-24T06:47:36.0445796Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:47:40.3317265Z ^[[36;1m    failed=1^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:47:40.3317663Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:47:40.3323492Z ^[[36;1m        "status": "Passed" if code == 0 else "Failed",^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:47:40.3325135Z ^[[36;1m    "status": "Passed" if anchor_code == 0 else "Failed",^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:47:40.3327187Z ^[[36;1mif [[ "$failed" -ne 0 \|\| "$anchor_status" -ne 0 \|\| "$TOOLING_FAILED" == "1" ]]; then^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:47:40.3327414Z ^[[36;1m  report_status="Failed"^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:47:40.3327561Z ^[[36;1m  failed=1^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:47:40.3331626Z ^[[36;1m  echo "::error::The shared lint report generator failed with exit $generator_status."^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:47:40.3331867Z ^[[36;1m  failed=1^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-24T06:47:40.3334361Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Full audit and publish detailed evidence	Set workflow result from audit and tooling outcomes	2026-11-24T06:47:47.4979692Z ^[[36;1m  echo "::error::The full audit found lint or validation failures. See reports/lint_reports/on_repo/latest-lint-report.md."^[[0m, Full audit and publish detailed evidence	Set workflow result from audit and tooling outcomes	2026-11-24T06:47:47.5080726Z ##[error]The full audit found lint or validation failures. See reports/lint_reports/on_repo/latest-lint-report.md., Full audit and publish detailed evidence	Set workflow result from audit and tooling outcomes	2026-11-24T06:47:47.5087471Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Repository-wide lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_repo/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.