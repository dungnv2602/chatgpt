# Subtask: Workspace-Bound CI Activation

**Template version:** 1.6

## Metadata

- **ID:** 20261127-173000-73
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** Done
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User explicitly requested “Fix your workflow” and supplied the standalone “Execute” cue on 2026-11-28.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** Done — acceptance criteria satisfied and all changed paths read back from branch `gpt`.
- **Required:** Yes
- **Created:** 2026-11-28 06:54 UTC
- **Updated:** 2026-11-28 07:00 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

> Fix your workflow

## 2. Subsequent Instructions

### 2026-11-28 06:54 UTC

> Execute

- **Action:** Authorize implementation of the prepared workflow correction.

## 3. Objective and Scope

Correct The Worker so CI work is activated only through an assigned CI task in the workspace. General session initialization must not independently inspect CI report indexes, report history, the Ledger, or establish a CI baseline. Update the Workflow Map to reflect the same boundary.

Scope is limited to the canonical Worker instructions and workflow overview, plus task tracking. Do not modify CI report data, Ledger state, CI scripts, task-board policy beyond publishing this task, or hosted workflows.

## 4. Acceptance Criteria

1. The Worker explicitly prohibits CI report, index, history, and Ledger inspection during ordinary session initialization and unrelated work.
2. CI operations and CI-specific references activate only when an assigned CI task exists in the workspace and is selected within authorized scope.
3. Startup P0/task reconciliation remains workspace-task based and does not imply an automatic CI baseline or Ledger reconciliation.
4. The Workflow Map shows CI as a task-activated workflow, not a mandatory startup phase.
5. The changed owner documents and task tracking are read back from branch `gpt`.

## 5. Decisions and Progress

- Parentage confirmed: this directly advances the persistent Refactor Skills objective and its workflow-refactoring acceptance criteria.
- Canonical owner: `.agent/skills/the-worker/SKILL.md`; map is its navigation summary.
- The CI Ledger reference remains intact and task-activated. No report or Ledger data is in scope.

## 6. State and Evidence

- **Commit SHA:** `f9bfbdb2ea5a4f1d0b051ac8a6c5963e00e2e82e` (Worker), `8d2b8187bae4f2c7f163959c0a3e7157132f9617` (Worker activation correction), `892825e5222e21e5e06661bee49d95bda2991c89` (Workflow Map), `b8bec9e517f048698a8a8b3b7de53f0ec9d67468` (task capture), `4c16cc30eb76db33304cb5ce12fba5e78b91ebe9` (subtask index), `9ca067ddb004c08223893aba41af6bb473e964d6` (board).
- **Changed paths:** `.agent/skills/the-worker/SKILL.md`; `.agent/WORKFLOW_MAP.md`; `workspace/task_board.md`; `workspace/tasks/20261127-173000/subtasks/README.md`; this subtask record.
- **Readback:** Worker SHA `a4cac0c49aa0c1b1d858f199e8564043e531ca93` confirms startup prohibits CI report/index/history/Ledger reads and CI baseline reconciliation; both CI references require an assigned selected workspace CI task. Workflow Map SHA `ba5ee2c8beba2dd3233dc7c60581b5a17d58e135` removes Ledger reconciliation from startup and states the workspace-task activation boundary. Board and index readback confirm tracking.
- **Checks:** No local scripts/tests/lint and no hosted CI inspection, per Worker restrictions.
- **Limitations:** Remote readback verifies committed content, not runtime behavior. Initial implementation commits were made without the required Task-ID trailer; the task-tracking closeout commit will carry the trailer and preserve provenance.

## 7. Completion

- **Status:** Done
- **Completed at:** 2026-11-28 07:00 UTC
- **Completion basis:** The Worker and Workflow Map now enforce workspace-assigned CI task activation; all changed files were read back from branch `gpt`.

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Execution self-check

- Canonical owner and map read from branch `gpt`.
- Parentage, scope, approval, and standalone execution cue verified.
- No CI data access is required for this workflow correction.
- Readback of every changed path is required before closeout.

## 10. Handoff

Workflow correction is complete and read back. Close this child under the persistent parent lifecycle; no CI data or hosted validation was accessed.

## 11. Ledger Findings

None.
