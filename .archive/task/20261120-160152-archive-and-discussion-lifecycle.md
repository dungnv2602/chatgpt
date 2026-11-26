# Task: Correct archive-operation and open-discussion lifecycle rules

## Metadata

- **ID:** 20261120-160152
- **Created:** 2026-11-20 16:01 UTC
- **Updated:** 2026-11-20 16:02 UTC
- **Priority:** P1
- **Status:** Done
- **Origin:** User
- **Approval:** Approved
- **Current execution:** No
- **Dependencies:** None
- **Related tasks:** 20261120-153700; 20261120-123000
- **Archived:** Yes
- **Archived at:** 2026-11-20 16:02 UTC

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

### 2026-11-20 16:02 UTC

- **Action:** Implemented the workflow corrections and completed branch read-back verification.
- **Result:** Conversation Mode now retains only unresolved discussions and removes each resolved thread automatically. The Worker now permits required archival/retention writes while keeping archive contents outside inspection and audit scope. The documentation-audit task's boundary now distinguishes content-audit exclusion from required archival writes. `workspace/discussion.md` contains only the empty-state placeholder because no unresolved discussions remain.
- **Commit:** [a6761ed](https://github.com/dungnv2602/chatgpt/commit/a6761ed13f27d2f170edfe8417183bd4cc6520b6).
- **Read-back:** Fetched all six changed paths from branch `gpt`. Verified the two skill rules, audit-task boundary correction, task-board state, task record, and exact discussion placeholder.
- **CI:** The bounded run-listing access attempt was unavailable. CI remains unverified. No local lint or CI was run; no workflow was dispatched, rerun, waited for, or polled.
- **Next:** Resume task `20261120-123000` after this task's archival closeout.


### 2026-11-20 16:01 UTC

- **Action:** Reviewed the Conversation Mode, The Worker, workspace, and current task instructions.
- **Result:** Found two workflow defects. The Worker incorrectly prohibited all archive changes, including required task archival. Conversation Mode treated `discussion.md` as a continuous transcript/report stream and cleared it only after approval, rather than retaining open discussions only.
- **References:** `skills/conversation-mode/SKILL.md`; `skills/the-worker/SKILL.md`; `workspace/README.md`; `workspace/task_board.md`.
- **CI snapshot:** Current branch head was `aa239b1903e0681879005b0938e14e0197906ae4). One bounded attempt to access each applicable workflow run listing was rejected by the GitHub fetch endpoint; current CI status is unverified. No local lint/CI was run and no workflow was dispatched, rerun, waited for, or polled.
- **Next:** Update the two skills, correct the audit task's archive wording, clear resolved discussion entries, and verify all changed active paths.

## 7. Current State

The workflow corrections are committed and verified on branch `gpt`. The discussion register is empty because no unresolved discussions remain.

## 8. Remaining Work

- Implement and verify the rule corrections.
- Clear resolved entries from `workspace/discussion.md`, retaining only genuinely open discussions.
- Commit the coherent change set to branch `gpt`.

## 9. Next Actions

1. Archive this completed task record and update the historical task-board link.
2. Resume task `20261120-123000`.

## 10. References

- `skills/conversation-mode/SKILL.md`
- `skills/the-worker/SKILL.md`
- `workspace/discussion.md`
- `workspace/task_board.md`
- `workspace/tasks/20261120-123000-repository-documentation-audit.md`

## 11. Verification

- **Check:** Rule consistency, task-board state, and discussion-register contents.
- **Method:** Fetch each changed path from branch `gpt`.
- **Result:** All six changed paths were fetched from branch `gpt`; targeted content checks passed.
- **Limitations:** CI status is unverified because the bounded workflow-listing access attempt failed. No local lint or CI execution was performed.

## 12. Handoff Instructions

This task is complete. Its record is archived at `archive/tasks/20261120-160152-archive-and-discussion-lifecycle.md`. Do not inspect archived contents. Resume task `20261120-123000` on branch `gpt`. Keep only unresolved discussions in `workspace/discussion.md` and remove each thread as soon as it becomes inactive.
