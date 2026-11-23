# Workspace

The workspace is the task-management and conversation-navigation area. The Worker owns task records, selection, progress, handoffs, archive closeout, and the shared discussion register. Document Standards governs workspace document formats.

## Files

| Path | Purpose |
|---|---|
| [discussion.md](discussion.md) | Current-step brief, open discussions, and the three latest verified success reports |
| [task_board.md](task_board.md) | Task index, priorities, states, and current execution |
| [TASK_TEMPLATE.md](TASK_TEMPLATE.md) | Canonical task-record format |
| [tasks/](tasks/) | Active task records |
| [../reports/README.md](../reports/README.md) | Lint, Actions, and issue-ledger navigation |
| [../archive/README.md](../archive/README.md) | Archive and retention policy |

## Task workflow

1. Check the board and active records before creating work. Update an existing task when the objective continues; otherwise create a distinct task.
2. Record the user's request, scope, constraints, approval, priority, dependencies, and acceptance criteria.
3. Select one current execution task. Follow explicit user direction, then dependencies, priority, and age.
4. Record meaningful actions, decisions, verification, and blockers in the task record. Keep the board as an index.
5. Close only after acceptance criteria pass, the archive copy is created and read back, the retention index is updated, the active record is removed, and the board links to the archive commit.

Task IDs use UTC `YYYYMMDD-HHMMSS`. Use only the statuses Proposed, Ready, In Progress, Blocked, Paused, Done, and Cancelled. Optional assistant improvements remain Proposed until approved. Necessary follow-ups may be created automatically within the approved scope.

## CI issue workflow

GitHub Actions runs validation and publishes diagnostic evidence. Lint reports and Actions reports feed the [central CI issue ledger](../reports/triage/README.md). The ledger is the issue backlog; it deduplicates findings and stores evidence. The Worker groups related findings into workspace tasks and links each finding through `task_refs`. Ledger ingestion never creates tasks.

Do not run periodic triage or poll workflows. Review CI only when the user asks, a known failure blocks the task, or the task requires validation. Ordinary successful Actions runs are not persisted as diagnostic reports. A successful validation run URL and timestamp are sufficient resolution evidence; request a full success capture only when detailed logs are specifically required.

## Discussion register

The Worker maintains [discussion.md](discussion.md) in both conversation modes. Its Conversation Mode reference defines the section order, pre-step brief, open-discussion lifecycle, and three-report limit. Keep technical progress and handoffs in task records, not in the register.

## Recovery

Read this file, the board, and the selected task record. Check the current `gpt` repository state before resuming. Follow the task's Next Actions. Reconcile discrepancies against the latest user instruction and committed repository state.