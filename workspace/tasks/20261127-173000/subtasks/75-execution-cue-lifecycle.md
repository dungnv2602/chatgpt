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
  "state": "awaiting_ci",
  "source_sha": "bac7881838c1c5598f5bf6ecd9905b881c9542e8",
  "policy_revision": "e61129bf855ae3eacd59dc77b53e835ca45bf86f",
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

- Approved consolidated correction package was implemented as one coherent specification, rather than symptom-specific patches.
- Replaced contradictory batch-only cue clauses in the Worker scheduler and execution-loop text. Updated parent/subtask templates and catalog to align the cue lifecycle semantics. Readback confirmed changed owner and tracking files.
- Implementation commits: child record `faf729e5c0c5e911ec083f939269df0ed4f84f1b`; Worker `8fdc1ade2ecd8dc0b3812456700f88ce6b6a44d3` and `7eecebbf305112bff2c7eed7520ec8d61dc0c7d1`; map `8fbd7079815f4d9a4b19c032fb0c195049e59db2`; index `b2c336d7d2593ed66777ee1adc61783c92250a31`; parent `45df0211fe5cd32256957a803b883d478dca23f0`; board `84bc41d143b8aad16f79cf2b5d2a126f1330cc0b`; templates `345f94048b94b8129c25fb46a77ee81f5a56ff22`, `0c105f2e49d6d75d1e8a3f3ba540032212a5369a`; catalog `bac7881838c1c5598f5bf6ecd9905b881c9542e8`.
- Readback verified the Worker, map, templates, catalog, board and task tracking. Local checks/tests/lint and hosted CI inspection were not performed.

## 6. State and Evidence

- **Commit SHA:** `bac7881838c1c5598f5bf6ecd9905b881c9542e8`
- **Changed paths:** `.agent/skills/the-worker/SKILL.md`; `.agent/WORKFLOW_MAP.md`; `.agent/skills/the-worker/assets/TASK_TEMPLATE.md`; `.agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md`; `.agent/skills/the-worker/references/document-type-catalog.md`; parent and subtask records/index; task board.
- **Readback:** Confirmed from branch `gpt` during reconciliation.
- **Checks:** Not performed
- **Limitations:** No local scripts, tests or lint; no hosted CI inspection.

## 7. Completion

- **Status:** Not Done — awaiting exact-SHA validation reconciliation.
- **Completed at:** Not applicable
- **Completion basis:** Implementation and readback criteria satisfied; policy lifecycle awaits CI.

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
