# Task: Remediate hard STE lint findings

## Metadata

- **Template version:** 1.1
- **ID:** 20261123-100738
- **Created:** 2026-11-23 10:07 UTC
- **Updated:** 2026-11-23 10:34 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** Assistant
- **Approval:** Approved
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** 20261123-054904 — Build GitHub Actions diagnostic reports and remove the CI preflight gate
- **Archived:** No

## 1. Original Request

Existing lint findings: approve.

## 2. Subsequent Instructions

- **2026-11-23:** User confirmed the working branch policy: "Keep delayed capture on gpt. Your branch is always the most up-to-date, main is just for preservation."
- **2026-11-23:** User approved a separate task to remediate the existing hard lint findings: "Existing lint findings: approve."
- **2026-11-23:** Keep all implementation and remediation commits on `gpt`. Do not modify `main`.

## 3. Objective

Resolve the existing hard STE lint findings without weakening lint rules, thresholds, baselines, or evaluation coverage. Preserve the meaning and technical accuracy of every edited document.

## 4. Requirements

1. Use the latest complete repository-wide lint report as the canonical starting point: run `45128445227`, generated from commit `cba473b33ce3dd108aa99526951432190cf1c828`.
2. The canonical report records 155 hard findings and 319 advisory findings across 49 evaluated files. The hard-finding set uses 155 stable fingerprints.
3. The latest changed-scope full-audit fallback, run `45152181405`, records the same 155 hard-finding fingerprints. Do not count the two scopes as 310 distinct findings.
4. Remediate the 155 hard findings only. The 319 advisory findings remain outside scope unless the user approves a separate task.
5. Read the complete source document and relevant context before each edit. Preserve facts, conditions, exceptions, modality, terminology, and technical meaning.
6. Follow `skills/asd-ste100/references/repository-writing-policy.md`. Use Strict mode for instructions and STE-flavored mode for reference prose.
7. Do not suppress findings, change rule definitions, weaken thresholds, raise baselines, or reduce lint scope to obtain a pass.
8. Prioritize high-density files and repeated rule patterns. The current report shows 75 hard findings in the Document Type Catalog and 82 semicolon findings across the report. Confirm every fix against the source meaning.
9. Keep user-authored task records and `workspace/discussion.md` unchanged. Do not rewrite historical or user-origin content as a lint cleanup.
10. Use stable finding fingerprints to track progress and avoid duplicate work across the two report scopes.
11. Group edits into reviewable batches. Keep each batch on branch `gpt`.
12. Let GitHub-hosted Actions validate changes. Do not run the linter, repository scripts, or tests locally. Do not poll or wait for workflows.
13. Review naturally available full-audit and changed-scope reports after each eligible push. Confirm that resolved fingerprints disappear and no new hard findings appear.
14. Complete the task only when the approved hard-finding set is resolved, the repository-wide hard-finding count is zero, and the final hosted report confirms the unchanged lint policy and full coverage.

## 5. Decisions

- **Approved:** Remediate hard findings from the current canonical report.
- **Out of scope:** Advisory findings, unrelated CI failures, workflow redesign, and optional style changes not needed to resolve a hard finding.
- **Preserve:** Lint rules, thresholds, per-file baselines, and repository-wide coverage.
- **Branch policy:** `gpt` is the active working branch. `main` is preservation-only and must not be modified.
- **Validation:** Use natural GitHub Actions runs. Do not manually dispatch or poll workflows.

## 6. Progress Log

### 2026-11-23 10:34 UTC

- **Action:** Completed the first reviewable batch in `skills/document-standards/references/document-type-catalog.md`.
- **Result:** Rewrote 15 catalog rows without changing their classifications, canonical paths, conditions, or handling decisions. The batch resolved 14 semicolon findings, one long-sentence finding, and one synonym-rotation finding. The source was read back after commit `62afd3b27a3a64eed75990ff5800de3568f767ec`. The catalog now contains 54 semicolons, down from 68. No linter or local tests were run.
- **Next:** Review the remaining catalog hard fingerprints and prepare the next coherent batch.

