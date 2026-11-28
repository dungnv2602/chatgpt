---
record_type: decision-record
template_version: "1.1"
id: "ADR-0005"
status: "accepted"
decision_date: "2026-11-28"
decision_makers:
  - "User"
proposed_by: "Assistant"
consulted: []
informed: []
source_draft: "DRAFT-0006"
source_draft_revision: 1
approved_scope: "Option 3, including the user's additional requirement to update associated templates. Session Start becomes a cue guard and pointer. Conversation Mode contains presentation settings only. The Worker becomes the single operating authority and initialization orchestrator. Existing focused references and specialist skills retain detailed procedures. Secondary initialization policy and skills index become navigation. Templates are updated to reflect the ownership hierarchy, execution self-check, and associated operational boundaries. Preserve the approved safeguards and behavior in DRAFT-0006 Revision 1."
related_adrs: []
supersedes: []
superseded_by: null
implementation_status: "complete"
implementation_tasks:
  - "20261127-173000-59"
review_triggers:
  - "A duplicate or conflicting operating rule appears in an entry file."
  - "Initialization, approval, or execution gates change."
  - "Associated templates no longer match the Worker-owned operating contract."
---
# Lean Session Start and Conversation Mode

## Context and Problem Statement

The repository distributes operating rules across Session Start, Conversation Mode, the Worker, initialization policy, indexes, templates, and references. Some instructions conflict and others repeat the same contract. The approved refactor makes The Worker the sole operational authority and reduces entry documents to their intended boundaries.

## Decision Drivers

- Remove conflicting and duplicated operational instructions.
- Keep initialization conditional and cue-based.
- Preserve required startup, safety, approval, scheduling, blocker, cleanup, and closeout behavior.
- Keep specialist details progressively loaded and owned by the relevant reference or skill.
- Update associated templates to prevent new records from reintroducing the old structure.
- Verify all changes by remote readback without inspecting hosted CI results.

## Considered Options

### Option 1 — Retain distributed policy
Keep current documents and repair individual contradictions. This leaves multiple owners and future drift risk.

### Option 2 — Consolidate everything into one oversized Worker file
Move every procedure into the Worker body. This removes duplicate entry policy but increases loading and maintenance burden and weakens progressive disclosure.

### Option 3 — Worker authority with focused references (approved)
The Worker owns operating policy and orchestration. Session Start is a cue guard and pointer. Conversation Mode contains settings only. Existing references and specialist skills retain focused details. Secondary files and templates are reconciled to this ownership model.

## Decision Outcome

Chosen option: Option 3, including associated-template reconciliation, as approved by the user on 2026-11-28.

### Consequences

- Good: clear ownership, fewer conflicts, explicit execution gates, improved drift detection.
- Neutral: The Worker remains the central orchestrator and routes detailed work to focused references.
- Bad: initial reconciliation requires multiple document and template updates. Some specialist initialization details move to focused references.

### Confirmation

- [x] Session Start contains only cue guard and pointer.
- [x] Conversation Mode contains presentation settings only.
- [x] Worker owns operational authority, mandatory self-check, contradiction detection, and execution gates.
- [x] Existing novelist/drawing procedures remain available through focused Worker references.
- [x] Initialization policy/navigation, skills index, catalog, board, discussion contract, and associated templates align.
- [x] Readback verifies every changed path.

## Implementation Scope

- In scope: entry files, Worker and references, associated templates, navigation/catalog records, task records, board, and discussion register reconciliation.
- Out of scope: unrelated skill refactors, local scripts/tests/lint, hosted CI review.
- Task: child 59 under Refactor Skills.
- Rollback: restore the prior branch content if readback identifies a material omission.

## More Information

- Source Draft: DRAFT-0006 Revision 1, approved.
- Additional user instruction: update associated templates.
- Approval and execution cue: user explicitly approved and instructed execution on 2026-11-28.


### Implementation closeout (2026-11-28)

- **Status:** Complete. Child 59 implementation reconciled under explicit user approval of DRAFT-0006 Revision 1, Option 3, including associated-template updates.
- **Evidence:** Repository progress and discussion records document updates to entry files, Worker ownership gates, specialist initialization references, navigation, catalog, templates, task evidence, and readback. The source Draft is retired and ADR-0005 is the canonical accepted record.
- **Limitations:** No local tests, scripts, lint, or hosted CI results were inspected for this closeout. Readback and tracking evidence do not establish runtime validation.
