# Task: Study Planning with Files and propose a file-backed Worker workflow

## Metadata

- **Template version:** 1.2
- **ID:** 20261124-113009
- **Created:** 2026-11-24 11:30 UTC
- **Updated:** 2026-11-25 07:11 UTC
- **Priority:** P1
- **Status:** Blocked
- **Origin:** User
- **Approval:** Approved to study the supplied project, inspect this repository's current workflow, and prepare a comprehensive proposal for user review. Do not implement proposed workflow changes before approval.
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** 20261124-103354 — Establish draft-to-ADR governance and repository analysis workflow. Keep DRAFT-0001 unchanged while it awaits user review.
- **Ledger group:** None
- **Archived:** No

<!-- Lifecycle invariant: keep the active record In Progress and Archived: No until the final archive copy is written and read back. Set Done/Cancelled and Archived: Yes only in the initial archive copy. Check its complete content and commit metadata before deleting the active path. After creation, treat the archive copy as immutable. Delete the active record only after archive verification. Move the board row to Historical only after the active path is absent and the board can link the exact archive path and archive commit. If any step fails, keep the task open and reconcile the partial state without rewriting the archive. -->

## 1. Original Request

Start session

Condensed mode

Here's the link: https://github.com/othmanadi/planning-with-files

Study it thoroughly and take inspirations from it. I would expect the result is a bunch of new templates, an update for our workflow and which skills to update, or even a new skill.

Compared to what we already have, I assume this is about the-worker and /workspace workflow or something similar. Suggest improvements for our workflow.

Here is my base ideas, expand on this. Better yet, try to utilize the best out of this. Make it exhaustive, comprehensive, so we would have a solid workflow. If you say you want to adopt it entirely, feel free to tell me, and explain.

## 2. Subsequent Instructions

- **2026-11-24:** The user selected Condensed Mode for this task.
- **2026-11-24:** The user supplied the Planning with Files external reference and requested a thorough study.
- **2026-11-24:** The user asked for a comprehensive, repository-specific workflow proposal, including templates and affected skills or a new skill where useful.
- **2026-11-24:** The user started the session explicitly.

- **2026-11-25:** The user requested an updated DRAFT-0002 with detailed assessments of all available options.
- **2026-11-25:** The user supplied master/Handoff.md and requested a session start and review. The hand-off asks for a separate Draft that refines and complements the user's approval of DRAFT-0002 by defining the area/project/task model, identifying gaps and deadlocks, reducing duplication, and improving the workflow.

## 3. Objective

Study Planning with Files and determine how its durable planning, research capture, progress logging, recovery, task isolation, error handling, and verification controls can improve this repository's Worker and workspace workflow. Prepare an exhaustive proposal that fits the repository's remote-only GitHub operating model and existing approval gates.

## 4. Requirements

1. Study Planning with Files and determine how its durable planning, research capture, progress logging, recovery, task isolation, error handling, and verification controls can improve this repository's Worker and workspace workflow.
2. Record the external branch, commit or version, exact files inspected, and material evidence. Treat vendor claims and benchmarks as claims with disclosed methodology, not as independent proof.
3. Inspect the current Worker skill, Conversation Mode reference, workspace README, task board, task template, Draft and ADR contracts, Document Type Catalog, and skill-authoring rules.
4. Compare the external three-file pattern with the records this repository already maintains. Identify overlap and avoid duplicate sources of truth.
5. Evaluate plan phases, findings/evidence, progress journals, durable checkpoints, resume procedures, error records, task isolation, parallel work, worker ownership, approval gates, and completion checks.
6. Evaluate which external capabilities can work in this ChatGPT/GitHub-connector environment. Do not assume local filesystem access, shell commands, lifecycle hooks, plugins, or stop gates that are not available.
7. Recommend a minimum viable design and a full design. Explain adoption costs, benefits, risks, and controls.
8. Identify exact templates, skill files, workflow documents, indexes, and catalog/path-coverage changes required by the recommended design.
9. Decide whether to update The Worker directly, add a focused Worker reference, create a task-specific skill, or use a combination. Keep foundational initialization conditional.
10. Preserve user approval gates. Do not create an accepted ADR or implement proposed workflow changes before the user approves the exact Draft.
11. Keep DRAFT-0001 unchanged and open while it awaits the user's separate review. Cross-link this task and any new Draft where useful. Reconcile overlapping decisions before either proposal is promoted.
12. Follow Document Standards and the repository writing policy for any Draft or other authored record.
13. Read back all changed repository paths and report only checks that actually occurred.
14. Do not run repository scripts or CI locally. Do not repair unrelated findings or poll Actions.
15. Review master/Handoff.md and prepare a separate, complementary architecture Draft for user review. Keep implementation out of scope.

