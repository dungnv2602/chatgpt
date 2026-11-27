# Task Board

Canonical format: [TASK_BOARD_TEMPLATE.md](TASK_BOARD_TEMPLATE.md). Preserve its structure and scheduler contract.

## Scheduler contract

The Worker is the sole scheduler. This board publishes its current selection and ordered eligible queue. It is not a second scheduler. Compare the board with task records and child indexes before declaring the queue empty.

Check eligibility before priority or age. Dependencies must be satisfied, execution must be authorized, and status must be Ready. Rank eligible tasks by priority (P0 first), then age within the same priority unless a documented dependency or material constraint changes the order. Keep ineligible tasks out of the queue. List them in the appropriate deferred section with the exact reason.

**Approval:** Approved records explicit authorization for the documented scope or applicable standing authorization. Pending means the user has not authorized execution. Declined means the user rejected the proposal. Approval does not depend on status or eligibility.

This is the sole index of active task parents. Each parent folder contains `task.md` and `subtasks/README.md`. The parent index lists substantive children. Board links point to parents, except Current Execution may link to the selected child. Keep a parent open while a required child remains open. The Worker owns status, selection, and deletion at closeout.

## Current Execution

[Refactor Skills — P0](tasks/20261127-173000/task.md) — [child 05: Markdown links and heading anchors](tasks/20261127-173000/subtasks/05-ci-remediation-fix-lint-tooling-check-markdown-links-and-heading-anchors.md). The parent is persistent and remains open for future skills-refactoring subtasks.

## Ordered Eligible Execution Queue

1. **P0** — [20261127-173100-03: Fix lint report regression tests](tasks/20261127-173100/subtasks/03-ci-remediation-fix-lint-tooling-check-lint-report-regression-tests.md) — Approved, Ready, no dependencies. This task is next after the selected child.

## Next Task

[20261127-173100-03](tasks/20261127-173100/subtasks/03-ci-remediation-fix-lint-tooling-check-lint-report-regression-tests.md) is next after the current Refactor Skills child.

## Deferred Work

### Blocked

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261126-142500-03 | Fix lint tooling check: Markdown links and heading anchors | P0 | Blocked | Approved | Repository diagnostic evidence is now available in the indexed on_repo report. Re-evaluate the prior path/availability blocker and inspect current source links before scheduling. | [03](tasks/20261126-142500/subtasks/03-ci-remediation-fix-lint-tooling-check-markdown-links-and-heading-anchors.md) |
| 20261126-142500-23 | Fix lint tooling check: Lint report regression tests | P0 | Blocked | Approved | Latest indexed report contains complete output for both failed regression assertions. Re-evaluate the blocker against the current generator, template, and test source. | [23](tasks/20261126-142500/subtasks/23-ci-remediation-fix-lint-tooling-check-lint-report-regression-tests.md) |

### Proposed — decision pending

_No proposed tasks._

### Paused

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261127-173000-03 | Correct objective-based task parent selection | P1 | Paused | Approved | Reparented under Refactor Skills. Remaining audit is deferred behind P0 work. | [subtask](tasks/20261127-173000/subtasks/03-correct-objective-based-task-parent-selection.md) |
| 20261127-173000-02 | Consolidate specialist skills into The Worker | P1 | Paused | Approved | Refactor Skills child. Deferred behind P0 work. | [subtask](tasks/20261127-173000/subtasks/02-consolidate-specialist-skills-into-worker.md) |

### Dependency-waiting

_No dependency-waiting tasks._
