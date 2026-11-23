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
6. Perform all repository inspection and modification through GitHub's remote APIs. Do not use a local checkout or local shell, Git, Python, container, or filesystem tools for repository work.
7. GitHub-hosted Actions runners are the only permitted execution environment for repository scripts, tests, builds, and CI validation. Git commands inside an approved workflow run on those hosted runners are permitted. Inspect results through GitHub Actions logs and artifacts.

This boundary exists because no local project environment is provided and the remote repository is the sole source of truth. Local copies may be absent or stale, and local execution cannot establish the state or validity of the authorized remote branch.

## 2. Scheduled archive cleanup

GitHub Actions runs the scheduled archive-retention workflow.

- Run the schedule from the repository default branch because GitHub scheduled events only run there.
- Check out `gpt`, which is the working/source branch.
- Read only `.github/archive-retention-index.json`. Never list or scan `archive/tasks/`.
- Retain each indexed record for at least 90 days from its UTC archive timestamp.
- Delete only exact indexed paths that have reached 90 days. Remove their index entries after processing.
- Preserve `.gitkeep`. Unindexed legacy records remain protected and must not be discovered by a directory scan.
- Allow only the native `schedule` event. The cleanup script must reject every other GitHub event.
- After cleanup, atomically fast-forward `main` to the resulting `gpt` commit. Never force-push or create an independent cleanup commit on `main`.
- Check that `main` is an ancestor of `gpt` before pushing. If the branches diverge, fail safely without updating either ref.
- Use a weekly cron schedule. The retention index avoids a daily or per-file scheduled workflow and prevents routine archive scans.

## 3. Report triage and archive retention

- Start at `reports/README.md`; maintain cross-family issue state in `reports/triage/ledger.json`.
- Resolved report files belong in `archive/reports/`, not in a report-root archive folder.
- The shared archive-retention workflow retains each exact indexed file for 90 days and deletes only that file after expiry. It does not scan archive directories.
- The index is `.github/archive-retention-index.json`; preserve unindexed legacy files.

## 4. Task-scoped CI diagnostics and repair

CI is not a gate that must be repaired before every user prompt or after skill initialization. Inspect CI when the user requests it, when the current task changes a workflow or validation target, or when a known result directly affects the task.

1. Start with `gh_ac_reports/README.md` for workflow-level failures, jobs, steps, logs, annotations, artifact metadata, and evidence limitations.
2. For STE lint details, start with `lint_reports/README.md`. Use its scope index and structured JSON for exact file-level findings, metrics, and baselines.
3. Inspect only the runs and checks relevant to the current task. Use a bounded snapshot when fresh status is material. Do not scan the entire workflow history without a reason.
4. Preserve GitHub's actual conclusion. Distinguish failure, timed out, action required, cancelled, skipped, neutral, queued, and in-progress states. Cancellation and skipped outcomes are not automatically failures. Do not treat missing evidence as proof of a workflow-definition defect.
5. Repair only the cause that is inside the user's current scope or is a direct dependency of the task. Do not repair unrelated failures before handling the request. Never weaken tests, workflow coverage, permission requirements, or lint baselines to make a check pass.
6. Keep reporting and source validation separate. A successful report publication does not convert a failed source workflow into success. A diagnostic reporter failure must not change the source workflow's validation conclusion.
7. Never wait for or poll CI. Do not manually dispatch or rerun a workflow unless the user asks or the current task explicitly requires it.
8. Never run the STE linter, CI workflows, CI test suites, or repository scripts locally. Use GitHub-hosted Actions only.
9. If GitHub Actions or report evidence is unavailable, record the exact limitation and mark the result unverified. Continue unless the task directly depends on that evidence. Do not claim that CI passed.
## 5. Inspect and preserve validation scope

### Archive boundary for Markdown checks

- Exclude all paths under `archive/` from full-document and changed-document lint.
- Exclude archived Markdown files from link-source and heading-anchor checks.
- For links from active documents to `archive/`, check whether the target path exists during routine lint. Ignore fragments for these targets.
- Do not read archived files solely for routine link or heading-anchor checks. You may read an exact archived record when a task requires its content.
- Never edit, replace, rename, move, or manually delete an archived record. Only the scheduled retention workflow may delete archived records.
- Do not add an `archive/README.md` lint exception. The entire `archive/` tree is outside lint scope.

Before changing a workflow, identify its events, branch/path filters, jobs, dependencies, permissions, concurrency, runner, timeout, cache, artifact behavior, and scripts. Identify which checks cover which files.

- Do not optimize by removing a required test or weakening its validation scope.
- Preserve required push, pull-request, release, and schedule events.
- Include workflow files, scripts, configuration, lockfiles, and source data that affect the result in the appropriate path filters.
- Keep full audits and incremental checks separate when they have different validation scopes.
- Avoid duplicate runs caused by overlapping triggers.

## 6. Design precise triggers

Use branch and path filters to avoid work that cannot check the changed files.

- When both branch and path filters exist, both conditions must match.
- GitHub evaluates path patterns in order. A later positive pattern can include a path that an earlier pattern excluded. A later negative pattern can exclude a path that an earlier pattern included.
- When using negative patterns inside `paths`, include at least one positive pattern.
- Do not use both `paths` and `paths-ignore` for the same event.
- Check branch-protection requirements before adding workflow-level filters. A skipped workflow can leave a required check pending. Use job-level conditions or a stable required check when every pull request needs a result.

## 7. Control concurrency and superseded runs

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

## 8. Preserve incremental-check correctness

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

This section consolidates repository execution-efficiency rules. This skill defines GitHub Actions validation scope and workflow behavior.

### Before editing

1. Inspect the branch head and the exact files, scripts, and configuration relevant to the request.
2. Identify the required change set. Do not expand the task into unrelated cleanup.
3. Reuse verified reads and tool results. Do not repeat searches or status checks without new evidence.
4. Batch related edits into one coherent commit. Avoid intermediate commits that create duplicate push-triggered runs.
5. Review the complete changed sections. Preserve facts, conditions, exceptions, numbers, scope, and modality.

### CI and validation scope

Apply Section 3 only when CI is relevant to the user's current request. Do not run a pre-prompt or post-initialization CI gate. Do not wait for or poll in-progress runs. Let GitHub-hosted Actions run validation; never run CI workflows or the STE linter locally.

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

- [Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [Workflow concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency)
- [Dependency caching](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching)
- [Workflow artifacts](https://docs.github.com/en/actions/tutorials/store-and-share-data)
- [Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)
