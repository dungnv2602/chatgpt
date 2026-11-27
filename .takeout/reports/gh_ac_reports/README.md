# GitHub Actions diagnostic reports

This directory is the review surface for actionable GitHub Actions execution failures and operational exceptions. It complements the STE lint evidence in the separate `.takeout/reports/lint_reports/` directory. Ordinary successful runs and cancellation-only runs are not persisted by default.

## Review order

1. Read `index.json` for the latest captured runs, pending run IDs, and the sweep watermark.
2. Read the `latest_report.history_path` entry in `index.json` to locate the newest canonical report.
3. Use the history path to inspect `report.json`, `integrity.json`, and captured job logs.
4. Render a human-readable Markdown view when needed:
   - Latest report: `python3 .agent/skills/the-worker/scripts/actions-report.py --render-latest`
   - Exact report: `python3 .agent/skills/the-worker/scripts/actions-report.py --render history/<workflow-id>/<run-id>-attempt-<attempt>-<stage>`
   Both commands write Markdown to stdout; redirect it to a temporary file if a persistent view is required.
5. Follow the Actions run URL when GitHub has evidence the reporter cannot access.

## Canonical evidence layout

- `history/<workflow-id>/<run-id>-attempt-<attempt>-<stage>/` stores each immutable capture.
- Each capture contains `report.json`, `integrity.json`, and `logs/job-<job-id>.log` files.
- `index.json` is the only index and latest-report pointer. It also records pending run IDs and the sweep watermark.
- `requests/pending/<request-name>.json` requests a backfill for one exact run. The JSON must contain a numeric `run_id`. A processed request moves to `requests/processed/`.
- There are no stored Markdown report copies, root latest-report copies, or per-workflow indexes/latest copies. Workflow-specific views can be derived by filtering the central index on `workflow_id`.

## Capture policy

- Only completed source runs are eligible for capture. In-progress, queued, pending, and other unfinished states are never written to report history.
- The diagnostics workflow listens for completed source workflows and runs the post-run sweep. Pending IDs discovered by an earlier push-triggered sweep are retried after the source workflow completes.
- A report is persisted only when classification contains at least one independent error: a failed job/step, a timeout, an action-required outcome, or a classified workflow-startup/configuration failure.
- Ordinary success, cancellation-only, skipped, neutral, and other issue-free outcomes are handled without report history.
- Every diagnostics sweep prunes legacy history outside this retention contract, removes derived report views, regenerates integrity manifests for canonical JSON and logs, and rebuilds the central index. Pending run IDs are preserved for completion-time capture.
- A cancelled run is retained only when it contains an independent completed job or step failure. Cancellation and downstream status-propagation failures do not qualify.
- A successful run with an independently failed non-blocking step is an error report and is retained.
- Manual requests can select older runs, but cannot override the error-only retention rule. A successful or cancellation-only run is never forced into report history.
- Reporter retention and Ledger ingestion use the same shared independent-error predicate. The reporter may retain an incomplete post-run error capture while bounded evidence retries continue; the Ledger creates observations only after capture completeness is Complete. Each retained complete error report is ingested. Every independent finding is task-eligible regardless of confidence-derived severity; stable finding and remediation-group identities deduplicate recurring errors and reuse active tasks.

## Failure classification

The report preserves the source conclusion reported by GitHub. Report-generation success does not mean that the source workflow succeeded.

- `failure`: GitHub reports failure.
- `cancelled`: GitHub reports cancellation. Cancellation alone does not create a report for new runs. A cancelled run with an independent classified failure is captured; cancellation and known downstream status-propagation steps do not create issues. Historical cancellation-only captures are removed by the retention sweep.
- `timed_out`: GitHub reports a timeout.
- `action_required`: GitHub reports an action-required state.
- `skipped` and `neutral` remain non-failure outcomes.
- `queued` and `in_progress` are not completed outcomes.
- `workflow_startup_or_configuration_failure` is a low-confidence classification when a failed run has no job records.
- `runner_initialization_failure` is used only when a job failed without step evidence.
- Explicit unittest failure markers take precedence over incidental keywords in captured output.
- Markers include `AssertionError`, `FAIL: test_`, `ERROR: test_`, and unittest failure summaries.
- These markers classify the step as `validation_or_test`, even when captured output includes `git push` or `checkout` text.
- For structured tab-delimited logs, the reporter uses only lines that match the failed step name.
- If no line matches, it does not reuse output from other steps.
- For unstructured logs, it uses the available log text.
- Other categories use job names, step names, annotations, and logs as diagnostic signals. They do not prove root cause.

A step can fail while its job succeeds when the workflow allows the step to continue. The report records step and job conclusions separately.

## Evidence limits and security

The collector records workflow metadata, job and step states, runner identifiers, check runs, annotations, artifact metadata, and sanitized job logs where GitHub exposes them. Check-run annotations use GitHub's array response format. It records artifact metadata but does not download artifact contents.

GitHub may not expose logs for a job that never started. Logs may expire, and annotations may be absent. These conditions appear in capture_errors and make the report Incomplete. A failed run with no job records is classified as a possible startup or configuration failure, not as a proven YAML error.

The collector redacts common token, authorization, password, and cloud-key patterns. GitHub also masks configured secrets. Do not echo credentials or sensitive personal data in workflow logs. Captured logs are committed to this private repository as diagnostic evidence.

## Coverage on branch gpt

