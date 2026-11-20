---
name: drawing
description: "Create and refine images in two deliberate visual modes: Realistic and Vintage. Use for image generation, editing, style transformations, composition, character continuity, and iterative visual refinement."
created: 2026-11-18T13:18
updated: 2026-11-20
---

# Drawing Skill

## Purpose

This skill provides two distinct drawing modes:

1. **Realistic Mode:** lifelike, photographic rendering.
2. **Vintage Mode:** nostalgic, crafted rendering with painterly, illustrated,
   traditional-media, or selected retro-print character.

These are different visual targets, not quality levels. Neither is the universal
default.

Mode and visual treatment are session-specific. A mode selected in an earlier
drawing session does not carry into a new session unless the new session brief
explicitly continues or adopts it. The active session-opening brief governs.

## 1. Mode selection and persistence

Accept direct commands:
- `Realistic mode` / `Switch to realistic`
- `Vintage mode` / `Switch to vintage`

Apply the selected mode immediately to subsequent drawing work within the same
specific drawing session. A new drawing session starts from its own opening
brief, even when it begins in the same conversation or continues the same
project. Do not silently switch modes because a prompt is difficult or an
earlier result failed.

When the current session brief does not name a mode:
1. Infer it from the visual language the user specifies in that session.
2. Use a mode visible in a reference only when the user assigns that image as a
   style reference for this session.
3. If the choice would materially change the result and the session brief does
   not resolve it, ask one short question: **Realistic or Vintage?**
4. Do not inherit a mode from an earlier drawing session without the user's
   explicit direction in the current session.

If the user requests a hybrid, establish which mode should dominate. Do not blur
the distinction so far that the result becomes neither.

## 2. Realistic Mode

**Visual objective:** a convincing lifelike image with photographic visual
logic. The output should read as a photograph or natural cinematic capture,
not an illustration.

### Rendering principles
- Natural, physically plausible lighting, shadows, reflections, and depth.
- Believable anatomy, body weight, posture, hands, and contact between subjects.
- Realistic skin, hair, fabric, glass, metal, and environmental texture.
- Coherent lens perspective, focus, depth of field, and camera framing.
- Natural color response and restrained retouching.
- Expressions and gestures should feel observed rather than artificially posed.
- Preserve supplied character features and visual continuity.

### Useful prompt language
Use terms such as photorealistic, natural photographic realism, realistic skin
and fabric texture, physically plausible warm window light, natural lens
perspective, restrained depth of field, candid, cinematic, editorial, or studio
photography as appropriate. Choose only the vocabulary that serves the brief.

### Avoid unless requested
Brush strokes, canvas grain, watercolor blooms, pencil hatching, ink outlines,
paper aging, illustration contours, plastic-looking skin, excessive HDR,
synthetic gloss, or artificial bokeh.

## 3. Vintage Mode

**Visual objective:** an image with a sense of age, craft, warmth, or artistic
memory. Vintage does **not** mean sepia by default, nor does it require a
specific historical period. Choose a treatment that fits the request.

### Core principles
- Visible material character: delicate brushwork, watercolor texture, gouache
  layering, oil-paint handling, pencil grain, print texture, or another
  appropriate medium.
- A coherent, restrained palette. Warm ivory, muted rose, amber, faded blue,
  earthy tones, and gentle pastels are options, not mandatory ingredients.
- Soft transitions, tactile surfaces, and subtly simplified forms.
- Nostalgic atmosphere without losing facial expression or anatomy.
- Important details remain legible. Texture must not obscure eyes, hands,
  fabric boundaries, or the direction of a gesture.

### Vintage treatments
Choose one dominant treatment per image unless a mixed-media result is requested:

- **Painterly storybook:** soft hand-painted forms, delicate brush texture,
  warm light, gentle natural simplification.
- **Classic oil painting:** layered pigments, tonal depth, controlled brushwork.
- **Watercolor:** transparent washes, soft edges, luminous paper, restrained line.
- **Gouache illustration:** opaque matte color, simplified shapes, tactile surface.
- **Vintage editorial illustration:** elegant drawing, limited palette, print-like
  texture and intentional silhouettes.
- **Retro print:** screenprint, lithograph, halftone, or restrained ink texture.
- **Analog-photo vintage:** film grain, faded color response, and period-informed
  photographic treatment. Use when the user wants a vintage photograph rather
  than a painting.

### Possible prompt language
When compatible with the active session brief, useful terms include softly
hand-painted digital illustration, delicate visible brush texture, warm
painterly shading, natural gently simplified forms, refined storybook realism,
or nostalgic lighting. Select the palette from the active brief; cream and
amber are optional, not defaults.

Warm lighting alone is not enough to make an image Vintage. The rendering
itself must show an illustrative, painterly, print, or analog character.

### Avoid unless requested
Automatic sepia, brown wash, fake cracks, heavy scratches, artificial yellowing,
or distressed paper. Do not confuse Vintage with cartoon, anime, caricature, or
exaggerated facial proportions. Avoid random mixtures of watercolor, oil, comic
ink, and 3D gloss.

## 4. Workflow for every drawing task

### Skill-loading cadence

The Drawing Skill is universal: its rules govern every drawing project,
regardless of subject, scene, or project switch. A project change does not make
the skill new and does not, by itself, require another retrieval.

At the beginning of each new ChatGPT conversation/session, after loading the
foundational session skills, retrieve the current Drawing Skill and its required
supporting references from the `gpt` branch. Keep the verified instructions
in working context and apply them to every drawing project throughout that
conversation. **Do not reread or refetch the full Drawing Skill merely because
the user switches projects or starts another drawing task within the same
conversation.**

Refresh the skill and its supporting references if the user asks for an
instruction refresh, if a relevant repository change is known or suspected, or
if newly introduced work depends on a supporting reference that has not yet
been read. A new ChatGPT conversation requires a fresh retrieval even when it
continues an existing project, so the new conversation starts from the current
repository version.

This session-level loading cadence does not reduce any per-attempt requirement
below. Before each generation or edit, review the relevant prompt history,
prepare and commit the exact authored prompt, verify that commit, then generate
or edit and record the actual outcome.


### A. Read the brief and complete the session-brief preflight

Identify the subject, selected mode, composition, camera/viewpoint, orientation,
character appearance, clothing, expression, pose, exact spatial relationships,
lighting, environment, mood, and what must remain unchanged in an edit.
Separate essential requirements from optional decorative details.

**Session-specific direction authority — the opening brief governs this drawing session:**

The user's opening brief for a specific drawing session is the source of truth
for its creative direction. This applies equally to a day-drawing session and a
novel-illustration session. No repository-wide image index, past portrait,
previous prompt, character sheet, successful image, or old project convention
automatically dictates the current session's face, identity, outfit, scene,
pose, style, palette, mood, setting, or composition.

1. At the start of each distinct drawing session, identify the user's opening
   vision and treat it as the active brief. Preserve the user's wording and
   distinguish what is explicitly specified from what remains open for creative
   choice. Do not turn unstated details into permanent locks.
2. For non-novel/day drawing, use the session brief stored under
   `prompts/YYYY-MM-DD/session-[NN]-brief.md`. For a named novel scene, use the
   scene-local session brief under
   `novel/[Novel-ID]/[Arc-ID]/[Scene-ID]/illustrations/session-[YYYY-MM-DD]-[NN]-brief.md`.
   The authoritative storage and verification procedure is in
   `skills/session-archiving/SKILL.md`.
3. A session brief records the intended subject/theme, scene or moment, mode,
   character appearance, outfit, pose, framing, environment, lighting, mood,
   continuity requirements, locked features, permitted variation, exclusions,
   and any visual references the user explicitly assigns to this session.
   Mark unspecified fields as open/not specified; never invent a lock.
4. Later explicit user instructions within the same session amend the active
   brief for the named property. Preserve the original opening brief and append
   the amendment to the session record; do not silently rewrite history.
