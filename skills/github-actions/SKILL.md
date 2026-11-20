---
name: github-actions
description: Design, maintain, optimize, secure, and check GitHub Actions workflows. Use when work changes CI workflows, triggers, path filters, concurrency, incremental checks, caching, runners, permissions, artifacts, or deployment automation.
metadata:
  project-role: foundational
  format: agentskills
---

# GitHub Actions

## 1. Purpose and activation

Use this skill for GitHub Actions workflow design and maintenance.

Activate it when a task creates, revises, optimizes, debugs, secures, or validates workflow files. Use it for triggers, path filters, concurrency, caching, runners, permissions, artifacts, incremental checks, and deployment workflows.

This skill governs workflow-specific decisions. The Conversation Mode skill governs general repository execution and CI checkpoint policy.

## 2. Authority and boundaries

1. Follow the user's current instructions and the repository's approved workspace boundary.
2. Use repository `dungnv2602/chatgpt`, branch `gpt`, as the source of truth.
3. Follow Sections 7 and 8 of `skills/conversation-mode/SKILL.md` for pending CI runs, batching, read-back, and commit verification.
4. Do not infer permission to change files outside the approved project directories.
5. Request the required authorization before you access or change workflow paths outside those directories.
6. Do not change `main` unless the user authorizes that change.

The imported optimization note is supporting source material. It is not an authority for current GitHub limits, prices, or default settings. See [the user-supplied optimization notes](references/user-supplied-optimization-notes.md).

## 3. Inspect before editing

1. check the current branch head.
2. Check known pending CI run IDs from the previous task.
3. Inspect each target workflow and every script or configuration file that it uses.
4. Record its events, branch filters, path filters, jobs, dependencies, permissions, concurrency, runner, timeout, cache, and artifact settings.
5. Identify required checks and their branch-protection role.
6. Define the validation scope before you change the workflow.

Do not optimize a workflow by removing a required test or weakening its validation scope.

## 4. Design precise triggers

Use event filters to avoid runs that cannot check the changed files.

- Use branch filters when a workflow only applies to selected branches.
- Use `paths` when a workflow applies to a defined file set.
- Include the workflow files, scripts, configuration, lockfiles, and source data that affect its result.
- Keep full audits and incremental checks separate when they have different validation scopes.
- Avoid overlapping event and path filters that start duplicate jobs.
- Preserve required push, pull-request, release, and schedule events.

When both branch and path filters exist, both conditions must match. Check their combined effect.

GitHub evaluates path patterns in order. A later positive pattern can include a path that an earlier negative pattern excluded. A later negative pattern can exclude a previously included path. Use at least one positive pattern when you use negative patterns. Do not reorder patterns without checking their effect.

Do not use both `paths` and `paths-ignore` for the same event. Use negative patterns inside `paths` when one event needs both inclusion and exclusion rules.

A workflow skipped by branch or path filters can leave a required check pending. Check branch-protection requirements before you add a workflow-level filter. Use job-level conditions or a stable required check when the repository needs a check on every pull request.

## 5. Control concurrency safely

Use a concurrency group that isolates the workflow and its branch or pull request.

For replaceable push-based validation, a common pattern is:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

Use `cancel-in-progress: true` when a newer run makes an older validation run obsolete.

Do not use one static concurrency group for unrelated workflows or branches. Do not cancel an active deployment unless the deployment design makes cancellation safe. Use environment protection or a deployment-specific concurrency policy when required.

Check whether push and pull-request events share a concurrency group. check that the group does not cancel a run that the user still needs.

### Reject superseded runs before checkout

Concurrency cancellation remains the primary control for replaceable push validation. Add a lightweight preflight job when a run can spend meaningful time or bandwidth on checkout before it reaches its first useful check.

- Run the preflight before any checkout, dependency setup, or repository script.
- Query the newest run for the same workflow, branch, and event. Compare its run ID with `github.run_id`.
- If a newer run exists, cancel the current run through the Actions API. Do not let a superseded run report a successful validation result.
- Give the preflight job `actions: write` only when it must cancel its own run. Add read permissions only for its API queries; for example, the compare-commits endpoint needs `contents: read`. Keep the validation job on the permissions it needs, usually `contents: read`.
- Make the validation job depend on the preflight output. If the preflight cancels the run, the validation job must not start.
- If the API cannot identify the newest run, continue with validation and emit a warning. Do not skip validation because the guard could not decide.
- Keep the preflight short and set a small job timeout.

A narrow race remains: a newer push can arrive after the guard passes and before checkout finishes. Keep `cancel-in-progress: true` so GitHub cancels the older run when the new run starts. The guard prevents checkout when a newer run already exists; it cannot prevent every race after the check.

## 6. Preserve incremental-check correctness

For push-based incremental checks, use the latest successful run of the same workflow and branch as the comparison baseline.

Do not rely only on `github.event.before`. A cancelled run can contain commits that the next push does not include in its event diff. A later incremental run can then omit those commits.

Use this procedure:

1. Query completed runs for the same workflow and branch.
2. Select the latest run with a successful conclusion.
3. Read its exact `head_sha`.
4. Use the GitHub compare API to check whether the baseline is an ancestor of the current commit before checkout. Accept `ahead` or `identical`; treat missing, failed, or divergent comparisons as an invalid baseline.
5. Check every relevant file changed since that baseline.
6. Run a full audit when the baseline is missing or invalid.

