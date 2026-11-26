## Current Step

Audit active README and skill cross-references, navigation links, and Document Type Catalog path assumptions against the reconstructed tree. Retrieve exact targets before considering edits. Task: [20261126-021200](tasks/20261126-021200-complete-reconstructed-repository-consistency-audit.md).

## Open Discussions

- **2026-11-25 — DRAFT-0003 — Area, Project, and Task Architecture:** [Review DRAFT-0003 revision 1](draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md). The proposal recommends project folders with nested task folders, one global task board, task-local findings, project-level coordination, global Draft/ADR governance, and exact-file task archives. User review is required for the Area/Project/Task boundaries, task file split, selectors, resource promotion, and project closeout.
- **2026-11-25 — DRAFT-0002 approval-state reconciliation:** The register records approval of Option 3 with added requirements, but revision 3 and its index still show in-review, and the task/board remain Blocked. Reconcile the exact approved scope before ADR promotion.
- **2026-11-23 — Drawing direction needed:** Session DRAWING-2026-11-23-01 is Active, but the user has not supplied a subject or visual direction.

## Reports

- **2026-11-26 — Image-pipeline path-index repair:** Corrected drawing manifest paths in processor reports and repaired publication-verifier path parsing for `area/drawing/YYYY-MM-DD/images/`. Added regression assertions. Read-back and commit-path checks completed. Tests and hosted Actions remain unrun. Commits: [processor](https://github.com/dungnv2602/chatgpt/commit/1fcfc601864e5ee784c261578f433d535b19a6c5), [verifier](https://github.com/dungnv2602/chatgpt/commit/6845bde3134028a96f64502535048f4e4bec4dff), [test](https://github.com/dungnv2602/chatgpt/commit/52ae30426904d72c0ac7fb5f7d4ea4caa8bc7e5b). [Task record](tasks/20261126-021200-complete-reconstructed-repository-consistency-audit.md).

- **2026-11-26 — Catalog and initialization navigation repair:** Remapped catalog references to `area/novel/`, `area/drawing/`, `.takeout/reports/`, and `.archive/`; corrected session-start and skill index links. Read-back was performed. Hosted validation and catalog checks remain unrun.

- **2026-11-26 — Archive-retention reconstruction repair:** Remapped 55 indexed archive paths to `.archive/task/` and `.archive/reports/`; repaired script, tests, guides, and session-start path references. All 55 indexed paths matched the remote tree. Tests/hosted validation not run.
