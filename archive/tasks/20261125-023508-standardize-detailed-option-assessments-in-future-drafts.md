# Task: Standardize detailed option assessments in future Drafts

## Metadata

- **Template version:** 1.3
- **ID:** 20261125-023508
- **Created:** 2026-11-25 02:35 UTC
- **Updated:** 2026-11-25 02:40 UTC
- **Priority:** P1
- **Status:** Done
- **Origin:** User
- **Approval:** Explicitly approved by the user to update the Draft workflow so future Drafts include detailed assessments of all available options.
- **Governing ADR(s):** None — workflow maintenance directly requested by the user; this task does not implement the pending DRAFT-0002 proposal.
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** 20261124-113009 — Study Planning with Files and propose a file-backed Worker workflow.
- **Ledger group:** None
- **Archived:** Yes
- **Archive timestamp:** 2026-11-25T02:40:00Z

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

### 2026-11-25 02:38 UTC

- **Action:** Updated the canonical Draft template to Version 1.2; strengthened the Draft workflow, decision-governance skill, and Document Type Catalog.
- **Result:** Future Drafts now require comparable, detailed assessment of every materially viable option, consistent decision drivers, a comparative matrix when multiple options exist, explicit recommendation traceability, evidence provenance/confidence/limitations, and disclosure of assumptions and unknowns. The standard prohibits unsupported scores and estimates and allows a reasoned no-matrix exception when only one option is viable. DRAFT-0002 revision 3 remains untouched and in-review.
- **References:** `workspace/DRAFT_TEMPLATE.md`; `workspace/draft/README.md`; `skills/decision-governance/SKILL.md`; `skills/document-standards/references/document-type-catalog.md`.
- **Next:** Read back and verify all changed paths, then archive this task under the normal closeout procedure.

## 7. Current State

The Draft authoring standard is implemented on branch `gpt`. The canonical template is Version 1.2. The Draft index/workflow, decision-governance skill, and Document Type Catalog now state the same detailed assessment requirements. DRAFT-0002 revision 3 remains in-review and was not modified or approved by this work.

## 8. Remaining Work

- None. Repository read-back checks passed. Archive closeout is the only remaining operation.

## 9. Next Actions

1. Write and read back the immutable archive copy.
2. Register its exact path and UTC timestamp.
3. Delete the active record and move its board entry to Historical.

## 10. References

- `workspace/DRAFT_TEMPLATE.md`
- `workspace/draft/README.md`
- `skills/decision-governance/SKILL.md`
- `skills/document-standards/references/document-type-catalog.md`
- DRAFT-0002 revision 3: `workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md`

## 11. Verification

- **Check:** Canonical Draft template, Draft workflow/index, decision-governance skill, and Document Type Catalog.
- **Method:** Read back all four changed paths from branch `gpt`. Checked template Version 1.2; all ten shared option-assessment dimensions; comparative matrix and one-option exception; evidence register and source provenance; prohibition on unsupported scores; Draft workflow requirements; governance review quality gate; and matching catalog description.
- **Result:** All structural consistency checks passed. The four canonical files contain aligned requirements. DRAFT-0002 revision 3 remains in-review and unchanged. The task board points to this task as Current Execution. No other task or proposal was approved.
- **Limitations:** No hosted Document Standards or lint workflow was run. Read-back and structural checks do not prove every future Draft will be substantively adequate; the governance quality gate is the required review control. No merge to `main` was requested or performed.

## 12. Handoff Instructions

Task completed and archived after read-back. The canonical Draft workflow now requires detailed, evidence-qualified option assessments. DRAFT-0002 revision 3 remains in-review and was not approved or implemented. No merge to `main` was requested or performed.
