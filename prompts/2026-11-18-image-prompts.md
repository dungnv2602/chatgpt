# Image Prompts — 18 November 2026

**Project:** The Weather Between Us  
**Repository:** `dungnv2602/chatgpt`  
**Branch:** `gpt`  
**Novel scene:** [Scene 003 — The Shape of a Pause](../novel/Novel-01/Arc-01/Scene-003/scene.md)  
**Successful prompts only:** [Index](successful-image-prompts-index.md)

## Attempt 01 — The quieter path

- **Status before call:** Pending.
- **Operation:** Fresh text-to-image generation.
- **Mode:** Realistic — natural cinematic photography.
- **Scene moment:** Maya and the narrator pause at a fork in a small public garden; both are looking toward the quieter, tree-lined path they have independently chosen.
- **Visual continuity:** Maya's canonical face, long dark hair, proportions, and exact ivory silk-wrap outfit and garment construction are locked. The narrator's physical appearance is not established; show him from behind or in an indistinct three-quarter rear view without inventing identifying facial details.
- **Source/reference:** No image attached. Fresh generation based on the canonical written visual specification; not an edit.
- **Exact authored prompt:**

> Create one standalone photorealistic cinematic scene illustration for a contemporary, understated romance. In a modest public garden, an adult woman and an adult man pause together at a fork in a narrow path. The woman is Maya: preserve her canonical approved face and facial features, long dark hair, proportions, and exact ivory silk-wrap outfit and garment construction. Her face and clothing are locked; do not redesign, replace, cover, simplify, or reinterpret them. The man is the first-person narrator; his appearance has not been established, so show him from behind in a natural three-quarter rear view, with no clearly visible or distinctive facial features and no invented accessories.
>
> They stand side by side, not touching, looking toward the quieter path that follows a low garden wall beneath mature trees. Their body language is relaxed and companionable. Maya has a small, thoughtful expression, as if she has just admitted that this is the route she herself wanted to take. The man is listening. The moment should communicate mutual consideration through a subtle shared choice, not overt romance or posed affection.
>
> The garden is small and believable: uneven paving, a low wall, mature trees, restrained planted beds, and soft late-morning daylight. Frame as a medium-wide environmental two-shot at natural eye level, with both figures visible and the fork in the path clearly readable. Natural anatomy, realistic skin and hair, physically plausible light and shadows, restrained color, candid photographic realism. No text, captions, collage, extra foreground people, decorative romantic symbols, or invented signage.
- **Specific test:** Capture the scene's mutual preference moment while preserving Maya's locked visual identity and wardrobe and leaving the narrator's appearance unspecified.
- **Tool-prompt visibility:** The authored prompt above is the submitted direction; the image tool may not expose its compiled internal payload.


### Attempt 01 result

- **Actual result:** One fresh image returned.
- **Generation ID:** `51fc9618-eae3-4c86-a1ec-e39eede6cabc`.
- **Conversation artifact:** `a_serene_outdoor_park_garden_scene_with_soft_natu.png` (delivered in this conversation; not committed to GitHub).
- **Observed match:** A woman and a man stand together in a leafy public garden. The man is shown from behind, so his facial appearance is not established. The woman has long dark hair, and the garden atmosphere is broadly consistent with the scene.
- **Misses:** The returned garment reads as a long-sleeved ivory wrap dress rather than the exact canonical silk-wrap outfit and garment construction. The composition shows the pair facing one another on a path, not pausing at a clearly readable fork. The woman's exact facial identity cannot be verified because no reference image was attached.
- **Prompt execution note:** The image tool metadata exposed an empty compiled-prompt field. The actual concise authored direction supplied at generation was: “In a softly lit, cinematic garden, a young East Asian woman in an elegant ivory wrap dress strolls along a winding, tree-lined path, smiling as she engages with a man beside her. Framed by lush greenery, dappled sunlight, and a low stone wall, the scene feels calm, intimate, and quietly romantic.” This materially diverged from the archived prompt, introduced an unapproved ethnicity and changed the garment wording. This was an assistant execution error; neither detail is canon.
- **Classification:** Fresh generation, partial visual match / missed defining continuity requirements. Not approved canon.
- **Learning:** Do not use this image as proof of Maya's exact identity or wardrobe. A future attempt must use the canonical written face and garment specification verbatim and must not substitute a wrap dress for the approved silk-wrap outfit.


