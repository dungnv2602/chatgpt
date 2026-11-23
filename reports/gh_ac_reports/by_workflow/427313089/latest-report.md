# Validate Document Standards — run 45182710700

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45182710700 / 1 |
| Run number | 143 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45182710700 |
| Branch | gpt |
| Commit | 80f213c600d70b55e60f999edaf942da0f77ab5a |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T13:19:01Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T13:20:52Z |

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

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 137720353607 | validate-document-standards | completed | failure | 8 | logs/job-137720353607.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 137720353607 | 4 | Run catalog validator regression tests | Blocking | medium | 2026-11-23T13:19:15.8853275Z Traceback (most recent call last): |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137720353607 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137720353607 | failure | .github | 59 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137720353607 | validate-document-standards | logs/job-137720353607.log | 32190 | False | validate-document-standards	Run catalog validator regression tests	2026-11-23T13:19:15.8853275Z Traceback (most recent call last):, validate-document-standards	Run catalog validator regression tests	2026-11-23T13:19:15.8870759Z FAILED (failures=1), validate-document-standards	Run catalog validator regression tests	2026-11-23T13:19:15.8965422Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.