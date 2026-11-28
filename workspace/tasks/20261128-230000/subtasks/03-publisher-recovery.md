# Subtask: Secure publisher, idempotency, recovery, checkpoint, and recursion prevention

## Metadata

- **Template version:** 1.7
- **ID:** 20261128-230000-03
- **Parent Task ID:** 20261128-230000
- **Type:** Implementation
- **Status:** Done
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Parent task 20261128-230000, explicitly authorized by user; execution cue provided.
- **Governing ADR(s):** ADR-0008
- **Dependencies:** 20261128-230000-01
- **Eligibility / deferral reason:** Completed; acceptance criteria met at repository-implementation level
- **Required:** Yes
- **Created:** 2026-11-28 23:00 UTC
- **Updated:** 2026-11-28 12:50 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## Validation Contract

Declare task-specific checks in this JSON block. The coordinator binds the contract to the exact source commit SHA. Use an empty array when no additional checks are required. Repository policy checks remain mandatory and cannot be removed or overridden. Use only registered adapters and repository-relative entrypoints. Never add shell command strings, credentials, environment overrides, or permission settings.

```json
{
  "contract_revision": "1",
  "checks": []
}
```

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

### 2026-11-28 — publisher, recovery, checkpoint and recursion prevention implemented

- Implemented a separate publisher workflow and Worker-owned publisher script. The isolated publisher checks out trusted branch gpt, executes no source-commit code, receives no user secrets, and has only contents: write in its publish job.
- Publisher validation binds the exact source SHA, policy blob SHA, coordinator run ID, attempt, terminal outcome, and aggregate completion timestamp. It resolves Task-ID only from the source commit trailer and source task record.
- Status record and review folder are committed atomically. Duplicate publication is idempotent; conflicting duplicate data fails closed. Concurrent push conflicts and Git operations have bounded retries/timeouts.
- Added a Worker-owned status-index schema, compact workspace index, and review-template interface. Cancelled/superseded attempts are recorded without review folders and are immediately reconciled. A cancellation before coordinator jobs exist is also classified and captured; null check-set identity is permitted only for non-success terminal states where no check set exists.
- Implemented paginated recovery of dispatcher workflow runs and attempts, structured aggregate-artifact recovery, publication-gap repair, bounded API/Git retries, a monotonic checkpoint, and three-day retention after reconciliation. Unresolved records are never pruned and stop checkpoint advancement.
- Added a recovery workflow with push, post-coordinator reusable-call, and schedule entry points. The scheduled trigger is not operational while the repository default branch remains main; opportunistic push and post-coordinator recovery remain available on gpt.
- Prevented metadata recursion across the dispatcher, changed-document lint, document-standards workflow, and legacy diagnostics push trigger. The recovery push filter excludes the status index and review folders. Added regression assertions for these exclusions.
- Updated Worker interface documentation, document catalog, workspace index, Workflow Map, and protected policy review paths.
- **Handoff boundary:** Recovery now reconciles dispatcher attempts and publication gaps. Discovery of committed tasks awaiting CI, current-task staleness, and Worker review/remediation lifecycle remain in dependent subtask 04.
- **Protection:** GitHub branch protection is not required by ADR-0008. Coordinator activation remains staged pending report migration and operational readiness.
- **Validation:** Publisher and recovery regression suites are registered in validate-document-standards.yml. No local scripts/tests/lint were run and no hosted workflow runs/logs were inspected. No end-to-end runtime success is claimed.

## 6. State and Evidence

- **Commit SHA:** 66fc180fe3a9b7ab6db6a72ab0d24a4e4d071e10 (branch gpt head at final readback).
- **Implementation range:** 88 commits after e2a9756a0f719882e2d35df1a049f0fada117dcb; task-specific commits carry Task-ID: 20261128-230000-03. Bot-authored publication commits are not treated as validation evidence.
- **Changed paths:** Worker task-validation policy, status schema and review template; publisher/recovery scripts and regression tests; publisher/recovery/dispatcher/coordinator workflows; changed-document lint and legacy diagnostics trigger filters; document catalog and task-validation interface reference; Workflow Map; workspace index and operations README; task record and subtask index.
- **Readback:** Relevant scripts, tests, workflows, policy, schema, catalog, interface reference, Workflow Map, and task record were read back from branch gpt at the stated head.
- **Checks:** Regression suites are registered in document-standards CI. Not executed locally. Hosted CI was not inspected. GitHub branch API reports protected: false; scheduled workflows are not active from gpt while default branch is main.
- **Limitations:** Runtime behavior, publisher permissions in a hosted run, scheduled recovery, and end-to-end confirmation remain unverified. Committed-task-awaiting-CI reconciliation is assigned to subtask 04. The legacy report system remains intact.

## 7. Completion

- **Status:** Done
- **Completed at:** 2026-11-28 12:50 UTC
- **Completion basis:** All subtask 03 repository implementation deliverables are committed and read back. Automated regression coverage is registered. External/runtime prerequisites are explicitly retained as verification debt and do not invalidate this implementation closeout.

## 8. Hosted Validation

- **Status:** Not reviewed; hosted workflow inspection is prohibited by the current Worker execution policy.
- **Run URL:** Not reviewed

## 9. Execution self-check

- Scope and parentage match ADR-0008 subtask 03.
- Every task-specific implementation commit includes the exact Task-ID trailer.
- Publisher and recovery implementations, workflows, schemas, regression tests, ownership references, and recursion exclusions are committed and read back.
- No local validation or hosted CI inspection was performed.
- Scheduled recovery availability and operational readiness remain prerequisites.
- Subtask 04 owns committed-task discovery and Worker lifecycle integration.

## 10. Handoff

Continue with eligible subtask 02, which remains In Progress. Subtask 04 becomes eligible after subtask 02 is complete. Keep coordinator activation staged, preserve .takeout/reports/, and do not claim operational Confirmation.

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| None | — | None yet | — |
