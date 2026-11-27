# Subtask: Enforce autonomous execution to quiescence

**Template version:** 1.5

## Metadata

- **ID:** 20261127-173000-57
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** Done
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User request on 2026-11-28 to audit and strengthen autonomous execution, blocker handling, and one-at-a-time user input.
- **Governing ADR(s):** ADR-0004
- **Dependencies:** None
- **Eligibility / deferral reason:** In Progress — authorized within the user's active Refactor Skills focus
- **Required:** Yes
- **Created:** 2026-11-27 23:01 UTC
- **Updated:** 2026-11-27 23:02 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

> Check if we already have the rule to not bother me unless absolutely necessary, you autonomously execute the task to the very end, if one subtask is blocked, you move on to another unblocked subtask. Only ping me with blocked ones and require my input one by one. Identify the gaps in your workflow, tighten it, make you must respect it while working.

## 2. Subsequent Instructions

None.

## 3. Objective and Scope

Make The Worker follow an explicit queue-draining procedure for every authorized execution batch. A task-level blocker must not stop independent eligible work. The Worker must rebuild the queue after each material task-state or dependency change. It must suppress routine user-facing progress and blocker messages. At quiescence, it may ask one essential question for one user-resolvable blocker, then resume queue selection after the answer.

Update the Worker, Conversation Mode, Session Start, initialization history, and task-board scheduler contract. Preserve existing authorization, decision governance, mandatory startup notices, safety, access, and hosted-CI restrictions. This task implements the existing Worker-owned selection and task-lifecycle contract in ADR-0004. It does not add a new project-wide scheduling model.

## 4. Acceptance Criteria

1. The Worker defines an ordered execution loop that rebuilds the full eligible queue after every task-state, approval, or dependency change.
2. A blocker isolated to one task does not stop another independent eligible task.
3. The Worker records exact blocker evidence and skips the blocked task without asking the user while eligible work remains.
4. Conversation Mode prohibits routine progress, status, and per-task blocker pings during an active batch, except for mandatory higher-priority notices or an immediate safety, privacy, access, or authority boundary.
5. At quiescence, the Worker asks at most one concise question about one user-resolvable blocker.
6. The Worker records the answer, rebuilds the queue, and asks about another blocker only after the resumed work reaches quiescence again.
7. Session Start and the task-board contract apply the same rules without weakening initialization or hosted-CI restrictions.
8. Read back every changed path and commit the work to branch `gpt`.

## 5. Decisions and Progress

- **Decision:** Treat this request as an operational clarification of the accepted Worker selection and task-lifecycle contract in ADR-0004. Do not create a new decision model.
- **Progress:** Audited the Worker, Conversation Mode, Session Start, initialization policy, task board, templates, and ADR-0004. Confirmed that general non-interruption guidance existed but lacked a deterministic queue-reselection procedure and explicit no-ping rule.
- **Implementation:** Updated the canonical execution loop, user-input coordination, startup batch steps, initialization history, and live task-board scheduler contract.
- **Closeout:** Read back all nine changed paths from branch `gpt`. Every expected change marker was present. The branch head matched the implementation commit.

## 6. State and Evidence

- **Commit SHA:** `c60358df2cc81747a5223f2d5aa5c750bb4773df`
- **Changed paths:** `.agent/skills/the-worker/SKILL.md`, `.agent/skills/the-worker/references/conversation-mode.md`, `.agent/SESSION_START.md`, `.agent/INITIALIZATION_POLICY.md`, `workspace/task_board.md`, `workspace/discussion.md`, `workspace/tasks/20261127-173000/task.md`, `workspace/tasks/20261127-173000/subtasks/README.md`, and this subtask.
- **Readback:** All nine paths were fetched from branch `gpt` at commit `c60358df2cc81747a5223f2d5aa5c750bb4773df`. Each expected change marker was present.
- **Checks:** No local scripts, tests, or lint were run. Hosted CI results were not inspected.
- **Limitations:** Readback confirms committed content. It does not prove hosted workflow behavior.

## 7. Completion

- **Status:** Done
- **Completed at:** 2026-11-27 23:02 UTC
- **Completion basis:** All eight acceptance criteria passed. The implementation commit is on `gpt`. Readback confirmed every changed path and the expected instruction markers.

## 8. Hosted Validation

Not applicable.

## 9. Handoff

Closed after commit and readback. The parent lifecycle requires deletion of completed child records after closeout. Do not inspect hosted CI.

## 10. Ledger Findings

None.
