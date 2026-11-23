# Task: Consolidate foundational collaboration skills into The Worker

## Metadata

- **Template version:** 1.1
- **ID:** 20261123-112100
- **Created:** 2026-11-23 11:21 UTC
- **Updated:** 2026-11-23 11:21 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** 20261123-100738 — Remediate hard STE lint findings; 20261123-054904 — Build GitHub Actions diagnostic reports and remove the CI preflight gate
- **Archived:** No

## 1. Original Request

These are foundational skills, or candidates to be, at the moment
- the-worker
- session-archiving
- github-actions
- document-standards
- conversation-mode
- asd-ste100
- agent-skill-authoring

Identify which are foundational, which are on-demand. Make sure foundational skills are loaded when start session since they're foundational.

Except asd-ste100 & github-actions, do you think we should consolidate all of foundational skills into the-worker? Expand on this, then update your workflow.

Alos, update SESSION_START.md & INITIALIZATION_POLICY.md if needed.

## 2. Subsequent Instructions

No subsequent changes to scope.

## 3. Objective

Classify the seven candidate skills. Consolidate the baseline collaboration and session-start responsibilities into The Worker while retaining ASD-STE100 and GitHub Actions as separate foundational skills. Update the startup sequence, mandatory loading gate, indexes, and initialization policy.

## 4. Requirements

1. Keep initialization conditional on the explicit `start session` cue.
2. Load every foundational skill before project work after the cue.
3. Keep The Worker, ASD-STE100, and GitHub Actions as the foundational startup set.
4. Integrate Conversation Mode's mode selection, discussion-register ownership, and response rules into The Worker package.
5. Move the foundational startup gate and cross-cutting workspace rules from Session Archiving into The Worker.
6. Keep Session Archiving as an on-demand skill for conversation archives, drawing-session closeout, image provenance, and media workflows.
7. Keep Agent Skill Authoring and Document Standards on demand for their respective tasks.
8. Keep the existing skill paths usable. Replace absorbed entry points with clear compatibility guidance instead of duplicating operational instructions.
9. Update `skills/SESSION_START.md`, `skills/INITIALIZATION_POLICY.md`, skill metadata and indexes, and cross-references that define activation.
10. Preserve ASD-STE100 and GitHub Actions as separate foundational skills.
11. Preserve task authority, approval boundaries, workspace restrictions, and existing repository behavior.
12. Commit related changes to branch `gpt` in one coherent commit where practical.
13. Read back every changed path. Do not run CI or local lint. Validation remains task-scoped.

## 5. Decisions

- **Foundational:** The Worker, ASD-STE100, and GitHub Actions.
- **On demand:** Session Archiving, Agent Skill Authoring, and Document Standards.
- **Consolidated component:** Conversation Mode becomes a mandatory component of The Worker, not a separate foundational skill.
- **Startup cue:** Keep `start session`; do not enable automatic initialization at the beginning of a conversation.

## 6. Progress Log

### 2026-11-23 11:21 UTC

- **Action:** Inspected the startup procedure, initialization policy, skills index, and candidate skill definitions. Checked the task board, workspace instructions, and current execution record.
- **Result:** The current startup list loads six separate skills. Conversation Mode and Session Archiving provide baseline collaboration and initialization behavior that belongs in The Worker. Agent Skill Authoring and Document Standards are activated by specific authoring tasks and do not need to load at every session start. Session Archiving retains separate archive and media procedures.
- **References:** `skills/SESSION_START.md`, `skills/INITIALIZATION_POLICY.md`, `skills/session-archiving/SKILL.md`, `skills/conversation-mode/SKILL.md`, `skills/the-worker/SKILL.md`, `skills/agent-skill-authoring/SKILL.md`, `skills/document-standards/SKILL.md`, `skills/README.md`, `workspace/README.md`, `workspace/task_board.md`.
- **Next:** Integrate the foundational collaboration and startup behavior into The Worker. Update activation metadata, compatibility pointers, indexes, and initialization policy.

## 7. Current State

The classification and consolidation design are established. No project source files have been changed yet. The task is the current execution.

## 8. Remaining Work

- Integrate Conversation Mode and the mandatory startup gate into The Worker.
- Demote Session Archiving and Agent Skill Authoring to on-demand activation.
- Retain Document Standards as on-demand.
- Update all authoritative initialization and index files.
- Read back each changed path and reconcile any contradictions.

## 9. Next Actions

1. Update The Worker and its mandatory collaboration reference.
2. Update Session Archiving, Conversation Mode compatibility entry point, and Agent Skill Authoring activation metadata.
3. Update Session Start, Initialization Policy, Skills README, and Workspace README.
4. Read back all changed paths and report the commit.

## 10. References

- `skills/SESSION_START.md`
- `skills/INITIALIZATION_POLICY.md`
- `skills/the-worker/SKILL.md`
- `skills/session-archiving/SKILL.md`
- `skills/conversation-mode/SKILL.md`
- `skills/agent-skill-authoring/SKILL.md`
- `skills/document-standards/SKILL.md`
- `skills/README.md`
- `workspace/README.md`
- `workspace/task_board.md`
- Related active task: `workspace/tasks/20261123-100738-remediate-hard-ste-lint-findings.md`

## 11. Verification

- **Check:** Inspect candidate skills and current activation dependencies.
- **Method:** Retrieve exact files from branch `gpt` and inspect metadata, scope, loading rules, and cross-references.
- **Result:** Passed for the listed paths.
- **Limitations:** Changes and post-commit read-back remain pending.

## 12. Handoff Instructions

Continue the approved consolidation on branch `gpt`. Load The Worker as the one baseline collaboration skill, including its mandatory Conversation Mode reference. Keep ASD-STE100 and GitHub Actions as separate foundational skills. Do not load Session Archiving, Agent Skill Authoring, or Document Standards at ordinary session start. Preserve each on-demand skill for its specialist task. Verify every changed path after commit.
