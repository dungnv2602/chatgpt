---
name: github-actions
description: Design, maintain, optimize, and secure GitHub Actions workflows. Use when work changes CI workflows, triggers, path filters, concurrency, incremental checks, caching, runners, permissions, artifacts, or deployment automation.
metadata:
  project-role: foundational
  format: agentskills
---

# GitHub Actions

## 1. Purpose and authority

Use this skill for GitHub Actions workflow design and maintenance. It governs workflow-specific decisions; the Conversation Mode skill governs general repository execution.

1. Follow the user's current instructions and the repository's approved workspace boundary.
2. Use `dungnv2602/chatgpt`, branch `gpt`, as the source of truth.
3. Follow the repository's approved project boundaries. Do not change `main` unless the user authorizes it.
4. Inspect the target workflows and the scripts/configuration they use before editing.
5. Do not treat historical notes, examples, or old cost figures as current GitHub policy.

## 2. Execution policy: implement, then let CI report

The default workflow for repository changes is implementation-first and event-driven:

1. Implement the requested workflow and documentation changes directly.
2. Commit related changes together so one coherent push produces the normal event-triggered CI run.
3. Do not manually invoke `workflow_dispatch`, `gh workflow run`, the Actions API dispatch endpoint, or any equivalent manual trigger.
4. Do not rerun, cancel, or otherwise stimulate CI manually.
5. Do not poll or inspect CI status as a routine post-edit step. Let the normal GitHub event trigger the configured workflows; failed CI is the feedback signal.
6. Do not add a workflow trigger solely to make a check run after an assistant edit.
7. If the user explicitly asks to investigate a CI failure, inspect the relevant run and fix the underlying cause. Otherwise, do not turn implementation work into a manual CI-verification exercise.

A workflow may retain a legitimate `workflow_dispatch` trigger for an operator's independent use. Its existence does not authorize the assistant to invoke it.

## 3. Inspect and preserve validation scope

Before changing a workflow, identify its events, branch/path filters, jobs, dependencies, permissions, concurrency, runner, timeout, cache, artifact behavior, and scripts. Identify which checks cover which files.

- Do not optimize by removing a required test or weakening its validation scope.
- Preserve required push, pull-request, release, and schedule events.
- Include workflow files, scripts, configuration, lockfiles, and source data that affect the result in the appropriate path filters.
- Keep full audits and incremental checks separate when they have different validation scopes.
- Avoid duplicate runs caused by overlapping triggers.

## 4. Design precise triggers

Use branch and path filters to avoid work that cannot validate the changed files.

- When both branch and path filters exist, both conditions must match.
- GitHub evaluates path patterns in order. A later positive pattern can include a path excluded earlier; a later negative pattern can exclude a path included earlier.
- When using negative patterns inside `paths`, include at least one positive pattern.
- Do not use both `paths` and `paths-ignore` for the same event.
- Check branch-protection requirements before adding workflow-level filters. A skipped workflow can leave a required check pending; use job-level conditions or a stable required check when every pull request needs a result.

## 5. Control concurrency and superseded runs

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
- Query the newest run for the same workflow, branch, and event; compare its run ID with `github.run_id`.
- If a newer run exists, cancel the current run through the Actions API. The validation job must depend on the guard output and must not start for a superseded run.
- Grant `actions: write` only to the guard job when it must cancel its own run. Grant only the read permissions needed for its queries; commit comparison requires `contents: read`.
- Keep the guard short and give it a small timeout.
- If the API cannot identify the newest run, emit a warning and continue validation. Never skip validation because the guard could not decide.
- Retain `cancel-in-progress: true` as the primary race protection. A new push can arrive after the guard passes; concurrency cancellation handles that race.

A separate guard job costs an additional runner allocation. Use it when avoiding checkout and setup on superseded runs justifies that cost. Do not add one to trivial workflows.

## 6. Preserve incremental-check correctness

For push-based incremental checks, compare against the latest successful run of the same workflow and branch, not merely the previous push event.

