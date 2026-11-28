# Task: ADR 8 implementation

## Metadata

- **Template version:** 2.7
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

## 6. Current State and Remaining Work

No ADR-0008 implementation deliverables are yet committed under this task. The legacy report pipeline remains intact. All five required subtasks are open; implementation and Confirmation remain pending.

## 7. Verification and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** Task records and board only
- **Readback:** Task creation and board reconciliation pending commit
- **Checks:** Not performed
- **Limitations:** This task administrative setup does not establish ADR-0008 operational behavior.

## 8. Execution self-check

- Repository and branch confirmed: `dungnv2602/chatgpt`, `gpt`.
- Governing ADR: ADR-0008.
- User request, authorization, and execution cue present.
- Parentage: this is the genuine implementation parent.
- Subtasks mapped to acceptance criteria.
- No local validation performed.
- Legacy report-tree retirement remains gated.

## 9. Handoff

Begin with subtask 01. Keep report capture intact. Do not mark the parent Done until all required implementation and Confirmation criteria are met.

## 10. Subtasks

Canonical index: [subtasks/README.md](subtasks/README.md).

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| None | — | No findings attributed yet | — |