## Attempt 02 — The corner Maya wanted to share

- **Status before call:** Pending.
- **Operation:** Fresh text-to-image generation.
- **Mode:** Realistic — natural cinematic photography.
- **Scene:** Scene 004 — *What People Leave Behind*.
- **Selected moment:** Maya shows the narrator the quiet courtyard corner she personally likes, where the late-afternoon light reaches the wall and the courtyard can be heard without having to join it.
- **Visual continuity:** Maya's canonical approved face and facial features, long dark hair, proportions, and exact ivory silk-wrap outfit and garment construction are locked. The narrator's appearance is not established; show him from a three-quarter rear view without inventing identifying features.
- **Source/reference:** No image attached. Fresh generation based on the canonical written visual specification in [the visual reference index](../images/reference-index.md); not an edit and not an image-reference-guided generation.
- **Exact authored prompt:**

> Create one standalone photorealistic cinematic scene illustration for the contemporary romance *The Weather Between Us*. Depict the quiet personal moment from Scene 004, “What People Leave Behind”: Maya has brought the narrator to the narrow, peaceful corner of the shared courtyard that she likes for its late-afternoon light and for being able to hear the courtyard without having to join it.
> 
> Maya is an adult woman. Preserve her canonical approved face and facial features, long dark hair, proportions, and exact ivory silk-wrap outfit and garment construction: the same softly draped ivory silk wrap blouse resting off one shoulder, with bare shoulders and collarbones and its naturally open neckline; preserve the established opaque silk coverage and exact garment design. Her face and outfit are locked. Do not replace, redesign, cover, simplify, or reinterpret either.
> 
> The narrator is an adult man whose appearance has not been established. Show him seated beside Maya in a natural three-quarter rear view, with his face mostly turned away and no distinctive facial features, hairstyle, clothing details, or accessories invented. They sit close enough to share the quiet corner but are not touching. Maya is turned slightly toward the courtyard, one hand resting naturally on the arm of her chair, while the narrator listens. Their expressions and posture are relaxed and unposed; the emotional note is the ease of letting someone see a place that matters personally.
> 
> The courtyard is a believable completed residential courtyard, not a grand garden: a narrow strip beside planted beds, a low wooden stool, a simple chair, a climbing plant growing unevenly along a trellis, and a wall catching the last warm light of late afternoon. In the background, suggest the lived-in courtyard through a few mismatched chairs, pots near a drain, and soft indications of residential windows. Keep background residents distant and unobtrusive. Do not add signs, readable text, a named city, or culturally specific architecture.
> 
> Use a medium-wide environmental two-shot at natural eye level, with both figures and the quiet corner clearly visible. Let the courtyard and the shared pause carry the scene rather than a posed romantic gesture. Natural anatomy, realistic skin, hair, and silk texture, physically plausible light and shadows, restrained natural color, candid fine-art photographic realism, subtle depth of field. One image only; no collage, panels, captions, decorative romantic symbols, or extra foreground people.

- **Specific test:** Depict the scene's personal, quiet sharing moment while preserving Maya's exact canonical face and outfit and leaving the narrator's appearance unspecified.
- **Tool-prompt visibility:** The authored prompt above is the archived direction. The image tool may not expose its compiled internal payload.
- **Actual result:** One fresh image returned.
- **Generation ID:** `c0ba5ae6-3082-44e8-9b90-3e6631c414a3`.
- **Conversation artifact:** `a_warm_sunlit_outdoor_courtyard_garden_scene_in_a.png` (delivered in this conversation; not committed to GitHub).
- **Observed match:** A woman and man sit in a residential courtyard; the woman is shown in profile and the man from behind. The late-afternoon light and courtyard atmosphere broadly fit the scene.
- **Misses:** The image direction introduced an unapproved East Asian identity description and rendered Maya's locked ivory silk-wrap blouse as a wrap-style dress. Her exact canonical face cannot be verified, and the exact approved garment construction is not preserved.
- **Execution note:** The image tool exposed an empty compiled-prompt field. The actual concise direction used for generation diverged materially from the archived authored prompt. This was an assistant execution error; the introduced ethnicity and changed garment are not canon.
- **Classification:** Fresh generation, generated but missed defining continuity requirements. Not approved canon; do not use as Maya's canonical appearance.
- **Learning:** For the next attempt, foreground the exact canonical silk-wrap blouse and omit all ethnicity descriptors. Keep the scene variation limited to the courtyard, seated interaction, and late-afternoon light.


