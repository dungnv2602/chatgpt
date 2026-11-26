# Discussion Register

## Current Step

- **2026-11-26 07:04 UTC:** Complete final closeout review for task [20261126-064951](tasks/20261126-064951-complete-non-image-repository-adaptation.md). The non-image path audit repaired stale references across workflows, skill instructions, report guides, workspace guides, and templates. The only remaining detected broken README links are in `.archive/adr/README.md`, where two links point to absent ADR files. The archive policy requires explicit authorization for a narrow reference-only correction. Ask before changing that archived index. Tests remain skipped.

## Open Discussions

- **Archived ADR index links:** Should the two dead file links in `.archive/adr/README.md` be replaced with links to their existing archival commits? This would be a reference-only correction and would not change ADR content.

## Reports

- **2026-11-26 07:04 UTC:** Read back all 14 changed files. All active README relative links resolve. No tests, validators, linter, or workflows were run. The root `README.md` remains absent.