## 5. Decisions

- **Approved:** Study the supplied external project.
- **Approved:** Inspect and compare the current Worker and workspace workflow.
- **Approved:** Prepare a comprehensive proposal for user review.
- **Approved:** Review master/Handoff.md and prepare a separate, complementary architecture Draft for user review.
- **Proposed:** Adapt the useful file-backed planning ideas to the existing task record and workspace system.
- **Not approved:** Installing or copying the external skill, adding local hooks or scripts, changing foundational initialization, adding automation, or implementing any proposed workflow change.
- **Constraint:** Do not change DRAFT-0001 or create ADR-0001 without the user's separate approval.

## 6. Progress Log

### 2026-11-24 11:30 UTC — Create and select the task

- **Action:** Read the workspace navigation, task board, task template, Draft and ADR contracts, existing governance task, and Document Type Catalog entries for workspace task records.
- **Result:** No task was in current execution. DRAFT-0001 remains open and in review. Its associated governance task remains Blocked. The existing task record is the authoritative lifecycle and progress record. The `workspace/tasks/*.md` family is Template required and Active.
- **References:** `workspace/README.md`; `workspace/task_board.md`; `workspace/TASK_TEMPLATE.md`; `workspace/draft/README.md`; `workspace/draft/DRAFT_TEMPLATE.md`; `workspace/adr/README.md`; `workspace/adr/ADR_TEMPLATE.md`; `skills/document-standards/references/document-type-catalog.md`; task `20261124-103354`.
- **Next:** Create the task record and update the board and discussion register.

### 2026-11-24 11:30 UTC — Complete foundational initialization and begin source study

- **Action:** Retrieved and read the required foundational skills and Conversation Mode reference. Retrieved the external repository README, canonical skill, reference, and examples.
- **Result:** Foundational initialization passed. Initial source review confirms a three-file model (`task_plan.md`, `findings.md`, and `progress.md`) with plan resolution, recovery, phase markers, error logging, task isolation, and optional host lifecycle hooks. A detailed review of the external implementation and security boundaries remains.
- **References:** `skills/SESSION_START.md`; `skills/the-worker/SKILL.md`; `skills/the-worker/references/conversation-mode.md`; `skills/asd-ste100/SKILL.md`; `skills/github-actions/SKILL.md`; `skills/document-standards/SKILL.md`; external `OthmanAdi/planning-with-files` at `master`: `README.md`, `skills/planning-with-files/SKILL.md`, `skills/planning-with-files/reference.md`, `skills/planning-with-files/examples.md`.
- **Next:** Inspect the remaining canonical templates, workflow guides, helper contracts, security notes, and tests. Then compare them with the repository's existing task and recovery model.

### 2026-11-24 11:34 UTC — Complete the external Planning with Files review

