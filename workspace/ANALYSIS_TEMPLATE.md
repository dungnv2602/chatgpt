---
record_type: repository-analysis
template_version: "1.0"
id: "ANALYSIS-YYYYQn[-short-event-name]"
status: "draft"
review_type: "quarterly"
review_date: "YYYY-MM-DD"
branch: "gpt"
commit_sha: "40-character commit SHA"
reviewer: "Assistant"
related_adrs: []
related_tasks: []
---

# Repository Analysis — YYYY Qn

## Executive Summary

{Summarize the repository state, highest-impact findings, and major changes since the prior review.}

## Scope and Method

- **Review type:** Quarterly / Event-triggered
- **Trigger:** {Quarterly cycle or exact event}
- **Scope:** {Repository areas and dimensions reviewed}
- **Exclusions:** {Paths, systems, or questions not reviewed}
- **Method:** {Read-only inspections, source comparisons, hosted evidence, and other methods}
- **Snapshot:** Branch `gpt` at the commit recorded in the metadata

## Repository Snapshot

| Area | Observed state | Evidence |
|---|---|---|
| Architecture and boundaries | {Observation} | {Exact paths or commits} |
| Workflow integrity | {Observation} | {Exact paths or commits} |
| Quality and reliability | {Observation} | {Reports or hosted validation} |
| Data and provenance | {Observation} | {Schemas, indexes, or reports} |
| Security and trust | {Observation} | {Policies, workflows, or evidence} |
| Documentation | {Observation} | {Catalog, links, or owner files} |
| Operational cost and complexity | {Observation} | {Measured or documented evidence} |
| User workflow | {Observation} | {Task, discussion, or workflow evidence} |
| Decision debt | {Observation} | {Drafts, ADRs, tasks, and confirmation records} |

## Findings

Use one finding block for each distinct observation.

### FINDING-01 — {Short title}

- **Class:** Strength / Gap / Risk / Contradiction / Drift / Opportunity
- **Impact:** Critical / High / Medium / Low
- **Confidence:** High / Medium / Low
- **Confidence rationale:** {Why this confidence is justified}
- **Evidence class:** Repository fact / User instruction / External claim / Inference / Hypothesis
- **Observation:** {What the evidence shows}
- **Implication:** {Why this matters}
- **Sources:** {Exact paths, commit-pinned links, report IDs, or URLs}
- **Limitations:** {Missing evidence or alternative explanations}

## Cross-Cutting Patterns

{Describe relationships between findings. Do not duplicate individual CI findings.}

## Decision and Task Handoffs

| Finding | Required next step | Governing ADR or Draft | Task link | Status |
|---|---|---|---|---|
| FINDING-01 | Draft / Existing ADR task / Monitor / No action | {ID or None} | {Link or None} | Proposed |

Analysis does not authorize implementation. A new decision requires a Draft. Work covered by an accepted ADR requires an implementation task linked to that ADR.

## Limitations and Unreviewed Areas

- {Limitation, unreviewed source, unavailable validation, or uncertainty}

## Review Conclusion

- **Overall assessment:** {Evidence-based conclusion}
- **Priority themes:** {Highest-impact cross-cutting issues}
- **Recommended review trigger:** {Next quarter or a specific event}
- **Proposed Drafts:** {Links or None}
- **ADR-linked tasks:** {Links or None}

## Review History

| Date | Commit SHA | Change | Reviewer |
|---|---|---|---|
| YYYY-MM-DD | {SHA} | Initial analysis snapshot | Assistant |
