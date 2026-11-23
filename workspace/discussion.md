# Current Step

- **2026-11-23 — Expand Document Standards CI path coverage.** The user requested template-standard enforcement against future drift. The validator now checks skill-owned template placement and catalog references, but its workflow does not run for most skill-template changes. Update only `.github/workflows/validate-document-standards.yml` to trigger on all skill files and the known project/workspace template locations. Preserve its test and validation steps. Do not change any other workflow.

## Open Discussions

- **2026-11-23 — CI repair boundary:** The latest changed-document lint run fails in the report-tooling test and in a report-generation shell command with a literal trailing backslash. The stale test assertion was corrected. The shell defect is in `.github/workflows/ste-lint-changed.yml` and is outside this workflow change.
- **2026-11-23 — Full-document STE lint:** The latest full-document run fails in the same stale report-generator test assertion. The assertion was corrected. Hosted confirmation remains pending.

## Reports

### 2026-11-23 — Template placement findings and hosted validation

- Enumerated 417 repository files (483 tree entries), without truncation. Identified two misplaced copy-ready templates in skill `references/` directories.
- Created exact copies under the owning skills' `assets/` directories, updated all known references and catalog entries, then deleted the superseded paths. Read-back confirmed exact source/target content equality before deletion.
- Strengthened the catalog validator to enforce skill-template placement and detect named templates under skill `references/`. Hosted run [45114001584](https://github.com/dungnv2602/chatgpt/actions/runs/45114001584) passed all 16 regression tests and catalog validation: 36 document types and 80 exact references.
- Updated Document Standards and The Worker to require canonical format creation, catalog registration, commit, and read-back before editing the governed document.

### 2026-11-23 — Lint-report evidence system implemented

- Added separate `on_repo` and `on_changed` report scopes with Markdown analysis, structured JSON evidence, indexes, latest pointers, and immutable per-run history.
- Added report-generation tooling and regression tests. Integrated report publication into both lint workflows. Migrated the legacy repository-wide report.
- Read-back checks confirmed the implementation on `gpt`. Hosted validation of the new reporting changes and execution of the changed-document report path remain unverified.
- No lint rules or baselines changed. No archive records were accessed or modified.
