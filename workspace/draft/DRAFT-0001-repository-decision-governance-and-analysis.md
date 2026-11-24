---
record_type: decision-draft
template_version: "1.0"
id: "DRAFT-0001"
status: "in-review"
created: "2026-11-24"
updated: "2026-11-24"
proposed_by: "Assistant"
decision_makers:
  - "User"
consulted: []
informed: []
related_drafts: []
related_adrs: []
---

# Establish Draft-to-ADR Governance and Repository Analysis

## Proposal Summary

Adopt a MADR-inspired, approval-gated workflow for durable repository decisions. Use Drafts for proposals and accepted ADRs for decisions. Link implementation tasks to one or more accepted ADRs. Archive implemented ADRs permanently.

Create `workspace/analysis/` for evidence-based repository reviews. Keep it inside `workspace/`, not at the repository root. Use analysis to identify gaps and produce Drafts or ADR-linked tasks. Do not use it as a second CI issue ledger.

This proposal adopts the useful parts of MADR and adds the lifecycle that this repository needs. It does not adopt MADR's optional tools, publication system, release process, or category layout.

The user has already directed creation of `workspace/draft/` and `workspace/adr/`. Their initial README files and templates are in place. This Draft proposes the complete governance model and the next workflow changes. It does not create an accepted ADR. The user must approve this exact Draft before ADR conversion.

## Context and Problem Statement

Repository decisions currently appear in task records, discussions, skills, workflows, and implementation commits. These records serve different purposes. They do not form one complete path from proposal to decision, implementation, and confirmation.

This creates several risks:

- A proposal can become implementation work before the user approves its exact scope.
- A task can lack a stable decision that explains why the work is required.
- An implementation can finish without evidence that it followed the original decision.
- Later work can change a decision without preserving the earlier rationale.
- Repository analysis can identify a gap without a standard path to resolve it.
- New sessions can lose direct links between the current task, the open proposal, and the user's pending decision.

The repository needs one source of truth for each stage. It also needs a clear link between those stages.

MADR provides a useful structure for the decision record itself. Its current `develop` branch uses Context and Problem Statement, Decision Drivers, Considered Options, Decision Outcome, Consequences, Confirmation, Pros and Cons, and More Information. It supports short and extended records by making some detail sections optional. It uses metadata for status and decision roles. It also keeps the title unnumbered and uses consecutive numeric filenames.

The repository needs more than the MADR template. It needs a proposal stage, explicit user approval, implementation tasks, portfolio analysis, and permanent decision archives.

## Goals and Non-Goals

### Goals

- Record durable proposals before implementation.
- Make the user's decision explicit and traceable.
- Preserve rejected, revised, and approved proposals.
- Give every implementation task one or more accepted ADRs.
- Separate approval of a decision from approval to execute a task.
- Confirm that implementation matches the accepted decision.
- Preserve implemented ADRs permanently.
- Make open tasks and Drafts visible in the discussion register.
- Analyze repository quality, decision coverage, and operational gaps on a repeatable basis.
- Keep existing CI diagnostics and the central Ledger as the source of truth for CI findings.

### Non-Goals

- Turn every chat message or minor idea into an ADR.
- Replace task records with ADRs.
- Replace the CI Ledger, lint reports, Actions diagnostics, or task board.
- Introduce automatic approval or automatic implementation.
- Build ADR-management software before a clear need exists.
- Move or rewrite existing task and report archives.
- Mass-migrate existing implementation tasks to new ADRs.
- Make the new decision-governance skill foundational.

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

- **Good:** MADR already has a concise and established decision structure.
- **Good:** The project can start with very few changes.
- **Neutral:** The repository can use MADR's full or minimal template.
- **Bad:** This does not define the required Draft stage or the approval transaction.
- **Bad:** This does not connect implementation tasks to accepted decisions.
- **Bad:** This does not define permanent ADR archival or repository analysis.

### Option 2 — Create a fully custom proposal and decision system

Create new formats and workflows without using MADR as the base.

- **Good:** The system can match every local requirement.
- **Neutral:** The templates can use local field names and statuses.
- **Bad:** It duplicates established decision-writing guidance.
- **Bad:** It increases the risk of inconsistent records.
- **Bad:** It creates more maintenance work for the repository.

### Option 3 — Adopt MADR's decision structure and add repository governance

Use MADR's core structure. Add Draft review, user approval, ADR lifecycle, task linkage, confirmation, analysis, and permanent archival.

