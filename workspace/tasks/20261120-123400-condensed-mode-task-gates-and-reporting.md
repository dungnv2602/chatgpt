# Task: Add task-inspection gates and discussion reports to Condensed Mode

## Metadata

- **ID:** 20261120-123400
- **Created:** 2026-11-20 12:34 UTC
- **Updated:** 2026-11-20 12:34 UTC
- **Priority:** P1
- **Status:** Ready
- **Origin:** User
- **Approval:** Approved
- **Current execution:** No
- **Dependencies:** None
- **Related tasks:** None
- **Archived:** No

## 1. Original Request

> Modify the condensed mode, when you successfully created a task, give me the link here to inspect before continue doing the work. When you done, be it successful or failed, you put your report in discussion.md, then give me the link here. This is what minimized actually is.

## 2. Subsequent Instructions

No subsequent clarifications recorded.

## 3. Objective

Update Condensed Mode so task creation and task reporting follow explicit user-inspection checkpoints and use `workspace/discussion.md` as the final report location.

## 4. Requirements

- After successfully creating a task, stop execution and provide a direct link to the task record so the user can inspect it before implementation continues.
- Do not continue task execution until the user gives a clear instruction to proceed.
- If task creation fails, do not claim success or provide an invented task link.
- When the requested work reaches an outcome, whether successful, partial, or failed, write a concise factual report to `workspace/discussion.md`.
- The report must include the outcome, task link when available, changed paths, commit link when one exists, verification result, and any blocker or next action.
- After writing the report, fetch it from branch `gpt` to verify it, then provide the user a direct link to `workspace/discussion.md`.
- Do not claim completion before the report is committed and verified.
- Preserve the distinction between the temporary discussion register and task records. Do not turn `discussion.md` into a full conversation transcript.
- Keep Condensed Mode responses minimal. The required task and report links are the primary user-facing output.

## 5. Decisions

- Task creation is an explicit inspection gate. Creating the task does not authorize immediate implementation.
- The final report is written to the existing discussion register, even when the work fails or cannot proceed.
- The user must explicitly authorize continuation after inspecting the task record.

## 6. Progress Log

### 2026-11-20 12:34 UTC

- **Action:** Inspected the Condensed Mode skill, Worker task rules, task board, task template, and current discussion register.
- **Result:** Existing Condensed Mode instructions require minimal reports but do not require a user inspection pause after task creation or a final report in `workspace/discussion.md`.
- **References:** `skills/conversation-mode/SKILL.md`, `skills/the-worker/SKILL.md`, `workspace/TASK_TEMPLATE.md`, `workspace/task_board.md`, `workspace/discussion.md`.
- **Next:** Present this task record for user inspection. Do not edit the Condensed Mode skill until the user authorizes continuation.

## 7. Current State

Task record created. Implementation has not started. The current Condensed Mode skill remains unchanged.

## 8. Remaining Work

- Obtain user instruction to continue after task inspection.
- Update `skills/conversation-mode/SKILL.md` with the task-creation gate and final discussion-report requirement.
- Ensure the task board and discussion-register rules remain consistent.
- Read back all changed paths and verify the final report.
- Commit the changes to branch `gpt`.

## 9. Next Actions

1. Wait for the user to inspect this task record.
2. Continue only after the user explicitly authorizes it.
3. Implement and verify the Condensed Mode changes.
4. Write the outcome report to `workspace/discussion.md` and provide its link.

## 10. References

- `skills/conversation-mode/SKILL.md`
- `skills/the-worker/SKILL.md`
- `workspace/discussion.md`
- `workspace/task_board.md`
- `workspace/TASK_TEMPLATE.md`

## 11. Verification

- **Check:** Confirm task record, board entry, and discussion report.
- **Method:** Fetch each committed path from branch `gpt`.
- **Result:** Pending read-back.
- **Limitations:** Condensed Mode implementation is intentionally paused pending user inspection.

## 12. Handoff Instructions

Stop after presenting the task link. Do not modify the Condensed Mode skill or continue implementation until the user explicitly says to proceed.
