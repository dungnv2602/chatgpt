# Validate Document Standards — run 45176147166

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45176147166 / 1 |
| Run number | 123 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45176147166 |
| Branch | gpt |
| Commit | aa6ad05461b380a667c29c47cb389cdd3ff1c0cb |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T12:37:58Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-23T12:39:48Z |

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
| 137697780036 | validate-document-standards | completed | failure | 8 | logs/job-137697780036.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 137697780036 | 4 | Run catalog validator regression tests | Blocking | medium | 2026-11-23T12:38:09.3303275Z Traceback (most recent call last): |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 137697780036 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 137697780036 | failure | .github | 244 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 137697780036 | validate-document-standards | logs/job-137697780036.log | 63523 | False | validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3303275Z Traceback (most recent call last):, validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3315341Z     self.assertTrue(any("matches no in-scope document" in error for error in errors)), validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3321741Z Traceback (most recent call last):, validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3324724Z     self.assertTrue(any("unsafe or excluded Markdown coverage pattern" in error for error in errors)), validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3330753Z Traceback (most recent call last):, validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3333814Z     self.assertTrue(any("referenced file does not exist" in error for error in errors)), validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3340368Z Traceback (most recent call last):, validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3343469Z     self.assertTrue(any("duplicate document type" in error for error in errors)), validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3349994Z Traceback (most recent call last):, validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3353387Z     self.assertTrue(any("must name its owner and live record" in error for error in errors)), validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3359760Z Traceback (most recent call last):, validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3364119Z     self.assertTrue(any("must reference its Python authority" in error for error in errors)), validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3370564Z Traceback (most recent call last):, validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3373781Z     self.assertTrue(any("must reference a regression test" in error for error in errors)), validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3380107Z Traceback (most recent call last):, validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3393518Z Traceback (most recent call last):, validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3396551Z     self.assertTrue(any("expected 4 table cells" in error for error in errors)), validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3403540Z Traceback (most recent call last):, validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3418217Z Traceback (most recent call last):, validate-document-standards	Run catalog validator regression tests	2026-11-23T12:38:09.3421152Z     self.assertTrue(any("does not exist" in error for error in errors)) |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.