5. A new drawing session starts with a new brief, even when it belongs to an
   existing project, character, novel, or series. Reuse earlier work only when
   the current brief explicitly continues that series or adopts those details.
   Even then, the current session brief overrides any conflicting older prompt
   or image.
6. For novel illustrations, scene text and novel records provide narrative
   facts only to the extent the user asks the image to follow or adapt them.
   They do not independently dictate visual design. The session-opening brief
   determines which moment, interpretation, appearance, outfit, mood, and
   visual treatment are wanted.
7. Use an uploaded or stored image as a reference only when the user assigns it
   a role in this session (identity, composition, style, or exact edit source).
   A historical image is not an active reference merely because it is stored,
   linked, approved, or previously used. A generation ID or filename is not an
   attachment.
8. If a current-session brief conflicts with a successful historical prompt,
   preserve the user's current brief and use the old prompt only as a technical
   wording aid for compatible details. Do not import its outdated appearance,
   clothing, setting, framing, or style.

The session brief—not a global image catalogue—is the visual authority.

### B. Establish the visual hierarchy
Order prompts by importance:
1. Main subject and defining pose/action.
2. Relative positions and spatial relationships.
3. Character continuity and clothing.
4. Critical hands, facial expression, and contact points.
5. Environment and composition.
6. Selected mode and rendering treatment.
7. Decorative details and exclusions.

For difficult poses, describe body geometry in plain spatial terms. State who
is upright, reclining, leaning, holding, or resting. Explicitly say which
direction must not be reversed.

For hands, identify the person, left or right hand, action, location, and which
hand is above or below. Avoid vague phrases such as "hands together" when exact
placement matters. Make the complete hands and wrists visible when they are
essential to the picture.

### Generated-output storage

For non-novel/day drawing sessions, store repository-retained generated image outputs in the current daily session folder at `drawings/YYYY-MM-DD/images/`. Use `attempt-XX.webp` for one output from an attempt, and `attempt-XX-01.webp`, `attempt-XX-02.webp`, etc. when an attempt returns multiple images. Deliver images in the conversation as usual. When the exact output asset is stored in the repository, link it from the attempt record and daily README using a relative path such as `images/attempt-07.webp`. Only link assets whose attempt provenance is verified. Do not create empty image folders solely for rejected or output-less attempts. This policy applies to new retained outputs; it does not authorize migrating, moving, renaming, or deleting existing image assets. Novel-scene illustration binaries continue to use their established scene-local asset library.

### C. Prepare and archive the prompt
Before every generation or edit attempt:
1. Follow `skills/session-archiving/SKILL.md`.
2. Read the active session-opening brief first. For a named novel scene, also
   read the relevant scene-local scene and illustration records; for non-novel
   work, read the session brief under `prompts/YYYY-MM-DD/`. The session brief
   governs visual direction; scene records supply narrative facts only where the
   brief asks the illustration to follow or adapt them.
3. Review the relevant daily attempt ledger at
   `drawings/YYYY-MM-DD/README.md` and the chronological prompt history for the
   same session and, when the user explicitly continues a series, that series'
   history. Use the ledger only to locate candidate attempts. Verify every
   candidate's series membership, outcome, approval, and prompt/output linkage
   in its authoritative attempt record. For a novel scene, use the
   scene-local illustration records. Do not consult or recreate a global
   image-reference index.
4. Select the most recent successful prompt in the active series as the
   historical text baseline, or the most recent successful prompt in the exact
   artwork thread if no series applies. Newer failures remain diagnostic only.
   The active session brief has higher authority than every historical prompt:
   adapt the baseline to the current brief and omit or replace every conflicting
   feature. If no relevant success exists, draft from the current session brief
   and the user's explicit constraints; do not borrow a prompt from an unrelated
   series.
5. Derive normally three to five observable acceptance criteria from the active
   session brief for this specific image. Identify critical requirements whose
   failure prevents a successful-match classification. Do not invent criteria
   or turn unspecified details into requirements.
6. Record the prompt difference in four explicit fields:
   - **Baseline:** exact successful prompt path/attempt, or `none / first attempt`.
   - **Preserved:** details carried forward from the baseline and active brief.
   - **Changed:** details deliberately modified, with the user instruction that
     authorizes each change.
   - **Excluded:** details deliberately not carried forward, with the reason.
   For a first attempt with no baseline, state that and map the prompt directly
   to the opening brief.
7. Record the exact authored prompt, operation type, source, mode, acceptance
   criteria, prompt difference, test objective, pending status, and every
   reference asset actually attached.
8. Commit the prompt to branch `gpt`.
9. Fetch and verify the committed prompt before calling the image tool.

For every illustration belonging to a named novel scene, keep a convenient
scene-local prompt record beside its illustration note:
`novel/[Novel-ID]/[Arc-ID]/[Scene-ID]/illustrations/illustration-[NN]-prompt.md`.
Create and commit this file before generation. For novel illustrations, this
scene-local file is the authoritative prompt and attempt record; keep all
novel-specific prompt history inside the novel and do not duplicate it in the
root `prompts/` folder. Link the local prompt from the illustration note and
scene record where practical. Do not replace one
with the other.

The scene-local record must preserve the exact authored prompt, operation
type, generation/edit identifier when available, source/reference details,
and the chronological sequence of attempts for that illustration. After the
image call, update the local record with the actual direction submitted when
known, outcome, deviations, and continuity assessment. Distinguish the authored
prompt from the tool's compiled or internally submitted payload. If the tool
does not expose its submitted payload, say so; never claim the authored text
is verbatim internal wording.

The authored prompt is not necessarily the tool's compiled prompt. If the tool
does not expose its submitted payload, say the archive records the authored
direction rather than claiming it is verbatim internal wording.

### D. Use image references honestly

A fresh text-to-image generation may be based on a written specification
contained in or explicitly adopted by the active session brief; an attached
image is not mandatory unless the user specifically requests a visual
reference or an exact edit of that image. Do not inherit a previous session's
canonical prompt or identity/wardrobe specification as current direction
unless the user explicitly adopts it in this session.

When an image is used, determine whether it is for identity, composition, style,
or an exact edit source. Pass the actual image asset or reference ID through the
image tool's supported reference mechanism. Merely naming a filename or image
ID in prompt text does not attach it.

Never claim an image was edited or reference-guided if the tool returned a
fresh generation or did not confirm source linkage. Check metadata and inspect
the result. If the user specifically requires source linkage and the tool cannot
accept or retain the source, state that limitation. Do not turn optional
reference attachment into a blocker for ordinary fresh generation.

### Series identity, membership, and prompt lineage

A **series** is a connected body of image-making organized around a shared creative theme or deliberate curatorial premise. The theme is the series' creative spine: it explains why these images belong together and what each new image is meant to explore, extend, revisit, or vary. It may be narrative, conceptual, emotional, relational, cultural, visual, subject-led, or editorial. A series need not be chronological and need not preserve the same character, location, outfit, or rendering style.

A recurring attribute alone does **not** establish a series. The same character, outfit, palette, medium, location, camera angle, subject category, or image format may simply be a reusable feature appearing in unrelated work. It becomes a series-defining principle only when the user declares it as the organizing concept or the images deliberately explore that feature as a coherent theme or collection. For example, several images that happen to use the same character are not automatically one series; a character study exploring that character across distinct moments is. Likewise, a shared palette becomes a series premise when the palette itself is the deliberate subject of a visual study or collection, not merely because the same colors recur.

**Series-first baseline rule:** When continuing a series, inspect its newest attempt to understand the latest context, corrections, and outcome—but build the next authored prompt from the most recent successful prompt in that same series. This keeps the work aligned with the series' current creative direction without allowing a newer failed, partial, or rejected attempt to replace the proven prompt. A later successful prompt in the same series supersedes the earlier successful baseline by chronology.

#### A. What can define a series

The following taxonomy is deliberately broad. These are possible organizing premises, not automatic classifications based on a feature's mere presence. A series may combine several types or use another coherent theme not listed here.

