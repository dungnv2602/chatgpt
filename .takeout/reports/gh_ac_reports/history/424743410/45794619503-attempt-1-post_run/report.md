# STE Lint Full Technical Documentation — run 45794619503

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Full Technical Documentation |
| Workflow path | .github/workflows/ste-lint-full-docs.yml |
| Run / attempt | 45794619503 / 1 |
| Run number | 208 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45794619503 |
| Branch | gpt |
| Commit | 3f6f505f904e81ec3f3b47796190e1f03ba879ff |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-26T09:43:30Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-26T10:14:17Z |

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
| 139821978343 | Validate target branch and reject superseded push runs | completed | success | 3 | logs/job-139821978343.log |
| 139822017968 | Full audit and publish detailed evidence | completed | failure | 9 | logs/job-139822017968.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 139822017968 | 6 | Set workflow result from audit and tooling outcomes | Blocking | medium | 2026-11-26T09:45:27.0061858Z ^[[36;1m  echo "::error::The full audit found lint or validation failures. See .takeout/reports/lint_reports/on_repo/latest-lint-report.md."^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 139821978343 | warning | .github | 35 |  | Could not identify the latest push run. Continue with validation. |
| 139822017968 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 139822017968 | failure | .github | 20 |  | Process completed with exit code 1. |
| 139822017968 | failure | .github | 19 |  | The full audit found lint or validation failures. See .takeout/reports/lint_reports/on_repo/latest-lint-report.md. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 139821978343 | Validate target branch and reject superseded push runs | logs/job-139821978343.log | 9982 | False | Validate target branch and reject superseded push runs	Validate branch and guard push runs	2026-11-26T09:43:33.3174026Z ^[[36;1m  echo "::error::Select the gpt branch when manually dispatching this workflow."^[[0m |
| 139822017968 | Full audit and publish detailed evidence | logs/job-139822017968.log | 54731 | False | Full audit and publish detailed evidence	Validate lint and report tooling	2026-11-26T09:45:12.5634772Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Full audit and publish detailed evidence	Validate lint and report tooling	2026-11-26T09:45:12.5641246Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-26T09:45:17.1634072Z ^[[36;1m    failed=1^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-26T09:45:17.1634788Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-26T09:45:17.1644831Z ^[[36;1m        "status": "Passed" if code == 0 else "Failed",^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-26T09:45:17.1647961Z ^[[36;1m    "status": "Passed" if anchor_code == 0 else "Failed",^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-26T09:45:17.1651190Z ^[[36;1mif [[ "$failed" -ne 0 \|\| "$anchor_status" -ne 0 \|\| "$TOOLING_FAILED" == "1" ]]; then^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-26T09:45:17.1651599Z ^[[36;1m  report_status="Failed"^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-26T09:45:17.1651858Z ^[[36;1m  failed=1^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-26T09:45:17.1658748Z ^[[36;1m  echo "::error::The shared lint report generator failed with exit $generator_status."^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-26T09:45:17.1659116Z ^[[36;1m  failed=1^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-26T09:45:17.1663479Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Full audit and publish detailed evidence	Set workflow result from audit and tooling outcomes	2026-11-26T09:45:27.0061858Z ^[[36;1m  echo "::error::The full audit found lint or validation failures. See .takeout/reports/lint_reports/on_repo/latest-lint-report.md."^[[0m, Full audit and publish detailed evidence	Set workflow result from audit and tooling outcomes	2026-11-26T09:45:27.0134983Z ##[error]The full audit found lint or validation failures. See .takeout/reports/lint_reports/on_repo/latest-lint-report.md., Full audit and publish detailed evidence	Set workflow result from audit and tooling outcomes	2026-11-26T09:45:27.0141642Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Repository-wide lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/.takeout/reports/lint_reports/on_repo/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.