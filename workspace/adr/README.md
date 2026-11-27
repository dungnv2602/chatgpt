# Accepted Decision Records

This folder is the permanent, flat home for every accepted ADR, including completed historical decisions. Do not move completed ADRs to a separate archive directory.

## Files

- [ADR_TEMPLATE.md](../ADR_TEMPLATE.md) — canonical template for decision records.
- NNNN-title-with-dashes.md — decision records use a four-digit global sequence and lowercase dashed filenames.

## Numbering and organization

- Assign a global, permanent ADR-NNNN ID only after the user approves the source Draft.
- Use the filename NNNN-title-with-dashes.md. Keep the Markdown title unnumbered.
- Keep one flat folder. Use optional metadata tags to group decisions. Do not create category folders or local numbering.
- Never reuse an ADR ID.

## Status and implementation

The decision status and implementation status are separate.

Decision statuses:

- promotion-pending — temporary provisional state during ADR promotion. It reserves the ADR ID but is not an accepted decision.
- accepted — the approved decision is active or remains authoritative for its scope.
- superseded — a later ADR replaces the decision. Link the replacement.
- deprecated — the decision is no longer recommended, with no direct replacement.
- reversed — the user explicitly reversed the decision.

Implementation statuses:

- not-started
- in-progress
- complete
- not-required
- superseded

Create the provisional ADR with promotion-pending. Do not list it under Current Accepted ADRs. Do not use it to govern an implementation task.

Change the status to accepted only after the source-Draft completeness checklist and provisional ADR read-back pass. Read back the accepted record before deleting the source Draft. If deletion fails, keep the source Draft temporarily under Promotion Cleanup Pending and retry only the deletion step.

Only accepted ADRs may govern implementation tasks. A rejected proposal remains a Draft. Do not create an ADR for a rejected or withdrawn proposal.

## Implementation rules

1. Every new implementation task must link one or more accepted ADRs.
2. Task approval remains separate from decision approval.
3. Each task must state which ADR requirements it implements.
4. An accepted ADR does not authorize unrelated scope.
5. If new work is not covered by an accepted ADR, create a Draft and obtain approval before implementation.
6. Update the ADR's task links and implementation status when task state changes.
7. Record evidence for each Confirmation criterion in the ADR or linked task records.

## Immutability and permanent retention

The accepted decision is immutable. Do not rewrite its rationale or chosen outcome. Create a new ADR that supersedes it when the decision changes.

Only update lifecycle metadata, task links, review history, and implementation confirmation. Record why and when each lifecycle change occurred.

Keep all ADR files permanently in this folder after acceptance and confirmation. Mark completed records with implementation status `complete` and retain their original IDs and filenames. Do not add ADRs to `.github/archive-retention-index.json`. The 90-day retention workflow applies only to task and report archives under `workspace/archive/`.

## Current Accepted ADRs

- [ADR-0004 — Task Folders, Subtasks, and Reliable CI Ledger Lifecycle](0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md) — Accepted Option 3. Implementation remains in progress under the linked P0 task.
- [ADR-0003 — Canonical GitHub Actions Diagnostic Report Artifact Layout](0003-canonical-github-actions-diagnostic-report-artifact-layout.md) — Accepted Option 3. Implementation remains outstanding under P0 task 20261126-090154.

## Completed Historical ADRs

- [ADR-0002 — Retire Source Drafts After Verified ADR Promotion](0002-retire-source-drafts-after-verified-adr-promotion.md) — Accepted; implementation complete and all Confirmation criteria passed. [Original archival commit](https://github.com/dungnv2602/chatgpt/commit/89d4d0765e8065080c4e350f3e4e2a8b1cfd59c6).
- [ADR-0001 — Establish Draft-to-ADR Governance and Repository Analysis](0001-establish-draft-to-adr-governance-and-repository-analysis.md) — Accepted; implementation complete and all Confirmation criteria passed. ADR-0002 supersedes only its source-Draft preservation rule. [Original archival commit](https://github.com/dungnv2602/chatgpt/commit/e7048886eb12c41d07fa02f8c7253bbb1efebbbe).
