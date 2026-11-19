# Image Prompts — 16 November 2026

**Project:** Maya_and_Me — Novel 01, *The Weather Between Us*
**Branch:** `chatgpt`
**Novel scene:** [Scene 001 — The Weather at the Window](../novel/Novel-01/Arc-01/Scene-001/scene.md)
**Illustration history:** The scene-local illustration records are authoritative for prompt lineage, outcomes, and approved outputs. The former cross-session catalogue was retired on 2026-11-20.

## Workflow
Each authored prompt is committed before its image-generation call. The image tool may not expose its compiled prompt; unless it does, this file records the exact authored direction, not a claim about hidden tool payload. Each result will be inspected and classified before the next attempt.

## Attempt 01 — Rain at the bookshop door

- **Status before call:** Pending.
- **Operation:** Fresh generation.
- **Mode:** Vintage — Painterly Storybook.
- **Source/reference:** No source image attached. Character appearances are provisional; Novel-01 does not establish fixed physical designs or wardrobe.
- **Moment:** The narrator has just stepped in from the rain; Maya is browsing beside the nearest bookshelf. This is the first visual beat of Scene 001.
- **Exact authored prompt:**

> Create a refined Vintage-mode painterly storybook illustration for a contemporary literary romance. Show the opening moment of Scene 001, “The Weather at the Window”: a small independent bookshop-café in a city during an early-evening downpour. The composition is a wide, atmospheric interior view from just inside the entrance. In the foreground, the first-person narrator has just stepped through the door, pausing to shake off the rain; show the narrator mostly from behind or in partial profile so their physical identity remains visually open. A few steps away, Maya, an adult woman with a natural, understated appearance and dark shoulder-length hair, stands beside the nearest bookshelf holding an open book. She has just made a dry, friendly remark about the wet floor and is beginning to look up toward the newcomer.
>
> Establish the specific shop described in the scene: shelves of books along one wall, a few modest wooden tables, a counter at the back, a crowded umbrella stand near the entrance, and broad front windows clouded at the edges. Outside, rain streaks the glass and blurs the street into soft reflections and passing lights. The atmosphere suggests coffee, damp paper, and something faintly sweet baking behind the counter. Let warm interior lamplight meet cool rainy blue-grey evening light at the window. The mood is observant, intimate, quietly witty, and entirely ordinary in the best sense: the first small opening between two strangers, not an exaggerated romantic pose.
>
> Render as a beautifully composed hand-painted literary illustration: delicate visible brushwork, tactile paper-and-gouache surface, nuanced natural anatomy, expressive but restrained faces, coherent perspective, a muted palette of warm amber, wood, ink blue, rain grey, and soft cream. Keep the scene visually specific and believable, with no text, lettering, captions, decorative borders, extra foreground characters, or melodramatic romantic symbols.

- **Specific test:** Establish the bookshop-café, rainy evening, first positions of Maya and the narrator, and a consistent painterly storybook visual language without canonizing the narrator's appearance.
- **Tool-prompt visibility:** Not yet known. The archived text is the authored direction.



### Attempt 01 result

- **Actual result:** One fresh image returned successfully.
- **Generation ID:** `10516b2d-1516-4f44-9ff5-e410846265e4`.
- **Conversation artifact:** `a_cozy_cinematic_painterly_illustration_of_a_rai.png` (delivered in this conversation; not committed to GitHub).
- **Observed match:** Rainy bookshop-café, warm interior against a cool wet street, Maya beside the shelves holding an open book, and the narrator entering with a rain-darkened coat. The umbrella stand and book-lined interior are visible.
- **Classification:** Partial match. The image is an attractive illustrated interpretation, but it leans toward polished anime-inspired digital art rather than the intended hand-painted literary storybook surface. It also adds decorative plants/flowers not specified in the scene and gives the narrator a masculine appearance that the novel has not established. Treat the character design as provisional, not canon.
- **Tool metadata:** Fresh generation; `edit_op: null`, `parent_gen_id: null`. The tool metadata's compiled prompt field was empty. The archived text is the authored direction, not a verbatim record of the tool's internal prompt.
- **Learning:** Use this first image only as a continuity reference for the next two illustrations, not as an edit source. Keep the same provisional character appearances and clothing, but return to the scene's understated, book-centred details.

## Attempt 02 — The book between them

