# Subtask: Create canonical task-board template

**Template version:** 1.5

## Metadata

- **ID:** 20261127-173100-01
- **Parent Task ID:** 20261127-173100
- **Type:** Implementation
- **Status:** Done
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User-authorized subtask under Template Fix.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** Eligible — Ready.
- **Required:** Yes
- **Created:** 2026-11-27 17:31 UTC
- **Updated:** 2026-11-27 17:31 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

> Create a task-board template.

## 2. Subsequent Instructions

None.

## 3. Objective and Scope

Create a reusable canonical template for task-board documents, including scheduler contract, current execution, ordered queue, and deferred/historical sections as applicable. Ensure the template governs board formatting and fields without becoming a second scheduler.

## 4. Acceptance Criteria

1. Read the current board and relevant governing templates/contracts before editing.
2. Create canonical task-board template and link it from the board workflow.
3. Ensure the template matches current board structure and scheduler/eligibility invariants.
4. Read back and commit changes.

## 5. Decisions and Progress

- **Action:** Created child record.
- **Result:** Implementation pending.
- **Next:** Read board contract and task templates before authoring.

## 6. State and Evidence

- **Commit SHA:** `cb768922209bb07fcd083d57b1212995fe1ca47b` (template); `8a9a9429181d214613cb541e45ecb0738a4c1ec8` (board link); `4435c51224e8cb471f990275bd35ae7b32a5193e` (navigation)
- **Changed paths:** `workspace/TASK_BOARD_TEMPLATE.md`; `workspace/task_board.md`; `workspace/README.md`.
- **Readback:** Confirmed template, board link, Workspace navigation, and subtask index on branch `gpt`.
- **Checks:** Not performed.
- **Limitations:** Structural template review only.

## 7. Completion

- **Status:** Done
- **Completed at:** 2026-11-27 UTC
- **Completion basis:** Template created, linked, and read back.

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Handoff

No remaining work for this subtask.

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
