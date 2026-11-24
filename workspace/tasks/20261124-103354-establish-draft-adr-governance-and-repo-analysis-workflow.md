# Task: Establish draft-to-ADR governance and repository analysis workflow

## Metadata

- **Template version:** 1.2
- **ID:** 20261124-103354
- **Created:** 2026-11-24 10:33 UTC
- **Updated:** 2026-11-24 10:33 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved to study MADR, create the requested `workspace/draft/` and `workspace/adr/` structures, and prepare a comprehensive proposal. Detailed governance rules and optional analysis structure remain subject to draft review and approval.
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** 20261123-225745 — Repair CI ledger task generation workflow
- **Ledger group:** None
- **Archived:** No

<!-- Lifecycle invariant: keep the active record In Progress and Archived: No until the final archive copy is written and read back. Set Done/Cancelled and Archived: Yes only in the initial archive copy. Check its complete content and commit metadata before deleting the active path. After creation, treat the archive copy as immutable. Delete the active record only after archive verification. Move the board row to Historical only after the active path is absent and the board can link the exact archive path and archive commit. If any step fails, keep the task open and reconcile the partial state without rewriting the archive. -->

## 1. Original Request

Start session 

Here's the link: https://github.com/adr/madr 

Study it thoroughly and take inspirations from it. I would expect the result is a bunch of new templates, an update for our workflow and which skills to update, or even a new skill. 

Create a /draft and an /adr folder inside workspace. From now on, we document your proposals and my decisions following this format. First a draft, then an ADR. When a draft is finalized and approved, you transform it into an ADR. A task should take one or more ADR to implement. 

From now on, in discussion.md, besides what we agreed on, Current Step section will have links to the tasks you're working on. Open Discussion section will have links to the drafts we're working on. 

When an ADR is implemented, it moved to 
/archive/adr. They should not be deleted. ADR records represent our decisions building the repo, worthy of analysis periodically. 

How to analyze and which gaps or improvements to look for, I let you to brainstorm. Should we create another /analysis folder for repo analysis, and where should we put it, in root folder or inside/workspace. 

Here is my base ideas, expand on this. Better yet, try to utilize the best out of this. Make it exhaustive, comprehensive, so we will have a solid workflow. If you say you want to adopt it entirely, feel free to tell me, and explain. 

## 2. Subsequent Instructions

- **2026-11-24:** The user explicitly authorized this session and requested a study of MADR at `https://github.com/adr/madr`.
- **2026-11-24:** The user directed creation of `workspace/draft/` and `workspace/adr/`.
- **2026-11-24:** From now on, proposals move through Draft → user review → approved ADR. Implementation tasks must reference one or more ADRs.
- **2026-11-24:** The Current Step section of `workspace/discussion.md` must link the active task records. Open Discussions must link the drafts under review.
- **2026-11-24:** Implemented ADRs move to `archive/adr/` and must not be deleted.
- **2026-11-24:** The location and need for a repository-analysis folder remain open for recommendation.

## 3. Objective

Study MADR and design a comprehensive, low-ambiguity decision-management workflow for proposals, architecture decisions, implementation tasks, repository analysis, review, and permanent ADR archiving. Prepare an initial draft for the user's review.

## 4. Requirements

1. Study the MADR repository, including its decision template, status model, numbering, metadata, guidance, and lifecycle practices.
2. Separate proposals, accepted decisions, implementation work, and repository analysis. Keep clear ownership and status transitions.
3. Create the requested workspace draft and ADR structures after their canonical formats and Markdown catalog coverage are defined.
4. Define copy-ready templates for drafts, accepted ADRs, implementation tasks, and periodic repository analyses where justified.
5. Define a stable ADR ID and filename convention. Prevent ID reuse and preserve decision history.
6. Require each implementation task to reference one or more accepted ADRs, including its implementation scope and acceptance criteria.
7. Define how a draft becomes an ADR only after explicit user approval. Preserve the finalized proposal and decision history.
8. Define ADR statuses, supersession links, amendment rules, reversals, and immutable archive behavior.
9. Move implemented ADRs to `archive/adr/`. Preserve them permanently and exclude them from the 90-day task/report retention workflow.
10. Extend `workspace/discussion.md`: Current Step links to active tasks. Open Discussions links to active drafts. Keep its three-section structure and report limit unless the proposal justifies a reviewed change.
11. Determine which existing skills and owner documents need updates. Consider The Worker, Document Standards, the task template and board, workspace README, archive policy, and whether one focused new skill is justified.
12. Evaluate a repository-analysis area. Recommend its location, scope, template, cadence, evidence rules, and link to ADRs without creating a duplicate issue ledger.
13. Keep CI/report findings, maintenance analysis, architectural proposals, and active implementation tasks distinct. Define clear handoffs between them.
14. Do not adopt the entire MADR design blindly. Identify useful practices, repository-specific adaptations, conflicts, and omitted safeguards.
15. Record design choices as Proposed until the user approves the draft. Do not create an Accepted ADR or implement optional design choices before approval.
16. Follow Document Standards and the repository writing policy. Update the catalog, owners, and path coverage in the correct order.
17. Read back all changed paths. Verify folder structures, links, numbering, statuses, and archive-retention exclusions.
18. Do not run repository scripts or tests locally. Use relevant GitHub-hosted validation only when it becomes naturally available. Do not poll CI.

