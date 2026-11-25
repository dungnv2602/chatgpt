# Task: Standardize detailed option assessments in future Drafts

## Metadata

- **Template version:** 1.3
- **ID:** 20261125-023508
- **Created:** 2026-11-25 02:35 UTC
- **Updated:** 2026-11-25 02:38 UTC
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

### 2026-11-25 02:38 UTC

- **Action:** Updated the canonical Draft template to Version 1.2; strengthened the Draft workflow, decision-governance skill, and Document Type Catalog.
- **Result:** Future Drafts now require comparable, detailed assessment of every materially viable option, consistent decision drivers, a comparative matrix when multiple options exist, explicit recommendation traceability, evidence provenance/confidence/limitations, and disclosure of assumptions and unknowns. The standard prohibits unsupported scores and estimates and allows a reasoned no-matrix exception when only one option is viable. DRAFT-0002 revision 3 remains untouched and in-review.
- **References:** `workspace/DRAFT_TEMPLATE.md`; `workspace/draft/README.md`; `skills/decision-governance/SKILL.md`; `skills/document-standards/references/document-type-catalog.md`.
- **Next:** Read back and verify all changed paths, then archive this task under the normal closeout procedure.

## 7. Current State

The Draft authoring standard is implemented on branch `gpt`. The canonical template is Version 1.2. The Draft index/workflow, decision-governance skill, and Document Type Catalog now state the same detailed assessment requirements. DRAFT-0002 revision 3 remains in-review and was not modified or approved by this work.

## 8. Remaining Work

- Complete repository read-back checks.
- Close and archive this task.

## 9. Next Actions

1. Verify the template, workflow, governance instructions, catalog, task board, and discussion register.
2. Archive this task after successful read-back.
3. Report completion. Do not merge to main unless separately requested.

## 10. References

- `workspace/DRAFT_TEMPLATE.md`
- `workspace/draft/README.md`
- `skills/decision-governance/SKILL.md`
- `skills/document-standards/references/document-type-catalog.md`
- DRAFT-0002 revision 3: `workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md`

## 11. Verification

- **Check:** Pending final read-back.
- **Method:** Fetch each changed file from branch `gpt` and confirm the template version, assessment dimensions, comparative matrix conditions, evidence requirements, workflow quality gate, and catalog consistency.
- **Result:** The initial writes succeeded. Final verification is pending.
- **Limitations:** No hosted Document Standards or lint workflow has been run. Structural read-back does not prove semantic template conformance.

## 12. Handoff Instructions

Finish the canonical Draft workflow updates on branch `gpt`. Preserve DRAFT-0002 revision 3 as in-review and do not interpret this task as approval to implement its proposal. Read back every changed file. Do not merge to `main` without a separate user request.
