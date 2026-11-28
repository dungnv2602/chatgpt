# Subtask: Generic verifier, exact-SHA aggregate, and coverage-preserving workflow migration

## Metadata

- **Template version:** 1.7
- **ID:** 20261128-230000-02
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
- **Updated:** 2026-11-28 12:55 UTC
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

Implement the generic verifier and aggregate outcome logic, migrate existing required checks into the coordinator/reusable flow, and preserve established coverage/baselines.

## 4. Acceptance Criteria

1. Generic verifier covers requirements not served by reusable checks.
2. Aggregate accounts for every expected check and exact source SHA/policy revision.
3. Missing, skipped, partial, cancelled, mismatched, and pending checks cannot produce success.
4. Existing coverage/baselines are preserved; coordinator terminal outcomes are explicit.

## 5. Decisions and Progress

- ADR-0008 governs this work.
- Preserve the direct-push validation/report path until the staged migration and Confirmation gates are satisfied.

### 2026-11-28 — exact-SHA verifier, aggregate and reusable validation entry points completed

- Implemented the Worker-owned contract builder. It requires exactly one final Task-ID trailer, resolves exactly one task record from the source commit tree, and binds the declared Validation Contract to the exact source SHA.
- Implemented the generic verifier with closed typed adapters, strict structured arguments, safe repository-relative paths, symlink containment, per-check timeouts, a 25-minute aggregate budget, shell-free execution, and a sanitized environment without secrets or write tokens.
- Implemented exact-SHA aggregation for the full mandatory policy set. It binds source SHA, policy blob SHA, check-set identity, coordinator run ID, and attempt. Missing, duplicate, unexpected, skipped, pending, partial, neutral, cancelled, superseded, mismatched, infrastructure, and capture states cannot produce success.
- Migrated the three established validation workflows to reusable exact-SHA entry points. Coordinator calls validate the exact source commit, skip legacy report publication and diagnostics, and preserve the direct-push report path while activation remains staged.
- Added regression suites for contract resolution, verifier security/resource constraints, and aggregate classification. They are registered in document-standards CI.
- Corrected terminal finalization so an artifact-upload failure does not turn a cancelled or superseded result into an actionable capture failure. Added a regression assertion for this behavior.
- **Protection and staging:** Effective branch protection remains unverified and the gpt branch is currently unprotected. Policy enforcement remains external-prerequisite; coordinator activation stays staged until branch protection and report migration are complete.
- **Validation:** Regression tests are registered but were not run locally. No hosted workflow results or logs were inspected. No runtime success is claimed.

## 6. State and Evidence

- **Commit SHA:** 4706077d47ac54e146361cf288b5129c7dd46dd9 (branch gpt head at final readback).
- **Changed paths:** Worker contract builder, generic verifier, aggregate, task-validation policy/schema/adapter registry; regression suites; coordinator and generic-verifier workflows; the three reusable validation workflows; task-validation interface, Worker instructions, catalog, templates and Workflow Map; task/subtask records and indexes.
- **Readback:** Contract builder, verifier, aggregate, their regression suites, policy/schema/registry, coordinator/verifier workflows, and all three reusable workflows read back from branch gpt at the stated head.
- **Checks:** Regression tests are registered in validate-document-standards.yml. No local scripts/tests/lint were run. No workflow dispatch or hosted-run inspection.
- **Limitations:** Coordinator activation remains staged. Branch protection is not enabled on gpt. Report producer/consumer migration and operational Confirmation remain in dependent subtasks 04 and 05. No runtime or CI success is claimed.

## 7. Completion

- **Status:** Done
- **Completed at:** 2026-11-28 12:55 UTC
- **Completion basis:** Contract builder, verifier, exact-SHA aggregation, reusable validation entry points, coverage-preserving staging, regression registration, and terminal outcome handling are committed and read back. Runtime and external prerequisites remain explicit verification debt.

## 8. Hosted Validation

- **Status:** Not reviewed; hosted workflow inspection is prohibited by the current Worker execution policy.
- **Run URL:** Not reviewed

## 9. Execution self-check

- Scope and parentage match ADR-0008 subtask 02.
- Task-specific implementation commits carry Task-ID: 20261128-230000-02.
- Exact-SHA contract binding, verifier, aggregate, reusable workflows, and regression suites were read back.
- Existing direct-push validation/report behavior remains intact while coordinator activation is staged.
- No local validation or hosted CI inspection was performed.
- Branch protection and report migration remain external/dependent gates.

## 10. Handoff

Subtasks 02 and 03 are complete. Subtask 04 is now dependency-eligible for Worker lifecycle and report migration. Subtask 05 remains dependency-waiting on subtask 04. Keep coordinator activation staged and preserve .takeout/reports/.
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
