# Subtask: Coordinator, protected policy, contracts, and reusable workflow entry points

## Metadata

- **Template version:** 1.6
- **ID:** 20261128-230000-01
- **Parent Task ID:** 20261128-230000
- **Type:** Implementation
- **Status:** Done
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Parent task 20261128-230000, explicitly authorized by user; execution cue provided.
- **Governing ADR(s):** ADR-0008
- **Dependencies:** None
- **Eligibility / deferral reason:** Complete — foundation deliverables committed and read back
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

Establish the exact-SHA coordination foundations, Worker-owned policy and task-contract interfaces, registered adapter interface, reusable workflow-call entry points, and documented security boundary. The operational coordinator and safe workflow migration are downstream deliverables.

## 4. Acceptance Criteria

1. Worker-owned policy, schema, and adapter registry exist at their cataloged canonical paths and express the accepted ADR-0008 requirements.
2. The policy declares the exact source-SHA and policy-blob binding requirements, mandatory check manifest, and terminal outcomes. Coordinator execution remains gated on safe reusable-workflow migration.
3. Existing required workflows expose reusable `workflow_call` entry points without replacing their direct triggers or weakening their existing validation behavior.
4. The interface documentation defines the security boundary, structured contract constraints, and distinguishes required policy integrity from optional repository hardening.
5. All canonical files and references are read back from branch `gpt`. No runtime or hosted-validation result is claimed.

## 5. Decisions and Progress

- ADR-0008 governs this work.
- Preserve existing validation coverage and the legacy report system until migration gates are met.

### 2026-11-28 — Initial implementation

- Added the initial task-validation policy, contract schema, adapter registry, and interface guide.
- Exposed `workflow_call` entry points and the optional `coordinator_call` boolean on the three existing validation workflows.
- The full-document workflow bypasses its direct-push supersession cancellation logic for coordinator calls.
- Read back the policy/schema/registry/interface files and all three modified workflow files.
- Existing reusable workflows still publish legacy reports with write permissions, and some check out a branch name rather than the immutable caller SHA. They must not be wired to the coordinator until subtask 02 removes those hazards.
- GitHub branch protection/ruleset enforcement is not required by ADR-0008.

### 2026-11-28 — Canonical ownership correction

- Subtask `20261127-173000-74` moved the policy, contract schema, and adapter registry into `.agent/skills/the-worker/assets/task-validation/`.
- It moved the explanatory interface guide into `.agent/skills/the-worker/references/task-validation-interfaces.md`.
- The old `.github/task-validation-*.json` and `.github/task-validation/README.md` paths were deleted.
- The Worker asset index and document-type catalog record the canonical ownership.
- GitHub Actions workflow definitions remain under `.github/workflows/`.
- The implementation should not impose branch-protection settings as an ADR-0008 requirement.
- The canonical prevention task is child 74 under the persistent Refactor Skills parent. Earlier implementation commits used reused child IDs 64 and 65 before the complete parent history was checked. Those commit trailers are immutable and are documented in the persistent parent history.

### 2026-11-28 — Foundation acceptance and closeout

- **Result:** The policy, schema, registry, and interface documentation satisfy this subtask's foundation scope. The policy binds mandatory checks and exact-SHA validation; it does not require GitHub branch protection.
- **Result:** The three existing workflows expose reusable entry points. Their legacy publication permissions and branch-based checkout behavior remain unsafe for coordinator invocation. Subtask 02 owns that migration.
- **Boundary:** This subtask does not claim that GitHub branch protection is active, that the coordinator or generic verifier exists, or that any hosted validation passed.
- **Next:** Subtasks 02 and 03 can proceed from the committed interface foundation. Protected-policy integrity and activation remain required; GitHub branch protection is not an ADR-0008 gate.

## 6. State and Evidence

- **Commit SHA:** Initial implementation foundation `fe1ae3700e02414dea5c9816a0f4dcc7a6231d51`; canonical ownership reconciliation `a64fbbb94b7c513c04634ca65f6a10a1bac71688`.
- **Changed paths:** Canonical policy, schema, adapter registry, interface guide, asset index, document catalog, Worker instructions, catalog validator/tests, and the three reusable validation workflows. Historical `.github/task-validation*` paths were removed.
- **Readback:** Canonical Worker-owned policy, schema, registry, interface guide, asset index, catalog, validator, regression tests, Worker and Agent Skill Authoring skills, and all three validation workflows were read from branch `gpt`.
- **Checks:** No local scripts, tests, lint, workflow dispatch, or hosted-run inspection performed.
- **Limitations:** GitHub branch-protection settings were not verified; this is outside ADR-0008 acceptance criteria. Coordinator/verifier implementation, exact-SHA migration, publisher, aggregate, and runtime behavior remain downstream work.

## 7. Completion

- **Status:** Done
- **Completed at:** 2026-11-28
- **Completion basis:** Foundation acceptance criteria satisfied; canonical paths and interfaces committed and read back. External policy enforcement and downstream runtime work remain explicit gates, not claims of completion.

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Execution self-check

Scope and parent confirmed. Deliverables are within the approved ADR-0008 implementation. Canonical ownership and format were checked. No local validation or hosted-run inspection was performed.

## 10. Handoff

Proceed with subtask 02 (generic verifier, exact-SHA aggregate, and coverage-preserving workflow migration) and subtask 03 (secure publisher and recovery). Do not close the parent until all required children and ADR confirmation gates are satisfied.

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| None | — | None yet | — |
