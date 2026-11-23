# STE Lint Full Technical Documentation — run 45123530849

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Full Technical Documentation |
| Workflow path | .github/workflows/ste-lint-full-docs.yml |
| Run / attempt | 45123530849 / 1 |
| Run number | 166 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45123530849 |
| Branch | gpt |
| Commit | 167c964f769ae57360c86c8b7b5781389a96d614 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T06:21:19Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T06:30:44Z |

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

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137522539668 | Validate target branch and reject superseded push runs | completed | success | 3 | logs/job-137522539668.log |
| 137522576770 | Full audit and publish detailed evidence | completed | failure | 9 | logs/job-137522576770.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 137522576770 | 6 | Set workflow result from audit and tooling outcomes | Blocking | medium | 2026-11-23T06:21:49.5192683Z ^[[36;1m  echo "::error::The full audit found lint or validation failures. See lint_reports/on_repo/latest-lint-report.md."^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137522539668 | warning | .github | 35 |  | Could not identify the latest push run. Continue with validation. |
| 137522576770 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137522576770 | failure | .github | 20 |  | Process completed with exit code 1. |
| 137522576770 | failure | .github | 19 |  | The full audit found lint or validation failures. See lint_reports/on_repo/latest-lint-report.md. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137522539668 | Validate target branch and reject superseded push runs | logs/job-137522539668.log | 9983 | False | Validate target branch and reject superseded push runs	Validate branch and guard push runs	2026-11-23T06:21:23.1414973Z ^[[36;1m  echo "::error::Select the gpt branch when manually dispatching this workflow."^[[0m |
| 137522576770 | Full audit and publish detailed evidence | logs/job-137522576770.log | 54442 | False | Full audit and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:21:36.9121359Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Full audit and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:21:36.9126518Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:21:41.1000455Z ^[[36;1m    failed=1^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:21:41.1001038Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:21:41.1009320Z ^[[36;1m        "status": "Passed" if code == 0 else "Failed",^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:21:41.1011992Z ^[[36;1m    "status": "Passed" if anchor_code == 0 else "Failed",^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:21:41.1014873Z ^[[36;1mif [[ "$failed" -ne 0 \|\| "$anchor_status" -ne 0 \|\| "$TOOLING_FAILED" == "1" ]]; then^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:21:41.1015198Z ^[[36;1m  report_status="Failed"^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:21:41.1015412Z ^[[36;1m  failed=1^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:21:41.1021163Z ^[[36;1m  echo "::error::The shared lint report generator failed with exit $generator_status."^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:21:41.1021491Z ^[[36;1m  failed=1^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:21:41.1024840Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Full audit and publish detailed evidence	Set workflow result from audit and tooling outcomes	2026-11-23T06:21:49.5192683Z ^[[36;1m  echo "::error::The full audit found lint or validation failures. See lint_reports/on_repo/latest-lint-report.md."^[[0m, Full audit and publish detailed evidence	Set workflow result from audit and tooling outcomes	2026-11-23T06:21:49.5286258Z ##[error]The full audit found lint or validation failures. See lint_reports/on_repo/latest-lint-report.md., Full audit and publish detailed evidence	Set workflow result from audit and tooling outcomes	2026-11-23T06:21:49.5295926Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Repository-wide lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/lint_reports/on_repo/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.