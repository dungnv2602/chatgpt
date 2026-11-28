# Subtask: Coordinator, protected policy, contracts, and reusable workflow entry points

## Metadata

- **Template version:** 1.6
- **ID:** 20261128-230000-01
- **Parent Task ID:** 20261128-230000
- **Type:** Implementation
- **Status:** Ready
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Parent task 20261128-230000, explicitly authorized by user; execution cue provided.
- **Governing ADR(s):** ADR-0008
- **Dependencies:** None
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

Design and implement exact-SHA coordination foundations, protected policy resolution, structured task contract/schema, registered adapter interfaces, reusable workflow-call entry points, and repository-owned verifier interface.

## 4. Acceptance Criteria

1. Protected policy and contract are established and validated against the accepted design.
2. Coordinator is commit- and policy-revision-bound; expected check manifest is explicit.
3. Reusable entry points preserve existing validation semantics and avoid duplicate trigger loops.
4. Security boundary and documented interfaces are ready for downstream work.

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
