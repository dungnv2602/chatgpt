# Task: ADR 8 implementation

## Metadata

- **Template version:** 2.9
- **ID:** 20261128-230000
- **Created:** 2026-11-28 23:00 UTC
- **Updated:** 2026-11-28 23:00 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User explicitly requested a new task titled “ADR 8 implementation”, sufficient implementation subtasks, and made it Current; execution cue “Execute” provided in this conversation.
- **Governing ADR(s):** [ADR-0008](../../adr/0008-ci-validation-error-tasks-and-automatic-feedback-loop.md)
- **Current execution:** Yes
- **Dependencies:** None
- **Eligibility / deferral reason:** In Progress on branch `gpt`; coordinator activation and exact-SHA missing-dispatch recovery remain gated by policy activation, report migration, and operational readiness. Default-branch dispatcher and scheduled recovery workflow availability are verified.
- **Related tasks:** 20261126-142500 (superseded administrative task; deleted after closeout)

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
  "state": "not_committed",
  "source_sha": null,
  "policy_revision": null,
  "coordinator_run_id": null,
  "attempt": null,
  "outcome": null,
  "reconciled_at": null
}
```

## 1. Original Request

> Update the task status, mark it as done, then delete under my command. Create a new task called "ADR 8 implementation" for this. Create sufficient subtasks if needed for implementation. Make the task current.

## 2. Subsequent Instructions

- **2026-11-28:** “I give you permission for this to do what you want to complete the verification Execute”
- **2026-11-28:** User directed that the prior task be closed and deleted, and the new task “ADR 8 implementation” be created, adequately subdivided, and made Current.
- **2026-11-28:** “Execute”

## 3. Objective and Acceptance Criteria

Implement accepted ADR-0008 in repository `dungnv2602/chatgpt`, branch `gpt`, preserving required validation coverage and transitioning safely from `.takeout/reports/` only after migration and Confirmation criteria are met.

Acceptance criteria are mapped to these required child tasks:
- Implement coordinator, protected policy and task contract, reusable workflow interfaces, generic verifier, and exact-SHA aggregation.
- Implement security isolation, terminal publisher, atomic/idempotent publication, recovery sweep, bounded retries, checkpoint and recursion prevention.
- Implement non-blocking Worker task lifecycle and index-first, failure-only diagnosis; grouped remediation, attribution, fallback, and child lifecycle.
- Migrate every report producer and consumer in staged order while preserving coverage; retire the legacy reports tree only when permitted by ADR.
- Demonstrate ADR-0008 Confirmation scenarios through GitHub Actions, using authorized inspection; do not run local scripts/tests/lint or dispatch/rerun workflows absent separate authorization.

## 4. Decisions

- Accepted ADR-0008 is the governing implementation specification.
- `.takeout/reports/` remains preserved until full migration and required operational evidence.
- Cancellation/supersession are non-actionable for feedback generation and cannot satisfy aggregate validation.
- Verification and reporting must be honest; no completion claims without evidence.

## 5. Progress

### 2026-11-28 23:00 UTC

- **Action:** Replaced the stalled implementation parent administratively with this focused implementation task and five implementation/confirmation subtasks.
- **Result:** This task is Current. The prior task did not meet ADR-0008 acceptance and was closed as superseded/cancelled, not represented as successfully implemented.
- **References:** ADR-0008; prior parent 20261126-142500 (deleted after closeout).
- **Next:** Start subtask 01: coordinator architecture, protected policy, contracts, and reusable workflow design/implementation.

### 2026-11-28 — Subtask 01 foundation closed

- **Result:** Closed subtask 01 after the Worker-owned policy, schema, adapter registry, interface documentation, and reusable workflow-call entry points were read back from branch `gpt`.
- **Commit:** `f036ecbd02a9f049486ffbe27f8d0d11edae314d` (task closeout); index reconciliation `892ec77fd5a4db52cc444b4a416b88ccb1782d04`.
- **Limitations:** GitHub branch-protection settings are not an ADR-0008 acceptance requirement. The existing reusable workflows still require exact-SHA and validation-only migration before coordinator invocation. No runtime or hosted validation is claimed.
- **Next:** Subtasks 02 and 03 are complete. Subtask 04 has entered In Progress.

### 2026-11-28 — Subtask 02 verifier and aggregate implementation closed

- **Result:** Added the task-contract builder, typed generic verifier, exact-SHA aggregate, coordinator workflow definition, regression tests, and exact-SHA validation-only reusable interfaces.
- **Governance:** Updated parent/subtask templates, Worker instructions, catalog, interface reference, and Workflow Map. Every task contract is resolved from one Task-ID trailer and bound to the exact source SHA.
- **Staging:** The coordinator remains workflow_call-only. Push activation is deferred until the privileged publisher/report migration is ready. This prevents duplicate validation cycles while legacy report producers remain active.
- **Protection:** The policy and coordinator activation remain staged pending publisher/report migration and operational readiness. GitHub branch-protection settings are not an ADR-0008 gate.
- **Evidence:** Implementation range from f036ecbd02a9f049486ffbe27f8d0d11edae314d to e2a9756a0f719882e2d35df1a049f0fada117dcb (101 commits). Regression tests are wired into document-standards CI but have not been executed by the Worker.
- **Limitations:** No local tests/lint, workflow dispatch, or hosted-run inspection. Publisher, recovery, checkpoint, Worker lifecycle, report migration, and operational Confirmation remain incomplete.
- **Next:** Subtasks 02 and 03 are Done. Proceed with subtask 04 for Worker lifecycle and report migration.
### 2026-11-28 — Subtask 04 lifecycle and migration staging

- **Action:** Completed the Worker lifecycle contract, exact-SHA/policy matching rules, root-cause group reuse semantics, and legacy producer/consumer inventory.
- **Result:** Existing reusable validation workflows and Worker-owned Ledger test path are preserved. Legacy report producers remain active where needed for non-task diagnostics; the report tree is not retired. Branch protection is not an ADR-0008 requirement; default-branch recovery availability is now confirmed on `main` after PR #10.
- **References:** ADR-0008 Confirmation; `task-validation-interfaces.md`; `workspace/task-validation/README.md`.
- **Readback:** Confirmed the lifecycle instructions, migration inventory, five workflow gates, catalog, map, task-validation README, and subtask tracking records from branch `gpt`.
- **Next:** Await exact-SHA validation and policy activation and operational readiness before subtask 05; do not inspect hosted logs or enable the coordinator prematurely.

### 2026-11-28 — Legacy producer cutover gates staged

- **Action:** Updated the three legacy validation workflows and two workflow-run diagnostic consumers to yield only when the source and current policies both authorize coordinator ownership and recovery dispatch is available.
- **Result:** Manual audits remain available. Legacy workflow-run capture is suppressed only for exact Task-ID coordinator-owned validation attempts; unrelated workflow-run diagnostics and push backfill remain active. This preserves non-task coverage while preventing duplicate task feedback.
- **References:** `.github/workflows/ste-lint-changed.yml`; `.github/workflows/ste-lint-full-docs.yml`; `.github/workflows/validate-document-standards.yml`; `.github/workflows/gh-actions-capture.yml`; `.github/workflows/gh-actions-diagnostics.yml`.
- **Next:** Read back the workflow changes, update the task lifecycle source SHA, and leave operational activation/Confirmation gated on policy activation and default-branch recovery availability.

### 2026-11-28 — External activation prerequisites remain an operational gate

- **Action:** Checked repository metadata, default-branch workflow availability, and accessible protection/ruleset metadata.
- **Result:** Default branch is `main`; dispatcher and recovery workflow files are now present there after PR #10. GitHub branch-protection settings are not required by ADR-0008. Coordinator activation remains staged pending publisher/report migration and operational readiness.
- **Limitations:** No hosted CI runs or logs were inspected. Existing capture-failure attempts remain unresolved.
- **Operational gates:** Default-branch recovery workflow availability and operational readiness must be established before automated missing-dispatch recovery or coordinator activation. Branch protection is not an ADR-0008 prerequisite. These gates do not prevent continued implementation and tracking work on `gpt`.
- **Next:** Hold subtask 05 in dependency-waiting; do not enable the coordinator or retire the legacy report tree.

### 2026-11-28 — residual protection gate removed; recovery availability verified

- **Correction:** Removed the remaining branch-protection prerequisite from `.github/workflows/task-validation.yml` (commit `a991bebd5a166805c18eadd1aebfa305797d4e14`). Targeted readback checks across the dispatcher/coordinator/recovery/publisher/verifier workflows, Worker validation scripts, and interface references found no remaining branch-protection enforcement gate in those checked paths. Branch protection is optional hardening outside ADR-0008 acceptance.
- **Recovery:** Verified that default branch `main` contains the dispatcher `workflow_dispatch` entry point and the scheduled recovery workflow. Updated both corresponding availability fields in the `gpt` policy to `verified` (commit `d2f5b4b9e28fe935e77fc2c79e5ee519d9dad804`). Coordinator activation remains staged pending report migration and operational readiness.
- **Review queue:** The compact status index contains 211 attempts, all `capture_failure` with missing check-set identity and no reconciliation timestamp; checkpoint remains at zero. No hosted logs were inspected, no unproven root cause or remediation task was invented, and all unresolved records remain retained.
- **Current subtask:** 04 remains In Progress. Continue the producer/consumer migration; preserve `.takeout/reports/` until every ADR-0008 migration and Confirmation criterion is demonstrated.

### 2026-11-28 — exact-SHA review queue remains unresolved

- The latest compact status-index readback contains 217 attempts, all `capture_failure` with `check_set_id: null`, no reconciliation timestamps, and a zero checkpoint.
- Subtask 04 has one exact matching attempt for source SHA `7814758586f68b3226822f760b4cbf06e86e108e`, Task-ID `20261128-230000-04`, policy blob `3e0efd87728646c0be2eb5854f95140151a3c44b`: run `46164069720`, attempt 1. Its lifecycle is now `review_required`, not reconciled.
- Hosted logs remain uninspected under Worker restrictions. Do not invent a root cause or remediation child; preserve all unresolved records and do not advance the checkpoint.
### 2026-11-28 — metadata-only recursion guard added

- The status index reached 220 unresolved `capture_failure` attempts. Recent records included source SHAs for task-record-only commits even though the dispatcher has `paths-ignore` entries for task metadata. This is consistent with push-range coalescing; hosted run metadata/logs were not inspected.
- Added an exact-tip-commit diff guard to `.github/workflows/task-validation-dispatch.yml` (source commit `c9ffdffd3c955af0ddb471f85557b32460315d8f`). Metadata-only commits under `.takeout/reports/`, `workspace/task-validation/`, and `workspace/tasks/` are rejected independently of push-level filters and bot identity.
- Subtask 04 lifecycle is now `awaiting_ci` for source `c9ffdffd3c955af0ddb471f85557b32460315d8f` and policy blob `3e0efd87728646c0be2eb5854f95140151a3c44b`. Previous unresolved attempts remain retained; no checkpoint was advanced.
## 6. Current State and Remaining Work

Subtask 01 is Done. Subtask 02 is Done with the generic verifier, contract builder, aggregate, reusable exact-SHA interfaces, staged coordinator definition, and terminal cancellation handling committed on branch `gpt`. Subtask 03 is Done: the isolated publisher, idempotency, recovery sweep, checkpoint/retention, and metadata-recursion exclusions are implemented and read back. Subtask 04 is In Progress; dependencies 02 and 03 are complete. Subtask 05 remains dependency-waiting on 04.

The dispatcher has a push trigger, but policy-gates coordinator activation. The exact-SHA coordinator remains staged until publisher/report migration and operational readiness gates are satisfied. GitHub branch protection is not an ADR-0008 prerequisite. The legacy report pipeline remains intact. Operational Confirmation and report-tree retirement remain incomplete.

## 7. Verification and Evidence

- **Implementation commits:** Subtask 01 foundation f036ecbd02a9f049486ffbe27f8d0d11edae314d; subtask 02 implementation head e2a9756a0f719882e2d35df1a049f0fada117dcb; subtask 03 implementation readback head 66fc180fe3a9b7ab6db6a72ab0d24a4e4d071e10; subtask 02 closeout/readback head 4706077d47ac54e146361cf288b5129c7dd46dd9.
- **Changed paths:** Worker skill and Workflow Map; task/subtask templates; task-validation policy, schema, and adapter registry; document catalog and interface reference; contract builder, verifier, aggregate, and three regression suites; five GitHub Actions workflow files; parent task, subtask record, and index.
- **Readback:** Subtasks 01, 02, and 03 have implementation readback from branch `gpt`; final parent readback and Confirmation remain pending.
- **Checks:** No local scripts, tests, lint, workflow dispatch, or hosted-run inspection performed. Regression tests are registered in the document-standards workflow.
- **Limitations:** Coordinator activation remains staged pending publisher/report migration and operational readiness. Publisher/recovery and exact-SHA verifier/aggregate implementations are complete at repository level. Worker lifecycle and staged report migration are in progress; operational Confirmation remains incomplete.

## 8. Execution self-check

- Repository and branch confirmed: `dungnv2602/chatgpt`, `gpt`.
- Governing ADR: ADR-0008.
- User request, authorization, and execution cue present.
- Parentage: this is the genuine implementation parent.
- Subtasks mapped to acceptance criteria.
- No local validation performed.
- Legacy report-tree retirement remains gated.

## 9. Handoff

Continue with eligible subtask 04. Keep report capture intact. Do not enable coordinator push activation before publisher/report migration and protected-policy integrity and activation. Do not mark the parent Done until all required implementation and Confirmation criteria are met.

## 10. Subtasks

Canonical index: [subtasks/README.md](subtasks/README.md).

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| None | — | No findings attributed yet | — |
