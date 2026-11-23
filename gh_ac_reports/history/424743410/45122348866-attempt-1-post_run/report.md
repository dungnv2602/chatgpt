# STE Lint Full Technical Documentation — run 45122348866

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Full Technical Documentation |
| Workflow path | .github/workflows/ste-lint-full-docs.yml |
| Run / attempt | 45122348866 / 1 |
| Run number | 163 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45122348866 |
| Branch | gpt |
| Commit | 59da3c4be4d6e29c97faebbeb4d8ebe17c8acd55 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T06:10:26Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T06:23:02Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | publication_or_push |
| Jobs | 4 |
| Steps | 30 |
| Issues | 3 |
| Annotations | 0 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

publication_or_push, checkout_or_action_download

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137518766692 | Validate target branch and reject superseded push runs | completed | success | 3 | logs/job-137518766692.log |
| 137518791288 | Full audit and publish detailed evidence | completed | failure | 9 | logs/job-137518791288.log |
| 137518948036 | Capture GH Actions diagnostics / Capture GH Actions diagnostics | completed | failure | 9 | logs/job-137518948036.log |
| 137518948361 | Capture GH Actions diagnostics / Backfill completed workflow runs | completed | failure | 9 | logs/job-137518948361.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| publication_or_push | 137518791288 | 6 | Set workflow result from audit and tooling outcomes | Blocking | high | Full audit and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:10:43.6858305Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m |
| publication_or_push | 137518948036 | 4 | Compile and test the diagnostic reporter | Blocking | high | Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:17.5828090Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR |
| checkout_or_action_download | 137518948361 | 4 | Compile and test the diagnostic reporter | Blocking | medium | Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:11:15.7786011Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR |

## Check annotations

No records were captured.

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137518766692 | Validate target branch and reject superseded push runs | logs/job-137518766692.log | 9983 | False | Validate target branch and reject superseded push runs	Validate branch and guard push runs	2026-11-23T06:10:30.0018281Z ^[[36;1m  echo "::error::Select the gpt branch when manually dispatching this workflow."^[[0m |
| 137518791288 | Full audit and publish detailed evidence | logs/job-137518791288.log | 54443 | False | Full audit and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:10:43.6858305Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Full audit and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:10:43.6865945Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:10:48.5040222Z ^[[36;1m    failed=1^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:10:48.5041544Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:10:48.5054528Z ^[[36;1m        "status": "Passed" if code == 0 else "Failed",^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:10:48.5058188Z ^[[36;1m    "status": "Passed" if anchor_code == 0 else "Failed",^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:10:48.5062372Z ^[[36;1mif [[ "$failed" -ne 0 \|\| "$anchor_status" -ne 0 \|\| "$TOOLING_FAILED" == "1" ]]; then^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:10:48.5062845Z ^[[36;1m  report_status="Failed"^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:10:48.5063180Z ^[[36;1m  failed=1^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:10:48.5071651Z ^[[36;1m  echo "::error::The shared lint report generator failed with exit $generator_status."^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:10:48.5072168Z ^[[36;1m  failed=1^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:10:48.5077233Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Full audit and publish detailed evidence	Set workflow result from audit and tooling outcomes	2026-11-23T06:10:56.6386599Z ^[[36;1m  echo "::error::The full audit found lint or validation failures. See lint_reports/on_repo/latest-lint-report.md."^[[0m, Full audit and publish detailed evidence	Set workflow result from audit and tooling outcomes	2026-11-23T06:10:56.6480437Z ##[error]The full audit found lint or validation failures. See lint_reports/on_repo/latest-lint-report.md., Full audit and publish detailed evidence	Set workflow result from audit and tooling outcomes	2026-11-23T06:10:56.6489247Z ##[error]Process completed with exit code 1. |
| 137518948036 | Capture GH Actions diagnostics / Capture GH Actions diagnostics | logs/job-137518948036.log | 41537 | False | Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:17.5828090Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:17.5852433Z ERROR: test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence), Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:17.5859658Z Traceback (most recent call last):, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:17.5894490Z Traceback (most recent call last):, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:17.5900376Z FAILED (failures=1, errors=1), Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:17.5983100Z ##[error]Process completed with exit code 1., Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:17.7822595Z Traceback (most recent call last):, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:17.7965418Z ##[error]Process completed with exit code 1., Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:17.8002752Z ^[[36;1m    echo "::error::Could not rebase the diagnostic evidence onto gpt."^[[0m, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:17.8004835Z ^[[36;1m    echo "::error::Push failed while origin/gpt was unchanged."^[[0m, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:17.8005688Z ^[[36;1mecho "::error::Could not publish diagnostic evidence after five attempts."^[[0m |
| 137518948361 | Capture GH Actions diagnostics / Backfill completed workflow runs | logs/job-137518948361.log | 32327 | False | Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:11:15.7786011Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR, Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:11:15.7788091Z ERROR: test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence), Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:11:15.7789481Z Traceback (most recent call last):, Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:11:15.7807164Z Traceback (most recent call last):, Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:11:15.7813265Z FAILED (failures=1, errors=1), Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:11:15.7918397Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Repository-wide lint report](../../../../lint_reports/on_repo/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.