# Current Step

- **2026-11-23 — Lint-report evidence system implemented on `gpt`.** Reporting architecture, generator, tests, scope indexes, legacy migration, and both lint-workflow integrations are committed and read back. Hosted validation is pending. Do not describe the new reporting workflows or regression tests as passed until their runs are reviewed.
- **Current branch head before this register update:** `0b9f4848fa2aadcd1dd2fb156b1d323a6907d381`.
- **Review policy:** Read `lint_reports/README.md` and the relevant scope index first. Use Actions artifacts only when the repository evidence does not answer the question.

## Open Discussions

- **Hosted validation pending:** The full-document workflow now runs report-tool syntax checks and regression tests. A new hosted run should be triggered by the workflow/script changes. Do not poll or manually dispatch it. Review its completed result during the next authorized preflight.
- **Changed-document report not yet exercised:** `on_changed/index.json` is initialized and empty. The next eligible changed-Markdown push will exercise incremental or full-audit-fallback publication. Do not claim this path is hosted-verified yet.
- **Existing lint debt remains:** Run `45107478771` (#106) passed the linter self-test and Markdown anchor check, generated the prior repository-wide report, and failed the final audit result because the existing lint findings exceeded configured thresholds. Reporting work did not change lint rules or baselines.

## Reports

### 2026-11-23 — Lint-report evidence system

- **User authorization:** Execute the approved detailed reporting design. Make `/lint_reports` self-sufficient for routine investigation. JSON is the structured evidence layer. Markdown is the analysis layer. Raw Actions logs remain fallback evidence.
- **Structure:** Added `lint_reports/on_repo/` and `lint_reports/on_changed/`, each with a README, `index.json`, and latest Markdown/JSON pointers. Per-run history uses run ID plus attempt to avoid overwriting reruns. The root `lint_reports/latest-lint-report.md` remains a compatibility path. Scope-specific reports are canonical.
- **Changed-document pipeline:** Added `skills/asd-ste100/scripts/generate_lint_report.py` and hosted regression tests. Extended `ste-lint-repository.sh` with optional `--json`, preserving its default output. The changed workflow captures per-file structured output, exact paths, exit codes, baseline SHA, stable finding fingerprints, new/recurring/resolved comparisons, runtime metadata, and full-audit-fallback mode. It publishes immutable report history, latest pointers, an index, SHA-256 integrity data, and the full-fallback anchor-check log. It preserves lint failure as the workflow conclusion and does not publish cancelled/superseded runs.
- **Repository-wide pipeline:** Updated `.github/workflows/ste-lint-full-docs.yml` to validate the report tooling, record the exact evaluated paths, structure findings from the original diagnostics, preserve the Markdown transcript, and publish JSON, Markdown, SHA-256 integrity data, history, latest pointers, and index atomically. Existing lint commands, scope, thresholds, and failure conditions remain unchanged.
- **Legacy migration:** Migrated the previous root report for run `45107478771` (#106) to `on_repo/history/45107478771/report.md` and JSON. Parsed all 453 diagnostic lines into structured findings grouped by rule. The old report did not enumerate all 48 evaluated paths, so the migration explicitly marks that path list unavailable. The legacy record predates the integrity manifest. Future workflow-generated records include exact coverage and integrity data.
- **Hosted evidence:** The inspected run #106 is from before the final report-workflow changes. Its self-test and anchor check passed, its audit step and report commit completed, and the final audit result failed on existing lint findings. The new report-generator tests have not yet been verified in Actions. The changed-document report path has not yet run.
- **Branch discipline:** All intended implementation files are on `gpt`. One root README creation briefly landed on `main` through the connector despite the explicit branch argument. A follow-up deleted it. The final `main` tree SHA `a15c4af352fe32f904c07c7624c84a371f174a3b` matches the tree of merge commit `1db67e1c681dd421e040407cf8fa3c801c347d39`. Main's content tree is unchanged, though the two corrective commits remain in its history.
- **Safeguards:** No archive files were accessed or changed. No lint baseline or rule was modified. No unrelated workflow was changed. All repository operations used GitHub APIs. Read-back checks confirmed the implementation files and migrated reports on `gpt`.

### 2026-11-23 — Approved archive-retention and STE lint remediation

- **Result:** Implemented and read back all changed paths on `gpt`. Archive retention uses a small index, a weekly schedule, and 90-day per-record eligibility. The cleanup script reads only the index, validates exact task-record paths, rejects non-scheduled/non-Actions execution, runs six temporary-file regression tests before cleanup, and stages only the index plus exact deleted paths. The index starts empty with unindexed legacy records protected. Only the exact `archive/README.md` policy file was fetched. No archive directory listing or recursive scan was performed.
- **STE lint:** Replaced the template's inconsistent “Check” verb with “Verify”. Added `lint_reports/` exclusions to the changed-workflow path filter, full-audit source list, and incremental changed-file list. No lint rules or baselines changed.
- **Policy alignment:** Updated `archive/README.md`, `skills/github-actions/SKILL.md`, `skills/the-worker/SKILL.md`, and `skills/session-archiving/SKILL.md`. Task closeout registers the exact archive path and UTC timestamp in the index.
- **Verification:** The six archive-retention regression tests remain unverified in hosted Actions. The changed-document STE workflow status was previously unavailable. Do not claim either CI result passed.
