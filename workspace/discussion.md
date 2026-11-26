# Discussion Register

## Current Step

- **2026-11-26:** Resolve P0 task [20261126-124129](tasks/20261126-124129-fix-lint-tooling-check-markdown-links-and-heading-anchors.md). Correct the active Draft's archived ADR link, make the changed-document workflow run the link/anchor check on every push. Use changed Markdown sources for incremental runs and all active sources for full audits. Add regression coverage and verify the hosted check. Preserve separate STE lint findings.

## Open Discussions

- **2026-11-26 11:55 UTC:** Lint report [45814417490](https://github.com/dungnv2602/chatgpt/actions/runs/45814417490) for commit `488bb1e` failed the Markdown links/heading anchors tooling check because DRAFT-0002 referenced an unavailable archived ADR path. Task 20261126-124129 owns the link-check remediation. The later full audit [45823182226](https://github.com/dungnv2602/chatgpt/actions/runs/45823182226) also exposed links from the then-active archived ADR path to an unavailable task path. The ADR is now in the immutable `.archive/adr/` area and is excluded as a source.
- **2026-11-26 11:45 UTC:** ADR-0003 is accepted. DRAFT-0004 was deleted after accepted-record read-back. Its Option 3 implementation is assigned to P0 task 20261126-090154. See [ADR-0003](adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md).
- **2026-11-26:** Hosted validation for task `20261126-101512-01` remains pending. The latest diagnostics run [45832275704](https://github.com/dungnv2602/chatgpt/actions/runs/45832275704) passed reporter regression tests, but task closeout must record its exact evidence and retain the finding until the archive lifecycle runs.

## Reports

- **2026-11-26:** Closed catalog P0 task [20261126-124305](../.archive/task/20261126-124305-review-validation-or-test-failures-in-validate-document-standard.md). Archive commit [04043bc](https://github.com/dungnv2602/chatgpt/commit/04043bc4ae35b66b433c8c3f04b69995ce08b9b7). Hosted validation [45832275652](https://github.com/dungnv2602/chatgpt/actions/runs/45832275652) passed.
