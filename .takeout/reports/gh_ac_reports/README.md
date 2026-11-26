# GitHub Actions diagnostic reports

This directory is the review surface for actionable GitHub Actions execution failures and operational exceptions. It complements the STE lint evidence in the separate `.takeout/reports/lint_reports/` directory. Ordinary successful runs and cancellation-only runs are not persisted by default.

## Review order

1. Read index.json for the latest captured runs, pending run IDs, and the sweep watermark.
2. Read latest-gh-ac-report.md for the newest captured report.
3. Open by_workflow/<workflow-id>/index.json and latest-report.md for workflow-specific history.
4. Read the immutable history entry for the exact run ID, attempt, and capture stage.
5. Open captured job logs and report.json for full evidence.
6. Follow the Actions run URL when GitHub has evidence the reporter cannot access.

## Evidence layout

- history/<workflow-id>/<run-id>-attempt-<attempt>-<stage>/ stores immutable captures.
- Each capture has report.md, report.json, integrity.json, and logs/job-<job-id>.log files.
- by_workflow/<workflow-id>/ contains a workflow index and latest pointers.
- index.json is the repository-wide index and records pending run IDs and the sweep watermark.
- latest-gh-ac-report.md and latest-gh-ac-report.json point to the newest capture.
- requests/pending/<request-name>.json requests a backfill for one exact run. The JSON must contain a numeric run_id. A processed request moves to requests/processed/.

## Capture policy

- Only completed source runs are eligible for capture. In-progress, queued, pending, and other unfinished states are never written to report history.
- The diagnostics workflow listens for completed source workflows and runs the post-run sweep. Pending IDs discovered by an earlier push-triggered sweep are retried after the source workflow completes.
- A report is persisted only when classification contains at least one independent error: a failed job/step, a timeout, an action-required outcome, or a classified workflow-startup/configuration failure.
- Ordinary success, cancellation-only, skipped, neutral, and other issue-free outcomes are handled without report history.
- Every diagnostics sweep prunes legacy history outside this retention contract and rebuilds the root and per-workflow indexes/latest pointers from retained reports. Pending run IDs are preserved for completion-time capture.
- A cancelled run is retained only when it contains an independent completed job or step failure. Cancellation and downstream status-propagation failures do not qualify.
- A successful run with an independently failed non-blocking step is an error report and is retained.
- Manual requests can select older runs, but cannot override the error-only retention rule. A successful or cancellation-only run is never forced into report history.
- Each retained Actions report is ingested into the Ledger. Every independent finding is task-eligible regardless of confidence-derived severity; stable finding and remediation-group identities deduplicate recurring errors and reuse active tasks.

## Failure classification

The report preserves the source conclusion reported by GitHub. Report-generation success does not mean that the source workflow succeeded.

- failure: GitHub reports failure.
- cancelled: GitHub reports cancellation. Cancellation alone does not create a report for new runs. A cancelled run with an independent classified failure is captured; cancellation and known downstream status-propagation steps do not create issues. Historical cancellation-only captures are removed by the retention sweep.
- timed_out: GitHub reports a timeout.
- action_required: GitHub reports an action-required state.
- skipped and neutral remain non-failure outcomes.
- queued and in_progress are not completed outcomes.
- workflow_startup_or_configuration_failure is a low-confidence classification when a failed run has no job records.
- runner_initialization_failure is used only when a job failed without step evidence.
- Other categories use job names, step names, annotations, and logs as diagnostic signals. They do not prove root cause.

A step can fail while its job succeeds when the workflow allows the step to continue. The report records step and job conclusions separately.

## Evidence limits and security

The collector records workflow metadata, job and step states, runner identifiers, check runs, annotations, artifact metadata, and sanitized job logs where GitHub exposes them. Check-run annotations use GitHub's array response format. It records artifact metadata but does not download artifact contents.

GitHub may not expose logs for a job that never started. Logs may expire, and annotations may be absent. These conditions appear in capture_errors and make the report Incomplete. A failed run with no job records is classified as a possible startup or configuration failure, not as a proven YAML error.

The collector redacts common token, authorization, password, and cloud-key patterns. GitHub also masks configured secrets. Do not echo credentials or sensitive personal data in workflow logs. Captured logs are committed to this private repository as diagnostic evidence.

## Coverage on branch gpt

Each source workflow runs a normal diagnostics job with job-level `continue-on-error: true`. That job checks out branch `gpt` and calls `.takeout/reports/gh_ac_reports/actions/capture`, a local composite action. This keeps report generation outside the source validation result. The separate push-triggered sweep backfills completed runs and catches failures when the finalizer does not run. It does not rely on a default-branch observer or scheduled trigger.

