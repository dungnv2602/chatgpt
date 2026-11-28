# Task: ADR 8 implementation

## Metadata

- **Template version:** 2.8
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
- **Eligibility / deferral reason:** Eligible — user authorization and execution cue satisfied
- **Related tasks:** 20261126-142500 (superseded administrative task; deleted after closeout)

## Validation Contract

Declare task-specific checks in this JSON block. The coordinator binds the contract to the exact source commit SHA. Use an empty array when no additional checks are required. Repository policy checks remain mandatory and cannot be removed or overridden. Use only registered adapters and repository-relative entrypoints. Never add shell command strings, credentials, environment overrides, or permission settings.

```json
{
  "contract_revision": "1",
  "checks": []
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
- **Limitations:** Effective GitHub branch protection remains unverified. The existing reusable workflows still require exact-SHA and validation-only migration before coordinator invocation. No runtime or hosted validation is claimed.
- **Next:** Subtasks 02 and 03 are now eligible.

### 2026-11-28 — Subtask 02 verifier and aggregate implementation in progress

- **Result:** Added the task-contract builder, typed generic verifier, exact-SHA aggregate, coordinator workflow definition, regression tests, and exact-SHA validation-only reusable interfaces.
- **Governance:** Updated parent/subtask templates, Worker instructions, catalog, interface reference, and Workflow Map. Every task contract is resolved from one Task-ID trailer and bound to the exact source SHA.
- **Staging:** The coordinator remains workflow_call-only. Push activation is deferred until the privileged publisher/report migration is ready. This prevents duplicate validation cycles while legacy report producers remain active.
- **Protection:** Effective GitHub branch protection/ruleset remains unverified. The policy remains external-prerequisite and activation remains staged. Both runtime gates fail closed.
- **Evidence:** Implementation range from f036ecbd02a9f049486ffbe27f8d0d11edae314d to e2a9756a0f719882e2d35df1a049f0fada117dcb (101 commits). Regression tests are wired into document-standards CI but have not been executed by the Worker.
- **Limitations:** No local tests/lint, workflow dispatch, or hosted-run inspection. Publisher, recovery, checkpoint, Worker lifecycle, report migration, and operational Confirmation remain incomplete.
- **Next:** Continue with eligible subtask 03 while subtask 02 remains In Progress pending activation and protection gates.
## 6. Current State and Remaining Work

Subtask 01 is Done. Subtask 02 remains In Progress with the generic verifier, contract builder, aggregate, reusable exact-SHA interfaces, and staged coordinator definition committed on branch `gpt`. Subtask 03 is Done: the isolated publisher, idempotency, recovery sweep, checkpoint/retention, and metadata-recursion exclusions are implemented and read back. Subtasks 04 and 05 remain dependency-waiting.

The coordinator has no push trigger. Its activation remains staged until the privileged publisher and report migration are ready. Effective branch protection/ruleset enforcement remains unverified and is an external prerequisite. The legacy report pipeline remains intact. Operational Confirmation and report-tree retirement remain incomplete.

## 7. Verification and Evidence

- **Implementation commits:** Subtask 01 foundation f036ecbd02a9f049486ffbe27f8d0d11edae314d; subtask 02 implementation head e2a9756a0f719882e2d35df1a049f0fada117dcb; subtask 03 implementation readback head 66fc180fe3a9b7ab6db6a72ab0d24a4e4d071e10.
- **Changed paths:** Worker skill and Workflow Map; task/subtask templates; task-validation policy, schema, and adapter registry; document catalog and interface reference; contract builder, verifier, aggregate, and three regression suites; five GitHub Actions workflow files; parent task, subtask record, and index.
- **Readback:** Initial and ongoing readback from branch `gpt`. Final readback and closeout remain pending.
- **Checks:** No local scripts, tests, lint, workflow dispatch, or hosted-run inspection performed. Regression tests are registered in the document-standards workflow.
- **Limitations:** Coordinator activation and external policy protection remain gated. Publisher/recovery, Worker lifecycle, report migration, and Confirmation are incomplete.

## 8. Execution self-check

- Repository and branch confirmed: `dungnv2602/chatgpt`, `gpt`.
- Governing ADR: ADR-0008.
- User request, authorization, and execution cue present.
- Parentage: this is the genuine implementation parent.
- Subtasks mapped to acceptance criteria.
- No local validation performed.
- Legacy report-tree retirement remains gated.

## 9. Handoff

Continue with eligible subtask 03. Keep report capture intact. Do not enable coordinator push activation before publisher/report migration and verified policy protection. Do not mark the parent Done until all required implementation and Confirmation criteria are met.

## 10. Subtasks

Canonical index: [subtasks/README.md](subtasks/README.md).

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| None | — | No findings attributed yet | — |