## Attempt 03 — The corner Maya wanted to share, exact wardrobe continuity

- **Status before call:** Pending.
- **Operation:** Fresh text-to-image generation.
- **Mode:** Realistic — natural cinematic photography.
- **Scene:** Scene 004 — *What People Leave Behind*.
- **Selected moment:** Maya shares the quiet courtyard corner she personally likes for its late-afternoon light and for being able to hear the courtyard without having to join it.
- **Source/reference:** No image attached. Fresh generation from the canonical written specification in [the visual reference index](../images/reference-index.md); not an edit and not reference-image-guided.
- **Continuity locks:** Preserve Maya's approved face and exact ivory silk-wrap blouse, including the off-shoulder drape and garment construction. No ethnicity descriptor. The narrator remains visually unspecified and is shown from behind.
- **Exact authored prompt:**

> Create one standalone photorealistic cinematic scene illustration for the contemporary romance *The Weather Between Us*. Depict the quiet personal moment from Scene 004, “What People Leave Behind”: Maya has brought the narrator to the narrow, peaceful corner of the shared courtyard that she likes for its late-afternoon light and for being able to hear the courtyard without having to join it.
> 
> Maya is an adult woman. Preserve her canonical approved face and facial features, long dark hair, proportions, and exact ivory silk-wrap blouse and garment construction: the same softly draped ivory silk wrap blouse resting off one shoulder, with bare shoulders and collarbones and its naturally open neckline. Preserve the exact approved garment design and opaque silk coverage. Her face and outfit are locked. Do not replace, redesign, cover, simplify, or reinterpret either. Do not add an ethnicity or cultural identity description.
> 
> The narrator is an adult man whose appearance has not been established. Show him seated beside Maya in a natural three-quarter rear view, with his face mostly turned away and no distinctive facial features, hairstyle, clothing details, or accessories invented. They sit close enough to share the quiet corner but are not touching. Maya is turned slightly toward the courtyard, one hand resting naturally on the arm of her chair, while the narrator listens. Their expressions and posture are relaxed and unposed; the emotional note is the ease of letting someone see a place that matters personally.
> 
> The courtyard is a believable completed residential courtyard, not a grand garden: a narrow strip beside planted beds, a low wooden stool, a simple chair, a climbing plant growing unevenly along a trellis, and a wall catching the last warm light of late afternoon. In the background, suggest the lived-in courtyard through a few mismatched chairs, pots near a drain, and soft indications of residential windows. Keep background residents distant and unobtrusive. Do not add signs, readable text, a named city, or culturally specific architecture.
> 
> Use a medium-wide environmental two-shot at natural eye level, with both figures and the quiet corner clearly visible. Let the courtyard and the shared pause carry the scene rather than a posed romantic gesture. Natural anatomy, realistic skin, hair, and silk texture, physically plausible light and shadows, restrained natural color, candid fine-art photographic realism, subtle depth of field. One image only; no collage, panels, captions, decorative romantic symbols, or extra foreground people.

- **Specific test:** Correct the previous execution drift by retaining the exact silk-wrap blouse and omitting invented identity details while changing only the courtyard scene and composition.
- **Tool-prompt visibility:** The authored prompt above is the archived direction; the image tool may not expose its compiled internal payload.
- **Outcome:** Pending; inspect immediately after generation.
