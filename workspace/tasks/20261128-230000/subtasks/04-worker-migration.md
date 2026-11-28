# Subtask: Worker queue, review/remediation lifecycle, attribution, grouping, and report migration

## Metadata

- **Template version:** 1.8
- **ID:** 20261128-230000-04
- **Parent Task ID:** 20261128-230000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Parent task 20261128-230000, explicitly authorized by user; execution cue provided.
- **Governing ADR(s):** ADR-0008
- **Dependencies:** 20261128-230000-02; 20261128-230000-03
- **Eligibility / deferral reason:** In Progress — dependencies 02 and 03 are Done and parent execution is active
- **Required:** Yes
- **Created:** 2026-11-28 23:00 UTC
- **Updated:** 2026-11-28 23:00 UTC
- **Root-cause group:** None
- **Ledger group:** None (legacy reports only)
- **Legacy Task IDs:** None

## Validation Contract

Declare task-specific checks in this JSON block. The coordinator binds the contract to the exact source commit SHA. Use an empty array when no additional checks are required. Repository policy checks remain mandatory and cannot be removed or overridden. Use only registered adapters and repository-relative entrypoints. Never add shell command strings, credentials, environment overrides, or permission settings.

```json
{
  "contract_revision": "1",
  "checks": []
}
```

## Validation Lifecycle

```json
{
  "state": "awaiting_ci",
  "source_sha": "c362482231e425125f642b84ceb642ba9a725856",
  "policy_revision": "a0a8173b716675638e18a30ff037f98dc52d60f6",
  "coordinator_run_id": null,
  "attempt": null,
  "outcome": null,
  "reconciled_at": null
}
```

## 1. Original Prompt

Implement the accepted ADR-0008 as part of the user's new parent task “ADR 8 implementation”.

## 2. Subsequent Instructions

- **2026-11-28:** User explicitly requested task creation, adequate subtasking, and Current selection; “Execute”.

## 3. Objective and Scope

Integrate non-blocking Worker lifecycle, index-first review, failure-only diagnosis, root-cause grouped child task reuse, attribution/fallback, cleanup lifecycle, and stage all producers/consumers onto the replacement.

## 4. Acceptance Criteria

1. Worker is non-blocking while validation runs and uses index-first triage.
2. Logs are inspected only for actionable recorded failures; failures grouped by root cause and child folders reused.
3. Parent attribution uses source Task-ID trailer; unresolved attribution uses permanent fallback without guessing.
4. Cancelled/superseded attempts create no feedback tasks and do not mutate task lifecycle.
5. Every producer and consumer migrates without weakening coverage; report tree remains until retirement gates are met.

## 5. Decisions and Progress

- ADR-0008 governs this work.
- Preserve existing validation coverage and legacy report system until migration gates are met.
- **Progress:** Added task lifecycle schema and task-record metadata, exact-SHA missing-dispatch recovery, and staged cutover gates for legacy producers/consumers. This commit completes the Worker lifecycle procedure, root-cause group reuse contract, migration inventory, catalog/navigation updates, and legacy Ledger ownership boundary. Added fail-closed direct-push cutover gates that require source/current policy activation, effective protection, and recovery dispatch availability; task-owned workflow-run diagnostics are suppressed while unrelated workflow-run diagnostics and push backfill remain available. Remaining: readback and Confirmation-dependent producer cutover.

## 6. State and Evidence

- **Commit SHA:** c362482231e425125f642b84ceb642ba9a725856
- **Changed paths:** Worker skill, task-validation interfaces, CI Ledger reference, document-type catalog, Workflow Map, task-validation README, task tracking records, and five validation/diagnostic workflows.
- **Readback:** Pending final readback
- **Checks:** Not performed
- **Limitations:** No local tests or hosted validation performed. Effective branch protection and default-branch recovery workflow availability remain external prerequisites; existing capture-failure attempts were not inspected or reconciled.

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
