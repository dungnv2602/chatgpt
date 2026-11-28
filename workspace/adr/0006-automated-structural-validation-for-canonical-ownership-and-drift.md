---
record_type: decision-record
template_version: "1.1"
id: "ADR-0006"
status: "accepted"
decision_date: "2026-11-28"
decision_makers:
  - "User"
proposed_by: "Assistant"
consulted: []
informed: []
source_draft: "DRAFT-0007"
source_draft_revision: 1
approved_scope: "Option 2: implement a lightweight deterministic structural validator, diagnostic-only, no automatic repairs or semantic policy interpretation."
related_adrs: ["ADR-0005"]
supersedes: []
superseded_by: null
implementation_status: "not-started"
implementation_tasks: ["20261127-173000-60"]
review_triggers: []
---

# Automated Structural Validation for Canonical Ownership and Drift

## Context and Problem Statement

ADR-0005 establishes canonical instruction ownership and initialization boundaries. Procedural checks are required, but independently repeatable structural checks can detect some observable drift. This decision implements a narrowly scoped validator without reproducing operating policy or interpreting instruction semantics.

## Decision Drivers

- Preserve canonical instruction ownership.
- Detect selected deterministic, observable structural regressions.
- Avoid false-positive prone semantic interpretation.
- Provide concise diagnostics and tests.
- Integrate into existing validation.

## Considered Options

- Manual-only procedural controls.
- Lightweight structural validator.
- Comprehensive semantic policy engine.

## Decision Outcome

Chosen option: "Option 2 — Lightweight structural validator", because it adds repeatable, bounded checks while leaving interpretation and operational authority with The Worker.

### Consequences

- **Good:** Independently checks selected structural invariants.
- **Neutral:** Manual review remains essential; only explicitly encoded checks are covered.
- **Bad:** Pattern and path checks can miss drift and may require maintenance.

### Confirmation

- [ ] Validator checks designated entry and pointer structure, required owner/reference presence, and target-path integrity.
- [ ] Tests cover expected pass/fail cases and diagnostic output.
- [ ] Existing validation workflow invokes the validator and tests.
- [ ] Readback confirms no automatic repairs or semantic policy logic.

## Pros and Cons of the Options

### Manual-only

- **Good:** No new runtime or maintenance.
- **Neutral:** Continues existing manual gates.
- **Bad:** No independent structural regression signal.

### Lightweight structural validator

- **Good:** Repeatable and focused detection with actionable diagnostics.
- **Neutral:** Bounded coverage; manual review remains.
- **Bad:** Maintenance and false-positive/missed-drift risks.

### Comprehensive semantic policy engine

- **Good:** Potentially broad semantic coverage.
- **Neutral:** High complexity and ongoing policy-model maintenance.
- **Bad:** Risks a second authority and unvalidated semantic judgements.

## Implementation Scope

- **In scope:** Deterministic checks of selected file boundaries, pointer/reference structure, and required canonical paths; test fixtures; validation workflow integration; diagnostic-only behavior.
- **Out of scope:** Semantic interpretation, auto-repair, policy duplication, hosted CI review.
- **Tasks:** Refactor Skills child 60.
- **Dependencies:** ADR-0005.
- **Migration / rollback:** Remove validator/test/workflow steps without altering canonical operating rules.

## More Information

- **Source Draft:** DRAFT-0007 Revision 1 (promoted and deleted after verified acceptance).
- **Approved scope:** Option 2, bounded structural validator as described in the source Draft.
- **Related ADRs:** ADR-0005.
- **Evidence:** Repository readback; no prototype or accuracy data.
- **Review trigger:** False-positive patterns, significant architecture changes, or evidence that checks duplicate policy.

## Decision Lifecycle History

| Date | Status / implementation change | Evidence and reason |
|---|---|---|
| 2026-11-28 | accepted | Provisional record read back and completeness reviewed; user approved DRAFT-0007 Revision 1, Option 2. |
