# {scope_title} STE Lint Evidence Report

- **Result:** {status}
- **Schema version:** {schema_version}
- **Run:** [#{run_number}]({run_url})
- **Run ID / attempt:** {run_id} / {attempt}
- **Workflow:** {workflow}
- **Branch / commit:** {branch} / {commit}
- **Event:** {event}
- **Execution mode:** {mode}
- **Baseline SHA:** {baseline_sha}
- **Linter source SHA:** {linter_source_sha}
- **Generated (UTC):** {generated_at}

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | {files_evaluated} |
| Files that failed | {files_failed} |
| Files with findings | {files_with_findings} |
| Total findings | {total_findings} |
| Hard findings | {hard_findings} |
| Advisory findings | {advisory_findings} |
| New findings | {new_findings} |
| Recurring findings | {recurring_findings} |
| Resolved findings | {resolved_findings} |
| Failed workflow checks | {failed_checks} |

## 2. Execution environment

- Runner OS: {runner_os}
- Python: {python_version}
- Platform: {platform}
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

{files_list}

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

{file_summary}

## 5. Findings by rule

Counts include hard and advisory findings.

{rule_summary}

## 6. Workflow and validation checks

Each check includes its observed result, exit code, and complete captured output. A skipped check is not a pass.

{checks}

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

{baseline_comparison}

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

{per_file_results}

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
