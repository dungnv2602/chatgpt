---
record_type: decision-record
template_version: "1.1"
id: "ADR-0004"
status: "promotion-pending"
decision_date: "2026-11-27"
decision_makers:
  - "User"
proposed_by: "Assistant"
consulted: []
informed: []
source_draft: "DRAFT-0005"
source_draft_revision: 1
approved_scope: "Option 3 and the complete scope of DRAFT-0005 revision 1: task folders with nested subtasks; commit-based CI remediation completion with separate hosted validation metadata; recurrence identity/history retention; ingestion-integrity and report-path hardening; Worker selection preservation; decision-governance gating; active-task migration; and legacy archive compatibility."
related_adrs:
  - "ADR-0003"
supersedes: []
superseded_by: null
implementation_status: "not-started"
implementation_tasks: []
review_triggers:
  - "A recurrence cannot be linked to its prior finding or remediation."
  - "A Ledger ingestion error is reported as success or an incomplete capture is consumed."
  - "Task/subtask completion is conflated with hosted validation."
  - "Task folder migration or archive retention breaks task discoverability or evidence durability."
---

# Task Folders, Subtasks, and Reliable CI Ledger Lifecycle

## Context and Problem Statement

The repository's active task and CI Ledger contracts use flat Markdown task notes and a validation-gated finding lifecycle. This does not implement the user's required model: a task is a folder, subtasks are contained within it, and CI remediation is one typed subtask with its own completion rule.

The static repository review at branch `gpt`, commit `44ff7e7b956209266951a290fd10080418bb2eec`, identified the following concrete mismatches:

- `workspace/tasks/` contains flat Markdown task records; `workspace/TASK_TEMPLATE.md` is version 1.3.
- `.takeout/reports/triage/scripts/ledger.py` generates flat task notes, scans only `workspace/tasks/*.md`, and writes flat paths into the task board.
- Generated task acceptance criteria require successful hosted validation before a finding can be resolved.
- `validate_semantics()` rejects a resolved finding unless successful validation URL and timestamp evidence exist.
- `retire_completed_task_findings()` removes terminal findings from the active Ledger after task archival, risking loss of finding identity and prior remediation links when the same issue recurs.
- Report-processing exceptions are surfaced as warnings while the command can still exit successfully, making partial ingestion appear successful.
- Incomplete Actions captures can be marked processed despite the capture policy requiring them to remain retryable.
- The task-board writer can make the last generated P0 task Current Execution, displacing a task selected by Worker priority-and-age rules.
- Task archive procedures and the Ledger archive reader assume one archived Markdown file per task.
- The generator can mark tasks Approved and In Progress while Governing ADR(s) is Pending. Decision Governance requires accepted ADR linkage before a task becomes Ready or In Progress; standing P0 authorization does not bypass this gate.

There are two existing decision relationships to preserve:

1. Accepted ADR-0003 defines the canonical GitHub Actions diagnostic report artifact layout and explicitly excludes task generation and Ledger task linkage from that decision. ADR-0004 authorizes only the separate task and Ledger lifecycle changes described here; it does not rewrite ADR-0003.
2. DRAFT-0003 proposes broader Area/Project/task architecture and a different boundary in which independently managed subtasks have separate Task IDs and folders. ADR-0004 decides only the task-folder and nested-subtask lifecycle described here. It does not approve DRAFT-0003's broader Area/Project architecture. The Worker must reconcile the two records without silently promoting or implementing DRAFT-0003.

Without a consistent contract, the Worker, generator, Ledger schema, task board, and archive workflow can disagree about whether work is complete. That makes the CI P0 workflow unreliable.

## Decision Drivers

- **Lifecycle clarity:** Parent tasks, child subtasks, CI findings, remediation completion, and hosted validation must have distinct meanings.
- **Recurrence traceability:** A later observation must retain links to the finding's previous resolution and remediation tasks.
- **Ingestion integrity:** Partial failure must not appear as successful complete ingestion.
- **Worker compatibility:** Task selection, approval, progress, archive ownership, and deferred hosted-results review must remain consistent.
- **Evidence durability:** Commit, report, task, and resolution history must remain auditable.
- **Migration safety:** Existing active task IDs and historical archives must remain usable.
- **Recovery:** A new session must locate parent and child work from the board and task folder.
- **Operational cost:** Avoid unnecessary scans, duplicate state, and coupling task completion to an external asynchronous validation system.

## Considered Options

### Option 1 — Keep flat task notes and model subtasks as linked notes

Keep one Markdown file per task under `workspace/tasks/`, add linked child notes and a CI-specific note format, and retain flat board/archive paths. Implement commit-based completion and recurrence retention without changing physical task paths.

