# Task: Apply CI P0 batch execution to session startup

## Metadata

- **Template version:** 1.3
- **ID:** 20261126-224100
- **Created:** 2026-11-26 22:41 UTC
- **Updated:** 2026-11-26 22:41 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Governing ADR(s):** None — direct user-authorized workflow maintenance
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** 20261126-223106
- **Ledger group:** None
- **Archived:** No

## 1. Original Request

“Approve. Apply it to thw workflow.”

## 2. Subsequent Instructions

- **2026-11-26 22:41 UTC:** The user approved the requirement for a pre-batch notice and asked to apply it to the formal workflow. The notice must tell the user that CI P0 batch execution is starting and ask them to wait until completion.

## 3. Objective

Update the canonical session-start procedure and its supporting policy so every /start runs the eligible CI-generated P0 batch before the assistant accepts the user's substantive prompt.

## 4. Requirements

1. Keep initialization conditional on the explicit /start cue.
2. After baseline initialization and required CI skill activation, send a clear pre-batch notice in every conversation mode.
3. Tell the user to wait until the assistant confirms readiness.
4. Execute all eligible CI Ledger-generated P0 tasks sequentially under the Worker batch procedure.
5. Respect task scope, dependencies, decision governance, safety, access, and destructive-action restrictions.
6. Continue independent eligible tasks when another task is blocked.
7. Commit remediation and update task records and the board.
8. Stop before hosted CI results review. Do not poll, dispatch, rerun, or inspect hosted results until the user triggers that phase.
9. After the batch ends, tell the user: “Ready to take your prompt.”
10. Keep the session-start file as the sole authority. Keep the initialization policy and Worker instructions consistent.

## 5. Decisions

- The pre-batch notice is mandatory in Default Mode and Condensed Mode.
- The batch includes only eligible CI Ledger-generated P0 tasks. It does not include unrelated P0 tasks.
- A blocked task does not stop independent eligible tasks.
- Completion of remediation does not mean hosted validation or task closeout is complete.

## 6. Progress Log

### 2026-11-26 22:41 UTC

- **Action:** Read the current session-start procedure, initialization policy, Worker batch procedure, Conversation Mode reference, CI workflow instructions, CI task board, task template, Agent Skill Authoring skill, and ASD-STE100 writing policy.
- **Result:** The Worker already owns P0 batch orchestration. The session-start procedure does not trigger the batch or require a pre-batch user notice.
- **References:** .agent/SESSION_START.md, .agent/INITIALIZATION_POLICY.md, .agent/skills/the-worker/SKILL.md, .agent/skills/the-worker/references/conversation-mode.md, .agent/skills/github-actions/SKILL.md, .agent/skills/agent-skill-authoring/SKILL.md, .agent/skills/asd-ste100/SKILL.md, .agent/skills/asd-ste100/references/repository-writing-policy.md, workspace/task_board.md.
- **Next:** Publish a committed Current Step brief, then update the three canonical instruction files.

## 7. Current State

The approved workflow change is not yet implemented. The existing Worker batch procedure is available for reuse.

## 8. Remaining Work

- Add the mandatory notice and automatic batch trigger to Session Start.
- Add the user-visible notice rule to The Worker.
- Align the initialization policy and revision history.
- Read back all changed files and the branch head.
- Record the result in the discussion register.

## 9. Next Actions

1. Publish the Current Step brief.
2. Update the session-start, Worker, and initialization policy files.
3. Read back the committed files and verify consistency.
4. Record the verified result and handoff.

## 10. References

- .agent/SESSION_START.md
- .agent/INITIALIZATION_POLICY.md
- .agent/skills/the-worker/SKILL.md
- .agent/skills/the-worker/references/conversation-mode.md
- .agent/skills/github-actions/SKILL.md
- .agent/skills/ci-ledger/SKILL.md
- workspace/discussion.md
- workspace/task_board.md

## 11. Verification

- **Check:** Read current canonical workflow and supporting policies.
- **Method:** Fetch exact files from branch gpt.
- **Result:** Read-back completed.
- **Limitations:** No edits have been committed yet. No CI validation was run or reviewed.

## 12. Handoff Instructions

Continue with the exact approved workflow update. Preserve the existing initialization sequence and Worker batch ownership. Do not run or inspect hosted CI results for this documentation change. After read-back, update the task and board. Keep this task open until its required repository checks are complete.

## 13. Ledger Findings

_No Ledger findings._