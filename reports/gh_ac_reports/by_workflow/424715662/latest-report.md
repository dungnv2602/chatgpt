# STE Lint Changed Documentation — run 45138510922

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45138510922 / 1 |
| Run number | 446 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45138510922 |
| Branch | gpt |
| Commit | 199dbf3694d547f2fbcbdde23a44c16250493d0c |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T08:25:37Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T08:27:53Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | publication_or_push |
| Jobs | 2 |
| Steps | 18 |
| Issues | 2 |
| Annotations | 4 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

publication_or_push, validation_or_test

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137570469880 | Reject superseded runs and find lint baseline | completed | success | 4 | logs/job-137570469880.log |
| 137570547781 | Lint changed Markdown files and publish detailed evidence | completed | failure | 14 | logs/job-137570547781.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| publication_or_push | 137570547781 | 10 | Generate and publish changed-document lint evidence | Blocking | high | 2026-11-23T08:26:13.1748521Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m |
| validation_or_test | 137570547781 | 11 | Preserve lint failure as workflow conclusion | Blocking | medium | 2026-11-23T08:26:15.3559514Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137570547781 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137570547781 | failure | .github | 21 |  | Process completed with exit code 1. |
| 137570547781 | failure | .github | 20 |  | Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md. |
| 137570547781 | failure | .github | 113 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137570469880 | Reject superseded runs and find lint baseline | logs/job-137570469880.log | 12714 | False |  |
| 137570547781 | Lint changed Markdown files and publish detailed evidence | logs/job-137570547781.log | 63244 | False | Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-23T08:25:58.0376733Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-23T08:25:58.0384594Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T08:26:06.3854083Z ^[[36;1m    failed=1^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T08:26:06.3855294Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T08:26:06.3856639Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-23T08:26:13.1748521Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-23T08:26:13.1754654Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-23T08:26:13.1758223Z ^[[36;1mif [[ "$TOOLING_FAILED" == "1" \|\| "$FULL_FAILED" == "1" \|\| "$CHANGED_FAILED" == "1" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-23T08:26:13.1758852Z ^[[36;1mif [[ "$ANCHOR_OUTCOME" != "skipped" && "$ANCHOR_EXIT" != "0" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-23T08:26:15.3465795Z error: failed to push some refs to 'https://github.com/dungnv2602/chatgpt', Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-23T08:26:15.3500120Z ##[error]Process completed with exit code 1., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T08:26:15.3559514Z ^[[36;1m  echo "::error::Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md."^[[0m, Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T08:26:15.3662105Z ##[error]Changed-document lint failed. See reports/lint_reports/on_changed/latest-lint-report.md., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T08:26:15.3668957Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/reports/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.