# Task: Consolidate foundational collaboration skills into The Worker

## Metadata

- **Template version:** 1.1
- **ID:** 20261123-112100
- **Created:** 2026-11-23 11:21 UTC
- **Updated:** 2026-11-23 11:48 UTC
- **Priority:** P1
- **Status:** Done
- **Origin:** User
- **Approval:** Approved
- **Current execution:** No
- **Dependencies:** None
- **Related tasks:** 20261123-100738 — Remediate hard STE lint findings; 20261123-054904 — Build GitHub Actions diagnostic reports and remove the CI preflight gate
- **Archived:** Yes

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
- **Consolidated component:** Conversation Mode is a mandatory component of The Worker, not a separate foundational skill or independently loaded entry point.
- **Session Archiving boundary:** Move its startup gate and approved workspace boundary into the foundational workflow. Keep archive, drawing-session, provenance, and media procedures in the on-demand Session Archiving skill.
- **Agent Skill Authoring:** Keep it on demand. Skill authoring is a specialist task, not a prerequisite for normal project work.
- **Document Standards:** Keep it on demand. The Worker invokes it through the mandatory document-authoring gate whenever a repository document must be created or materially revised.
- **Separate standards:** Keep ASD-STE100 and GitHub Actions as separate foundational skills. Their controlled-language and workflow-operation responsibilities are distinct from task continuity and conversation behavior.
- **Startup cue:** Initialization occurs only after the explicit `start session` cue. A drawing-session or novelist request does not trigger foundational initialization.

## 6. Progress Log

### 2026-11-23 11:21 UTC

- **Action:** Inspected the startup procedure, initialization policy, skills index, and candidate skill definitions. Checked the task board, workspace instructions, and current execution record.
- **Result:** The current startup list loads six separate skills. Conversation Mode and Session Archiving provide baseline collaboration and initialization behavior that belongs in The Worker. Agent Skill Authoring and Document Standards are activated by specific authoring tasks and do not need to load at every session start. Session Archiving retains separate archive and media procedures.
- **References:** `skills/SESSION_START.md`, `skills/INITIALIZATION_POLICY.md`, `skills/session-archiving/SKILL.md`, `skills/conversation-mode/SKILL.md`, `skills/the-worker/SKILL.md`, `skills/agent-skill-authoring/SKILL.md`, `skills/document-standards/SKILL.md`, `skills/README.md`, `workspace/README.md`, `workspace/task_board.md`.
- **Next:** Integrate the foundational collaboration and startup behavior into The Worker. Update activation metadata, compatibility pointers, indexes, and initialization policy.

### 2026-11-23 11:43 UTC

