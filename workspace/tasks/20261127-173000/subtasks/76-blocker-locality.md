# Subtask: Blocker-locality enforcement and stop-proof scheduler gate

**Template version:** 1.9

## Metadata

- **ID:** 20261127-173000-76
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User approved tightening blocker-locality logic and explicitly issued Execute.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** Eligible — approved and execution authorized.
- **Required:** Yes
- **Created:** 2026-11-28
- **Updated:** 2026-11-28
- **Root-cause group:** None
- **Ledger group:** None (legacy reports only)
- **Legacy Task IDs:** None

## Validation Contract

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

## 1. Original Prompt

> Tighten the logic

## 2. Subsequent Instructions

- **2026-11-28:** User explicitly approved and issued Execute for the proposed blocker-locality and stop-proof tightening.

## 3. Objective and Scope

Strengthen the Worker scheduler so operation-specific blockers cannot implicitly stop universal execution or independent eligible work. Make continuation mandatory and stop conditions demonstrable, without broadening authorization or bypassing safety and permission gates.

## 4. Acceptance Criteria

1. A blocker is scoped to the specific operation/prerequisite it prevents.
2. Scheduler immediately reselects independent eligible work and preserves execution authorization for unaffected scope.
3. Repeated retries/polling are avoided; blocked work is revisited only when relevant conditions change.
4. Stop requires reconciliation of remaining in-scope work and proof that no eligible/recoverable operation remains or a boundary prevents all progress.
5. Reporting cannot serve as a scheduler transition or premature transfer of control.
6. Changed canonical owner and tracking read back; no unperformed validation claimed.

## 5. Decisions and Progress

- User approved this tightening and Execute.
- Reinforced the Worker’s canonical execution invariant with a mandatory blocker-locality rule, continuation step, and stop-proof gate. This is a scheduler-enforcement specification rather than a duplicate instruction in secondary references.
- Kept ADR-0008 as Current Execution; this child is tracked under the persistent skills-refactoring parent and does not divert the scheduler focus.

## 6. State and Evidence

- **Commit SHA:** Not committed yet
- **Changed paths:** `.agent/skills/the-worker/SKILL.md`; task record; subtask index; parent record; task board.
- **Readback:** Pending
- **Checks:** Not performed
- **Limitations:** No local tests/scripts/lint or hosted CI inspection.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Execution self-check

Scope, parentage, approval and canonical owner verified. Implementation commit and tracking/readback remain.

## 10. Handoff

Complete tracking and readback; close at implementation quiescence. No hosted CI inspection authorized.

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| None | — | None | — |
