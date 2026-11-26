# STE Lint Changed Documentation — run 45816537286

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45816537286 / 1 |
| Run number | 799 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45816537286 |
| Branch | gpt |
| Commit | 8dc231ed8ac78ec53589b416b5b88b92a7a77b12 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-26T12:06:14Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-26T12:08:06Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | validation_or_test |
| Jobs | 2 |
| Steps | 17 |
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
| 139897606574 | Find lint baseline and select execution mode | completed | success | 3 | logs/job-139897606574.log |
| 139897667772 | Lint changed Markdown files and publish detailed evidence | completed | failure | 14 | logs/job-139897667772.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 139897667772 | 11 | Preserve lint failure as workflow conclusion | Blocking | medium | 2026-11-26T12:07:08.4859050Z ^[[36;1m  echo "::error::Changed-document lint failed. See .takeout/reports/lint_reports/on_changed/latest-lint-report.md."^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 139897606574 | warning | .github | 46 |  | No complete tooling-valid lint baseline exists. Run one full audit. |
| 139897667772 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 139897667772 | failure | .github | 21 |  | Process completed with exit code 1. |
| 139897667772 | failure | .github | 20 |  | Changed-document lint failed. See .takeout/reports/lint_reports/on_changed/latest-lint-report.md. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 139897606574 | Find lint baseline and select execution mode | logs/job-139897606574.log | 11723 | False | Find lint baseline and select execution mode	Find the latest complete lint baseline	2026-11-26T12:06:18.4960356Z ^[[36;1m  ($report.status == "Passed" or $report.status == "Failed") and^[[0m |
| 139897667772 | Lint changed Markdown files and publish detailed evidence | logs/job-139897667772.log | 63230 | False | Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-26T12:06:54.2902080Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-26T12:06:54.2906413Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-26T12:06:58.4797787Z ^[[36;1m    failed=1^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-26T12:06:58.4798165Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-26T12:06:58.4798563Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-26T12:07:06.5595486Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-26T12:07:06.5598740Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-26T12:07:06.5601285Z ^[[36;1mif [[ "$TOOLING_FAILED" == "1" \|\| "$FULL_FAILED" == "1" \|\| "$CHANGED_FAILED" == "1" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-26T12:07:06.5601706Z ^[[36;1mif [[ "$ANCHOR_OUTCOME" != "skipped" && "$ANCHOR_EXIT" != "0" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-26T12:07:08.4859050Z ^[[36;1m  echo "::error::Changed-document lint failed. See .takeout/reports/lint_reports/on_changed/latest-lint-report.md."^[[0m, Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-26T12:07:08.4950904Z ##[error]Changed-document lint failed. See .takeout/reports/lint_reports/on_changed/latest-lint-report.md., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-26T12:07:08.4956682Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/.takeout/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.