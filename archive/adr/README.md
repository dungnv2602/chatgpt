# Permanent ADR Archive

This folder stores accepted Decision Records after implementation and confirmation.

1. Archive an ADR only after all linked implementation tasks are Done.
2. Verify every Confirmation criterion before the move.
3. Preserve the ADR ID and filename.
4. Read back the archive copy after its initial write.
5. Keep the archived ADR immutable.
6. Never add ADR paths to `.github/archive-retention-index.json`.
7. Do not edit, replace, rename, move, or delete an archived ADR unless the user explicitly authorizes a narrow reference-only correction. Never change its accepted decision content.

The archive-retention workflow applies only to indexed task and report files. It must not delete this folder's contents.

## Archived ADRs

- [ADR-0001 — Establish Draft-to-ADR Governance and Repository Analysis](0001-establish-draft-to-adr-governance-and-repository-analysis.md) — Accepted; implementation complete and all Confirmation criteria passed. [Archival commit](https://github.com/dungnv2602/chatgpt/commit/e7048886eb12c41d07fa02f8c7253bbb1efebbbe).
