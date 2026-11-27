# Subtask: Audit universal prompt-to-task workflow rules

**Template version:** 1.3

## Metadata

- **ID:** 20261126-142500-01
- **Parent Task ID:** 20261126-142500
- **Type:** Analysis
- **Status:** Done
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User request dated 2026-11-27 to check whether the workflow reflects the prompt-to-task/subtask rule.
- **Governing ADR(s):** Not required — read-only workflow audit
- **Dependencies:** None
- **Eligibility / deferral reason:** Complete
- **Required:** Yes
- **Created:** 2026-11-27 09:22 UTC
- **Updated:** 2026-11-27 09:22 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

> This relate to the rule, every of my prompt you must create a task for it. If my prompt is the follow-up of an already existed task, then you should create a subtasks for it. So, none of my request for lost.
>
> Check if workflow already reflect this.

## 2. Objective

Audit the current Worker, task templates, workspace documentation, task board, CI Ledger policy, and task-generation implementation against the universal prompt-capture and follow-up hierarchy.

## 3. Scope

Read-only audit of the authoritative workflow and relevant Ledger handoff. No repository changes were included in this audit child.

## 4. Acceptance Criteria

1. Identify whether every substantive user prompt must be captured as a task or subtask.
2. Verify follow-up parentage requirements.
3. Verify CI remediation parentage against the genuine originating task.
4. Report concrete gaps and the required correction.

## 5. Result

The workflow was only partially aligned. Existing task templates preserved parent prompts and supported linked subtasks, but The Worker had no explicit universal prompt-capture gate. Workspace README used ambiguous “update an existing task” language instead of requiring a distinct follow-up subtask. The CI Ledger still generated work-target parents per affected file or workflow, contrary to the genuine originating-task hierarchy. The board and Ledger publication contracts also used different layouts.

## 6. Verification

- **Check:** Current authoritative files on branch gpt.
- **Method:** Remote readback of The Worker, CI Ledger, task/subtask templates, workspace README, and task board.
- **Result:** Gaps identified as recorded above.
- **Limitations:** Static documentation/code inspection only. No scripts, tests, or hosted CI results were run or inspected.

## 7. Completion Record

- **Status:** Done
- **Completed at:** 2026-11-27
- **Completion basis:** All four audit acceptance criteria were answered with specific repository evidence.
- **Evidence:** This audit record and the current conversation report.

## 8. Handoff

Implementation and workflow repair are tracked separately in subtask [20261126-142500-02](20261126-142500-02.md).
