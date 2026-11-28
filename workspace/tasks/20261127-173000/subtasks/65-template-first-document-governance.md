# Subtask: Template-first document governance

**Template version:** 1.6

## Metadata

- **ID:** 20261127-173000-65
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User's explicit request in this conversation to create these two subtasks under Refactor Skills.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** In Progress — authorized execution batch active for the prepared batch
- **Required:** Yes
- **Created:** 2026-11-28 15:00 UTC
- **Updated:** 2026-11-28 15:00 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

Whenever you modify a document, consult its template first. Assess whether you should update the template to reflect the latest document/repo state. Only then modify the document accordingly to the (updated) template. Check if your workflow already reflects this, reinforce your workflow.

## 2. Subsequent Instructions

- **2026-11-28:** Task captured under the persistent Refactor Skills parent. The user explicitly selected Refactor Skills as current task and issued `Execute`, authorizing the prepared P0 batch.

## 3. Objective and Scope

Audit the Worker workflow for template-first document governance. Strengthen it so every document modification first consults the canonical template, evaluates template drift and whether the template should be updated, and then edits the target using the updated template. Assess existing enforcement and close gaps without creating duplicate policy.

## 4. Acceptance Criteria

1. Identify the canonical document/template mapping and the existing template-first rule and enforcement gaps.\n2. Reinforce the canonical workflow owner with a mandatory template consultation and template-state assessment gate before each document edit.\n3. Define when a template update is warranted and when target-only changes are appropriate.\n4. Reconcile relevant template/catalog/index pointers without duplicating operational rules.\n5. Commit and remote-readback all changes and report evidence and limitations.

## 5. Decisions and Progress

- **Decision:** Preserve the request and its scope as this child. Execution authorized for this batch by the user's explicit `Execute` cue.
- **Progress:** Execution started. Existing Worker gate already requires reading the catalog and applicable template/contract before edits, but does not explicitly require assessing template freshness against latest repo/document state before editing.

## 6. State and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** Task record, parent subtask index, task board, parent task tracking
- **Readback:** Pending commit
- **Checks:** Not performed
- **Limitations:** This record captures scope only; implementation and repository audit remain pending.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Execution self-check

- Canonical template consulted: `.agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md`.
- Parentage confirmed: Refactor Skills.
- Scope and acceptance criteria recorded.
- Execution authorization cue: pending.

## 10. Handoff

Execution is authorized. Audit the template-first gate, strengthen the freshness assessment, reconcile related contracts and records, and close out with readback.

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
