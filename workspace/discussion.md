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


## Condensed Mode compliance

**Status:** Active

### 2026-11-20 — User

> We're in condensed mode, why you text here?

**Assistant correction:** The previous reply violated Condensed Mode. Do not place explanations, acknowledgements, status updates, or answers in chat. Put required communication in this file and provide only its direct GitHub link. In chat, the only permitted links are the active task link and this discussion-file link.

**CI preflight:** Checked before handling this message. Current branch head `b1ba32ac693949bcd70829faf19c2c586c045a95` has a successful changed-document run. The latest full-document run also succeeded on its triggering commit `a259f689d470299bac74d08e62f4b60965aaf1da`. No pending runs were reported for the current head.


## No open discussions
