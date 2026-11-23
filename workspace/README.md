# Workspace

The workspace tracks project tasks and the shared pre-step brief, discussion, and success-report register across conversations and modes.

Task operations follow [The Worker skill](../skills/the-worker/SKILL.md).

[Conversation Mode](../skills/conversation-mode/SKILL.md) owns the temporary discussion register.

## Files

| Path | Purpose |
|---|---|
| [discussion.md](discussion.md) | Current work-step brief, open discussions, and the three most recent successful reports in every mode |
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
- Check repository state before resuming a task.
- Update the task record before switching tasks or ending work.
- Create necessary assistant follow-ups automatically.
- Mark optional assistant improvements as Proposed. Wait for user approval before execution.
- Apply the same task workflow in every conversation mode.
- Conversation Mode maintains `discussion.md` in every mode. The Worker supplies task state and ensures the register remains current.

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

Read this file, then [task_board.md](task_board.md), then the selected task record. Check the repository before resuming. Follow the task's Next Actions.

In both modes, Conversation Mode reads and maintains [discussion.md](discussion.md). Before each meaningful work step, it commits and reads back a concise Current Step brief, then links the file before execution. The file has three sections in this order: Current Step, Open Discussions, then Reports. Current Step contains only the next action, its scope, and expected result. Open Discussions contains anything awaiting user input and all unresolved failure outcomes. Reports contains only completed, verified successes and retains at most the three most recent entries. Default Mode may add normal chat detail. Condensed Mode uses extremely short chat responses and the single-link rule.

## Navigation

- [Open discussions](discussion.md)
- [Task board](task_board.md)
- [Task template](TASK_TEMPLATE.md)
- [The Worker skill](../skills/the-worker/SKILL.md)
- [Conversation Mode skill](../skills/conversation-mode/SKILL.md)
- [Archive policy](../archive/README.md)