- **Good:** The decision record remains recognizable and compact.
- **Good:** The repository gains a complete proposal-to-implementation chain.
- **Good:** Existing task and diagnostics systems keep their current responsibilities.
- **Good:** A focused skill can own the new process.
- **Bad:** The Worker, task template, Ledger renderer, tests, catalog, and archive guidance need coordinated updates.
- **Bad:** Users and the assistant must maintain explicit links and lifecycle metadata.
- **Bad:** Repository analysis needs discipline to avoid duplicate reports and excessive findings.

## Proposed Recommendation

Choose Option 3. Adopt the useful MADR structure and add the controls below.

### 1. Repository layout

Use this layout:

```text
workspace/
├── draft/
│   ├── README.md
│   ├── DRAFT_TEMPLATE.md
│   └── DRAFT-NNNN-short-title.md
├── adr/
│   ├── README.md
│   ├── ADR_TEMPLATE.md
│   └── NNNN-short-title.md
├── analysis/                 # proposed, create after approval
│   ├── README.md
│   ├── ANALYSIS_TEMPLATE.md
│   └── ANALYSIS-YYYYQn.md
├── tasks/
├── task_board.md
├── TASK_TEMPLATE.md
└── discussion.md

archive/
└── adr/
    ├── README.md
    └── NNNN-short-title.md

skills/
└── decision-governance/      # proposed task-specific skill
    └── SKILL.md
```

Keep `workspace/analysis/` inside the workspace. Do not create a root-level `analysis/`.

The workspace holds active planning and coordination records. The root contains distinct product and operating domains. A root-level analysis folder would create another peer domain without a clear owner.

Keep automated diagnostic evidence under `reports/`. Keep analysis as a separate synthesis of repository state and decisions.

### 2. Drafts

Use one Draft for each distinct decision. Split unrelated decisions into separate Drafts. Link related Drafts when they depend on each other.

Use permanent IDs such as `DRAFT-0001`. Keep a separate Draft sequence from the ADR sequence. Use filenames in the form `DRAFT-NNNN-short-title.md`.

Use these statuses:

- `draft` — the assistant is preparing the proposal.
- `in-review` — the assistant has presented it to the user.
- `changes-requested` — the user has requested revisions.
- `approved-for-adr` — the user approved the exact revision.
- `promoted` — an ADR was created from the approved Draft.
- `rejected` — the user rejected the proposal.
- `withdrawn` — the proposal was withdrawn.
- `superseded` — another Draft replaced it before approval.

The Draft template should capture the problem, scope, goals, non-goals, decision drivers, options, recommendation, consequences, risks, affected repository areas, implementation outline, questions, and review history.

The assistant must link every Draft under review from its Open Discussion item in `workspace/discussion.md`.

A Draft is a proposal. It does not authorize implementation.

Preserve a Draft after promotion. Change its status to `promoted` and link the new ADR. Keep rejected and withdrawn Drafts as historical proposal records. Do not create an additional `archive/draft/` folder in the first release.

### 3. Draft approval and ADR creation

The assistant must ask the user to review the complete Draft. The user must approve its exact revision and scope.

Do not treat silence, task creation, a related approval, or a general positive response as approval. Ask one focused question when the approval scope is unclear.

After approval:

1. Fetch and verify the approved Draft.
2. Assign the next unused ADR ID.
3. Create a new ADR from the approved decision and its supporting rationale.
4. Set its decision status to `accepted`.
5. Record the source Draft, decision-maker, approval date, related ADRs, and implementation state.
6. Mark the original Draft `promoted` and link the ADR.
7. Read back both records and their indexes.

Do not create an ADR before explicit approval. Do not silently expand the approved scope during conversion.

### 4. Accepted ADRs

Use a global, permanent ADR sequence. Assign `ADR-0001`, `ADR-0002`, and later IDs only after approval.

Use filenames such as `0001-repository-decision-governance.md`. Keep the Markdown heading unnumbered. Use a flat `workspace/adr/` folder. Use optional metadata tags to support search. Do not create category subfolders or local numbering.

This differs from MADR's category discussion. A single global sequence is easier to reference across skills, tasks, workflows, and reports. A decision can affect several repository areas. Its category may also be unclear when the Draft begins.

Use these decision status values:

- `accepted` — the decision is active.
- `superseded` — a later ADR replaces the decision.
- `deprecated` — the decision is no longer recommended, with no direct replacement.
- `reversed` — the user explicitly reversed the decision.

