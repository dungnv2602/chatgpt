# Task: Enforce conversation integrity before image relocation

## Metadata

- **Template version:** 1.2
- **ID:** 20261123-162826
- **Created:** 2026-11-23 16:28 UTC
- **Updated:** 2026-11-23 16:28 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** None
- **Ledger group:** None
- **Archived:** No

## 1. Original Request

Create a task for this and proceed to work on it: Identify the problems in images/takeout, 18 images there, no conversation and relocation happened. Fix the workflow.

## 2. Subsequent Instructions

- **2026-11-23:** The user directed that the task be created and execution begin immediately. The repository is dungnv2602/chatgpt, branch gpt, and is the sole source of truth.

## 3. Objective

Investigate the 18 images committed under images/takeout/, determine which have defensible source and conversation provenance, identify why the intake and relocation process can proceed without a checkable conversation archive, and correct the workflow so it cannot relocate assets before required records and mappings are present and verified.

## 4. Requirements

1. Inventory all 18 top-level image files by exact path, Git blob SHA, and size. Preserve their bytes.
2. Trace the import and processing history. Distinguish upload into the repository intake from final workflow relocation into destination folders.
3. Reconcile each image against attempt/output records and any conversation-integrity/session archive. Do not infer mappings from filenames, chronology, memory, or visual similarity.
4. Identify unclassified images and missing conversation records. Do not invent visual descriptions, approvals, prompt IDs, native IDs, or conversation contents.
5. Correct the hand-off schema, processor, workflow, and documentation so required conversation/source records and output mappings are checked before any original or WebP is relocated.
6. Preserve a safe Draft/quarantine path for incomplete or ambiguous items. Partial conversation archives must state their gaps and must not claim verbatim completeness.
7. Add regression coverage for missing, malformed, partial, and valid source records; verify that failure leaves intake originals and the active hand-off intact.
8. Recover or create only records supported by retained evidence. Distinguish reconstructed/editorial summaries from verbatim conversation.
9. Read back every modified path and check the resulting branch head. Do not run repository scripts/tests locally, manually dispatch Actions, or poll CI. Allow GitHub-hosted validation to occur naturally.
10. Keep all work on gpt. Do not modify main or unrelated workflows.

## 5. Decisions

- Keep the current batch in Draft until every item passes the updated provenance requirements.
- Keep the seven entries already marked unclassified unresolved until their image content and source can be reliably inspected.
- Attempt records alone do not establish that a session conversation has been archived. Check the session-level integrity record.
- Do not delete, rename, or move existing image bytes during the initial audit.
- A conversation-integrity record may be Partial when source material is unavailable, but it must identify missing material and label editorial summaries honestly.
- When evidence is unavailable, preserve the images in intake and report the blocker instead of weakening the gate.

## 6. Progress Log

### 2026-11-23 16:28 UTC

- **Action:** Traced the processor control flow and reviewed all eleven referenced drawing attempt records.
- **Result:** The processor exits without processing when HANDOFF status is Draft or empty. For Ready batches it validates listed source files and basic hand-off fields, but it has no conversation_record field or conversation-integrity check. mapping_evidence is optional free text and is not verified against the attempt record. An attempt number alone causes a manifest row to be labelled Corroborated, even without validating the actual asset ID and generation ID in the attempt note. WebPs are fully staged before originals move, but manifest reconciliation occurs after the move and relies on rollback if it fails. All eleven mapped hand-off entries have matching asset IDs and generation IDs in their referenced attempt files; the two relevant day folders still lack conversation-integrity files. Seven items have no attempt mapping and cannot be visually checked with the current text-only file reader.
- **References:** skills/the-worker/scripts/process_takeout.py (main hand-off gate and processing transaction); skills/the-worker/scripts/test_process_takeout_unittest.py; drawings/2026-11-20/attempt-04.md through attempt-06.md; drawings/2026-11-21/attempt-09.md through attempt-16.md; drawings/2026-11-20/README.md; drawings/2026-11-21/README.md.
- **Next:** Implement a mandatory archived conversation-record check and validate drawing asset/generation identity before conversion staging or relocation. Add regression coverage and update the hand-off documentation.


### 2026-11-23 16:28 UTC