1. **Character or identity series:** the same person, fictional character, avatar, creature, or recognizable identity across different images.
2. **Relationship series:** a couple, family, friendship, rivalry, group, or recurring interpersonal dynamic.
3. **Narrative or story series:** chapters, episodes, scenes, story beats, alternate moments, or different viewpoints within a narrative.
4. **World or universe series:** a shared fictional world, setting, lore, civilization, mythology, rules, or imagined reality.
5. **Thematic or conceptual series:** a central idea such as intimacy, solitude, freedom, memory, identity, belonging, mortality, or transformation.
6. **Emotional series:** an emotional experience or spectrum such as tenderness, longing, confidence, vulnerability, grief, joy, or peacefulness.
7. **Subject series:** a recurring subject or subject class, such as a particular animal, flower, vehicle, building, object, or type of person.
8. **Location or environment series:** one room, home, building, city, landscape, destination, natural environment, or architectural space explored through different images.
9. **Situation or context series:** a recurring circumstance, such as quiet mornings, evenings at home, travelling, waiting, reunions, or conversations in a café.
10. **Visual-style or medium series:** a shared artistic language, such as cinematic realism, painterly storybook imagery, watercolor, oil painting, analog photography, or a defined illustration style.
11. **Color, light, or atmosphere series:** a recognizable palette, tonal range, lighting language, season of light, or atmospheric treatment.
12. **Wardrobe, fashion, or costume series:** a fashion collection, outfit study, character wardrobe, uniform family, historical dress, or intentionally fixed garment design.
13. **Motif or symbolism series:** a recurring object, symbol, visual metaphor, gesture, pattern, or compositional motif.
14. **Activity, occupation, or ritual series:** recurring actions, hobbies, professions, routines, sports, crafts, performances, or ceremonies.
15. **Seasonal or temporal series:** seasons, times of day, stages of a year, recurring dates, or the passage of time.
16. **Life-stage or transformation series:** growth, aging, changing appearance, personal development, metamorphosis, or symbolic transformation.
17. **Historical or cultural series:** a historical period, culture, civilization, tradition, festival, or cultural interpretation.
18. **Event or occasion series:** a wedding, celebration, journey, festival, concert, performance, or other event documented or reimagined through multiple images.
19. **Editorial, brand, or campaign series:** magazine spreads, advertising campaigns, promotional artwork, posters, identity systems, or coordinated brand imagery.
20. **Format or genre series:** recurring book covers, portraits, character sheets, postcards, illustrations, posters, comics panels, or another defined image format.
21. **Composition or photography-language series:** a recurring camera viewpoint, framing, lens character, perspective, posing language, shot type, or lighting arrangement.
22. **Technical or artistic study series:** controlled explorations of anatomy, gesture, fabric, reflections, lighting, materials, rendering, perspective, or other techniques.
23. **Comparison or variation series:** alternatives, parallel interpretations, before-and-after images, controlled A/B variations, or deliberate visual contrasts.
24. **Collection or catalogue series:** a curated body organized around a meaningful subject, class, taxonomy, or collecting principle, even without narrative continuity.
25. **Hybrid or cross-disciplinary series:** a deliberate combination of two or more of the above, or a coherent theme crossing disciplines, genres, media, or subject categories.
26. **Other user-defined series:** any other recurring creative premise the user identifies or the work demonstrably develops.

Use this cohesion test when membership is inferred rather than explicitly declared:

1. **Theme test:** Can the shared premise be stated in one clear sentence without merely listing common attributes?
2. **Purpose test:** Does each image contribute to, interpret, or deliberately vary that premise?
3. **Boundary test:** Can the series be distinguished from other work that happens to share a character, style, outfit, palette, location, or format?

If the answers are unclear, do not force a series classification. Record the work as provisional or standalone/unassigned. The user may explicitly define even a one-image beginning as a series seed; do not require multiple images when the user has declared the intended series.

#### B. How to recognize and classify a series

A series may be established in any of these ways:

- **Explicitly declared:** the user names it, calls the work a series, identifies its theme, or says that a new image belongs to an existing series.
- **Clearly continued:** the user asks to continue the same storyline, character journey, collection, campaign, visual study, or recurring theme. A shared project folder, character, or prior subject alone is not enough; the current request must continue the same organizing premise.
- **Contextually evident:** multiple prompts or images share a distinctive central premise and the user is developing variations of that premise.
- **Proposed by the assistant, confirmed by the user:** the assistant notices a coherent recurring theme, but must not silently impose a series label when that classification would affect prompt selection or continuity.

Do not require a minimum number of images when the user has explicitly declared a series. Without an explicit declaration, one image alone is normally insufficient evidence of an established series; it may be the first entry or a standalone image. Two or more related entries can reveal an implicit series when their shared theme is clear.

For each series, identify and record where available:

- **Series name or ID:** a stable, concise identifier. Do not invent a formal title when the user has not named it; use a neutral working label.
- **Theme spine:** the central idea that explains why the images belong together.
- **Series type:** one or more categories from the taxonomy above.
- **Primary continuity anchors:** the features that must persist, such as character identity, relationship, world rules, defining motif, subject, mood, or visual language.
- **Permitted variation:** what may change from image to image, such as scene, action, pose, framing, secondary subjects, time, location, or style.
- **Continuity strength:** strict, flexible, or thematic. Strict series preserve specified identity/world/design features; flexible series preserve core anchors while allowing substantial variation; thematic series preserve the underlying idea without requiring the same subjects or visual treatment.
- **Parent or related series:** record this only when the work is genuinely a branch, spin-off, crossover, or companion series.

When archiving a prompt, include its series name/ID, theme spine, and whether it is a continuation, a new entry, a branch, a crossover, or standalone. If the series is not known, record it as unassigned/standalone rather than guessing. A series may be renamed without changing its underlying lineage; preserve the previous label as an alias where useful.

#### C. Boundaries, overlap, and branching

- **Project versus series:** a project is an organizational container and may contain several distinct series. Do not treat every image in one project as belonging to one series.
- **Series versus sequence:** a sequence is ordered by chronology, process, or narrative progression. A series may be non-linear; a sequence can be one form of series when it has a shared theme.
- **Series versus collection:** a collection groups items by curation or category. It becomes a series in this workflow when a recognizable creative premise connects the images, but a collection need not imply visual or narrative continuity.
- **Series versus reusable style:** using the same mode, technique, palette, or character does not merge otherwise unrelated series.
- **Subseries:** a narrower theme may sit inside a parent series. Preserve both identities and use the subseries as the primary prompt lineage when the current request clearly belongs to it.
- **Branch or spin-off:** create a related branch when a new direction grows from an existing series but develops its own distinct theme. Record the parent relationship and the branch point. Do not keep using the parent series' newest prompt once the branch has established its own successful prompt lineage.
- **Crossover:** an image may intentionally combine two series. Record one as the primary series for prompt-baseline selection and the other as a secondary membership. Do not blend their prompt histories indiscriminately.
- **Series change:** if the central theme changes enough that the previous images no longer explain the new work, start a new series or branch rather than forcing continuity.
- **User authority:** the user's explicit grouping, separation, naming, or reassignment overrides assistant inference. Do not merge, split, or rename a series against the user's direction.

One image can have multiple thematic connections, but every prompt used for an iteration must have one **primary series** (or be explicitly standalone). Use that primary series to select the prompt baseline. Secondary tags help retrieval; they do not authorize borrowing a baseline from an unrelated series.

#### D. Choosing the correct prompt within a series

Apply this order whenever an image belongs to an established series:

1. **Read the active session brief first.** Confirm what the user wants in this
   session, which details are locked, and what may vary. Identify a primary
   series only when the current brief explicitly continues or adopts it; do not
   infer creative authority from project membership or a shared character.
2. **Locate the most recent successful prompt in that series.** Determine recency from the authoritative chronological attempt records, not from the order of entries in the success index. The prompt must have a reliable link to an output recorded as successful.
3. **Use that most recent successful prompt as a historical text baseline.**
   Carry forward only the wording and details that are compatible with the
   active session brief. The session brief outranks the historical prompt and
   overrides any conflicting face, identity, outfit, scene, pose, mood, style,
   palette, setting, or composition. Do not use a later failed, rejected, partial,
   or missed-target prompt as the base merely because it is newer.
