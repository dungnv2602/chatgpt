## Current Step

Inspect the changed-report generator, templates, anchor checker, workflow definitions, current evidence, and related regression tests before designing the repair.
## Open Discussions

- **2026-11-23 05:06 UTC — Changed-document lint-report failure:** Newest run [45115031724](https://github.com/dungnv2602/chatgpt/actions/runs/45115031724) fails because the anchor checker treats `{run_url}` in the report template as a local file. Report generation then fails because the workflow passes a literal `\\` argument. User has now authorized investigation and repair of the changed-report workflow and reporting system.
- **2026-11-23 05:06 UTC — Full-document lint result needs classification:** Newest run [45114176416](https://github.com/dungnv2602/chatgpt/actions/runs/45114176416) completed its full audit and published evidence, then failed its final gate because the audit reported lint findings. Confirm whether those findings are legitimate new violations or report/parser defects.
- **2026-11-23 — Document Standards workflow:** Path filters now include `skills/**`, `novels/templates/**`, the novel README/workflow, and the shared task template/README. The change has not yet received a verified hosted result. Do not wait or poll.
- **2026-11-23 — Session startup and lint-report investigation:** User invoked `start session` and authorized investigation and repair of the changed-document lint-report workflow, including report generation, report placement, detail level, workflow reliability, and regression coverage.

## Reports

### 2026-11-23 — Template placement audit completed

- Enumerated the full repository tree. The first scan contained 417 files and the final read-back contained 420 files (488 entries). Neither tree was truncated. Reviewed all named template/schema candidates, all skill reference files, and the two archived task records within the user's read-only audit scope.
- Relocated Prompt Master's copy-ready template library from `skills/prompt-master/references/templates.md` to `skills/prompt-master/assets/prompt-templates.md`.
- Relocated Drawing's pattern-entry templates from `skills/drawing/references/patterns/PATTERN-TEMPLATES.md` to `skills/drawing/assets/pattern-entry-templates.md`.
- Updated all identified active references and catalog entries. Read-back confirmed exact original content in both new assets. The old paths return 404. No named template or schema remains under a skill `references/` directory.
- Other candidates are correctly placed. Novel templates remain under `novels/templates/`. Workspace and skill templates remain in their canonical workspace or owner `assets/` locations. Reference patterns, examples, procedures, and embedded contracts remain in `references/`.
- Document Standards and The Worker now require the canonical format, catalog entry, and owner instructions to be committed and read back before the target document is created or materially edited. The gate applies in Default Mode and Condensed Mode.
- The catalog validator enforces skill-template placement and detects named templates under skill `references/`. Hosted run [45114001584](https://github.com/dungnv2602/chatgpt/actions/runs/45114001584) passed all 16 regression tests and catalog validation: 36 document types and 80 exact references.
- The Document Standards workflow path filters now cover all skill files and known project/workspace template locations. The workflow edit has been read back. Hosted confirmation remains unverified.
- Session Archiving now allows a user-authorized read-only full-repository audit without weakening archive immutability.
- Task archived at `archive/tasks/20261123043747-audit-template-placement-and-enforce-template-first-workflow.md`. Archive commit: `3ccf93348157870727c7fe9ea3d38f677e350977`. Retention-index commit: `3bab970ca474676bef3999847c24c60e04396e8f`. Active-record deletion commit: `f7d8ddc833e7e3d2cb56f7358f63d2fc1fd36a38`. Task-board reconciliation commit: `fc3a488137106951b0ffbb50af1342ff1f93222b`. Archive copy was read back exactly. The retention index contains the exact path and UTC timestamp. The active record is absent. The board has no active task and retains seven historical entries.

### 2026-11-23 — Lint-report evidence system implemented

- Added separate `on_repo` and `on_changed` report scopes with Markdown analysis, structured JSON evidence, indexes, latest pointers, and immutable per-run history.
- Added report-generation tooling and regression tests. Integrated report publication into both lint workflows. Migrated the legacy repository-wide report.
- Read-back checks confirmed the implementation on `gpt`. Hosted validation of the new reporting changes and execution of the changed-document report path remain unverified.
- No archived records were modified.
