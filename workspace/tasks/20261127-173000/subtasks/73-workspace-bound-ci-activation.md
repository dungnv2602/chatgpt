# Subtask: Workspace-Bound CI Activation

**Template version:** 1.6

## Metadata

- **ID:** 20261127-173000-73
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User explicitly requested “Fix your workflow” and supplied the standalone “Execute” cue on 2026-11-28.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** In Progress — explicit execution authorization received; canonical workflow and map are being corrected.
- **Required:** Yes
- **Created:** 2026-11-28 06:54 UTC
- **Updated:** 2026-11-28 06:54 UTC
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

- **Commit SHA:** Not committed
- **Changed paths:** Pending
- **Readback:** Pending
- **Checks:** Not performed; local scripts/tests/lint and hosted CI are outside this scope.
- **Limitations:** Remote readback verifies committed content, not runtime behavior.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Execution self-check

- Canonical owner and map read from branch `gpt`.
- Parentage, scope, approval, and standalone execution cue verified.
- No CI data access is required for this workflow correction.
- Readback of every changed path is required before closeout.

## 10. Handoff

Implement the task-scoped CI activation gate in The Worker, align the Workflow Map, read back all changed files, then reconcile and close this child under the parent lifecycle.

## 11. Ledger Findings

None.
