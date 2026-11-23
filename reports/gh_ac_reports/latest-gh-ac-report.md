# Validate Document Standards — run 45182961508

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45182961508 / 1 |
| Run number | 144 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45182961508 |
| Branch | gpt |
| Commit | 56c893dae7d7be52b2533e5b14fd7b79c2d6d718 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T13:20:32Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T13:21:44Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
| Primary category | validation_or_test |
| Jobs | 1 |
| Steps | 8 |
| Issues | 1 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

validation_or_test

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137721188374 | validate-document-standards | completed | failure | 8 | logs/job-137721188374.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 137721188374 | 4 | Run catalog validator regression tests | Blocking | medium | 2026-11-23T13:20:44.8355587Z Traceback (most recent call last): |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137721188374 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137721188374 | failure | .github | 59 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137721188374 | validate-document-standards | logs/job-137721188374.log | 32183 | False | validate-document-standards	Run catalog validator regression tests	2026-11-23T13:20:44.8355587Z Traceback (most recent call last):, validate-document-standards	Run catalog validator regression tests	2026-11-23T13:20:44.8375996Z FAILED (failures=1), validate-document-standards	Run catalog validator regression tests	2026-11-23T13:20:44.8478872Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.