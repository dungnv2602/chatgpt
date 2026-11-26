# Validate Document Standards — run 45291707545

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45291707545 / 1 |
| Run number | 230 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45291707545 |
| Branch | gpt |
| Commit | 9415eb62e6fcaecdf07632c4d491fe635bf75e55 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-23T23:46:41Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / failure |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-26T05:09:55Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | checkout_or_action_download |
| Jobs | 1 |
| Steps | 8 |
| Issues | 1 |
| Annotations | 2 |
| Artifacts | 0 |
| Capture errors | 0 |

## Failure classification

checkout_or_action_download

The report records an actionable workflow failure or operational exception. Ordinary successful runs and cancellation-only runs are not captured by default. A successful run is retained when a step failed but the workflow allowed it to continue. A cancelled run is retained only when it contains an independent actionable failure. Known downstream status-propagation steps after cancellation are excluded. Explicit run-backfill requests can override the default capture filter.

## Jobs and steps

| Job ID | Job | Status | Conclusion | Steps | Log |
| --- | --- | --- | --- | --- | --- |
| 138101820923 | validate-document-standards | completed | failure | 8 | logs/job-138101820923.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| checkout_or_action_download | 138101820923 | 5 | Validate the document type catalog | Blocking | medium | validate-document-standards	UNKNOWN STEP	2026-11-23T23:46:52.6152623Z ERROR: Line 106: Markdown coverage pattern matches no in-scope document: 'reports/lint_reports/latest-lint-report.md'. |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 138101820923 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 138101820923 | failure | .github | 16 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 138101820923 | validate-document-standards | logs/job-138101820923.log | 31419 | False | validate-document-standards	UNKNOWN STEP	2026-11-23T23:46:52.6152623Z ERROR: Line 106: Markdown coverage pattern matches no in-scope document: 'reports/lint_reports/latest-lint-report.md'., validate-document-standards	UNKNOWN STEP	2026-11-23T23:46:52.6154257Z ERROR: Line 108: Markdown coverage pattern matches no in-scope document: 'reports/lint_reports/on_*/latest-lint-report.md'., validate-document-standards	UNKNOWN STEP	2026-11-23T23:46:52.6157425Z ERROR: Line 109: Markdown coverage pattern matches no in-scope document: 'reports/lint_reports/on_*/history/**/*.md'., validate-document-standards	UNKNOWN STEP	2026-11-23T23:46:52.6158388Z Catalog validation failed: 3 error(s), 33 document type(s), 73 reference(s)., validate-document-standards	UNKNOWN STEP	2026-11-23T23:46:52.6228003Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.