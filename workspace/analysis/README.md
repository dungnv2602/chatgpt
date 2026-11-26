# Repository Analysis

This folder stores evidence-based reviews of repository health and decision coverage.

## Files

- [`ANALYSIS_TEMPLATE.md`](../ANALYSIS_TEMPLATE.md) — canonical analysis template.
- `ANALYSIS-YYYYQn.md` — quarterly review.
- `ANALYSIS-YYYYQn-short-event-name.md` — event-triggered review.

## Purpose and boundaries

Analysis describes the repository at a fixed branch commit. It identifies strengths, gaps, risks, contradictions, drift, and opportunities.

Analysis is not an implementation plan or issue backlog.

- Analysis records the observed state and evidence.
- Drafts propose decisions.
- ADRs record user-approved decisions.
- Tasks implement accepted decisions.
- The CI Ledger owns active lint and GitHub Actions findings.

Cite Ledger findings and diagnostic reports. Do not copy their issue records into analysis.

## Review cadence

Perform one manual repository-wide review each quarter.

Perform an event-triggered review after a major architecture or workflow change, significant incident, repeated systemic failure, or major dependency or platform change. Also review after a failed ADR Confirmation criterion or a direct user request.

Begin with manual reviews. Do not create a scheduled workflow. Review the cadence after two quarterly cycles.

## Record rules

1. Use `ANALYSIS-YYYYQn.md` for quarterly reviews.
2. Use `ANALYSIS-YYYYQn-short-event-name.md` for event reviews.
3. Record the exact branch and commit SHA.
4. State the scope, exclusions, methods, and limitations.
5. Link exact source paths, reports, commits, and ADRs.
6. Separate repository facts from external claims, inferences, and hypotheses.
7. Assign a confidence level and justify it.
8. Do not make code changes from analysis records.
9. Create a Draft when a finding needs a new decision.
10. Create or update a task when an accepted ADR already covers the work.

Keep completed analysis records in this folder as immutable snapshots. Do not create `.archive/analysis/` in the first release.