- **Action:** Reviewed the external canonical skill, the three planning templates, workflow and long-running task guides, security policy, plan inventory contract, resolver, completion checker, Stop-gate dispatcher, examples, context-engineering reference, and relevant resolver/template regression tests.
- **Source version:** External branch `master`, release metadata `3.29.1`, branch head `aaa38bc62053f5f7c1bfbcb60f0405f7cf0ee228` (committed 2026-11-23 11:57:02 UTC). The skill blob at that revision is `e95f7dc8c5864a89ca51e2d40de45b2de82c0622`.
- **Core mechanisms:** The project separates a phase plan (`task_plan.md`), a research/evidence store (`findings.md`), and a chronological run log (`progress.md`). It requires one explicit plan owner, records one exact next action, keeps phase markers machine-readable, and reads the selected plan before resume or major decisions.
- **Task selection and isolation:** Named plan directories use an explicit `PLAN_ID` and optional project-root pin. An invalid pin or ambiguous plan selection fails closed. The shared active pointer is for sequential switching, not parallel-session binding. Workers report in their own ledgers or files while one orchestrator owns shared planning state.
- **Reliability controls:** The skill requires phase updates, error logging, non-identical recovery attempts, and a three-attempt escalation guideline. Completion scripts validate the phase structure and statuses. Their validation does not prove that acceptance criteria or implementation are complete.
- **Security controls:** External material belongs in the findings file and remains untrusted. The skill documents the limitations of delimiters, nonce framing, and SHA-256 attestation. Its v3 modes require attestation for plan injection and replace free-text progress injection with a structured ledger summary. The gate is host-dependent and includes block-count and stall limits.
- **Lifecycle trade-offs:** The three files are working memory, not durable records by default. The external workflow documents that plans are commonly gitignored and are neither extracted nor archived automatically. It requires explicit user approval before archiving plans. It also distinguishes a valid phase-format check from proof of completion.
- **Repository fit:** The external project assumes a local project filesystem, shell/PowerShell/Python helpers, and compatible agent lifecycle hooks. This repository uses GitHub-hosted files as its sole project workspace. It has no equivalent per-turn local hook runtime. Its Worker task record already owns task metadata, approvals, progress history, current state, recovery, verification, and handoff. A literal three-file transplant would duplicate these records and add unsupported runtime dependencies.
- **Tests inspected, not executed:** `tests/test_check_complete_resolver.py` pins resolver compatibility, template phase counts, Next Step placement, and gate phase extraction. The external project also has many path, catchup, attestation, and adapter regression tests. No external tests or repository scripts were run.
- **Path lookup correction:** An initial lookup for `docs/plan-inventory.md` returned 404. The canonical inventory was found at `skills/planning-with-files/plan-inventory.md`. The unavailable `docs/evals.md` path was not used.
- **Next:** Compare these mechanisms against The Worker and the task renderer. Recommend only the parts that fit the current authority and runtime model.

### 2026-11-24 11:40 UTC — Compare the systems and prepare DRAFT-0002

- **Action:** Compared the external workflow with the Worker task authority, Progress Log, discussion register, workspace navigation, task archive, and CI Ledger renderer.
- **Result:** Recommended a selective hybrid. Keep one task record as the plan and activity log. Add phase tracking with exit criteria and one Next Step. Add an optional evidence note for research-heavy work. Do not install the external skill or add local hooks.
- **Decision proposal:** Update The Worker and add a focused Worker reference. Do not create a new skill. Preserve the existing task board and discussion register structures. Keep the separate DRAFT-0001 decision open.
- **Artifact:** Created [DRAFT-0002 — Phase-Aware Planning and Evidence Capture](../draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md), revision 1, status in-review.
- **Index:** Added DRAFT-0002 to `workspace/draft/README.md`. The existing Draft path rule already covers the new file.
- **Next:** Add DRAFT-0002 to Open Discussions, reconcile the task board to Blocked, and read back all changed paths.

### 2026-11-24 11:43 UTC — Register and verify the proposal

- **Action:** Added DRAFT-0002 to the Draft index and Open Discussions. Changed this task to Blocked and kept it as the current review item.
- **Result:** The task record is Blocked. The board has one matching Blocked row and keeps the task in Current Execution. Open Discussions contains both DRAFT-0002 and the separate DRAFT-0001 review. Reports retains exactly three success entries.
- **Readback:** Retrieved the task, board, discussion register, Draft index, DRAFT-0002, and DRAFT-0001 from branch `gpt`. DRAFT-0002 is revision 1 and in-review. Its recommendation and all required proposal sections are present. DRAFT-0001 remains in-review and was not edited.
- **Commits:** DRAFT-0002 `51eadc2849a6e63fc1d9a8c1380429d3df784b81`; Draft index `31bb58dfe0d7acd5914b7b34ee8b41464f0658ee`; task state `4b5aaea8a552a0b93c017636689b0c95ce503e1d`; task board `db16a7267cb64e6e4e4c780e3303cae54e7ac7ac`; discussion register `da614212a8d87a3d042b1316b2ce39db4134850b`.
- **Next:** Await the user's decision on DRAFT-0002 revision 1. Do not create an ADR or implement the proposal before approval.

