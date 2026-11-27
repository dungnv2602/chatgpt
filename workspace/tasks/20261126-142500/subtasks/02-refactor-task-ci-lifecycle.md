# Subtask: Enforce prompt capture and refactor task/CI workflow

**Template version:** 1.4

## Metadata

- **ID:** 20261126-142500-02
- **Parent Task ID:** 20261126-142500
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit “Approve / Execute” authorization dated 2026-11-27.
- **Governing ADR(s):** Existing accepted decisions apply; no new decision gate was identified.
- **Dependencies:** None
- **Eligibility / deferral reason:** In Progress
- **Required:** Yes
- **Created:** 2026-11-27 09:22 UTC
- **Updated:** 2026-11-27
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

> Approve
>
> Execute
>
> Expand on this, fix gaps, fix floodings, fix deadlocks, tighten, close the cycle, refactor by trimming down redundancy and minimize content without losing full context, optimize workflow, update templates, update skills, etc.
>
> If you really understand, you would know you should create a task for this to track your progress.

## 2. Subsequent Instructions

- **2026-11-27 — Prompt tracking:** The user's preceding prompt requires every request with an identifiable outcome to be captured as a task; follow-ups receive their own subtasks under the genuine existing parent.
- **2026-11-27 — CI attribution:** CI remediation subtasks must be children of the genuine user task whose commit triggered the report. Never create synthetic CI parents. Leave uncertain attribution unassigned.
- **2026-11-27 — Closeout:** Commit and remote readback are completion evidence. Do not inspect hosted CI results. Delete completed task folders directly and do not create archive/retention copies.

## 3. Objective and Scope

Make every user request with an identifiable outcome traceable to a genuine parent task or a dedicated follow-up subtask. Close the prompt-to-task-to-commit-to-report-to-CI-child-to-closeout lifecycle.

- Mandatory prompt capture before answering or performing requested work.
- New objective -> parent task. Substantive follow-up/correction/extension -> its own child under the genuine parent.
- Preserve original prompts and subsequent instructions verbatim.
- Use exact `Task-ID:` commit trailers as CI attribution. Resolve child IDs through Parent Task ID.
- Create CI remediation children only under verified active user-originated parents. Missing, ambiguous, invalid, inactive, or deleted attribution stays unassigned.
- Keep Worker ownership of status, approval, dependencies, scheduling, Current Execution, board, and closeout. Ledger owns findings and attributed children only.
- Remove synthetic CI parent generation and stale Ledger board writing.
- Align task templates, skills, workspace docs, report capture, workflows, schema, generator, and regression coverage.
- Prevent flooding through stable finding/group identities, idempotent ingestion, bounded evidence, baseline suppression, and child reuse.
- Preserve stable finding IDs, occurrence counts, evidence, resolution history, accepted risk, and legacy references.

## 4. Acceptance Criteria

1. Every user request with an identifiable outcome is captured verbatim before its outcome is delivered.
2. Every substantive follow-up receives its own child record under the genuine parent; unrelated objectives do not share a parent.
3. Every task-specific implementation commit carries one exact Task-ID trailer.
4. Lint and Actions reports preserve source Task-ID provenance and resolve a parent only when its record and parent relationship are verified.
5. Unattributed reports remain visible without synthetic task or parent creation.
6. CI remediation children are P0, Approved, Ready by default and do not modify parent priority/status or the Worker board.
7. Repeated reports reuse the same finding and child; evidence is bounded; recurrence preserves prior resolution and uses latest attribution.
8. Report ingestion, task/subtask/index publication, and rollback remain idempotent and fail closed on invalid data.
9. The owning skills, templates, schemas, scripts, workflows, README, and Document Type Catalog agree.
10. All changed files are committed and remotely read back. Any unperformed tests or validation are stated accurately.

## 5. Decisions and Progress

### 2026-11-27 — implementation

- **Action:** Rewrote The Worker, Conversation Mode brief contract, CI Ledger skill, GitHub Actions task/CI contract, workspace README, and task/subtask templates. Updated Document Type Catalog to versions 2.5/1.4.
- **Result:** Prompt capture is mandatory for each request with an identifiable outcome. Follow-ups receive individual child records. The discussion brief is explicitly not a substitute for task records.
- **References:** Commits `b88183c2c916f7bdfc92452875a4562e8cac02cd`, `d6154255101dd5265647d014fe5d844d26c5337a`, `27824c83285f49522e578fa9ce4ea87403e931df`, `118f56446b911db88bffcccb34abe3bd13e8c24b`, `015c393799b2b9a99d871dd89f26ddccb0d879ad`, `ec5e5539863f36718a6ad13ed245b9c443df1efc`, `60c6c22b37608d4997a52cb819e5715f4426f56`, `f75ec2958ef664727a643062ef601400c0bcd45e`.
- **Next:** Finish code/schema/workflow/static consistency review.

