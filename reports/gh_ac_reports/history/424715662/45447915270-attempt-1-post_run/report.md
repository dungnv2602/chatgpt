# STE Lint Changed Documentation — run 45447915270

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45447915270 / 1 |
| Run number | 670 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45447915270 |
| Branch | gpt |
| Commit | f150a5b5bc7f5eeaee922e85106564e78e10ffe3 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-24T17:22:50Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-24T17:25:06Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | validation_or_test |
| Jobs | 2 |
| Steps | 17 |
| Issues | 1 |
| Annotations | 3 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

validation_or_test

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 138636678427 | Find lint baseline and select execution mode | completed | success | 3 | logs/job-138636678427.log |
| 138636762686 | Lint changed Markdown files and publish detailed evidence | completed | failure | 14 | logs/job-138636762686.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 138636762686 | 11 | Preserve lint failure as workflow conclusion | Blocking | medium | 2026-11-24T17:23:33.8452053Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138636762686 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138636762686 | failure | .github | 21 |  | Process completed with exit code 1. |
| 138636762686 | failure | .github | 20 |  | Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138636678427 | Find lint baseline and select execution mode | logs/job-138636678427.log | 11637 | False | Find lint baseline and select execution mode	Find the latest complete lint baseline	2026-11-24T17:22:53.6948298Z ^[[36;1m  ($report.status == "Passed" or $report.status == "Failed") and^[[0m |
| 138636762686 | Lint changed Markdown files and publish detailed evidence | logs/job-138636762686.log | 66936 | False | Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-24T17:23:26.8426813Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-24T17:23:26.8430483Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Run STE linter on changed Markdown files	2026-11-24T17:23:31.6651849Z ^[[36;1m    failed=1^[[0m, Lint changed Markdown files and publish detailed evidence	Run STE linter on changed Markdown files	2026-11-24T17:23:31.6652420Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Run STE linter on changed Markdown files	2026-11-24T17:23:31.6653058Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T17:23:31.8062376Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T17:23:31.8067163Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T17:23:31.8070076Z ^[[36;1mif [[ "$TOOLING_FAILED" == "1" \|\| "$FULL_FAILED" == "1" \|\| "$CHANGED_FAILED" == "1" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-24T17:23:31.8070540Z ^[[36;1mif [[ "$ANCHOR_OUTCOME" != "skipped" && "$ANCHOR_EXIT" != "0" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-24T17:23:33.8452053Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m, Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-24T17:23:33.8546972Z ##[error]Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-24T17:23:33.8554483Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.