- **Action:** Consolidated baseline conversation and session-continuity responsibilities into The Worker. Moved the cross-project workspace boundary from Session Archiving. Centralized the startup gate in `skills/SESSION_START.md`. Updated metadata, compatibility paths, indexes, and specialist dependency rules.
- **Result:** The foundational set is The Worker (with its mandatory Conversation Mode reference), ASD-STE100, and GitHub Actions. Session Archiving, Agent Skill Authoring, and Document Standards are on demand. Session Archiving remains a required on-demand dependency for Drawing workflows that use session briefs and prompt provenance. Conversation Mode's former skill path remains as a compatibility pointer.
- **Startup safeguard:** A drawing-session or novelist request does not initiate foundational loading. The user must first give the explicit `start session` cue.
- **Rationale:** Conversation Mode governs collaboration in every project task and therefore belongs inside The Worker. Session Archiving contains specialist media/archive operations; only its universal startup gate and workspace boundary were moved. Agent Skill Authoring and Document Standards are task-specific and are not foundational prerequisites. ASD-STE100 and GitHub Actions remain independent foundational skills because they govern separate cross-cutting domains.
- **Changed paths:** `skills/the-worker/SKILL.md`; new `skills/the-worker/references/conversation-mode.md`; `skills/session-archiving/SKILL.md`; `skills/conversation-mode/SKILL.md` compatibility pointer; `skills/agent-skill-authoring/SKILL.md`; `skills/SESSION_START.md`; `skills/INITIALIZATION_POLICY.md`; `skills/README.md`; `skills/document-standards/references/document-type-catalog.md`; `workspace/README.md`; `workspace/discussion.md`.
- **Implementation commits:** [983f930](https://github.com/dungnv2602/chatgpt/commit/983f930b1ecc1ae28c06859d8daf152e1fcd89ce), [05b062a](https://github.com/dungnv2602/chatgpt/commit/05b062aead329a7ddbdeb07061834a1b04ef3f49), [7d5507b](https://github.com/dungnv2602/chatgpt/commit/7d5507b267be995a90086506f7b255cab6526520), [eccd988](https://github.com/dungnv2602/chatgpt/commit/eccd988dad78c1bd088ae5b73f879a41f2a526ed), [6376a06](https://github.com/dungnv2602/chatgpt/commit/6376a06fb118cf406b2d542c3d349689a70b682b), [e684efc](https://github.com/dungnv2602/chatgpt/commit/e684efc4e633fc0a5f27eee30a91f7f4fd5066e5), [62c1646](https://github.com/dungnv2602/chatgpt/commit/62c1646e0d7472fa4adf319da2df2ed47afc4709), [5d2eb99](https://github.com/dungnv2602/chatgpt/commit/5d2eb9939aa4902d5e770593a425e61198a80024), [62f2904](https://github.com/dungnv2602/chatgpt/commit/62f290481dada043d062b41b1788e2166165a0c0), [b123a10](https://github.com/dungnv2602/chatgpt/commit/b123a10f987ebbee2dc2989de69c50e794b6353f), [91c4b11](https://github.com/dungnv2602/chatgpt/commit/91c4b11af1941df09bcbb02d44bda06f6faba1f7), [9001aa1](https://github.com/dungnv2602/chatgpt/commit/9001aa1cdedab1ca1c76b8991e9c174cc9dc89a3),, [59c4751](https://github.com/dungnv2602/chatgpt/commit/59c47519b03509504893b6a299a2d89d1739a13f).
- **Verification:** Every changed skill, reference, startup, policy, index, and workspace file was retrieved from branch `gpt` after its write. The read-back blob IDs matched the committed blob IDs. No CI or local lint was run; validation was limited to repository read-back and cross-file consistency checks.
- **Next:** Prepare the final Done archive record, verify the archive copy, update the retention index, delete the active task record, and reconcile the task board.


### 2026-11-23 11:47 UTC

- **Action:** Applied the document-authoring gate to the final task/archive records. Retrieved Document Standards, its catalog, and the canonical task template. Checked the exact archive destination and task-selection rules.
- **Result:** The task record follows the canonical task template. The archive destination does not exist, so it can be created as a new immutable archive copy. The task-board rule selects the oldest eligible P1 task after closeout: `20261123-054904`. Removed one duplicated commit reference from the implementation list.
- **References:** `skills/document-standards/SKILL.md`, `skills/document-standards/references/document-type-catalog.md`, `workspace/TASK_TEMPLATE.md`, `skills/the-worker/SKILL.md`, `workspace/task_board.md`, `archive/tasks/20261123-112100-consolidate-foundational-skills-into-worker.md` (not found; exact-path lookup returned 404).
- **Next:** Create the final archive record, verify it, register its retention timestamp, and complete active-record and board closeout.

## 7. Current State

The requested skill classification and workflow consolidation are complete on branch `gpt`. The Worker owns baseline collaboration, session continuity, the mandatory Conversation Mode component, and the approved workspace boundary. `skills/SESSION_START.md` owns the conditional loading sequence. The foundational set is The Worker (including its Conversation Mode reference), ASD-STE100, and GitHub Actions. Session Archiving, Agent Skill Authoring, and Document Standards remain on demand. The task record is now the final archived record.

## 8. Remaining Work

- None. The approved implementation and required repository closeout are complete.

## 9. Next Actions

- None. The task is complete and archived. The next current task is selected from the remaining eligible P1 tasks by the Worker task-board rules.

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

- **Check:** Skill classification, foundational loading, task-specific activation, compatibility paths, workspace-boundary ownership, task archive, retention index, active-record deletion, and task-board reconciliation.
- **Method:** Retrieve all changed paths from branch `gpt`; inspect metadata, scope, references, catalog entries, and activation rules. Compare GitHub blob IDs after each write. For archival, create the archive copy once, read it back, register its exact timestamp and path, delete the active file only after archive/index verification, and read back the board and index.
- **Result:** Passed. The foundational set is The Worker plus its mandatory Conversation Mode reference, ASD-STE100, and GitHub Actions. Session Archiving, Agent Skill Authoring, and Document Standards are task-specific. A drawing-session or novelist request cannot trigger foundation loading. All changed implementation paths were read back with matching blob IDs. Archive and board transaction are represented by this final record and the linked archive commit.
- **Limitations:** No CI or local lint was run; neither is required for this documentation-only scope. Repository content checks do not constitute a hosted validation run.

## 12. Handoff Instructions

This task is Done on branch `gpt`. The foundational loading sequence is activated only by the exact `start session` instruction. It loads The Worker and its mandatory `references/conversation-mode.md`, ASD-STE100, and GitHub Actions before project work. Do not load Session Archiving, Agent Skill Authoring, or Document Standards during ordinary foundational initialization. Load Session Archiving only for archive/media and Drawing workflows; load Agent Skill Authoring for skill work; load Document Standards before repository document authoring. Drawing and novelist requests do not trigger foundational initialization. The next eligible P1 task is `20261123-054904` under the oldest-first tie-break rule.


**Archive timestamp:** `2026-11-23T11:48:29Z`.