- **Good:** Lowest structural migration; existing task links and archive paths remain valid; current Worker readers need fewer path changes.
- **Neutral:** Child notes can have independent acceptance criteria, but parent-child discovery depends on synchronized links and naming conventions.
- **Bad:** A task remains a note, not a folder. Child records are not physically contained by the parent; evidence and work can become scattered. This fails the user's explicit task-folder requirement.
- **Repository fit and evidence:** Strong compatibility with the current generator, board, and archive reader, which all assume flat files. No prototype tested this alternative.
- **Cost, dependencies, and risks:** Lower path migration cost, but still requires lifecycle, recurrence, ingestion, and governance fixes. Link drift can hide incomplete child work; schema-like references and tests reduce but do not eliminate this structural weakness.

### Option 2 — Task folders with hosted-validation-gated CI subtasks

Store each task in `workspace/tasks/<task-id>/task.md` with child records under `subtasks/`. A CI remediation subtask remains open until hosted CI reports success; the parent remains open until all children, including hosted validation, are complete.

- **Good:** Done would imply both committed remediation and successful hosted validation.
- **Neutral:** Worker operations must separate source remediation from asynchronous hosted validation even though both are represented by one subtask status.
- **Bad:** A committed fix cannot be marked complete while hosted validation is pending. Independent work is blocked by an external asynchronous system. This conflicts with the user's selected completion rule and the boundary that hosted results are reviewed only on explicit user trigger.
- **Repository fit and evidence:** It adopts the folder model but preserves the current validation-gated resolution behavior observed in the generator and schema.
- **Cost, dependencies, and risks:** Requires the same structural migration as Option 3 and retains a dependency on hosted workflow availability and results review for every CI subtask closeout. A failed or unavailable hosted run can leave a technically completed remediation open.

### Option 3 — Task folders with commit-complete CI subtasks and separate validation metadata

Store each task in `workspace/tasks/<task-id>/task.md`. Every task folder contains `subtasks/README.md` and zero or more child records. CI remediation is a typed child record. Mark it Done only after the fix commit exists on the intended branch, the Worker verifies the commit and reads back the changed files, and the commit SHA plus concise remediation summary are recorded. Hosted validation is separate metadata with states such as pending, passed, or failed. The parent task becomes Done only when every required child subtask is Done.

- **Good:** Parent outcome and child work have distinct acceptance boundaries. CI remediation can finish without waiting for hosted validation, allowing independent work to continue. Validation remains visible without redefining task completion. A task folder is a stable recovery and archive unit.
- **Neutral:** A parent can be Done while hosted validation metadata is Pending or Failed. Readers must distinguish the two states; this is intentional.
- **Bad:** A commit may later fail hosted validation. The workflow must create or link a new recurrence/remediation record without rewriting the completed historical subtask. Done means authorized remediation work is complete, not that every external validation system is green.
- **Repository fit and evidence:** Matches the user's explicit task-folder hierarchy and selected commit-based completion rule. Static review identified the generator, schema, Worker, board, and archive reader as the main enforcement points. The existing `upsert_finding()` can preserve resolution history on recurrence, but current retirement deletes the identity.
- **Cost, dependencies, and risks:** Highest initial migration cost. Requires coordinated template, generator, schema, test, skill, board, catalog, and archive changes. Commit verification on the intended branch is required. Hosted validation is metadata and remains subject to explicit user-triggered results review.
- **Evidence limitations:** No hosted regression run or production recurrence replay has validated this design. Archive cleanup compatibility for nested paths must be tested before rollout.

### Comparative Assessment

| Criterion | Option 1: Flat notes | Option 2: Folder + validation gate | Option 3: Folder + commit gate |
|---|---|---|---|
| Task-folder requirement | Not met | Met | Met |
| Parent/subtask containment | Linked notes only | Physical child records | Physical child records |
| Commit-based CI completion | Possible | Blocked by hosted validation | Explicit |
| Hosted validation visibility | Separate field possible | Coupled to subtask status | Separate metadata |
| Recurrence traceability | Can be added | Can be added | Retain finding identity and prior task refs |
| Migration complexity | Lower | High | High |
| Fit with user direction | Partial | Conflicts with completion rule | Full |

Option 1 has the lowest migration cost but fails the required physical containment. Option 2 provides containment but keeps the rejected hosted-validation gate. Option 3 has the highest initial cost and is the only option that satisfies both task-folder structure and commit-based CI remediation completion while preserving the user's results-review boundary.

## Decision Outcome

**Chosen option: Option 3 — Task folders with commit-complete CI subtasks and separate validation metadata.**

The user's explicit approval of DRAFT-0005 revision 1 on 2026-11-27 authorizes this decision and its complete scope.

