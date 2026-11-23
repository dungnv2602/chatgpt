# Task: Remediate hard STE lint findings

## Metadata

- **Template version:** 1.1
- **ID:** 20261123-100738
- **Created:** 2026-11-23 10:07 UTC
- **Updated:** 2026-11-23 11:32 UTC
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

### 2026-11-23 11:32 UTC

- **Action:** Completed source-level remediation of all five baseline hard findings in `skills/drawing/references/archive-and-delivery.md`.
- **Result:** Split two long instructions. Standardized check terminology across the reference. Rephrased the adjective false positive without changing the asset-matching requirement. The file now contains no semicolons and no flagged synonym variants. Readback passed after commit `8c3aa5723b89d4ba4187799d0bd4f54258119ea5`. No local lint or tests were run. Hosted validation remains pending natural workflow execution.
- **Next:** Review the five hard findings in `skills/github-actions/SKILL.md`.

### 2026-11-23 11:24 UTC

- **Action:** Completed source-level remediation of all nine baseline hard findings in `skills/the-worker/SKILL.md`.
- **Result:** Split the CI-scope condition into explicit cases. Standardized check, delete, fix, retrieve, and change terminology. Split the two archive and triage clauses without changing task-state or retention rules. The skill now contains no semicolons and no instances of the flagged verb variants. Readback passed after commit `70a6f61e23c1935e79798be2c48d9ce99100b21c`. No local lint or tests were run. Hosted validation remains pending natural workflow execution.
- **Next:** Review the five hard findings in `skills/drawing/references/archive-and-delivery.md`.

### 2026-11-23 11:16 UTC

- **Action:** Completed source-level remediation of all 14 baseline hard findings in `skills/drawing/SKILL.md`.
- **Result:** Reworked the mandatory takeout hand-off into discrete instructions. Split long prompt-fidelity and reference rules without changing their conditions. Replaced synonym rotation with the established verb. The skill now contains no semicolons. Readback passed after commit `3d6c079b3c85539e99c5348846bc8a2bf1d2f998`. No local lint or tests were run. Hosted validation remains pending natural workflow execution.
- **Next:** Review the nine hard findings in `skills/the-worker/SKILL.md`.

### 2026-11-23 11:08 UTC

- **Action:** Completed source-level remediation of the Document Type Catalog and addressed the non-example findings in `skills/asd-ste100/SKILL.md`.
- **Result:** All 75 catalog hard findings now have source-level edits. The catalog has zero semicolons. In the STE skill, the 28-word sentence was split without changing the quoted ASD text. The non-example synonym rotation changed from "confirms" to "shows". Thirteen findings remain in deliberate examples of prohibited wording. The repository writing policy says to preserve quoted examples that intentionally show violations. Those examples remain unchanged. Readback passed after commit `23207a3fe8bd2c25a3d933b2b2da7bd6126d31be`. Hosted validation remains pending natural workflow execution.
- **Next:** Review the 14 hard findings in `skills/drawing/SKILL.md` and preserve its operational requirements and examples.

### 2026-11-23 11:00 UTC

- **Action:** Resolved the final long-sentence finding in the Document Type Catalog.
- **Result:** All 75 baseline hard findings in the catalog have source-level edits: 68 semicolon findings, three synonym-rotation findings, and four long-sentence findings. The final Skill changelog row now has fewer than 25 words. Readback confirms zero semicolons in the catalog after commit `f5496655ac37864be20d82d5c9562bd001cece51`. No linter or local tests were run. Hosted validation remains pending natural workflow execution.
- **Next:** Review the 15 hard findings in `skills/asd-ste100/SKILL.md` before the next edit batch.

### 2026-11-23 10:54 UTC

- **Action:** Completed the fifth catalog batch and reviewed the full set of catalog findings.
- **Result:** The five batches removed all 68 baseline semicolon findings and all three synonym-rotation findings. They also addressed three of four baseline long-sentence findings. The catalog readback contains no semicolons. One long-sentence fingerprint remains to reconcile against its reported source location before the catalog can be considered complete. The catalog maintenance requirements remain intact. Readback passed after commit `9bc43433477815c90a178ebde7b4fcd260d10842`.
- **Next:** Reconcile the remaining catalog long-sentence fingerprint. Then review the next highest-density file.

### 2026-11-23 10:50 UTC

- **Action:** Completed the fourth catalog batch in the legacy-example table.
- **Result:** Revised six rows and removed 17 semicolons. Preserved historical version declarations, migration rules, and retention constraints. Readback passed after commit `bf361fd04c45eb6634b09bce553251ad73758904`. The catalog now contains one semicolon.
- **Next:** Review the remaining catalog synonym-rotation findings and final semicolon.

### 2026-11-23 10:46 UTC

- **Action:** Completed the third catalog batch in the representative-record table.
- **Result:** Revised seven rows and removed 14 semicolons. Preserved each record's scope, observed facts, and handling decision. Readback passed after commit `6f9a067c3795af4b7f6d0dde5e378161e6ce33c4`. The catalog now contains 18 semicolons.
- **Next:** Review the legacy-example table and its remaining hard findings.

### 2026-11-23 10:42 UTC

- **Action:** Completed the second reviewable batch in the novel template field-contract table of `skills/document-standards/references/document-type-catalog.md`.
- **Result:** Revised all eight Version 1.1 template rows. The batch removed 22 semicolons and split two long sentences. Required, conditional, optional, and repeatable field rules remain intact. Readback passed after commit `8694f8e59c320024f153b0e73a2eca53d86dc97f`. The catalog now contains 32 semicolons.
- **Next:** Review the representative-record table and its remaining hard findings.

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

The approved task is In Progress and is the current execution. All 75 baseline hard findings in the Document Type Catalog, all 14 in `skills/drawing/SKILL.md`, all nine in `skills/the-worker/SKILL.md`, and all five in `skills/drawing/references/archive-and-delivery.md` have source-level edits. In `skills/asd-ste100/SKILL.md`, two non-example findings have source-level edits. Thirteen findings remain in deliberate examples that the repository writing policy says to preserve. Hosted validation remains pending. The 319 advisory findings remain out of scope.

## 8. Remaining Work

- Resolve all 155 approved hard findings without changing lint policy.
- Review every modified document for semantic accuracy and technical correctness.
- Verify each natural hosted full-audit result and changed-scope result.
- Confirm the final repository-wide report has zero hard findings and retains full coverage.

## 9. Next Actions

1. Review the five hard findings in `skills/github-actions/SKILL.md` against the complete source and workflow references.
2. Preserve trigger, validation, and branch-policy semantics.
3. Apply fixes on `gpt` and inspect naturally generated hosted reports.
4. Repeat until the approved hard-finding set is resolved or a policy conflict requires user direction.

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
