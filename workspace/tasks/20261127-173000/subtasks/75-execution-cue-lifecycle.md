# Subtask: Universal execution cue and authorization lifecycle hardening

**Template version:** 1.8

## Metadata

- **ID:** 20261127-173000-75
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User approved the consolidated workflow correction package and explicitly issued Execute.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** Eligible — approved and execution authorized.
- **Required:** Yes
- **Created:** 2026-11-28 00:00 UTC
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

> Are there still holes in the workflow regarding this? Else say I should declare "execute" for you.

> Approve
>
> And my cue "execute" is universal, not just apply for batch execution. Check if workflow already has that clarification.

> Approve
>
> What else? Are there still holes in the workflow regarding this?
>
> Else say I should declare "execute" for you.

> Approve
>
> Do you need my declare now or are there still suggestions you want to recommend?

> Execute

## 2. Subsequent Instructions

- **2026-11-28:** User approved the universal cue clarification, combined cue handling, authorization persistence, scope boundaries, execution audit, recovery and idempotency, false-quiescence prevention, and consolidated canonical Worker correction. User explicitly issued Execute. All these approvals and the cue are authorization for this deliverable.

## 3. Objective and Scope

Consolidate the execution-cue and authorization lifecycle in The Worker so `execute` is a universal execution directive, with context-dependent mechanism, and execution proceeds autonomously through recoverable operations to genuine quiescence within scope. Update the workflow map and any necessary references/contractual surfaces, without duplicating the canonical operating rules.

## 4. Acceptance Criteria

1. Cue recognition follows clear directive intent and ordered message semantics, distinguishing quotation, discussion, hypothetical, negation, and genuine directive use.
2. `execute` is universal; batch is a scheduling mechanism, not the cue's definition or limitation. The directive can initiate, resume, prepare/reconcile and proceed, or otherwise execute eligible work within the authorized scope.
3. Combined cues and operations are processed sequentially, without retroactive authorization or redundant cue resets.
4. Authorization persists through routine preparation, reconciliation, implementation, commit/readback, recovery and task transitions; ends at genuine quiescence, scope exhaustion or real authority boundary.
5. Scope tests distinguish routine execution work from independent objectives and genuine authorization boundaries.
6. Recoverable failures/interruption lead to safe reconciliation, retry/resumption, and duplicate prevention where practical; isolated blockers do not stop independent eligible work.
7. Quiescence cannot be inferred from shallow scans, readback, preparation or reporting alone; reconciled evidence covers actual state and eligible work.
8. The Worker canonically owns these semantics; map and necessary references are aligned and concise.
9. Changed files and tracking are read back. No unperformed validation is claimed.

## 5. Decisions and Progress

- Approved consolidated correction package is to be implemented as one coherent specification, rather than symptom-specific patches.

## 6. State and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** Not yet determined
- **Readback:** Pending
- **Checks:** Not performed
- **Limitations:** No local scripts, tests or lint; no hosted CI inspection.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Execution self-check

Parentage verified under persistent Refactor Skills parent. Scope and approval confirmed. Explicit Execute issued. Canonical owner, reference surfaces, verification/readback and cleanup to be reconciled.

## 10. Handoff

Implement and reconcile the Worker cue semantics, map, references and task tracking; close at implementation/readback quiescence.

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| None | — | None | — |
