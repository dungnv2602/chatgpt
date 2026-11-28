# Subtask: Consolidate Session Start and Conversation Mode

**Template version:** 1.5

## Metadata

- **ID:** 20261127-173000-59
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** The user's explicit request to make Session Start pointer-only, limit Conversation Mode to settings, relocate duplicated operating rules to their proper Worker or specialist owners, and reassess and reconcile the workflow.
- **Governing ADR(s):** ADR-0005 — Lean Session Start and Conversation Mode
- **Dependencies:** None
- **Eligibility / deferral reason:** In Progress — preparing the decision Draft under the user's direct instruction.
- **Required:** Yes
- **Created:** 2026-11-27 23:53 UTC
- **Updated:** 2026-11-27 23:55 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

This child belongs under the standing Refactor Skills parent because it directly refactors the repository's foundational skill and session instructions.

## 1. Original Prompt

> Session start and conversation mode should be absolutely lean.
>
> Session start should only contisn pointer and reading skills instructions based on my cue. Conversation mode should only have conversation settings.
>
> Identify redundancy in them and relocate to appropriate places in the Worker.
>
> Reassess your workflow, check if it already contains how you should work before, identify gaps why you didn't follow it, reconcile and refactor with what you recently added. No redundancy, refactor and optimize your workflow.

## 2. Subsequent Instructions

### 2026-11-28

> Approve

> You also need to update associated templates

> Approve

> Execute

- **Decision:** Approved DRAFT-0006 Revision 1 and ADR-0005. Execution scope includes associated templates and the drift-prevention self-check.

## 3. Objective and Scope

Prepare one decision Draft for the requested workflow architecture. The proposal must make Session Start a cue guard and pointer to The Worker, limit Conversation Mode to presentation settings, and place operational authority in The Worker and its existing Worker-owned or specialist references.

The review must reconcile the recently added recovery-cleanup and sequential decision-collection rules with existing task, startup, skill-loading, and CI instructions. It must remove contradictory or duplicated live instructions rather than copy the same rule into another file.

This task implements the approved architecture and associated template reconciliation under ADR-0005.

## 4. Acceptance Criteria

1. The Draft assesses the current architecture, no-change, full centralization in the Worker, and a Worker-owned single-source architecture that uses existing focused references for detailed procedures.
2. The Draft records the observed instruction conflicts and the correct ownership boundary for each procedure.
3. The Draft identifies all affected canonical files and explains their proposed roles.
4. The Draft preserves cue-controlled initialization, progressive skill loading, the startup P0 batch, user-decision collection before batch execution, immediate temporary-material cleanup, and the existing restrictions on local validation and hosted CI review.
5. The Draft states exact non-goals, implementation order, verification limits, and confirmation criteria.
6. The accepted ADR governs implementation.
7. Session Start and Conversation Mode have the approved lean boundaries.
8. Operational instructions, specialist references, indexes, templates, and board are reconciled without duplicated authority.
9. The changed paths pass remote readback.

## 5. Decisions and Progress

### 2026-11-28 — approval and implementation

- The user approved DRAFT-0006 Revision 1 and added template reconciliation to scope, then explicitly instructed execution.
- ADR-0005 was provisionally created, read back, accepted, and verified. ADR commit: `142b6ccdc82a5f3a66e77d395f587eeb92c0d5e6`.
- Refactored Session Start to a cue guard and Worker pointer. Conversation Mode now contains presentation settings only.
- Added Worker canonical ownership, initialization routing, pre-action self-check, and drift/contradiction gate.
- Preserved novelist and drawing-session instructions in focused Worker references.
- Updated initialization policy, skills index, catalog, task/subtask/discussion/task-board templates, live task board, and ADR index.
- Hosted CI results were not inspected. Local scripts, tests, and lint were not run.

## 5. Decisions and Progress

### 2026-11-27T23:55:36Z — Draft prepared and indexed

- Created DRAFT-0006 Revision 1 using the canonical Draft template. The proposal recommends a Worker-owned operating model, a cue-pointer-only Session Start, and a settings-only Conversation Mode.
- Readback confirmed the Draft includes all three options, the exact approval gate, impact map, implementation outline, and evidence register.
- Draft commit: `dd2e36a071f1214fd23bc83b97e47fe18986eb24`.
- Draft index commit: `d7ad84f13339b8fe958921d3ad88f8237113d75a`.
- Discussion register commit: `a8f17f4b3fbd056bba3eee9f0e0cc7966e9366e3`.
- Task index commit: `ce8f9981f2b61c4bc4914ea67ff3d89217a65ca0`.
- Task board commit: `a48f629e360e5e5e8410ddad61187d89a47ebb07`.
- Parent progress commit: `d2c2a63741c2ee2777a79eb60ac01a49b3fc264c`.
- Next: present the exact Draft for user approval. No implementation is authorized yet.

### 2026-11-27T23:53:02Z — task captured

- Created this decision-preparation child under the persistent Refactor Skills parent.
- Audited Session Start, Conversation Mode, The Worker, Initialization Policy, the Skills Directory index, the document-type catalog, and the task-board contract.
- Found a direct conflict: Session Start step 8 resumes execution after the first blocker answer. Its step 10 and The Worker require all user-resolvable calls to be collected before executing newly unlocked work.
- Found duplicated operational ownership for cleanup, task progression, blocker coordination, approval cues, repository discipline, startup CI handling, skill loading, and the discussion register.
- Next: prepare and present Draft DRAFT-0006. Do not implement until its exact revision receives approval and the resulting ADR is accepted.

## 6. State and Evidence

- **Commit SHA:** Draft `dd2e36a071f1214fd23bc83b97e47fe18986eb24`; supporting task and register commits listed in Decisions and Progress.
- **Changed paths:** This subtask record, parent task, parent subtask index, task board, DRAFT-0006, draft index, and workspace/discussion.md.
- **Readback:** Draft, draft index, discussion register, task index, task board, parent task, and this subtask were fetched from branch gpt after their writes. Draft content and key approval markers were confirmed.
- **Checks:** Repository source review only. No scripts, tests, lint, or hosted CI review.
- **Limitations:** The audit establishes the content and contradictions in the retrieved branch files. It does not establish hosted validation results or client-side skill-loader behavior.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Draft DRAFT-0006 is read back and presented for an explicit user decision. Implementation remains outside this child.

## 8. Hosted Validation

Conditional: CI remediation only.

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Handoff

DRAFT-0006 Revision 1 is in review and linked from workspace/discussion.md. Await the user's decision. If approved, follow the Worker execution cue and decision-governance gate. Promote the exact revision to an accepted ADR before creating a separate implementation child. Do not implement the proposed refactor before that gate passes.

## 10. Ledger Findings

No CI finding is assigned to this decision-preparation task.
