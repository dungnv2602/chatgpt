# Task: Establish draft-to-ADR governance and repository analysis workflow

## Metadata

- **Template version:** 1.2
- **ID:** 20261124-103354
- **Created:** 2026-11-24 10:33 UTC
- **Updated:** 2026-11-24 15:06 UTC
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

### 2026-11-24 15:06 UTC — Reconcile the latest hosted checks and correct the catalog finding

- **Action:** Reviewed the exact Lint #635, Document Standards #319, and Diagnostics #586 runs on source commit 725896a. Inspected all relevant job steps and the complete Lint #635 job log.
- **Result:** Document Standards [#319](https://github.com/dungnv2602/chatgpt/actions/runs/45416735133) passed all 37 Ledger regression tests, all 32 catalog regression tests, catalog validation, and its diagnostics publisher. Diagnostics [#586](https://github.com/dungnv2602/chatgpt/actions/runs/45416735144) passed reporter tests, backfill, Ledger ingestion, and publication.
- **Lint finding:** Lint [#634](https://github.com/dungnv2602/chatgpt/actions/runs/45416574844) recorded one hard 27-word sentence and 29 advisory findings in the GitHub Actions run and job diagnostics catalog row. Commit 725896a changed table separators, not that sentence. Lint [#635](https://github.com/dungnv2602/chatgpt/actions/runs/45416735141) therefore still set CHANGED_FAILED=1 for the catalog file.
- **Publication failure:** Lint #635 also failed to publish its report. Its generated report commit could not rebase because the source checkout at 725896a did not contain Lint #634's later report commit [5f61509](https://github.com/dungnv2602/chatgpt/commit/5f61509f28c99bb8bb98e48c7c122790228f5daa). Git reported conflicts in `reports/lint_reports/on_changed/index.json`, `latest-lint-report.json`, and `latest-lint-report.md`. The #635 report was not added to the lint history. The diagnostics pre-finalizer capture is Incomplete because it ran before the source workflow finished; the complete Actions job log was inspected directly.
- **Correction:** Commit [4dfbde6](https://github.com/dungnv2602/chatgpt/commit/4dfbde63708f0ab0862d142952710b1b42ef5d7a) splits the 27-word description into two sentences and retains all evidence types and exceptions. Exact read-back confirmed the updated catalog row at line 63.
- **Scope:** No report workflow or generated report was edited. The corrected commit starts from the current branch, which already contains Lint #634's report state. No local tests ran and no Actions runs were polled or rerun.
- **Next:** Review the fresh hosted validation results naturally triggered by commit 4dfbde6. Keep this task Blocked until the lint, Document Standards, and diagnostics results all pass.

### 2026-11-24 14:42 UTC — Correct the inventory table structure and publish final reruns

- **Action:** Reviewed Lint #631 and the subsequent catalog corrections. The linter kept attributing long-sentence findings to the last row in each long Initial inventory table section. Shortening the row text alone did not resolve the findings.
- **Action:** Split the Initial inventory table at the publication-verification and master-catalogue sections. The first split in commit 8bcfdf lacked blank separators, so Markdown treated the repeated headings as data rows. Commit [725896a](https://github.com/dungnv2602/chatgpt/commit/725896a79c8a9c3decef0f8d507cc9cacdaed4fc) added the blank separators. It preserves both entries and all canonical references.
- **Result:** Document Standards [#316](https://github.com/dungnv2602/chatgpt/actions/runs/45415350984) passed 37 Ledger tests, 32 catalog tests, and catalog validation. Its diagnostics publisher passed. Diagnostics [#583](https://github.com/dungnv2602/chatgpt/actions/runs/45415351025) also passed reporter validation, backfill, Ledger ingestion, and publication.
- **Current validation:** Lint [#635](https://github.com/dungnv2602/chatgpt/actions/runs/45416735141) and Document Standards [#319](https://github.com/dungnv2602/chatgpt/actions/runs/45416735133) are pending on commit 725896a. Diagnostics [#586](https://github.com/dungnv2602/chatgpt/actions/runs/45416735144) is also pending. No final result is available yet.
- **Next:** Keep the task Blocked. Review Lint #635 and Document Standards #319 after their complete results publish. Do not poll Actions.

### 2026-11-24 14:28 UTC — Remove duplicate catalog inventory rows and confirm hosted coverage

- **Action:** Reviewed the complete lint #629 report and the completed Document Standards #313 job steps.
- **Result:** Lint #629 reported two hard long-sentence findings in the Initial inventory table. The same document families already have exact coverage rules in the Markdown inventory section. Those rules name the lint generator and test authority and the direct and nested skill-reference path patterns.
- **Action:** Removed the duplicate STE lint-report and technical-reference summary rows in commit [dbd7ad2](https://github.com/dungnv2602/chatgpt/commit/dbd7ad280198ee39849f926b6d32c50d7856da58). Retained the detailed path-coverage rules and all generator/test references. The catalog passed exact read-back.
- **Result:** Document Standards [#313](https://github.com/dungnv2602/chatgpt/actions/runs/45413378979) passed 37 Ledger regression tests, 32 catalog regression tests, and catalog validation. Its diagnostics publisher passed. Diagnostics [#581](https://github.com/dungnv2602/chatgpt/actions/runs/45414156266) also passed reporter validation, backfill, Ledger ingestion, and publication.
- **Current validation:** Lint [#630](https://github.com/dungnv2602/chatgpt/actions/runs/45414156337) is in progress and Document Standards [#314](https://github.com/dungnv2602/chatgpt/actions/runs/45414156487) is pending on commit dbd7ad2. These final results are not available yet.
- **Next:** Keep the task Blocked. Review the complete results for Lint #630 and Document Standards #314 when naturally published. Do not poll Actions.

### 2026-11-24 14:24 UTC — Reconcile the final catalog lint correction

- **Action:** Reviewed Lint #627 and Document Standards #311. Lint #627 still reported two hard long-sentence findings in the Document Type Catalog. The catalog validator and Ledger regression suites passed in Document Standards #311.
- **Result:** Document Standards [#311](https://github.com/dungnv2602/chatgpt/actions/runs/45412770209) passed 37 Ledger tests, 32 catalog tests, and catalog validation. Its diagnostics companion passed. Diagnostics [#578](https://github.com/dungnv2602/chatgpt/actions/runs/45412770199) also passed reporter validation, backfill, Ledger ingestion, and publication.
- **Action:** Commit [58d15b6](https://github.com/dungnv2602/chatgpt/commit/58d15b642db046eeb8bbd32ec622033e2dec1dec) shortened the two remaining catalog rows. The lint-report inventory keeps exact generator, test, template, and schema references. The technical-reference inventory uses a compact README example. Existing wildcard path-coverage rules remain unchanged.
- **Result:** Exact read-back confirmed both modified catalog rows. Diagnostics [#580](https://github.com/dungnv2602/chatgpt/actions/runs/45413378988) passed on commit 58d15b6. Lint [#629](https://github.com/dungnv2602/chatgpt/actions/runs/45413378995) is in progress and Document Standards [#313](https://github.com/dungnv2602/chatgpt/actions/runs/45413378979) is pending. Lint #628 was cancelled after commit 58d15b6 superseded it. This is not a source-workflow failure.
- **Next:** Keep the task Blocked. Review the complete results for Lint #629 and Document Standards #313 when naturally published. Do not poll Actions.

### 2026-11-24 14:20 UTC — Reconcile hosted validation and the latest catalog lint correction

- **Action:** Reviewed lint run #626 and Document Standards run #310 on commit 6e1cf47. Also reviewed the completed Diagnostics run #577.
- **Result:** Document Standards [#310](https://github.com/dungnv2602/chatgpt/actions/runs/45412245960) passed all 37 Ledger regression tests, all 32 catalog regression tests, and the catalog validator. Diagnostics [#577](https://github.com/dungnv2602/chatgpt/actions/runs/45412246098) passed reporter validation, backfill, Ledger ingestion, and publication.
- **Lint finding:** Changed-document lint #626 reported two hard long-sentence findings in the Document Type Catalog. The governance skill passed without hard findings.
- **Action:** Shortened the remaining catalogue descriptions in commit [b1e6ca6](https://github.com/dungnv2602/chatgpt/commit/b1e6ca640cfebc29f917d60c15f9ae42496e5600). The STE report inventory now describes the shared generator in fewer words. The technical-reference inventory now uses a compact description. Exact read-back confirmed the complete catalog file.
- **Current validation:** Lint [#627](https://github.com/dungnv2602/chatgpt/actions/runs/45412770212) is in progress. Document Standards [#311](https://github.com/dungnv2602/chatgpt/actions/runs/45412770209) is pending on commit b1e6ca6. Diagnostics #578 passed on the same commit. These final lint and catalog results remain open.
- **Next:** Keep the task Blocked. Review the complete results for Lint #627 and Document Standards #311 when they are naturally published. Do not poll Actions.

### 2026-11-24 14:12 UTC — Resolve the three remaining catalog lint findings

- **Action:** Reviewed the complete changed-document lint report for run #623. It reported three hard findings in the Document Type Catalog. The governance skill passed with no hard findings.
- **Findings:** The catalog still had two long inventory entries and one `check` / `validate` terminology conflict. The findings were on the CI Ledger row, the skill changelog row, and the Markdown path coverage explanation.
- **Action:** Updated the catalog in commit [594ab39](https://github.com/dungnv2602/chatgpt/commit/594ab39e461e8bc9473ef73fd40048b8f0f6eb72). The CI Ledger row retains the generator and regression-test references but uses a shorter summary. The redundant one-off changelog inventory row was removed. The general `skills/*/CHANGELOG.md` coverage rule remains Active. The path explanation now uses `audit` rather than `check`.
- **Result:** The complete catalog file passed exact read-back. Document Standards run [#307](https://github.com/dungnv2602/chatgpt/actions/runs/45410835359) passed both test suites and catalog validation on the earlier commit f44b5a7. Run [#308](https://github.com/dungnv2602/chatgpt/actions/runs/45411400908) was queued for commit 594ab39. No changed-document lint run for commit 594ab39 was visible at the last inspection.
- **Next:** Keep this task Blocked. Review the complete hosted results for Document Standards #308 and the changed-document lint rerun for commit 594ab39. Do not poll Actions.

### 2026-11-24 14:04 UTC — Confirm the hosted governance validation criterion and isolate the final lint rerun

- **Action:** Reviewed the hosted run #305 and its completed job steps. Also reconciled the full Document Standards, Diagnostics, and changed-document lint results since DRAFT-0001 approval.
- **Result:** Document Standards run [#305](https://github.com/dungnv2602/chatgpt/actions/runs/45409620929) passed on commit 7fa7483. It passed all 37 Ledger regression tests, all 32 catalog regression tests, and the Document Type Catalog validator. Its diagnostics companion job also passed. This confirms the hosted Document Standards and Ledger validation criterion in ADR-0001.
- **Result:** Earlier hosted validation also passed on runs #302 and #304. Diagnostics runs #569 and #571 passed reporter tests, backfill, Ledger ingestion, and publication. The initial shell failure in run #300 was corrected in commit 454672a.
- **Action:** Resolved the blocking lint findings in successive edits. Commit 849c027 addressed 52 hard findings from run #616. Commit aa69d96 addressed seven findings from run #618. Commit b1aec86 addressed four findings from run #619. Commit [7fa7483](https://github.com/dungnv2602/chatgpt/commit/7fa7483122c074c48e8d0b82ea65d59f4aca37f4) shortened the last over-limit catalog descriptions and removed the final terminology conflicts reported by run #620.
- **Current validation:** Changed-document lint run [#621](https://github.com/dungnv2602/chatgpt/actions/runs/45409620876) is still in progress on commit 7fa7483. Its complete result is not yet available. Keep this task Blocked until the run completes successfully.
- **References:** `reports/lint_reports/on_changed/index.json`; full lint reports for runs #616, #618, #619, and #620; `.github/workflows/validate-document-standards.yml`; `reports/triage/ledger.json`; and commits 454672a, 849c027, aa69d96, b1aec86, and 7fa7483.
- **Next:** Review the naturally published complete result for Lint #621. Do not poll Actions. If it passes, record the run URL and UTC timestamp, complete the task acceptance criteria, and begin archive closeout.

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

The approved governance implementation is committed on branch `gpt`. Commit 74005cc moved the Draft, ADR, and analysis templates to the workspace root and corrected catalog ownership. Commit ad8bf8b added Ledger regression coverage to the hosted Document Standards workflow. Commit 454672a fixed the shell command used to run the Ledger suite.

The latest completed validation on source commit 725896a produced mixed results:

- Document Standards [#319](https://github.com/dungnv2602/chatgpt/actions/runs/45416735133) passed all 37 Ledger tests, all 32 catalog tests, and catalog validation. Its diagnostics publisher also passed.
- Diagnostics [#586](https://github.com/dungnv2602/chatgpt/actions/runs/45416735144) passed reporter validation, backfill, Ledger ingestion, and publication.
- Changed-document lint [#635](https://github.com/dungnv2602/chatgpt/actions/runs/45416735141) failed. The catalog description still contained the one hard 27-word sentence identified by Lint #634. Its evidence-publication step also failed to rebase the report commit onto a branch that already contained Lint #634's report publication. The resulting report commit was not published.

Commit [4dfbde6](https://github.com/dungnv2602/chatgpt/commit/4dfbde63708f0ab0862d142952710b1b42ef5d7a) now splits the hard sentence in the catalog diagnostics row. Read-back confirms the complete corrected row. The push triggers fresh hosted validation from a branch state that already includes the earlier lint report commit. Those new results have not yet been reviewed.

The task remains Blocked. Do not infer a pass from the earlier successful Document Standards or Diagnostics runs. Keep the three Ledger-generated lint tasks Proposed until the user approves their remediation. Keep DRAFT-0002 separate and unmodified.
## 8. Remaining Work

- Confirm that a fresh changed-document lint run on commit 4dfbde6 passes with no hard findings and publishes its complete report.
- Confirm that a fresh Document Standards run on commit 4dfbde6 passes its Ledger tests, catalog tests, and catalog validator.
- Confirm that the corresponding Diagnostics publication/backfill completes successfully.
- Record the fresh run URLs and UTC timestamps. Inspect complete logs and reports for any failed result. Do not poll Actions or rerun workflows.
- Update ADR-0001 lifecycle evidence with the final hosted validation results.
- Complete the task acceptance criteria and archive this task.
- Move ADR-0001 to `archive/adr/` only after every linked task is Done and every Confirmation criterion passes.
- Keep the three Ledger-generated lint tasks Proposed until the user approves their remediation.
- Keep DRAFT-0002 separate and unmodified.
## 9. Next Actions

1. Review the naturally published changed-document lint result for the catalog correction in commit 4dfbde6.
2. Review the corresponding Document Standards run. Confirm the Ledger tests, catalog tests, and catalog validator passed.
3. Review the Diagnostics publication result for the new runs.
4. If any run fails, inspect its complete report and job log. Correct only issues within this task's approved scope. Keep the task Blocked.
5. If all required runs pass, record their URLs and UTC timestamps. Update ADR-0001's lifecycle history, complete task closeout, and archive the task.
6. Archive ADR-0001 only after all linked tasks are Done and every Confirmation criterion passes.
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
- Document Standards runs [#302](https://github.com/dungnv2602/chatgpt/actions/runs/45407620289), [#304](https://github.com/dungnv2602/chatgpt/actions/runs/45408954986), [#305](https://github.com/dungnv2602/chatgpt/actions/runs/45409620929), [#307](https://github.com/dungnv2602/chatgpt/actions/runs/45410835359), [#308](https://github.com/dungnv2602/chatgpt/actions/runs/45411400908), [#309](https://github.com/dungnv2602/chatgpt/actions/runs/45411867050), [#310](https://github.com/dungnv2602/chatgpt/actions/runs/45412245960), [#311](https://github.com/dungnv2602/chatgpt/actions/runs/45412770209), [#313](https://github.com/dungnv2602/chatgpt/actions/runs/45413378979), [#314](https://github.com/dungnv2602/chatgpt/actions/runs/45414156487), [#315](https://github.com/dungnv2602/chatgpt/actions/runs/45414832231), and [#316](https://github.com/dungnv2602/chatgpt/actions/runs/45415350984)
- Diagnostics runs [#569](https://github.com/dungnv2602/chatgpt/actions/runs/45407620173), [#571](https://github.com/dungnv2602/chatgpt/actions/runs/45408955121), [#573](https://github.com/dungnv2602/chatgpt/actions/runs/45410287179), [#577](https://github.com/dungnv2602/chatgpt/actions/runs/45412246098), [#578](https://github.com/dungnv2602/chatgpt/actions/runs/45412770199), [#580](https://github.com/dungnv2602/chatgpt/actions/runs/45413378988), [#581](https://github.com/dungnv2602/chatgpt/actions/runs/45414156266), [#582](https://github.com/dungnv2602/chatgpt/actions/runs/45414832198), and [#583](https://github.com/dungnv2602/chatgpt/actions/runs/45415351025)
- Changed-document lint runs [#616](https://github.com/dungnv2602/chatgpt/actions/runs/45403469914), [#618](https://github.com/dungnv2602/chatgpt/actions/runs/45407620144), [#619](https://github.com/dungnv2602/chatgpt/actions/runs/45408533122), [#620](https://github.com/dungnv2602/chatgpt/actions/runs/45408955146), [#621](https://github.com/dungnv2602/chatgpt/actions/runs/45409620876), [#623](https://github.com/dungnv2602/chatgpt/actions/runs/45410835376), [#624](https://github.com/dungnv2602/chatgpt/actions/runs/45411401151), [#626](https://github.com/dungnv2602/chatgpt/actions/runs/45412245944), [#627](https://github.com/dungnv2602/chatgpt/actions/runs/45412770212), [#629](https://github.com/dungnv2602/chatgpt/actions/runs/45413378995), [#630](https://github.com/dungnv2602/chatgpt/actions/runs/45414156337), [#631](https://github.com/dungnv2602/chatgpt/actions/runs/45414832243), [#632](https://github.com/dungnv2602/chatgpt/actions/runs/45415351074), and [#635](https://github.com/dungnv2602/chatgpt/actions/runs/45416735141)
- Commits [74005cc](https://github.com/dungnv2602/chatgpt/commit/74005ccb1afc79d21966112501baa39772905864), [454672a](https://github.com/dungnv2602/chatgpt/commit/454672ae649a607db689876ddfb77cb5b4450e65), [849c027](https://github.com/dungnv2602/chatgpt/commit/849c027ee97b1a6c7d52f4d3020c6a152c4bae60), [aa69d96](https://github.com/dungnv2602/chatgpt/commit/aa69d966969a8d5a3cc5106a74f1204a0f324e3e), [b1aec86](https://github.com/dungnv2602/chatgpt/commit/b1aec86f3f13eb7ac5c2dd92e8a7ba1f0f150a00), [7fa7483](https://github.com/dungnv2602/chatgpt/commit/7fa7483122c074c48e8d0b82ea65d59f4aca37f4), [f44b5a7](https://github.com/dungnv2602/chatgpt/commit/f44b5a744a0b4748153f68e512d94255ebf59fe3), [594ab39](https://github.com/dungnv2602/chatgpt/commit/594ab39e461e8bc9473ef73fd40048b8f0f6eb72), [6e1cf47](https://github.com/dungnv2602/chatgpt/commit/6e1cf47bc8b0b40dcc309e457059ba0b63d8c960), [b1e6ca6](https://github.com/dungnv2602/chatgpt/commit/b1e6ca640cfebc29f917d60c15f9ae42496e5600), [58d15b6](https://github.com/dungnv2602/chatgpt/commit/58d15b642db046eeb8bbd32ec622033e2dec1dec), [dbd7ad2](https://github.com/dungnv2602/chatgpt/commit/dbd7ad280198ee39849f926b6d32c50d7856da58), [9606a5f](https://github.com/dungnv2602/chatgpt/commit/9606a5f825b57cab8e30e36ebd372429e9e7ada3), [2b878e2](https://github.com/dungnv2602/chatgpt/commit/2b878e201fb39d951049855ec1bae9cb538f00da), [3295bcb](https://github.com/dungnv2602/chatgpt/commit/3295bcbe74b9a0a11b544146e987a6ce3ccff7a2), [8bcfdf16](https://github.com/dungnv2602/chatgpt/commit/8bcfdf16b30ae18bedbec3c412eb54614711f5a0), and [725896a](https://github.com/dungnv2602/chatgpt/commit/725896a79c8a9c3decef0f8d507cc9cacdaed4fc)
- Related task: `20261123-225745`
## 11. Verification

- **Check:** Catalog/template placement and governance owner references.
- **Method:** Read back all nine paths changed by commit 74005cc. Compare relocated template blob SHAs with their original values. Confirm that former nested paths return 404.
- **Result:** All nine paths passed read-back. The three relocated templates retained their original blob SHAs. The old paths no longer exist.
- **Check:** Hosted Document Standards and Ledger validation.
- **Method:** Inspect the job steps for the completed Document Standards runs, including #319. Inspect the corresponding Diagnostics runs.
- **Result:** Document Standards runs #302, #304, #305, #307, #308, #309, #310, #311, #313, #314, #315, #316, and #319 passed their relevant Ledger tests, catalog tests, and catalog validator. Run #319 passed all 37 Ledger tests and all 32 catalog tests. Diagnostics #586 passed reporter validation, backfill, Ledger ingestion, and publication.
- **Check:** Changed-document lint and report publication.
- **Method:** Inspect Lint #634's immutable report, Lint #635's complete Actions job log, its pre-finalizer diagnostic capture, and the exact catalog source text.
- **Result:** Lint #634 reported one hard 27-word sentence and 29 advisory findings. Lint #635 set CHANGED_FAILED=1 and its report publisher failed to rebase because Lint #634's report commit had updated the same index and latest-report files after source SHA 725896a. The #635 report did not reach the lint history.
- **Correction:** Commit 4dfbde6 split the 27-word catalog description into two sentences. Exact read-back confirms the correction. Fresh hosted validation on this commit remains outstanding.
- **Limitations:** Do not claim that Lint #635 passed or that the post-correction hosted checks succeeded. The #635 pre-finalizer diagnostic capture is Incomplete because it was created while the source run was still in progress. No local repository scripts or tests ran. No CI polling or reruns occurred.
## 12. Handoff Instructions

Read `workspace/README.md`, `workspace/task_board.md`, this task record, and `workspace/discussion.md`. Keep the task Blocked until a fresh changed-document lint run and Document Standards run on the corrected catalog commit pass, and the corresponding Diagnostics publication succeeds. Do not poll or rerun Actions. If a run fails, inspect its complete report and job log. Keep the three Ledger-generated lint tasks Proposed until the user approves remediation. DRAFT-0002 remains separate and unmodified. Do not archive ADR-0001 until every linked task is Done and every Confirmation criterion passes.
## 13. Ledger Findings

_No Ledger findings are linked to this task._

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
