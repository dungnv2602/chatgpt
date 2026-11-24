---
record_type: decision-record
template_version: "1.0"
id: "ADR-0001"
status: "accepted"
decision_date: "2026-11-24"
decision_makers:
  - "User"
proposed_by: "Assistant"
consulted: []
informed: []
source_draft: "DRAFT-0001"
related_adrs: []
supersedes: []
superseded_by: null
implementation_status: "in-progress"
implementation_tasks:
  - "20261124-103354"
review_triggers:
  - "A Confirmation criterion fails."
  - "A later user instruction changes decision-governance scope."
  - "The repository archive or task model changes."
---

# Establish Draft-to-ADR Governance and Repository Analysis

## Context and Problem Statement

Repository decisions currently appear in task records, discussions, skills, workflows, and implementation commits. These records serve different purposes. They do not form one complete path from proposal to decision, implementation, and confirmation.

This creates several risks:

- A proposal can become implementation work before the user approves its exact scope.
- A task can lack a stable decision that explains why the work is required.
- An implementation can finish without evidence that it followed the original decision.
- Later work can change a decision without preserving the earlier rationale.
- Repository analysis can identify a gap without a standard path to resolve it.
- New sessions can lose direct links between the current task, the open proposal, and the user's pending decision.

MADR provides a useful structure for the decision record. This repository also needs a proposal stage, explicit user approval, implementation tasks, repository analysis, and permanent decision archives.

The user approved DRAFT-0001 revision 1 on 2026-11-24. The approval covers the complete Draft, including `workspace/analysis/` and the task-specific `decision-governance` skill. This ADR records that accepted decision. It does not include DRAFT-0002 or its separate planning proposal.

## Decision Drivers

- The user remains the final decision-maker.
- The record must preserve why a choice was made, not only what changed.
- A task must have a traceable decision basis before implementation.
- Draft review must be simple and visible.
- Accepted decisions must remain stable and auditable.
- The process must work with GitHub Markdown and existing repository tools.
- The process must not duplicate existing ledgers or create unnecessary automation.
- Repository analysis must use verifiable evidence and clear scope.
- The process must remain easy to use as the repository grows.

## Considered Options

### Option 1 — Adopt MADR with no repository-specific lifecycle

Use the MADR template and store ADRs in a decision folder. Keep the current task, discussion, archive, and analysis procedures unchanged.

- **Good:** MADR already has a concise decision structure.
- **Neutral:** The project can use full or minimal records.
- **Bad:** This does not define Draft approval, task linkage, confirmation, permanent archival, or repository analysis.

### Option 2 — Create a fully custom proposal and decision system

Create new formats and workflows without using MADR as the base.

- **Good:** The system can match every local requirement.
- **Neutral:** Templates can use local field names and statuses.
- **Bad:** It duplicates established decision-writing guidance and increases maintenance.

### Option 3 — Adopt MADR's decision structure and add repository governance

Use MADR's core structure. Add Draft review, user approval, ADR lifecycle, task linkage, confirmation, analysis, and permanent archival.

- **Good:** The decision record remains recognizable and compact.
- **Good:** The repository gains a complete proposal-to-implementation chain.
- **Good:** Existing task and diagnostics systems keep their current responsibilities.
- **Good:** A focused skill can own the new process.
- **Bad:** The Worker, task template, Ledger renderer, tests, catalog, and archive guidance need coordinated updates.
- **Bad:** The user and assistant must maintain explicit links and lifecycle metadata.
- **Bad:** Repository analysis needs discipline to avoid duplicate reports and excessive findings.

## Decision Outcome

Chosen option: **Option 3 — Adopt MADR's decision structure and add repository governance.**

Adopt the useful MADR structure. Do not adopt its optional tooling, publication system, release process, or category layout.

### Consequences

