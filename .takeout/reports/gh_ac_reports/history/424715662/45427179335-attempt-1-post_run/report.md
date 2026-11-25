# STE Lint Changed Documentation — run 45427179335

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45427179335 / 1 |
| Run number | 640 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45427179335 |
| Branch | gpt |
| Commit | fd068b52a7e050826f5d83975f4820f1ebb8522e |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T15:34:59Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-24T15:54:08Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | publication_or_push |
| Jobs | 2 |
| Steps | 17 |
| Issues | 2 |
| Annotations | 5 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

publication_or_push, validation_or_test

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 138562244298 | Find lint baseline and select execution mode | completed | success | 3 | logs/job-138562244298.log |
| 138562364811 | Lint changed Markdown files and publish detailed evidence | completed | cancelled | 14 | logs/job-138562364811.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| publication_or_push | 138562364811 | 10 | Generate and publish changed-document lint evidence | Blocking | high | 2026-11-24T15:35:54.9553964Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m |
| validation_or_test | 138562364811 | 11 | Preserve lint failure as workflow conclusion | Blocking | medium | 2026-11-24T15:35:57.4935903Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138562364811 | failure | .github | 1 |  | Canceling since a higher priority waiting request for STE Lint Changed Documentation-refs/heads/gpt exists |
| 138562364811 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138562364811 | failure | .github | 21 |  | Process completed with exit code 1. |
| 138562364811 | failure | .github | 20 |  | Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md. |
| 138562364811 | failure | .github | 115 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138562244298 | Find lint baseline and select execution mode | logs/job-138562244298.log | 11634 | False | Find lint baseline and select execution mode	Find the latest complete lint baseline	2026-11-24T15:35:03.1790594Z ^[[36;1m  ($report.status == "Passed" or $report.status == "Failed") and^[[0m |
| 138562364811 | Lint changed Markdown files and publish detailed evidence | logs/job-138562364811.log | 67468 | False | Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-24T15:35:49.5064458Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-24T15:35:49.5070077Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Run STE linter on changed Markdown files	2026-11-24T15:35:54.7933611Z ^[[36;1m    failed=1^[[0m, Lint changed Markdown files and publish detailed evidence	Run STE linter on changed Markdown files	2026-11-24T15:35:54.7934374Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Run STE linter on changed Markdown files	2026-11-24T15:35:54.7935025Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T15:35:54.9553964Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T15:35:54.9559483Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T15:35:54.9562948Z ^[[36;1mif [[ "$TOOLING_FAILED" == "1" \|\| "$FULL_FAILED" == "1" \|\| "$CHANGED_FAILED" == "1" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T15:35:54.9563431Z ^[[36;1mif [[ "$ANCHOR_OUTCOME" != "skipped" && "$ANCHOR_EXIT" != "0" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T15:35:57.4864510Z error: failed to push some refs to 'https://github.com/dungnv2602/chatgpt', Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T15:35:57.4886866Z ##[error]Process completed with exit code 1., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-24T15:35:57.4935903Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m, Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-24T15:35:57.5003199Z ##[error]Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-24T15:35:57.5005278Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.