Each source workflow runs a normal diagnostics job with job-level `continue-on-error: true`. That job checks out branch `gpt` and calls `.takeout/reports/gh_ac_reports/actions/capture`, a local composite action. This keeps report generation outside the source validation result. The separate push-triggered sweep backfills completed runs and catches failures when the finalizer does not run. It does not rely on a default-branch observer or scheduled trigger.

The repository default branch is `main`. GitHub only starts `workflow_run` and schedule observers when the workflow file exists on the default branch. This implementation does not change `main`. A workflow that fails before any job starts is discovered on a later `gpt` push or by a request file. Instant capture of that case needs a default-branch observer or an external GitHub App webhook.

When a new workflow is added, append a normal job that needs the source jobs, uses `if: always()` and job-level `continue-on-error: true`, checks out `gpt`, and calls `./.takeout/reports/gh_ac_reports/actions/capture`. The push sweep still backfills runs when the finalizer does not run.

## Relationship to lint reports

Detailed lint findings, per-file metrics, fingerprints, and baselines remain in `.takeout/reports/lint_reports`. This report captures workflow, job, step, log, annotation, artifact, and publication context around a lint run. It links to the matching lint scope rather than duplicating its findings. This layout change does not modify the separate STE lint report layout.

## Integrity and history

Each retained post-run error capture is immutable. The retention sweep removes pre-finalizer captures and any success-only, cancellation-only, or otherwise issue-free records, then removes only derived Markdown/navigation copies and rebuilds the central index. Canonical `report.json` and captured log bytes remain unchanged. SHA-256 values in `integrity.json` cover `report.json` and every captured job log. The generator verifies each manifest after it writes it. Every diagnostics sweep regenerates and verifies all retained manifests before it continues. A mismatch stops the sweep and prevents publication.

The central latest pointer advances by source run time, attempt, and capture-stage precedence. Markdown is rendered from canonical JSON on demand and is not committed as a report artifact. Generated evidence is machine-owned.

Change the schema, template, collector, generator, regression tests, workflow integration, this guide, and the Document Type Catalog together.

## Publication concurrency

All source-workflow finalizers and the push-driven sweep use the same repository-wide concurrency group with `cancel-in-progress: false` and `queue: max`. GitHub runs one writer at a time and retains up to 100 pending writers instead of replacing the previous pending writer. Requests beyond that platform limit can still be cancelled. Dependent workflow jobs acquire the group sequentially, so no job holds the writer group while waiting for another writer. If a publication still fails, the next sweep can backfill completed runs; do not resolve concurrent index conflicts by discarding immutable captures.

## Changed-document evidence publication retries

The changed-document lint workflow uses up to five push attempts. Before each attempt, it fetches `gpt` and rebases its report commit onto the latest branch. A rebase conflict stops publication and leaves source reports unchanged. After a failed push, the job fetches `gpt` again. It retries only when the remote branch advanced. A failed push with an unchanged remote branch stops immediately. The workflow reports failure after five unsuccessful attempts. It never drops immutable report evidence to resolve a conflict.

## Reporter self-monitoring

The diagnostics workflow is deliberately excluded from its own run sweep to prevent recursive report generation. Its own failures are not included in the reports it creates. Inspect the diagnostics workflow's own run and job logs directly in the GitHub Actions interface. Failure of the report-only job in a source workflow is separately contained by the caller's job-level `continue-on-error: true` setting. Explicit backfill requests do not override the error-only retention rule; successful and cancellation-only runs are never retained.

If a diagnostics run fails before GitHub exposes job steps or a log URL, record an evidence gap and leave pending IDs unchanged. Do not infer a source-workflow defect from an empty job record. Allow a later eligible `gpt` push to trigger another sweep; do not dispatch or poll the failed diagnostics run.

## Bounded retry and request handling

Automatic post-run captures retry an Incomplete report at most three times per source run attempt, with at least one hour between attempts. The collector records exhausted run IDs in `exhausted_run_ids` and removes them from `pending_run_ids`. Review exhausted reports and submit a new explicit request only when another capture attempt is justified.

A request in `requests/pending/` is consumed into `requests/processed/` after one completed-run capture result. The processed request records `Complete`, `Incomplete`, or `Not actionable`, the processing timestamp, and the incomplete report path when available. An incomplete requested capture remains in the normal pending queue only while the automatic retry budget remains. The request file itself does not replay every sweep.

A complete capture is never rewritten or duplicated, even when a manual request uses force mode. Force bypasses the automatic backoff for one explicit request, but does not bypass the completed-capture guard.

## Reporting periods

A clean-start reset requires explicit user authorization. It deletes active generated report payloads, workflow snapshots, latest pointers, request queues, and all previous `workspace/archive/reports/**` period snapshots. It resets the repository-wide index and request state to an empty reporting period with a new UTC watermark. It does not delete scripts, schemas, templates, assets, workflow definitions, operator guides, or task archives.

The first report captures source runs created after the reset watermark. Do not carry pending runs or import old reports into the new period. Use the normal report indexes and immutable post-reset capture paths from then onward.

Normal report rollover is different: it preserves open-finding evidence and does not clear the Ledger. See `.takeout/reports/triage/README.md` for task-linked finding retirement and baseline seeding.


## Worker governance

The Worker skill `.agent/skills/the-worker/SKILL.md` is the operational owner of this report family. Its GitHub Actions reference governs diagnosis and remediation. The workflow, capture action, generator, schema, template, index, and history paths remain stable implementation locations until a coordinated relocation updates all callers.