Track implementation separately:

- `not-started`
- `in-progress`
- `complete`
- `not-required`
- `superseded`

Create an ADR only after approval. Do not create rejected ADRs.

Use these MADR sections:

- Context and Problem Statement
- Decision Drivers
- Considered Options
- Decision Outcome
- Consequences
- Confirmation
- Pros and Cons of the Options
- More Information

Keep Decision Drivers and detailed Pros and Cons optional when they add little value. Require a Confirmation section for every ADR. Put the outcome before detailed option analysis so readers see the decision first.

Use YAML front matter for stable metadata. Record the ADR ID, status, date, decision-makers, proposer, consulted and informed parties, source Draft, related ADRs, supersession links, implementation status, task links, and review triggers.

The ADR record is immutable in its decision content after acceptance. Do not rewrite its Context, Considered Options, or Decision Outcome to hide a later change. Create a new ADR that supersedes the old decision.

Only update lifecycle metadata, task links, review history, and implementation confirmation. Record the reason and evidence for each lifecycle update.

### 5. Implementation tasks

Every new implementation task must reference one or more accepted ADRs. An existing ADR can govern several tasks. One task can implement multiple closely related ADRs.

Add a mandatory `Governing ADR(s)` field to the task template. Include each ADR ID and link. Each task must explain which part of each ADR it implements.

The implementation task must map its acceptance criteria to the ADR's Confirmation criteria. It must record test, review, CI, or operational evidence.

Keep task approval separate from ADR approval. The ADR approves the decision. The task approval authorizes execution of its stated scope under the Worker's existing approval rules.

If no accepted ADR covers proposed implementation work, create a Draft first. Do not move the task to Ready or start implementation until an accepted ADR exists.

The CI Ledger may continue to create Proposed task handoffs from diagnostics. It should set ADR linkage to pending. The Worker must review the finding and decision scope before approval. A Ledger-created task does not authorize implementation.

Do not retrofit old tasks. Existing active tasks remain valid under the instructions that governed them when they started. The current CI Ledger repair task is grandfathered.

Add ADR references to the task board. Keep the ADR IDs concise. Update the Ledger task renderer and hosted tests when the task template changes.

### 6. Confirmation and ADR archival

A completed task does not by itself prove that an ADR was implemented correctly.

The task owner must check every Confirmation criterion. The evidence must show that the implemented repository state follows the accepted decision.

When all linked implementation tasks are Done and all Confirmation criteria pass, set the ADR implementation status to `complete`. Move the ADR to `archive/adr/` without changing its ID or filename.

For an ADR with implementation status `not-required`, confirm that the decision itself is in effect before archival. If a decision is superseded before implementation, resolve its linked tasks and archive it with the superseding ADR link.

Keep archived ADRs permanently. Never add them to `.github/archive-retention-index.json`. The current retention cleaner accepts only exact paths under `archive/tasks/` and `archive/reports/`. It preserves unindexed files and does not scan archive directories.

Add `archive/adr/README.md` and update `archive/README.md` when the archive process is implemented. Treat archived ADRs as immutable. Do not delete them.

### 7. Discussion register

Keep the existing three-section structure and three-report limit.

- **Current Step:** Link every active task record that the assistant is working on. Include multiple task links when required.
- **Open Discussions:** Link each Draft that awaits user review. Put the Draft link in the relevant discussion item.
- **Reports:** Continue to record only verified successful outcomes.

Keep task links and Draft links current. Remove them when the relevant work closes. Do not create links to records that do not exist.

The link requirements are already recorded in the Conversation Mode reference. The new decision skill and Worker updates should make them part of the task and decision lifecycle.

### 8. Repository analysis

Create `workspace/analysis/` after the user approves this Draft. Do not create a root-level `analysis/`.

Use an analysis record to describe repository health at a fixed commit. Record the branch, commit SHA, review date, scope, exclusions, methods, source paths, evidence, limitations, and confidence.

Use the proposed `ANALYSIS_TEMPLATE.md` for each review. Keep the template separate from Drafts and ADRs:

- Analysis identifies the current state.
- Drafts propose a change.
- ADRs record an accepted decision.
- Tasks implement accepted decisions.

Analyze these dimensions:

