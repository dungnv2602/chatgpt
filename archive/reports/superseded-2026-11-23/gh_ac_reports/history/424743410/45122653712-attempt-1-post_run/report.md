# STE Lint Full Technical Documentation — run 45122653712

## Run identity

| Field | Value |
| --- | --- |
| Workflow | STE Lint Full Technical Documentation |
| Workflow path | .github/workflows/ste-lint-full-docs.yml |
| Run / attempt | 45122653712 / 1 |
| Run number | 164 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45122653712 |
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
| Captured (UTC) | 2026-11-23T06:23:28Z |

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
| 137519758603 | Validate target branch and reject superseded push runs | completed | success | 3 | logs/job-137519758603.log |
| 137519782528 | Full audit and publish detailed evidence | completed | failure | 9 | logs/job-137519782528.log |
| 137519938169 | Capture GH Actions diagnostics / Capture GH Actions diagnostics | completed | failure | 9 | logs/job-137519938169.log |
| 137519938195 | Capture GH Actions diagnostics / Backfill completed workflow runs | completed | failure | 9 | logs/job-137519938195.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| publication_or_push | 137519782528 | 6 | Set workflow result from audit and tooling outcomes | Blocking | high | Full audit and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:13:39.9760628Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m |
| publication_or_push | 137519938169 | 4 | Compile and test the diagnostic reporter | Blocking | high | Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:07.3258016Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR |
| checkout_or_action_download | 137519938195 | 4 | Compile and test the diagnostic reporter | Blocking | medium | Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:14:05.4388252Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR |

## Check annotations

No records were captured.

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137519758603 | Validate target branch and reject superseded push runs | logs/job-137519758603.log | 9982 | False | Validate target branch and reject superseded push runs	Validate branch and guard push runs	2026-11-23T06:13:25.0096737Z ^[[36;1m  echo "::error::Select the gpt branch when manually dispatching this workflow."^[[0m |
| 137519782528 | Full audit and publish detailed evidence | logs/job-137519782528.log | 54440 | False | Full audit and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:13:39.9760628Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Full audit and publish detailed evidence	Validate lint and report tooling	2026-11-23T06:13:39.9765635Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:13:45.8917477Z ^[[36;1m    failed=1^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:13:45.8918166Z ^[[36;1m  if [[ "$status" -ne 0 ]]; then failed=1; fi^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:13:45.8928102Z ^[[36;1m        "status": "Passed" if code == 0 else "Failed",^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:13:45.8930862Z ^[[36;1m    "status": "Passed" if anchor_code == 0 else "Failed",^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:13:45.8934289Z ^[[36;1mif [[ "$failed" -ne 0 \|\| "$anchor_status" -ne 0 \|\| "$TOOLING_FAILED" == "1" ]]; then^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:13:45.8934657Z ^[[36;1m  report_status="Failed"^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:13:45.8934936Z ^[[36;1m  failed=1^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:13:45.8941212Z ^[[36;1m  echo "::error::The shared lint report generator failed with exit $generator_status."^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:13:45.8941603Z ^[[36;1m  failed=1^[[0m, Full audit and publish detailed evidence	Run full repository-wide audit and generate structured reports	2026-11-23T06:13:45.8945657Z ^[[36;1mecho "failed=$failed" &gt;&gt; "$GITHUB_OUTPUT"^[[0m, Full audit and publish detailed evidence	Set workflow result from audit and tooling outcomes	2026-11-23T06:13:52.1669971Z ^[[36;1m  echo "::error::The full audit found lint or validation failures. See lint_reports/on_repo/latest-lint-report.md."^[[0m, Full audit and publish detailed evidence	Set workflow result from audit and tooling outcomes	2026-11-23T06:13:52.1746021Z ##[error]The full audit found lint or validation failures. See lint_reports/on_repo/latest-lint-report.md., Full audit and publish detailed evidence	Set workflow result from audit and tooling outcomes	2026-11-23T06:13:52.1752495Z ##[error]Process completed with exit code 1. |
| 137519938169 | Capture GH Actions diagnostics / Capture GH Actions diagnostics | logs/job-137519938169.log | 41537 | False | Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:07.3258016Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:07.3261795Z ERROR: test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence), Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:07.3264462Z Traceback (most recent call last):, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:07.3288300Z Traceback (most recent call last):, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:07.3295621Z FAILED (failures=1, errors=1), Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:07.3427813Z ##[error]Process completed with exit code 1., Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:07.6430752Z Traceback (most recent call last):, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:07.6568872Z ##[error]Process completed with exit code 1., Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:07.6613092Z ^[[36;1m    echo "::error::Could not rebase the diagnostic evidence onto gpt."^[[0m, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:07.6616292Z ^[[36;1m    echo "::error::Push failed while origin/gpt was unchanged."^[[0m, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:14:07.6617619Z ^[[36;1mecho "::error::Could not publish diagnostic evidence after five attempts."^[[0m |
| 137519938195 | Capture GH Actions diagnostics / Backfill completed workflow runs | logs/job-137519938195.log | 32329 | False | Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:14:05.4388252Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR, Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:14:05.4391389Z ERROR: test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence), Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:14:05.4393446Z Traceback (most recent call last):, Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:14:05.4414750Z Traceback (most recent call last):, Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:14:05.4420765Z FAILED (failures=1, errors=1), Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:14:05.4588236Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

[Repository-wide lint report](../../../../lint_reports/on_repo/latest-lint-report.md)

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.