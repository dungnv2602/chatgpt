# STE Lint Changed Documentation — run 45123260178

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45123260178 / 1 |
| Run number | 431 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45123260178 |
| Branch | gpt |
| Commit | a845babb053e5cdd122ed280224d3583459f6f1a |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T06:18:52Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | Not captured |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T06:30:36Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | checkout_or_action_download |
| Jobs | 4 |
| Steps | 36 |
| Issues | 2 |
| Annotations | 7 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

checkout_or_action_download, validation_or_test

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137521685460 | Reject superseded runs and find lint baseline | completed | success | 4 | logs/job-137521685460.log |
| 137521751475 | Lint changed Markdown files and publish detailed evidence | completed | failure | 14 | logs/job-137521751475.log |
| 137521909269 | Capture GH Actions diagnostics / Capture GH Actions diagnostics | completed | success | 9 | logs/job-137521909269.log |
| 137521909288 | Capture GH Actions diagnostics / Backfill completed workflow runs | completed | failure | 9 | logs/job-137521909288.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 137521751475 | 11 | Preserve lint failure as workflow conclusion | Blocking | medium | 2026-11-23T06:19:28.7279888Z ^[[36;1m  echo "::error::Changed-document lint failed. See lint_reports/on_changed/latest-lint-report.md."^[[0m |
| checkout_or_action_download | 137521909288 | 5 | Backfill completed runs and explicit requests | Blocking | medium | Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:19:45.1954747Z Traceback (most recent call last): |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137521751475 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137521751475 | failure | .github | 21 |  | Process completed with exit code 1. |
| 137521751475 | failure | .github | 20 |  | Changed-document lint failed. See lint_reports/on_changed/latest-lint-report.md. |
| 137521909269 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137521909269 | failure | .github | 27 |  | Process completed with exit code 1. |
| 137521909288 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137521909288 | failure | .github | 28 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137521685460 | Reject superseded runs and find lint baseline | logs/job-137521685460.log | 12711 | False |  |
| 137521751475 | Lint changed Markdown files and publish detailed evidence | logs/job-137521751475.log | 62651 | False | Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:19:15.7001671Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:19:15.7019026Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T06:19:20.8215976Z ^[[36;1m    failed=1^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T06:19:20.8216627Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T06:19:20.8217225Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-23T06:19:26.6124766Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-23T06:19:26.6132138Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-23T06:19:26.6136434Z ^[[36;1mif [[ "$TOOLING_FAILED" == "1" \|\| "$FULL_FAILED" == "1" \|\| "$CHANGED_FAILED" == "1" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-23T06:19:26.6137188Z ^[[36;1mif [[ "$ANCHOR_OUTCOME" != "skipped" && "$ANCHOR_EXIT" != "0" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T06:19:28.7279888Z ^[[36;1m  echo "::error::Changed-document lint failed. See lint_reports/on_changed/latest-lint-report.md."^[[0m, Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T06:19:28.7375567Z ##[error]Changed-document lint failed. See lint_reports/on_changed/latest-lint-report.md., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T06:19:28.7384060Z ##[error]Process completed with exit code 1. |
| 137521909269 | Capture GH Actions diagnostics / Capture GH Actions diagnostics | logs/job-137521909269.log | 38207 | False | Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:19:43.7116107Z Traceback (most recent call last):, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:19:43.7300991Z ##[error]Process completed with exit code 1., Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:19:43.7358827Z ^[[36;1m    echo "::error::Could not rebase the diagnostic evidence onto gpt."^[[0m, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:19:43.7361576Z ^[[36;1m    echo "::error::Push failed while origin/gpt was unchanged."^[[0m, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:19:43.7362662Z ^[[36;1mecho "::error::Could not publish diagnostic evidence after five attempts."^[[0m |
| 137521909288 | Capture GH Actions diagnostics / Backfill completed workflow runs | logs/job-137521909288.log | 32277 | False | Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:19:45.1954747Z Traceback (most recent call last):, Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:19:45.2104368Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](https://github.com/dungnv2602/chatgpt/blob/gpt/lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.