- **Status before call:** Pending.
- **Operation:** Fresh generation.
- **Mode:** Vintage — Painterly Storybook.
- **Source/reference:** Attempt 01 image, generation ID `10516b2d-1516-4f44-9ff5-e410846265e4`, attached as a visual continuity reference only. This is not an edit.
- **Moment:** A book slips from the shelf and the narrator retrieves it; Maya approaches, and their first exchange becomes a conversation.
- **Exact authored prompt:**

> Create a new, separate illustration for Scene 001, using the attached first illustration only as a visual continuity reference. This is not an edit of that image. Preserve the same provisional appearance and clothing of both characters: Maya has dark shoulder-length wavy hair, a cream textured sweater, and a dark skirt; the narrator has short dark hair and a dark raincoat. Keep their faces and clothing consistent with the reference.
>
> Show the precise moment after a book has slipped from a crowded shelf and landed face-down beside the narrator's small wooden table near the rainy front window. The narrator has bent to pick up the book and is now holding it out toward Maya. Maya has stepped close from the bookshelf, reaching to accept it, with a small amused smile. Their eyes meet over the book; the exchange is lightly humorous and unforced, the first moment when two strangers choose to keep talking. Make the book the clear visual bridge between them. Include a coffee cup on the table and rain-streaked glass behind them. Keep the shop intimate and modest: bookshelves, wood, warm counter light, and a subdued background.
>
> Use a genuinely hand-painted storybook treatment with delicate brush texture, softly layered gouache-like color, natural anatomy, expressive restrained faces, and a tactile illustrated surface. The composition should be a medium two-shot at eye level, with both faces and the hands holding the book clearly visible. Warm amber interior light contrasts gently with cool rainy blue-grey window light. The mood is quiet curiosity, dry wit, and the first trace of connection. No captions, lettering, decorative border, extra people, dramatic romantic symbols, or unnecessary props.

- **Specific test:** Preserve the provisional visual continuity from Attempt 01 while illustrating the book handoff as the scene's first shared action.
- **Tool-prompt visibility:** Not yet known. The archived text is the authored direction.



### Attempt 02 result

- **Actual result:** One fresh image returned, but it was a nine-panel comic-page collage rather than the requested single book-handoff scene.
- **Generation ID:** `147173cd-0b03-4beb-849a-21ca86edaf2f`.
- **Conversation artifact:** `a_cinematic_anime_photorealistic_style_collage_co.png` (delivered in this conversation; not committed to GitHub).
- **Classification:** Generated but missed target. It contains several moments from the scene, but adds captions and invented dialogue, displays an invented phone number, and does not clearly depict the specific book handoff requested.
- **Tool metadata:** Fresh generation; `edit_op: null`, `parent_gen_id: null`. The compiled prompt field was empty. The archived authored direction was not exposed as the tool's compiled prompt.
- **Learning:** The next attempt must be a single image, not a collage or comic page; no captions, lettering, phone numbers, or invented dialogue. Keep the composition tightly focused on the book being returned to Maya.

## Attempt 03 — The book handoff, single scene

- **Status before call:** Pending.
- **Operation:** Fresh generation.
- **Mode:** Vintage — Painterly Storybook.
- **Source/reference:** Attempt 01, generation ID `10516b2d-1516-4f44-9ff5-e410846265e4`, attached as visual continuity inspiration only. Do not use Attempt 02 as a reference.
- **Moment:** The narrator returns the fallen book to Maya beside the table and rain-streaked window.
- **Exact authored prompt:**

> Create exactly one standalone illustration, not a comic page, storyboard, collage, diptych, or sequence of panels. Depict one precise moment from Scene 001: Maya and the narrator meet beside a small wooden table in the rainy bookshop-café. A book has just slipped from the crowded shelf and landed on the floor. The narrator has picked it up and is holding it out to Maya; Maya stands close to the shelf, reaching to accept the book. Their eyes meet over the book, and Maya has a small, amused smile. The book is the clear centre of their interaction. A single coffee cup rests on the table; the rain-streaked front window and softly lit bookshelves form the background.
>
> Use the attached first illustration only as a visual reference for the same provisional character designs: Maya's dark shoulder-length wavy hair, cream textured sweater, and dark skirt; the narrator's short dark hair and dark raincoat. Keep their appearance and clothing consistent, but create a completely new camera composition focused on the handoff.
>
> Render as a single hand-painted literary storybook illustration with visible delicate brushwork, layered gouache-like color, natural anatomy, restrained expressions, and a tactile painted surface. Medium two-shot at eye level; show both faces and the book clearly. Warm amber light inside, cool rainy blue-grey light outside. The feeling is a quiet, witty first connection between two strangers.
>
> Absolutely no panels, frames, captions, words, lettering, signs, numbers, phone numbers, speech bubbles, graphic-novel layout, decorative borders, extra people, or invented props.

