# Task: Audit Document Templates and Enforce Inventory Coverage

## Metadata

- **Template version:** 1.1
- **ID:** 20261123-123459
- **Created:** 2026-11-23 12:34 UTC
- **Updated:** 2026-11-23 12:58 UTC
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

## 7. Current State

Template inventory enforcement is implemented. The latest prior verified inventory found 1,058 Markdown documents covered by 48 rules. The expanded workflow refactor is in progress. No additional recurring template has been identified. The task remains In Progress until conflicting instructions are reconciled, affected READMEs are updated, all changed paths pass read-back, and hosted validation is naturally available.

## 8. Remaining Work

- Reconcile the image-edit versus fresh-generation decision across Drawing, Worker, and Novelist guidance.
- Remove stale `session-archiving` paths and script references.
- Make Document Standards the single authority for the full template/inventory authoring gate; remove duplicated Worker steps.
- Reduce redundant operational text in the affected skills and references without removing any required constraints.
- Update affected README files and verify every link/path.
- Hosted regression execution remains unverified until a naturally triggered GitHub Actions run reports results. Do not poll or dispatch workflows.

## 9. Next Actions

1. Implement the single Drawing operation decision and remove obsolete Session Archiving references.
2. Consolidate the Document Standards gate and reduce duplicated Worker instructions.
3. Update Drawing, report-triage, workspace, and other affected README files.
4. Read back all changed paths and check the `gpt` branch head.
5. Do not run local scripts or tests. Do not poll or dispatch Actions; review the next natural hosted validation result.

## 10. References

- `skills/document-standards/SKILL.md`
- `skills/document-standards/references/document-type-catalog.md`
- `skills/document-standards/scripts/validate_catalog.py`
- `skills/document-standards/scripts/test_validate_catalog.py`
- `.github/workflows/validate-document-standards.yml`
- `workspace/task_board.md`
- Baseline commit: `63a82060d21ce8266aaaafac2795fcee9d411ae9`

## 11. Verification

- **Check:** Recursive tree inventory, Markdown path coverage, changed-file read-back, and workflow trigger exclusions.
- **Method:** GitHub recursive tree API on branch `gpt`; 48 catalog path patterns evaluated with segment-aware glob semantics; all changed files retrieved again from the branch.
- **Result:** Non-truncated tree at commit `be736d5dd885c8084133542afc72458d50ccbf63`; 4,351 in-scope files and 1,058 Markdown documents. All 1,058 Markdown paths are covered; all 48 rules match at least one current document; zero uncovered paths and zero stale rules. All nine relevant repository paths were read back.
- **Limitations:** Hosted regression tests and the validator were not executed or inspected. The workflow is configured to run on relevant changes; leave this task In Progress until a natural hosted result is available. The content review classified all Markdown families and representative records; machine-readable JSON/YAML/CSV records remain governed by their catalogued schemas and generators.

## 12. Handoff Instructions

Continue on branch `gpt`. Do not access `master/` or `archive/`. Template inventory coverage is committed at `be736d5dd885c8084133542afc72458d50ccbf63`, with a later branch head at the start of this expanded review. Continue on `gpt`. Do not access `master/` or `archive/`. No extra template is required unless the audit identifies a genuinely new recurring type. Do not run local validation or poll/dispatch Actions.
