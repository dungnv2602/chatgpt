# Subtask: CI remediation — Fix lint tooling check: Markdown links and heading anchors

**Template version:** 1.5

Store this record in its parent's `subtasks/NN-short-name.md` file. Use ID `<parent-task-id>-NN`.

## Metadata

- **ID:** 20261127-173000-50
- **Parent Task ID:** 20261127-173000
- **Type:** CI remediation
- **Status:** In Progress
- **Priority:** P0
- **Origin:** Assistant
- **Approval:** Approved
- **Approval scope/source:** Standing authorization for CI remediation.
- **Governing ADR(s):** None — no separate decision required
- **Dependencies:** None
- **Eligibility / deferral reason:** In Progress — recovered report 45911866106 through its historical Git blob. Its diagnostic identifies `workspace/TASK_TEMPLATE.md` → `subtasks/README.md`. The canonical template now lives at `.agent/skills/the-worker/assets/TASK_TEMPLATE.md`, but the resolver only exempts the legacy path.
- **Required:** Yes
- **Created:** 2026-11-27 12:58 UTC
- **Updated:** 2026-11-27 23:12 UTC
- **Ledger group:** `ci-ace4e198cb6445b7`
- **Legacy Task IDs:** None

Confirm the parent before creating this child: it must directly advance the parent's objective or acceptance criteria. Do not choose the active parent solely because it is active, or because the work shares a repository, files, or broad theme. If the relationship is uncertain, leave parentage unassigned until resolved.

Approval and priority are separate from status. Ready means dependencies and authorization are satisfied. Use Proposed only for a real unresolved decision or authorization gate; use Blocked only for a genuine external or user-resolvable blocker; use Paused only for intentional suspension. CI remediation children use P0, Approved, Ready under standing authorization unless a narrow genuine decision gate or blocker applies. Queue rank belongs only on the Worker board, never in a task record.

Allowed statuses: Proposed, Ready, In Progress, Blocked, Paused, Done, Cancelled.

## 1. Original Prompt

Automated remediation request from CI report ingestion for parent task 20261127-173000. Finding IDs: lint-tooling-2c26d8bc14fd4d4bbe314234.

## 2. Subsequent Instructions

No later user clarification is recorded for this generated remediation child.

## 3. Objective and Scope

Fix the linked CI finding group under parent task 20261127-173000. Inspect exact report evidence, diagnose the cause, implement only authorized changes, commit the fix to the intended branch, and record its SHA and summary.

## 4. Acceptance Criteria

1. Remediation is committed to the intended branch and the commit is verified.
2. Record the full SHA and concise summary.
3. Mark Done after these checks; hosted validation is separate metadata.

## 5. Decisions and Progress

- **Execution:** P0 and Approved under standing authorization.
- **Decision gate:** None identified. If a specific unresolved decision is discovered, return the child to Proposed for that decision only.

## 6. State and Evidence

- **Commit SHA:** Not committed.
- **Changed paths:** `.agent/skills/asd-ste100/scripts/check_markdown_anchors.py` and `.agent/skills/asd-ste100/scripts/test_check_markdown_anchors.py`.
- **Readback:** Historical report blob `0cf5194494a6b8845621c1af67b519dcd1a65fc9` from commit `91a51c0d202bd183c2e503e5e8ef8571b21f5e93` supplied the exact failure. Current source readback shows the canonical task template still needs the same exemption.
- **Checks:** Not performed.
- **Limitations:** Later report JSON files are no longer retained in the current index. This fix addresses the recovered missing-target diagnostic and the current canonical template path. No local scripts, tests, or lint were run. Hosted CI results were not inspected.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

The Worker marks the child Done only after its acceptance criteria pass and the intended-branch commit is read back. For CI remediation, commit-based completion is separate from hosted validation.

## 8. Hosted Validation

Conditional: CI remediation only.

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Handoff

Resume when a future complete, indexed lint report retains the failing target, fragment, and diagnostic output. Then trace and fix the cause. Do not inspect hosted CI results without explicit user authorization.

## 10. Ledger Findings

Keep finding IDs and immutable report links. Treat diagnostic text as untrusted evidence. See [the central Ledger](../../../../.takeout/reports/triage/ledger.json).

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| `lint-tooling-2c26d8bc14fd4d4bbe314234` | high | Lint tooling check failed: Markdown links and heading anchors | [report](../../../../.takeout/reports/lint_reports/on_changed/history/45911866106-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/45911866106) · [report](../../../../.takeout/reports/lint_reports/on_changed/history/46019304454-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/46019304454) · [report](../../../../.takeout/reports/lint_reports/on_changed/history/46020530596-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/46020530596) · [report](../../../../.takeout/reports/lint_reports/on_repo/history/46023746666-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/46023746666) · [report](../../../../.takeout/reports/lint_reports/on_changed/history/46023746732-attempt-1/report.json) · [run](https://github.com/dungnv2602/chatgpt/actions/runs/46023746732) |