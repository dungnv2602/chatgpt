# Subtasks — 20261126-232913

Parent: [20261126-232913](../task.md)  
Governing decision: [ADR-0004](../../../adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md)

Each child is an independently tracked work unit with its own stable ID, type, status, acceptance criteria, evidence, and completion record. Parent completion is blocked until every required child is Done.

## Execution order
1. [20261126-232913-01 — Task folder templates and Worker lifecycle](01-task-folder-templates-and-worker-lifecycle.md) — In Progress
2. [20261126-232913-02 — Ledger task generation and governance handoff](02-ledger-task-generation-and-governance.md) — Ready
3. [20261126-232913-03 — Commit-based CI resolution and recurrence retention](03-ci-resolution-and-recurrence-retention.md) — Ready
4. [20261126-232913-04 — Ingestion integrity and report-index hardening](04-ingestion-integrity-and-report-index-hardening.md) — Ready
5. [20261126-232913-05 — Active-task migration and folder archive compatibility](05-active-task-migration-and-archive-compatibility.md) — Ready
6. [20261126-232913-06 — Regression coverage and documentation/catalog alignment](06-regression-tests-and-documentation.md) — Ready

## Completion contract
- Each child is Done only when its own acceptance criteria pass and evidence is recorded.
- CI remediation children use the commit-based rule in ADR-0004; hosted validation remains separate metadata.
- The parent is Done only when all six required children are Done and the parent outcome is verified.
