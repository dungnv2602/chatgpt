# Subtask: Reconcile the skill directory index and activation metadata

**Template version:** 1.5

## Metadata

- **ID:** 20261127-173000-56
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Standing user authorization to continue the Refactor Skills parent. The portfolio audit identified this low-risk index and metadata correction.
- **Governing ADR(s):** None — index and frontmatter consistency only. No activation policy changes.
- **Dependencies:** Child 55 audit completed.
- **Eligibility / deferral reason:** In Progress — selected as the next Refactor Skills child after the portfolio audit.
- **Required:** Yes
- **Created:** 2026-11-27 18:05 UTC
- **Updated:** 2026-11-27 18:05 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

> Continue with the Refactor Skills task.

## 2. Subsequent Instructions

The full user instruction is preserved in the parent task's Subsequent Instructions.

## 3. Objective and Scope

Make `.agent/skills/README.md` a complete index of the active skill portfolio. Preserve the existing foundational and specialist dependency hierarchy. List each task-specific skill once with an accurate activation summary.

Correct the ASD-STE100 `project-role` metadata to match its task-activated loading policy. Move Prompt Master's version field under the Agent Skills `metadata` mapping.

Do not change skill activation behavior, merge skills, or rewrite skill content in this task.

## 4. Acceptance Criteria

1. The index accounts for all 17 active skill directories exactly once.
2. The foundational, Drawing, and Novelist dependency hierarchy remains accurate.
3. The task-specific table lists every remaining skill and states its activation boundary.
4. Remove the duplicate Romantic Storyteller entry from the task-specific table.
5. Set ASD-STE100 `project-role` to `task-specific`.
6. Move Prompt Master's version to `metadata.version`.
7. Preserve every skill name and description. Keep all descriptions within 1,024 characters.
8. Read back every changed path. Do not run local scripts or tests.

## 5. Decisions and Progress

- **Execution:** Approved within the standing Refactor Skills parent.
- **Boundary:** This task updates discoverability and metadata only. It does not change skill activation or merge capabilities.

## 6. State and Evidence

- **Commit SHA:** Not committed.
- **Changed paths:** Pending.
- **Readback:** Pending.
- **Checks:** Not performed.
- **Limitations:** No local validation or hosted CI review.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Handoff

After closeout, prepare separate tasks for the skill-authoring overlap and ChatGPT platform compatibility findings. Do not change activation policy without user approval.

## 9. Ledger Findings

Not applicable.
