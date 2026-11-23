# Task: Audit Document Templates and Enforce Inventory Coverage

## Metadata

- **Template version:** 1.1
- **ID:** 20261123-123459
- **Created:** 2026-11-23 12:34 UTC
- **Updated:** 2026-11-23 12:42 UTC
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

## 3. Objective

Audit all in-scope repository documents on branch `gpt`, excluding `master/` and `archive/`. Identify recurring document types without a canonical template, schema, embedded contract, or generator-owned format. Create any genuinely missing canonical assets in their owning locations. Strengthen Document Standards so future document creation cannot silently introduce an unclassified type.

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
10. Read back every changed path and inspect the resulting branch head. Do not run repository scripts or tests locally.

## 5. Decisions

- The recursive tree audit found 4,291 in-scope files and 1,044 Markdown documents at baseline commit `63a82060d21ce8266aaaafac2795fcee9d411ae9`.
- The 1,044 Markdown files are distributed as follows: drawings 97; images 2; novels 33; reports 854; skills 51; workspace 7.
- Initial review found canonical formats already exist for the recurring types. No additional standalone template is justified at this stage. Several legacy daily indexes and prompt logs predate current templates; preserve them. One-off Samantha visual/scenario direction notes remain exempt.
- The primary gap is enforcement: the catalog validator checks catalog rows and references but does not ensure that every in-scope Markdown document belongs to a classified family. Add a path-pattern coverage register and validator check.

## 6. Progress Log

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

## 7. Current State

Implementation and repository read-back are complete. The audit found no missing recurring template. Existing canonical templates are sufficient. The 48-rule Markdown coverage register classifies all 1,052 in-scope Markdown documents. The validator uses segment-aware glob semantics, and workflow path filters exclude generated report output to prevent recursive runs. The task remains In Progress only because hosted regression execution has not been inspected.

## 8. Remaining Work

- Hosted regression execution remains unverified until a naturally triggered GitHub Actions run reports results. Do not poll or dispatch workflows.

## 9. Next Actions

1. Do not poll or dispatch workflows.
2. When a natural hosted result is available in later work, review the Document Standards regression tests and catalog validator.
3. If hosted validation fails, create a remediation task from the diagnostic evidence.

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
- **Result:** Non-truncated tree at commit `36c091fd601c08bde911a5ffa225b22c2f6cce9d`; 4,337 in-scope files and 1,055 Markdown documents. All 1,055 Markdown paths are covered; all 48 rules match at least one current document; zero uncovered paths and zero stale rules. All nine relevant repository paths were read back.
- **Limitations:** Hosted regression tests and the validator were not executed or inspected. The workflow is configured to run on relevant changes; leave this task In Progress until a natural hosted result is available. The content review classified all Markdown families and representative records; machine-readable JSON/YAML/CSV records remain governed by their catalogued schemas and generators.

## 12. Handoff Instructions

Continue on branch `gpt`. Do not access `master/` or `archive/`. Implementation is committed and read back at `36c091fd601c08bde911a5ffa225b22c2f6cce9d`. The 48-rule register covers all 1,055 Markdown files in the latest verified tree. No new standalone template was required. Do not poll or dispatch workflows; review the naturally triggered hosted validation when available. If it fails, use the diagnostic evidence to create a remediation task.
