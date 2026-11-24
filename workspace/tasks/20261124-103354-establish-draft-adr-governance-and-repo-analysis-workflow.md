# Task: Establish draft-to-ADR governance and repository analysis workflow

## Metadata

- **Template version:** 1.2
- **ID:** 20261124-103354
- **Created:** 2026-11-24 10:33 UTC
- **Updated:** 2026-11-24 13:45 UTC
- **Priority:** P1
- **Status:** Blocked
- **Origin:** User
- **Approval:** Approved for implementation. The user approved DRAFT-0001 revision 1 on 2026-11-24 12:25 UTC and directed execution.
- **Current execution:** Yes
- **Governing ADR(s):** ADR-0001 — [Establish Draft-to-ADR Governance and Repository Analysis](../adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md)
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
- **2026-11-24:** The repository-analysis location and detailed governance rules remained open until the user approved DRAFT-0001 revision 1.
- **2026-11-24 12:25 UTC:** The user approved DRAFT-0001 revision 1 and directed execution of this task.

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

### 2026-11-24 10:47 UTC — Reconcile blocked task status and handoff

- **Action:** Moved this task's board row from In Progress to Blocked. Kept it in Current Execution because DRAFT-0001 requires the user's decision before work can continue.
- **Result:** Task metadata and board status now both show Blocked. The task board has no stale In Progress row for this task. The discussion register links the active task in Current Step and DRAFT-0001 in Open Discussions. All older CI discussions remain intact.
- **Commit:** Board reconciliation [b442ec9](https://github.com/dungnv2602/chatgpt/commit/b442ec98b51af4fa6faf8074bf9eee6167ecc8c7). Current brief [47268ad](https://github.com/dungnv2602/chatgpt/commit/47268ad8554247fc9f5b2622e6e189bd22884fda).
- **Next:** Wait for explicit user review of DRAFT-0001 revision 1. Do not create ADR-0001 or implement optional changes before approval.

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

### 2026-11-24 12:25 UTC — User approves DRAFT-0001 revision 1

- **Action:** The user approved the exact DRAFT-0001 revision 1 and directed execution of this task.
- **Result:** Approval covers the complete Draft, including `workspace/analysis/`, the task-specific `decision-governance` skill, task-to-ADR linkage, Ledger changes, and permanent ADR archival. DRAFT-0002 remains a separate, unapproved proposal.
- **References:** `workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md`; user instruction in this conversation.
- **Next:** Create ADR-0001 and implement its approved governance scope.

### 2026-11-24 12:42 UTC — Implement the core governance contracts

- **Action:** Added the decision-governance skill, analysis templates, task ADR field, aligned task board, Worker integration, permanent ADR archive rules, and catalog coverage.
- **Result:** The core governance contracts now exist. The Ledger renderer and its tests still require coordinated updates. Final read-back and hosted validation remain outstanding.
- **Next:** Update the Ledger handoff and generated board row, then read back all changed paths.

### 2026-11-24 13:05 UTC — Complete implementation read-back and reconcile validation evidence

- **Action:** Read back the accepted ADR, promoted Draft, decision-governance skill, analysis files, Worker rules, task template, task board, archive policies, Ledger renderer, Ledger tests, triage guide, and Document Type Catalog.
- **Result:** The approved governance files are present and linked. The task board now uses eight columns, including ADR(s). Legacy pre-policy rows use `—`. The transition-era Ledger-generated Proposed task 20261124-123847 now has a Pending ADR review field and matching board cell.
- **Validation evidence:** The committed changed-document lint report passed for two evaluated documents. A committed Actions diagnostic for run #296 reported a failure at the Document Standards catalog validation step. The capture was incomplete and contained no job log. Static review found that `workspace/adr/ADR-*.md` did not match ADR-0001's numeric filename. The catalog rule is now `workspace/adr/????-*.md`. A post-correction hosted result has not been observed.
- **Corrections:** Closed the Ledger header-guard string, aligned the task-board separators, corrected the Ledger task-template placeholder, updated its regression assertions, and removed a duplicate DRAFT-0002 index row.
- **Next:** Keep this task Blocked until the next naturally published hosted validation confirms the catalog and Ledger checks. Do not poll CI or run scripts locally.

## 7. Current State

The approved governance files and three shared templates are present in branch `gpt`. Commit 74005cc moved the templates to the shared workspace root, corrected the catalog owner references, and updated the owner links and workspace navigation. All nine changed paths passed read-back.

Commit ad8bf8b adds the Ledger regression suite to the hosted Document Standards workflow. The workflow also runs when Ledger scripts or the Ledger schema change. The workflow and ADR changes passed read-back.

The Ledger handoff criterion is now confirmed. The Ledger processed the changed-document lint report for run 45403469914 and created three Proposed task records. Each record and board row marks the governing ADR as Pending. ADR-0001 records this evidence.

The task remains Blocked. Document Standards run #298 completed with a catalog failure on earlier commit `d66901394de689223394f990047705d42108cef0`. It predates the catalog correction. The changed-document lint run #616 for commit 74005cc failed with 52 hard and 52 advisory findings across 10 files. Its tooling regression checks passed. Its report does not establish that all findings came from this task. No hosted result for the updated validation workflow has been confirmed.
## 8. Remaining Work

- Confirm that hosted catalog validator regression tests pass after the template and catalog corrections.
- Confirm that the hosted `test_ledger.py` suite passes through the updated validation workflow.
- Confirm that the catalog validator passes on the corrected catalog.
- Record the successful validation run URLs and UTC timestamps.
- Complete the remaining ADR-0001 Confirmation criteria with evidence.
- Archive this task only after all acceptance criteria pass.
- Move ADR-0001 to `archive/adr/` only after every linked task is Done and every Confirmation criterion passes.
- Keep the three Ledger-generated lint tasks Proposed until the user approves their remediation.
- Keep DRAFT-0002 separate and unmodified.
## 9. Next Actions

1. Do not poll Actions. In a later task session, inspect the next naturally published complete validation evidence for commit ad8bf8b or its descendants.
2. Confirm that catalog validator tests, catalog validation, and Ledger regression tests all pass. Record the exact run URL and UTC time.
3. If a validation fails, inspect its complete post-run report and job log. Correct only causes within this task's approved scope. Keep the task Blocked.
4. Update ADR-0001 Confirmation only after each criterion has supporting evidence.
5. Close and archive this task only after its acceptance criteria pass. Archive ADR-0001 only after all linked tasks are Done and all Confirmation criteria pass.
## 10. References

- External source: `https://github.com/adr/madr`
- `skills/SESSION_START.md`
- `skills/the-worker/SKILL.md`
- `skills/the-worker/references/conversation-mode.md`
- `skills/document-standards/SKILL.md`
- `skills/document-standards/references/document-type-catalog.md`
- `workspace/README.md`
- `workspace/TASK_TEMPLATE.md`
- `workspace/ADR_TEMPLATE.md`
- `workspace/DRAFT_TEMPLATE.md`
- `workspace/ANALYSIS_TEMPLATE.md`
- `.github/workflows/validate-document-standards.yml`
- `reports/triage/ledger.json` and `reports/triage/scripts/test_ledger.py`
- Document Standards run [#298](https://github.com/dungnv2602/chatgpt/actions/runs/45399711310) (pre-correction failure)
- Changed-document lint run [#616](https://github.com/actions/runs/45403469914) (commit 74005cc)
- Commit [74005cc](https://github.com/dungnv2602/chatgpt/commit/74005ccb1afc79d21966112501baa39772905864)
- Commit [ad8bf8b](https://github.com/dungnv2602/chatgpt/commit/ad8bf8b0b6730ecbc4b04460b2749fab2a8ff6f6)
- Related task: `20261123-225745`
## 11. Verification

- **Check:** Ledger task handoff and ADR linkage.
- **Method:** Read the published Ledger JSON, the task board, and all three task records. Match Ledger `task_refs` to task IDs and inspect each task's Status, Approval, and Governing ADR(s) fields.
- **Result:** The Ledger links findings to three Proposed tasks. Each task is Pending approval and has Governing ADR(s) set to Pending. The board marks each row Proposed with ADR value Pending. ADR-0001 now records this confirmed criterion.
- **Check:** Hosted validation workflow wiring.
- **Method:** Read the committed workflow and ADR after commit ad8bf8b.
- **Result:** The workflow runs `python -m unittest discover -s reports/triage/scripts -p 'test_ledger.py' -v` and has paths for `reports/triage/scripts/**` and `reports/triage/ledger-schema.json`. ADR-0001 marks the observed Ledger handoff criterion complete.
- **Limitations:** Document Standards run #298 failed on the earlier commit d669013. No confirmed hosted execution of the updated workflow exists yet. Changed-document lint run #616 failed with findings, although its tooling regression checks passed. No repository scripts or tests ran locally.
## 12. Handoff Instructions

Read `workspace/README.md`, `workspace/task_board.md`, this task record, and `workspace/discussion.md`. Keep the task Blocked until the hosted workflow validates the catalog and Ledger regression tests. Do not poll Actions. Review only a naturally published complete report. Use exact run URLs and UTC timestamps for ADR-0001 Confirmation. Do not modify the three Proposed lint tasks without user approval.

## 13. Ledger Findings

_No Ledger findings are linked to this task._

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
