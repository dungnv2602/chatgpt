# Workspace

Navigation for task records, decision records, analysis, and unified CI evidence. The Worker owns repository task operations and document governance.

## Records and canonical formats

| Path | Purpose |
|---|---|
| [discussion.md](discussion.md) | Current discussion and decisions |
| [task_board.md](task_board.md) | Published execution and deferred state |
| [tasks/](tasks/) | Active task folders and subtask indexes |
| [task-validation/](task-validation/README.md) | Exact-SHA status index, recovery checkpoint, and review queue |
| [draft/](draft/README.md) | Decision proposals |
| [adr/](adr/README.md) | Accepted decisions |
| [analysis/](analysis/README.md) | Repository analysis snapshots |
| [../.agent/skills/the-worker/assets/](../.agent/skills/the-worker/assets/README.md) | Canonical task, subtask, board, decision and analysis templates |
| [../.takeout/reports/README.md](../.takeout/reports/README.md) | Legacy CI evidence navigation pending ADR-0008 migration |

## Ownership

- Follow [The Worker](../.agent/skills/the-worker/SKILL.md) for task capture, hierarchy, approvals, scheduling, execution, decisions, verification, and closeout.
- Use the canonical templates and document-type catalog. Do not copy operating rules into this navigation file.
- Use `task-validation/` and The Worker for ADR-0008 attempt review and lifecycle. The legacy report guide applies only to pre-migration findings and evidence.
