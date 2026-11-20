# Task: Fix Condensed Mode adherence gaps

## Metadata

- **ID:** 20261120-153700
- **Created:** 2026-11-20 15:37 UTC
- **Updated:** 2026-11-20 15:37 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** 20261120-123000
- **Archived:** No

## 1. Original Request

> Check your workflow to fix this any gaps regarding this matter

## 2. Subsequent Instructions

None.

## 3. Objective

Inspect the Condensed Mode workflow and correct any instruction gaps that could cause the assistant to ignore a valid mode selection or violate Condensed Mode output rules.

## 4. Requirements

- Preserve conditional initialization and the sole `start session` cue.
- Preserve the rule that a new conversation defaults to Default Mode unless an explicit user selection or session handoff carries another mode.
- Accept the user's natural-language mode cues, including the prefix form `Conversation mode: condensed mode`.
- Require mode resolution before processing the rest of each prompt and before composing any user-visible output.
- Resolve the conflict between the required transition acknowledgement and Condensed Mode's link-only output.
- Resolve the conflict between the link-only output rule and the no-commit/no-change/error reporting rules.
- Keep `workspace/discussion.md` access under Conversation Mode. Do not let The Worker read or write it.
- Do not change unrelated mode policy, initialization cues, or repository boundaries.
- Fetch and verify every changed path from branch `gpt`.

## 5. Decisions

- The prior mode cue was valid. The observed failure was an execution failure, not a cue-recognition failure.
- The current skill contains contradictory user-visible output requirements. A transition acknowledgement exception and a single-link rule for all later Condensed Mode responses will resolve this conflict.
- The mode check will be made an explicit per-turn gate. This strengthens the existing mode policy without changing its default or persistence rules.

## 6. Progress Log

### 2026-11-20 15:37 UTC

- **Action:** Read the current discussion register, Conversation Mode skill, Session Start procedure, The Worker skill, Initialization Policy, workspace instructions, task board, task template, and the active documentation-audit task.
- **Result:** Conversation Mode is already a foundational skill loaded by the explicit `start session` procedure. The user's earlier cue `Conversation mode: condensed mode` is covered by the existing natural-language cue rule. The failure therefore was not caused by a missing foundational dependency.
- **Findings:** Section 4 requires an acknowledgement when switching modes, while Section 3 prohibits all chat text except one direct link. The no-commit rule also requires a sentence in chat, which conflicts with the link-only rule. The skill has no explicit per-turn mode-resolution gate before response composition.
- **CI snapshot:** Branch head was `56e58a688135d0bb90cadefb9a2a8cca77e442d3`. The newest available changed-document run was `44763230785`, successful on `808d1bca5ddb3af15ef9ddaf3f57cbc7ddb09282`. The current branch head had no corresponding run in the bounded snapshot. No CI result was awaited.
- **References:** `skills/conversation-mode/SKILL.md`, `skills/SESSION_START.md`, `skills/the-worker/SKILL.md`, `skills/INITIALIZATION_POLICY.md`, `workspace/README.md`, `workspace/task_board.md`, `workspace/TASK_TEMPLATE.md`, `workspace/tasks/20261120-123000-repository-documentation-audit.md`.
- **Next:** Add an explicit per-turn mode gate, document accepted prefixed cues, and resolve the output-rule conflicts. Update task continuity and the discussion record.

## 7. Current State

The causes of the workflow ambiguity are identified. No repository changes for this task have been committed yet.

## 8. Remaining Work

- Revise `skills/conversation-mode/SKILL.md`.
- Update the task board and checkpoint the repository documentation-audit task.
- Record the complete answer in `workspace/discussion.md`.
- Fetch all changed paths from branch `gpt` and verify the exact content.

## 9. Next Actions

1. Revise the Conversation Mode skill with the explicit per-turn gate and consistent output rules.
2. Update task metadata and the task board.
3. Add the answer and verification report to the top of `workspace/discussion.md`.
4. Fetch all changed paths and confirm the committed result.

## 10. References

- `skills/conversation-mode/SKILL.md`
- `skills/SESSION_START.md`
- `skills/the-worker/SKILL.md`
- `skills/INITIALIZATION_POLICY.md`
- `workspace/discussion.md`
- Related task: `workspace/tasks/20261120-123000-repository-documentation-audit.md`

## 11. Verification

- **Check:** Compare mode-selection, persistence, transition, and output requirements.
- **Method:** Read the authoritative files from branch `gpt` and perform read-back after each commit.
- **Result:** The conflicting requirements and missing response gate are identified.
- **Limitations:** Repository instructions cannot guarantee model execution. The change makes the required behavior explicit and testable but cannot prove future compliance in every response.

## 12. Handoff Instructions

Continue on branch `gpt`. Keep Condensed Mode active. Do not inspect anything under `archive/`. Do not read or write `workspace/discussion.md` through The Worker. Conversation Mode owns that file. Do not run lint or CI locally, dispatch workflows, or wait for CI. Fetch and verify every changed path before reporting completion.