### 2026-11-25 02:20 UTC — Resume the proposal after the user's review request

- **Action:** Reconciled the current task and repository state. Compared `main` and `gpt`, completed the user-authorized fast-forward, and verified that both branches matched at commit `3bce922cb6348e38e04ea7c2d43597af9d908fc3`. Read DRAFT-0002 revision 2, the Decision Governance skill, Draft template, draft index, Document Type Catalog, and the original research task.
- **Result:** The user's new request continues this task. The task is now In Progress. DRAFT-0002 revision 2 remains in-review but is no longer the revision requested for a decision. The task must prepare revision 3 with detailed, balanced assessments of all four existing options. No implementation is approved. The Draft path family is already covered by the catalog and template, so no catalog change is required for this revision.
- **References:** `workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md`; `skills/decision-governance/SKILL.md`; `workspace/DRAFT_TEMPLATE.md`; `workspace/draft/README.md`; `skills/document-standards/references/document-type-catalog.md`; merge commit `3bce922cb6348e38e04ea7c2d43597af9d908fc3`.
- **Next:** Verify the external source at its current branch head, assess each option against the repository's operating constraints, then revise DRAFT-0002 as revision 3. Keep implementation blocked pending exact Draft and accepted ADR approval.

### 2026-11-25 02:23 UTC — Verify the current external source and complete the option assessment

- **Action:** Queried the external repository API for the current `master` head and latest release. Read the pinned canonical skill, three templates, long-running-task guide, evaluation report, attestation guide, security policy, and plan resolver from that source commit.
- **Source snapshot:** The current `master` head is still `aaa38bc62053f5f7c1bfbcb60f0405f7cf0ee228`, committed 2026-11-23 11:57:02 UTC. The latest release is v3.29.1, published 2026-11-23 09:26:21 UTC. The latest commit changes README sponsor material; it does not change the planning mechanisms reviewed here.
- **Mechanisms confirmed:** The external system uses task-scoped three-file state, named `.planning/<id>` directories, `PLAN_ID` and `PWF_PLAN_ROOT` selectors, a shared active pointer for sequential switching, one plan owner, separate worker ledgers, host-dependent context-injection hooks, optional autonomous/gated modes, and SHA-256 plan attestation. Its attestation is not a human approval or a keyed signature. Plan content remains untrusted data.
- **Evaluation evidence and limits:** The repository's Test 5 is an internal 2026-07-06 benchmark of v3.4.0 on Claude Code, not the current v3.29.1 release or this ChatGPT/GitHub environment. It reports 77 graded cells with correctness parity across all arms; a forced recovery subset reports 5.0 stage-two turns for Planning with Files versus 8.3–13.3 for six alternatives. The same report says the current file-only recovery path was not re-tested under that protocol; the unforced tasks cover only two small tasks; and long-horizon drift, cross-IDE behavior, multi-day work, and independent task corpora were not tested. The historical v2.21.0 tests and 3/3 blind A/B comparison are also author-run and limited. These results support a hypothesis about structured planning and recovery, not a quantified performance promise for this repository.
- **Assessment:** Option 1 remains the lowest-cost baseline and is adequate for short, single-stage work, but does not resolve explicit phase/next-action gaps. Option 2 has the strongest integrated mechanics when a compatible local agent host can run them, but is a poor direct fit here because it introduces overlapping authority and depends on local filesystem/runtime hooks. Option 3 best preserves the repository's task authority and remote-only workflow while addressing the gaps with bounded overhead. Option 4 may support structural checks through GitHub Actions, but cannot provide per-turn injection or runtime stop behavior in this environment; a full hook framework is premature.
- **References:** External `master` commit `aaa38bc62053f5f7c1bfbcb60f0405f7cf0ee228`: `skills/planning-with-files/SKILL.md`, `templates/task_plan.md`, `templates/findings.md`, `templates/progress.md`, `docs/long-running-agent-tasks.md`, `docs/evals.md`, `docs/attestation-locking.md`, `SECURITY.md`, `scripts/resolve-plan-dir.sh`; GitHub latest release v3.29.1.
- **Next:** Draft revision 3 with a neutral assessment of all four options, an explicit fit matrix, evidence limitations, and a staged Option 3 recommendation. Keep implementation approval separate.

