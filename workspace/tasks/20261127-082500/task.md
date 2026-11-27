# Task Folder: Refactor task board to reflect scheduler working order

## Metadata

- **ID:** 20261127-082500
- **Created:** 2026-11-27 08:25 UTC
- **Updated:** 2026-11-27 08:25 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User explicitly approved the board refactor described in the conversation on 2026-11-27.
- **Governing ADR(s):** None — non-implementation task
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** None
- **Ledger parent group:** None

Approval is authorization, not status or eligibility. Approved means explicit authorization for the recorded scope or applicable standing authorization; Pending means not authorized; Declined means rejected. Record approval scope/source. A concise "Approve" authorizes the immediately preceding proposal only within its stated scope. Do not infer approval from task status.

## 1. Original Request

The approved change is to refactor the task board so that it explicitly reflects the scheduler's working order, including:
- Current Execution
- Ordered eligible execution queue, ranked according to scheduling rules
- Next task, clearly identifiable
- Deferred work: Proposed, Blocked, Paused, and dependency-waiting tasks, separated from executable work
- The Worker remains the scheduling authority. The board reflects its decisions without introducing competing scheduling logic.

## 2. Subsequent Instructions

- **2026-11-27:** User approved the refactor. Approval authorizes implementation of the described board design.

## 3. Objective

Make the task board visibly represent the Worker's scheduling order and decision, so readers can see the current task, ordered eligible candidates, next selection, and deferred tasks with reasons.

## 4. Requirements and Acceptance Criteria

1. The board clearly identifies Current Execution.
2. It presents an ordered eligible execution queue with the Worker's scheduling rationale or rank.
3. It clearly identifies the Next Task.
4. It separates Proposed, Blocked, Paused, and dependency-waiting work from eligible execution.
5. The Worker remains the only scheduling authority. The board is a published representation, not a competing scheduler.
6. The board remains concise and does not duplicate full task details.
7. The board's task links, statuses, and pointer reconcile with active records.

## 5. Decisions

- Keep one Current Execution pointer.
- Display ranked candidates only when eligible.
- Show deferred categories and reasons separately.
- Do not invent a second scheduling mechanism.

## 6. Progress Log

### 2026-11-27 08:25 UTC

- **Action:** Initialized the approved task and committed a Current Step brief.
- **Result:** Brief read back from branch gpt.
- **References:** `workspace/discussion.md`, commit `918adfdd4321f0349b26cfcc352e237adeec0a8d`.
- **Next:** Create task records and refactor board structure.

## 7. Current State

The task is in progress. The board refactor has not yet been committed.

## 8. Remaining Work

- Refactor board layout.
- Read back and verify the board and task records.
- Commit and reconcile the board and discussion register.

## 9. Next Actions

1. Create task record and child index.
2. Refactor `workspace/task_board.md`.
3. Read back and verify all changed paths.
4. Complete closeout and delete the task folder after acceptance checks.

## 10. References

- `workspace/task_board.md`
- `.agent/skills/the-worker/SKILL.md`
- `.agent/skills/the-worker/references/conversation-mode.md`
- `workspace/README.md`
- `.agent/skills/document-standards/references/document-type-catalog.md`

## 11. Verification

- **Check:** Startup and source instructions read back.
- **Method:** GitHub remote file readback.
- **Result:** Verified.
- **Limitations:** Board implementation and hosted validation not yet checked.

## 12. Handoff Instructions

Complete the board refactor within the approved scope. The Worker retains scheduling authority. Do not inspect hosted CI results.

## 13. Subtasks

Canonical child index: [subtasks/README.md](subtasks/README.md).

The subtask index is authoritative. The parent cannot become Done while any required subtask is not Done.

## 14. Ledger Findings

None.
