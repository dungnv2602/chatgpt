# Validate Document Standards — run 45128076785

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45128076785 / 1 |
| Run number | 35 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45128076785 |
| Branch | gpt |
| Commit | 3cc93083c3e6a655038f9c5f22a970ac4ff9e731 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T07:00:57Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T07:06:16Z |

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
| 137537008771 | validate-document-standards | completed | failure | 8 | logs/job-137537008771.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 137537008771 | 5 | Validate the document type catalog | Blocking | medium | 2026-11-23T07:01:20.2791862Z ERROR: Line 46: Embedded contract must name its owner and live record. |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137537008771 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137537008771 | failure | .github | 17 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137537008771 | validate-document-standards | logs/job-137537008771.log | 30481 | False | validate-document-standards	Validate the document type catalog	2026-11-23T07:01:20.2791862Z ERROR: Line 46: Embedded contract must name its owner and live record., validate-document-standards	Validate the document type catalog	2026-11-23T07:01:20.2793214Z ERROR: Line 55: Generator-owned must reference its Python authority., validate-document-standards	Validate the document type catalog	2026-11-23T07:01:20.2794665Z ERROR: Line 55: Generator-owned must reference a regression test., validate-document-standards	Validate the document type catalog	2026-11-23T07:01:20.2795882Z ERROR: Line 56: referenced file does not exist: reports/lint_reports., validate-document-standards	Validate the document type catalog	2026-11-23T07:01:20.2797354Z Catalog validation failed: 4 error(s), 31 document type(s), 63 reference(s)., validate-document-standards	Validate the document type catalog	2026-11-23T07:01:20.2853905Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.