1. Query completed runs for the same workflow and branch.
2. Select the latest successful run and read its exact `head_sha`.
3. Use the GitHub compare API before checkout to confirm that the baseline is an ancestor of the current commit. Accept `ahead` or `identical`; treat missing, failed, or divergent comparisons as an invalid baseline.
4. Check every relevant file changed since that baseline.
5. Run a full audit when the baseline is missing or invalid.

Do not rely only on `github.event.before`: a cancelled run may contain commits omitted from the next push's event diff.

Prefer `fetch-depth: 1`. After checkout, fetch only the successful baseline commit with `git fetch --no-tags --depth=1 origin "$BASE_SHA"`. If that fetch fails, run a full audit rather than omitting changes. Use full history only when the workflow's Git operations genuinely require it. Do not use `git merge-base` as an ancestry test in a shallow checkout.

Do not treat failed, cancelled, queued, or in-progress runs as successful baselines. For pull-request checks, compare the pull-request head with the appropriate base commit; do not reuse a push baseline without a clear reason.

## 7. Cache dependencies only when useful

- Cache dependencies that are expensive to download or install and can be safely reused.
- Build keys from the operating system, runtime, package manager, and dependency lockfiles.
- Use restore prefixes only when older cache contents remain compatible.
- Prefer supported cache options in official setup actions when they meet the requirement.
- Do not cache standard-library-only jobs, secrets, credentials, or sensitive build outputs.
- Do not add caching when restore/save overhead exceeds the work avoided.
- Prevent untrusted jobs from writing cache content later consumed by privileged workflows.

## 8. Choose runners and timeouts

- Select the least costly supported runner that meets operating-system, architecture, toolchain, and security requirements.
- Do not use Linux when the job requires Windows or macOS behavior.
- Pin a runner image when reproducibility requires a specific environment.
- Set `timeout-minutes` for every job and a step timeout when an individual command can hang.
- Use self-hosted runners only when their isolation and maintenance model are suitable.

Do not repeat historical runner prices, billing multipliers, minute-rounding rules, or quotas as current facts without checking current official GitHub billing documentation.

## 9. Minimize artifact storage

- Upload only outputs that later jobs or users need.
- Exclude temporary and reproducible files when they are not required.
- Compress large outputs when compression reduces transfer or storage cost.
- Set `retention-days` to the shortest period that still meets the workflow's operational needs.
- Download only artifacts required by a later job.
- Do not add artifact settings to workflows that do not upload artifacts.

Logs and workflow artifacts can have different storage rules. Check current GitHub documentation before stating limits or defaults.

## 10. Apply least privilege and protect inputs

Set permissions explicitly at workflow or job level. Grant each job only what it needs.

- Use `contents: read` for checkout-only jobs.
- Grant `actions: write` only to jobs that must cancel or modify workflow runs.
- Use `permissions: {}` when a job does not need a GitHub token.
- Grant write permissions at job level when only one job needs them.
- Prefer short-lived credentials and OpenID Connect when supported by the deployment provider.
- Do not expose secrets to untrusted pull-request code.
- Do not use `pull_request_target` to execute untrusted pull-request code with elevated permissions.
- Pass event values to scripts through environment variables; quote and validate them.
- Do not interpolate untrusted event data directly into shell commands.
- Follow repository policy for action pinning and verify an action's owner/source before adopting a version.
- Isolate self-hosted runners that execute untrusted code.

## 11. Keep workflow structure maintainable

- Use separate workflows when triggers, permissions, validation scopes, or operational lifecycles differ.
- Use a reusable workflow when multiple workflows genuinely share a maintained job sequence. Do not abstract a single small job without a clear reuse case.
- Keep permissions, concurrency, runner choice, and timeouts close to the job that uses them.
- Explain non-obvious conditions that protect coverage or safety.
- Do not duplicate checks without a distinct purpose.
- Do not remove a full audit merely because an incremental check is faster.
- Batch related workflow, script, and documentation edits into one coherent commit to avoid intermediate pushes and duplicate CI runs.

## 12. Decision checklist

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
10. Has the assistant avoided manually dispatching, rerunning, or polling CI unless the user explicitly requested CI investigation?

## 13. Official references

- [Workflow syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)
- [Workflow concurrency](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs)
- [Dependency caching](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows)
- [Workflow artifacts](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts)
- [Secure use reference](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)
