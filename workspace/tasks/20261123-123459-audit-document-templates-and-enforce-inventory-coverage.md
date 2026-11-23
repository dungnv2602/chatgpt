# Task: Audit Document Templates and Enforce Inventory Coverage

## Metadata

- **Template version:** 1.1
- **ID:** 20261123-123459
- **Created:** 2026-11-23 12:34 UTC
- **Updated:** 2026-11-23 14:25 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** 20261123043747 template-first audit; 20261123-120700 Document Standards promotion
- **Archived:** No

## 1. Original Request

> Scan repo except /master, /archive to check there are still documents that you forgot to create templates for them. Then create them, and put them into appropriate places. I do not expect this to happens again, so tighten your workflow if needed.

## 2. Subsequent Instructions

- **2026-11-23 12:34 UTC:** User approved the preceding CI-report filtering and Worker–ledger handoff proposal. This task is a separate direct request to audit document coverage and improve the template-authoring gate.
- **2026-11-23 19:58 ICT:** User expanded the task: “Read all skills again except prompt-master & philosophy-religion-asceticism. Assess if the workflow cycle is closed. Identify the gaps, look for possible deadlocks, fix them, then refactor by trimming down redundant wordings, trimming down unnecessarily excessive parts, minimize content without losing full context, then tighten, and optimize the workflow. Then scan the repo except where you shouldn't scan (/master, /archive, etc.) to update the README files to correctly reflect the updated workflow.”

## 3. Objective

Audit all in-scope repository documents on branch `gpt`, excluding `master/` and `archive/`. Identify recurring document types without a canonical template, schema, embedded contract, or generator-owned format. Create any genuinely missing canonical assets in their owning locations. Strengthen Document Standards so future document creation cannot silently introduce an unclassified type. Extend the audit to the complete task, CI-report, remediation, drawing, and document-authoring lifecycles. Resolve conflicting instructions and deadlocks, reduce duplicated operational rules, and align in-scope README files.

## 4. Requirements

1. Use the repository tree on branch `gpt` as the inventory source.
2. Exclude `master/` and `archive/` entirely; do not read or modify their contents.
3. Review all in-scope Markdown documents and classify each family as template-required, schema-required, embedded-contract, generator-owned, lightweight-pattern, or exempt.
4. Do not create redundant templates for generated outputs, external formats, legacy records, or one-off creative prose.
5. Create missing templates or schemas in their owning canonical directories, update the Document Type Catalog, and update owner instructions/indexes.
6. Add machine-enforced inventory coverage so an in-scope Markdown document cannot be added without matching a documented document-family rule.
7. Require the authoring workflow to check the catalog and inventory coverage before creation, and validate the new document after creation.
8. Expand the Document Standards workflow path filters so document-family changes trigger hosted validation.
9. Preserve historical and approved documents; do not mass-migrate them merely to match current templates.
10. Read every in-scope skill definition except `prompt-master` and `philosophy-religion-asceticism`; read relevant supporting references and owner workflows.
11. Trace the task, CI reporting, ledger, Worker handoff, validation, resolution, archive, drawing, and document-authoring cycles. Identify deadlocks and contradictory authorities.
12. Keep one authoritative owner for each workflow contract. Remove duplicated instructions only after preserving required decisions, triggers, exceptions, safety, provenance, and verification rules.
13. Reconcile prompt-based fresh generation and source-image editing into one operation decision. Correct stale references to deleted skills and paths.
14. Scan in-scope README files, excluding `master/`, `archive/`, and the two skills excluded by the user. Update only inaccurate or incomplete workflow guidance. Preserve historical daily indexes.
15. Read back every changed path and inspect the resulting branch head. Do not run repository scripts or tests locally.

## 5. Decisions

- The recursive tree audit found 4,291 in-scope files and 1,044 Markdown documents at baseline commit `63a82060d21ce8266aaaafac2795fcee9d411ae9`.
- The 1,044 Markdown files are distributed as follows: drawings 97; images 2; novels 33; reports 854; skills 51; workspace 7.
- Initial review found canonical formats already exist for the recurring types. No additional standalone template is justified at this stage. Several legacy daily indexes and prompt logs predate current templates; preserve them. One-off Samantha visual/scenario direction notes remain exempt.
- The primary gap was enforcement: the catalog validator did not ensure that every in-scope Markdown document belonged to a classified family. The path-pattern coverage register and validator check now address that gap.
- The expanded workflow review found conflicting image-operation rules: Drawing's core skill required prompt-only reconstruction for every adjustment, while series guidance and the novelist skill permitted genuine source-image edits. The Worker reference also described prompt-first as the default but allowed direct edits in exceptions. Consolidate this into a single intent/source-availability decision.
- Several drawing references still named the deleted `session-archiving` skill or its former script path. Conversation Mode still assigned archive ownership to that deleted skill.
- The Worker repeats the full Document Standards authoring gate. Document Standards itself repeats the inventory check across multiple procedures. Keep the full contract in Document Standards and make The Worker enforce it by reference.
- The workflow cycles are otherwise connected: Actions evidence → reports → deduplicated ledger → Worker-owned linked tasks → hosted validation evidence → ledger resolution. Routine successful Actions reports are filtered; a validation run URL is sufficient resolution evidence. Explicit successful-run backfill remains an optional evidence request.

