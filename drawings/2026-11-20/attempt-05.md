# Attempt 05 — Localized nonphysical edge edit of Samantha

- **Date:** 2026-11-20
- **Session ID:** SAMANTHA-2026-11-20-01
- **Session brief:** [session-01-brief.md](session-01-brief.md)
- **Status before call:** Prompt archived and verified; proceeding under the user's delegation to let the assistant drive.
- **Operation type:** Edit of the exact Attempt 04 output.
- **Source image:** Attempt 04; generation ID `061c1943-f7cc-4818-a897-3f07e16b38d4`; asset ID `file_0000000047908207866f8f6e1b84ddb1`; local artifact `/mnt/data/a_warm_cinematic_sunlit_indoor_portrait_scene_a.png`.
- **Source role:** Assistant-selected provisional working source. Not yet a user-approved keeper. This image is present in the current conversation as the immediately preceding generated image; the edit call must use that actual image, not merely cite the generation ID in text.
- **Mode:** Realistic — preserve naturalistic cinematic photography.
- **Specific objective:** Make the nonphysical nature legible through a small, optically plausible loss of contour along a short section of window-side hair and adjacent shoulder, while preserving every other source property.

## Acceptance criteria — before generation/editing

| # | Observable requirement | Critical? | Expected visible evidence |
|---|---|---|---|
| 1 | Exact Attempt 04 portrait remains the source | Yes | Same face, gaze, expression, hair, blouse, pose, crop, room, window, and lighting |
| 2 | Only the localized window-side contour is changed | Yes | A small section of hair/shoulder edge softens and partially loses continuity; all other regions remain visually unchanged |
| 3 | The edge reads as a temporary nonphysical presence | Yes | A perceptible, gradual thinning/feathering into bright air, not merely particles or decorative sparkle |
| 4 | Naturalistic photographic appearance is preserved | Yes | Physically plausible daylight and subtle optical transition; no fantasy or science-fiction overlay |
| 5 | The edit introduces no unrelated additions | Yes | No new objects, face changes, clothing changes, pose changes, extra figures, particles, UI, or decorative VFX |

## Prompt difference

- **Baseline:** No successful Samantha prompt exists. The active session brief and Samantha visual-drive note are the creative authority. Attempt 04 is the immediate visual edit source only, not a successful prompt baseline.
- **Preserved:** The exact Attempt 04 woman's face, expression, auburn hair, freckles, coral-red blouse, posture, crop, apartment, window, city background, warm light, color grade, and photographic rendering.
- **Changed:** One small portion of the viewer-right, window-side outer hair/shoulder contour is allowed to feather and partially dissolve into bright air. This is the assistant's chosen next test under the user's explicit delegation to let the assistant drive.
- **Excluded:** The previous floating amber flecks are not to be amplified; they read as dust/sparkle rather than loss of physical contour. Exclude glow, glitter, particles, ghost/hologram effects, interface graphics, and all unrelated redesign.

## Exact authored edit prompt

> Edit the exact supplied Attempt 04 portrait. This is a tightly localized image edit, not a new generation or a reinterpretation of the scene.
> 
> Preserve the woman's exact face, facial features, eyes, freckles, expression, gaze, auburn hairstyle, hair volume and overall hair shape, coral-red blouse, fabric, neckline, shoulders, body, pose, posture, hands, crop, camera angle, window, apartment interior, background, city view, lighting, color grade, depth of field, and photographic texture. Preserve the existing composition and every object in it. Do not beautify, redesign, replace, or reinterpret her.
> 
> Make one localized change only: on a short, narrow section of the outer hair contour and the adjacent shoulder contour nearest the bright window on the viewer-right side of the image, let the physical edge gently lose continuity into the sunlit air. A few individual hair strands should become faintly translucent and feather away; the shoulder edge should soften and partially dissolve into the window light over a small, controlled area. The transition should be optically plausible, as though a brief human shape is thinning into bright air—not as though an effect has been pasted on top. The change must be visibly readable at normal image size but remain subtle and localized. Keep her face, eyes, central hair mass, neck, chest, and the rest of her body completely solid and unchanged.
> 
> Do not add floating particles, glitter, dust, sparks, glow, halos, smoke, haze, circuitry, grids, symbols, interface graphics, neon, holographic transparency, ghost effects, or new objects. Do not change the woman's face, expression, hair design, clothing, pose, body, background, window, lighting, or framing. If a convincing localized edge transition cannot be achieved without altering other parts of the portrait, preserve the source rather than redesigning it.

## Result — fresh generation, not a confirmed edit

- **Actual result:** One portrait was returned. Visually it is very close to Attempt 04, but similarity does not establish source continuity.
- **Generation ID:** `86f0848c-6d9d-41f7-96c0-cf6c4f9b28bd`.
- **Asset ID:** `file_000000009638820799fc4d49f7b1d885`.
- **Local artifact:** `/mnt/data/a_warm_softly_lit_indoor_portrait_scene_in_a_cozy.png`.
- **Tool metadata:** `edit_op: null`, `parent_gen_id: null`, `prompt: ""`, `seed: null`. No source linkage was confirmed. The compiled-prompt field was empty.
- **Visual assessment:** The portrait remains naturalistic and close in appearance to Attempt 04. The outer hair/shoulder contour still reads as physically continuous; minor bright flecks/rim light do not communicate a body dissolving into air.
- **Acceptance criteria:** Exact source preservation — Not assessable (no parent linkage); localized-only change — Not assessable as an edit; nonphysical edge cue — Fail; naturalistic appearance — Pass; no unrelated additions — Pass.
- **Outcome:** Fresh generation, not a confirmed edit; the defining target remains unmet.
- **Approval:** Not yet assessed by the user. Do not promote this image to a keeper or prompt baseline.
- **Execution correction:** The authored note identified Attempt 04's asset ID, but the actual image-edit call did not pass that ID in `referenced_image_ids`. This was an assistant execution omission, not evidence that the tool cannot accept the reference.
- **Next step:** One corrected attempt will pass the exact Attempt 04 asset ID explicitly via the image tool's reference argument. If returned metadata still lacks source linkage, stop further edit retries and explain the limitation rather than repeating context-only calls.

The authored prompt was committed and read back before the image-edit call. After the call, record whether the tool actually confirms Attempt 04 as the parent/source, inspect the rendered result, score each criterion separately, and state any source-linkage uncertainty. Do not call it a confirmed edit merely because it looks similar.


## User approval — 2026-11-20
- **Attempt 05:** Approved as the **casual path**. This is a user approval of the image/branch for casual-path continuity; it does not retroactively confirm source linkage or promote the prompt to a successful edit baseline.
- **Attempt 06:** Approved as the **sweet path**. This is a user approval of the image/branch for sweet-path continuity; it does not retroactively confirm source linkage or erase recorded mismatches.
