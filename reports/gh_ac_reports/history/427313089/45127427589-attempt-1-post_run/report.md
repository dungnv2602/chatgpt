# Validate Document Standards — run 45127427589

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45127427589 / 1 |
| Run number | 25 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45127427589 |
| Branch | gpt |
| Commit | 501deb3a96171ddd3bf601f72a3f126abb2149c9 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T06:55:25Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T06:56:25Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | cancelled |
| Jobs | 1 |
| Steps | 7 |
| Issues | 1 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

cancelled

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137534890514 | validate-document-standards | completed | cancelled | 7 | logs/job-137534890514.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| cancelled | 137534890514 | 2 | Check out gpt | Blocking | high | validate-document-standards	Check out gpt	2026-11-23T06:55:30.7264270Z ##[error]The operation was canceled. |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137534890514 | failure | .github | 1 |  | Canceling since a higher priority waiting request for document-standards-refs/heads/gpt exists |
| 137534890514 | failure | .github | 70 |  | The operation was canceled. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137534890514 | validate-document-standards | logs/job-137534890514.log | 18464 | False | validate-document-standards	Check out gpt	2026-11-23T06:55:30.7264270Z ##[error]The operation was canceled. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.