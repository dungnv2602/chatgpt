# Subtask: Operational Confirmation, scenario demonstrations, coverage reconciliation, and gated retirement

## Metadata

- **Template version:** 1.6
- **ID:** 20261128-230000-05
- **Parent Task ID:** 20261128-230000
- **Type:** Implementation
- **Status:** Ready
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Parent task 20261128-230000, explicitly authorized by user; execution cue provided.
- **Governing ADR(s):** ADR-0008
- **Dependencies:** 20261128-230000-02; 20261128-230000-03; 20261128-230000-04
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

Demonstrate ADR-0008 Confirmation operational scenarios through Actions, reconcile check coverage and all report producers/consumers, and retire .takeout/reports only after all Confirmation criteria are genuinely satisfied.

## 4. Acceptance Criteria

1. Demonstrate success, failure, missing/skipped check, cancellation/supersession, duplicate delivery, concurrent publication, missed trigger, publisher failure, stale result, and recursion prevention.
2. Confirm complete exact-SHA aggregation and protected policy binding.
3. Confirm recovery, checkpoint, bounded retention, unresolved protection, task attribution and grouping.
4. Confirm all report producers/consumers migrated and coverage preserved.
5. Retire the full .takeout/reports tree only after replacement is operational and Confirmation satisfied; document evidence and close parent/subtasks.

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
