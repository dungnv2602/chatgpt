# Validate Document Standards — run 45122653702

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45122653702 / 1 |
| Run number | 21 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45122653702 |
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
| Captured (UTC) | 2026-11-23T06:23:20Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | publication_or_push |
| Jobs | 3 |
| Steps | 26 |
| Issues | 3 |
| Annotations | 0 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

publication_or_push, checkout_or_action_download

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137519758494 | validate-document-standards | completed | failure | 8 | logs/job-137519758494.log |
| 137519826257 | Capture GH Actions diagnostics / Capture GH Actions diagnostics | completed | failure | 9 | logs/job-137519826257.log |
| 137519826475 | Capture GH Actions diagnostics / Backfill completed workflow runs | completed | failure | 9 | logs/job-137519826475.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| checkout_or_action_download | 137519758494 | 5 | Validate the document type catalog | Blocking | medium | validate-document-standards	Validate the document type catalog	2026-11-23T06:13:32.7156418Z ERROR: Line 46: unsafe or out-of-scope path 'gh_ac_reports/README.md'. |
| publication_or_push | 137519826257 | 4 | Compile and test the diagnostic reporter | Blocking | high | Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:13:48.2104745Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR |
| checkout_or_action_download | 137519826475 | 4 | Compile and test the diagnostic reporter | Blocking | medium | Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:13:47.8475019Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR |

## Check annotations

No records were captured.

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137519758494 | validate-document-standards | logs/job-137519758494.log | 30692 | False | validate-document-standards	Validate the document type catalog	2026-11-23T06:13:32.7156418Z ERROR: Line 46: unsafe or out-of-scope path 'gh_ac_reports/README.md'., validate-document-standards	Validate the document type catalog	2026-11-23T06:13:32.7157445Z ERROR: Line 54: unsafe or out-of-scope path 'gh_ac_reports/scripts/report.py'., validate-document-standards	Validate the document type catalog	2026-11-23T06:13:32.7158458Z ERROR: Line 54: unsafe or out-of-scope path 'gh_ac_reports/assets/report-template.md'., validate-document-standards	Validate the document type catalog	2026-11-23T06:13:32.7159250Z ERROR: Line 54: unsafe or out-of-scope path 'gh_ac_reports/assets/report-schema.json'., validate-document-standards	Validate the document type catalog	2026-11-23T06:13:32.7160096Z ERROR: Line 54: unsafe or out-of-scope path 'gh_ac_reports/scripts/test_report.py'., validate-document-standards	Validate the document type catalog	2026-11-23T06:13:32.7160896Z Catalog validation failed: 5 error(s), 29 document type(s), 59 reference(s)., validate-document-standards	Validate the document type catalog	2026-11-23T06:13:32.7203957Z ##[error]Process completed with exit code 1. |
| 137519826257 | Capture GH Actions diagnostics / Capture GH Actions diagnostics | logs/job-137519826257.log | 41537 | False | Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:13:48.2104745Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:13:48.2109147Z ERROR: test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence), Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:13:48.2111674Z Traceback (most recent call last):, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:13:48.2141125Z Traceback (most recent call last):, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:13:48.2152522Z FAILED (failures=1, errors=1), Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:13:48.2264139Z ##[error]Process completed with exit code 1., Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:13:48.5636918Z Traceback (most recent call last):, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:13:48.5644792Z ##[error]Process completed with exit code 1., Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:13:48.5683582Z ^[[36;1m    echo "::error::Could not rebase the diagnostic evidence onto gpt."^[[0m, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:13:48.5686358Z ^[[36;1m    echo "::error::Push failed while origin/gpt was unchanged."^[[0m, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:13:48.5687417Z ^[[36;1mecho "::error::Could not publish diagnostic evidence after five attempts."^[[0m |
| 137519826475 | Capture GH Actions diagnostics / Backfill completed workflow runs | logs/job-137519826475.log | 32334 | False | Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:13:47.8475019Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR, Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:13:47.8476546Z ERROR: test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence), Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:13:47.8477670Z Traceback (most recent call last):, Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:13:47.8493055Z Traceback (most recent call last):, Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:13:47.8497379Z FAILED (failures=1, errors=1), Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:13:47.8578688Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.