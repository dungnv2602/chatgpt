# STE Lint Changed Documentation — run 45127450010

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45127450010 / 1 |
| Run number | 436 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45127450010 |
| Branch | gpt |
| Commit | c88346e0663152db270680e43e751011bd356fe6 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T06:55:36Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T06:58:05Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | cancelled |
| Jobs | 2 |
| Steps | 18 |
| Issues | 1 |
| Annotations | 3 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

cancelled

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137535052229 | Reject superseded runs and find lint baseline | completed | success | 4 | logs/job-137535052229.log |
| 137535105386 | Lint changed Markdown files and publish detailed evidence | completed | cancelled | 14 | logs/job-137535105386.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| cancelled | 137535105386 | 7 | Run full technical-document lint | Blocking | high | Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:56:09.1925176Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137535105386 | failure | .github | 1 |  | Canceling since a higher priority waiting request for STE Lint Changed Documentation-refs/heads/gpt exists |
| 137535105386 | warning | .github | 4 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137535105386 | failure | .github | 48 |  | The operation was canceled. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137535052229 | Reject superseded runs and find lint baseline | logs/job-137535052229.log | 12716 | False |  |
| 137535105386 | Lint changed Markdown files and publish detailed evidence | logs/job-137535105386.log | 41670 | False | Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:56:09.1925176Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:56:09.1932482Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T06:56:17.2328510Z ^[[36;1m    failed=1^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T06:56:17.2329932Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T06:56:17.2331253Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T06:57:09.8592323Z ##[error]The operation was canceled., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T06:57:09.8716356Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/reports/lint_reports/on_changed/latest-lint-report.md."^[[0m |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.