# Global Successful Drawing Patterns

Reusable techniques extracted from the pre-19 November 2026 historical prompt archive. The corresponding prompt records are indexed in [Historical Successful Prompt Index](../../../../drawings/history/successful-prompts.md).

Only patterns with traceable successful or user-approved evidence belong here. A pattern's confidence describes the reusable lesson, not the perfection of every output.

---

## S-001 — Reuse a proven prompt baseline verbatim before changing it

- **Confidence:** Supported
- **Last reviewed:** 2026-11-20
- **Scope:** Iterations on a visual direction that already has a successful or user-approved result.

### Principle
When a prompt has already produced an accepted result, use its authored wording as the controlled baseline for the next attempt. Do not first reinterpret, redesign, or embellish it.

### Problem addressed
Unnecessary assistant-added wording and creative reinterpretation can move a new attempt away from the direction the user already accepted. It also makes it difficult to determine which change affected the result.

### Implementation
1. Identify the exact archived prompt associated with the accepted result.
2. Reuse its authored wording unchanged for a baseline reproduction.
3. Do not attach a reference image or introduce new restrictions unless the current brief requires them.
4. After the baseline has been tested, change one clearly identified dimension at a time.
5. Record whether the new result actually follows the changed requirement.

### Evidence
- [12 November 2026 — Attempt 33](../../../../drawings/history/2026-11-12-image-prompts.md#33--historical-silk-wrap-portrait-direction-realistic-mode) — successful historical silk-wrap portrait direction; two outputs were returned and later approved by the user.
- [13 November 2026 — Attempt 04](../../../../drawings/history/2026-11-13-image-prompts.md#attempt-04--direct-reuse-of-the-proven-silk-wrap-portrait-direction) — the same authored prompt was reused verbatim in a later session; the prompt record's final user assessment is successful.

### Limitations
This is a controlled-reuse method, not a guarantee that every requested detail will be reproduced. Retain any technical caveats in the source record, and never assume that an earlier success authorizes changes to a current locked requirement.

---

## S-002 — Anchor a portrait with a coherent set of positive visual cues

- **Confidence:** Supported
- **Last reviewed:** 2026-11-20
- **Scope:** Realistic portrait prompts and similarly focused character imagery.

### Principle
Describe the intended image through a compact, internally consistent set of positive visual anchors: subject, hair or other identifying appearance, garment and material, pose, expression, lighting, composition, setting, and rendering medium.

### Problem addressed
Vague aesthetic labels alone leave too much of the intended visual direction unspecified. Excessive negative instructions can also obscure the central image being requested.

### Implementation
For a focused portrait, specify:
- The clearly adult subject and the relevant visible appearance.
- The garment, fabric, drape, and intended construction.
- The pose and direction of the gaze.
- The emotional expression.
- The light quality and environment.
- The camera distance or framing.
- The intended rendering medium and finish.

Keep the cues mutually consistent. Prefer direct descriptions of what should appear over a long list of things that must not appear.

### Evidence
- [12 November 2026 — Attempt 33](../../../../drawings/history/2026-11-12-image-prompts.md#33--historical-silk-wrap-portrait-direction-realistic-mode) — the prompt specified the adult subject, dark chestnut hair, ivory silk-wrap styling, shoulder and collarbone drape, warm golden light, softly blurred interior, close upper-body composition, affectionate gaze, and photorealistic fine-art treatment. Two outputs matched the overall portrait direction.
- [13 November 2026 — Attempt 04](../../../../drawings/history/2026-11-13-image-prompts.md#attempt-04--direct-reuse-of-the-proven-silk-wrap-portrait-direction) — reuse of the same positive art-direction cues was again designated successful in the final user assessment.

### Limitations
Positive visual specificity does not guarantee exact garment construction, identity continuity, or source-image editing. Inspect the returned image for the actual physical result; do not infer a detail from the prompt alone.

---

## S-003 — Assign each person an explicit role in a physical interaction

- **Confidence:** Provisional
- **Last reviewed:** 2026-11-20
- **Scope:** Two-person scenes involving contact, leaning, carrying, resting, or hand placement.

### Principle
Name the actor, the action, and the recipient directly. Describe the physical relationship from each person's role rather than relying on a vague phrase such as “the couple cuddles.”

### Problem addressed
Two-person poses can be reversed while still producing a plausible or attractive image. General mood language does not reliably define who is doing what.

### Implementation
Use direct constructions such as:
- “The man lies on his side with his head resting against the woman's shoulder.”
- “The woman sits upright and supports the back of his head with her left hand.”
- “Her right hand is underneath; his left hand rests on top.”

State the essential spatial relationship before decorative setting details. For complicated contact, separate each hand or limb by actor and side.

### Evidence
- [12 November 2026 — Attempt 04](../../../../drawings/history/2026-11-12-image-prompts.md#04--comfort-after-a-long-workday) — the prompt assigned the man's resting position against the seated woman and her action of cradling his head; the user liked the resulting overall comforting composition.

### Limitations
This pattern is provisional and does not guarantee pose compliance. Later attempts [14–20](../../../../drawings/history/2026-11-12-image-prompts.md#14--mistaken-tea-scene-interpretation-cream-cardigan-and-navy-polo) repeatedly reversed the resting roles even after more detailed instructions. It should improve clarity, not be treated as a proven solution to persistent pose inversion.