## 5. Decisions

- **Approved:** Study and adapt MADR.
- **Approved:** Create `workspace/draft/` and `workspace/adr/`.
- **Approved:** Require explicit user approval before converting a finalized draft into an ADR.
- **Approved:** Require implementation tasks to reference one or more ADRs.
- **Approved:** Move implemented ADRs to permanent `archive/adr/` storage.
- **Approved:** Link active tasks in Current Step and active drafts in Open Discussions.
- **Proposed:** Place a repository-analysis area under `workspace/analysis/` rather than at repository root. Await the user's review of the initial draft.
- **Proposed:** Use one initial governance ADR as the bootstrap decision. The current task is authorized directly by the user's instruction. After the bootstrap decision, new implementation tasks require accepted ADR references.

## 6. Progress Log

### 2026-11-24 10:33 UTC — Create the tracked governance task

- **Action:** Read the session-start procedure, foundational skills, workspace README, task board, task template, and current conversation-mode rules. Created this task record and selected it for current execution.
- **Result:** The current CI Ledger repair task remains In Progress and is checkpointed. This governance task is a separate P1 task. Its scope includes the MADR study and the initial proposal. No MADR material or repository governance files have been changed yet.
- **References:** `skills/SESSION_START.md`; `skills/the-worker/SKILL.md`; `skills/the-worker/references/conversation-mode.md`; `skills/asd-ste100/SKILL.md`; `skills/github-actions/SKILL.md`; `skills/document-standards/SKILL.md`; `workspace/README.md`; `workspace/task_board.md`; `workspace/TASK_TEMPLATE.md`.
- **Next:** Study MADR and inspect its canonical templates and lifecycle before writing the initial proposal.

## 7. Current State

The request is tracked as a separate P1 task. The user approved a MADR study and the requested workspace folders. Detailed workflow rules and the optional analysis area remain open for review.

## 8. Remaining Work

- Study MADR and collect its core conventions.
- Prepare the architecture proposal and templates.
- Define the document-family coverage and owner updates.
- Create requested folders and first draft only after catalog and template setup.
- Present the draft for user review. Do not create an accepted ADR until approval.

## 9. Next Actions

1. Inspect the MADR repository and official guidance.
2. Compare MADR practices with the existing task, report, archive, and discussion workflows.
3. Draft the complete proposal, including whether `workspace/analysis/` is justified.
4. Define canonical templates and catalog coverage before creating first records.
5. Create the requested folder structures and the initial draft.
6. Stop for explicit user review and approval before ADR conversion and implementation of optional policy changes.

## 10. References

- External source: `https://github.com/adr/madr`
- `skills/SESSION_START.md`
- `skills/the-worker/SKILL.md`
- `skills/the-worker/references/conversation-mode.md`
- `skills/document-standards/SKILL.md`
- `skills/document-standards/references/document-type-catalog.md`
- `workspace/README.md`
- `workspace/TASK_TEMPLATE.md`
- Related task: `20261123-225745`

## 11. Verification

- **Check:** Foundational initialization, workspace operating rules, active task state, and task template.
- **Method:** Retrieved the exact canonical files from branch `gpt`.
- **Result:** Required foundational skills were available. The CI Ledger task remains active. No duplicate task for the ADR workflow was present in the current board.
- **Limitations:** MADR study and the initial proposal remain incomplete.

## 12. Handoff Instructions

Continue on branch `gpt`. Study MADR before choosing templates or copying practices. Keep proposals in Draft status until the user approves them. Convert a draft into an ADR only after explicit approval. Do not implement optional governance choices merely because they appear in a proposal. Once approved, link every implementation task to its accepted ADRs. Preserve implemented ADRs permanently under `archive/adr/`.

## 13. Ledger Findings

_No Ledger findings are linked to this task._

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