4. **Inspect later unsuccessful attempts only as diagnostics.** They can reveal what failed, what the user corrected, and what specific change the user still wants. Extract only explicit user-requested or user-approved changes, then apply those deltas to the most recent successful prompt. Do not copy assistant-added wording, speculative embellishments, or failed prompt structure simply because they appeared later.
5. **A partial result does not displace the successful baseline.** Preserve useful visual observations from it, but build the next authored prompt from the most recent successful prompt. Promote a partial result to a successful series result only when the user explicitly accepts it as successful for the intended purpose; record that user decision and its exact originating prompt.
6. **Separate prompt success from image approval.** A user-approved image is a valid visual keeper or reference. It also establishes a successful prompt baseline only when its originating attempt is reliably identified and the user's approval clearly accepts that attempt/result as successful for the requested purpose. If the image-to-prompt mapping is uncertain, use the image only as a visual reference or edit source; do not invent or infer its prompt.
7. **Respect prompt lineage within branches.** A new subseries or spin-off may inherit the parent's most recent successful prompt as its initial seed at the moment the branch is created. Record that seed and branch point. Once the branch has its own successful prompt, use the branch's most recent successful prompt—not later prompts from the parent series.
8. **Handle a series with no successful prompt honestly.** For its first entry,
   use the active session brief and any visual references explicitly assigned
   within that session. For a new branch with no success of its own, use its
   documented parent-series seed only if the user has explicitly derived the
   branch from that parent and the seed does not conflict with the session brief.
   Do not borrow a successful prompt from an unrelated series.
9. **For work that is not a series, preserve artwork continuity.** If the user is iterating on one standalone image or artwork thread, use the most recent successful prompt for that exact thread. Do not treat the word "standalone" as permission to search across unrelated projects for a loosely similar prompt.
10. **Keep crossover lineage explicit.** A crossover has one primary series for baseline selection and one or more secondary memberships. Use the primary series' most recent successful prompt as the text baseline and carry secondary-series requirements as constraints. If no primary series is clear and the distinction materially changes the prompt, ask one focused question.
11. **Match the baseline to the operation.** The newest successful prompt in the active series remains the latest-success anchor. Use it directly when its operation and scope fit the next task. If it is a localized edit or style-only prompt that cannot serve as a full-scene prompt for a new generation, use the most recent successful full-generation prompt from the same series as the full-scene text skeleton, and carry forward only later successful, user-approved details that remain
   compatible with the active session brief. Record both prompt references and why the older full-scene skeleton is necessary. This is an operation-compatibility exception, not permission to use a failed prompt or borrow from another series.
12. **Keep exact edits separate from prompt baselines.** When the user requests a visual edit of a specific successful image, the actual image is the edit source if it is accessible and can be attached through the supported mechanism. The successful prompt remains useful context, but it does not replace the source image. Conversely, an image filename or generation ID is not an attached source.
13. **Honor explicit user selection.** If the user names a particular successful prompt as the baseline, use it after verifying the record. If the user names an image as the visual/edit baseline, use that image for the requested role when it is actually available; do not mislabel it as a prompt.
14. **Resolve ambiguity proportionately.** If series membership or the primary branch is genuinely unclear and would materially alter baseline selection, ask one focused question. Otherwise use the clearest context, record provisional membership, and proceed.

The controlling rule is: **the newest successful prompt in the active series is the baseline; newer unsuccessful prompts are evidence, never the baseline.** Preserve the series' evolving creative spirit by applying only the requested changes to that successful foundation. Keep every unmentioned locked feature unchanged.

### Session closeout cue

Do not close, finalize, or archive a drawing session as complete on the
assistant's initiative. The user's explicit cue is **`end session`**.

Treat the cue as invoked only when the user sends `end session` as a direct,
standalone instruction (case-insensitive; surrounding punctuation is harmless).
A quoted mention, question about the cue, or discussion of the phrase is not an
invocation. A pause, goodbye, topic change, last image, or beginning of another
session does not substitute for it.

Until the cue is given, keep the session status Active or Paused and preserve
its open state. Create each new session as Active; when a new distinct brief
supersedes an open session, mark the previous session Paused and the new one
Active. When resuming a Paused session, make it Active and pause any other
currently Active session.

When the cue is given, close the current drawing session under discussion,
whether Active or Paused, by following `skills/session-archiving/SKILL.md`.
If multiple open sessions could reasonably be the target, ask one concise
question to identify the session before changing any record; do not ask for a
second approval once the target is clear. Do not generate another image as part
of closeout unless the user separately requests it.

### Default iteration rule — build on proven success without redundant generation

**Do not generate a new image merely to edit it immediately afterward. Choose the
next operation based on what actually succeeded: the prompt, the image, or both.**

1. Identify the active series or exact artwork thread. Locate its most recent
   successful prompt and result first. Inspect any newer attempts for corrections
   and diagnostic evidence, but do not treat a failed or partial prompt as the
   baseline.
2. **Successful prompt, scene/detail change:** Reuse the proven prompt as the
   baseline. Make the requested targeted prompt changes and generate directly.
   Do not create an unnecessary intermediate image.
3. **Successful image, exact visual modification requested:** If the actual image
   is accessible and can be passed through a supported image-reference/edit
   mechanism, edit that source directly. This avoids needlessly regenerating an
   image that already works.
4. **Successful prompt but source image unavailable for editing:** Keep the proven
   prompt as the baseline, apply the requested changes to it, and make a fresh
   generation. Do not pretend the unavailable image is being edited.
5. **Unsuccessful prompt or image:** Diagnose the precise miss. Keep the most
   recent successful prompt in the active series/artwork thread as the text
   baseline. Apply only the required correction to that baseline; do not build
   the next prompt by editing the failed prompt itself.
6. **Multiple attempts within a series:** The most recent successful prompt in
   that series is the only default text baseline. A newer failed, rejected,
   partial, or missed-target prompt is diagnostic context only. Extract a change
   from it only when the user requested or approved that change, then apply the
   change to the successful baseline. Never make the failed prompt the base.
7. **Image-source verification:** A generation ID, filename, local path, archived
   note, or textual mention is not an image attachment. Use a direct edit only
   when the exact source is accessible and can be supplied through a supported
   image-reference mechanism. Verify the actual source asset and record what was
   attached.
8. **Provenance:** After an edit, inspect returned operation and parent/source
   metadata. If source linkage is not confirmed, classify it as a fresh
   generation or an unconfirmed-source operation—not a confirmed edit. Similar
   appearance does not prove linkage.
9. **Archive before the operation:** Record the exact authored prompt, operation
   type, source/reference actually attached, intended change, and pending
   status. Commit and read-back verify before generation or editing. Afterward,
   record the actual result and deviations. Distinguish authored prompt text
   from tool-compiled/submitted text if the latter is unavailable.

The guiding principle is **reuse proven success efficiently**: when the prompt
already works, change the prompt directly; when the image already works and
needs a visual alteration, edit it directly if the real source is available.
Use fresh generation only when it is the appropriate next step—not as a
redundant intermediate.

### E. Generate or edit
Use one dominant mode consistently:
- Realistic: photographic rendering vocabulary and physical plausibility.
- Vintage: a selected traditional or illustrative medium and its texture.

For edits, identify the one intended change first. Explicitly freeze composition,
subjects, pose, wardrobe, hands, lighting, and background as needed. Do not
introduce unrelated improvements.

If repeated attempts fail the central requirement, change the method, reduce
the scope, or stop and explain the limitation instead of repeating near-identical
prompts.

### E2. Refusal-aware recovery and retry ownership

A tool refusal must not automatically become a request for the user to rewrite the prompt.

