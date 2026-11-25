# Task: Standardize detailed option assessments in future Drafts

## Metadata

- **Template version:** 1.3
- **ID:** 20261125-023508
- **Created:** 2026-11-25 02:35 UTC
- **Updated:** 2026-11-25 02:35 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Explicitly approved by the user to update the Draft workflow so future Drafts include detailed assessments of all available options.
- **Governing ADR(s):** None — workflow maintenance directly requested by the user; this task does not implement the pending DRAFT-0002 proposal.
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** 20261124-113009 — Study Planning with Files and propose a file-backed Worker workflow.
- **Ledger group:** None
- **Archived:** No

## 1. Original Request

"I expect these in the future drafts, so update your draft workflow."

## 2. Subsequent Instructions

- 2026-11-25: Treat detailed, evidence-based assessment of every viable option as a permanent requirement for future Drafts, based on the user's request for detailed assessments of all available options in DRAFT-0002.

## 3. Objective

Update the canonical Draft template, Draft workflow, decision-governance instructions, and Document Type Catalog so every future decision Draft assesses all viable options in a consistent, evidence-qualified, decision-useful manner.

## 4. Requirements

- Require substantive strengths, weaknesses, neutral trade-offs, fit, cost, dependencies, risks, and limitations for every viable option.
- Require explicit decision criteria and a comparative matrix when comparing multiple viable options.
- Require evidence provenance and clear separation of repository facts, external claims, inferences, and hypotheses.
- Require explicit disclosure of evidence quality, source versions/dates, sample and host limits, benchmark transferability, and unresolved uncertainty when applicable.
- Require a reasoned recommendation tied to the decision criteria and comparative evidence.
- Keep no-change/current-state options in scope when viable.
- Avoid artificial scoring, unsupported quantitative rankings, and filler where evidence is unavailable.
- Update canonical owner instructions and catalog metadata consistently.
- Do not alter DRAFT-0002's pending approval state or implement its proposed Option 3.

## 5. Decisions

- **Approved:** Update the Draft workflow and canonical assets to require detailed option assessments in future Drafts.
- **Not approved:** The user's request does not approve DRAFT-0002 revision 3 or its proposed implementation.

## 6. Progress Log

### 2026-11-25 02:35 UTC

- **Action:** Inspected the canonical Draft template, Draft index/workflow, decision-governance skill, Document Standards skill, catalog entry, task board, and discussion register.
- **Result:** The current template asks for Good/Neutral/Bad but does not require consistent evaluation dimensions, comparative criteria, evidence limitations, or recommendation traceability. The governance skill similarly requires comparison but lacks a detailed assessment checklist.
- **References:** `workspace/DRAFT_TEMPLATE.md`; `workspace/draft/README.md`; `skills/decision-governance/SKILL.md`; `skills/document-standards/references/document-type-catalog.md`.
- **Next:** Update the canonical template, workflow, governance instructions, and catalog, then read back and structurally verify every changed path.

## 7. Current State

The scope is authorized. Canonical source files have been inspected. No files have yet been changed.

## 8. Remaining Work

- Update the Draft template and increment its template version.
- Update the Draft workflow and decision-governance review procedure.
- Update the Document Type Catalog.
- Read back all changed paths and verify consistency.
- Update the task board and discussion register.

## 9. Next Actions

1. Update canonical Draft authoring and review requirements.
2. Read back and verify the changes.
3. Report completion without merging to main unless separately requested.

## 10. References

- `workspace/DRAFT_TEMPLATE.md`
- `workspace/draft/README.md`
- `skills/decision-governance/SKILL.md`
- `skills/document-standards/references/document-type-catalog.md`
- DRAFT-0002 revision 3: `workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md`

## 11. Verification

- **Check:** Pending.
- **Method:** Read back all changed paths and inspect the detailed-assessment requirements.
- **Result:** Not performed.
- **Limitations:** No hosted validation has been run.

## 12. Handoff Instructions

Finish the canonical Draft workflow updates on branch `gpt`. Preserve DRAFT-0002 revision 3 as in-review and do not interpret this task as approval to implement its proposal. Read back every changed file. Do not merge to `main` without a separate user request.
