# Validate Document Standards — run 45127450021

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45127450021 / 1 |
| Run number | 28 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45127450021 |
| Branch | gpt |
| Commit | c88346e0663152db270680e43e751011bd356fe6 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T06:55:36Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T06:57:01Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | validation_or_test |
| Jobs | 1 |
| Steps | 8 |
| Issues | 1 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

validation_or_test

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137535041953 | validate-document-standards | completed | failure | 8 | logs/job-137535041953.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 137535041953 | 5 | Validate the document type catalog | Blocking | medium | 2026-11-23T06:56:02.2443663Z ERROR: Line 46: referenced file does not exist: lint_reports/README.md. |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137535041953 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137535041953 | failure | .github | 19 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137535041953 | validate-document-standards | logs/job-137535041953.log | 30854 | False | validate-document-standards	Validate the document type catalog	2026-11-23T06:56:02.2443663Z ERROR: Line 46: referenced file does not exist: lint_reports/README.md., validate-document-standards	Validate the document type catalog	2026-11-23T06:56:02.2444616Z ERROR: Line 46: unsafe or out-of-scope path 'gh_ac_reports/README.md'., validate-document-standards	Validate the document type catalog	2026-11-23T06:56:02.2445685Z ERROR: Line 54: unsafe or out-of-scope path 'gh_ac_reports/scripts/report.py'., validate-document-standards	Validate the document type catalog	2026-11-23T06:56:02.2446628Z ERROR: Line 54: unsafe or out-of-scope path 'gh_ac_reports/assets/report-template.md'., validate-document-standards	Validate the document type catalog	2026-11-23T06:56:02.2447579Z ERROR: Line 54: unsafe or out-of-scope path 'gh_ac_reports/assets/report-schema.json'., validate-document-standards	Validate the document type catalog	2026-11-23T06:56:02.2448592Z ERROR: Line 54: unsafe or out-of-scope path 'gh_ac_reports/scripts/test_report.py'., validate-document-standards	Validate the document type catalog	2026-11-23T06:56:02.2449476Z Catalog validation failed: 6 error(s), 29 document type(s), 59 reference(s)., validate-document-standards	Validate the document type catalog	2026-11-23T06:56:02.2495447Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.