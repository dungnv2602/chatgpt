# Task: Audit Document Templates and Enforce Inventory Coverage

## Metadata

- **Template version:** 1.1
- **ID:** 20261123-123459
- **Created:** 2026-11-23 12:34 UTC
- **Updated:** 2026-11-23 12:34 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** 20261123-230000? Existing template-first audit; 20261123-120700 Document Standards promotion
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

- The recursive tree audit found 4,287 in-scope files and 1,042 Markdown documents at baseline commit `15111d8be94e6518682001a8766f6c39b30e8bb1`.
- The 1,042 Markdown files are distributed as follows: drawings 97; images 2; novels 33; reports 853; skills 51; workspace 6.
- Initial review found canonical formats already exist for the recurring types. No additional standalone template is justified at this stage. Several legacy daily indexes and prompt logs predate current templates; preserve them. One-off Samantha visual/scenario direction notes remain exempt.
- The primary gap is enforcement: the catalog validator checks catalog rows and references but does not ensure that every in-scope Markdown document belongs to a classified family. Add a path-pattern coverage register and validator check.

## 6. Progress Log

### 2026-11-23 12:34 UTC

- **Action:** Retrieved the branch tree and enumerated all files outside `master/` and `archive/`; grouped Markdown documents by root and family.
- **Result:** 4,287 files and 1,042 Markdown documents found. No tree truncation. No missing recurring template identified in the first content review. Existing templates cover novel records, drawing attempts/session briefs/daily indexes, conversation/session records, task records, and report formats.
- **References:** `skills/document-standards/references/document-type-catalog.md`; `skills/document-standards/SKILL.md`; drawing, novel, report, and workspace owner files.
- **Next:** Finish classifying historical and generated document families, add machine-enforced Markdown path coverage, and strengthen the authoring gate.

## 7. Current State

The audit is in progress. No project files have been changed by this task yet. The existing canonical templates appear sufficient; the gap is that the validator does not enforce repository-wide document-family coverage.

## 8. Remaining Work

- Complete classification of every in-scope Markdown path.
- Add the coverage register and validator enforcement with regression tests.
- Tighten Document Standards authoring procedure and catalog maintenance.
- Expand hosted workflow triggers to relevant document roots.
- Read back all changes and verify branch head.
- Hosted validation will remain unverified until a naturally triggered GitHub Actions run reports results.

## 9. Next Actions

1. Add the Markdown inventory coverage register to the Document Type Catalog.
2. Extend the catalog validator and regression tests to reject uncovered in-scope Markdown files.
3. Tighten the authoring workflow and hosted validation path filters.
4. Read back every changed file and reconcile task board/discussion state.

## 10. References

- `skills/document-standards/SKILL.md`
- `skills/document-standards/references/document-type-catalog.md`
- `skills/document-standards/scripts/validate_catalog.py`
- `skills/document-standards/scripts/test_validate_catalog.py`
- `.github/workflows/validate-document-standards.yml`
- `workspace/task_board.md`
- Baseline commit: `15111d8be94e6518682001a8766f6c39b30e8bb1`

## 11. Verification

- **Check:** Recursive Git tree enumeration and Markdown extension count.
- **Method:** GitHub tree API with recursive traversal; filtered out paths beginning `master/` and `archive/`.
- **Result:** Complete, non-truncated tree; 4,287 in-scope files and 1,042 Markdown documents.
- **Limitations:** The content classification is a targeted review of document families and representative records, not a semantic line-by-line review of all generated report instances. Machine-enforced path coverage will close the future inventory gap.

## 12. Handoff Instructions

Continue on branch `gpt`. Do not access `master/` or `archive/`. Build an explicit path-pattern register for all current in-scope Markdown families, then make the catalog validator fail on any uncovered Markdown file. Keep generated reports, historical legacy records, technical references, and one-off creative notes classified without forcing redundant templates. Use hosted Actions for tests and validation; do not run repository scripts locally.
