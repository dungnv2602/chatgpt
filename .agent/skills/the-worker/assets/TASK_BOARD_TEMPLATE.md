# Task Board

Canonical template path: `.agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md`
**Template version:** 1.1

## Scheduler contract

Follow `.agent/skills/the-worker/SKILL.md` for task selection, eligibility, execution authorization, queue rebuilding, decision collection, and closeout. This board publishes current state only. It does not define operating rules.

## Current Execution

[One selected task/child, or _None._]

## Ordered Eligible Execution Queue

[Ordered list of eligible Ready, approved tasks with satisfied dependencies, within the current authorized focus, or _No eligible tasks._]

## Next Task

[Next task within the current authorized focus. If none remains, list other open parents only as unselected; otherwise _None._]

## Deferred Work

### Blocked

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| [Populate rows, or _No blocked tasks._] |

### Proposed — decision pending

[List tasks requiring a user decision or authorization, or _No proposed tasks._]

### Paused

| ID | Title | Priority | Status | Approval | Reason | Task record |
|---|---|---:|---|---|---|---|
| [Populate rows, or _No paused tasks._] |

### Dependency-waiting

[List tasks waiting on prerequisites that are not external blockers, or _No dependency-waiting tasks._]

## Template usage

Copy this structure to `workspace/task_board.md`. Replace placeholders with current verified state; omit unused table rows and use explicit empty-state statements. Keep scheduling and decision rules in The Worker. Do not duplicate them on the board.
