# GitHub Actions diagnostic reports

This directory is the review surface for GitHub Actions execution failures and operational warnings. It complements the STE lint evidence in the separate lint_reports directory.

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

## Capture stages

- pre_finalizer is captured by the local composite action in a normal diagnostics job after the source jobs finish. The parent workflow is still in progress. The report records the observed status, finished source jobs, and a projected conclusion. It does not invent a final conclusion.
- post_run is captured by the push-driven sweep after GitHub marks the source run completed. It records the actual conclusion. It is a separate immutable capture. It does not overwrite pre_finalizer evidence.

The sweep stores pending run IDs for queued, running, or incomplete captures. It checks pending IDs during a later sweep. It also discovers runs created since the bootstrap watermark, including tag and scheduled runs. A request file can capture an older run.

## Failure classification

The report preserves the source conclusion reported by GitHub. Report-generation success does not mean that the source workflow succeeded.

- failure: GitHub reports failure.
- cancelled: GitHub reports cancellation. Cancellation is not automatically a failure.
- timed_out: GitHub reports a timeout.
- action_required: GitHub reports an action-required state.
- skipped and neutral remain non-failure outcomes.
- queued and in_progress are not completed outcomes.
- workflow_startup_or_configuration_failure is a low-confidence classification when a failed run has no job records.
- runner_initialization_failure is used only when a job failed without step evidence.
- Other categories use job names, step names, annotations, and logs as diagnostic signals. They do not prove root cause.

A step can fail while its job succeeds when the workflow allows the step to continue. The report records step and job conclusions separately.

## Evidence limits and security

The collector records workflow metadata, job and step states, runner identifiers, check runs, annotations, artifact metadata, and sanitized job logs where GitHub exposes them. It records artifact metadata but does not download artifact contents.

GitHub may not expose logs for a job that never started. Logs may expire, and annotations may be absent. These conditions appear in capture_errors and make the report Incomplete. A failed run with no job records is classified as a possible startup or configuration failure, not as a proven YAML error.

The collector redacts common token, authorization, password, and cloud-key patterns. GitHub also masks configured secrets. Do not echo credentials or sensitive personal data in workflow logs. Captured logs are committed to this private repository as diagnostic evidence.

## Coverage on branch gpt

Each source workflow runs a normal diagnostics job with job-level `continue-on-error: true`. That job checks out branch `gpt` and calls `gh_ac_reports/actions/capture`, a local composite action. This keeps report generation outside the source validation result. The separate push-triggered sweep backfills completed runs and catches failures when the finalizer does not run. It does not rely on a default-branch observer or scheduled trigger.

The repository default branch is main. GitHub only starts workflow_run and schedule observers when the workflow file exists on the default branch. This implementation does not change main. A workflow that fails before any job starts is discovered on a later gpt push or by a request file. Instant capture of that case needs a default-branch observer or an external GitHub App webhook.

When a new workflow is added, append a normal job that needs the source jobs, uses `if: always()` and job-level `continue-on-error: true`, checks out `gpt`, and calls `./gh_ac_reports/actions/capture`. The push sweep still backfills runs when the finalizer does not run.

## Relationship to lint reports

Detailed lint findings, per-file metrics, fingerprints, and baselines remain in lint_reports. This report captures workflow, job, step, log, annotation, artifact, and publication context around a lint run. It links to the matching lint scope rather than duplicating its findings.

## Integrity and history

Report captures are append-only. A later post_run capture does not rewrite pre_finalizer evidence. SHA-256 values in integrity.json cover report.md, report.json, and every captured log.

Index latest pointers advance by source run time, attempt, and capture-stage precedence. Older captures cannot replace newer pointers. Generated reports are machine-owned.

Change the schema, template, collector, generator, regression tests, workflow integration, this guide, and the Document Type Catalog together.

## Reporter self-monitoring

The diagnostics workflow is deliberately excluded from its own run sweep to prevent recursive report generation. Its own failures are not included in the reports it creates. Inspect the diagnostics workflow's own run and job logs directly in the GitHub Actions interface. Failure of the report-only job in a source workflow is separately contained by the caller's job-level `continue-on-error: true` setting.
