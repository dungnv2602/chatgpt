# Subtask: Clarify implementation closeout, verification debt, and mandatory queue continuation

**Template version:** 1.6

## Metadata

- **ID:** 20261127-173000-62
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** Done
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User approved the proposed workflow improvements and instructed execution.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** Eligible — Ready, approved and no dependencies
- **Required:** Yes
- **Created:** 2026-11-28
- **Updated:** 2026-11-28
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

> I want you to stop standing still, I need you to move on another unblocked task immediately when a task is considered done. The problem right now is you standing here reporting to me you will not mark a task done without results validation when we agreed to let the worker to handle errors through CI task generation for you.
>
> Assess the workflow, bring me improvements suggestions.

## 2. Subsequent Instructions

> Approve
>
> Execute

## 3. Objective and Scope

Revise Worker lifecycle instructions and associated templates/reference contracts so implementation completion is distinct from runtime validation evidence and completing an authorized task triggers mandatory immediate queue rebuilding and continuation to quiescence.

Scope: Worker skill, task/subtask templates, board template, and GitHub Actions reference. Avoid a second scheduler or unrelated refactoring.

## 4. Acceptance Criteria

1. Define implementation closeout based on deliverable criteria, intended-branch commit, and readback, without making unperformed runtime validation a universal gate.
2. Track validation gaps separately as verification debt or follow-up, preserving evidence boundaries and genuine criteria-specific verification gates.
3. Make post-completion scheduling a mandatory immediate transition. No authorized execution batch may stop while an eligible task within its focus remains.
4. Clarify CI-generated remediation handoff into the same Worker's queue.
5. Update associated templates and references with minimal duplication and canonical ownership.
6. Read back every changed path and reconcile task/index/board records.
7. Preserve restrictions on local tests/scripts and hosted CI inspection.

## 5. Decisions and Progress

### 2026-11-28

- **Action:** Created this approved child following the user's approval and execution instruction.
- **Result:** Executing the bounded lifecycle revision.
- **References:** The Worker skill, task templates, board template, and GitHub Actions reference.
- **Next:** Implement and readback.

## 6. State and Evidence

- **Commit SHA:** Readback commits: `68b00ab984e2c8eac2724247bca62525dbfd071f`, `fa9f8dfd52f8fd013306fd2db29533430c4f2d46`, `3b7f145e3b02c82aa7919cd1c0c2d0dca934faf2`, `2ae6f37f62e4c108c91aee5649283acc7347274a`, `575d27d953318175031f89284cad19b42eb0571a`
- **Changed paths:** `.agent/skills/the-worker/SKILL.md`, `.agent/skills/the-worker/assets/TASK_TEMPLATE.md`, `.agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md`, `.agent/skills/the-worker/assets/TASK_BOARD_TEMPLATE.md`, `.agent/skills/the-worker/references/github-actions.md`
- **Readback:** All five changed paths were fetched from `gpt` after commits and confirmed available.
- **Checks:** Not performed. Local execution and hosted CI review remain restricted.
- **Limitations:** Readback verifies repository content, not runtime behavior or hosted CI.

## 7. Completion

- **Status:** In Progress
- **Completed at:** Not applicable
- **Completion basis:** Criteria satisfied by implementation and readback. Validation execution remains unperformed by policy.

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Execution self-check

Canonical Worker ownership and template-first requirements were read. Parentage and approval are explicit. Scope is bounded. No local scripts, tests, lint, or hosted CI inspection will be performed. Readback and cleanup will follow repository commit operations.

## 10. Handoff

Close after all acceptance criteria pass and readback confirms the intended-branch content. Rebuild the authorized Refactor Skills queue immediately.

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
