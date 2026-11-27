# Subtask: Reconcile task board scheduling and task templates with ready CI remediation children

**Template version:** 1.4

## Metadata

- **ID:** 20261126-142500-21
- **Parent Task ID:** 20261126-142500
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit request dated 2026-11-27 to fix the task board and update its templates.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** In Progress
- **Required:** Yes
- **Created:** 2026-11-27 10:00 UTC
- **Updated:** 2026-11-27 10:00 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

> If you see this 
>
> workspace/tasks/20261126-142500/subtasks 
>
> Then clearly a bunch of P0 CI for you. 
>
> Fix task board, update its templates.

## 2. Subsequent Instructions

None.

## 3. Objective and Scope

Repair the Worker task board and task templates so Ready CI remediation children are visible and schedulable, priority/status metadata and board queue format are consistent, and blocked/dependency-waiting work is not represented as eligible. This is a follow-up under the genuine parent task.

## 4. Acceptance Criteria

1. Reconcile the board against active task/subtask records and list eligible tasks in scheduler order.
2. Keep blocked work out of the eligible queue and show its reason.
3. Update templates to prevent queue omissions and clarify priority, eligibility, approval, and deferral fields.
4. Read back all changed files; do not inspect hosted CI.

## 5. Decisions and Progress

- 2026-11-27: Board review showed many Ready CI P0 children under the active parent but an empty board queue. The existing child index is not itself a scheduler output. This remediation corrects the Worker board and template contract.

## 6. State and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** Not yet
- **Readback:** Initial review complete
- **Checks:** Not performed
- **Limitations:** Hosted CI results not reviewed.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Handoff

Reconcile the active board, templates, and parent child index. Commit and read back the changes. Do not inspect hosted CI results.

## 9. Ledger Findings

None.
