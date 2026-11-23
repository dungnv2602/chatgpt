# Current Step

- **2026-11-23 — Relocate the two misplaced template assets.** Create exact copies of Prompt Master's reusable prompt-template library and Drawing's copy-ready pattern-entry templates under their owning skills' `assets/` directories. Read back and compare the full content before updating references or removing the old paths. Then correct the catalog classifications.

## Open Discussions

- **2026-11-23 — Session-start CI snapshot unverified:** The available GitHub connection did not expose workflow-run listings. No CI result is claimed. Recheck during the next mandatory preflight when run-list access is available.
- **2026-11-23 — Document Standards Actions path filters:** The existing validation workflow does not trigger for most skill-owned template or Worker changes. A workflow-path change may be needed after the validator is strengthened. Do not edit `.github/workflows/*` without separate explicit authorization.

## Reports

### 2026-11-23 — Lint-report evidence system implemented

- Added separate `on_repo` and `on_changed` report scopes with Markdown analysis, structured JSON evidence, indexes, latest pointers, and immutable per-run history.
- Added report-generation tooling and regression tests. Integrated report publication into both lint workflows. Migrated the legacy repository-wide report.
- Read-back checks confirmed the implementation on `gpt`. Hosted validation of the new reporting changes and execution of the changed-document report path remain unverified.
- No lint rules or baselines changed. No archive records were accessed or modified.

### 2026-11-23 — Archive-retention policy implemented

- Implemented weekly, indexed, 90-day per-record archive retention on `gpt`. Legacy unindexed records remain protected.
- Read-back checks confirmed the changed policy and implementation files. Hosted regression-test results remain unverified.
