# Subtask: Coordinator, protected policy, contracts, and reusable workflow entry points

## Metadata

- **Template version:** 1.6
- **ID:** 20261128-230000-01
- **Parent Task ID:** 20261128-230000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Parent task 20261128-230000, explicitly authorized by user; execution cue provided.
- **Governing ADR(s):** ADR-0008
- **Dependencies:** None
- **Eligibility / deferral reason:** Ready when dependency subtasks are completed
- **Required:** Yes
- **Created:** 2026-11-28 23:00 UTC
- **Updated:** 2026-11-28
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

### 2026-11-28 — Initial implementation

- Added `.github/task-validation-policy.json` with the initial mandatory-check manifest, exact-SHA/policy binding requirements, terminal outcomes, and explicit external branch-protection prerequisite.
- Added `.github/task-validation-contract.schema.json` defining exact-SHA task contracts, closed adapter IDs, repository-relative entrypoints, structured arguments, and bounded timeouts; arbitrary shell strings and extra properties are excluded.
- Added `.github/task-validation-adapters.json` as the initial closed typed-adapter registry.
- Added `.github/task-validation/README.md` documenting policy semantics, current validation coverage, reusable workflow interface, and downstream security/migration gates.
- Exposed `workflow_call` entry points and the optional `coordinator_call` boolean on the three existing validation workflows. The full-document workflow bypasses its direct-push supersession cancellation logic for coordinator calls.
- Read back all new policy/schema/registry/interface files and all three modified workflow files from branch `gpt`.
- **Not complete:** Existing reusable workflows still publish legacy reports with write permissions and some check out the branch name rather than the immutable caller SHA. They are deliberately not wired to a coordinator until subtask 02 removes those hazards.
- **Not complete:** GitHub branch protection/ruleset enforcement for policy files is an external prerequisite and has not been established or verified. The policy explicitly records this rather than claiming protection.
- **Checks:** No local scripts, tests, lint, workflow dispatch, or hosted-run inspection performed.

- **Next:** Implement the coordinator only after reusable workflow migration provides exact-SHA, validation-only entry points. External protection remains a gate; do not claim policy is protected.



### 2026-11-28 — canonical ownership correction

- **Action:** Subtask `20261127-173000-74` owns the Worker governance correction. Its implementation moved the task-validation policy, contract schema, and adapter registry into `.agent/skills/the-worker/assets/task-validation/`. It moved the explanatory interface guide into `.agent/skills/the-worker/references/task-validation-interfaces.md`.
- **Result:** The old `.github/task-validation-*.json` and `.github/task-validation/README.md` paths were deleted. GitHub workflow definitions remain under `.github/workflows/`. The original paths above remain historical commit provenance, not current locations.
- **Current owner:** The Worker skill owns the policy, schema, registry, and explanatory guidance. The Worker asset index and document-type catalog link the canonical files.
- **Scope:** This correction does not change ADR-0008 validation semantics or claim that branch protection has been established.

- **Task attribution correction:** The canonical prevention task is child 74 under the persistent Refactor Skills parent. Earlier implementation commits used reused child IDs 64 and 65 before the complete parent history was checked. Those commit trailers are immutable and are documented in child 74. Subsequent commits use child 74.

## 6. State and Evidence

- **Commit SHA:** `fe1ae3700e02414dea5c9816a0f4dcc7a6231d51` (current branch HEAD; implementation foundation is present in branch history)
- **Changed paths:** `.github/task-validation-policy.json`; `.github/task-validation-contract.schema.json`; `.github/task-validation-adapters.json`; `.github/task-validation/README.md`; `.github/workflows/ste-lint-changed.yml`; `.github/workflows/ste-lint-full-docs.yml`; `.github/workflows/validate-document-standards.yml`.
- **Readback:** Policy, schema, adapter registry, interface README, and all three existing validation workflows read back from `gpt`.
- **Checks:** No local scripts/tests/lint and no workflow dispatch or hosted-run inspection, as prohibited by parent task without separate authorization.
- **Limitations:** Coordinator workflow is not implemented or wired. Existing reusable workflows still have write-capable report publishers and branch-name checkout paths, so they are unsafe for coordinator invocation. Repository rulesets endpoint returned an empty list; branch-protection read was forbidden to the integration, so effective branch protection remains unverified. No runtime claims.

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
