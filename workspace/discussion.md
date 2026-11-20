# Open Discussions

> This file contains unresolved discussions and the latest completed-work report.
>
> Conversation Mode owns this file. Default Mode must not read or write it.
>
> When no discussions remain, keep the `No open discussions` placeholder.

## Latest Work Report

**Updated:** 2026-11-20

**Outcome:** Updated Condensed Mode communication rules. Chat replies now contain only the active task link or the discussion file link. All other user-facing communication must be written in this file.

**Task:** User-directed workflow update. No separate task record was created.

**Changed paths:**
- [Conversation Mode skill](../skills/conversation-mode/SKILL.md)
- [Discussion report](discussion.md)

**Commits:**
- [Conversation Mode workflow update](https://github.com/dungnv2602/chatgpt/commit/858035a7c2985486daa41cbe1550410fa063a4b6)

**Verification:** Fetched the updated skill and confirmed the two-link-only rule, the discussion-file communication rule, and the existing approval behavior. Fetched this report after commit and checked its contents.

**Blocker / Next:** Continue the active repository documentation audit.

## CI preflight before every prompt

**Status:** Approved — documentation pending

### 2026-11-20 13:30 UTC — User

> ---
> Do not inspect CI results unless you explicitly ask. When you ask, inspect failures and fix them.
> ---
>
> Wrong. You must check and fix CI before taking my prompt, ve whatever it is. You always check CI and fix first. You also must check and fix CI after loading skills by following my cue.
>
> ---
>
> Update your workflow accordingly.

**Assistant note:** The user replaced the previous deferred-inspection policy. The approved change requires a CI preflight before every prompt and another preflight after cue-triggered skill loading. The initial CI failures were repaired before this task began. Both applicable workflows passed on commit `a5ce29072ba5a983c1c769e744dd86962d4a5c41`.

**Outstanding:** Update the authoritative GitHub Actions policy and all related skill-loading and task-execution instructions. Verify the changes and their CI runs.

## No open discussions