The repository default branch is main. GitHub only starts workflow_run and schedule observers when the workflow file exists on the default branch. This implementation does not change main. A workflow that fails before any job starts is discovered on a later gpt push or by a request file. Instant capture of that case needs a default-branch observer or an external GitHub App webhook.

When a new workflow is added, append a normal job that needs the source jobs, uses `if: always()` and job-level `continue-on-error: true`, checks out `gpt`, and calls `./.takeout/reports/gh_ac_reports/actions/capture`. The push sweep still backfills runs when the finalizer does not run.

## Relationship to lint reports

Detailed lint findings, per-file metrics, fingerprints, and baselines remain in `.takeout/reports/lint_reports`. This report captures workflow, job, step, log, annotation, artifact, and publication context around a lint run. It links to the matching lint scope rather than duplicating its findings.

## Integrity and history

Each retained post-run error capture is immutable. The retention sweep removes pre-finalizer captures and any success-only, cancellation-only, or otherwise issue-free records, then rebuilds indexes and latest pointers. A later post-run capture does not rewrite a retained report. SHA-256 values in integrity.json cover report.md, report.json, and every captured log.

Index latest pointers advance by source run time, attempt, and capture-stage precedence. Older captures cannot replace newer pointers. Generated reports are machine-owned.

Change the schema, template, collector, generator, regression tests, workflow integration, this guide, and the Document Type Catalog together.

## Publication concurrency

All source-workflow finalizers and the push-driven sweep use the same repository-wide concurrency group with `cancel-in-progress: false` and `queue: max`. GitHub runs one writer at a time and retains up to 100 pending writers instead of replacing the previous pending writer. Requests beyond that platform limit can still be cancelled. Dependent workflow jobs acquire the group sequentially, so no job holds the writer group while waiting for another writer. If a publication still fails, the next sweep can backfill completed runs; do not resolve concurrent index conflicts by discarding immutable captures.

## Reporter self-monitoring

The diagnostics workflow is deliberately excluded from its own run sweep to prevent recursive report generation. Its own failures are not included in the reports it creates. Inspect the diagnostics workflow's own run and job logs directly in the GitHub Actions interface. Failure of the report-only job in a source workflow is separately contained by the caller's job-level `continue-on-error: true` setting. Explicit backfill requests do not override the error-only retention rule; successful and cancellation-only runs are never retained.

If a diagnostics run fails before GitHub exposes job steps or a log URL, record an evidence gap and leave pending IDs unchanged. Do not infer a source-workflow defect from an empty job record. Allow a later eligible `gpt` push to trigger another sweep; do not dispatch or poll the failed diagnostics run.

## Resolution and archive

The cross-family issue state is tracked in `.takeout/reports/triage/ledger.json`. A finding is resolved only after its fix commit and successful relevant validation are recorded. The successful run URL and UTC timestamp are sufficient; a full successful-run diagnostic report is not required. Use a request file only when the successful run's detailed evidence is specifically needed. Resolved report files are moved to `.archive/reports/`; the shared archive-retention workflow deletes each exact indexed file after 90 days. The archive uses the shared `.github/archive-retention-index.json`. Do not create a report archive under `.takeout/reports/` or a separate retention workflow.


## Bounded retry and request handling

Automatic post-run captures retry an Incomplete report at most three times per source run attempt, with at least one hour between attempts. The collector records exhausted run IDs in `exhausted_run_ids` and removes them from `pending_run_ids`. Review exhausted reports and submit a new explicit request only when another capture attempt is justified.

A request in `requests/pending/` is consumed into `requests/processed/` after one completed-run capture result. The processed request records `Complete`, `Incomplete`, or `Not actionable`, the processing timestamp, and the incomplete report path when available. An incomplete requested capture remains in the normal pending queue only while the automatic retry budget remains. The request file itself does not replay every sweep.

A complete capture is never rewritten or duplicated, even when a manual request uses force mode. Force bypasses the automatic backoff for one explicit request, but does not bypass the completed-capture guard.

## Reporting periods

A clean-start reset requires explicit user authorization. It deletes active generated report payloads, workflow snapshots, latest pointers, request queues, and all previous `.archive/reports/**` period snapshots. It resets the repository-wide index and request state to an empty reporting period with a new UTC watermark. It does not delete scripts, schemas, templates, assets, workflow definitions, operator guides, or task archives.

The first report captures source runs created after the reset watermark. Do not carry pending runs or import old reports into the new period. Use the normal report indexes and immutable post-reset capture paths from then onward.

Normal report rollover is different: it preserves open-finding evidence and does not clear the Ledger. See `.takeout/reports/triage/README.md` for task-linked finding retirement and baseline seeding.