- **Specific test:** Determine whether a single, text-free handoff composition can be produced while maintaining the provisional character design from Attempt 01.
- **Tool-prompt visibility:** The tool may not expose its compiled prompt. The full authored direction is also placed immediately before the generation call so the visual request is explicit in the active conversation.



### Attempt 03 result

- **Actual result:** One fresh image returned, again as a multi-panel comic collage rather than one standalone book-handoff illustration.
- **Generation ID:** `4cd49ffd-cedb-47c1-a30a-d71fcdd98667`.
- **Conversation artifact:** `a_cinematic_anime_style_high_detail_comic_manga.png` (delivered in this conversation; not committed to GitHub).
- **Observed match:** It retains the rainy bookshop setting, the same broad character styling, and several recognizable moments from Scene 001, including Maya with a book and the pair talking near the window.
- **Classification:** Generated but missed target. Despite the explicit single-image direction, the output is another multi-panel comic page. It adds invented handwritten wording (“Another day? :)”) and does not provide the requested focused book-handoff composition.
- **Tool metadata:** Fresh generation; `edit_op: null`, `parent_gen_id: null`. The compiled prompt field was empty, and source-reference linkage was not confirmed.
- **Learning / stop decision:** Two consecutive attempts returned comic-page collages despite explicit directions for a single image. Stop this generation sequence rather than submit more near-identical calls. The first standalone image remains the only single-frame illustration; the two collages are supplementary visual interpretations, not successful matches to their archived prompts.

## Attempt 04 — Maya listens across the book

- **Status before call:** Pending.
- **Operation:** Fresh text-to-image generation.
- **Novel scene:** [Scene 002 — A Place Between Pages](../novel/Novel-01/Arc-01/Scene-002/scene.md).
- **Mode:** Realistic — cinematic natural-light photography.
- **Source/reference:** No image attached. This was a fresh generation based on written character and wardrobe direction; it was not an edit or a source-attached generation.
- **Actual authored prompt sent to the image tool:**

> A realistic, photo-like café scene shows a young East Asian woman with fair skin and long, wavy dark-brown hair, wearing soft makeup and an ivory silk off-shoulder blouse. Resting her head on one hand, she smiles calmly toward a blurred dark-haired man in the foreground, while an open book and two foamy coffees sit on the wooden table amid warm lighting, shelves, café equipment, and a window overlooking soft greenery.

- **Specific test:** Establish Maya and the narrator at their second meeting, with the book and coffee as visual anchors.
- **Tool-prompt visibility:** The tool metadata did not expose a compiled prompt; the text above is the authored direction actually supplied to the tool.

### Attempt 04 result

- **Actual result:** One standalone fresh image returned.
- **Generation ID:** `19db6405-1197-4a6b-b2aa-fb803347f90f`.
- **Conversation artifact:** `sebuah_realistic_photo_like_scene_a_young_adult.png` (delivered in this conversation; not committed to GitHub).
- **Observed match:** A woman with long dark hair sits across from a blurred man in a café. An open book and two coffees are visible. The image uses warm natural light and a realistic photographic treatment.
- **Continuity assessment:** The ivory silk garment is broadly consistent with the canonical wrap direction, but the exact garment construction and Maya's exact facial identity cannot be verified from a written prompt alone.
- **Classification:** Partial match; fresh generation, not an edit. Do not mark as canon or approved. The missing visual identity check is an uncertainty, not a reason to block future prompt-based generation.
- **Tool metadata:** `edit_op: null`, `parent_gen_id: null`; compiled prompt field empty.

## Attempt 05 — A closer listening moment

- **Status before call:** Pending at the time of the call; archival sequencing error — this entry is being documented retrospectively because the second generation call was made before its own prompt was committed.
- **Operation:** Fresh text-to-image generation.
- **Novel scene:** [Scene 002 — A Place Between Pages](../novel/Novel-01/Arc-01/Scene-002/scene.md).
- **Mode:** Realistic — cinematic natural-light photography.
- **Source/reference:** No image attached. Fresh generation from written direction; not an edit and not reference-attached.
- **Actual authored prompt sent to the image tool:**

