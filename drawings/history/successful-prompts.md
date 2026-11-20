# Historical Successful Prompt Index

**Scope:** Drawing prompts archived before 19 November 2026 in this folder.

This is a navigational index, not a replacement for the chronological records. The full authored prompt wording and its outcome record remain in the linked source entry. Links below point to those canonical records so that prompt text is not duplicated or allowed to drift.

## Classification rules

- **User-approved success:** The user explicitly accepted or designated the result as successful. Preserve that judgment, even when the archive also records technical caveats.
- **Recorded success with limitation:** The archive records a successful generation, but one requested detail was not independently verified or was imperfect.
- **Prompt compliance:** Do not infer prompt compliance merely because an image was returned. Fresh generation and source-image editing are distinct operations.
- A prompt with no recoverable authored wording cannot be listed as a reusable prompt.
- A user-approved image whose originating prompt cannot be mapped reliably is recorded separately, not attributed to a guessed attempt.

## Prompt index

### SP-01 — Comfort after a long workday

- **Source:** [12 November 2026 — Attempt 04](2026-11-12-image-prompts.md#04--comfort-after-a-long-workday)
- **Image:** [cozy-romantic-bedroom-portrait.png.webp](images/cozy-romantic-bedroom-portrait.png.webp)
- **Operation:** Fresh generation.
- **Classification:** Recorded successful composition; user liked the result.
- **What worked:** A coherent, warm, fully clothed comfort scene. The prompt assigned the man's resting position against the seated woman's upper chest/shoulder and gave her a clear comforting action.
- **Limitation:** The user later identified a hand-placement anatomy issue. This is evidence for the overall scene composition, not proof that the hand arrangement was correct.
- **Reuse value:** A starting point for the cozy after-work scene direction. Preserve the roles and actions accurately; specify hand ownership and layering separately when needed.

### SP-02 — Minimal hand-order correction using the original picture

- **Source:** [12 November 2026 — Attempt 11](2026-11-12-image-prompts.md#11--minimal-hand-order-correction-using-the-original-picture)
- **Image:** [tender-moments-in-a-cozy-bedroom.png.webp](images/tender-moments-in-a-cozy-bedroom.png.webp)
- **Operation:** The authored direction asked to preserve the existing image, but the actual tool result was a fresh generation, not a pixel-level edit.
- **Classification:** Qualified generation success; the image was returned and the broad cozy composition was preserved.
- **What worked:** A short, localized instruction: keep the picture the same, change only the two hands, and state which hand is underneath.
- **Limitation:** The exact left/right hand order was not independently confirmed. The prompt must not be cited as a proven hand-anatomy fix or as evidence that the source image was edited.
- **Reuse value:** An example of concise, localized authored direction, with the above limitation.

### SP-03 — Final source-linked painterly edit call

- **Source:** [12 November 2026 — Attempt 25](2026-11-12-image-prompts.md#25--final-source-linked-painterly-edit-call)
- **Operation:** Intended as a source-linked style edit; returned metadata did not confirm an edit or source attachment.
- **Classification:** **User-designated successful** on 19 November 2026.
- **What is known:** The user explicitly designated this attempt as successful, and that user classification is preserved.
- **Image link:** The archive does not provide a reliable filename-to-asset mapping for this attempt, so no image link is assigned rather than guessing.
- **Important caveat:** The same archival entry records that the returned image appeared to differ from the authored pose, hand placement, character-continuity, and style requirements, and that `edit_op` and `parent_gen_id` were null. Do not use this entry as technical proof that source-linked editing worked or that all prompt constraints were followed.
- **Reuse value:** Preserve as a user-designated success record. Its technical limitations remain visible.

### SP-04 — Historical silk-wrap portrait direction

- **Source:** [12 November 2026 — Attempt 33](2026-11-12-image-prompts.md#33--historical-silk-wrap-portrait-direction-realistic-mode)
- **Image 01:** [realistic-silk-wrap-portrait-soft-gaze-01.png.webp](images/realistic-silk-wrap-portrait-soft-gaze-01.png.webp)
- **Image 02:** [realistic-silk-wrap-portrait-close-framing-02.png.webp](images/realistic-silk-wrap-portrait-close-framing-02.png.webp)
- **Operation:** Fresh generation; no reference image attached.
- **Classification:** Successful match for the portrait brief. Two outputs were returned, and the user later approved both.
- **What worked:** A clearly adult subject; long, softly flowing dark chestnut hair; ivory silk-wrap styling; naturally draped bare shoulder and visible collarbones; warm golden cinematic light; a softly blurred interior; close upper-body framing; affectionate direct gaze; photorealistic fine-art treatment.
- **Provenance note:** The authored prompt was newly composed from historical art-direction notes. The archive explicitly does not claim it was a verbatim recovery of an unavailable earlier prompt.
- **Reuse value:** Strongest historically supported baseline for this specific realistic silk-wrap portrait direction. The prompt text is preserved in full at the source link.

### SP-05 — Direct reuse of the proven silk-wrap portrait direction

- **Source:** [13 November 2026 — Attempt 04](2026-11-13-image-prompts.md#attempt-04--direct-reuse-of-the-proven-silk-wrap-portrait-direction)
- **Image:** [file_000000005280821180bb6e444a0a80cd.png.webp](images/file_000000005280821180bb6e444a0a80cd.png.webp) — the archived binary name is retained; the November 13 record maps it to the user-approved “realistic-silk-wrap-portrait-open-drape-03.png” output.
- **Operation:** Fresh generation, without a reference attachment.
- **Base prompt:** Reuses the authored wording of [12 November — Attempt 33](2026-11-12-image-prompts.md#33--historical-silk-wrap-portrait-direction-realistic-mode) verbatim.
- **Classification:** The prompt record's final user assessment is **successful**. An earlier technical assessment noted a garment-construction mismatch; that observation remains in the source record and is not erased by the later user classification.
- **What worked:** Returning to the original art direction without the assistant-added reference attachment, conservative wardrobe redesign, and extra identity-preservation wording.
- **Reuse value:** Cross-session evidence for using the proven baseline unchanged before introducing further variations.

## User-approved outputs without reliable prompt attribution

The user separately designated these five cozy-scene images as successful:

- [cozy-couples-warm-indoor-embrace.png.webp](images/cozy-couples-warm-indoor-embrace.png.webp)
- [cozy-evening-embrace-by-lamplight.png.webp](images/cozy-evening-embrace-by-lamplight.png.webp)
- [cozy-lavender-bedroom-cuddle.png.webp](images/cozy-lavender-bedroom-cuddle.png.webp)
- [tender-bedroom-cuddle.png.webp](images/tender-bedroom-cuddle.png.webp)
- [tender-evening-on-the-floral-sofa.png.webp](images/tender-evening-on-the-floral-sofa.png.webp)

**Source record:** [13 November conversation integrity — user confirms five cozy-scene images](2026-11-13-conversation-integrity.md#10-user-confirms-five-cozy-scene-images-as-successful-index-and-skill-updated).

The chronological prompt record does not reliably map these filenames to exact prompt attempts. They remain user-approved outputs, but are deliberately not attributed to invented prompt IDs or used as prompt-level evidence in the global successful-pattern index.

## Related results not classified as successful prompts

- [12 November — Attempt 03](2026-11-12-image-prompts.md#03--reversed-lap-pose) produced an image the user found beautiful, but the resting roles were reversed from the requested pose. It is indexed among off-target results, not as a successful prompt.
- [12 November — Attempt 21](2026-11-12-image-prompts.md#21--reference-guided-reconstruction-of-the-correct-after-work-pose) achieved the correct resting direction but missed the painterly style target and did not conclusively establish hand laterality. It remains a partial result, not a full prompt success.

## Coverage and exclusions

This index includes prompt-level outcomes that the surviving records support. Attempts with no recorded result (including pending entries) are not silently classified as success or failure. The 11 November conversation archive says the exact rejected and successful prompt text is unavailable; its images and events cannot be reliably mapped to reproducible prompt wording. The 12 November transcript fragments are conversation records, not verified prompt-and-result pairs.
