---
name: github-actions
description: Design, maintain, optimize, and secure GitHub Actions workflows. Use when work changes CI workflows, triggers, path filters, concurrency, incremental checks, caching, runners, permissions, artifacts, or deployment automation.
metadata:
  project-role: foundational
  format: agentskills
---

# GitHub Actions

## 1. Purpose and authority

Use this skill for GitHub Actions workflow design and maintenance. It governs workflow-specific decisions. The Conversation Mode skill governs general repository execution.

1. Follow the user's current instructions and the repository's approved workspace boundary.
2. Use `dungnv2602/chatgpt`, branch `gpt`, as the source of truth.
3. Follow the repository's approved project boundaries. Do not change `main` unless the user authorizes it.
4. Inspect the target workflows and the scripts/configuration they use before editing.
5. Do not treat historical notes, examples, or old cost figures as current GitHub policy.

## 2. Scheduled archive cleanup

The scheduled archive-retention workflow is owned by GitHub Actions.

- Run the schedule from the repository default branch because GitHub scheduled events only run there.
- Check out `gpt`, which is the working/source branch.
- Delete the complete contents of `archive/tasks/` as one batch only after the 14-day interval has elapsed. Do not calculate per-record expiry.
- Preserve `.gitkeep` and the task-board historical entries.
- After cleanup, atomically fast-forward `main` to the resulting `gpt` commit. Never force-push or create an independent cleanup commit on `main`.
- Check that `main` is an ancestor of `gpt` before pushing. If the branches diverge, fail safely without updating either ref.
- Keep the cleanup implementation reusable through `workflow_call` and operator-accessible through `workflow_dispatch`. A forced manual run must be an explicit input.
- GitHub cron has no exact every-14-days syntax. Use a weekly schedule plus a committed UTC last-cleanup marker to enforce a minimum 14-day interval.

## 3. Mandatory CI preflight and repair

Run one bounded CI snapshot before handling every new user prompt. This rule applies to all request types and conversation modes.

1. Inspect the newest available run for each applicable workflow on branch `gpt`. Also inspect the current branch head's combined status and check runs.
2. For each workflow, act only on its newest run. A completed success clears that workflow. A completed failure requires investigation and repair.
3. Treat an older failure as superseded when a newer run for the same workflow succeeds.
4. Treat queued, in-progress, cancelled, skipped, or absent runs as pending or unavailable. They do not block the user's request. Never wait, poll, dispatch, or rerun to obtain a result.
5. When a newest completed run fails, inspect its jobs, failed steps, and logs. Fix the cause on `gpt` before handling the user's request. Do not weaken tests, path coverage, or baselines.
6. After you push a repair, continue with the user's request. GitHub Actions owns validation. Review the result during the next mandatory preflight.
7. Never run the STE linter, CI workflows, or CI test suites locally. Do not manually dispatch or rerun workflows unless the user explicitly asks.
8. If GitHub Actions cannot be accessed, make one bounded access attempt. Record the status as unverified in `workspace/discussion.md` in Condensed Mode. Do not claim that CI passed. Continue with the user's request. Do not let unavailable CI access deadlock the conversation.

After loading skills for `start session`, `start a drawing session`, or `Be the novelist`, run the same one-time snapshot. Repair any visible newest completed failure before project work. Do not wait for pending or unavailable results. If a repair starts new CI runs, continue initialization without waiting for them.

## 4. Inspect and preserve validation scope

Before changing a workflow, identify its events, branch/path filters, jobs, dependencies, permissions, concurrency, runner, timeout, cache, artifact behavior, and scripts. Identify which checks cover which files.

- Do not optimize by removing a required test or weakening its validation scope.
- Preserve required push, pull-request, release, and schedule events.
- Include workflow files, scripts, configuration, lockfiles, and source data that affect the result in the appropriate path filters.
- Keep full audits and incremental checks separate when they have different validation scopes.
- Avoid duplicate runs caused by overlapping triggers.

## 5. Design precise triggers

Use branch and path filters to avoid work that cannot check the changed files.

