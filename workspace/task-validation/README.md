# Task Validation Operations

The Worker owns this status index and review queue. The publisher and recovery workflows update them atomically.
Operational authority and task lifecycle: .agent/skills/the-worker/SKILL.md.

## Canonical state

- `status-index.json` is the only task-validation run-status index.
- Its schema is `.agent/skills/the-worker/assets/task-validation/task-validation-status-index.schema.json`.
- `closed_through` is the monotonic recovery checkpoint. Advance it only after every earlier attempt is accounted for and reconciled.
- `attempts` stores only the compact fields allowed by ADR-0008. Do not add findings, logs, diagnostics, evidence, remediation state, or task history.

## Review queue

- `reviews/<run-id>-<attempt>/review.md` is one review folder per non-cancelled, non-superseded terminal attempt.
- The publisher creates the status record and review folder in one commit.
- The Worker is non-blocking while CI runs. When assigned to review, it reads this index first; successful attempts need no log inspection, and logs are opened only for recorded actionable failures when authorized.
- The source Task-ID trailer resolves to an active genuine parent. Missing, invalid, ambiguous, or inactive attribution routes to the single policy-designated permanent fallback parent: `workspace/tasks/20261128-193800/task.md`. Never infer a parent or use the current board pointer.
- Group related failures by root cause and parent. Create or reuse one P0 child per actionable root cause, not one child per check, job, log line, or attempt.
- After review, the Worker marks the attempt reconciled and removes its review folder. Reconciled attempt records remain for three days.
- Cancelled and superseded attempts have status records but no review folder, feedback task, or task-state mutation.
- Only a complete success for the exact current task SHA and policy revision, with no required subtasks remaining, may mark a task Done.

## Recovery and retention

- Unresolved attempts never expire.
- Recovery uses coordinator run metadata and aggregate artifacts. It never reads logs or validates source code.
- The checkpoint advances only through a fully reconciled, contiguous sequence of attempts.
- Metadata-only commits under this directory must not trigger source validation.
