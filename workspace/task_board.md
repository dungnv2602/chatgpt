# Task Board

Canonical format: [TASK_BOARD_TEMPLATE.md](../.agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md). Preserve its structure and Worker pointer.

**Template version:** 1.1

## Scheduler contract

Follow [The Worker](../.agent/skills/the-worker/SKILL.md) for task selection, eligibility, execution authorization, queue rebuilding, decision collection, and closeout. This board publishes current state only. It does not define operating rules.

## Current Execution

- **20261127-173000-74 — Prevent Worker skill-governance drift** — P1, In Progress, Approved. [Subtask](tasks/20261127-173000/subtasks/74-prevent-worker-skill-governance-drift.md)
  - Parent: [20261127-173000 — Refactor Skills](tasks/20261127-173000/task.md)

## Ordered Eligible Execution Queue

_None. Current execution is active._

## Next Task

- **20261127-173000-74 — Prevent Worker skill-governance drift** — Current execution. [Subtask](tasks/20261127-173000/subtasks/74-prevent-worker-skill-governance-drift.md)

## Deferred Work

### Current focus reconciliation

The current child corrects Worker-owned artifact placement and closes the document catalog's non-Markdown coverage gap. ADR-0008 implementation remains open under current task **20261128-230000**. Preserve .takeout/reports until migration and Confirmation gates are satisfied.

### Blocked

_None._

### Proposed — decision pending

**DRAFT-0009 — Project, Task, and Knowledge Lifecycle.** Proposal in review; no implementation authorization.

### Paused

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| 20261128-221000 | Plans | P2 | Paused | Approved | Future planning is explicitly deferred by the user. | [task](tasks/20261128-221000/task.md) |

### Dependency-waiting

_None._
