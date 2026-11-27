# Subtask: Enforce template-first document editing

**Template version:** 1.5

## Metadata

- **ID:** 20261127-173000-04
- **Parent Task ID:** 20261127-173000
- **Type:** Governance
- **Status:** Ready
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit user instruction on 2026-11-27 to require reading a document's template before modifying it, and to raise a proposed template to the user when none exists.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** Eligible — Ready, dependencies and authorization satisfied
- **Required:** Yes
- **Created:** 2026-11-27 11:26 UTC
- **Updated:** 2026-11-27 11:26 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

This child directly advances the persistent Refactor Skills parent's objective by consolidating document-authoring governance into The Worker rather than introducing a separate specialist skill.

## 1. Original Prompt

> Before you modify a document, you must read its template first. If its template doesn't exist, suggest one, raise it to me.
>
> Check if there's a task for this. If not, create a subtask in "refactor skills"

## 2. Subsequent Instructions

None.

## 3. Objective and Scope

Make template-first document editing a durable Worker-owned rule.

Scope:
- Identify the applicable canonical template before modifying any repository document.
- Read the complete applicable template before editing the target document.
- If no applicable template exists, do not modify the target document. Propose a suitable template, explain its intended structure and use, and raise it to the user for approval.
- After approval, create the template before editing documents that depend on it.
- Distinguish documents that are governed by a template from files whose format is intrinsically defined by another contract (for example source code, generated artifacts, schemas, or machine-readable data); do not invent templates where they are inappropriate.
- Apply the rule to Worker workflows and relevant repository instructions without creating a separate skill.

## 4. Acceptance Criteria

1. The Worker explicitly requires locating and reading the applicable template before every document modification.
2. The Worker explicitly prohibits modifying a document when its required template is missing; it must propose the template and raise it to the user first.
3. The rule defines how to handle documents with no applicable template and distinguishes them from non-document artifacts governed by other contracts.
4. Relevant references, indexes, and instructions are reconciled; no standalone specialist skill is introduced.
5. All changed documents were edited only after their applicable templates were read.
6. Changed files are read back from branch `gpt`; validation limitations are recorded accurately.

## 5. Decisions and Progress

### 2026-11-27 11:26 UTC

- **Action:** Searched the active repository for an existing task covering the template-first rule. No matching task was found. Read `workspace/TASK_TEMPLATE.md`, `workspace/SUBTASK_TEMPLATE.md`, and `workspace/TASK_BOARD_TEMPLATE.md` before creating this child and preparing any task-governance changes.
- **Result:** Created this approved P1 child under the persistent Refactor Skills parent. Existing task templates are present; no new task template is needed for this work.
- **References:** Parent `20261127-173000`; canonical templates in `workspace/`.
- **Next:** Update The Worker and relevant governance references to enforce this rule, always reading their templates before edits.

## 6. State and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** `workspace/tasks/20261127-173000/subtasks/04-enforce-template-first-document-editing.md`
- **Readback:** Pending
- **Checks:** Not performed
- **Limitations:** Task creation records the requirement; it does not yet enforce it in Worker behavior.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Hosted Validation

Not applicable.

## 9. Handoff

Select this child after the current approved specialist-skill consolidation as the next Worker governance change. Before modifying The Worker or any other document, read its applicable template. If no applicable template exists, stop and raise a proposed template to the user before proceeding.

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