- When both branch and path filters exist, both conditions must match.
- GitHub evaluates path patterns in order. A later positive pattern can include a path that an earlier pattern excluded. A later negative pattern can exclude a path that an earlier pattern included.
- When using negative patterns inside `paths`, include at least one positive pattern.
- Do not use both `paths` and `paths-ignore` for the same event.
- Check branch-protection requirements before adding workflow-level filters. A skipped workflow can leave a required check pending. Use job-level conditions or a stable required check when every pull request needs a result.

## 6. Control concurrency and superseded runs

Use a concurrency group that isolates a workflow and its branch or pull request:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

- Use `cancel-in-progress: true` for replaceable validation runs when a newer commit makes an older run obsolete.
- Do not use one static group for unrelated workflows or branches.
- Do not cancel an active deployment unless cancellation is safe for that deployment.
- Keep deployment concurrency separate from ordinary validation concurrency.

### Reject stale pushes before checkout

For expensive push validation, a short preflight job can reject a superseded run before the validation job checks out the repository.

- Run the guard before checkout, dependency setup, or repository scripts.
- Query the newest run for the same workflow, branch, and event. Compare its run ID with `github.run_id`.
- If a newer run exists, cancel the current run through the Actions API. The validation job must depend on the guard output and must not start for a superseded run.
- Grant `actions: write` only to the guard job when it must cancel its own run. Grant only the read permissions needed for its queries. Commit comparison requires `contents: read`.
- Keep the guard short and give it a small timeout.
- If the API cannot identify the newest run, emit a warning and continue validation. Never skip validation because the guard could not decide.
- Retain `cancel-in-progress: true` as the primary race protection. A new push can arrive after the guard passes. Concurrency cancellation handles that race.

A separate guard job costs an additional runner allocation. Use it when avoiding checkout and setup on superseded runs justifies that cost. Do not add one to trivial workflows.

## 7. Preserve incremental-check correctness

For push-based incremental checks, compare against the latest successful run of the same workflow and branch, not merely the previous push event.

1. Query completed runs for the same workflow and branch.
2. Select the latest successful run and read its exact `head_sha`.
3. Use the GitHub compare API before checkout to check that the baseline is an ancestor of the current commit. Accept `ahead` or `identical`. Treat missing, failed, or divergent comparisons as an invalid baseline.
4. Check every relevant file changed since that baseline.
5. Run a full audit when the baseline is missing or invalid.

Do not rely only on `github.event.before`: a cancelled run may contain commits omitted from the next push's event diff.

Prefer `fetch-depth: 1`. After checkout, fetch only the successful baseline commit with `git fetch --no-tags --depth=1 origin "$BASE_SHA"`. If that fetch fails, run a full audit rather than omitting changes. Use full history only when the workflow's Git operations genuinely require it. Do not use `git merge-base` as an ancestry test in a shallow checkout.

Do not treat failed, cancelled, queued, or in-progress runs as successful baselines. For pull-request checks, compare the pull-request head with the appropriate base commit. Do not reuse a push baseline without a clear reason.

## 8. Cache dependencies only when useful

- Cache dependencies that are expensive to download or install and can be safely reused.
- Build keys from the operating system, runtime, package manager, and dependency lockfiles.
- Use restore prefixes only when older cache contents remain compatible.
- Prefer supported cache options in official setup actions when they meet the requirement.
- Do not cache standard-library-only jobs, secrets, credentials, or sensitive build outputs.
- Do not add caching when restore/save overhead exceeds the work avoided.
- Prevent untrusted jobs from writing cache content later consumed by privileged workflows.

## 9. Choose runners and timeouts

- Select the least costly supported runner that meets operating-system, architecture, toolchain, and security requirements.
- Do not use Linux when the job requires Windows or macOS behavior.
- Pin a runner image when reproducibility requires a specific environment.
- Set `timeout-minutes` for every job and a step timeout when an individual command can hang.
- Use self-hosted runners only when their isolation and maintenance model are suitable.

Do not repeat historical runner prices, billing multipliers, minute-rounding rules, or quotas as current facts without checking current official GitHub billing documentation.

## 10. Minimize artifact storage

