# Task: Repair lint-report evidence workflow and unify report generation

## Metadata

- **Template version:** 1.1
- **ID:** 20261123-051200
- **Created:** 2026-11-23 05:12 UTC
- **Updated:** 2026-11-23 05:21 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** 20261123-041640, 20261123043747
- **Archived:** No

## 1. Original Request

> Start session, then read below:
>
> Looked like CI /lint_reports did not doing the work. There's no report inside /on_changed. Investigate, fix issues, and tighten and optimize the workflow, make the report more details compared to the artifacts and more easily for you to work with.

## 2. Subsequent Instructions

- **2026-11-23:** Use the GitHub repository `dungnv2602/chatgpt`, branch `gpt`, as the sole project source of truth. Do not use Library.
- **2026-11-23:** The user invoked `start session`. Complete foundational initialization and the bounded CI preflight before project work.
- **2026-11-23:** The user authorized investigation and repair of the lint-report workflow and reporting system.

## 3. Objective

Repair the changed-document lint evidence pipeline. Unify repository-wide and changed-document report generation. Publish complete, detailed, machine-readable reports that support efficient review and future task recovery.

## 4. Requirements

1. Ensure each eligible changed-document run publishes a Markdown report, structured JSON, integrity manifest, scope index entry, latest pointers, and immutable history.
2. Correct the report-generator invocation and template-link validation defects.
3. Correct repository-wide coverage extraction and remove the duplicated inline JSON conversion.
4. Use one tested generator and compatible schema for both report scopes.
5. Make Markdown reports more complete than the transient CI evidence. Include exact file coverage, per-file metrics and outcomes, all findings, rule totals, baseline comparisons, check results, run metadata, and relevant execution failures.
6. Preserve the original per-file structured linter records and diagnostic fields in JSON.
7. Keep report status distinct from lint findings and execution failures. Do not hide findings, weaken baselines, or remove checks.
8. Keep report scopes, history, latest pointers, index entries, and compatibility paths clear and documented.
9. Add regression tests for both scopes, template placeholders, exact coverage, detailed findings, failure records, comparisons, latest pointers, index entries, and integrity hashes.
10. Preserve workflow triggers, incremental-baseline correctness, permissions, concurrency safety, and hosted-only validation.
11. Read back every changed repository path and the final branch head. Do not wait for or poll CI.

## 5. Decisions

- Use the existing generator-owned lint-report format. Do not create a second report template or competing schema.
- Keep `lint_reports/on_changed/` as the canonical changed-document report scope.
- Keep `lint_reports/on_repo/` as the canonical repository-wide report scope.
- Keep the root `lint_reports/latest-lint-report.md` as a compatibility pointer unless the existing owner documentation supports a safe removal.
- Treat current hard lint findings as genuine until evidence proves a report parser defect. Do not raise baselines or reduce coverage to force a passing workflow.
- Make related changes in coherent commits. The Document Standards template-first rule requires the generator-owned format, catalog entry, owner instructions, and tests to be authoritative before publishing governed output changes.

## 6. Progress Log

### 2026-11-23 04:59 UTC

- **Action:** Completed the mandatory session-start sequence. Read Session Archiving, Conversation Mode, The Worker, Agent Skill Authoring, ASD-STE100, GitHub Actions, and the repository writing policy.
- **Result:** Foundational initialization passed. The startup notice was committed and read back. Default Mode applies.
- **References:** `skills/SESSION_START.md`, `skills/session-archiving/SKILL.md`, `skills/conversation-mode/SKILL.md`, `skills/the-worker/SKILL.md`, `skills/agent-skill-authoring/SKILL.md`, `skills/asd-ste100/SKILL.md`, `skills/github-actions/SKILL.md`, `skills/asd-ste100/references/repository-writing-policy.md`, `workspace/discussion.md`.
- **Next:** Complete the required post-load CI snapshot.

### 2026-11-23 05:04 UTC

