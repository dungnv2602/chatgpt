# Open Discussions

### 2026-11-20 13:55 UTC

**User**

> Check if there's rule to prevent you from running lint locally, and are you respecting it?
>
> Check if there's rule to prevent you from running CI manually locally or waiting for CI results, whatever the case, and are you respecting it?

**Assistant**

The repository already had an explicit rule against running the STE linter locally. It appeared in the ASD-STE100 skill and the repository writing policy. I did not run the linter locally during this session or the preceding documentation audit.

Before this update, the GitHub Actions skill did not explicitly prohibit running every kind of CI workflow locally. It did prohibit manual dispatch, reruns, and polling unless the user requested a CI investigation. However, its mandatory preflight also told me to wait for in-progress runs and wait for repair runs to pass. Those instructions conflicted with the user's requirement to delegate CI execution to GitHub Actions without waiting.

I have corrected the policy:
- Do not run the STE linter locally.
- Do not run CI workflows or CI test suites locally.
- Do not manually dispatch or rerun workflows unless the user explicitly asks.
- Inspect the latest available workflow results and current branch checks at each mandatory preflight.
- Do not wait for or poll in-progress runs.
- Repair applicable completed failures before handling the prompt.
- After pushing a change, leave its CI execution to GitHub Actions. Review its result at a later mandatory preflight.

**Current-session verification**

- Session initialization loaded the six required foundational skills.
- The post-load CI preflight found no check runs or status entries on branch head `11856d3ff017c4c8182b1e2dbe78fada6b4855f0`.
- The latest available changed-document run succeeded on `b1ba32ac693949bcd70829faf19c2c586c045a95`.
- The latest available full-document run succeeded on `a259f689d470299bac74d08e62f4b60965aaf1da`.
- No CI result was awaited or polled after the documentation updates.

**Updated files**

- [Conversation Mode](../skills/conversation-mode/SKILL.md)
- [GitHub Actions](../skills/github-actions/SKILL.md)
- [Session Archiving](../skills/session-archiving/SKILL.md)
- [ASD-STE100](../skills/asd-ste100/SKILL.md)
- [Repository writing policy](../skills/asd-ste100/references/repository-writing-policy.md)

**Commits**

- [Conversation Mode](https://github.com/dungnv2602/chatgpt/commit/b4b92c6587dfdaf07af7f734ffa03966f072daed)
- [GitHub Actions](https://github.com/dungnv2602/chatgpt/commit/8d81fc542536c0d7e61471aa0d8e8c248bfdd21c)
- [Session Archiving](https://github.com/dungnv2602/chatgpt/commit/ec68a20d4c5af1191148f6869ffe2012ee37dc28)
- [ASD-STE100](https://github.com/dungnv2602/chatgpt/commit/4d9311e0a707df834a7b9e8b6e5c17f529c0fde5)
- [Repository writing policy](https://github.com/dungnv2602/chatgpt/commit/abf9df018af1e19c6bd654c524abb8c95b13ac3f)
- [Cleared communication register after approval](https://github.com/dungnv2602/chatgpt/commit/b1723784b408b55c936b65dea7fcf3d32d57ce62)

**Verification:** Fetched all five updated skills/policy files and checked the new wording. Cleared `workspace/discussion.md` after the approved changes, then added this reply as the newest conversation entry. GitHub Actions will run and report the new commits independently.