1. Read the refusal as a result, not as an invitation to resubmit the same prompt.
2. Check the actual request and authored prompt for explicit nudity, erotic activity, sexual solicitation, or combinations of wording and staging that make the image overtly sexual.
3. If the user's underlying creative goal has a clearly non-explicit interpretation, preserve that goal while making a material change to the visual treatment. For example, move from bedroom/boudoir staging to a fashion or portrait setting; use ordinary elegant clothing; describe posture, expression, lighting, and composition without erotic instructions.
4. Do not use euphemisms to disguise a prohibited request, and do not try to defeat or probe safety systems. The revision must genuinely change the content into an allowed depiction.
5. Archive and commit the revised prompt before another call. Record each refusal and each materially revised attempt accurately.
6. After a refusal, make one meaningful autonomous revision when the safe intent is clear. If that safer version is also refused, do not continue with near-identical safety rewrites. However, first complete the prompt-interpretation audit in E2.1. If that audit reveals that the assistant itself materially drifted from a relevant, previously successful prompt, one bounded restoration of that proven baseline may be justified as a distinct diagnostic test. This is not permission for unlimited retries or for reproducing prohibited content.
7. Do not ask the user to say “retry” or write a new prompt when the intent is already clear. Ask only when a genuine creative choice is unresolved or the remaining request crosses a boundary that needs the user's decision.

Image tools may provide only a generic refusal message. Do not claim to know the exact trigger unless the tool identifies it. A refusal can be over-inclusive, but it must still be treated as a real failure for the attempt log.

### E2.1. Prompt-interpretation audit and proven-baseline recovery

**A refusal or unsuccessful result is not automatically proof that the user's creative
intent is disallowed, that the reference image is the cause, or that the image tool
is incapable of producing the requested visual.** Diagnose the assistant's own
interpretation before redesigning the brief.

Before rewriting a prompt after a refusal, repeated failure, or user correction:

1. **Return to the evidence.** Identify the active series/artwork thread and
   inspect its authoritative chronological prompt history first. Locate the
   most recent successful prompt in that same series/thread and inspect the
   actual approved image assets where relevant. Use the relevant
   `drawings/YYYY-MM-DD/README.md` as a navigation aid, then verify chronology,
   series membership, finalized outcome, and prompt/output linkage in the
   authoritative attempt records. For a novel scene, use its scene-local
   illustration history. Do not rely on memory, a summary, or the most recent
   failed prompt alone.
2. **Find the correct series baseline first.** Identify the active primary
   series and inspect its most recent prompt. Use the most recent successful
   prompt in that same series as the execution baseline. If no series applies
   but the work is an identifiable continuation of one artwork/thread, use the
   most recent successful prompt for that exact thread. A success from another
   series or artwork is not a substitute merely because it shares a subject,
   outfit, mood, or rendering style. Only when neither a series nor an exact
   continuing artwork/thread can be identified should you search for the
   strongest comparable success across the broader prompt history.
3. **Audit prompt drift.** Compare the user's actual brief and successful
   baseline against the new authored prompt. Identify every assistant-added
   element, including identity-preservation claims, extra scene details,
   wardrobe changes, more restrictive coverage, altered framing, sensuality
   labels, repeated negative clauses, and unnecessary safety disclaimers.
   Ask which changes the user requested and which are genuinely necessary.
4. **Restore before redesigning.** When the user's goal is unchanged, the
   relevant archived baseline achieved that goal, and the content remains
   within applicable policy, restore the successful authored prompt verbatim
   or make only the smallest user-requested change. Do not automatically
   replace an approved open neckline, off-shoulder garment, romantic mood, or
   other defining feature with a high neckline, conservative fashion portrait,
   different outfit, or different setting merely because an earlier attempt
   was refused.
5. **Do not over-engineer safety language.** Use clear positive descriptions
   of the intended allowed image. Do not stack unnecessary phrases such as
   repeated "no nudity / no cleavage / no suggestive pose" clauses when they
   were not part of the successful baseline and do not address a concrete
   issue. Such additions can distort the user's brief and may themselves
   foreground interpretations the user did not request. This does not reduce
   or bypass the actual safety review.
6. **Treat references as a deliberate choice.** Determine whether an image
   reference is needed for identity, style, or composition. If the proven
   successful method was fresh text-to-image generation without a reference,
   do not attach an image merely as ritual. Conversely, when a reference is
   needed, attach the actual asset through the supported mechanism and verify
   that it was included. Never confuse an inspiration reference with an edit
   source.
7. **Separate observations from hypotheses.** Record the exact tool response.
   A generic refusal does not identify the offending word, visual feature,
   context, or attached reference. Label possible causes as hypotheses only.
   Do not present the assistant's interpretation as an internal tool diagnosis.
8. **Take user corrections seriously.** When the user says the assistant has
   misread or over-restricted the request, reopen the successful history and
   audit the assistant's own additions before defending the previous approach
   or blaming the tool. Do not make the user repeat a sufficiently clear brief.
9. **Use a bounded recovery sequence.** After a refusal, first make one
   genuinely safety-aware revision if needed. If that revision also fails,
   stop similar rewrites. If the audit then exposes a distinct assistant-made
   deviation from a relevant successful baseline, one baseline-restoration
   attempt may be made and must be archived before generation. If the restored
   baseline is also refused, stop and explain the limitation; do not keep
   probing or submit cosmetic variations.
10. **Preserve the user's creative intent.** Safety review must be accurate and
    proportionate. Do not invent sexual intent from ordinary affection,
    fashion, exposed shoulders, or non-explicit anatomy. At the same time,
    successful historical outputs do not override current policy: never
    recreate disallowed content or use prior acceptance as a way to evade
    safeguards.

The purpose of this audit is to prevent assistant-created prompt drift, not to
guarantee that a tool will accept every prompt. The assistant owns its
interpretation and must test its assumptions against the project's actual
successful work.

### E2.2. Documented silk-wrap series and baseline-selection case

The November 12–13, 2026 silk-wrap portrait sequence is a historical example
of prompt lineage only. The current session brief controls creative direction;
the latest **successful** prompt controls only historical prompt lineage:

- **Attempt 33** in `prompts/2026-11-12-image-prompts.md` established the
  successful Realistic portrait direction and produced two user-approved
  images. It is the original successful prompt in this portrait series.
- **Attempt 04** in `prompts/2026-11-13-image-prompts.md` reused Attempt 33's
  authored wording verbatim in a fresh generation. The assistant initially
  judged a garment-construction detail as missed. The user later explicitly
  assessed the Attempt 04 result as successful. That final user assessment
  supersedes the assistant's narrower preliminary judgment. Because the
  prompt-to-output association is explicit, Attempt 04 is a user-approved
  successful result and the most recent successful prompt record in this
  series at the time of the archive.
- **Attempt 05** added one positive sentence about the silk panels overlapping
  across the bust, but the tool rejected the attempt and returned no image.
  It is a failed attempt, not a new baseline. Its wording must not replace or
  become the base prompt. The additional construction instruction is only a
  pending delta if the user still requests it in a future task; it must not be
  silently imposed on the approved Attempt 04 direction.
- **Attempt 06** attempted a localized edit of the actual Attempt 04 image.
  The source image was attached for that call, but the tool rejected the edit
  and returned no edited image. The original Attempt 04 image remained
  unchanged and user-approved. Attempt 06 is not a successful prompt or edit
  baseline. A future exact edit still requires the actual source asset to be
  attached in that future call; the historical file ID alone is not attachment.

**Operational lesson:** Attempt 04—not the newer failed Attempts 05 or 06—is
the latest user-approved successful prompt/output record in this series.
Attempt 33 remains its earlier successful origin and has the same authored
prompt wording. Any future successful prompt in this same series would
supersede Attempt 04 by chronology. This case also demonstrates that the
user's final assessment controls whether an output is accepted; an earlier
assistant assessment must not override a later explicit user approval.

  
### E2.5. Session-local image asset naming and provenance

Images supplied or selected for a drawing session are session-specific unless
the user explicitly says they should be retained for future use.

1. Inspect the actual image and identify its role in the current session:
   inspiration, identity, composition, style, exact edit source, keeper, or
   temporary comparison. Do not infer its role from its filename.
