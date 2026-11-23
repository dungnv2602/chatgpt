# STE Lint Changed Documentation — run 45158427480

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45158427480 / 1 |
| Run number | 463 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45158427480 |
| Branch | gpt |
| Commit | 75e8531c1cdfa8249aea46610a34f6e84723a4ca |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T10:41:39Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / cancelled |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T10:44:05Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | None |
| Jobs | 2 |
| Steps | 18 |
| Issues | 0 |
| Annotations | 5 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

No failure category identified.

The run conclusion records the workflow outcome. A cancelled run remains in history. Cancellation alone does not create an actionable issue. The generator also excludes known downstream status-propagation steps after cancellation.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137637383531 | Reject superseded runs and find lint baseline | completed | success | 4 | logs/job-137637383531.log |
| 137637457257 | Lint changed Markdown files and publish detailed evidence | completed | cancelled | 14 | logs/job-137637457257.log |

## Actionable step outcomes

No records were captured.

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137637457257 | failure | .github | 1 |  | Canceling since a higher priority waiting request for STE Lint Changed Documentation-refs/heads/gpt exists |
| 137637457257 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137637457257 | failure | .github | 21 |  | Process completed with exit code 1. |
| 137637457257 | failure | .github | 20 |  | Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md. |
| 137637457257 | failure | .github | 48 |  | The operation was canceled. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137637383531 | Reject superseded runs and find lint baseline | logs/job-137637383531.log | 12716 | False |  |
| 137637457257 | Lint changed Markdown files and publish detailed evidence | logs/job-137637457257.log | 41779 | False | Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-23T10:42:15.3621997Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-23T10:42:15.3629019Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T10:42:24.3784671Z ^[[36;1m    failed=1^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T10:42:24.3785361Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T10:42:24.3786093Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T10:42:31.1787123Z ##[error]The operation was canceled., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T10:42:31.1866150Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m, Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T10:42:31.1972539Z ##[error]Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T10:42:31.1982778Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.