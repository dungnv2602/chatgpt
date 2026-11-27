# Subtask: Consolidate Document Standards into The Worker

**Template version:** 1.5

## Metadata

- **ID:** 20261127-173000-01
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** Done
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Existing approval retained from original task 20261127-102301 and explicit reparenting instruction.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** Eligible — Ready; approved, no dependencies. Parent Refactor Skills is the selected P0 execution.
- **Required:** Yes
- **Created:** 2026-11-27 17:30 UTC
- **Updated:** 2026-11-27 18:30 UTC
- **Ledger group:** None
- **Legacy Task IDs:** 20261127-102301

## 1. Original Prompt

> Approve
>
> Consolidate document skill into the Worker

## 2. Subsequent Instructions

- Before modifying a document, read its applicable template first.
- Parentage corrected from CI task to independent document-governance objective; subsequently placed under Refactor Skills.

## 3. Objective and Scope

Consolidate document-format governance and template-first execution guidance into The Worker. Remove redundant standalone activation while retaining supporting catalog, coverage, schema, validator and owner responsibilities. Preserve partial progress and the nested implementation child.

## 4. Acceptance Criteria

1. Worker mandates template-first document editing.
2. Document-format classes, migration, catalog/coverage, schema/generator ownership and validation limits are retained.
3. Standalone activation and maintenance are removed or redirected.
4. References, catalog and coverage rules are reconciled.
5. Changes committed and read back.

## 5. Decisions and Progress

- **Action:** Relocated the catalog and validator infrastructure into The Worker and removed the separate skill activation/index entry.
- **Result:** The standalone skill will be deleted; Worker owns the format governance and supporting assets directly.
- **Next:** Reconcile exact file references, delete the standalone skill directory contents, read back and close this child.

## 6. State and Evidence

- **Commit SHA:** `c7b7678f8e5fc19db75be0aced703c461aac66e6` (deletion commit; consolidation series includes subsequent relocation and reconciliation commits)
- **Changed paths:** `.agent/skills/the-worker/references/document-type-catalog.md`; `.agent/skills/the-worker/scripts/validate_document_catalog.py`; `.agent/skills/the-worker/scripts/test_validate_document_catalog.py`; `.agent/skills/the-worker/SKILL.md`; `.agent/skills/README.md`; removed `.agent/skills/document-standards/` assets.
- **Readback:** All relocated files and updated Worker/index were retrieved from branch `gpt`. Standalone skill and assets were deleted.
- **Checks:** Tests and validator not executed; prohibited local execution was not used.
- **Limitations:** No local validation or hosted CI inspection. Readback verifies committed content, not test behavior.

## 7. Completion

- **Status:** Done
- **Completed at:** 2026-11-27 18:30 UTC
- **Completion basis:** Consolidation, deletion, references/index reconciliation, and branch readback.

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Handoff

Complete remaining consolidation and reconciliation as the first execution step under the P0 parent. Preserve partial work.

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
