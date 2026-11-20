# Workspace

The workspace tracks project tasks across conversations.

The Worker skill defines the operating procedure. Read [The Worker](../skills/the-worker/SKILL.md) before you manage tasks.

## Files

| Path | Purpose |
|---|---|
| [task_board.md](task_board.md) | Task index, priority, status, and selection order |
| [TASK_TEMPLATE.md](TASK_TEMPLATE.md) | Template for individual task records |
| [tasks/](tasks/) | Current task records |
| [../archive/README.md](../archive/README.md) | Archive and retention policy |
| [../archive/tasks/](../archive/tasks/) | Archived task records |

## Operating rules

- Use UTC for task IDs and timestamps.
- Check the board before creating a task.
- Keep one current execution task.
- Preserve original user requests and relevant clarifications in task records.
- Record every meaningful action and result in the task file.
- Keep the board as an index. Do not duplicate detailed progress there.
- Verify repository state before resuming a task.
- Update the task record before switching tasks or ending work.
- Create necessary assistant follow-ups automatically.
- Mark optional assistant improvements as Proposed. Wait for user approval before execution.
- Apply the same task workflow in every conversation mode.

## Task ID and filename

Use YYYYMMDD-HHMMSS in UTC. Add a two-digit suffix when IDs collide within one second.

Use YYYYMMDD-HHMMSS-short-kebab-title.md for task filenames.

## Task status

- Proposed — optional assistant task awaiting approval.
- Ready — approved and eligible for selection.
- In Progress — work has started and remains incomplete.
- Blocked — a dependency or external condition prevents progress.
- Paused — work is intentionally inactive.
- Done — acceptance criteria are met.
- Cancelled — the task will not continue.

## Recovery

Read this file, then [task_board.md](task_board.md), then the selected task record. Verify the repository before resuming. Follow the task's Next Actions.

## Navigation

- [Task board](task_board.md)
- [Task template](TASK_TEMPLATE.md)
- [The Worker skill](../skills/the-worker/SKILL.md)
- [Archive policy](../archive/README.md)
