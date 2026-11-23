# Task: Enforce conversation integrity before image relocation

## Metadata

- **Template version:** 1.2
- **ID:** 20261123-162826
- **Created:** 2026-11-23 16:28 UTC
- **Updated:** 2026-11-23 16:59 UTC
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

## 6A. Implementation Progress

### 2026-11-23 16:59 UTC

- **Action:** Implemented the fail-closed conversation provenance gate, the post-publication verifier checks, the Partial conversation-record template, and operational documentation. Created evidence-limited records for the two mapped drawing dates and added the corresponding record references to the eleven mapped hand-off entries.
- **Result:** The processor now requires a dated conversation-integrity record for every Ready hand-off item, checks its coverage and gap disclosures, and matches the exact source filename, attempt, source/platform Asset ID, and Generation / Output ID before staging. For drawing outputs, it also verifies the identifier pair against the referenced attempt record. The published-manifest verifier repeats those checks against the remote branch. The repository naming `asset_id` remains distinct from `source_asset_id`, so the platform Asset ID cannot alter stored filenames. Seven unclassified images remain unmapped and untouched. The active hand-off remains Draft.
- **Regression coverage:** Added seven tests for missing records, malformed Partial records, incorrect source mappings, attempt-identity mismatches, and missing or inconsistent published conversation records. Existing tests were updated to create synthetic Partial fixtures.
- **Limitations:** The two new archives are Partial summaries, not complete transcripts. Exact original conversation turns and tool payloads are unavailable in retained repository evidence. The seven unclassified image binaries have not been visually inspected. No local scripts or tests were run, and no GitHub Actions workflow was dispatched or polled.
- **Next:** Commit the implementation and read back every changed file. Keep the hand-off Draft until the seven unmapped files have defensible source records and an approved destination.

## 7. Current State

The eighteen PNGs were imported into `images/takeout/` by commit `1192a4a53640b6188f3500abda75b1c9d5fe004d`. The evidence does **not** show final processor relocation: the current `HANDOFF.yml` remains `status: draft`, and all eighteen image files remain in the intake folder.

Eleven items have exact mappings to Samantha drawing attempts 04–06 (20 November) and 09–16 (21 November). Their attempt notes contain matching source Asset IDs and Generation IDs. Two new Partial conversation-integrity records summarise only what is supported by the retained session briefs and attempt notes. They explicitly record unavailable transcript material and include exact source mapping tables for those eleven items.

Seven items remain unclassified. Their pixels have not been visually inspected, and no reliable source/attempt association is present. No mapping or conversation content has been invented for them.

The hand-off now contains `source_asset_id` and `conversation_record` for the eleven mapped items only. It remains Draft. The processor and publication verifier changes are prepared but are not yet committed to the branch. The seven unmapped items and all eighteen original image bytes remain untouched.

## 8. Remaining Work

- Commit the processor, publication verifier, regression tests, partial conversation records, template, hand-off schema, documentation, and workflow triggers as one coherent change set on `gpt`.
- Read back every modified path and verify the resulting branch head.
- Resolve the seven unclassified images by inspecting their actual pixels and comparing them with retained generation/session evidence. Do not guess based on filenames or chronology.
- Keep the hand-off Draft until every item has valid source mapping and an approved destination/quarantine disposition.
- Allow the existing hosted workflow to run naturally after the commit; do not manually dispatch or poll Actions.
- Review the naturally returned hosted test result when it becomes available through normal workflow reporting. Do not claim tests pass before that evidence exists.

## 9. Next Actions

1. Commit the code, tests, publication verifier, two Partial archives, eleven mapped hand-off entries, workflow triggers, and documentation updates.
2. Read back every changed file and confirm the branch head on `gpt`.
3. Inspect the seven remaining image binaries using a reliable image-capable path and reconcile them against retained source evidence. Keep unresolved files in Draft.
4. Review natural hosted validation only when it is recorded by the normal workflow. Do not run or poll Actions manually.

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

## 14. Intake Inventory — 2026-11-23

The following inventory records the exact image blob SHA and byte size from the `gpt` tree at the start of this task. The classification is based on the hand-off and attempt-note evidence; it does not imply visual inspection of the image.

| Source file | Git blob SHA | Bytes | Evidence classification |
|---|---|---:|---|
| `file_00000000065c8207a6cd810d3ed13633.png` | `d18a6e0c6bc03043c389452169c35afb15a8893d` | 2,188,334 | Attempt 16 — mapped |
| `file_00000000081c82078133f71b2fa24c59.png` | `00237b46def92c1ffa9a857cf51abcaef085844d` | 2,275,263 | Attempt 13 — mapped |
| `file_000000001b508211a06139988c2a68df.png` | `811ebb8302571576abc1cedae155f993b0f6fec9` | 2,311,759 | Attempt 11 — mapped |
| `file_000000001e9882079286e1de59e27f1b.png` | `d78a758d49b5950125e4c29b840f45429354afe9` | 2,351,478 | Unclassified |
| `file_000000003a088207af254e352a9cb34a.png` | `df35c836f01961c5fc1222e575a5655ac4126f93` | 2,412,253 | Attempt 12 — mapped |
| `file_0000000047908207866f8f6e1b84ddb1.png` | `48ebe53785761c255f469c1ddac24fed818cd827` | 2,137,618 | Attempt 04 — mapped |
| `file_000000004b9c82119aa3e8e273bb1f2c.png` | `336d50a4517f963a0316b5918a5e39e531f031f6` | 1,881,690 | Unclassified |
| `file_0000000064d08211910f68838cb1237a.png` | `beb126d753f74a900c8965e5c655a7cee2021e8e` | 1,863,926 | Unclassified |
| `file_0000000066108207ac853d7dc9be1511.png` | `0dc0d981d29c5a84f0e9cd8aef12e013972bd153` | 2,366,473 | Attempt 10 — mapped |
| `file_0000000069f082079011ee0627b3995c.png` | `4b02b18f8b13d42360e87ab53798e6511693ba06` | 2,251,040 | Unclassified |
| `file_0000000089c8821182f53369d6fd3d0e.png` | `2c7c87e9b4a497da8b4476737509cb45b90e58c0` | 2,237,916 | Attempt 09 — mapped |
| `file_000000008c6882118eba4e134b3a76c2.png` | `a7afc0b15348df7d082972d0344d219dee5f191e` | 2,039,482 | Unclassified |
| `file_0000000093588207aecb418f8b7cf5c8.png` | `4818d76064c4b68baded9a8987b1dc76f095daa0` | 2,309,814 | Attempt 06 — mapped |
| `file_000000009638820799fc4d49f7b1d885.png` | `ab08e41316d93c86aeefc6f22bcc71ae3a8acec8` | 2,051,759 | Attempt 05 — mapped |
| `file_00000000a69c82079d17a0619f87d572.png` | `5b8c0af5f32a8bc185e798d3a8835a976d9328ae` | 2,327,329 | Attempt 14 — mapped |
| `file_00000000dfa08211a68e0644d6c6f2a1.png` | `d48628129129bc911f19be123c000995fc1407cd` | 1,969,510 | Unclassified |
| `file_00000000e5e482118465d6df866ea0d9.png` | `73d7c36832444601fd5691d9056e8541af37ea65` | 2,005,729 | Unclassified |
| `file_00000000f9108207bbd749f89003c6c2.png` | `073a47c6351915a4615be744dd37bfe486795cc7` | 2,215,056 | Attempt 15 — mapped |

