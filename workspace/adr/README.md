# Accepted Decision Records

Navigation and accepted-decision index. The Worker and [Decision Governance](../../.agent/skills/the-worker/references/decision-governance.md) own ADR approval, promotion, implementation linkage, lifecycle changes, and Confirmation.

## Canonical format

- [ADR_TEMPLATE.md](../../.agent/skills/the-worker/assets/ADR_TEMPLATE.md) — canonical record format.
- Use the global four-digit sequence and flat folder. Never reuse an ID.

## Accepted ADRs

- [ADR-0008 — CI Validation, Error Tasks, and Automatic Feedback Loop](0008-ci-validation-error-tasks-and-automatic-feedback-loop.md) — accepted; implementation not started. Supersedes ADR-0003 and ADR-0007, and scoped CI/report lifecycle clauses in ADR-0004.
- [ADR-0007 — Unified index as the sole latest lint report locator](0007-unified-index-as-latest-lint-report-locator.md) — superseded by ADR-0008; retained as permanent decision history.
- [ADR-0006 — Automated Structural Validation for Canonical Ownership and Drift](0006-automated-structural-validation-for-canonical-ownership-and-drift.md) — accepted, implementation complete.
- [ADR-0005 — Lean Session Start and Conversation Mode](0005-lean-session-start-and-conversation-mode.md) — accepted, implementation complete.
- [ADR-0004 — Task Folders, Subtasks, and Reliable CI Ledger Lifecycle](0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md) — accepted, partially superseded by ADR-0008 for CI completion and findings/report lifecycle only. General task-folder, parent/child, governance, and deletion rules remain.
- [ADR-0003 — Canonical GitHub Actions Diagnostic Report Artifact Layout](0003-canonical-github-actions-diagnostic-report-artifact-layout.md) — superseded by ADR-0008 after the approved report-system migration is completed; retained as permanent decision history.

## Completed historical decisions

- [ADR-0002 — Retire Source Drafts After Verified ADR Promotion](0002-retire-source-drafts-after-verified-adr-promotion.md) — accepted and implementation complete.
- [ADR-0001 — Establish Draft-to-ADR Governance and Repository Analysis](0001-establish-draft-to-adr-governance-and-repository-analysis.md) — accepted and implementation complete.

## Ownership and retention

- Only accepted ADRs govern implementation.
- Keep accepted ADRs in this flat directory. Do not create an ADR archive.
- Follow Decision Governance for status changes, task linkage, Confirmation evidence and supersession.
- Do not rewrite an accepted decision. Propose a new decision when its outcome changes.