- Upload only outputs that later jobs or users need.
- Exclude temporary and reproducible files when they are not required.
- Compress large outputs when compression reduces transfer or storage cost.
- Set `retention-days` to the shortest period that still meets the workflow's operational needs.
- Download only artifacts required by a later job.
- Do not add artifact settings to workflows that do not upload artifacts.

Logs and workflow artifacts can have different storage rules. Check current GitHub documentation before stating limits or defaults.

## 11. Apply least privilege and protect inputs

Set permissions explicitly at workflow or job level. Grant each job only what it needs.

- Use `contents: read` for checkout-only jobs.
- Grant `actions: write` only to jobs that must cancel or change workflow runs.
- Use `permissions: {}` when a job does not need a GitHub token.
- Grant write permissions at job level when only one job needs them.
- Prefer short-lived credentials and OpenID Connect when supported by the deployment provider.
- Do not expose secrets to untrusted pull-request code.
- Do not use `pull_request_target` to execute untrusted pull-request code with elevated permissions.
- Pass event values to scripts through environment variables. Quote and check them.
- Do not interpolate untrusted event data directly into shell commands.
- Follow repository policy for action pinning and check an action's owner/source before adopting a version.
- Isolate self-hosted runners that execute untrusted code.

## 12. Keep workflow structure maintainable

- Use separate workflows when triggers, permissions, validation scopes, or operational lifecycles differ.
- Use a reusable workflow when multiple workflows genuinely share a maintained job sequence. Do not abstract a single small job without a clear reuse case.
- Keep permissions, concurrency, runner choice, and timeouts close to the job that uses them.
- Explain non-obvious conditions that protect coverage or safety.
- Do not duplicate checks without a distinct purpose.
- Do not delete a full audit merely because an incremental check is faster.
- Batch related workflow, script, and documentation edits into one coherent commit to avoid intermediate pushes and duplicate CI runs.

## 13. Decision checklist

Use these questions when implementing an optimization:

1. Does the trigger match only relevant events, branches, and paths without bypassing required checks?
2. Can concurrency safely cancel obsolete validation without interrupting important deployments?
3. Is any preflight job worth its additional runner allocation?
4. Does the incremental baseline include every commit since the last successful validation?
5. Does a missing or unreachable baseline cause a full audit?
6. Is dependency caching useful and safe for this job?
7. Are runner, timeout, artifact retention, and permissions appropriate to the actual workload?
8. Can repeated logic be shared without creating needless abstraction?
9. Are changes grouped into one coherent push?
10. Does the assistant leave workflow execution to GitHub Actions, avoid local CI execution, and avoid waiting or polling for results?

## 14. Repository execution discipline

This section consolidates the former repository CI preflight and execution-efficiency rules from Conversation Mode. This skill is the sole authority for CI and GitHub Actions behavior.

### Before editing

1. Inspect the branch head and the exact files, scripts, and configuration relevant to the request.
2. Identify the required change set. Do not expand the task into unrelated cleanup.
3. Reuse verified reads and tool results. Do not repeat searches or status checks without new evidence.
4. Batch related edits into one coherent commit. Avoid intermediate commits that create duplicate push-triggered runs.
5. Review the complete changed sections. Preserve facts, conditions, exceptions, numbers, scope, and modality.

### CI gate

Follow Section 3 before every user prompt and after cue-triggered skill loading. Do not defer this gate until the user asks. Do not wait for or poll in-progress runs. Repair applicable completed failures. Never run the STE linter or CI workflows locally.

### After editing

1. Read back each changed path after the commit when repository access supports it.
2. Check the commit result and report its exact SHA.
3. State which read-back checks you performed. Do not run CI locally or wait for GitHub Actions results.
4. Separate verified changes, unresolved blockers, and work that requires user authorization.
5. Report the result once. Do not claim verification that did not occur.

### Efficiency constraints

- Do not make speculative edits.
- Do not create one-line commits when related changes can be grouped.
- Do not repeat wording reviews without a defined rule or finding.
- Do not reduce necessary file verification to save time. Reduce redundant operations instead.

## 15. Official references

- [Workflow syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)
- [Workflow concurrency](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs)
- [Dependency caching](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows)
- [Workflow artifacts](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts)
- [Secure use reference](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)
