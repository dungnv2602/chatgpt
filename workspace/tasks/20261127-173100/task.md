# Task: Template Fix

**Template version:** 2.6

## Metadata

- **ID:** 20261127-173100
- **Created:** 2026-11-27 17:31 UTC
- **Updated:** 2026-11-27 17:31 UTC
- **Priority:** P1
- **Status:** Ready
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit request to create Template Fix with two approved subtasks: create a task-board template; scan documents for missing templates and create any missing templates.
- **Governing ADR(s):** None
- **Current execution:** No
- **Dependencies:** None
- **Eligibility / deferral reason:** Eligible — Ready; approved, no dependencies.
- **Related tasks:** None

## 1. Original Request

> Create another task named "template fix", create Subtask to create a task board template, create another Subtask to scan repo if any document still haven't have its template, then create its template.

## 2. Subsequent Instructions

None.

## 3. Objective and Acceptance Criteria

Improve template coverage for task-board and repository document types.

1. Create a canonical task-board template and define its maintenance/usage contract.
2. Scan the repository systematically for documents that lack an applicable canonical template, schema, or embedded contract.
3. Before creating any identified missing template, read the applicable existing template/contract first and establish the gap and document owner/type.
4. Create missing templates only where the scan establishes a genuine gap; reconcile catalog, indexes, and coverage references.
5. Commit and read back all changes and results. No unobserved validation claimed.

## 4. Decisions

- Repository scan and template creation are assigned to a separate child from task-board-template creation.

## 5. Progress

### 2026-11-27 17:31 UTC

- **Action:** Created the Template Fix parent with two children for task-board template creation and document template coverage audit/remediation.
- **Result:** Child records established; implementation is not yet started.
- **References:** Parent and subtask index.
- **Next:** Execute children in Worker queue order.

## 6. Current State and Remaining Work

Both children are Ready. No template work or repository audit has yet been performed.

## 7. Verification and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** Task records and board
- **Readback:** Pending
- **Checks:** Not performed
- **Limitations:** Repository-wide template audit not performed.

## 8. Handoff

Execute children independently, template-first, with evidence.

## 9. Subtasks

Canonical index: [subtasks/README.md](subtasks/README.md).

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
