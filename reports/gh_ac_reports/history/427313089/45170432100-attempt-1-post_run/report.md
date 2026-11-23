# Validate Document Standards — run 45170432100

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45170432100 / 1 |
| Run number | 95 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45170432100 |
| Branch | gpt |
| Commit | 947ab9f2f8fc0d120eaf22f3d39d9b5906e52933 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T12:01:40Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / cancelled |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T12:06:06Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | None |
| Jobs | 1 |
| Steps | 7 |
| Issues | 0 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

No failure category identified.

The run conclusion records the workflow outcome. A cancelled run remains in history. Cancellation alone does not create an actionable issue. The generator also excludes known downstream status-propagation steps after cancellation.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137678225361 | validate-document-standards | completed | cancelled | 7 | logs/job-137678225361.log |

## Actionable step outcomes

No records were captured.

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137678225361 | failure | .github | 1 |  | Canceling since a higher priority waiting request for document-standards-refs/heads/gpt exists |
| 137678225361 | failure | .github | 19 |  | The operation was canceled. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137678225361 | validate-document-standards | logs/job-137678225361.log | 15554 | False | validate-document-standards	Check out gpt	2026-11-23T12:01:44.7408708Z ##[error]The operation was canceled. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.