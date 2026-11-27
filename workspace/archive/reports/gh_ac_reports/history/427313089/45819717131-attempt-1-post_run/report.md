# Validate Document Standards — run 45819717131

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45819717131 / 1 |
| Run number | 619 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45819717131 |
| Branch | gpt |
| Commit | abcbe20e42e2790d6d3a84d2c55c058c8ace6222 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-26T12:26:50Z |
| Status at capture | completed |
| Observed conclusion | failure |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-26T12:42:52Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | failure |
| Primary category | validation_or_test |
| Jobs | 1 |
| Steps | 9 |
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
| 139908514957 | validate-document-standards | completed | failure | 9 | logs/job-139908514957.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 139908514957 | 6 | Validate the document type catalog | Blocking | medium | 2026-11-26T12:27:03.7778234Z ERROR: 3 Markdown file(s) are not covered by the catalog: archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md, archive/adr/0002-retire-source-drafts-after-verified-adr-promotion.md, archive/adr/README.md. |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 139908514957 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 139908514957 | failure | .github | 14 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 139908514957 | validate-document-standards | logs/job-139908514957.log | 46726 | False | validate-document-standards	Validate the document type catalog	2026-11-26T12:27:03.7778234Z ERROR: 3 Markdown file(s) are not covered by the catalog: archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md, archive/adr/0002-retire-source-drafts-after-verified-adr-promotion.md, archive/adr/README.md., validate-document-standards	Validate the document type catalog	2026-11-26T12:27:03.7779671Z Catalog validation failed: 1 error(s), 18 document type(s), 28 reference(s)., validate-document-standards	Validate the document type catalog	2026-11-26T12:27:03.7840434Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.