### 2026-11-23 10:28 UTC

- **Action:** Activated the approved lint-remediation task after hosted validation of the cancellation-safe diagnostic fix.
- **Result:** Task 20261123-100738 is now the current execution. The diagnostic task remains In Progress for its independent pending captures and scheduled retention observation. No lint source edits have started.
- **Next:** Review the canonical hard-finding fingerprints and the complete highest-density source document before the first remediation batch.

### 2026-11-23 10:07 UTC

- **Action:** Inspected the current repository-wide and changed-scope lint indexes, latest Markdown report, and structured JSON.
- **Result:** Repository-wide run `45128445227` records 155 hard findings and 319 advisory findings across 49 files. Changed-scope full-audit fallback run `45152181405` records the same counts. A fingerprint comparison confirms that both scopes contain the same 155 hard findings. The 155 hard findings are concentrated in 21 files. The Document Type Catalog contains 75. The rule totals include 82 semicolon findings, 33 synonym-rotation findings, and 28 long-sentence findings.
- **References:** `reports/lint_reports/on_repo/latest-lint-report.md`, `reports/lint_reports/on_repo/latest-lint-report.json`, `reports/lint_reports/on_repo/index.json`, `reports/lint_reports/on_changed/index.json`, and `reports/lint_reports/on_changed/latest-lint-report.json`. Runs [45128445227](https://github.com/dungnv2602/chatgpt/actions/runs/45128445227) and [45152181405](https://github.com/dungnv2602/chatgpt/actions/runs/45152181405).
- **Next:** Start with the highest-density source files. Review each full document and its hard findings before editing.

## 7. Current State

The approved task is In Progress and is the current execution. The canonical hard-finding set contains 155 unique fingerprints. Both report scopes agree. The first catalog batch is complete. Remaining catalog findings require review. The 319 advisory findings remain out of scope.

## 8. Remaining Work

- Resolve all 155 approved hard findings without changing lint policy.
- Review every modified document for semantic accuracy and technical correctness.
- Verify each natural hosted full-audit result and changed-scope result.
- Confirm the final repository-wide report has zero hard findings and retains full coverage.

## 9. Next Actions

1. Review the remaining hard-finding fingerprints in the Document Type Catalog and plan the next coherent batch.
2. Read complete source context for each subsequent target document.
3. Apply fixes on `gpt` and inspect naturally generated hosted reports.
4. Repeat until the approved hard-finding set is resolved.

## 10. References

- `skills/asd-ste100/references/repository-writing-policy.md`
- `skills/asd-ste100/SKILL.md`
- `reports/lint_reports/README.md`
- `reports/lint_reports/on_repo/README.md`
- `reports/lint_reports/on_changed/README.md`
- `reports/lint_reports/on_repo/latest-lint-report.md`
- `reports/lint_reports/on_repo/latest-lint-report.json`
- `reports/lint_reports/on_changed/latest-lint-report.json`
- Related task: `20261123-054904`

## 11. Verification

- **Check:** Compare the hard-finding fingerprint sets in the latest repository-wide and changed-scope reports.
- **Method:** Read both structured JSON reports from branch `gpt` and compare the 155 hard-finding fingerprints.
- **Result:** Passed. Both sets contain 155 fingerprints and are identical.
- **Limitations:** This confirms the starting finding set. It does not validate any remediation because no edits have started.

## 12. Handoff Instructions

The user approved remediation of the existing hard lint findings. Start from the 155 unique hard fingerprints in repository-wide run `45128445227`. The changed-scope full-audit fallback run `45152181405` contains the identical set. Remediate only these hard findings. Keep advisory findings out of scope. Preserve lint rules, thresholds, baselines, and coverage. Read full source context before editing. Do not rewrite user task records or the discussion register. Commit only to `gpt`. Use natural hosted validation and never poll or manually dispatch workflows. Do not modify `main`.
