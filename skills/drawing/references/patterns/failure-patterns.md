# Global Failure Drawing Patterns

Recurring failures extracted from the pre-19 November 2026 historical prompt archive. The corresponding prompt-level records are indexed in [Historical Failed Prompt Index](../../../../drawings/history/failed-prompts.md).

Observed outcomes, suspected causes, and tested countermeasures are kept separate. An unknown cause must remain unknown.

---

## F-001 — Two-person pose direction can be reversed despite explicit role descriptions

- **Confidence:** Supported
- **Last reviewed:** 2026-11-20
- **Scope:** Two-person scenes with asymmetric resting, leaning, holding, or hand-placement roles.

### Observed failure
Despite explicit role assignments, the image repeatedly showed the wrong person resting or leaning. It also moved the hands to a different contact area.

### Impact
The output can look coherent and affectionate while failing the defining action of the brief. Clothing and setting may be close, but the scene's physical meaning is reversed.

### Suspected cause
The archive does not establish the image model's internal cause. Repeated role reversal is observed. Claims about prompt length, model bias, or hidden context are hypotheses, not findings.

### Countermeasures tested

| Countermeasure | Evidence | Result |
|---|---|---|
| Repeatedly restate the role and hand arrangement in increasingly detailed prompts | [12 November — Attempts 14–20](../../../../drawings/history/failed-prompts.md#fp-05--repeated-reversed-resting-roles-in-the-cozy-bedroom-sequence) | Ineffective in this sequence. The resting direction continued to reverse |
| Reuse a shorter prompt with explicit role assignment | [12 November — Attempt 20](../../../../drawings/history/2026-11-12-image-prompts.md#20--concise-reuse-of-successful-after-work-pose) | Ineffective. The same reversed composition returned |
| Use a reference-guided reconstruction | [12 November — Attempt 21](../../../../drawings/history/2026-11-12-image-prompts.md#21--reference-guided-reconstruction-of-the-correct-after-work-pose) | Partial improvement: resting direction was correct, but style and hand laterality remained unresolved |
| Request style-only transformations of the partial result | [12 November — Attempts 22–27](../../../../drawings/history/failed-prompts.md#fp-07--style-transfer-and-source-preservation-attempts) | Ineffective. The source composition was not preserved |

### Effective prevention rule
Not established. Do not keep repeating superficial prompt variations after a persistent reversal. Reassess the brief and generation method. Classify the result against the defining physical action.

### Limitations
The evidence is concentrated in one cozy-bedroom task. It does not prove that all two-person compositions are equally difficult.

---

## F-002 — An intended image edit may return a fresh generation instead

- **Confidence:** Supported
- **Last reviewed:** 2026-11-20
- **Scope:** Image edits, style transfers, and prompts that depend on preserving a supplied source image.

### Observed failure
Several operations were described or intended as edits, but the returned image was a new generation. The output did not preserve the source composition, and the metadata did not confirm a parent/edit relationship.

### Impact
The user may believe a source image was modified when it was not. The resulting image can lose composition, identity, pose, or other locked details.

### Suspected cause
The records show missing attachments in some calls and null edit/parent metadata in others. They do not establish one universal technical cause.

### Countermeasures tested

| Countermeasure | Evidence | Result |
|---|---|---|
| Mention the source filename in prompt prose | [13 November — Attempt 01](../../../../drawings/history/2026-11-13-image-prompts.md#attempt-01--source-guided-silk-wrap-portrait) | Failed as a source-guided workflow. The actual image was not attached |
| Attach the actual image reference | [13 November — Attempt 02](../../../../drawings/history/2026-11-13-image-prompts.md#attempt-02--reference-attached-silk-wrap-portrait) | The reference was attached, but generation was rejected. This did not test successful editing |
| Supply structured reference arguments and request a style edit | [12 November — Attempts 23–26](../../../../drawings/history/failed-prompts.md#fp-07--style-transfer-and-source-preservation-attempts) | Returned outputs did not confirm source-linked edits. Metadata remained null |

### Effective prevention rule
Treat source preservation as unverified until the tool confirms the source/edit relationship and the returned image visibly preserves the source. If edit/parent metadata is null or the composition changes, record the result as a fresh or unverified generation, not a successful edit.

### Limitations
Metadata checks prevent false claims. They do not themselves make the tool perform a valid edit.

---

## F-003 — Explicit single-image instructions can still produce a multi-panel layout

- **Confidence:** Supported
- **Last reviewed:** 2026-11-20
- **Scope:** Scene illustrations intended as one standalone frame.

### Observed failure
Two consecutive prompts requested one standalone illustration and expressly excluded comic pages, collages, panels, and captions. Both outputs were multi-panel comic-page collages.

### Impact
The output format and narrative moment are wrong even when some characters or setting details are recognizable.

### Suspected cause
No internal cause is established. The record demonstrates non-compliance with the requested layout, not why it occurred.

### Countermeasures tested

| Countermeasure | Evidence | Result |
|---|---|---|
| Explicitly require exactly one standalone illustration and forbid panels/captions | [16 November — Attempt 03](../../../../drawings/history/2026-11-16-image-prompts.md#attempt-03--the-book-handoff-single-scene) | Ineffective. Another multi-panel collage was returned after the earlier collage |

### Effective prevention rule
Not established. After repeated output-format failure, do not submit near-identical retries and assume that adding more negative wording will solve it.

### Limitations
The evidence concerns two sequential bookshop-scene attempts, not all illustration tasks.

---

## F-004 — A generic safety refusal does not identify the prompt element that triggered it

- **Confidence:** Supported
- **Last reviewed:** 2026-11-20
- **Scope:** Image-generation refusals that provide only a broad safety message.

### Observed failure
Several materially different prompt attempts received the same generic refusal and returned no image. The tool did not identify a specific triggering phrase, image feature, or contextual factor.

### Impact
A prompt author can waste attempts by treating a generic refusal as a precise diagnosis and changing arbitrary wording.

### Suspected cause
Unknown. Do not assert that a particular garment, pose, source image, or phrase caused the refusal unless the tool provides that information.

### Countermeasures tested

| Countermeasure | Evidence | Result |
|---|---|---|
| Attach a reference and retain the earlier art direction | [13 November — Attempt 02](../../../../drawings/history/2026-11-13-image-prompts.md#attempt-02--reference-attached-silk-wrap-portrait) | Rejected. No specific cause was identified |
| Materially change to a conventional modest editorial treatment | [13 November — Attempt 03](../../../../drawings/history/2026-11-13-image-prompts.md#attempt-03--modest-editorial-silk-wrap-portrait-safety-aware-revision) | Same generic refusal |
| Change indoor fashion framing to a daylight outdoor fashion setting | [12 November — Attempts 31–32](../../../../drawings/history/failed-prompts.md#fp-08--generic-safety-refusals-during-portrait-retries) | Same generic refusal |

### Effective prevention rule
Do not claim to know the trigger. Make at most a genuinely meaningful, policy-compliant revision when appropriate. If it is also refused, stop the retry loop rather than probing with superficial wording changes.

### Limitations
This pattern documents refusal behavior and the limits of diagnosis. It does not classify the underlying content or imply that a future version would necessarily be refused.

---

## F-005 — The prompt recorded as authored can differ from the prompt actually submitted

- **Confidence:** Provisional
- **Last reviewed:** 2026-11-20
- **Scope:** Workflows where a canonical or pre-committed prompt is prepared before an image call.

### Observed failure
One archived attempt records a major difference between the authored and submitted prompts. The submitted text was shorter and added details that the authored version did not contain.

### Impact
The image result cannot fairly be evaluated as a test of the archived prompt. It also introduces unsupported character or scene details and weakens the reliability of the prompt archive.

### Suspected cause
The record identifies an execution deviation, but not why the submitted wording diverged.

### Countermeasures tested

| Countermeasure | Evidence | Result |
|---|---|---|
| Commit a canonical prompt before the image call | [16 November — Attempt 06](../../../../drawings/history/2026-11-16-image-prompts.md#attempt-06--maya-across-the-café-table) | The workflow was not followed faithfully. The submitted wording differed |

### Effective prevention rule
Before the image call, compare the exact text about to be submitted with the committed prompt. Record any intentional change before generation. Do not claim that a prompt was tested when a different prompt was actually sent.

### Limitations
The archive provides one clearly documented instance. Confidence remains provisional.

---

## F-006 — A requested attribute can remain unchanged despite a successful generation

- **Confidence:** Provisional
- **Last reviewed:** 2026-11-20
- **Scope:** Revisions where one visible attribute must change while the surrounding image is retained.

### Observed failure
A fresh generation was returned after a prompt requested a cream cardigan, but the result retained the preceding lavender outfit.

### Impact
A successful tool call can be mistaken for a successful revision even though the defining requested change did not happen.

### Suspected cause
The archive suggests that the preceding image and conversation context may have influenced the output. This is an interpretation, not a confirmed internal cause.

### Countermeasures tested

| Countermeasure | Evidence | Result |
|---|---|---|
| Fresh generation with the requested cream cardigan stated in the prompt | [12 November — Attempt 13](../../../../drawings/history/2026-11-12-image-prompts.md#13--fresh-generation-in-the-preferred-cream-cardigan) | Ineffective in this attempt. Lavender remained |

### Effective prevention rule
Evaluate the changed attribute itself. A returned image is not a successful revision unless the requested visible change is present. No reliable prevention method is established by this single example.

### Limitations
This is one observed clothing revision and does not prove that preceding visual context is the cause.

---

## F-007 — Prompt language can be retained after the user has explicitly rejected it

- **Confidence:** Provisional
- **Last reviewed:** 2026-11-20
- **Scope:** Prompt reuse and revision when a user has corrected or withdrawn specific wording, especially restrictions or negative instructions.

### Observed failure
During the formal redo of the November 19 portrait, the assistant reused the earlier prompt with its closing restrictive sentence still present. The user then explicitly instructed that the sentence be removed. The next formal attempt removed that sentence and preserved the remaining authored wording. The user also identified unnecessary additions and restrictive boilerplate as an unwanted recurring behavior.

### Impact
The prompt no longer follows the user's latest direction. Reusing a historical prompt verbatim can become incorrect when the user has since amended or rejected part of it. It can also undermine trust and make the resulting generation an invalid test of the current brief.

### Suspected cause
The records support a workflow failure to apply the latest instruction when reusing a historical baseline. They do not establish a technical image-model cause.

### Countermeasures tested

| Countermeasure | Evidence | Result |
|---|---|---|
| Remove only the specifically rejected closing sentence while preserving all other prompt wording | [20 November — Attempt 46](../../../../drawings/2026-11-19/attempt-46.md) | The prompt record confirms the requested sentence was removed and the remaining wording was preserved. The user has not yet approved the resulting image. |
| Make pattern consultation and a full prompt-fidelity check mandatory before committing a prompt | [20 November — Attempts 45–46](../../../../drawings/2026-11-19/attempt-45.md) and [Drawing Skill](../../SKILL.md) | The prevention procedure was adopted. Its effectiveness across future attempts is not yet established. |

### Effective prevention rule

The mandatory, exhaustive rule is maintained in
[Prompt Fidelity and Unrequested Restrictions](../prompt-fidelity.md).
Apply that reference before every prompt draft, reuse, revision, archive, and
generation. In particular, compare the complete draft with the active brief
and the user's latest instructions. Do not restore wording merely because it appears in an older successful prompt. Do not add or relocate equivalent restrictions after the user has rejected them. Keep only language supported by the current brief or genuinely required by the task.

### Limitations
This entry documents one explicit correction sequence and a broader user-identified concern. It does not establish that every negative instruction is unnecessary. The active brief and applicable requirements remain controlling.
