# The Worker assets

Canonical copy-ready templates and supporting static formats owned by The Worker.

| Asset | Purpose | Canonical consumer |
|---|---|---|
| [TASK_TEMPLATE.md](TASK_TEMPLATE.md) | Parent task record | `workspace/tasks/<task-id>/task.md` |
| [SUBTASK_TEMPLATE.md](SUBTASK_TEMPLATE.md) | Child task record | `workspace/tasks/<parent>/subtasks/NN-*.md` |
| [TASK_BOARD_TEMPLATE.md](TASK_BOARD_TEMPLATE.md) | Scheduler board structure | `workspace/task_board.md` |
| [DISCUSSION_TEMPLATE.md](DISCUSSION_TEMPLATE.md) | Discussion register structure | `workspace/discussion.md` |
| [ADR_TEMPLATE.md](ADR_TEMPLATE.md) | Accepted decision record | `workspace/adr/` |
| [DRAFT_TEMPLATE.md](DRAFT_TEMPLATE.md) | Proposed decision record | `workspace/draft/` |
| [ANALYSIS_TEMPLATE.md](ANALYSIS_TEMPLATE.md) | Repository analysis snapshot | `workspace/analysis/` |
| [actions-report-template.md](actions-report-template.md) | Diagnostic report | Generated report family |
| [session-brief-template.md](session-brief-template.md) | Session brief | Drawing session records |
| [session-summary-template.md](session-summary-template.md) | Session closeout summary | Drawing session closeout |
| [conversation-integrity-template.md](conversation-integrity-template.md) | Conversation integrity record | Conversation archive |
| [task-validation/task-validation-policy.json](task-validation/task-validation-policy.json) | ADR-0008 mandatory validation policy | Task-validation coordinator |
| [task-validation/task-validation-contract.schema.json](task-validation/task-validation-contract.schema.json) | Exact-source-SHA task contract schema | Generic verifier |
| [task-validation/task-validation-adapters.json](task-validation/task-validation-adapters.json) | Closed typed adapter registry | Generic verifier |
| [task-validation/task-validation-status-index.schema.json](task-validation/task-validation-status-index.schema.json) | Compact run-status index schema and recovery checkpoint | Publisher and recovery workflows |
| [task-validation/task-validation-review-template.md](task-validation/task-validation-review-template.md) | Per-attempt review queue entry | Publisher workflow and Worker |

Catalog and governance: [document-type-catalog.md](../references/document-type-catalog.md). Templates are static assets; scripts and explanatory reference documents remain in their respective directories.