1. Architecture and boundaries: component ownership, dependencies, duplication, coupling, and unclear interfaces.
2. Workflow integrity: state transitions, approvals, handoffs, error handling, recovery, and closeout.
3. Quality and reliability: tests, validation, coverage, CI behavior, failure patterns, and operational evidence.
4. Data and provenance: schemas, source identity, indexing, retention, migration, and auditability.
5. Security and trust: permissions, secrets handling, dependency integrity, untrusted inputs, least privilege, and safety boundaries.
6. Documentation: discoverability, consistency, broken links, stale instructions, missing formats, and duplicated authority.
7. Operational cost and complexity: unnecessary automation, repeated work, fragile dependencies, runner use, and maintenance burden.
8. User workflow: friction, approval clarity, status visibility, recovery, and control over consequential changes.
9. Decision debt: missing ADRs, orphan tasks, incomplete implementation, failed confirmation, conflicting decisions, and decisions that no longer match repository behavior.

Classify each finding as a strength, gap, risk, contradiction, drift, or opportunity. State its impact and confidence. Link exact evidence. Separate observed facts from hypotheses.

Do not duplicate the CI Ledger. Cite a Ledger finding or report instead of copying its diagnostic. Use analysis to identify cross-cutting patterns and issues that individual reports do not explain.

Do not make code changes from an analysis record. Create a Draft when the finding requires a new decision. Create or update an implementation task when an accepted ADR already covers the work.

Use two review triggers:

- **Periodic:** one repository-wide review each quarter.
- **Event-driven:** after a major architecture or workflow change, a significant incident, repeated failures, a major dependency or platform change, an unsuccessful ADR confirmation, or a user request.

Begin with manual reviews. Do not add a scheduled GitHub Action. Review the analysis cadence after two quarterly cycles.

Keep finalized analysis records in `workspace/analysis/` as historical snapshots. Do not add an `archive/analysis/` family in the first release.

### 9. Skills and repository files to update

Create one task-specific skill named `decision-governance`. It should own Draft, ADR, analysis, approval, review, and archival procedures. Do not make it foundational.

Update these files after the user approves this Draft:

| File | Proposed responsibility |
|---|---|
| `skills/decision-governance/SKILL.md` | Full decision and analysis lifecycle |
| `skills/README.md` | Discoverability and task-specific activation |
| `skills/the-worker/SKILL.md` | Task-to-ADR enforcement, task lifecycle, and ADR archive handoff |
| `skills/the-worker/references/conversation-mode.md` | Keep task and Draft links in the register |
| `workspace/README.md` | Workspace navigation and decision workflow |
| `workspace/TASK_TEMPLATE.md` | Governing ADR references and implementation criteria |
| `workspace/task_board.md` | ADR reference column |
| `reports/triage/scripts/ledger.py` | Render the new task ADR-linkage field |
| `reports/triage/scripts/test_ledger.py` | Validate generated Proposed task linkage |
| `reports/triage/README.md` | Explain pending ADR linkage for new Ledger handoffs |
| `archive/README.md` | Permanent ADR archive rules |
| `archive/adr/README.md` | ADR archive navigation and immutability |
| `skills/document-standards/references/document-type-catalog.md` | New analysis record family and any final format changes |

The workspace Draft and ADR folders, templates, catalog entries, workspace navigation, and discussion link rules are already present. The analysis folder and new skill remain uncreated until approval.

Do not update `skills/SESSION_START.md` or `skills/INITIALIZATION_POLICY.md`. The decision skill is task-specific. The Worker can load it when the task requires decision governance.

### 10. Document and validation order

After approval, implement the accepted ADR in controlled stages:

1. Create ADR-0001 from the approved Draft. Mark DRAFT-0001 promoted.
2. Finalize the decision-governance skill and its activation entry.
3. Update the Worker, task template, board, Ledger renderer, tests, archive guidance, and Document Type Catalog.
4. Create `workspace/analysis/` and its template only if this Draft's analysis recommendation is approved.
5. Update all links and indexes.
6. Read back all changed paths.
7. Use the relevant GitHub-hosted Document Standards and Ledger workflows for validation.
8. Confirm the ADR's implementation criteria with actual evidence.
9. Archive ADR-0001 under `archive/adr/` only after its confirmation gate passes.

Do not run repository scripts locally. Do not wait for or poll GitHub Actions.

## Consequences and Trade-Offs