2. Use an image as a drawing reference only when the user assigns that role in
   the active session brief or a later explicit instruction. Do not silently
   promote a previously uploaded, approved, or stored image into a global or
   future-session default.
3. If the user requests retention in the repository, give the image a clear,
   descriptive, stable filename based on its visible content. For a set, use
   consistent names and numbered suffixes. If the user does not request
   retention, use the supplied image only within the current session.
4. **Preserve the original image exactly.** The default is rename-only:
   preserve its bytes, format, extension, resolution, dimensions, metadata, and
   visual content. Do not recompress, resize, crop, rotate, filter, retouch, or
   strip metadata. The user has explicitly authorized one repository workflow
   exception: an image submitted through `images/takeout/` with a ready
   `HANDOFF.yml` may be moved/renamed to its declared master path and converted
   to a separate WebP derivative by the existing GitHub Action. The original
   bytes and format must remain identical. Do not perform this conversion or
   relocation manually outside that hand-off pipeline.
5. Record the exact asset path, file/attachment ID, source generation ID when
   known, original upload name, dimensions, byte size, checksum where available,
   and its session-specific role in that session's brief or attempt record.
   State whether the binary is stored in GitHub, the persistent Files Library,
   or only the conversation. Never claim repository storage unless verified.
6. Link the image directly from the session brief or the relevant attempt note.
   Do not create or maintain a global image reference index. Do not add
   persistent face, outfit, palette, or style rules merely because an image was
   approved in an earlier session.
7. Keep inspiration references distinct from exact edit sources. A filename,
   repository path, Library ID, or generation ID is not an attachment. Attach
   the actual asset through the image tool's supported mechanism and verify
   source linkage before claiming a reference-guided result or confirmed edit.
8. For a user-approved output, record the approval and its exact originating
   prompt when reliably known. Approval makes the image a keeper; it does not
   make it a default visual direction for future sessions.

**GitHub rename and takeout rules:**

- If an image is already tracked in its permanent location under an opaque
  filename, rename that existing Git tree path using the same blob SHA. Verify
  the old name is absent, the descriptive name exists, and the blob SHA and byte
  size are identical.
- For newly uploaded retained images, use the universal flat intake
  `images/takeout/`. Inspect the actual image, determine its descriptive title
  and destination, and prepare `images/takeout/HANDOFF.yml`; do not manually
  rename or move it. The hand-off uses the exact uploaded filename, optional
  stable asset ID, descriptive title, and destination directory.
- The existing Action derives the permanent filename as
  `[asset-id-][slugified-title].[original-extension]` and keeps the original
  bytes unchanged. It stages each WebP under
  `images/takeout/webp/[batch-id]/attempt-NNN/`, appending `.webp` to the
  exact incoming filename (for example, `upload.png.webp`). After verification,
  it moves the master and WebP to the declared destination. It refuses
  collisions and verifies master SHA-256 and WebP integrity before clearing
  the hand-off.
- Failed attempts retain successfully converted WebPs in their staging folder
  for inspection; retries use a new attempt number. A successful attempt moves
  its WebPs to final destinations and removes its now-empty staging folder.
- Each successful or failed attempt is archived with the original hand-off,
  `conversion-report.csv`, and `verification-report.md` under
  `images/takeout/history/[batch-id]/attempt-NNN/`. The CSV records staging
  and final paths. Do not claim repository storage or a successful hand-off
  until the final paths and reports are read back and verified.

### E4. Use daily attempt ledgers and authoritative records

Do not create a separate cross-session success catalogue. For non-novel
drawing sessions, use `drawings/YYYY-MM-DD/README.md` as the daily navigation
ledger. It must contain one contiguous Markdown table with exactly six fields:

1. **Attempt / prompt:** the attempt number or stable ID, a concise descriptive
   title, and a direct link to the full attempt record.
2. **Session / brief:** the session ID or name and a direct link to the active
   opening brief. If no separate brief exists, state that explicitly; do not
   invent one.
3. **Series / baseline lineage:** the verified primary series ID/name and
   theme, plus the parent attempt or successful text baseline where known.
   Mark uncertain membership `legacy/unassigned` or `not established`
   rather than guessing.
4. **Execution outcome:** what actually happened—generated, edited with
   verified source linkage, rejected, blocked, pending, superseded, or
   unconfirmed—and whether the result met the defining acceptance criteria.
   Approval of a prompt for generation is not a successful image outcome.
5. **User approval / output evidence:** record user approval separately from
   the assistant's visual assessment. State whether an image was delivered in
   conversation, no output was returned, approval was not recorded, or storage
   and provenance remain unverified.
6. **Image:** link every generated image output once its exact repository asset
   is uploaded and verified, regardless of whether the user approved it or the
   result met the prompt. Link partial, off-target, superseded, and unapproved
   outputs too; approval belongs only in field 5. If an image was generated
   but its asset has not yet been uploaded, write `Waiting for image upload`.
   Use `—` only when no image was returned or generated. Use `Not verified`
   when the tool outcome is unconfirmed and no attempt-specific image can be
   attributed. Never withhold a generated-image link because the user rejected
   or did not approve the result.

Include every attempt in chronological order, including rejected, failed,
partial, pending, and superseded attempts. Do not turn the table into a
success-only list. Keep its six fields populated with concise, evidence-based
facts; put the complete prompt, source IDs, exact tool metadata, acceptance
criteria, visual assessment, and detailed provenance in the linked attempt
record.

The daily README is a navigation and status summary, not an authority that can
override the attempt record. The attempt record is the source of truth for the
authored prompt, actual operation, source linkage, execution result, visual
assessment, user approval, and output identity. When the table and attempt
record disagree, correct the table from the verified attempt record.

For a named novel scene, maintain the complete chronological prompt and output
history in that scene's local illustration records instead of duplicating the
prompt history in a daily non-novel ledger. The scene-local record remains
authoritative.

After each attempt is finalized:
- Update the attempt record with the actual result and its evidence.
- Update the corresponding row in the daily README, keeping each attempt in
  exactly one row and preserving chronological order.
- If the user explicitly approves an image, record that approval in the attempt
  record and the table's approval/output field without rewriting a different
  execution outcome. A user-approved keeper with uncertain prompt mapping must
  remain unlinked to an invented prompt.
- When any generated image is retained through the takeout workflow, the
  verified WebP link must appear in both the attempt record and the daily
  README's Image column, even if the result was partial, off-target, superseded,
  or not approved. Do not make linking conditional on user approval. Do not
  link an unverified filename or infer prompt association.
- Do not omit unsuccessful attempts, promote a generated-but-missed-target
  result to a success, or infer approval from delivery alone.

The latest successful text baseline must be determined from the authoritative
attempt records within the active series or exact artwork thread. The daily
ledger helps locate those records; it does not define visual direction or
baseline eligibility.
 
### F. Inspect and classify
Evaluate the image against the pre-recorded acceptance criteria and the active
session brief. For each criterion, record **Pass**, **Partial**, **Fail**, or
**Not assessable**, with a brief visual observation as evidence. Evaluate every
returned image separately. A critical criterion marked Fail or Not assessable
prevents a successful-match classification unless the user explicitly accepts
the result for the intended purpose.

Also inspect mode, subject count, character continuity, pose direction,
hands/fingers/wrists, clothing/colors, framing, lighting, background, artifacts,
unrequested additions, and whether the source was actually used.

For clothing, inspect **garment construction and coverage**, not just fabric
material or neckline appearance. Verify that the fabric physically lies across
the body areas the brief says it should cover. An opaque garment draped below
the bust does not count as a covered wrap blouse simply because the material is
non-transparent. For wrap garments, check that the front panels visibly cross
and overlap in the intended place; check that the neckline opens above that
overlap. Compare the result with the active session brief and only those reference images
the user explicitly assigned to this session.
Do not infer success from phrases in the prompt or from the absence of visible
nipples; inspect the actual garment boundaries and coverage.

