# Task: Correct archive-operation and open-discussion lifecycle rules

## Metadata

- **ID:** 20261120-160152
- **Created:** 2026-11-20 16:01 UTC
- **Updated:** 2026-11-20 16:01 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** 20261120-153700; 20261120-123000
- **Archived:** No

## 1. Original Request

> This is one.
>
> This is two: in condensed mode, you only retain open discussions in discussion.md, clear the others shen they're no longer active.
>
> Fix your workflow.

## 2. Subsequent Instructions

> The active repository boundary says not to inspect or modify archive/.
>
> You asked if you should audit that folder, I said no. There's no global rule to not touch it.

## 3. Objective

Correct the repository workflow so that archive content remains outside audit scope without blocking required task archival operations, and Condensed Mode retains only unresolved discussions in `workspace/discussion.md`.

## 4. Requirements

- Preserve the user's refusal to audit or inspect archive contents.
- Explicitly permit required task archival writes and scheduled retention operations without reading archived contents.
- Keep task-board links and archival commit references correct.
- Define `workspace/discussion.md` as a temporary register of open discussions only, not a transcript, progress log, or historical record.
- Remove each discussion automatically when it becomes inactive; preserve unrelated open discussions.
- Leave only an empty-state placeholder when no open discussions remain.
- Keep durable progress and completion reports in task records.
- Update relevant workflow instructions and read back every changed active path from branch `gpt`.
- Do not inspect archived contents.

## 5. Decisions

- A refusal to audit archive contents does not prohibit required task archival writes.
- A discussion closes when it is answered, decided, implemented, rejected, withdrawn, or no longer needs user input.
- Clearing a resolved discussion is routine lifecycle maintenance. It does not require separate user approval.
- Closing one discussion must not clear unrelated open discussions.

## 6. Progress Log

### 2026-11-20 16:01 UTC

- **Action:** Reviewed the Conversation Mode, The Worker, workspace, and current task instructions.
- **Result:** Found two workflow defects. The Worker incorrectly prohibited all archive changes, including required task archival. Conversation Mode treated `discussion.md` as a continuous transcript/report stream and cleared it only after approval, rather than retaining open discussions only.
- **References:** `skills/conversation-mode/SKILL.md`; `skills/the-worker/SKILL.md`; `workspace/README.md`; `workspace/task_board.md`.
- **CI snapshot:** Current branch head was `aa239b1903e0681879005b0938e14e0197906ae4). One bounded attempt to access each applicable workflow run listing was rejected by the GitHub fetch endpoint; current CI status is unverified. No local lint/CI was run and no workflow was dispatched, rerun, waited for, or polled.
- **Next:** Update the two skills, correct the audit task's archive wording, clear resolved discussion entries, and verify all changed active paths.

## 7. Current State

The defects are identified. No workflow files have been changed yet.

## 8. Remaining Work

- Implement and verify the rule corrections.
- Clear resolved entries from `workspace/discussion.md`, retaining only genuinely open discussions.
- Commit the coherent change set to branch `gpt`.

## 9. Next Actions

1. Update Conversation Mode and The Worker.
2. Update the documentation-audit task boundary and checkpoint.
3. Update the task board and clear inactive discussion entries.
4. Read back all changed active paths and verify the commit.

## 10. References

- `skills/conversation-mode/SKILL.md`
- `skills/the-worker/SKILL.md`
- `workspace/discussion.md`
- `workspace/task_board.md`
- `workspace/tasks/20261120-123000-repository-documentation-audit.md`

## 11. Verification

- **Check:** Rule consistency, task-board state, and discussion-register contents.
- **Method:** Fetch each changed path from branch `gpt`.
- **Result:** Pending.
- **Limitations:** CI status is unverified because the bounded workflow-listing access attempt failed. No local lint or CI execution is permitted.

## 12. Handoff Instructions

Complete this task on branch `gpt`. Do not inspect archived contents. Required archival writes remain permitted. Keep only unresolved discussions in `workspace/discussion.md`; remove each thread as soon as it is inactive. When no unresolved discussions remain, leave the empty-state placeholder. After verification, archive this completed task through the normal Worker closeout procedure and resume task `20261120-123000`.