- **Action:** Inspected the newest completed Actions runs on branch `gpt`, the current branch checks, and failed jobs.
- **Result:** Newest changed lint run `45115031724` failed. Newest full-document lint run `45114176416` failed after publishing its repository-wide evidence. Document Standards and image-conversion workflow runs succeeded. The current head had no completed check runs.
- **References:** [Changed lint run](https://github.com/dungnv2602/chatgpt/actions/runs/45115031724), [Full lint run](https://github.com/dungnv2602/chatgpt/actions/runs/45114176416), [Document Standards run](https://github.com/dungnv2602/chatgpt/actions/runs/45114777373).
- **Next:** Inspect workflow source, generator, schema, template, anchor checker, test coverage, and current report paths.

### 2026-11-23 05:08 UTC

- **Action:** Read both lint workflows, the shared generator, JSON Schema, report template, generator tests, anchor checker, report READMEs, current indexes, and report files.
- **Result:** Confirmed that `lint_reports/on_changed/` has no latest report or run history. Its index has an empty `runs` list. The changed workflow passes literal backslash arguments to the generator. The anchor checker treats `{run_url}` as a local file. The full workflow's unescaped backticks cause shell command substitution and blank coverage entries. Its separate inline JSON converter omits file-count and finding-count index fields and does not retain generator-style original per-file records.
- **References:** `.github/workflows/ste-lint-changed.yml`, `.github/workflows/ste-lint-full-docs.yml`, `skills/asd-ste100/scripts/generate_lint_report.py`, `skills/asd-ste100/scripts/test_generate_lint_report.py`, `skills/asd-ste100/scripts/check_markdown_anchors.py`, `skills/asd-ste100/assets/lint-report-template.md`, `skills/asd-ste100/assets/lint-report-schema.json`, `lint_reports/on_changed/`, `lint_reports/on_repo/`, `lint_reports/latest-lint-report.md`.
- **Next:** Complete the template-first owner review. Then implement a shared evidence contract and workflow integration.

### 2026-11-23 05:12 UTC

- **Action:** Read Document Standards, its Document Type Catalog, the workspace README, task board, and canonical task template. Checked the active task directory.
- **Result:** The board had no active task, and `workspace/tasks/` contained only `.gitkeep`. The catalog classified the changed report as Generator-owned and the repository-wide report as an Embedded contract. The two formats needed one owner.
- **References:** `skills/document-standards/SKILL.md`, `skills/document-standards/references/document-type-catalog.md`, `workspace/README.md`, `workspace/task_board.md`, `workspace/TASK_TEMPLATE.md`.
- **Next:** Create the approved task record and define the shared report contract.

### 2026-11-23 05:21 UTC

- **Action:** Unified the report schema and generator for `on_changed` and `on_repo`. Expanded Markdown with exact coverage, per-file metrics and diagnostics, workflow-check output, baseline comparisons, and provenance. Updated index metadata and protected latest pointers from older concurrent runs. Updated the Document Type Catalog. Added four generator tests and three anchor-check tests. Fixed runtime template-placeholder handling.
- **Result:** Format commit `c7bf066b7fc27d57764467d0f038c1a3350201f2` and anchor-check changes `82d3081671508a136317e1860db7ed943a6f957c`, `642b5b21c4b3360e0ae06b0c83ffcf348234582c` are on `gpt`. Read-back exposed a missing regex declaration and then an indentation defect. Both were corrected and the relevant source was read back. Hosted run `45116930355` confirmed the indentation defect before its correction. The generator tests and new anchor tests have not yet received a hosted result.
- **References:** `skills/asd-ste100/scripts/generate_lint_report.py`, `skills/asd-ste100/scripts/test_generate_lint_report.py`, `skills/asd-ste100/scripts/check_markdown_anchors.py`, `skills/asd-ste100/scripts/test_check_markdown_anchors.py`, `skills/asd-ste100/assets/lint-report-template.md`, `skills/asd-ste100/assets/lint-report-schema.json`, `skills/document-standards/references/document-type-catalog.md`, [report-format commit](https://github.com/dungnv2602/chatgpt/commit/c7bf066b7fc27d57764467d0f038c1a3350201f2), [placeholder declaration](https://github.com/dungnv2602/chatgpt/commit/82d3081671508a136317e1860db7ed943a6f957c), [syntax correction](https://github.com/dungnv2602/chatgpt/commit/642b5b21c4b3360e0ae06b0c83ffcf348234582c).
- **Next:** Integrate the shared generator into both lint workflows and capture all validation and per-file execution evidence.


### 2026-11-23 05:27 UTC

- **Action:** Integrated the shared generator into both lint workflows. The changed workflow now removes the invalid trailing-backslash arguments, records tooling and anchor-check results, captures raw per-file JSON and reports all check outputs. The full workflow no longer builds Markdown and parses it through a separate inline JSON converter. It captures one structured linter record per evaluated file, records validation logs, calls the same generator, compares with the previous full report, and retains the root Markdown compatibility copy. Updated report-scope documentation. Corrected check-log name mapping, made full-run publication failures fail the job, and added previous-report comparison.
- **Result:** Workflow integration commit `72bbc615fff312918c6ddb133c08d76f66ec901e`; reliability correction `705fadf5a997fd32170464c37b99f27cefa62635`; full-audit comparison `77e272c9c06042155dbe7243c868c91d88278e86`. Read-back verified both workflows, all three report README files, the generator, its tests, anchor checker and tests, template, schema, and catalog. The full-audit run `45117759354` was in progress at the single snapshot. The changed-document report is still absent because no eligible Markdown commit has triggered the repaired workflow yet.
- **References:** [workflow integration](https://github.com/dungnv2602/chatgpt/commit/72bbc615fff312918c6ddb133c08d76f66ec901e), [log mapping and publication error correction](https://github.com/dungnv2602/chatgpt/commit/705fadf5a997fd32170464c37b99f27cefa62635), [previous full report comparison](https://github.com/dungnv2602/chatgpt/commit/77e272c9c06042155dbe7243c868c91d88278e86), [full-audit run](https://github.com/dungnv2602/chatgpt/actions/runs/45117759354).
- **Next:** Publish the lint-evidence navigation link in the Workspace README, then inspect the eligible changed-document run and resulting report if it completes before the one bounded snapshot.


## 7. Current State

- Session initialization and required CI preflight are complete.
- The shared generator, schema, detailed Markdown report, and catalog now support both report scopes.
- Both lint workflows are integrated with the shared generator. The invalid changed-workflow arguments and duplicated full-workflow JSON converter are removed.
- Both workflow files and all report format assets, tests, scope documentation, and catalog entries have been read back.
- A full-document run triggered by the workflow changes was in progress at the last snapshot. No polling was performed.
- The changed-document workflow has not yet run with the new code. The `on_changed` directory still has only its README and index.
- The last recorded full audit before integration included 49 Markdown files, 455 findings, 142 hard findings, and 10 files that failed the configured threshold or execution. The report must retain those findings and thresholds.


## 8. Remaining Work

- Add the canonical lint-evidence guide to Workspace navigation. This is relevant documentation and an eligible changed-document trigger.
- Verify the newest hosted full-audit and changed-document runs once, without polling.
- Confirm that `on_changed` publishes Markdown, JSON, integrity manifest, latest pointers, and run history with the detailed evidence format.
- If hosted execution exposes further defects, correct them and read back the affected files.
- Update the task record, report register, and branch head with exact verification limits.


## 9. Next Actions

1. Update `workspace/README.md` to link the lint-evidence guide and explain the review order.
2. Read back the change and take one bounded snapshot of the triggered runs and report paths.
3. Fix any newly observed issue and read back all final repository changes.
4. Close the task only when the changed-report publication and verification gates are satisfied.


## 10. References

- [Repository](https://github.com/dungnv2602/chatgpt/tree/gpt)
- [Changed lint workflow](https://github.com/dungnv2602/chatgpt/blob/gpt/.github/workflows/ste-lint-changed.yml)
- [Full lint workflow](https://github.com/dungnv2602/chatgpt/blob/gpt/.github/workflows/ste-lint-full-docs.yml)
- [Lint evidence directory](https://github.com/dungnv2602/chatgpt/tree/gpt/lint_reports)
- [Report generator](https://github.com/dungnv2602/chatgpt/blob/gpt/skills/asd-ste100/scripts/generate_lint_report.py)
- Related task `20261123-041640`: Worker mode independence and lint-report format implementation.
- Related task `20261123043747`: Template placement and template-first authoring.

## 11. Verification

- **Check:** Session initialization and mandatory skill loading.
- **Method:** Retrieve and read each required file from branch `gpt`.
- **Result:** Passed.
- **Limitations:** Does not validate the lint workflow implementation.

- **Check:** Latest CI preflight.
- **Method:** Inspect latest runs, jobs, failed steps, and logs for applicable workflows.
- **Result:** Changed lint and full-document lint failed. Document Standards and image-conversion workflows succeeded. Current branch head had no completed check runs.
- **Limitations:** No later workflow result is claimed.

- **Check:** Current report publication paths.
- **Method:** Retrieve exact files and list `lint_reports/on_changed/` and `lint_reports/on_repo/`.
- **Result:** Changed-document report and history are absent. Repository-wide report and history exist.
- **Limitations:** Reports describe their own recorded commits and do not establish the state after this task's future changes.

## 12. Handoff Instructions

Continue on branch `gpt` only. Do not use Library or local repository execution. Keep the existing lint thresholds and checks. Read and follow Document Standards for the generator-owned report format. Make the report Markdown the detailed review surface, with complete structured JSON alongside it. Fix the proven workflow defects. Do not wait for CI or claim success without hosted evidence. Update the task record and discussion register at each meaningful checkpoint.
