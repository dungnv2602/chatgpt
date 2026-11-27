# Task: Refactor Skills

**Template version:** 2.6

## Metadata

- **ID:** 20261127-173000
- **Created:** 2026-11-27 17:30 UTC
- **Updated:** 2026-11-27 11:08 UTC
- **Priority:** P0
- **Status:** Ready
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit request to create the Refactor Skills task and place workspace/tasks/20261127-102301 beneath it.
- **Governing ADR(s):** None
- **Current execution:** Yes
- **Dependencies:** None
- **Eligibility / deferral reason:** Eligible — Ready; approved, no dependencies. Selected as current execution by user's explicit priority instruction.
- **Related tasks:** None

## 1. Original Request

> Create a task named "refactor skills" and put workspace/tasks/20261127-102301 as subtask into it.

## 2. Subsequent Instructions

### 2026-11-27 18:27 UTC

> workspace/tasks/20261127-173000/task.md Make this task P0, we focus on this task from now on.

- **Action:** Set parent priority to P0 and select it as Current Execution.
- **Approval:** Explicit authorization to prioritize and focus execution on this task.

## 3. Objective and Acceptance Criteria

Serve as the persistent, open parent task and coordination point for skills refactoring in the repository, including the current consolidation work and future refactoring initiatives. This is an explicitly authorized standing parent for skills-refactoring work; it is not a finite deliverable and must not be retired or closed merely because its current children are complete.

1. Keep this parent task open as the enduring skills-refactoring workstream.
2. Capture each distinct current or future skills-refactoring deliverable as its own subtask under this parent, after confirming it genuinely concerns refactoring the repository's skills.
3. Preserve original prompts, approvals, dependencies, progress, evidence, and history in each child record.
4. Keep the subtask index and task board reconciled as children are created, activated, paused, completed, or removed at closeout.
5. Never mark this parent Done, Cancelled, or delete its task folder as ordinary child closeout. Only a new explicit user instruction may change this standing lifecycle rule.

## 4. Decisions

- The existing task is reparented as a subtask rather than duplicated as an independent parent.
- This is a persistent skills-refactoring parent, not a finite project task. Completed children may be closed and deleted under normal closeout, but the parent and its folder remain open indefinitely unless the user explicitly instructs otherwise.

### 2026-11-27 18:40 UTC

> This task acts as a placeholder for refractoring skills now and in the future. You do not retire this task, only creat subtasks under it.

- **Decision:** Preserve this task as the standing parent for current and future skills-refactoring work. Create follow-up deliverables as child subtasks; do not create replacement parents for work within this defined scope or close/delete this parent at child closeout.

## 5. Progress

### 2026-11-27 18:29 UTC

- **Action:** Set this parent to P0 and selected it as Current Execution. Activated child 01 and reconciled the board and child index.
- **Result:** Readback confirmed parent, child, index, and board state. Children 02 and 03 remain Paused.
- **References:** Commit `1e6800f40e4c1bf1e15263f0a479a54afe81468a`; child `24f697da8a75972ff7f6a0dca7302a125e63499c`; index `3f0101796d08a5eba78dfe2fd4120b7445bf5c62`; board `91ca878a4c151aeb65d3f5ff78b438af8e437aa3`.
- **Next:** Execute child 01.

### 2026-11-27 17:30 UTC

- **Action:** Created Refactor Skills parent and began reparenting existing document-governance consolidation.
- **Result:** Parent record and child structure created.
- **References:** Existing task ID 20261127-102301.
- **Next:** Reconcile hierarchy and board.

## 6. Current State and Remaining Work

This parent remains open as the persistent skills-refactoring workstream. Child 01 (document governance consolidation) has been completed and closed. Children 02 and 03 remain tracked as Paused. Future skills-refactoring requests that fit this scope must be captured as new child subtasks under this parent. Do not retire this parent when the current children are complete.

## 7. Verification and Evidence

- **Commit SHA:** `1e6800f40e4c1bf1e15263f0a479a54afe81468a` (parent priority/current-execution); `24f697da8a75972ff7f6a0dca7302a125e63499c` (child 01 activation); `3f0101796d08a5eba78dfe2fd4120b7445bf5c62` (subtask index); `91ca878a4c151aeb65d3f5ff78b438af8e437aa3` (board)
- **Changed paths:** `workspace/tasks/20261127-173000/task.md`; `workspace/tasks/20261127-173000/subtasks/01-consolidate-document-standards-into-worker.md`; `workspace/tasks/20261127-173000/subtasks/README.md`; `workspace/task_board.md`
- **Readback:** Verified all four paths on branch `gpt`.
- **Checks:** Not performed
- **Limitations:** No tests performed.

## 8. Handoff

Keep this persistent P0 Refactor Skills parent open. Create and execute child subtasks for current and future skills-refactoring deliverables. Do not close or delete the parent task unless the user explicitly changes this instruction.

## 9. Subtasks

Canonical index: [subtasks/README.md](subtasks/README.md).

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| `lint-tooling-fd63ee164167664baaa97d9b` | high | Lint tooling check failed: Lint report regression tests | [report](../../../.takeout/reports/lint_reports/on_changed/history/45979960470-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45979960470) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45984083069-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45984083069) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45985300823-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45985300823) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45985475477-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45985475477) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45986815109-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45986815109) |
| `lint-tooling-2c26d8bc14fd4d4bbe314234` | high | Lint tooling check failed: Markdown links and heading anchors | [report](../../../.takeout/reports/lint_reports/on_changed/history/45911866106-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911866106) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45981578057-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45981578057) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45981806913-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45981806913) · [report](../../../.takeout/reports/lint_reports/on_changed/history/45984083069-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45984083069) · [report](../../../.takeout/reports/lint_reports/on_repo/history/45987814713-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45987814713) |