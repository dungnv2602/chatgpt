# Validate Document Standards — run 45566012929

## Run identity

| Field | Value |
| --- | --- |
| Workflow | Validate Document Standards |
| Workflow path | .github/workflows/validate-document-standards.yml |
| Run / attempt | 45566012929 / 1 |
| Run number | 381 |
| Run URL | https://github.com/dungnv2602/chatgpt/actions/runs/45566012929 |
| Branch | gpt |
| Commit | 65a5ee5021c9659535d1c9c8eff733b41432ec50 |
| Event | push |
| Actor | dungnv2602 |
| Created (UTC) | 2026-11-25T07:10:03Z |
| Status at capture | completed |
| Observed conclusion | cancelled |
| Projected conclusion | Not calculated |
| Reporter job | completed / success |
| Capture stage | post_run |
| Completeness | Complete |
| Captured (UTC) | 2026-11-25T07:11:23Z |

## Executive summary

| Measure | Result |
| --- | --- |
| State | cancelled |
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
| 139040870241 | validate-document-standards | completed | failure | 9 | logs/job-139040870241.log |

## Actionable step outcomes

| Category | Job | Step | Name | Effect | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| validation_or_test | 139040870241 | 6 | Validate the document type catalog | Blocking | medium | 2026-11-25T07:10:14.9582639Z ERROR: Misplaced skill template under references/: skills/migrate-to-rust/references/infographic_template.html. Move copy-ready assets to the owning skill's assets/ directory. |

## Check annotations

| Job | Level | Path | Line | Title | Message |
| --- | --- | --- | --- | --- | --- |
| 139040870241 | warning | .github | 2 |  | Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ |
| 139040870241 | failure | .github | 15 |  | Process completed with exit code 1. |

## Artifacts

No records were captured.

## Captured job logs

| Job | Name | File | Bytes | Truncated | Markers |
| --- | --- | --- | --- | --- | --- |
| 139040870241 | validate-document-standards | logs/job-139040870241.log | 45952 | False | validate-document-standards	Validate the document type catalog	2026-11-25T07:10:14.9582639Z ERROR: Misplaced skill template under references/: skills/migrate-to-rust/references/infographic_template.html. Move copy-ready assets to the owning skill's assets/ directory., validate-document-standards	Validate the document type catalog	2026-11-25T07:10:14.9588608Z ERROR: 15 Markdown file(s) are not covered by the catalog: skills/pdf/FORMS.md, skills/pdf/REFERENCE.md, skills/skill-creator/agents/analyzer.md, skills/skill-creator/agents/comparator.md, skills/skill-creator/agents/grader.md, skills/theme-factory/themes/arctic-frost.md, skills/theme-factory/themes/botanical-garden.md, skills/theme-factory/themes/desert-rose.md, skills/theme-factory/themes/forest-canopy., validate-document-standards	Validate the document type catalog	2026-11-25T07:10:14.9594633Z Catalog validation failed: 2 error(s), 18 document type(s), 28 reference(s)., validate-document-standards	Validate the document type catalog	2026-11-25T07:10:14.9656343Z ##[error]Process completed with exit code 1. |

## Evidence coverage

All requested evidence endpoints and completed-job log captures returned data.

## Related lint evidence

No separate lint report applies to this workflow.

## Integrity

The immutable run directory contains report.md, report.json, integrity.json, and captured job logs. The integrity manifest contains SHA-256 hashes for every file in this capture.