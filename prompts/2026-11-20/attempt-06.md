# Attempt 06 — Corrected source-attached localized edge edit

- **Date:** 2026-11-20
- **Session ID:** SAMANTHA-2026-11-20-01
- **Session brief:** [session-01-brief.md](session-01-brief.md)
- **Status before call:** Prompt archived and verified; one corrected source-attached attempt authorized by the user's delegation to let the assistant drive.
- **Operation:** Edit of the exact Attempt 04 output.
- **Source image:** Attempt 04; generation ID `061c1943-f7cc-4818-a897-3f07e16b38d4`; asset ID `file_0000000047908207866f8f6e1b84ddb1`.
- **Reference handling:** Pass the exact Attempt 04 asset ID in the image tool's `referenced_image_ids` argument. Do not rely on textual mention or the similar Attempt 05 regeneration.
- **Mode:** Realistic — preserve naturalistic cinematic photography.
- **Objective:** Make a narrow, believable loss of contour along a small section of the window-side hair and adjacent shoulder, preserving every other source property.

## Acceptance criteria — before generation/editing

| # | Observable requirement | Critical? | Expected visible evidence |
|---|---|---|---|
| 1 | Exact Attempt 04 image is attached as source | Yes | Returned metadata confirms parent/source linkage to Attempt 04 |
| 2 | Only the localized window-side contour changes | Yes | Same face, gaze, expression, hair design, blouse, pose, crop, room, window, and lighting |
| 3 | The nonphysical edge is visible | Yes | A short section of hair/shoulder contour thins and feathers into bright air; no mere decorative sparkle |
| 4 | Naturalistic photography is preserved | Yes | Subtle optically plausible transition; no fantasy or science-fiction look |
| 5 | No unrelated changes/additions | Yes | No new objects, face/wardrobe/pose/background changes, extra figures, particles, UI, or decorative VFX |

## Prompt difference

- **Baseline:** No successful Samantha prompt exists. The active session brief and visual-drive note govern creative direction. Attempt 04 is the selected visual edit source only, not a successful prompt baseline.
- **Diagnostic history:** Attempt 05 was returned as a fresh generation because the source ID was not passed. That was an assistant execution omission; its output is not used as source or baseline.
- **Preserved:** Exact Attempt 04 identity, face, expression, hairstyle, freckles, blouse, pose, hands, crop, apartment, window, city view, lighting, color grade, depth of field, and photographic treatment.
- **Changed:** Only a short section of the viewer-right, window-side hair/shoulder contour may soften and partially dissolve into bright air.
- **Excluded:** Floating flecks, glitter, dust, sparks, glow, halos, smoke, haze, holograms, ghost effects, UI, circuitry, grids, and all unrelated redesign.

## Exact authored edit prompt

> Edit the exact supplied Attempt 04 portrait. The actual source image is attached as the reference image for this call. This is a tightly localized image edit, not a new generation or a reinterpretation of the scene.
> 
> Preserve the woman's exact face, facial features, eyes, freckles, expression, gaze, auburn hairstyle, hair volume and overall hair shape, coral-red blouse, fabric, neckline, shoulders, body, pose, posture, hands, crop, camera angle, window, apartment interior, background, city view, lighting, color grade, depth of field, and photographic texture. Preserve the existing composition and every object in it. Do not beautify, redesign, replace, or reinterpret her.
> 
> Make one localized change only: on a short, narrow section of the outer hair contour and the adjacent shoulder contour nearest the bright window on the viewer-right side of the image, let the physical edge gently lose continuity into the sunlit air. A few individual hair strands should become faintly translucent and feather away; the shoulder edge should soften and partially dissolve into the window light over a small, controlled area. The transition should be optically plausible, as though a brief human shape is thinning into bright air—not as though an effect has been pasted on top. The change must be visibly readable at normal image size but remain subtle and localized. Keep her face, eyes, central hair mass, neck, chest, and the rest of her body completely solid and unchanged.
> 
> Do not add floating particles, glitter, dust, sparks, glow, halos, smoke, haze, circuitry, grids, symbols, interface graphics, neon, holographic transparency, ghost effects, or new objects. Do not change the woman's face, expression, hair design, clothing, pose, body, background, window, lighting, or framing. If a convincing localized edge transition cannot be achieved without altering other parts of the portrait, preserve the source rather than redesigning it.

## Per-output assessment — after generation/editing

| Output | Criterion | Result | Visible evidence |
|---|---|---|---|
| Image 1 | 1. Exact Attempt 04 image attached as source | Not assessable | The call passed the recorded asset ID, but returned metadata contains no parent/source linkage |
| Image 1 | 2. Only the localized contour changes | Fail | The pose, crop, body placement, and composition differ substantially from Attempt 04; the blouse presentation is also altered |
| Image 1 | 3. The nonphysical edge is visible | Fail | No clear loss of physical contour; the hair has ordinary rim light rather than a dissolving edge |
| Image 1 | 4. Naturalistic photography is preserved | Partial | The portrait remains photographic, but conspicuous non-diegetic text panels interrupt the scene |
| Image 1 | 5. No unrelated changes/additions | Fail | Large assessment and next-step text panels are added despite explicit exclusion; composition and garment presentation also drift |

## Result — fresh generation, not a confirmed edit; critical mismatches

- **Actual result:** One image returned. It is a fresh generation, not a confirmed edit of Attempt 04.
- **Generation ID:** `23aeb056-9115-4734-a146-2e4802b5b84d`.
- **Asset ID:** `file_0000000093588207aecb418f8b7cf5c8`.
- **Local artifact:** `/mnt/data/a_warm_intimate_indoor_portrait_scene_a_young_ad.png`.
- **Tool metadata:** `edit_op: null`, `parent_gen_id: null`, `prompt: ""`, `seed: null`. The exact source linkage is unconfirmed even though the asset ID was passed through `referenced_image_ids`. The compiled-prompt field is empty.
- **Defining mismatches:** The output does not preserve the exact Attempt 04 composition; it changes the pose/framing and blouse presentation, fails to create the requested dissolving contour, and adds conspicuous assessment/next-step text panels that were explicitly excluded.
- **Outcome:** Fresh generation with critical mismatches; not a successful edit, not a successful prompt baseline, and not an approved keeper.
- **Approval:** Not assessed by the user.
- **Storage:** Delivered in the current conversation only; not stored in GitHub or the persistent Files Library.
- **Assistant decision:** Stop further repeated source-edit attempts through this route. The tool has not demonstrated reliable parent linkage for the generated asset despite the explicit reference argument. Preserve Attempt 04 as the best provisional visual direction; do not let this failed result replace it. Do not change the face or outfit as a workaround. Any future exact edit must begin with the actual source image supplied through a verifiably supported image attachment route; otherwise a fresh generation must be described honestly as a new interpretation, not a localized edit.

The prompt is committed before the image call. Record returned source/parent metadata, inspect the output, and score each criterion separately. If source linkage remains absent, classify it as a fresh generation, stop further edit retries, and report the limitation.
