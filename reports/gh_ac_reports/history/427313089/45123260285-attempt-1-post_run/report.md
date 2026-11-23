# Validate Document Standards — run 45123260285

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45123260285 / 1 |
| Run number | 23 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45123260285 |
| Branch | gpt |
| Commit | a845babb053e5cdd122ed280224d3583459f6f1a |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T06:18:52Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T06:23:54Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | checkout_or_action_download |
| Jobs | 3 |
| Steps | 26 |
| Issues | 2 |
| Annotations | 0 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

checkout_or_action_download

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137521686368 | validate-document-standards | completed | failure | 8 | logs/job-137521686368.log |
| 137521768927 | Capture GH Actions diagnostics / Backfill completed workflow runs | completed | failure | 9 | logs/job-137521768927.log |
| 137521769370 | Capture GH Actions diagnostics / Capture GH Actions diagnostics | completed | success | 9 | logs/job-137521769370.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| checkout_or_action_download | 137521686368 | 5 | Validate the document type catalog | Blocking | medium | validate-document-standards	Validate the document type catalog	2026-11-23T06:19:03.7857846Z ERROR: Line 46: unsafe or out-of-scope path 'gh_ac_reports/README.md'. |
| checkout_or_action_download | 137521768927 | 5 | Backfill completed runs and explicit requests | Blocking | medium | Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:19:24.9715460Z Traceback (most recent call last): |

## Check annotations

No records were captured.

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137521686368 | validate-document-standards | logs/job-137521686368.log | 30690 | False | validate-document-standards	Validate the document type catalog	2026-11-23T06:19:03.7857846Z ERROR: Line 46: unsafe or out-of-scope path 'gh_ac_reports/README.md'., validate-document-standards	Validate the document type catalog	2026-11-23T06:19:03.7859570Z ERROR: Line 54: unsafe or out-of-scope path 'gh_ac_reports/scripts/report.py'., validate-document-standards	Validate the document type catalog	2026-11-23T06:19:03.7860991Z ERROR: Line 54: unsafe or out-of-scope path 'gh_ac_reports/assets/report-template.md'., validate-document-standards	Validate the document type catalog	2026-11-23T06:19:03.7862322Z ERROR: Line 54: unsafe or out-of-scope path 'gh_ac_reports/assets/report-schema.json'., validate-document-standards	Validate the document type catalog	2026-11-23T06:19:03.7863485Z ERROR: Line 54: unsafe or out-of-scope path 'gh_ac_reports/scripts/test_report.py'., validate-document-standards	Validate the document type catalog	2026-11-23T06:19:03.7864478Z Catalog validation failed: 5 error(s), 29 document type(s), 59 reference(s)., validate-document-standards	Validate the document type catalog	2026-11-23T06:19:03.7922528Z ##[error]Process completed with exit code 1. |
| 137521768927 | Capture GH Actions diagnostics / Backfill completed workflow runs | logs/job-137521768927.log | 32278 | False | Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:19:24.9715460Z Traceback (most recent call last):, Capture GH Actions diagnostics / Backfill completed workflow runs	UNKNOWN STEP	2026-11-23T06:19:25.0322662Z ##[error]Process completed with exit code 1. |
| 137521769370 | Capture GH Actions diagnostics / Capture GH Actions diagnostics | logs/job-137521769370.log | 38208 | False | Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:19:21.8550385Z Traceback (most recent call last):, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:19:21.8698207Z ##[error]Process completed with exit code 1., Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:19:21.8759232Z ^[[36;1m    echo "::error::Could not rebase the diagnostic evidence onto gpt."^[[0m, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:19:21.8761788Z ^[[36;1m    echo "::error::Push failed while origin/gpt was unchanged."^[[0m, Capture GH Actions diagnostics / Capture GH Actions diagnostics	UNKNOWN STEP	2026-11-23T06:19:21.8763151Z ^[[36;1mecho "::error::Could not publish diagnostic evidence after five attempts."^[[0m |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.