# Task: Study Planning with Files and propose a file-backed Worker workflow

## Metadata

- **Template version:** 1.2
- **ID:** 20261124-113009
- **Created:** 2026-11-24 11:30 UTC
- **Updated:** 2026-11-25 02:26 UTC
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
- **2026-11-24:** The user supplied `https://github.com/othmanadi/planning-with-files` as the external reference and requested a thorough study.
- **2026-11-24:** The user asked for a comprehensive, repository-specific workflow proposal, including templates and affected skills or a new skill where useful.
- **2026-11-24:** The user started the session explicitly.

- **2026-11-25:** The user instructed: "Start session / Merge gpt to main / Then https://github.com/dungnv2602/chatgpt/blob/gpt/workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md#considered-options / Give me an updated draft in which you give me detailed assessments about all available options."

## 3. Objective

Study Planning with Files and determine how its durable planning, research capture, progress logging, recovery, task isolation, error handling, and verification controls can improve this repository's Worker and workspace workflow. Prepare an exhaustive proposal that fits the repository's remote-only GitHub operating model and existing approval gates.

## 4. Requirements

1. Study the external repository's current canonical skill, templates, documentation, release/lifecycle design, recovery model, modes, security boundaries, and relevant tests.
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

## 5. Decisions

- **Approved:** Study the supplied external project.
- **Approved:** Inspect and compare the current Worker and workspace workflow.
- **Approved:** Prepare a comprehensive proposal for user review.
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
- **Result:** DRAFT-0002 revision 3 is in-review and has been read back from GitHub. Checks confirmed all four option headings, assessment basis, comparative matrix, twelve operating-design sections, explicit automation exclusions, correct pinned source SHA, no duplicate headings, and pending approval metadata. The Draft index now identifies revision 3. No ADR or implementation was created.
- **References:** `workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md`; `workspace/draft/README.md`; external commit `aaa38bc62053f5f7c1bfbcb60f0405f7cf0ee228`; release v3.29.1.
- **Next:** Present revision 3 for the user's decision. Keep DRAFT-0001 separate. Do not implement before approval of the exact revision and acceptance of its implementation ADR.

## 7. Current State

The external source study and repository comparison are complete. DRAFT-0002 revision 3 is complete, read back, indexed, and in-review. It contains detailed assessments of all four considered options, a qualitative comparison matrix, refreshed source/evaluation limits, and a staged Option 3 operating design.

The user-authorized fast-forward merged the gpt commit into main. The branches matched at `3bce922cb6348e38e04ea7c2d43597af9d908fc3` immediately after the merge. Subsequent task and Draft review changes are committed to gpt only. The user did not request a second merge.

The task is Blocked while the user reviews revision 3. DRAFT-0001 remains a separate open decision. No implementation ADR has been created for DRAFT-0002. No proposed workflow, template, skill, Ledger, or archive changes are approved.

## 8. Remaining Work

- Await the user's decision on DRAFT-0002 revision 3 and its exact scope.
- If the user requests changes, revise the same Draft ID and increment its revision. Keep it in-review.
- If the user approves it, reconcile any overlap with DRAFT-0001 before creating the implementation ADR under the accepted governance process.
- Do not implement the proposed workflow before the exact Draft approval and an accepted implementation ADR.
- Preserve DRAFT-0001 as a separate open decision until its own review is resolved.

## 9. Next Actions

1. Await the user's decision on DRAFT-0002 revision 3.
2. Record the decision against the exact revision and scope.
3. Proceed only through the Draft-to-ADR process. Do not implement without an accepted implementation ADR.

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
- Related task: `20261124-103354`

## 11. Verification

- **Check:** DRAFT-0002 revision 3 content, option coverage, review metadata, source references, and Draft index.
- **Method:** Read the complete Draft and index back from the GitHub repository. Checked for revision 3 and in-review status; all four option sections; the assessment criteria and external evidence caveats; the comparative matrix; all twelve operating-design sections; explicit scope exclusions; unique headings; correctly pinned external source SHA; revision history; and pending user approval. Read back the Draft index entry.
- **Result:** The checks passed. Revision 3 remains in-review; user decision is pending; approved scope is not approved; no resulting ADR exists. The Draft index points to the revision 3 document. No implementation files were changed.
- **Limitations:** No repository lint workflow, GitHub Actions validation, or external/repository tests were run. Read-back and structural checks do not establish that the user accepts the recommendation.

## 12. Handoff Instructions

Continue on branch `gpt`. The approved scope now includes revising DRAFT-0002 after the user's explicit request for detailed assessments of all available options. Keep the existing task ID and DRAFT-0002 ID. Preserve DRAFT-0001 and its separate pending review. Do not create an implementation ADR or implement proposed changes before the user approves the exact Draft revision and the repository accepts its implementation ADR. The post-merge `main` ref was verified equal to `gpt` at `3bce922cb6348e38e04ea7c2d43597af9d908fc3`; do not assume later gpt-only edits are already on main.

## 13. Ledger Findings

_No Ledger findings are linked to this task._

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