### 2026-11-27 — report attribution and Ledger

- **Action:** Added lint report Task-ID capture for push commits, updated lint report schema/template, and passed the source marker through changed/full lint workflows. Updated Ledger evidence schema to 1.8.0. Reworked Ledger attribution to resolve source parent or child IDs and create CI remediation children only under verified active user parents. Removed synthetic parent rendering, archive fallback, and Ledger task-board writer.
- **Result:** Missing, malformed, ambiguous, inactive, or deleted attribution remains unassigned. The Ledger updates parent finding summaries, child records, and the child index only. It does not set Current Execution or edit the board.
- **References:** Ledger implementation `0fc8903bbb90c3ae3cb72df8dc46e337d5e68f77`; Ledger schema `65a7b6afd26eef9a794b7e5f55227e1e68af9ddd`; lint generator `d15e90f8c07381440359855ee083629f2b1b6e39`; lint report schema `637eecdb9660a1291ea1c7880400f1104e52287a`; lint report template `09465be09f830303a41e431b2a5c35bba3b00a24`; lint report documentation `3031f8f1dc0ccdd856de7120bcde2436aeec0fcc`; workflows `5b19371230d162367f855531ea9a42917ead21b2` and `96345459c986c71d95cc77fe0676985300e135a7`.
- **Next:** Complete regression and repository-wide static readback.

### 2026-11-27 — regression coverage and board

- **Action:** Replaced obsolete synthetic-parent assertions with attribution lifecycle tests. Added coverage for missing/invalid/ambiguous/unresolvable markers, parent and child IDs, repeated lint/Actions reports, tooling failure recurrence, evidence bounding, baseline suppression, malformed/missing reports, schedule events, preservation of human-managed state, resolution, and untrusted diagnostic escaping. Added lint report generator tests for push attribution and scheduled-run exclusion. Fixed Current Execution board layout.
- **Result:** Regression tests are present but were not executed. No local scripts or tests were run. No hosted CI results were inspected.
- **References:** `.takeout/reports/triage/scripts/test_ledger.py` commit `b545641923afeb43d2a398b4c9b966114008e4f3`; `.agent/skills/asd-ste100/scripts/test_generate_lint_report.py` commit `b773e1d76be004768544296bfcbb4beaf0c2e288`; board commit `35ace4b32ec7954a8e27af81afc161f6adf718cd`.
- **Next:** Perform final remote readback of every changed path, correct any static mismatch, then close this child.

## 6. State and Evidence

- **Commit SHA:** Multiple commits, listed above.
- **Changed paths:** `.agent/skills/the-worker/SKILL.md`; `.agent/skills/the-worker/references/conversation-mode.md`; `.agent/skills/ci-ledger/SKILL.md`; `.agent/skills/github-actions/SKILL.md`; `.agent/skills/document-standards/references/document-type-catalog.md`; `.agent/skills/asd-ste100/scripts/generate_lint_report.py`; `.agent/skills/asd-ste100/scripts/test_generate_lint_report.py`; `.agent/skills/asd-ste100/assets/lint-report-schema.json`; `.agent/skills/asd-ste100/assets/lint-report-template.md`; `workspace/README.md`; `workspace/TASK_TEMPLATE.md`; `workspace/SUBTASK_TEMPLATE.md`; `workspace/task_board.md`; `workspace/discussion.md`; `.github/workflows/ste-lint-changed.yml`; `.github/workflows/ste-lint-full-docs.yml`; `.takeout/reports/lint_reports/README.md`; `.takeout/reports/triage/README.md`; `.takeout/reports/triage/ledger-schema.json`; `.takeout/reports/triage/scripts/ledger.py`; `.takeout/reports/triage/scripts/test_ledger.py`; parent task and both child records.
- **Readback:** Final combined readback pending.
- **Checks:** Static inspection only. Regression cases added. Tests not executed.
- **Limitations:** No runtime ingestion or hosted workflow validation is claimed.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Awaiting final remote readback.

## 8. Hosted Validation

- **Status:** Not inspected by user policy
- **Run URL:** Not reviewed
- **Reviewed at:** Not applicable

## 9. Handoff

Finish the remote readback. If a static inconsistency is found, correct it within this subtask and read it back. Do not run local scripts/tests or inspect hosted CI results. Once acceptance criteria pass, mark this child Done. Keep the parent open for any remaining original report-ingestion criteria.

## 10. Ledger Findings

No CI finding IDs are assigned to this workflow subtask.
