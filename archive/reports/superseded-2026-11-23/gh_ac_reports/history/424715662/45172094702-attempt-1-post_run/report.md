# STE Lint Changed Documentation — run 45172094702

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45172094702 / 1 |
| Run number | 524 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45172094702 |
| Branch | gpt |
| Commit | 00d1b0a5c0ee10cecb6a25882730fcd8d1749483 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T12:12:25Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / cancelled |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T12:16:32Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | None |
| Jobs | 2 |
| Steps | 17 |
| Issues | 0 |
| Annotations | 3 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

No failure category identified.

The run conclusion records the workflow outcome. A cancelled run remains in history. Cancellation alone does not create an actionable issue. The generator also excludes known downstream status-propagation steps after cancellation.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137683922103 | Reject superseded runs and find lint baseline | completed | success | 4 | logs/job-137683922103.log |
| 137684022118 | Lint changed Markdown files and publish detailed evidence | completed | cancelled | 13 | logs/job-137684022118.log |

## Actionable step outcomes

No records were captured.

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137684022118 | failure | .github | 1 |  | Canceling since a higher priority waiting request for STE Lint Changed Documentation-refs/heads/gpt exists |
| 137684022118 | warning | .github | 4 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137684022118 | failure | .github | 60 |  | The operation was canceled. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137683922103 | Reject superseded runs and find lint baseline | logs/job-137683922103.log | 12714 | False |  |
| 137684022118 | Lint changed Markdown files and publish detailed evidence | logs/job-137684022118.log | 20259 | False | Lint changed Markdown files and publish detailed evidence	Check out current commit	2026-11-23T12:12:43.2966388Z ##[error]The operation was canceled., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T12:12:43.3251530Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.