> In a warm, cinematic café setting, a softly backlit young woman with long, dark hair leans her cheek into her hand while listening affectionately to a blurred man across the wooden table; her ivory satin off-shoulder blouse, natural makeup, and gentle smile complement the intimate, shallow-focus mood. An open book, two latte-filled cups, and a small vase of white flowers sit nearby, while window light, bokeh, and a softly blurred urban café interior create a romantic, film-like atmosphere.

- **Specific test:** Create a slightly wider and more cinematic version of the second-meeting composition.
- **Tool-prompt visibility:** The tool metadata did not expose a compiled prompt; the text above is the authored direction actually supplied to the tool.

### Attempt 05 result

- **Actual result:** One standalone fresh image returned.
- **Generation ID:** `e6adc238-556f-4e87-87e1-ab26ef001cfc`.
- **Conversation artifact:** `a_warm_cinematic_photorealistic_scene_in_a_cozy.png` (delivered in this conversation; not committed to GitHub).
- **Observed match:** Maya-like woman with long dark hair sits opposite a blurred man; an open book, two coffee cups, and a café window are visible. The result is photorealistic with warm window light and a wider table composition.
- **Continuity assessment:** The ivory satin garment is broadly consistent with the canonical wrap direction, but exact garment construction and facial identity remain unverified without a visual identity reference. Do not mark as canon or approved.
- **Classification:** Partial match; fresh generation, not an edit.
- **Tool metadata:** `edit_op: null`, `parent_gen_id: null`; compiled prompt field empty.
- **Learning:** Prompt-only generation is a valid workflow and should not be blocked by the absence of an attached portrait. However, exact identity fidelity cannot be certified from text-only generation; preserve the canonical face and outfit wording literally and inspect every output carefully.

## Attempt 06 — Maya across the café table

- **Status before call:** Pending.
- **Operation:** Fresh text-to-image generation.
- **Novel scene:** [Scene 002 — A Place Between Pages](../novel/Novel-01/Arc-01/Scene-002/scene.md).
- **Mode:** Realistic.
- **Source/reference:** No image attached. Fresh generation; not an edit and not source-attached.
- **Actual authored prompt sent to the image tool:**

> In a warmly lit, cinematic café, Maya—a young East Asian woman with fair skin, long dark hair, subtle makeup, and pearl-drop earrings—rests her cheek on her hand and gazes playfully and affectionately at the narrator, her ivory satin wrap slipping elegantly from one shoulder. Across from her, the slightly blurred man in glasses and a dark shirt leans into their conversation, while latte-filled cups, a vase of delicate white flowers, and a closed dark book sit on the wooden table amid cozy shelves, soft bokeh, and greenery beyond the window.

- **Specific test:** Depict Maya and the narrator during their second café meeting.
- **Prompt-discipline note:** The actual call did not use the archived Attempt 06 canonical-identity prompt above it. The sent wording was materially shorter and introduced unverified details (pearl-drop earrings and glasses on the narrator). This is an assistant execution error, not a change to the user's canon.
- **Tool-prompt visibility:** The tool metadata did not expose a compiled prompt; the text above is the authored direction actually sent.

### Attempt 06 result

- **Actual result:** One standalone fresh image returned.
- **Generation ID:** `01da3cef-08f5-45ae-8bf4-96ef7773b5fb`.
- **Conversation artifact:** `a_cozy_cinematic_café_scene_with_a_romantic_inti.png` (delivered in this conversation; not committed to GitHub).
- **Observed match:** A long-haired woman in an ivory satin off-shoulder wrap-like garment sits across from a man wearing glasses; a closed book, two cups, and a vase of flowers are on the table.
- **Misses:** The scene text has an open book and no established glasses for the narrator; the image adds background people and props. Exact facial identity and exact garment construction are not verifiable from the text-only generation.
- **Classification:** Generated but missed target / partial visual match. Not approved canon.
- **Tool metadata:** `edit_op: null`, `parent_gen_id: null`; compiled prompt field empty.
- **Learning:** The authored prompt must be copied faithfully into the actual generation call. Do not add unestablished accessories, physical traits, or props. A written canonical prompt remains a valid basis, but prompt execution must preserve its exact locked identity and wardrobe instructions.
