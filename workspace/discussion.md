# Current Step

- **2026-11-23 — Classify report document types and define canonical formats.** Inspect the relevant catalog entries, report generator contracts, and both lint-scope outputs. Decide whether each report needs a standalone template, schema, or generator-owned classification. Identify the canonical storage path and required catalog/workflow updates.

## Open Discussions

- **2026-11-23 — Session-start CI snapshot unverified:** The available GitHub connection did not expose workflow-run listings. The combined status query for the last known discussion-recorded commit returned no statuses. No CI result is claimed. Recheck during the next mandatory preflight when run-list access is available.

## Reports

### 2026-11-23 — Lint-report evidence system implemented

- Added separate `on_repo` and `on_changed` report scopes with Markdown analysis, structured JSON evidence, indexes, latest pointers, and immutable per-run history.
- Added report-generation tooling and regression tests. Integrated report publication into both lint workflows. Migrated the legacy repository-wide report.
- Read-back checks confirmed the implementation on `gpt`. Hosted validation of the new reporting changes and execution of the changed-document report path remain unverified.
- No lint rules or baselines changed. No archive records were accessed or modified.

### 2026-11-23 — Archive-retention policy implemented

- Implemented weekly, indexed, 90-day per-record archive retention on `gpt`. Legacy unindexed records remain protected.
- Read-back checks confirmed the changed policy and implementation files. Hosted regression-test results remain unverified.
