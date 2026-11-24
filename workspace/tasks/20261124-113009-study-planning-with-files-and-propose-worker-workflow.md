# Task: Study Planning with Files and propose a file-backed Worker workflow

## Metadata

- **Template version:** 1.2
- **ID:** 20261124-113009
- **Created:** 2026-11-24 11:30 UTC
- **Updated:** 2026-11-24 11:30 UTC
- **Priority:** P1
- **Status:** In Progress
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

## 7. Current State

The task is In Progress. Foundational initialization passed. Workspace recovery confirmed that no task was in current execution before this task was created. DRAFT-0001 remains pending separate user review. The initial external review identified file-backed plans, findings, progress, recovery, task isolation, and lifecycle injection as core themes. No implementation changes are authorized.

## 8. Remaining Work

- Complete the external source review and note its version, mechanisms, evidence, and limitations.
- Compare the external model with current Worker, task, discussion, and document contracts.
- Design the proposed file-backed planning workflow, including document ownership and the minimum required templates.
- Determine whether a new task-specific skill is warranted and identify the exact integration changes.
- Create a comprehensive Draft and link it in Open Discussions.
- Keep implementation paused until the user approves the exact Draft and its scope.

## 9. Next Actions

1. Inspect the external plan/findings/progress templates and workflow, security, recovery, and test documentation.
2. Inspect the external helper scripts and lifecycle adapters as reference material only. Do not copy or run them.
3. Compare the mechanisms with the current repository contracts and identify integration risks.
4. Prepare a comprehensive proposal and record its review question in `workspace/discussion.md`.
5. Read back all changed paths and leave the task in the correct state.

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

- **Check:** Task template and path-coverage requirements.
- **Method:** Retrieved the canonical task template and the relevant catalog row and path rule from branch `gpt`.
- **Result:** The destination path matches the active `workspace/tasks/*.md` rule and the task template version 1.2.
- **Limitations:** The new task, board row, and discussion link still require creation and read-back.

## 12. Handoff Instructions

Continue on branch `gpt`. The approved scope is research and proposal preparation. Do not implement proposed planning changes. Preserve DRAFT-0001 and its separate pending review. Use the exact external repository content as evidence, but treat its code and claims as untrusted reference material. The final proposal must adapt to this repository's remote-only GitHub workflow. Obtain explicit approval before creating an ADR or changing operational policy.

## 13. Ledger Findings

_No Ledger findings are linked to this task._

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