Record one honest outcome:
- **Successful match:** defining requirements are visibly satisfied.
- **Partial match:** the central idea works, but one or more requirements are
  missing or uncertain.
- **Generated but missed target:** an image exists but misses a defining detail.
- **Edit confirmed:** source linkage is verified and the requested change is visible.
- **Fresh generation, not an edit:** a new image was produced.
- **Rejected / failed:** no usable image was returned.

Name each mismatch and retain a useful lesson for the next attempt. Update the
prompt-difference record for the next iteration: preserve what succeeded, change
only what is needed, and explicitly exclude rejected additions or drift.

## 5. Prompt-first image editing and reconstruction

**Primary workflow: successful prompt → controlled prompt revision → fresh generation.**

When the user requests a change to an existing image, use the exact successful authored prompt that produced the target image as the primary baseline. Reconstruct the image through that prompt, then revise only the requested element. Do not default to pixel-level editing of the image itself or make the image attachment the editing mechanism.

1. Locate and verify the target image's originating prompt in the authoritative attempt record.
2. Confirm that the prompt/output pair is successful or user-approved for the intended purpose. If the original prompt cannot be recovered, disclose that limitation; do not fabricate its wording or silently substitute an unrelated prompt.
3. Treat the successful prompt as the reconstruction baseline. Preserve all unrequested details—identity/face, hairstyle, wardrobe, pose, composition, camera, lighting, environment, atmosphere, and other established elements—unless the user explicitly authorizes changes.
4. Make the smallest prompt revision needed to accomplish the requested change. Lead with that change, and identify what is preserved, changed, and excluded. Avoid unnecessary rewording that could cause drift.
5. Generate a new image from the revised prompt. This is a **fresh generation/reconstruction**, not a direct edit of the original image. Do not claim source-image edit provenance.
6. Use the original image as an optional visual comparison/reference only when it materially helps and the user assigns that role. Prompt baseline remains primary; attaching an image is not required for prompt-first reconstruction.
7. Inspect the result against the successful baseline and the specific requested change. Record deviations and the actual outcome.

If the user explicitly asks for a direct image edit or source-image fidelity that prompt reconstruction cannot reliably preserve, direct editing may be considered as a secondary method only when the actual source image is accessible and supported. Do not silently switch away from the prompt-first method. If a direct edit is attempted, verify source linkage and classify it accurately.

For a style-only change, use the successful prompt as the reconstruction baseline and revise only the rendering treatment; preserve people, pose, hands, clothing, objects, lighting, camera position, crop, and scene content unless the user explicitly requests otherwise.

## 6. Session-specific scene and character continuity

No scene composition, character identity, relationship, pose, wardrobe,
hairstyle, prop, location, palette, or emotional treatment is a universal
drawing default. These are determined by the active session-opening brief and
the user's explicit updates within that session.

- For a day-drawing session, follow its own opening brief and amendments.
- For a novel illustration, follow the scene-specific opening brief. Use the
  novel text and scene records for narrative facts only where the user asks the
  illustration to follow or adapt them.
- Preserve a face, outfit, pose, design, or other feature as locked only when
  the user explicitly locks it in the current session or explicitly adopts a
  prior design for that session.
- Do not carry a previous session's visual direction into a new one merely
  because the project, character, relationship, or novel is the same.
- A successful historical prompt is a prompt-lineage aid, not authority over
  the current session brief. Reconcile it with the active brief before use.
- Record scene-specific continuity in the session brief and its attempt notes,
  not in a repository-wide visual index.

## 7. Response and delivery

Deliver images in the conversation. Briefly identify the selected mode when
helpful. Be candid about partial matches, failed edits, and source-reference
problems. Never claim repository storage of an image binary unless it was
actually uploaded and verified.

**Active-session reminder:** While the drawing session being discussed is
Active or Paused, end each response that continues or discusses that session
with a brief reminder that it remains open and the user can say `end session`
if they want formal closeout. This reminder is unobtrusive and does not
interrupt drawing or require a reply. Once the user invokes `end session`,
suppress the reminder during closeout; resume it only in later responses if
closeout cannot be completed and the session remains open. Stop reminding once
the session is Closed. The reminder is not a closeout trigger.

All repository work must use branch `gpt` and remain strictly inside
`approved project directories`.

## Supporting references
- `references/style-guide.md` — detailed mode definitions and visual cues.
- `references/image-editing-protocol.md` — source references, edit, and
  verification procedure.

 
## 8. WebP delivery copies and master-image preservation

The original PNG/JPEG is the permanent master. WebP is a separate delivery
derivative, never a replacement. All newly uploaded assets intended for
repository retention pass through the single intake at `images/takeout/`.

- The incoming filename may be arbitrary. Inspect the actual image and prepare
  the structured `HANDOFF.yml` with source filename, descriptive title,
  optional stable ID, and exact destination directory. For an image belonging
  to a non-novel drawing attempt, also include that attempt number in the item
  as `attempt: NN` and target `drawings/YYYY-MM-DD/images` for its session.
- The existing workflow runs on branch `gpt` and calls
  `images/scripts/process_takeout.py`. It accepts static PNG, JPG, and JPEG.
  APNG and other unsupported formats fail the batch; animation is never
  flattened silently.
- PNGs use exact lossless WebP encoding
  (`-lossless -q 100 -m 6 -exact`); JPEGs use high-quality lossy encoding
  (`-preset picture -q 92 -m 6 -sharp_yuv`). ICC profiles are copied.
  EXIF/XMP metadata are not copied to WebP, but remain in the original master.
- The original upload is moved byte-for-byte into the destination's
  `original/` subfolder under its hand-off-derived name. The same-stem WebP
  remains in the destination root. Attempt notes and the daily README link
  only the WebP delivery file. Novel illustrations use
  `novel/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`; retained
  non-novel assets use their declared destination under `images/`.
- When an item targets `drawings/YYYY-MM-DD/images`, an explicit `attempt: NN`
  is mandatory. The processor validates the matching `attempt-NN.md` and
  six-column daily README, then automatically adds the verified WebP link to
  both records for every uploaded generated output; approval and success
  classification are irrelevant to link creation. Multiple images may identify the same attempt; their links
  are grouped in that row.
  Items without `attempt` metadata are processed as ordinary assets and do not
  alter a prompt record or daily README. The GitHub Action commits these
  Markdown changes together with the processed assets.
- The Action converts the entire batch into persistent staging at
  `images/takeout/webp/[batch-id]/attempt-NNN/` before moving any original.
  Staged filenames append `.webp` to each exact incoming filename. It checks
  destination collisions, exact hand-off coverage, original/master SHA-256
  equality, WebP signatures, and final WebP hashes. It does not overwrite
  existing assets.
- For drawing sessions, the processor maintains `manifest.csv` one row per
  output, preserving existing rows/columns and conservatively inventorying
  legacy WebPs. New rows are `Pending` until the post-push verifier reads the
  exact published master and WebP blobs, verifies both hashes, and checks the
  canonical WebP URL. Legacy assets without originals remain `Not verifiable`.
- Every attempt is archived under
  `images/takeout/history/[batch-id]/attempt-NNN/` with the original hand-off,
  `conversion-report.csv`, and `verification-report.md`. The CSV records
  staging and final paths, sizes, size difference, encoder profile/version,
  hashes, status, and errors. Both `history/` and `webp/` are excluded from
  intake detection.
- The active hand-off is cleared only after every image is converted,
  relocated, and verified locally and the reports are written. On failure, the
  ready hand-off and source images remain available for correction, and
  successful WebPs from that attempt remain in staging. A retry uses a fresh
  attempt directory; successful processing removes its empty staging
  directory. The Action then reads back the original and WebP Git blobs,
  canonical WebP URL, daily README inventory/table links, and attempt-note
  WebP link before publishing manifest verification statuses.
- Never alter a master or WebP after conversion as part of this pipeline.
  Separate image edits require the normal prompt-archive and explicit editing
  workflow.


## Mandatory generated-image archive verification (2026-11-20)