- **Good:** Every durable decision has a proposal, approver, rationale, implementation, and confirmation trail.
- **Good:** The user reviews the exact proposal before it becomes an accepted decision.
- **Good:** Tasks have a clear decision basis and acceptance criteria.
- **Good:** ADRs remain available for long-term analysis.
- **Good:** Repository analysis can identify systemic issues without duplicating operational reports.
- **Neutral:** The repository gains more files and metadata.
- **Neutral:** Analysis reviews require a fixed commit snapshot and evidence.
- **Bad:** Draft approval and ADR linkage add a step before implementation.
- **Bad:** The Worker, Ledger renderer, and tests need coordinated maintenance.
- **Bad:** The assistant must maintain Draft, ADR, task, and analysis links.

### Confirmation

The implementation task must collect evidence for every criterion.

- [x] The user approved DRAFT-0001 revision 1 and its complete scope.
- [x] ADR-0001 records the accepted decision and links to its source Draft.
- [x] Draft and ADR lifecycle instructions are implemented and read back.
- [x] The task template and task board require and display governing ADR references.
- [ ] The Ledger creates Proposed task handoffs with ADR linkage marked pending.
- [x] The decision-governance skill, workspace analysis area, and permanent ADR archive guidance exist.
- [x] The Document Type Catalog contains all required active and reserved path rules.
- [ ] Relevant hosted Document Standards and Ledger validation pass.
- [ ] The implementation task is complete and archived. Then move this ADR to `archive/adr/`.

## Pros and Cons of the Options

### Option 1 — Adopt MADR without local lifecycle rules

- **Good:** Low initial change cost.
- **Neutral:** Familiar record format.
- **Bad:** Missing proposal approval, task linkage, confirmation, permanent archive, and analysis controls.

### Option 2 — Build a fully custom system

- **Good:** Exact local fit.
- **Neutral:** No external format dependency.
- **Bad:** Duplicates established guidance and creates more maintenance.

### Option 3 — Adopt MADR structure with repository governance

- **Good:** Reuses established decision structure.
- **Good:** Preserves the current Worker, board, and Ledger ownership model.
- **Neutral:** Adds explicit records and lifecycle metadata.
- **Bad:** Requires coordinated documentation and renderer updates.

## Implementation Scope

- **In scope:** Draft and ADR lifecycle, explicit approval, task-to-ADR linkage, confirmation, permanent ADR archival, repository analysis, and one task-specific decision-governance skill.
- **Out of scope:** The separate DRAFT-0002 planning proposal, host-specific hooks, automatic approval, scheduled analysis automation, a root-level `analysis/` folder, and changes to foundational initialization.
- **Tasks:** [20261124-103354 — Establish draft-to-ADR governance and repository analysis workflow](../tasks/20261124-103354-establish-draft-adr-governance-and-repo-analysis-workflow.md). This is the bootstrap implementation task authorized by the user's original request. It now references ADR-0001.
- **Dependencies:** None.
- **Migration / rollback:** Do not mass-migrate existing tasks. Preserve legacy records. Revert only the implementation changes if a later approved decision supersedes this ADR. Preserve this ADR and create a superseding record for any decision change.

## More Information

- **Source Draft:** [DRAFT-0001 — Establish Draft-to-ADR Governance and Repository Analysis](../draft/DRAFT-0001-repository-decision-governance-and-analysis.md), revision 1, approved 2026-11-24.
- **Related ADRs:** None.
- **Evidence:** `workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md`, `workspace/TASK_TEMPLATE.md`, `workspace/task_board.md`, `reports/triage/scripts/ledger.py`, `reports/triage/scripts/test_ledger.py`, and `skills/document-standards/references/document-type-catalog.md`.
- **Review trigger:** Review this decision when confirmation fails, when the user changes the governance model, or when task or archive ownership changes.

## Decision Lifecycle History

| Date | Status / implementation change | Evidence and reason |
|---|---|---|
| 2026-11-24 | Accepted | The user approved DRAFT-0001 revision 1 in this conversation. |
| 2026-11-24 | Implementation in progress | Core governance files are committed and read back. Hosted Document Standards and Ledger validation remain pending after a catalog filename-pattern correction. |
