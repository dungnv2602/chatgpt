# Current Step

- **2026-11-23 — Record and implement the approved workflow correction.** Create the task record from `workspace/TASK_TEMPLATE.md`. Update The Worker, Conversation Mode, Session Archiving, and workspace guidance so the discussion register and task workflow apply in every mode. Correct the lint-report catalog classifications. Do not add standalone templates that duplicate generated formats. Add an external template only when its generator consumes it.

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