### 2026-11-25 02:26 UTC — Complete DRAFT-0002 revision 3 and validate its review state

- **Action:** Rewrote all four considered-option assessments with strengths, weaknesses, neutral factors, repository fit, evidence limits, and adoption cost. Added assessment criteria and a qualitative comparison matrix. Refreshed the external source snapshot and its benchmark/security caveats. Expanded the recommended Option 3 operating design, separated planning level from execution mode, made exclusions explicit, and updated review questions and revision history. Updated the Draft index.
- **Result:** DRAFT-0002 revision 3 is in-review and has been read back from GitHub. Checks confirmed all four option headings, assessment basis, comparative matrix, twelve operating-design sections, explicit automation exclusions, correct pinned source SHA, no duplicate headings, and pending approval metadata. Read-back also confirmed that the Draft index identifies revision 3; the task record and board are Blocked awaiting review; and the discussion register links revision 3, retains the separate drawing discussion, and records only verified success reports. A final branch comparison confirms that the post-merge gpt changes remain ahead of main while main still points to the verified merge commit. No ADR or implementation was created.
- **References:** `workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md`; `workspace/draft/README.md`; external commit `aaa38bc62053f5f7c1bfbcb60f0405f7cf0ee228`; release v3.29.1.
- **Next:** Present revision 3 for the user's decision. Keep DRAFT-0001 separate. Do not implement before approval of the exact revision and acceptance of its implementation ADR.

### 2026-11-25 07:11 UTC — Review the project hand-off and prepare the companion architecture Draft

- **Action:** Read master/Handoff.md and compared its area, project, task, resource, conversation, and archive proposals with the current Worker, Conversation Mode, task template, workspace, Draft/ADR governance, archive contract, Document Type Catalog, and the existing novel-area structure. Prepared the separate companion proposal DRAFT-0003.
- **Result:** DRAFT-0003 revision 1 is in-review. It recommends project folders with nested task folders, one global task board, task-level authority retained in TASK.md, optional task-local FINDINGS.md, project-level milestone/dependency planning, canonical resource promotion, global Draft/ADR governance, and exact-file task retention. It rejects word-for-word transcripts, project-local boards/ADRs, duplicate task PLAN/PROGRESS files in the first release, and whole-project 90-day deletion.
- **Approval-state discrepancy:** The discussion register records Option 3 of DRAFT-0002 as approved with added requirements. However, DRAFT-0002 revision 3 and its index still show in-review, and this task still records a blocked review state. DRAFT-0003 documents this discrepancy. Do not promote or implement either proposal until the exact approved DRAFT-0002 revision and scope are reconciled.
- **References:** master/Handoff.md; workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md; workspace/draft/README.md; skills/decision-governance/SKILL.md; workspace/DRAFT_TEMPLATE.md; workspace/adr/README.md; archive/README.md; novels/README.md; novels/WORKFLOW.md.
- **Commits:** DRAFT-0003 creation 65a5ee5021c9659535d1c9c8eff733b41432ec50; DRAFT-0003 reconciliation update ea028555265345d8d945133aaac014687360b391; Draft index c259604f5c331c12fa98215f244df66a5dc3fc6c.
- **Verification:** Read back the complete DRAFT-0003 and Draft index from gpt. Checked revision/status metadata, four full option assessments, common assessment dimensions, comparative matrix, user questions, evidence register, unique headings, and index links. No lint, CI workflow, or repository scripts were run.
- **Next:** Await the user's review of DRAFT-0003 revision 1 and reconcile the exact approved DRAFT-0002 revision and additions. Do not create an ADR or implement proposed changes without the required approval.

## 7. Current State

The external Planning with Files study and DRAFT-0002 revision 3 are complete. The user later approved Option 3 with additional requirements recorded in the discussion register: task-folder isolation, recovery from task records and associated ADRs, dedicated research evidence, and named plan directories/selectors for independently managed subtasks.

The user supplied master/Handoff.md and asked for a review and a separate, complementary proposal. DRAFT-0003 revision 1 now exists, is indexed, and is in-review. It defines the Area, Project, Task, Resource, Discussion, Decision Draft, ADR, and Archive boundaries and compares four viable hierarchy models. Its recommendation is project folders with nested task folders, one global task board, task-record authority, optional task-local findings, project-level coordination, global Draft/ADR governance, and exact-file task retention.