### Consequences

- **Good:** Each task has a stable folder containing its parent record and child subtask records. Parent completion depends on required child completion. CI remediation can finish when its verified commit is recorded, without waiting for hosted validation. Finding identity and resolution history remain available for recurrence.
- **Neutral:** Hosted validation can remain Pending or Failed after remediation is Done. Task completion and validation status must be displayed and interpreted separately.
- **Bad:** Active task paths, board links, generator, schema, tests, documentation, and archive handling require coordinated migration. A later recurrence becomes a new remediation record and does not retroactively reopen the old completed record.

### Normative Lifecycle Rules

1. A task is a folder: `workspace/tasks/<task-id>/`.
2. Every task folder contains authoritative `task.md` and a `subtasks/` directory with an index (`subtasks/README.md`), even when there are no child records.
3. Every subtask has its own stable ID, type, status, acceptance criteria, evidence, and completion record.
4. The parent task owns the overall outcome. It becomes Done only when every required subtask is Done.
5. A CI remediation subtask becomes Done only after the remediation is committed to the intended branch, the Worker verifies the commit and reads back the changed files, and the commit SHA and remediation summary are recorded.
6. Hosted validation is separate metadata (for example Pending, Passed, or Failed). It is not a prerequisite for CI remediation subtask Done and does not retroactively change that subtask's completion.
7. A later CI observation is a new recurrence/remediation record linked to the prior finding and remediation. Do not rewrite a completed prior remediation as incomplete merely because later validation fails or the issue recurs.
8. Ledger `task_refs` identify stable parent Task IDs. The Ledger retains terminal finding identity and resolution history after task archival; archiving must not delete a finding's identity or prior task references.
9. When a resolved finding recurs, preserve its previous resolution in `resolution_history`, reopen the same finding identity, and append the new parent task reference. If the prior task is no longer active, create a new parent folder and CI subtask.
10. Report-ingestion errors must be surfaced as errors and produce a non-zero command result. Safe partial progress may be published, but failed reports remain retryable.
11. Incomplete or pre-finalizer Actions captures remain unprocessed and eligible for retry.
12. Validate report-index identifiers before constructing paths. Missing indexed complete reports and unsafe identifiers fail closed.
13. Creating a new P0 task must not displace a valid Current Execution task selected under Worker priority-and-age rules.
14. A Ledger-generated implementation task with Governing ADR(s) Pending remains Proposed and is not executable. The Worker must link an accepted ADR before moving it to Ready or In Progress. P0 priority does not bypass decision governance.
15. New folder archives store the complete parent folder at `.archive/task/<task-id>/`, with `task.md` as the indexed parent record. Historical flat archived task files remain immutable and readable.
16. Preserve existing report capture classification, error eligibility, lint baselines, report retention, shared report-writer architecture, and the explicit user-triggered hosted-results-review boundary.

### Confirmation

The implementation is complete only when the repository provides observable evidence for all of the following:

- [ ] Every active task is a folder containing `task.md` and `subtasks/`.
- [ ] Every task folder has a subtask index. Every child record has an ID, type, status, acceptance criteria, evidence, and completion record.
- [ ] The Ledger generates a parent task folder and a CI remediation subtask, not a flat note.
- [ ] Ledger `task_refs` identify stable parent Task IDs; parent Done is blocked while any required child is not Done.
- [ ] A CI remediation subtask can be Done with a verified commit SHA and remediation summary while hosted validation remains Pending.
- [ ] The Ledger accepts commit-based resolution without hosted validation; optional validation metadata is schema-validated.
- [ ] Recurrence reopens the same finding identity, preserves the prior resolution in `resolution_history`, and creates a new task/subtask when the prior task is no longer active.
- [ ] Task archival does not delete finding identity or prior task references.
- [ ] Malformed indexed reports produce visible errors and a non-zero command result; safe partial changes remain publishable and failed reports remain retryable.
- [ ] Incomplete or pre-finalizer Actions captures are not marked processed.
- [ ] Missing indexed complete reports and unsafe run identifiers fail closed.
- [ ] New P0 task creation does not displace a valid Worker-selected Current Execution task.
- [ ] New folder archives and legacy single-file archives are both read correctly by the Ledger and retention workflow.
- [ ] Generated tasks with Governing ADR(s) Pending remain Proposed and cannot execute until accepted ADR linkage exists.
- [ ] The hosted Ledger regression suite and Document Type Catalog validation pass. No test result is claimed until observed.
- [ ] Active task folders, board links, discussion register, and archive retention index agree after migration and closeout.

## Pros and Cons of the Options

### Option 1 — Flat task notes with linked child notes