- **Action:** Inspected the takeout tree, hand-off, related session indexes and attempt records, Worker provenance rules, conversation-integrity template, processor, and WebP workflow. Traced the commits that introduced the 18 images and the current hand-off.
- **Result:** All 18 PNGs were added to images/takeout/ together in commit 1192a4a53640b6188f3500abda75b1c9d5fe004d (“add images”). The current HANDOFF.yml was reconciled in commit 516d6311412e759829f492717053e3abf1ae9821 and remains status: draft. Eleven items name Samantha drawing attempts; seven are explicitly unclassified and routed to images/unclassified, with a note that their pixels were not inspected. The 20 and 21 November drawing folders contain session/attempt records but no conversation-integrity.md. The hand-off contract and processor do not require a conversation-integrity record before relocation. All 18 images remain in intake. The image blobs cannot be rendered by the available UTF-8-only GitHub file reader, so no visual classification is claimed.
- **References:** images/takeout/HANDOFF.yml; images/takeout/README.md; skills/the-worker/scripts/process_takeout.py; skills/the-worker/scripts/test_process_takeout_unittest.py; .github/workflows/convert-images-to-webp.yml; skills/the-worker/references/image-provenance-and-webp.md; skills/the-worker/references/archive-records-and-image-prompts.md; skills/the-worker/assets/conversation-integrity-template.md; drawings/2026-11-20/; drawings/2026-11-21/.
- **Next:** Inspect the exact validation and relocation sequence, reconcile all 18 entries against retained records, then implement the pre-relocation provenance gate and regression tests.

## 7. Current State

The intake contains exactly 18 PNG files, all committed in one import commit. The active hand-off contains 18 corresponding items and remains Draft. Eleven items have attempt-level mappings; seven are labelled unclassified. The 20 and 21 November drawing session records do not have a session-level conversation-integrity file. The processor does not require a conversation-integrity path as part of the hand-off contract. The 18 images are still under images/takeout/; there is no evidence that the takeout processor has finally relocated this batch.

The first inspection did not establish the visual content of the seven unclassified images because the current GitHub connector cannot return image binary data to the text reader. Their source and destination remain unresolved.

## 8. Remaining Work

- Inspect processor validation, staging, rollback, relocation, and hand-off-clearing code.
- Check all eleven mapped attempts against their session records and identify missing provenance without inventing dialogue.
- Determine whether retained context supports partial conversation-integrity records for either session; record gaps explicitly.
- Define and implement a source-record contract that blocks relocation when provenance is absent or invalid.
- Add and update regression tests and operational documentation.
- Keep unsupported items in Draft/quarantine.
- Read back changed paths and leave hosted validation to a natural run.

## 9. Next Actions

1. Review the exact processor code around hand-off parsing, validation, drawing-record reconciliation, staging, relocation, rollback, and hand-off reset.
2. Compare each mapped item against its attempt record and session brief; document missing source fields.
3. Implement the mandatory source-record check and positive/negative test cases.
4. Update the takeout procedure and Worker provenance rules.
5. Reconcile the 18-item batch without setting it to Ready until its evidence is complete.

## 10. References

- images/takeout/README.md and images/takeout/HANDOFF.yml
- skills/the-worker/references/image-provenance-and-webp.md
- skills/the-worker/references/archive-records-and-image-prompts.md
- skills/the-worker/assets/conversation-integrity-template.md
- skills/the-worker/scripts/process_takeout.py and test_process_takeout_unittest.py
- .github/workflows/convert-images-to-webp.yml
- Import commit: https://github.com/dungnv2602/chatgpt/commit/1192a4a53640b6188f3500abda75b1c9d5fe004d
- Hand-off reconciliation commit: https://github.com/dungnv2602/chatgpt/commit/516d6311412e759829f492717053e3abf1ae9821

## 11. Verification

- **Check:** Takeout inventory and provenance state.
- **Method:** Inspected the branch tree, hand-off YAML, session indexes and attempt records, source commit history, archive procedures, processor, and workflow.
- **Result:** Exactly 18 intake PNGs are present. The hand-off has 18 items and is Draft. Eleven are associated with attempts; seven are unclassified. The two relevant daily drawing folders have no conversation-integrity file. The processor does not enforce a conversation-integrity record. The 18 images remain in intake.
- **Limitations:** Image pixels were not available through the UTF-8-only GitHub content reader. No visual classification or source conversation has been inferred. No scripts/tests were run and no Actions workflows were dispatched or polled.

## 12. Handoff Instructions

Continue on branch gpt. Do not set the hand-off to Ready or process the batch before confirming the complete validation and rollback sequence and implementing a hard pre-relocation provenance gate. Create only evidence-supported partial conversation-integrity records and label all gaps. Keep the seven unclassified images in Draft until source and destination are established. Preserve all 18 source bytes. Do not poll or manually dispatch GitHub Actions.

## 13. Ledger Findings

_The CI Ledger maintains this section for event-driven finding links. No Ledger finding is associated with this user task._

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
