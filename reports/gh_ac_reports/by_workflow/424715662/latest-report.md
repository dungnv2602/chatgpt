# STE Lint Changed Documentation — run 45157077230

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45157077230 / 1 |
| Run number | 457 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45157077230 |
| Branch | gpt |
| Commit | 9bc43433477815c90a178ebde7b4fcd260d10842 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T10:32:47Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / cancelled |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T10:35:05Z |

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
| 137632966209 | Reject superseded runs and find lint baseline | completed | success | 4 | logs/job-137632966209.log |
| 137633038597 | Lint changed Markdown files and publish detailed evidence | completed | cancelled | 13 | logs/job-137633038597.log |

## Actionable step outcomes

No records were captured.

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137633038597 | failure | .github | 1 |  | Canceling since a higher priority waiting request for STE Lint Changed Documentation-refs/heads/gpt exists |
| 137633038597 | warning | .github | 4 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137633038597 | failure | .github | 60 |  | The operation was canceled. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137632966209 | Reject superseded runs and find lint baseline | logs/job-137632966209.log | 12721 | False |  |
| 137633038597 | Lint changed Markdown files and publish detailed evidence | logs/job-137633038597.log | 20252 | False | Lint changed Markdown files and publish detailed evidence	Check out current commit	2026-11-23T10:33:42.5667295Z ##[error]The operation was canceled., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T10:33:42.7389988Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.