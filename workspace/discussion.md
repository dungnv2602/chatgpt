## Current Step

Unify the Drawing generation/edit decision and remove stale Session Archiving references; then consolidate authoring rules and update affected READMEs.

## Open Discussions





- **2026-11-23 12:42 UTC — Document Standards hosted validation pending:** The 48-rule Markdown coverage register, segment-aware validator, regression tests, and generated-report trigger exclusions are committed on `gpt`. Review the hosted result only when it becomes naturally available. Do not poll or dispatch workflows.

- **2026-11-23 10:16 UTC — Hosted retention validation:** The cleanup script and tests cover exact individual files in both archive folders. A hosted run of the schedule-only cleanup has not yet been observed. It runs on the schedule from main. No manual dispatch or user action is needed. Do not modify main.

- **2026-11-23 10:08 UTC — Pending diagnostic post-run captures:** Five source runs remain pending in the diagnostics index. A later eligible natural sweep can capture them. Do not poll or dispatch workflows.

- **2026-11-23 12:21 UTC — Hosted validation pending:** The approved capture-filter and Worker–ledger handoff changes are committed on `gpt`. Reporter and ledger regression tests must run on a naturally triggered GitHub-hosted diagnostics run. Do not poll or dispatch workflows.

## Reports

- **2026-11-23 12:42 UTC — Full Markdown template audit and coverage enforcement implemented:** Audited 4,351 in-scope files and 1,058 Markdown documents, excluding `master/` and `archive/`. No missing recurring template was found. Added 48 narrow coverage rules, segment-aware glob validation and regression tests, clarified legacy record classifications and structured-record authority, and excluded generated report output from workflow triggers. All 1,058 paths are covered; no stale rules. All changed paths were read back at commit [be736d5d](https://github.com/dungnv2602/chatgpt/commit/be736d5dd885c8084133542afc72458d50ccbf63). Hosted validation remains pending.

- **2026-11-23 12:28 UTC — CI report filtering and Worker–ledger handoff implemented:** Routine successes and cancellation-only outcomes are skipped by default; non-blocking failed steps and independent failures from cancelled runs remain actionable. Added workflow-level timeout findings, ledger `task_refs`, and the Worker procedure for grouping findings into linked tasks. Existing historical reports remain unchanged. All 14 changed paths passed read-back verification in commit [4f31211d](https://github.com/dungnv2602/chatgpt/commit/4f31211d9da8ed9c6a2d7e8536e5633f8b364a73). Hosted regression validation is pending.

- **2026-11-23 12:09 UTC — Document Standards promoted to foundational:** Added `skills/document-standards/SKILL.md` to the explicit foundational loading sequence and dependency hierarchy. Updated `skills/INITIALIZATION_POLICY.md`, `skills/README.md`, The Worker, and Document Standards metadata. Document Standards remains independent; its catalog and specific canonical assets load only when needed. The archived Session Archiving task record was left unchanged. Task record [20261123-120700](../archive/tasks/20261123-120700-promote-document-standards-to-foundational.md) was archived at commit [fe38c1a9](https://github.com/dungnv2602/chatgpt/commit/fe38c1a977b3d0d992e11f6998865c7b1853def4). No local scripts, tests, or CI were run.


