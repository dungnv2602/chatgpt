# Validate Document Standards — run 45167456974

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45167456974 / 1 |
| Run number | 77 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45167456974 |
| Branch | gpt |
| Commit | 5d2eb9939aa4902d5e770593a425e61198a80024 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T11:41:33Z |
| Status at capture | in_progress |
| Observed conclusion | Not yet available |
| Projected conclusion | cancelled |
| Reporter job | in_progress / Pending |
| Capture stage | pre_finalizer |
| Completeness | Incomplete |
| Captured (UTC) | 2026-11-23T11:44:02Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | in_progress |
| Primary category | None |
| Jobs | 1 |
| Steps | 1 |
| Issues | 0 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 1 |

## Failure classification

No failure category identified. The parent run is still in progress. The projected conclusion is provisional.

The run conclusion records the workflow outcome. A cancelled run remains in history. Cancellation alone does not create an actionable issue. The generator also excludes known downstream status-propagation steps after cancellation.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137668362600 | validate-document-standards | completed | cancelled | 1 | logs/job-137668362600.log |

## Actionable step outcomes

No records were captured.

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137668362600 | failure | .github | 1 |  | Canceling since a higher priority waiting request for document-standards-refs/heads/gpt exists |
| 137668362600 | failure | .github | 31 |  | A task was canceled. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137668362600 | validate-document-standards | logs/job-137668362600.log | 82 | False |  |

## Evidence coverage

One or more evidence sources were unavailable. This report is Incomplete.

| Source | HTTP status | Limitation |
| --- | --- | --- |
| job_log | Not recorded | run 45167456974 is still in progress; logs will be available when it is complete  |

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.