For every drawing session, archive **every generated image output**, regardless of approval, rejection, prompt compliance, or whether it is superseded. Each output must be individually recorded and directly linked from the session README once its exact repository asset exists and is verified. Preserve generation order and prompt-to-output association. Approval is a separate field and never determines archival or linking eligibility.


## Generation provenance and output mapping workflow (approved 2026-11-20)

Use capture-at-generation-time to avoid retrospective image-to-attempt guesses. This is mandatory for every drawing session and applies to approved, rejected, pending, partial, off-target, failed, and superseded outputs.

### Before generation
1. Assign internal session, attempt, and prompt IDs before invoking image generation (for example, session `2026-11-20`, attempt `A001`, prompt `P001`). These are archive IDs, not platform Generation IDs.
2. Reserve output IDs such as `A001-O01`, `A001-O02`. Reconcile reserved slots against actual outputs; do not assume the number returned.
3. Preserve the exact authored prompt and operation type. Follow the existing pre-generation prompt commit and read-back requirement.

### Immediately after generation
4. Capture every returned image in its returned sequence and associate it directly with its attempt/output record. Do not map by filename, visual similarity, chronology alone, or memory when direct association is available.
5. Record platform Generation ID and native image/output ID only when exposed by the generation system. Keep native IDs separate from internal archive IDs. If unavailable, explicitly mark them unavailable/not exposed; never invent IDs.
6. Preserve original bytes when accessible. If they cannot be retrieved, record the limitation; do not substitute a screenshot, thumbnail, or recompressed preview as the original.
7. Record the actual output count and sequence. Remove unused reserved slots; do not create phantom outputs. If the association cannot be established reliably, mark it Unmapped or Unverified.

### Mapping evidence and identity
8. Use internal output IDs (e.g. `A001-O01`) as stable archive identifiers when native IDs are not exposed. They must not be represented as native platform IDs.
9. Keep internal session/attempt/prompt/output IDs, native Generation ID, native image/output ID, approval, outcome, mapping evidence/status, original-byte availability, archive path, SHA-256, and verification status separate.
10. Direct generation-return association or reliable original metadata can support Verified mapping. Chronology and visual comparison may corroborate but cannot alone make a mapping Verified. Filename numbering is never proof.
11. Mapping statuses: `Verified`, `Corroborated`, `Probable`, `Unmapped`, or `Conflicting`. Explain uncertain or retrospective evidence; never silently upgrade status.
12. Calculate SHA-256 only from original image bytes when accessible. A hash proves byte identity, not generation event, prompt association, visual content, or approval. Record original and derivative hashes separately.

### Archive and verify
13. Archive every output regardless of approval. Preserve sequence, prompt association, direct links, and statuses; use the established asset-intake procedure.
14. Extend the session `manifest.csv` with one row per output and include internal attempt/output IDs, native Generation ID, native image/output ID, mapping evidence/status, and original-byte availability. Preserve existing required columns. Unavailable native IDs remain empty or explicitly unavailable.
15. Reconcile generation records, attempt notes, README, manifest, and actual assets. Verify paths, links, and hashes only after checking them; read back all edited records.
16. Do not block drawing on GitHub, hashing, or archival latency. Generate, capture outputs and their associations immediately, then complete metadata, hashing, archive, and verification. If capture or archival is incomplete, retain an explicit pending/incomplete status; do not claim complete closeout.

Provenance chain: **Session → Attempt → Prompt → Generation event (native ID if exposed) → Output (internal ID; native output ID if exposed) → original bytes → SHA-256 → archived asset/link**. Every link is evidence-backed; missing native IDs are stated honestly.

Maintain a session-level `manifest.csv` as the machine-readable source for archival tracking. Required columns:
```csv
session_date,image_id,filename,prompt_id,approval_status,github_url,sha256,verification_status
```
Use one row per generated output (not merely one row per prompt when an attempt yields multiple images). Record `approval_status` as Approved, Rejected, Pending, or Not recorded; use `verification_status` values that distinguish Pending, Verified, Failed, and Not verifiable. Do not invent identifiers, URLs, checksums, or statuses. Keep prompt IDs and image IDs stable and unambiguous.


Calculate SHA-256 from the actual original image bytes whenever those bytes are accessible. Do not calculate a checksum from screenshots, thumbnails, or recompressed derivatives and misrepresent it as the original checksum. If the original is unavailable, record SHA-256 as unavailable/pending rather than guessing. A checksum identifies exact file bytes; it does not establish visual content, prompt lineage, approval, or authenticity by itself.

When the user supplies a downloaded image's SHA-256, compare it with the recorded checksum for the candidate archived original. A match verifies byte-identical files; a mismatch means the files are not byte-identical and must not be marked verified. Renaming or moving a file does not change its checksum; re-encoding, editing, resizing, or converting usually does. If a source original and a WebP derivative are both archived, calculate and record their checksums separately and do not compare them as if they were the same byte stream.

README image links must point directly to the correct image asset and be checked against the repository path/blob before they are marked Verified. The manifest must not mark a URL or checksum Verified until the corresponding verification actually occurs. After archive changes, read back the README and manifest and reconcile every generated output against the chronological attempt record. Report any missing asset, link, prompt association, checksum, or verification explicitly.


## Original-image SHA-256 identity and WebP derivatives (approved 2026-11-20)

SHA-256 is mandatory **when the actual original generated image bytes are accessible immediately after generation**. Calculate the hash from those exact original bytes, never from a preview, screenshot, thumbnail, or recompressed copy. Record it against the session, attempt, prompt, and output ID before the user downloads the image. If original bytes are not accessible, state that the generation-time hash is unavailable; do not invent or calculate a hash from a substitute.


When the user later uploads an unchanged original, the GitHub Action calculates SHA-256 from the uploaded original before conversion and compares it with the generation-time hash. A match establishes byte-for-byte identity and may verify the original-to-output mapping. A mismatch is a review flag—not an automatic rejection—because metadata alteration, recompression, or conversion may change bytes. Do not silently fall back to filenames or visual guessing to claim a verified match. Use metadata and image-content comparison only as separately documented fallback evidence, with conservative mapping status.

The WebP is a derivative with different bytes and therefore is **not expected to match the original SHA-256**. The original hash remains the identity key for the output; record the derivative's path and link under the same output ID. A WebP SHA-256 is optional and only for independent derivative integrity checks. Never compare original PNG/JPEG hashes against converted WebP hashes as if equality were expected.

The GitHub Action should automate original-hash calculation and matching, mapping validation, conversion, renaming/relocation, direct README and attempt-record links, manifest reconciliation, and verification reporting. Preserve existing upload filenames unchanged; filenames are not identity evidence. Do not claim implementation is present until the Action itself has been inspected and modified.


## GitHub Action implementation status (2026-11-20)
The takeout processor retains original PNG/JPEG masters in each destination's
`original/` subfolder and places WebP delivery files in the destination root.
Attempt records and daily README rows link only the WebP. Drawing-session
`manifest.csv` updates preserve existing rows and columns, append one record
per new output, and backfill legacy WebP assets conservatively. Generation-time
hash matches, explicit attempt associations, native identifiers, approval,
and original/derivative hashes remain separate fields.

New manifest records remain `Pending` until the post-push verifier reads the
exact original and WebP Git blobs from `origin/gpt`, validates their SHA-256
values and WebP format, and checks the canonical GitHub URL, daily README
inventory/table links, and the corresponding attempt-note WebP link. Legacy
records without an original master remain `Not verifiable`; their retained
WebP URL, derivative hash, and available README links are still checked.

The Action does not query image-generation history or autonomously discover
native platform IDs. It consumes the explicit `attempt`, prompt/output IDs,
and generation hash supplied in `HANDOFF.yml`; missing provenance remains
blank and mapping confidence is never upgraded by filename. A supplied
generation-hash mismatch is retained for review, with mapping status
`Probable`, rather than rejecting the uploaded image. The workflow runs
Python compilation and regression tests before processing. The GitHub Actions
run must pass and its published output must be read back before the workflow
is described as fully verified.