- **Good:** Every durable decision has a clear proposal, approver, rationale, implementation, and confirmation trail.
- **Good:** The user can review the exact proposal before it becomes an accepted decision.
- **Good:** Tasks have a clear authority and acceptance criteria.
- **Good:** ADRs remain available for long-term analysis.
- **Good:** Repository analysis can identify systemic issues without duplicating operational reports.
- **Neutral:** The repository gains more files and some additional metadata.
- **Neutral:** Analysis reviews require a stable commit snapshot and careful evidence collection.
- **Bad:** Draft approval and ADR linkage add a step before implementation.
- **Bad:** The Worker, Ledger renderer, and tests need coordinated changes.
- **Bad:** The assistant must maintain Draft, ADR, task, and analysis links as records change.

## Risks and Safeguards

| Risk | Impact | Safeguard |
|---|---|---|
| Too many ADRs for trivial work | High process friction | Reuse an applicable accepted ADR. Create a new Draft only when no accepted decision covers the work. |
| ADR approval is mistaken for task approval | Unauthorized execution | Keep task approval separate under The Worker. |
| Draft approval scope is ambiguous | Incorrect ADR conversion | Record the exact Draft revision and approved scope. Ask one focused question when unclear. |
| ADR content changes after acceptance | Decision history becomes unreliable | Use a superseding ADR. Change only lifecycle metadata in the old record. |
| Archived ADRs are deleted by retention | Permanent decision history is lost | Never add ADR paths to the retention index. Keep archive files unindexed. |
| Analysis duplicates CI reporting | Two sources of issue truth | Cite Ledger findings and analyze only cross-cutting implications. |
| Analysis becomes an unbounded audit | High cost and low value | Define scope, commit, exclusions, and timebox. Review a fixed set of dimensions. |
| The process becomes too heavy | Users bypass it | Use short Drafts for simple decisions and optional detail for complex decisions. Review friction after two cycles. |

## Repository Impact

| Area | Immediate state | After approval |
|---|---|---|
| `workspace/draft/` | Created with README and Draft template | Holds proposals and promotion history |
| `workspace/adr/` | Created with README and ADR template | Holds accepted ADRs awaiting confirmation |
| `workspace/analysis/` | Not created | Create if the user approves this recommendation |
| `archive/adr/` | Not yet needed | Permanent archive for implemented ADRs |
| Conversation Mode | Task and Draft link rules updated | Keep links synchronized through all workflow steps |
| Document Type Catalog | Draft and ADR formats registered | Register analysis format if approved |
| Decision governance skill | Not yet created | New task-specific skill |
| Task and Ledger formats | Existing formats retained | Add mandatory ADR linkage and hosted regression tests |

## Questions for the User

1. Do you approve Draft DRAFT-0001, revision 1, as written, including the recommendation to create `workspace/analysis/` and the task-specific `decision-governance` skill? You can also request specific changes instead of approving the complete Draft.

## Review and Approval

- **Revision presented:** Revision 1
- **User decision:** Pending
- **Approved scope:** Not approved
- **Decision date:** Pending
- **Resulting ADR:** Not created

## Discussion and Revision History

| Date | Revision | Change | User feedback / decision |
|---|---|---|---|
| 2026-11-24 | 1 | Initial comprehensive proposal based on MADR and repository integration review | Pending |

## References

- [MADR repository](https://github.com/adr/madr)
- [MADR guidance](https://github.com/adr/madr/blob/develop/docs/index.md)
- [MADR full template](https://github.com/adr/madr/blob/develop/template/adr-template.md)
- [MADR examples](https://github.com/adr/madr/blob/develop/docs/examples.md)
- [MADR status metadata decision](https://github.com/adr/madr/blob/develop/docs/decisions/0008-add-status-field.md)
- [MADR ADR linking decision](https://github.com/adr/madr/blob/develop/docs/decisions/0009-support-links-between-adrs-inside-an-adrs.md)
- [MADR category decision](https://github.com/adr/madr/blob/develop/docs/decisions/0010-support-categories.md)
- [MADR metadata decision](https://github.com/adr/madr/blob/develop/docs/decisions/0013-use-yaml-front-matter-for-meta-data.md)
- [MADR confirmation decision](https://github.com/adr/madr/blob/develop/docs/decisions/0018-use-confirmation-as-heading.md)
- `workspace/draft/README.md`
- `workspace/adr/README.md`
- `workspace/TASK_TEMPLATE.md`
- `skills/the-worker/references/conversation-mode.md`
- `skills/document-standards/references/document-type-catalog.md`
