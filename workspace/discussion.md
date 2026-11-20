
# Open Discussions

### 2026-11-20 14:02 UTC

**User**

> https://github.com/dungnv2602/chatgpt/blob/gpt/workspace/tasks/20261120-133053-ci-preflight-before-every-prompt.md
>
> Delete this, no longer needed
>
> Double check to tighten the workflow, to prevent you from deadlock
>
> Check if there's rule to prevent you from running lint locally, and are you respecting it?
>
> Check if there's rule to prevent you from running CI manually locally or waiting for CI results, whatever the case, and are you respecting it?
>
> Fix accordingly if any.

**Assistant**

Deleted the obsolete CI-preflight task and removed its Current Execution row from the task board.

The policy already prohibited local STE linting. It did not prohibit every local CI workflow or test-suite run in one explicit rule. The previous update also left blocking language in The Worker and Session Archiving. Those rules required waiting for CI or stopping when GitHub Actions was unavailable. The session-start text also treated incomplete CI results as a possible initialization block.

The workflow is now non-blocking:

- Take one bounded CI snapshot before each prompt and after cue-triggered skill loading.
- Repair a failure only when the newest run for an applicable workflow is completed with a failure conclusion.
- Treat pending, in-progress, cancelled, skipped, absent, and inaccessible results as non-blocking.
- Never wait for or poll CI results.
- After pushing a repair, continue with the user's request. Review the result at the next preflight.
- Never run the STE linter, CI workflows, or CI test suites locally.
- Do not manually dispatch or rerun workflows unless the user explicitly asks.

The latest available full-document run succeeded on commit `abf9df018af1e19c6bd654c524abb8c95b13ac3f`. The latest available changed-document run succeeded on commit `ec68a20d4c5af1191148f6869ffe2012ee37dc28`. The current branch head before these edits had no status entries or check runs. Its combined status was `pending` with zero reported checks. This is not evidence that the current head passed CI. Older failures were superseded by newer successful runs.

I did not run the linter locally. I did not run CI locally, manually dispatch a workflow, rerun a workflow, wait for a result, or poll for completion.

**Updated paths**

- `skills/github-actions/SKILL.md`
- `skills/the-worker/SKILL.md`
- `skills/session-archiving/SKILL.md`
- `skills/SESSION_START.md`
- `skills/agent-skill-authoring/SKILL.md`
- `skills/INITIALIZATION_POLICY.md`
- `workspace/task_board.md`
- `workspace/discussion.md`

**Additional check:** The ASD-STE100 skill and repository writing policy already prohibit local linter and CI execution. Their existing rules were retained.

**Verification:** The updated files will be read back from branch `gpt`. The task deletion will be checked through the resulting repository tree. GitHub Actions will execute any triggered checks independently. No result will be awaited.
