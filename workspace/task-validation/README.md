# Task Validation Operations

The Worker owns this status index and review queue. The publisher and recovery workflows update them atomically.

## Canonical state

- `status-index.json` is the only task-validation run-status index.
- Its schema is `.agent/skills/the-worker/assets/task-validation/task-validation-status-index.schema.json`.
- `closed_through` is the monotonic recovery checkpoint. Advance it only after every earlier attempt is accounted for and reconciled.
- `attempts` stores only the compact fields allowed by ADR-0008. Do not add findings, logs, diagnostics, evidence, remediation state, or task history.

## Review queue

- `reviews/<run-id>-<attempt>/review.md` is one review folder per non-cancelled, non-superseded terminal attempt.
- The publisher creates the status record and review folder in one commit.
- The Worker reads the index first. It opens logs only for recorded actionable failures.
- The Worker marks the attempt reconciled and removes its review folder after review. Reconciled attempt records remain for three days.
- Cancelled and superseded attempts have status records but no review folder or feedback task.

## Recovery and retention

- Unresolved attempts never expire.
- Recovery uses coordinator run metadata and aggregate artifacts. It never reads logs or validates source code.
- The checkpoint advances only through a fully reconciled, contiguous sequence of attempts.
- Metadata-only commits under this directory must not trigger source validation.
