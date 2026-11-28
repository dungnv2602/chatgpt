# Subtask: Secure publisher, idempotency, recovery, checkpoint, and recursion prevention

## Metadata

- **Template version:** 1.6
- **ID:** 20261128-230000-03
- **Parent Task ID:** 20261128-230000
- **Type:** Implementation
- **Status:** Ready
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Parent task 20261128-230000, explicitly authorized by user; execution cue provided.
- **Governing ADR(s):** ADR-0008
- **Dependencies:** 20261128-230000-01
- **Eligibility / deferral reason:** Ready when dependency subtasks are completed
- **Required:** Yes
- **Created:** 2026-11-28 23:00 UTC
- **Updated:** 2026-11-28 23:00 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

Implement the accepted ADR-0008 as part of the user's new parent task “ADR 8 implementation”.

## 2. Subsequent Instructions

- **2026-11-28:** User explicitly requested task creation, adequate subtasking, and Current selection; “Execute”.

## 3. Objective and Scope

Implement secret/write-permission isolation, atomic terminal status/review-task publication, safe concurrent idempotency, bounded recovery, durable checkpoint, and recursion prevention.

## 4. Acceptance Criteria

1. Verifier executes without secrets or write token; publisher has minimal scoped permissions and never executes untrusted code.
2. Each terminal attempt yields one atomic/idempotent status and review task.
3. Recovery handles missed triggers, partial failures, concurrency and retries safely.
4. Checkpoint advances only after fully reconciled events; unresolved records are protected and retention is 3 days after reconciliation.
5. Publisher commits cannot recursively trigger source validation.

## 5. Decisions and Progress

- ADR-0008 governs this work.
- Preserve existing validation coverage and legacy report system until migration gates are met.
- **Next:** Implement and commit this subtask's deliverables, then readback as required by the task workflow.

## 6. State and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** Not yet determined
- **Readback:** Pending
- **Checks:** Not performed
- **Limitations:** No runtime claims.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Execution self-check

Scope and parent are confirmed. Required, approved, and executed under the authorized parent batch. Preserve evidence and verification boundaries.

## 10. Handoff

Implement deliverables, commit, and update status/evidence. Do not close the parent until every required child and ADR confirmation gate is satisfied.

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| None | — | None yet | — |
