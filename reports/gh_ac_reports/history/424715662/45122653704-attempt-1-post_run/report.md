# STE Lint Changed Documentation — run 45122653704

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Changed Documentation |
| Workflow path | .github/workflows/ste-lint-changed.yml |
| Run / attempt | 45122653704 / 1 |
| Run number | 429 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45122653704 |
| Branch | gpt |
| Commit | 535b8052bf1e33cbb04fc19d965ec5e056981959 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T06:13:21Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T06:23:35Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | publication_or_push |
| Jobs | 4 |
| Steps | 36 |
| Issues | 3 |
| Annotations | 0 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

publication_or_push, checkout_or_action_download

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137519758836 | Reject superseded runs and find lint baseline | completed | success | 4 | logs/job-137519758836.log |
| 137519810022 | Lint changed Markdown files and publish detailed evidence | completed | failure | 14 | logs/job-137519810022.log |
| 137520013630 | Capture GH Actions diagnostics / Backfill completed workflow runs | completed | failure | 9 | logs/job-137520013630.log |
| 137520013970 | Capture GH Actions diagnostics / Capture GH Actions diagnostics | completed | failure | 9 | logs/job-137520013970.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| publication_or_push | 137519810022 | 11 | Preserve lint failure as workflow conclusion | Blocking | high | Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:13:46.5936357Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m |
| checkout_or_action_download | 137520013630 | 4 | Compile and test the diagnostic reporter | Blocking | medium | Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:14:24.6256629Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR |
| publication_or_push | 137520013970 | 4 | Compile and test the diagnostic reporter | Blocking | high | Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:26.0810435Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR |

## Check annotations

No records were captured.

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137519758836 | Reject superseded runs and find lint baseline | logs/job-137519758836.log | 12720 | False |  |
| 137519810022 | Lint changed Markdown files and publish detailed evidence | logs/job-137519810022.log | 63005 | False | Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:13:46.5936357Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:13:46.5943652Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T06:13:53.3208856Z ^[[36;1m    failed=1^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T06:13:53.3209501Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Run full technical-document lint	2026-11-23T06:13:53.3210208Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-23T06:14:00.4939645Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-23T06:14:00.4945569Z ^[[36;1m        "status": "Passed" if exit_code == 0 else "Failed",^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-23T06:14:00.4948983Z ^[[36;1mif [[ "$TOOLING_FAILED" == "1" \|\| "$FULL_FAILED" == "1" \|\| "$CHANGED_FAILED" == "1" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Generate and publish changed-document lint evidence	2026-11-23T06:14:00.4949591Z ^[[36;1mif [[ "$ANCHOR_OUTCOME" != "skipped" && "$ANCHOR_EXIT" != "0" ]]; then status="Failed"; fi^[[0m, Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T06:14:03.0910295Z ^[[36;1m  echo "::error::Changed-document lint failed. See lint_reports/on_changed/latest-lint-report.md."^[[0m, Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T06:14:03.1027883Z ##[error]Changed-document lint failed. See lint_reports/on_changed/latest-lint-report.md., Lint changed Markdown files and publish detailed evidence	Preserve lint failure as workflow conclusion	2026-11-23T06:14:03.1039337Z ##[error]Process completed with exit code 1. |
| 137520013630 | Capture GH Actions diagnostics / Backfill completed workflow runs | logs/job-137520013630.log | 37616 | False | Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:14:24.6256629Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR, Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:14:24.6260055Z ERROR: test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence), Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:14:24.6262628Z Traceback (most recent call last):, Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:14:24.6287871Z Traceback (most recent call last):, Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:14:24.6294688Z FAILED (failures=1, errors=1), Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:14:24.6439347Z ##[error]Process completed with exit code 1. |
| 137520013970 | Capture GH Actions diagnostics / Capture GH Actions diagnostics | logs/job-137520013970.log | 41537 | False | Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:26.0810435Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:26.0812742Z ERROR: test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence), Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:26.0814206Z Traceback (most recent call last):, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:26.0830916Z Traceback (most recent call last):, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:26.0835924Z FAILED (failures=1, errors=1), Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:26.0953900Z ##[error]Process completed with exit code 1., Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:26.3683534Z Traceback (most recent call last):, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:26.3797885Z ##[error]Process completed with exit code 1., Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:26.3831464Z ^[[36;1m    echo "::error::Could not rebase the diagnostic evidence onto gpt."^[[0m, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:26.3833828Z ^[[36;1m    echo "::error::Push failed while origin/gpt was unchanged."^[[0m, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:26.3834834Z ^[[36;1mecho "::error::Could not publish diagnostic evidence after five attempts."^[[0m |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Changed-document lint report](../../../../lint_reports/on_changed/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.