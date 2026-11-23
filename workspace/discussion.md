# Current Step

- **2026-11-23 — Inspect candidate template assets and ownership.** The recursive Git tree returned 483 entries without truncation. Review every template/schema candidate outside immutable archive content, inspect its owning skill or project workflow, and classify whether it belongs in `assets/`, `references/`, `scripts/`, or a project-level templates directory. Also inspect likely template content whose filename does not contain “template”.

## Open Discussions

- **2026-11-23 — Session-start CI snapshot unverified:** The available GitHub connection did not expose workflow-run listings. No CI result is claimed. Recheck during the next mandatory preflight when run-list access is available.

## Reports

### 2026-11-23 — Lint-report evidence system implemented

- Added separate `on_repo` and `on_changed` report scopes with Markdown analysis, structured JSON evidence, indexes, latest pointers, and immutable per-run history.
- Added report-generation tooling and regression tests. Integrated report publication into both lint workflows. Migrated the legacy repository-wide report.
- Read-back checks confirmed the implementation on `gpt`. Hosted validation of the new reporting changes and execution of the changed-document report path remain unverified.
- No lint rules or baselines changed. No archive records were accessed or modified.

### 2026-11-23 — Archive-retention policy implemented

- Implemented weekly, indexed, 90-day per-record archive retention on `gpt`. Legacy unindexed records remain protected.
- Read-back checks confirmed the changed policy and implementation files. Hosted regression-test results remain unverified.
