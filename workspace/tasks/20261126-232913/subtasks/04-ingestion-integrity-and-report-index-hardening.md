# Subtask: Ingestion integrity and report-index hardening

## Metadata
- **ID:** 20261126-232913-04
- **Parent:** [20261126-232913](../task.md)
- **Type:** Implementation
- **Status:** Ready
- **Priority:** P0
- **Approval:** Approved
- **Governing ADR:** [ADR-0004](../../../adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md)
- **Created:** 2026-11-26 23:29 UTC
- **Updated:** 2026-11-26 23:29 UTC
- **Required:** Yes

## Objective
Ingestion integrity and report-index hardening as part of the accepted ADR-0004 implementation.

## Acceptance Criteria
1. Surface per-report ingestion failures as structured errors and return non-zero after safe partial progress is published.
2. Leave failed reports unprocessed and retryable.
3. Do not mark incomplete or pre-finalizer Actions captures as processed.
4. Validate report/run identifiers before path construction and reject traversal or malformed identifiers.
5. Fail closed when the index references a missing report classified complete.
6. Add regression tests for each failure and retry invariant.

## Progress
- **Current state:** Ready; follow the execution order in the parent subtask index.
- **Evidence:** None recorded.
- **Completion record:** Not Done. Record commit SHA(s), changed paths, and verification evidence on completion.

## Handoff
Execute only this subtask's scope. Record meaningful changes and evidence here and in the parent task. Do not mark Done until every acceptance criterion passes.