## 6. Progress Log

### 2026-11-23 13:58 UTC

- **Action:** Recovered the approved task on branch `gpt`, read all seven in-scope skill definitions, and compared the current recursive tree with the catalog's Markdown path patterns.
- **Result:** The non-truncated tree at `ef69eb76fc485e55e2617ef70293be5f78e3852a` contains 6,311 entries and 1,108 in-scope Markdown files. All 1,108 match the 48 catalog rules. Every rule matches at least one file. The scan excluded `master/` and `archive/`. A bootstrap deadlock remains: the validator rejects a zero-match coverage rule, while the authoring gate requires the new family rule to be committed before its first document is created.
- **References:** `skills/SESSION_START.md`; `skills/the-worker/SKILL.md`; `skills/the-worker/references/conversation-mode.md`; the six other in-scope `SKILL.md` definitions; `skills/document-standards/references/document-type-catalog.md`; `skills/document-standards/scripts/validate_catalog.py`; `workspace/task_board.md`.
- **Next:** Review in-scope README and lifecycle references. Design a reserved-family state that allows template-first commits while preserving stale active-rule detection. Then complete link/read-back and hosted-validation checks without polling or dispatching Actions.

### 2026-11-23 13:19 UTC

- **Action:** Completed the workflow and README refactor. Unified Drawing's operation selector and delegated image-operation choice from The Worker to Drawing. Removed the duplicate Worker authoring gate and made Document Standards the sole template/inventory authority. Rewrote the shared image-delivery guide as Drawing-specific rules, refreshed Workspace, CI diagnostics, ledger, and Novel README guidance, and clarified that old initialization change-log entries are historical.
- **Result:** Commits `948f21c514687504f8ba69866bd8a14d111fd711`, `d440b0c4cac714e63d2ddf0d52fcb2d2e159ab76`, `0af276a4573c27aca943326f0fd2f4577ab2c375`, `40f202aec209bb5f69956d1aaeb14244f5e065fe`, `77215ed647279aa8467eb8ccc97af46abd553350`, `cacdab7fc1a130a0cc646b0f53e54c67c038c936`, `a0e8e30e64e866fba384395598b6be8e2065c502`, `23bd49ae4f01f9d95ac7281280e232079b99d450`, `1fc800febaa3a3d7c678f06c4b4567dd46777814`, `3d6c4fe8794c60a1573dfdbe0856cfbafd94ed9f`, and `80f213c600d70b55e60f999edaf942da0f77ab5a` contain the refactor, owner delegation, README, and inventory changes. The latest checked recursive tree before the catalog refresh was non-truncated: 4,509 in-scope files and 1,096 Markdown documents; all 1,096 matched the 48 path rules, with no unused rule.
- **Additional finding:** Hosted validation run [45180357440](https://github.com/dungnv2602/chatgpt/actions/runs/45180357440) failed two catalog-validator regression tests because their temporary catalogs did not cover Markdown files created by those tests. The validator behaved correctly. The test fixture now accepts test-specific coverage rows; the project-template and report-root tests declare their own narrow patterns. This correction is in commit `91df44b9e599457e2b8b3a635788857b41ae5e6c`. No validator rule was weakened. A later pre-finalizer report [45181736988](https://github.com/dungnv2602/chatgpt/actions/runs/45181736988) also captured the regression failure before that fixture correction; its job logs were unavailable while the run was still in progress. Do not poll it.
- **References:** `skills/drawing/`; `skills/the-worker/`; `skills/document-standards/`; `workspace/README.md`; `reports/gh_ac_reports/README.md`; `reports/triage/README.md`; `novels/README.md`; `skills/INITIALIZATION_POLICY.md`.
- **Next:** Read back every changed path and verify the current recursive inventory and link targets. Keep the task In Progress until a natural hosted run validates the corrected fixtures and current catalog.


### 2026-11-23 12:58 UTC

- **Action:** Expanded the approved task to cover the end-to-end workflow audit, conflict resolution, documentation compression, and README alignment. Re-read the in-scope skill definitions and the relevant Worker, Drawing, Document Standards, CI-report, and novel workflow references. Reviewed the recursive tree and the in-scope README inventory without opening `master/` or `archive/`.
- **Result:** The earlier Markdown inventory remains covered by 48 path rules. No additional recurring template is indicated. The main workflow defects are conflicting image edit rules, stale Session Archiving paths, duplicated authoring-gate instructions, and README wording that no longer matches session-scoped Drawing mode. The task and discussion register now reflect the expanded scope.
- **References:** `skills/the-worker/SKILL.md`; `skills/document-standards/SKILL.md`; `skills/drawing/SKILL.md`; `skills/drawing/references/`; `skills/the-worker/references/`; `skills/romantic-storyteller-visual-artist/`; `reports/gh_ac_reports/README.md`; `reports/triage/README.md`; `.github/workflows/validate-document-standards.yml`.
- **Next:** Consolidate drawing operation selection and document-authoring authority. Then update the affected READMEs and validate all changed paths by read-back.

### 2026-11-23 12:34 UTC

- **Action:** Retrieved the branch tree and enumerated all files outside `master/` and `archive/`; grouped Markdown documents by root and family.
- **Result:** Initial scan found 4,287 files and 1,042 Markdown documents. No tree truncation. No missing recurring template was identified. Existing templates cover novel records, drawing attempts/session briefs/daily indexes, conversation/session records, task records, and report formats.
- **References:** `skills/document-standards/references/document-type-catalog.md`; `skills/document-standards/SKILL.md`; drawing, novel, report, and workspace owner files.
- **Next:** Reconcile the inventory against the latest branch tree and enforce coverage.

### 2026-11-23 12:37 UTC

- **Action:** Rechecked the latest branch tree after concurrent hosted report-publication commits and classified all Markdown families. Drafted a 42-rule path-coverage register and added validator enforcement, regression tests, authoring-gate rules, and workflow path filters.
- **Result:** The latest read-back before this refinement found 4,326 in-scope files and 1,052 Markdown documents. All 1,052 matched the 42-rule register. No new standalone template is required. Static read-back corrected the test fixture newlines and changed path matching so `*` cannot cross `/` while `**` can span directories. The report path filter was also found to include generated Markdown output, which could retrigger validation; negative exclusions are being added.
- **References:** Catalog coverage register; `scripts/validate_catalog.py`; `scripts/test_validate_catalog.py`; `.github/workflows/validate-document-standards.yml`; The Worker Markdown document gate.
- **Next:** Correct the test fixture newlines and enforce segment-aware glob matching before final verification.

### 2026-11-23 12:43 UTC

- **Action:** Rechecked the branch after further generated diagnostic-report publication and widened the hosted validation trigger to cover all workflow-definition changes.
- **Result:** Latest read-back at `be736d5dd885c8084133542afc72458d50ccbf63` contains 4,351 in-scope files and 1,058 Markdown documents. All 1,058 paths match the 48-rule register; every rule matches at least one current document. No uncovered or stale rules. The workflow now excludes generated reports from its path triggers and runs when any workflow definition changes. Hosted validation remains uninspected.
- **References:** `.github/workflows/validate-document-standards.yml`; Document Type Catalog; commit `be736d5dd885c8084133542afc72458d50ccbf63`.
- **Next:** Leave hosted validation pending; do not poll or dispatch workflows.

### 2026-11-23 14:15 UTC

- **Action:** Implemented a five-column Markdown coverage register with explicit `Active` and `Reserved` states. Updated the validator, four regression cases, catalog version, and Document Standards authoring gate in one atomic commit.
- **Result:** Active rules must match at least one current Markdown file. Reserved rules must match none. The first document activates its rule in the same commit as that document. The validator still rejects stale Active rules, unknown states, uncovered files, unsafe paths, duplicate patterns, and invalid canonical authorities. Commit: `852beb643a188c3edfe1e0e9c94d6c6623664fd9`.
- **Inventory:** Non-truncated tree at `e40e15438ab263e83082ca5bc8d1fdb9194fb741` contains 6,350 tree entries and 1,110 in-scope Markdown documents. All 1,110 match the 48 Active rules. Every rule matches at least one current path. `master/` and `archive/` remain excluded.
- **Workflow review:** Reviewed all 17 eligible README files and all in-scope skill definitions. Worker task creation remains the sole task-creation owner; the ledger only records `task_refs`. Generated report paths are excluded from their own push triggers. Diagnostics self-monitoring remains an explicit GitHub UI limitation. The image-operation selector agrees with the Novel workflow.
- **Next:** Remove duplicated image-lifecycle instructions without changing ownership or technical requirements. Then read back every changed path and review a naturally completed hosted validation. Do not run local scripts or tests, poll, or dispatch Actions.

### 2026-11-23 14:25 UTC

- **Action:** Consolidated duplicated image-intake, provenance, conversion, and manifest wording. Reduced `images/README.md` from 101 to 34 lines and the Worker image-provenance reference from 145 to 54 lines. Removed repeated acceptance-criteria and session-summary instructions from the Worker archive reference. Corrected the Novel asset-tree example to place original PNG/JPEG masters under `original/` and WebP delivery files in the destination root.
- **Ownership:** The Worker owns the shared image lifecycle; `images/takeout/README.md` owns the exact hand-off schema, conversion profiles, staging, retry, and report procedure; the Drawing archive reference owns session manifest and attempt-link requirements; Novel documentation describes only the novel destination and its record relationship.
- **Validation:** Read back all four changed lifecycle/README files. Checked internal Markdown links against the current non-truncated tree; no unresolved links. Latest tree at `1a5c8380036dac0132216635951f95a971ceee25` contains 6,375 entries and 1,114 in-scope Markdown files. All 1,114 are covered by the 48 Active rules; every rule matches at least one current file. No Reserved rules remain in the current catalog.
- **Commit:** `25fc8f291061476663f460e8428b57c9a9723e38`.
- **Next:** Verify the final branch head and all changed paths again. Review naturally completed hosted validation only; do not poll or dispatch Actions.

## 7. Current State

Template inventory enforcement, the Reserved/Active bootstrap fix, and the image-lifecycle refactor are implemented. The latest non-truncated tree audit at `1a5c8380036dac0132216635951f95a971ceee25` found 1,114 in-scope Markdown files. All 1,114 match the 48 Active rules, and every rule matches at least one file. All 17 eligible README files and all in-scope skill definitions have been reviewed. The task, ledger, and GitHub Actions ownership cycles have no unresolved circular dependency. Hosted validation after the Reserved/Active validator change remains pending.

## 8. Remaining Work

- Verify the final branch head and read back all paths changed by this task.
- Review a naturally completed Document Standards run after the Active/Reserved validator change. Do not poll or dispatch workflows.
- If hosted validation passes and the final inventory/read-back remains consistent, complete the task closeout and archive it through The Worker's required transaction.

## 9. Next Actions

1. Read back all changed Document Standards, image, novel, Worker, task, and workspace paths from `gpt`.
2. Recheck the latest non-truncated Markdown inventory and the 48 Active coverage rules.
3. Review a naturally completed hosted Document Standards result; do not poll or dispatch.
4. If every check passes, reconcile the task board, archive the task record, and verify the final closeout transaction.

## 10. References

- `skills/document-standards/SKILL.md`
- `skills/document-standards/references/document-type-catalog.md`
- `skills/document-standards/scripts/validate_catalog.py`
- `skills/document-standards/scripts/test_validate_catalog.py`
- `.github/workflows/validate-document-standards.yml`
- `workspace/task_board.md`
- Baseline commit: `63a82060d21ce8266aaaafac2795fcee9d411ae9`

## 11. Verification

- **Check:** Recursive tree inventory, Markdown path coverage, README alignment, changed-file read-back, and hosted regression evidence.
- **Method:** GitHub recursive tree API on branch `gpt`; 48 catalog patterns evaluated with segment-aware glob semantics; exact repository files read back.
- **Result:** Initial inventory audit: 4,509 in-scope files and 1,096 Markdown documents at commit `9ef2567e99a52045ac636c8a7749ecb5ccbb1e31`. Intermediate audit: 6,350 tree entries and 1,110 in-scope Markdown documents at commit `e40e15438ab263e83082ca5bc8d1fdb9194fb741`. Latest audit: 6,375 tree entries and 1,114 in-scope Markdown documents at commit `1a5c8380036dac0132216635951f95a971ceee25`. All 1,114 current Markdown paths match the 48 Active rules; every rule matches at least one current file; zero uncovered paths and zero unused rules. The Active/Reserved validator, tests, and authoring gate were committed at `852beb643a188c3edfe1e0e9c94d6c6623664fd9`.
- **Limitations:** The repository validator and test suite were not run locally. The latest stored pre-finalizer run predates the fixture correction and had unavailable logs. Hosted validation after the fix is not yet verified. The content review classified all Markdown families and representative records; structured JSON/YAML/CSV records remain governed by their catalogued schemas and generators.

## 12. Handoff Instructions

Continue on branch `gpt`. Do not access `master/` or `archive/`. No new template is required unless a genuinely new recurring type appears. The 48-rule catalog uses Active/Reserved coverage: register a new family as Reserved with its canonical format, then activate it in the same commit as the first record. The latest 1,114-file Markdown inventory is fully covered. Image lifecycle instructions now have distinct Worker, Takeout README, Drawing archive, and Novel destination owners. Read back the final branch state and review the next naturally completed hosted validation. Do not run local scripts or poll/dispatch Actions.
