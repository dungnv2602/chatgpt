# Validate Document Standards — run 45128450035

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45128450035 / 1 |
| Run number | 36 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45128450035 |
| Branch | gpt |
| Commit | d24bd314e5342201325e789fc1b66647ef90a9bf |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T07:04:15Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / cancelled |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T07:06:42Z |

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
| 137538136537 | validate-document-standards | completed | failure | 8 | logs/job-137538136537.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 137538136537 | 5 | Validate the document type catalog | Blocking | medium | 2026-11-23T07:04:27.7203281Z ERROR: Line 46: Embedded contract must name its owner and live record. |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137538136537 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137538136537 | failure | .github | 17 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137538136537 | validate-document-standards | logs/job-137538136537.log | 30481 | False | validate-document-standards	Validate the document type catalog	2026-11-23T07:04:27.7203281Z ERROR: Line 46: Embedded contract must name its owner and live record., validate-document-standards	Validate the document type catalog	2026-11-23T07:04:27.7204108Z ERROR: Line 55: Generator-owned must reference its Python authority., validate-document-standards	Validate the document type catalog	2026-11-23T07:04:27.7204943Z ERROR: Line 55: Generator-owned must reference a regression test., validate-document-standards	Validate the document type catalog	2026-11-23T07:04:27.7205745Z ERROR: Line 56: referenced file does not exist: reports/lint_reports., validate-document-standards	Validate the document type catalog	2026-11-23T07:04:27.7206857Z Catalog validation failed: 4 error(s), 31 document type(s), 63 reference(s)., validate-document-standards	Validate the document type catalog	2026-11-23T07:04:27.7249132Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.