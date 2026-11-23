# STE Lint Full Technical Documentation — run 45127311600

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Full Technical Documentation |
| Workflow path | .github/workflows/ste-lint-full-docs.yml |
| Run / attempt | 45127311600 / 1 |
| Run number | 168 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45127311600 |
| Branch | gpt |
| Commit | fb7ea1ff7f831a707ba74863f56b2241d16c8a79 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T06:54:25Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T06:55:47Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | cancelled |
| Jobs | 2 |
| Steps | 12 |
| Issues | 1 |
| Annotations | 4 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

cancelled

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137534611812 | Validate target branch and reject superseded push runs | completed | success | 3 | logs/job-137534611812.log |
| 137534645371 | Full audit and publish detailed evidence | completed | cancelled | 9 | logs/job-137534645371.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| cancelled | 137534645371 | 4 | Validate lint and report tooling | Blocking | high | Full audit and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:54:56.8094043Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137534611812 | warning | .github | 35 |  | Could not identify the latest push run. Continue with validation. |
| 137534645371 | failure | .github | 1 |  | Canceling since a higher priority waiting request for STE Lint Full Technical Documentation-refs/heads/gpt exists |
| 137534645371 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137534645371 | failure | .github | 32 |  | The operation was canceled. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137534611812 | Validate target branch and reject superseded push runs | logs/job-137534611812.log | 9983 | False | Validate target branch and reject superseded push runs	Validate branch and guard push runs	2026-11-23T06:54:44.1855641Z ^[[36;1m  echo "::error::Select the gpt branch when manually dispatching this workflow."^[[0m |
| 137534645371 | Full audit and publish detailed evidence | logs/job-137534645371.log | 23449 | False | Full audit and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:54:56.8094043Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Full audit and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:54:56.8097113Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Full audit and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:55:01.6229740Z ##[error]The operation was canceled. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Repository-wide lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_repo/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.