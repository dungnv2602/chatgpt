# Validate Document Standards — run 45122348940

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45122348940 / 1 |
| Run number | 20 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45122348940 |
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
| Captured (UTC) | 2026-11-23T06:23:09Z |

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
| 137518766744 | validate-document-standards | completed | failure | 8 | logs/job-137518766744.log |
| 137518834509 | Capture GH Actions diagnostics / Capture GH Actions diagnostics | completed | failure | 9 | logs/job-137518834509.log |
| 137518834654 | Capture GH Actions diagnostics / Backfill completed workflow runs | completed | failure | 9 | logs/job-137518834654.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| checkout_or_action_download | 137518766744 | 5 | Validate the document type catalog | Blocking | medium | validate-document-standards	Validate the document type catalog	2026-11-23T06:10:37.1132706Z ERROR: Line 46: unsafe or out-of-scope path 'gh_ac_reports/README.md'. |
| publication_or_push | 137518834509 | 4 | Compile and test the diagnostic reporter | Blocking | high | Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:00.8429306Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR |
| checkout_or_action_download | 137518834654 | 4 | Compile and test the diagnostic reporter | Blocking | medium | Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:10:58.8828946Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR |

## Check annotations

No records were captured.

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137518766744 | validate-document-standards | logs/job-137518766744.log | 30690 | False | validate-document-standards	Validate the document type catalog	2026-11-23T06:10:37.1132706Z ERROR: Line 46: unsafe or out-of-scope path 'gh_ac_reports/README.md'., validate-document-standards	Validate the document type catalog	2026-11-23T06:10:37.1134107Z ERROR: Line 54: unsafe or out-of-scope path 'gh_ac_reports/scripts/report.py'., validate-document-standards	Validate the document type catalog	2026-11-23T06:10:37.1135412Z ERROR: Line 54: unsafe or out-of-scope path 'gh_ac_reports/assets/report-template.md'., validate-document-standards	Validate the document type catalog	2026-11-23T06:10:37.1136584Z ERROR: Line 54: unsafe or out-of-scope path 'gh_ac_reports/assets/report-schema.json'., validate-document-standards	Validate the document type catalog	2026-11-23T06:10:37.1137879Z ERROR: Line 54: unsafe or out-of-scope path 'gh_ac_reports/scripts/test_report.py'., validate-document-standards	Validate the document type catalog	2026-11-23T06:10:37.1139031Z Catalog validation failed: 5 error(s), 29 document type(s), 59 reference(s)., validate-document-standards	Validate the document type catalog	2026-11-23T06:10:37.1196299Z ##[error]Process completed with exit code 1. |
| 137518834509 | Capture GH Actions diagnostics / Capture GH Actions diagnostics | logs/job-137518834509.log | 41534 | False | Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:00.8429306Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:00.8437011Z ERROR: test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence), Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:00.8463051Z Traceback (most recent call last):, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:00.8480087Z Traceback (most recent call last):, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:00.8486655Z FAILED (failures=1, errors=1), Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:00.8596247Z ##[error]Process completed with exit code 1., Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:01.0298802Z Traceback (most recent call last):, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:01.0430028Z ##[error]Process completed with exit code 1., Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:01.0465470Z ^[[36;1m    echo "::error::Could not rebase the diagnostic evidence onto gpt."^[[0m, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:01.0467945Z ^[[36;1m    echo "::error::Push failed while origin/gpt was unchanged."^[[0m, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:11:01.0468999Z ^[[36;1mecho "::error::Could not publish diagnostic evidence after five attempts."^[[0m |
| 137518834654 | Capture GH Actions diagnostics / Backfill completed workflow runs | logs/job-137518834654.log | 32327 | False | Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:10:58.8828946Z test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence) ... ERROR, Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:10:58.8832827Z ERROR: test_latest_pointer_and_stage_precedence (test_report.StorageTests.test_latest_pointer_and_stage_precedence), Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:10:58.8835844Z Traceback (most recent call last):, Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:10:58.8861022Z Traceback (most recent call last):, Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:10:58.8868868Z FAILED (failures=1, errors=1), Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:10:58.9005513Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.