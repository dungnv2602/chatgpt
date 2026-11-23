# Current Step

- **2026-11-23 — Final consistency review and task verification.** The Document Standards workflow now triggers for all skill files and the known project/workspace template locations. Review The Worker for duplicate wording, verify every relocated asset link and catalog row, inspect the exact remaining CI workflow defect without changing it, then read back all changed paths and the branch head.

## Open Discussions

- **2026-11-23 — Changed-document lint workflow defect:** Run [45113875454](https://github.com/dungnv2602/chatgpt/actions/runs/45113875454) failed in report tooling. Its test failure was a stale assertion for `resolved_findings`, now corrected. The report-generation command also receives a literal backslash from `.github/workflows/ste-lint-changed.yml`. That workflow was not modified.
- **2026-11-23 — Hosted lint confirmation:** The full-document lint run [45111202565](https://github.com/dungnv2602/chatgpt/actions/runs/45111202565) failed on the same stale assertion. The test was corrected. Do not claim hosted confirmation until a later result is observed.
- **2026-11-23 — Document Standards workflow:** Path filters now include `skills/**`, `novels/templates/**`, the novel README/workflow, and the shared task template/README. The workflow-file change itself will trigger validation. Do not wait or poll.

## Reports

### 2026-11-23 — Template placement findings and hosted validation

- Enumerated 417 repository files (483 tree entries), without truncation. Reviewed all named template/schema candidates, all skill reference files, and the two archived task records within the requested read-only audit scope.
- Identified two misplaced copy-ready templates in skill `references/` directories. Created exact copies under the owning skills' `assets/` directories, updated active references and catalog entries, then deleted the superseded paths. Read-back confirmed exact source/target content equality before deletion.
- Other template candidates are correctly placed. Novel templates belong in `novels/templates/`. Shared task and skill templates belong in the relevant workspace or skill `assets/` directory. Reference patterns, examples, procedures, and embedded contracts remain in `references/`.
- Strengthened the catalog validator to enforce skill-template placement and detect named templates under skill `references/`. Hosted run [45114001584](https://github.com/dungnv2602/chatgpt/actions/runs/45114001584) passed all 16 regression tests and catalog validation: 36 document types and 80 exact references.
- Updated Document Standards and The Worker to require canonical format creation, catalog registration, commit, and read-back before editing the governed document. Updated Session Archiving to permit explicit read-only whole-repository audits without weakening archive immutability.
- Expanded the Document Standards workflow's path filters. Hosted validation of that workflow-file change is not yet verified.

### 2026-11-23 — Lint-report evidence system implemented

- Added separate `on_repo` and `on_changed` report scopes with Markdown analysis, structured JSON evidence, indexes, latest pointers, and immutable per-run history.
- Added report-generation tooling and regression tests. Integrated report publication into both lint workflows. Migrated the legacy repository-wide report.
- Read-back checks confirmed the implementation on `gpt`. Hosted validation of the new reporting changes and execution of the changed-document report path remain unverified.
- No lint rules or baselines changed. No archive records were modified.
