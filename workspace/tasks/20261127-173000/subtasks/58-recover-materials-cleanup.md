# Subtask: Recover task materials and clean temporary artifacts automatically

**Template version:** 1.5

## Metadata

- **ID:** 20261127-173000-58
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit instruction in this conversation to add this rule and update the workflow.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** Eligible — Ready, dependencies and authorization satisfied
- **Required:** Yes
- **Created:** 2026-11-28 06:50 UTC
- **Updated:** 2026-11-28 06:54 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

> Add this rule, whenever you need to recover materials for your task, recover them, but you must delete them immediately when you're done with the task. No need to ask for my permission. Update your workflow.

## 2. Subsequent Instructions

None.

## 3. Objective and Scope

Update the Worker workflow so it automatically retrieves task-required materials without seeking permission, and deletes temporary recovered copies or extracts immediately after their task use ends. Preserve canonical repository files and evidence governed by retention rules.

## 4. Acceptance Criteria

1. Worker instructions clarify automatic retrieval within the task's authorized scope.
2. Temporary recovered material is cleaned up immediately after use or task completion.
3. Cleanup does not delete canonical source files, user-owned originals, repository evidence, or materials whose retention is required by governance or explicit instructions.
4. Cleanup/readback and limitations are recorded, and changed files are verified.

## 5. Decisions and Progress

- Completed 2026-11-28 06:54 UTC. Updated The Worker, Conversation Mode, and Session Start. Updated subtask index, task board, and discussion register. Readback verified.
- Apply automatic recovery for materials needed to carry out an already authorized task. Recovery does not broaden the task's authority or scope.
- Remove temporary downloaded, extracted, copied, or staged recovery artifacts immediately when their task use ends. For materials used across several task steps, retain only until the last necessary step.
- Do not remove canonical source material, repository records, user-owned originals, or evidence subject to retention. When a deletion could affect canonical or user-owned material, preserve it and do not infer deletion authority.
- Implementation in progress.

## 6. State and Evidence

- **Commit SHA:** `9ecd0f75ffe7645b9049dcff7cacfb22edba5c99`, `2e5e836c339d548bdce30521232fc386238565c4`, `aae4009ad08ac6ff1f4e462cdc4cf3fc09737024`, `5faab1be3046a89240325675880d52bc19b1e040`, `578c50639c425c2d1544698cf05673aa68ec1a42`, `cf67438b845f339cc75905c8a79da577e5cace7d`
- **Changed paths:** `.agent/skills/the-worker/SKILL.md`; `.agent/skills/the-worker/references/conversation-mode.md`; `.agent/SESSION_START.md`; subtask index; task board; discussion register.
- **Readback:** Verified each updated file via remote fetch. The three workflow files contain the recovery/cleanup rules; index and board are updated.
- **Checks:** Not performed
- **Limitations:** No local scripts, tests, or lint will be run.

## 7. Completion

- **Status:** Done
- **Completed at:** Not applicable
- **Completion basis:** Workflow rule added to all three operational sources and readback verified.

## 8. Hosted Validation

Not applicable.

## 9. Handoff

Complete workflow updates, read back all changed files, and close out this child.

## 10. Ledger Findings

Not applicable.
