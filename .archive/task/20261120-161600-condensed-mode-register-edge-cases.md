# Task: Expand Condensed Mode register rules and edge-case handling

## Metadata

- **ID:** 20261120-161600
- **Created:** 2026-11-20 16:16 UTC
- **Updated:** 2026-11-20 16:16 UTC
- **Priority:** P1
- **Status:** Done
- **Origin:** User
- **Approval:** Approved
- **Current execution:** No
- **Dependencies:** None
- **Related tasks:** 20261120-160152
- **Archived:** Yes
- **Archived:** 2026-11-20 16:16 UTC

## 1. Original Request

> Add one more thing: in condensed mode, besides open discussions as mentioned before, discussion.md only retain the last 3 most recent reports, be it successful or not.

> The order is open discussions first, then reports. They are devided by headings 2.

> Inside each section, newest ones come first. Treat a report of failure as open discussion, clarifications on my prompt is open discussion, basically anything that need my call is open discussion. That means, the reports section pnly contains successful reports. Expand on this to cover edge cases.

## 2. Subsequent Instructions

- The user switched to Default Mode before this refinement.
- Preserve the two-section order: Open Discussions first, Reports second.
- Sort entries newest first within each section.
- Classify failures, prompt clarifications, and anything requiring the user's call as Open Discussions.
- Reports contains successful reports only.

## 3. Objective

Define an unambiguous Condensed Mode register lifecycle, including classification, ordering, retention, closure, failure handling, empty states, and link selection.

## 4. Requirements

- Use exactly two H2 sections in this order: `## Open Discussions`, then `## Reports`.
- Sort both sections newest first.
- Open Discussions includes any unresolved matter requiring user input, judgment, approval, clarification, or a choice.
- Prompt clarifications remain open until answered or withdrawn.
- Failed operations and unsuccessful final outcomes never appear in Reports. Keep unresolved failures in Open Discussions.
- A transient failure repaired autonomously before the final outcome may be described as part of a successful report, provided the final result is verified.
- Reports contains only completed, supportable, verified successes.
- Retain at most the three newest success reports. This limit does not apply to Open Discussions.
- Keep each section heading and its own empty-state placeholder even when empty.
- Close discussions only when resolved, superseded, withdrawn, or no longer requiring user input. Do not close them due to age or inactivity alone.
- A successful milestone may be reported while a larger task continues. Record any separate user decision in Open Discussions.
- Use UTC timestamps. Keep detailed progress and verification in task records.
- In Condensed Mode, link to discussion.md when it contains any open discussion or retained report; otherwise link to the active task record.
- Default Mode must not read or write discussion.md.

## 5. Decisions

- Classification is based on the current state and need for user input, not on the origin of the item.
- A failed final outcome is always an Open Discussion until resolved; Reports is success-only.
- Reports are retained by verified completion time, newest first, with a strict maximum of three.
- Meaningful updates to an open thread move it to the top; cosmetic edits do not.
- Partial answers leave only the unanswered portion open.
- A successful outcome and a distinct unresolved follow-up may appear separately in the two sections without duplicating the same information.

## 6. Progress Log

### 2026-11-20 16:16 UTC

- **Action:** Expanded the Condensed Mode register lifecycle and edge-case rules.
- **Result:** Updated Conversation Mode, The Worker, and workspace navigation guidance. The rules now define open-discussion classification, success-only reporting, failure and clarification handling, ordering, timestamps, three-report retention, closure conditions, empty states, partial answers, supersession, mixed success/open follow-ups, verification standards, and Condensed Mode link selection.
- **References:** `skills/conversation-mode/SKILL.md`; `skills/the-worker/SKILL.md`; `workspace/README.md`.
- **Commits:** Conversation Mode `5e4978ea0d109ec593d4d7065d8ad1b19564b566`; The Worker `40760367245c2cd13f19e01d7275243e2d5d9ef7` and `9bac7ad52eda6621684ff6fb16b7fd1e364525f5`; workspace README `ee68edbad99f2389ee43d6838f1daaeb548b7278`.
- **Read-back:** Fetched all three committed files from branch `gpt`. Confirmed the required section order, failure/clarification classification, success-only reports, three-report cap, empty-state placeholders, and link-selection rule.
- **Next:** None. Implementation and read-back are complete.

## 7. Current State

The Condensed Mode register policy is updated and verified on branch `gpt`. No change was made to `workspace/discussion.md`, because the active mode is Default Mode and that mode must not access the register.

## 8. Remaining Work

None.

## 9. Next Actions

None.

## 10. References

- `skills/conversation-mode/SKILL.md`
- `skills/the-worker/SKILL.md`
- `workspace/README.md`
- Related workflow correction task: `20261120-160152`

## 11. Verification

- **Check:** Read back the three changed files from branch `gpt`.
- **Method:** Fetch each committed path and inspect required rule markers.
- **Result:** Passed. All required policy markers were present.
- **Limitations:** CI was not run or awaited. The discussion register was not read or changed in Default Mode.

## 12. Handoff Instructions

No further work is required for this task. Future Condensed Mode turns must apply the updated policy. Conversation Mode alone owns `workspace/discussion.md`; The Worker must not read or write it directly.