Prefer a shallow checkout with `fetch-depth: 1`. After checkout, fetch only the successful baseline commit with `git fetch --no-tags --depth=1 origin "$BASE_SHA"`. If that fetch fails, run a full audit instead of failing open or omitting changes. Use full checkout history only when the validation itself needs broader history. Do not use `git merge-base` as an ancestry test in a shallow checkout.

Do not silently treat a failed, cancelled, queued, or in-progress run as a successful baseline.

For pull-request checks, compare the pull-request head with the appropriate base commit. Use the event payload and Git history that match the pull-request validation design. Do not reuse a push baseline without a reason.

Test the full-audit fallback. It protects the workflow when the branch has no successful baseline or its history has changed.

## 7. Cache dependencies only

Add a cache when a job downloads or installs dependencies that later runs can reuse.

- Build cache keys from the operating system, runtime, package manager, and dependency lockfiles.
- Use restore prefixes only when the restored cache remains compatible.
- Prefer supported cache options in official setup actions when they meet the requirement.
- Do not cache standard-library-only jobs.
- Do not cache secrets, authentication tokens, private keys, or sensitive build outputs.
- Do not add a cache when the restore and save steps cost more than the work they avoid.

Review cache scope when pull requests can run untrusted code. Prevent untrusted jobs from writing cache content used by privileged workflows.

## 8. Select runners and set timeouts

Select a runner that meets the job's operating-system, architecture, toolchain, and security requirements.

- Prefer a lower-cost supported runner when it meets the job requirements.
- Do not select `ubuntu-latest` when the job requires Windows or macOS behavior.
- Pin a runner image when reproducibility requires a specific environment.
- Set `timeout-minutes` for every job.
- Set a step timeout when one command can hang independently.
- Use self-hosted runners only when their isolation and maintenance model are suitable.

Do not quote runner prices or multipliers without checking current GitHub billing documentation.

## 9. Minimize artifact storage

Upload only files that later jobs or users need.

- Exclude temporary and reproducible files when they are not required.
- Compress large outputs when compression reduces transfer or storage cost.
- Set `retention-days` to the shortest period that still supports the workflow.
- Download only the artifacts that a later job needs.
- Do not add artifact settings to workflows that do not upload artifacts.

Do not assume that logs and workflow artifacts share the same storage rules. Check current GitHub documentation before you report storage limits or retention defaults.

## 10. Apply least privilege and protect inputs

Set workflow permissions explicitly. Grant each job only the permissions that it needs.

- Use `contents: read` when a job only needs repository checkout.
- Add `actions: read` only when a job must query workflow runs or artifacts.
- Grant write permissions at job level when only one job needs them.
- Use short-lived credentials and OpenID Connect when the deployment provider supports it.
- Do not expose secrets to untrusted pull-request code.
- Do not use `pull_request_target` to execute untrusted pull-request code with elevated permissions.
- Pass event values to scripts through environment variables. Quote and check each value before use.
- Do not interpolate untrusted event data directly into shell commands.
- Follow repository policy for action pinning. check the action owner and source before you adopt an action version.
- Isolate self-hosted runners that execute untrusted code. Do not reuse a privileged persistent workspace across trust boundaries.

## 11. Keep workflow structure maintainable

Use separate workflows when they have different triggers, permissions, validation scopes, or operational lifecycles.

Use a reusable workflow when multiple workflows need the same maintained job sequence. Do not build an abstraction for a single small job without a clear reuse case.

Keep permissions, concurrency, runner choice, and timeouts close to the workflow or job that uses them. Add comments when a non-obvious condition protects coverage or safety.

Do not duplicate checks across workflows unless each check has a distinct purpose. Do not remove a full audit merely because an incremental check is faster.

Batch related workflow, script, and documentation edits into one coherent commit when the available write interface supports it. Avoid intermediate commits that trigger duplicate CI runs.

## 12. check and report

1. Parse every changed workflow as YAML.
2. Run `actionlint` when it is available.
3. Run the workflow's relevant scripts and tests when the execution environment supports them.
4. Review event filters, permission scope, concurrency groups, baseline selection, and fallback behavior.
5. Read back every changed path from branch `gpt`.
6. check the final branch head and associate each CI result with the exact commit SHA it checked.
7. Report run IDs and pending states. Follow the Conversation Mode CI checkpoint policy. Do not wait for or repeatedly poll an in-progress run.

Do not claim that a workflow passed because a commit has no status entries. Report unavailable checks as unverified.

## 13. Treat the imported note as historical input

The reference file preserves the user's original optimization note. Use it to identify potential improvements.

check mutable claims against current official GitHub documentation before you rely on them. This includes runner prices, billing multipliers, job-minute rounding, storage quotas, retention periods, and default settings.

Do not copy example action versions or runtime versions without checking whether they remain supported. Do not add caching or artifact retention when the workflow has no dependency or artifact requirement.

The note recommends dependency caching, safe concurrency cancellation, path filters, suitable runners, job timeouts, artifact compression, and shorter artifact retention. Evaluate each recommendation against the actual workflow. Do not apply it by default.

## 14. Official references

- [Workflow syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)
- [Workflow concurrency](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs)
- [Dependency caching](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows)
- [Workflow artifacts](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts)
- [Secure use reference](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)