**Approval-state discrepancy:** workspace/discussion.md records DRAFT-0002 Option 3 as approved with added requirements, but DRAFT-0002 revision 3 metadata and the Draft index still show in-review. This task also remains Blocked pending user review. The exact approved revision and added scope must be reconciled before ADR promotion. DRAFT-0003 is a separate proposal and remains pending user review.

No implementation ADR has been created for these workflow changes. No Worker, template, task path, project folder, Ledger, archive, or foundational initialization changes have been implemented.

## 8. Remaining Work

- Await the user's review of DRAFT-0003 revision 1 and its exact scope.
- Resolve the DRAFT-0002 approval-state discrepancy. Confirm the exact approved revision and the additional requirements before changing its metadata or promoting it.
- Reconcile the DRAFT-0002 task execution, findings, and folder paths with DRAFT-0003. Do not create duplicate task-notes and task-local findings systems.
- Revise either Draft only when the user requests changes. Preserve its ID and increment its revision.
- Do not create an ADR or implement the proposed workflow until the relevant exact Draft revisions are approved and the implementation ADR is accepted.
- Preserve the separate open decision for DRAFT-0001.

## 9. Next Actions

1. Await the user's review of DRAFT-0003 revision 1.
2. Confirm the exact approved revision and scope of DRAFT-0002, including its added requirements.
3. Reconcile the two Drafts and proceed only through the global Draft-to-ADR process. Do not implement without an accepted ADR.

## 10. References

- External reference: https://github.com/othmanadi/planning-with-files
- `skills/SESSION_START.md`
- `skills/the-worker/SKILL.md`
- `skills/the-worker/references/conversation-mode.md`
- `skills/document-standards/SKILL.md`
- `skills/document-standards/references/document-type-catalog.md`
- `skills/agent-skill-authoring/SKILL.md`
- `workspace/README.md`
- `workspace/TASK_TEMPLATE.md`
- `workspace/task_board.md`
- `master/Handoff.md`
- `workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md`
- Related task: `20261124-103354`

## 11. Verification

- **Check:** DRAFT-0002 and DRAFT-0003 status, option coverage, architectural boundaries, cross-Draft consistency, index links, and task state.
- **Method:** Read the complete DRAFT-0003 and Draft index from branch gpt. Checked the four considered options, common assessment dimensions, comparative matrix, exact evidence register, user questions, unique headings, and metadata. Read the current task and task board. Compared the discussion register's DRAFT-0002 approval statement with the Draft metadata and task state.
- **Result:** DRAFT-0003 revision 1 and its index entry are present and read back. The proposal is in-review. The discussion register and DRAFT-0002 metadata/task state do not agree on whether the Option 3 decision has been formally applied to an exact revision. The discrepancy is recorded; no approval metadata was changed by inference. The task and board remain Blocked. No ADR or implementation was created.
- **Limitations:** No repository lint, CI workflow, or scripts were run. Read-back and structural checks do not establish user approval or validate future runtime behavior.

## 12. Handoff Instructions

Continue on branch gpt. The active review work is DRAFT-0002 revision 3 and its companion DRAFT-0003 revision 1. Read the exact Draft and global Draft index before changing either.

DRAFT-0003 is in-review and asks the user to decide the Area/Project/Task boundaries, nested project task paths, task-local findings location, task-ID selectors, resource promotion, and project/archive lifecycle. DRAFT-0002's task-plan and progress semantics remain the basis for the task record. The DRAFT-0003 proposal places optional FINDINGS.md beside TASK.md and does not create separate task PLAN.md or PROGRESS.md files.

The discussion register records DRAFT-0002 Option 3 as approved with added requirements, but its metadata and task state still show in-review/Blocked. Reconcile the exact approved revision and scope with the user before promotion. Do not silently change approval status.

Do not create an ADR, update Worker behavior, migrate task paths, create Project folders, change archive retention, update the Ledger renderer, or implement any proposed workflow until the relevant exact Draft approvals and accepted implementation ADR are in place. Keep DRAFT-0001 as a separate decision. Do not assume later gpt commits are on main.

## 13. Ledger Findings

_No Ledger findings are linked to this task._

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
