# Subtask: Generic verifier, exact-SHA aggregate, and coverage-preserving workflow migration

## Metadata

- **Template version:** 1.7
- **ID:** 20261128-230000-02
- **Parent Task ID:** 20261128-230000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Parent task 20261128-230000, explicitly authorized by user; execution cue provided.
- **Governing ADR(s):** ADR-0008
- **Dependencies:** 20261128-230000-01
- **Eligibility / deferral reason:** Eligible — subtask 01 foundation is complete
- **Required:** Yes
- **Created:** 2026-11-28 23:00 UTC
- **Updated:** 2026-11-28 23:00 UTC
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
- Preserve existing validation coverage and legacy report system until migration gates are met.
### 2026-11-28 — exact-SHA verifier and aggregate implementation

- Added the Worker-owned task contract builder. It resolves exactly one Task-ID trailer and task record from the source commit tree.
- Added machine-readable Validation Contract blocks to parent/subtask templates. The coordinator injects the exact source SHA and rejects missing, ambiguous, malformed, or duplicate-key contracts.
- Added the typed generic verifier, closed adapter registry checks, safe repository path resolution, shell-free execution, sanitized task environment, isolated HOME/TMP, per-check timeouts, and a 25-minute aggregate execution budget.
- Added the exact-SHA aggregate. It binds source SHA, policy blob SHA, complete task-contract identity, coordinator run ID, and attempt. Missing, duplicate, skipped, pending, partial, mismatched, cancelled, and superseded states cannot produce success.
- Added regression suites for contract resolution, verifier security and resource limits, and aggregate classification. Wired them into validate-document-standards.yml.
- Migrated the three existing validation workflows to reusable exact-SHA inputs. Coordinator mode skips legacy report publishers and diagnostics jobs. Direct-push report behavior remains intact.
- Added task-validation.yml as a reusable coordinator and task-validation-verifier.yml as the isolated verifier. The coordinator is deliberately staged as workflow_call only. It has no push trigger while legacy publishers remain active.
- Updated the Worker skill, task templates, interface reference, document catalog, and Workflow Map to enforce canonical contract ownership and placement.
- Protection gate: protection.enforcement_status remains external-prerequisite; effective branch protection/ruleset could not be verified. coordinator.activation_status remains staged. Both gates fail closed.
- Validation: Regression tests are registered in CI but were not executed locally. No workflow was dispatched and no hosted run, logs, or artifacts were inspected.
- Next: Proceed with eligible publisher/recovery subtask 03. Do not enable the coordinator until its publisher and report migration gates pass.

## 6. State and Evidence

- **Commit SHA:** e2a9756a0f719882e2d35df1a049f0fada117dcb (latest implementation readback; 101 commits after subtask 01 foundation f036ecbd02a9f049486ffbe27f8d0d11edae314d)
- **Changed paths:** .agent/WORKFLOW_MAP.md; Worker SKILL.md; task and subtask templates; task-validation policy, schema, and adapter registry; document catalog and task-validation interface reference; verifier, contract builder, aggregate scripts and three regression suites; .github/workflows/ste-lint-changed.yml, ste-lint-full-docs.yml, validate-document-standards.yml, task-validation.yml, and task-validation-verifier.yml; parent task, this subtask, and subtask index.
- **Readback:** Implementation files and governance references read back from branch gpt. Final readback continues before closeout.
- **Checks:** No local scripts, tests, or lint executed. Regression tests are wired into the document-standards workflow. No workflow dispatch or hosted-run inspection.
- **Limitations:** Coordinator activation is staged and effective external policy protection is unverified. The privileged publisher, recovery sweep, durable checkpoint, and report migration belong to dependent work and remain incomplete. No runtime or CI success is claimed.
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
