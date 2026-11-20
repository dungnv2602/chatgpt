# Task: Add a Condensed Mode discussion register

## Metadata

- **ID:** 20261120-120302
- **Created:** 2026-11-20 12:03 UTC
- **Updated:** 2026-11-20 12:03 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** None
- **Archived:** No

## 1. Original Request

"We need discussion.md inside workspace, to prevent me from starting a new chat quickly repeatedly. In conversation mode - default, this file is not used. In conversation mode - condensed, this file is use to document your reply, and my prompt on here. So I would expect on here will have my prompts mostly, while yours is minimized. This is handy for long discussion that we haven't finalized as my approval. When you got my approval, after documentation needed, then you clear that file. Doing it make sure discussion.md is only for open conversation that haven't finalized.

Expand on this and suggest your workspace adjustments."

## 2. Subsequent Instructions

- 2026-11-20 12:03 UTC — User: "The discussion should be easy for me to read, so lastest chat is at the top."
- 2026-11-20 12:03 UTC — User: "Approve all."

## 3. Objective

Create a temporary, prompt-focused register for unresolved discussions. Use it only in Condensed Mode. Preserve user prompts verbatim, minimize assistant notes, place the newest discussion and message first, and clear resolved entries only after required documentation is complete and verified.

## 4. Requirements

- Create and retain `workspace/discussion.md` as a predictable path.
- Keep a short placeholder when no discussions remain.
- Default Mode must not read, consult, create, or update the discussion register.
- Condensed Mode must read the register once when starting work in each conversation.
- Record relevant user prompts verbatim and in reverse chronological order.
- Put the newest discussion at the top of the file and the newest message at the top of its discussion.
- Keep assistant notes short and limited to findings, proposals, decisions, rejected options, and outstanding questions.
- Do not turn the file into a full conversation transcript or a task index.
- Keep distinct discussions separate.
- Track open, awaiting-approval, and approved-but-undocumented states.
- On approval, transfer the original prompts and relevant clarifications into task records or permanent project documents.
- Create or update the task board when the approved outcome requires a task.
- Verify required documentation before removing a resolved discussion.
- Remove only the resolved entry. Preserve all other open discussions.
- Record important rejection or withdrawal decisions in permanent records when needed, then clear the resolved entry.
- Keep an entry when documentation or verification remains incomplete.
- Do not create a separate discussion archive.
- Do not record credentials, access tokens, hidden reasoning, or unrelated sensitive information.
- Update workspace navigation, Conversation Mode, and Worker boundaries to define ownership.
- Work only on branch `gpt`.

## 5. Decisions

- User approved the complete proposed design.
- The newest discussion and newest message must appear at the top.
- Conversation Mode owns `workspace/discussion.md`.
- The Worker must not read or write the discussion register directly.
- Default Mode does not use the register.
- Condensed Mode uses the register for open discussions.
- Resolved entries are removed only after required documentation is complete and verified.
- Keep the file present with a `No open discussions` placeholder when empty.
- Git history retains prior committed versions. Do not create a separate discussion archive.

## 6. Progress Log

### 2026-11-20 12:03 UTC

- **Action:** Inspected workspace navigation, task rules, Conversation Mode, Session Archiving, and Worker instructions.
- **Result:** The workspace had no discussion register. Conversation Mode did not define temporary discussion recovery. The Worker explicitly prohibited conversation transcripts and preserved approved prompts in task records.
- **References:** `workspace/README.md`, `workspace/task_board.md`, `workspace/TASK_TEMPLATE.md`, `skills/conversation-mode/SKILL.md`, `skills/the-worker/SKILL.md`, `skills/session-archiving/SKILL.md`.
- **Next:** Add the register and define mode ownership and resolution behavior.

### 2026-11-20 12:03 UTC

- **Action:** Read the skill-authoring rules and repository writing policy. Confirmed that `workspace/discussion.md` does not exist.
- **Result:** The approved changes can remain within `workspace/` and `skills/`. No foundational initialization changes are required.
- **References:** `skills/agent-skill-authoring/SKILL.md`, `skills/asd-ste100/SKILL.md`, `skills/asd-ste100/references/repository-writing-policy.md`.
- **Next:** Implement the approved design in one commit and verify every changed path.

## 7. Current State

The design is approved. The repository changes are not yet committed.

## 8. Remaining Work

- Create `workspace/discussion.md`.
- Update `workspace/README.md`.
- Update `skills/conversation-mode/SKILL.md`.
- Update `skills/the-worker/SKILL.md`.
- Update the task board and current-execution metadata.
- Read back every changed path.
- Run the repository technical-documentation linter on changed documentation.

## 9. Next Actions

1. Create the approved files and updates on branch `gpt`.
2. Read back all changed paths and verify their content.
3. Run the applicable documentation linter.
4. Update this task record with the commit and verification results.

## 10. References

- `workspace/discussion.md`
- `workspace/README.md`
- `workspace/task_board.md`
- `skills/conversation-mode/SKILL.md`
- `skills/the-worker/SKILL.md`
- `skills/agent-skill-authoring/SKILL.md`
- `skills/asd-ste100/SKILL.md`
- `skills/asd-ste100/references/repository-writing-policy.md`

## 11. Verification

- **Check:** Existing workspace and mode instructions.
- **Method:** Retrieved and read the exact files from branch `gpt`.
- **Result:** Completed.
- **Limitations:** The proposed changes have not yet been committed or validated.

## 12. Handoff Instructions

The user approved the full design, including newest-first ordering. Implement only the listed workspace and skill changes on branch `gpt`. Do not modify `main` or unrelated paths.
