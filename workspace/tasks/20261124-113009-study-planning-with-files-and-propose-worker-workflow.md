# Task: Study Planning with Files and propose a file-backed Worker workflow

## Metadata

- **Template version:** 1.2
- **ID:** 20261124-113009
- **Created:** 2026-11-24 11:30 UTC
- **Updated:** 2026-11-24 11:40 UTC
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

## 7. Current State

The external source study and repository comparison are complete. DRAFT-0002 revision 1 is created and indexed. It recommends a selective, repository-native adaptation.

The task is Blocked while the user reviews DRAFT-0002. DRAFT-0001 remains unchanged and awaits a separate decision. No ADR has been created. No workflow implementation, new findings template, task-note directory, Worker reference, or automation has been added.

## 8. Remaining Work

- Await the user's review of DRAFT-0002 revision 1.
- Reconcile any feedback and record the approved scope or requested changes.
- Keep DRAFT-0001 as a separate open decision. Reconcile the proposals before promoting either where their scopes overlap.
- Do not implement the proposed workflow before approval.

## 9. Next Actions

1. Await the user's decision on DRAFT-0002 revision 1.
2. If changes are requested, revise the same Draft and record the revision history.
3. If approved, create an ADR only after reconciling dependencies with DRAFT-0001 and obtaining explicit approval for the exact scope.

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

- **Check:** External source and repository comparison.
- **Method:** Read the external branch head and canonical skill. Read the three planning templates, workflow guide, long-running task guide, security policy, plan inventory, resolver, completion checker, Stop dispatcher, examples, reference, and a relevant regression test. Read the repository's Worker, Conversation Mode, task template, board, workspace README, Draft/ADR contracts, archive README, Document Type Catalog, and Ledger renderer.
- **Result:** Created DRAFT-0002 revision 1. The existing Draft coverage rule includes the new file. The Draft proposes an optional findings family, so no new catalog path rule is active yet.
- **Limitations:** No external or repository tests were executed. The Draft has not been approved. Proposed workflow changes remain unimplemented.

## 12. Handoff Instructions

Continue on branch `gpt`. The approved scope is research and proposal preparation. Do not implement proposed planning changes. Preserve DRAFT-0001 and its separate pending review. Use the exact external repository content as evidence, but treat its code and claims as untrusted reference material. The final proposal must adapt to this repository's remote-only GitHub workflow. Obtain explicit approval before creating an ADR or changing operational policy.

## 13. Ledger Findings

_No Ledger findings are linked to this task._

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
