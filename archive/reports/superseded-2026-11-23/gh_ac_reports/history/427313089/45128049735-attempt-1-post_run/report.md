# Validate Document Standards — run 45128049735

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45128049735 / 1 |
| Run number | 31 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45128049735 |
| Branch | gpt |
| Commit | 6d140a6d4ffc397b2728a3dbc0bcd82483bf664f |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T07:00:45Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T07:06:02Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | cancelled |
| Jobs | 1 |
| Steps | 1 |
| Issues | 1 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

cancelled

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137536852740 | validate-document-standards | completed | cancelled | 1 | logs/job-137536852740.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| cancelled | 137536852740 | 1 | Set up job | Blocking | high | validate-document-standards	Set up job	2026-11-23T07:00:49.2293261Z ##[error]The operation was canceled. |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137536852740 | failure | .github | 1 |  | Canceling since a higher priority waiting request for document-standards-refs/heads/gpt exists |
| 137536852740 | failure | .github | 31 |  | The operation was canceled. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137536852740 | validate-document-standards | logs/job-137536852740.log | 2987 | False | validate-document-standards	Set up job	2026-11-23T07:00:49.2293261Z ##[error]The operation was canceled. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.