- **Good:** Lowest migration cost and maximum compatibility with current flat-file consumers.
- **Neutral:** Independent child completion is possible but depends on manually maintained references.
- **Bad:** Does not satisfy physical task/subtask containment and leaves task evidence fragmented.

### Option 2 — Task folders with validation-gated CI subtasks

- **Good:** CI subtask Done would imply hosted validation success as well as committed remediation.
- **Neutral:** A single status combines local remediation and external validation.
- **Bad:** Blocks completion and independent work on asynchronous hosted results; conflicts with the user's approved completion rule and review boundary.

### Option 3 — Task folders with commit-complete CI subtasks

- **Good:** Meets the task-folder requirement, separates parent and child completion, enables commit-driven remediation completion, and preserves recurrence history.
- **Neutral:** Done remediation can coexist with Pending or Failed hosted validation; consumers must keep those states distinct.
- **Bad:** Requires coordinated migration and may leave external validation pending after task completion.

## Implementation Scope

- **In scope:** Task and subtask templates; active flat-task migration; task-board paths; Worker parent/child lifecycle and folder archive closeout; CI Ledger task generation, schema, recurrence, resolution, and ingestion integrity; GitHub Actions remediation guidance; Document Type Catalog; workspace and triage documentation; regression tests; legacy archive compatibility.
- **Out of scope:** Rewriting historical archived task records; changing report capture classification, report eligibility, lint baselines, report retention, or the shared report-writer architecture; automatically polling, dispatching, rerunning, or inspecting hosted CI results; approving or implementing DRAFT-0003's broader Area/Project architecture; weakening tests or protections; changing ADR-0003's report-artifact decision.
- **Tasks:** Create one implementation task after ADR acceptance. It must link to ADR-0004 and map every applicable Confirmation criterion to acceptance criteria. Do not execute implementation before the accepted ADR exists.
- **Dependencies:** ADR-0003 remains authoritative for canonical report artifact layout. Decision Governance and Document Standards govern task/ADR format and execution approval. DRAFT-0003 remains a separate in-review proposal and must not be treated as accepted.
- **Migration / rollback:** Migrate only active flat task records to ID folders while preserving task IDs and record content; update board and relative links; keep historical archives immutable. Retain dual readers for new folder archives and legacy flat archives. Roll back by restoring the previous active paths and board references from the pre-migration commit while retaining immutable archive history. Do not delete or overwrite historical archive records.

## More Information

- **Source Draft:** DRAFT-0005, revision 1, approved by the user on 2026-11-27. The source Draft is deleted after successful promotion; its ID and revision remain here as provenance.
- **Approved scope:** Option 3 and all normative lifecycle rules, Confirmation criteria, migration boundaries, and Ledger integrity repairs in DRAFT-0005 revision 1.
- **Related ADRs:** ADR-0003 defines diagnostic report artifact layout; this ADR authorizes separate task/Ledger lifecycle changes without altering ADR-0003. DRAFT-0003 is a related proposal only, not an accepted ADR.
- **Evidence:**
  - `.takeout/reports/triage/scripts/ledger.py`, branch `gpt`, reviewed commit `44ff7e7b956209266951a290fd10080418bb2eec`: flat task generation and parsing, validation-gated resolution, finding retirement, ingestion error handling, report-index path use, and Current Execution update behavior.
  - `.takeout/reports/triage/ledger-schema.json`, schema 1.5.0 at the same commit: resolved finding validation requirements.
  - `.takeout/reports/triage/scripts/test_ledger.py`, same commit: existing regression expectations for flat task files and finding retirement. Tests were not run during Draft assessment.
  - `.agent/skills/ci-ledger/SKILL.md`, `.agent/skills/the-worker/SKILL.md`, `.agent/skills/github-actions/SKILL.md`: current lifecycle and ownership contracts.
  - `workspace/TASK_TEMPLATE.md`, `workspace/task_board.md`, `workspace/README.md`: active task and board conventions.
  - `.agent/skills/decision-governance/SKILL.md`: accepted ADR prerequisite for implementation tasks and Ledger handoff rules.
  - `workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md`: related unapproved architecture proposal.
  - `workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md`: accepted report-artifact decision and scope exclusion.
  - User approval in this conversation on 2026-11-27: approval of DRAFT-0005 revision 1.
- **Review trigger:** Any recurrence-link loss, partial-ingestion false success, incomplete-capture consumption, completion/validation conflation, task discoverability failure, or archive-retention regression.

## Decision Lifecycle History

| Date | Status / implementation change | Evidence and reason |
|---|---|---|
| 2026-11-27 | Promotion pending | User approved DRAFT-0005 revision 1 and its full scope. Provisional ADR created for completeness comparison and read-back. |
