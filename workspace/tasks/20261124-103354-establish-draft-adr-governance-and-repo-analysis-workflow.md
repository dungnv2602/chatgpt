# Task: Establish draft-to-ADR governance and repository analysis workflow

## Metadata

- **Template version:** 1.2
- **ID:** 20261124-103354
- **Created:** 2026-11-24 10:33 UTC
- **Updated:** 2026-11-24 10:45 UTC
- **Priority:** P1
- **Status:** Blocked
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

### 2026-11-24 10:45 UTC — Create the first governance Draft

- **Action:** Created the Draft and ADR folder contracts and templates. Updated workspace navigation, the discussion-register rules, and Document Type Catalog 1.11. Read back all seven changed paths. Created DRAFT-0001 from the canonical Draft template and activated its previously Reserved path rule.
- **Result:** The repository now has `workspace/draft/` and `workspace/adr/` with README files and copy-ready templates. The catalog records both document families. DRAFT-0001 is linked in Open Discussions and remains `in-review`. No ADR has been created. The optional analysis folder and new decision-governance skill remain proposals for user review.
- **Commit:** Folder, template, workspace, register, and catalog scaffolding [a53401d](https://github.com/dungnv2602/chatgpt/commit/a53401d489d9a1acbaff71211f9eee7e716c1659). The DRAFT-0001 record and Active path rule are in the current commit.
- **Next:** Wait for the user's review. Do not create ADR-0001 or implement optional workflow changes without approval.

### 2026-11-24 10:38 UTC — Complete MADR and repository integration study

- **Action:** Read MADR's current `develop` documentation, README, full and minimal templates, examples, changelog, and its own ADRs covering identifiers, status, metadata, categories, neutral arguments, consequences, confirmation, links, and template evolution. Inspected the local Document Type Catalog, workspace and task formats, Ledger task renderer/tests, archive policy, and exact archive-retention validator.
- **MADR findings:** MADR defines one decision per record. Its full template uses Context and Problem Statement, Decision Drivers, Considered Options, Decision Outcome, Consequences, Confirmation, Pros and Cons, and More Information. It supports short and extended records by making detail sections optional. It puts the outcome before detailed pros/cons. Its metadata can carry status, date, decision-makers, consulted, and informed. It uses consecutive numeric filenames with lowercase dashed titles and keeps the title itself unnumbered. It places related ADR links in More Information. It supports neutral arguments and requires a confirmation method for checking the implemented decision. MADR also maintains full, minimal, bare, and bare-minimal templates. The current branch studied was `develop`, tree `ba75bb1b20d42af5746b246ad348c202419ae681`.
- **Local integration findings:** The Document Type Catalog requires narrow Markdown path rules. New record families start Reserved and become Active in the same commit as their first record. The Ledger renderer replaces exact Task Template v1.2 text and its regression suite checks the generated format. Any new mandatory ADR field must update the task template, renderer, and hosted tests together. The archive cleanup script validates only indexed paths under `archive/tasks/` and `archive/reports/`. It preserves unindexed files and never scans archive directories. Therefore `archive/adr/` can remain permanent when ADRs are never added to the 90-day retention index.
- **Design direction:** Use Drafts for proposals and Accepted ADRs for approved decisions. Keep decision status separate from implementation status. Require explicit approval of the exact draft before ADR creation. Preserve the promoted draft as provenance. Keep accepted decisions immutable except for lifecycle metadata. Use a global ADR sequence and a flat folder to avoid category and local-ID ambiguity. Link implementation tasks to accepted ADRs. Keep CI findings in the existing Ledger rather than duplicating them in repository analysis.
- **Analysis recommendation:** Create `workspace/analysis/`, not a root-level `analysis/`. Analysis is repository stewardship work, alongside tasks, drafts, and decisions. Keep automated CI evidence under `reports/`. Analysis records should cite a fixed branch commit, distinguish observations from hypotheses, and produce Drafts or ADR-linked tasks rather than directly authorize changes. Recommend quarterly portfolio reviews plus event-triggered reviews. Do not add scheduled automation initially.
- **References:** [MADR repository](https://github.com/adr/madr); [MADR guidance](https://github.com/adr/madr/blob/develop/docs/index.md); [MADR full template](https://github.com/adr/madr/blob/develop/template/adr-template.md); [MADR examples](https://github.com/adr/madr/blob/develop/docs/examples.md); [MADR confirmation decision](https://github.com/adr/madr/blob/develop/docs/decisions/0018-use-confirmation-as-heading.md); `skills/document-standards/references/document-type-catalog.md`; `workspace/TASK_TEMPLATE.md`; `reports/triage/scripts/ledger.py`; `reports/triage/scripts/test_ledger.py`; `.github/scripts/cleanup-archive.py`; `archive/README.md`.
- **Next:** Create the requested workspace folders, draft and ADR templates, and a first comprehensive governance draft. Keep the optional analysis folder and detailed workflow extensions proposed until the user reviews the draft.

### 2026-11-24 10:33 UTC — Create the tracked governance task

- **Action:** Read the session-start procedure, foundational skills, workspace README, task board, task template, and current conversation-mode rules. Created this task record and selected it for current execution.
- **Result:** The current CI Ledger repair task remains In Progress and is checkpointed. This governance task is a separate P1 task. Its scope includes the MADR study and the initial proposal. No MADR material or repository governance files have been changed yet.
- **References:** `skills/SESSION_START.md`; `skills/the-worker/SKILL.md`; `skills/the-worker/references/conversation-mode.md`; `skills/asd-ste100/SKILL.md`; `skills/github-actions/SKILL.md`; `skills/document-standards/SKILL.md`; `workspace/README.md`; `workspace/task_board.md`; `workspace/TASK_TEMPLATE.md`.
- **Next:** Study MADR and inspect its canonical templates and lifecycle before writing the initial proposal.

## 7. Current State

MADR research and repository integration review are complete. The requested `workspace/draft/` and `workspace/adr/` folders now contain README files and templates. Workspace navigation and discussion-register link rules are updated. Document Type Catalog 1.11 registers both record families. DRAFT-0001 is committed with status `in-review` and linked in `workspace/discussion.md`. The task is Blocked pending user review. No ADR has been created. The optional `workspace/analysis/` folder and `decision-governance` skill are still proposed.

## 8. Remaining Work

- Obtain the user's review and decision on DRAFT-0001 revision 1.
- Apply any requested revisions and present the revised Draft.
- After explicit approval, create ADR-0001 and mark DRAFT-0001 promoted.
- Create linked implementation tasks and complete the accepted workflow changes.
- Keep the analysis folder and new skill uncreated until the user approves them.

## 9. Next Actions

1. Wait for the user to review [DRAFT-0001](../draft/DRAFT-0001-repository-decision-governance-and-analysis.md).
2. Record the user's decision and any requested changes.
3. Convert the approved revision into ADR-0001 only after explicit approval.
4. Continue with the implementation tasks that ADR-0001 authorizes.

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

- **Check:** Draft/ADR folder setup, templates, catalog coverage, workspace navigation, and discussion link rules.
- **Method:** Retrieved all changed paths from branch `gpt` and checked their content. Verified the Draft coverage rule changed from Reserved to Active when DRAFT-0001 was created.
- **Result:** All required files exist and read back. DRAFT-0001 is `in-review`. The ADR record path remains Reserved because no ADR has been approved yet.
- **Limitations:** The detailed governance process remains a proposal. No ADR has been accepted. No local scripts or tests were run.

## 12. Handoff Instructions

Continue on branch `gpt`. The user must review DRAFT-0001 revision 1. Do not create ADR-0001 until the user explicitly approves the exact Draft revision and scope. Record requested changes in the Draft. Keep `workspace/analysis/` and the new decision-governance skill uncreated until approved. After approval, link implementation tasks to ADR-0001 and preserve the decision under `archive/adr/` after confirmation.

## 13. Ledger Findings

_No Ledger findings are linked to this task._

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
