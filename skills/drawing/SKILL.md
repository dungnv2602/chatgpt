---
name: drawing
description: "Create and refine images in two deliberate visual modes: Realistic and Vintage. Use for image generation, editing, style transformations, composition, character continuity, and iterative visual refinement."
created: 2026-11-18T13:18
updated: 2026-11-18T13:18
---

# Drawing Skill

## Purpose

This skill provides two distinct drawing modes:

1. **Realistic Mode:** lifelike, photographic rendering.
2. **Vintage Mode:** nostalgic, crafted rendering with painterly, illustrated,
   traditional-media, or selected retro-print character.

These are different visual targets, not quality levels. Neither is the universal
default.

For the current cozy-bedroom artwork thread, the most recent partial success is
classified as **Vintage Mode**, specifically a warm painterly storybook
treatment. Continue in Vintage Mode for that artwork unless the user explicitly
switches to Realistic Mode.

## 1. Mode selection and persistence

Accept direct commands:
- `Realistic mode` / `Switch to realistic`
- `Vintage mode` / `Switch to vintage`

Apply the selected mode immediately to subsequent drawing work in the current
conversation or continuous artwork task. Do not silently switch modes because a
prompt is difficult or an earlier result failed.

When a new image request does not name a mode:
1. Infer it from clear visual language or an attached style reference.
2. Continue the active mode if the user is clearly continuing the same artwork.
3. If the choice would materially change the result and context does not resolve
   it, ask one short question: **Realistic or Vintage?**
4. Do not assume a mode carries into an unrelated new conversation unless the
   user or a session handoff specifies it.

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

### Useful prompt language for the current artwork
Prefer: softly hand-painted digital illustration, delicate visible brush
texture, warm painterly shading, natural gently simplified forms, refined
storybook realism, nostalgic warm light, and a restrained cream-and-amber
palette.

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


### A. Read the brief and complete the reference preflight

Identify the subject, selected mode, composition, camera/viewpoint, orientation,
character appearance, clothing, expression, pose, exact spatial relationships,
lighting, environment, mood, and what must remain unchanged in an edit.
Separate essential requirements from optional decorative details.

**Mandatory project-continuity check — before drafting any image prompt:**

1. Read `ChatGPT/images/reference-index.md` on branch `gpt` and
   identify the active reference, its scope, and the approved visual features.
   This is a continuity-information check, not an instruction to attach the
   image to every generation.
2. For Maya, use the approved canonical prompt direction and the indexed
   description as the identity/wardrobe specification. Preserve her approved
   face, facial features, long dark hair, proportions, and exact ivory
   silk-wrap outfit and garment construction. These are locked; do not
   redesign, replace, simplify, or reinterpret them.
3. **A written canonical prompt is sufficient for a fresh text-to-image
   generation.** The actual reference image is optional, not a technical or
   workflow prerequisite. Use the strongest approved prompt in the successful
   prompt index as the base, carry forward the canonical identity and wardrobe
   wording, and direct creative variation toward scene, pose, expression,
   setting, lighting, and composition.
4. Attach the actual image only when the user asks to use it as a visual
   reference, when a task materially benefits from visual-reference guidance,
   or when performing an edit of that exact image. If an image is attached,
   record its exact path and attachment identifier and verify receipt where
   metadata permits.
5. Keep reference roles distinct: an **inspiration reference** guides a new
   generation; an **edit source** is the exact image being modified. A
   filename, repository link, or prompt mention is not an attachment.
   Never claim an image was reference-guided or edited unless the tool call
   actually supports and confirms that linkage.
6. **Do not block a fresh generation merely because the canonical image
   cannot be downloaded or attached.** Proceed from the approved canonical
   prompt and written continuity specification. Stop only when the user
   specifically requires an exact source-image edit or actual visual
   attachment and that source cannot be supplied.

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

### C. Prepare and archive the prompt
Before every generation or edit attempt:
1. Follow `ChatGPT/skills/session-archiving/SKILL.md`.
2. Read `ChatGPT/prompts/successful-image-prompts-index.md`, then the relevant
   chronological image-prompt log in `prompts/`.
3. Read `ChatGPT/images/reference-index.md` for canonical continuity
   information and complete the project-continuity check in section A. Use an
   approved prompt as the base; image attachment is optional for fresh
   text-to-image generation.
4. Reuse the most relevant successful prompt or source image as a base.
5. Change as little as practical for a controlled revision.
6. Record the exact authored prompt, operation type, source, mode, test
   objective, pending status, and every reference asset actually attached.
7. Commit the prompt to branch `gpt`.
8. Fetch and verify the committed prompt before calling the image tool.

The authored prompt is not necessarily the tool's compiled prompt. If the tool
does not expose its submitted payload, say the archive records the authored
direction rather than claiming it is verbatim internal wording.

### D. Use image references honestly

A fresh text-to-image generation may be based on an approved written prompt;
an attached image is not mandatory unless the user specifically requests a
visual reference or an exact edit of that image. For Maya, the canonical prompt
and locked written identity/wardrobe specification are sufficient to proceed.

When an image is used, determine whether it is for identity, composition, style,
or an exact edit source. Pass the actual image asset or reference ID through the
image tool's supported reference mechanism. Merely naming a filename or image
ID in prompt text does not attach it.

Never claim an image was edited or reference-guided if the tool returned a
fresh generation or did not confirm source linkage. Check metadata and inspect
the result. If the user specifically requires source linkage and the tool cannot
accept or retain the source, state that limitation. Do not turn optional
reference attachment into a blocker for ordinary fresh generation.

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

1. **Return to the evidence.** Consult
   `ChatGPT/prompts/successful-image-prompts-index.md` first, then inspect the
   full relevant entries in the chronological prompt history and the actual
   approved image assets. Do not rely on memory, a short summary, or the most
   recent failed prompt alone.
2. **Find the strongest comparable success.** Match the intended subject,
   wardrobe, pose, framing, mood, and rendering style. A prior successful
   prompt that achieved the same visual direction is a stronger baseline than
   a speculative rewrite.
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

### E2.2. Documented silk-wrap recovery case

The November 13, 2026 silk-wrap sequence is a project-specific training example:

- Attempts 02 and 03 introduced assistant-authored changes, including
  identity-preservation language, an attached inspiration reference, repeated
  restrictions, and a conservative wardrobe redesign. Both received the same
  generic refusal. The tool did not reveal a precise trigger.
- The user challenged the assistant's interpretation and directed it to
  examine the successful historical work.
- Attempt 33 in
  `ChatGPT/prompts/2026-11-12-image-prompts.md` had already produced two
  user-approved Realistic portraits with the intended ivory silk-wrap styling,
  open but covered neckline, warm lighting, and affectionate gaze.
- Attempt 04 in
  `ChatGPT/prompts/2026-11-13-image-prompts.md` restored Attempt 33's
  authored prompt verbatim and used a fresh generation without an attached
  reference. It recovered the broad visual direction, but the generated silk
  fell away from the bust instead of overlapping across it. The output
  therefore missed a defining garment-construction requirement and must not
  be classified as a successful match or treated as a keeper.
- After inspecting Attempt 04, the user clarified that the work was not yet
  successful. Attempt 05 adds only one positive spatial instruction to the
  Attempt 33 baseline: the two silk front panels cross and overlap across the
  bust, with the open neckline above that overlap. The result remains pending
  until visually inspected.

**Operational lesson:** Returning to a proven prompt can correct assistant
prompt drift, but prompt reuse alone does not guarantee that every defining
visual requirement will be followed. Inspect the actual garment construction,
not just the material, neckline, or overall resemblance. For this portrait
family, use Attempt 33 as the first-choice baseline and retain the approved
silk-wrap styling without silently redesigning it.


### E2.5. Uploaded-image naming and cross-linking

For every image the user uploads as part of the Maya_and_Me drawing workflow:

1. Inspect the actual image. Do not infer its contents from its filename alone. Identify whether it is a successful output, an inspiration reference, an edit source, or a temporary comparison.
2. Unless the user explicitly says the upload is temporary or not to be retained, give it a clear, descriptive, stable filename based on the visible subject and its distinguishing composition. For a set, use consistent names and numbered suffixes.
3. **Renaming changes the filename only. Never convert or alter an uploaded image without explicit user permission.** Preserve its exact original bytes, file format, extension, resolution, dimensions, metadata, and visual content. Do not recompress, resize, crop, rotate, filter, retouch, strip metadata, create derivatives, or make convenience copies.
4. Perform task-related file creation and editing only inside the assigned repository root workspace. Do not create, edit, convert, stage, or save task-related files outside `images/`, `ChatGPT/prompts/`, or `skills/` unless the user explicitly authorizes a specific outside location. This includes temporary files and conversion intermediates.
5. Record its exact storage path and file ID, source generation ID when known, original upload name, dimensions, byte size, and checksum where available in `ChatGPT/images/reference-index.md`. State explicitly whether the binary is stored in GitHub, the persistent Files Library, or only the current conversation.
6. When the image belongs to a successful generation, edit the corresponding successful result entry in `ChatGPT/prompts/YYYY-MM-DD-image-prompts.md` and add a direct relative Markdown link to its reference-index anchor, alongside the descriptive filename and stable asset ID. Do not leave the reference link only in a separate end-of-file note.
7. In `ChatGPT/prompts/YYYY-MM-DD-conversation-integrity.md`, record the user's upload/approval and the rename/storage action as a chronological tool event. Add direct links to each image's reference-index anchor and to the corresponding successful prompt entry.
8. Verify the renamed asset through Files metadata and read back every updated GitHub Markdown file. Never invent a Library URL or claim that a Markdown index means the binary is committed to Git.
9. If the upload is an edit source rather than a keeper/inspiration, preserve that role explicitly. An uploaded image is not automatically proof that a later generation edited it; source linkage must still be verified separately.

These steps are part of the normal drawing workflow, not optional cleanup after the session.

**GitHub rename rule:** If the uploaded image already exists as a binary in `ChatGPT/images/` under an opaque filename, rename that existing Git tree path using the same blob SHA and remove the old path in the same commit. Verify that the old name is absent, the descriptive name exists, and the blob SHA and byte size are identical. Do not re-upload or re-encode the image merely to rename it.

### E3. Reuse user-approved visual references

Before writing a new prompt, inspect `ChatGPT/images/reference-index.md` and the relevant chronological prompt history. A user-approved successful image is a stronger starting point than speculative rewording.

For the realistic silk-wrap portrait direction, attempt 33 is the successful authored-prompt base. Its two approved reference images are indexed at `ChatGPT/images/reference-index.md`:
- `realistic-silk-wrap-portrait-soft-gaze-01.png`: slightly wider portrait and softer framing.
- `realistic-silk-wrap-portrait-close-framing-02.png`: closer crop and more pronounced but still covered neckline.

Preserve the visual features the user explicitly approved: long dark hair, ivory silk draped off one shoulder, bare shoulders and collarbones, an open natural neckline with opaque coverage, warm cinematic light, and an affectionate direct gaze. Do not silently replace this styling with a high neckline, a formal high-neck gown, or a generic conservative portrait. Do not exaggerate it into nudity or explicit sexual content.

Keep **inspiration reference** and **edit source** separate:
- An inspiration reference guides style, wardrobe, mood, and composition for a new generation.
- An edit source is the exact image being modified. Claim an edit only when the image tool confirms source linkage.
- A Library file ID, filename, or URL in prompt prose is not by itself an attached image. Retrieve and attach the actual image through a supported reference mechanism when available.
- If a reference image cannot be attached, say so; do not pretend the prompt was source-guided.

When the user approves generated images for future inspiration, preserve their descriptive filenames and provenance in the reference index. Keep each image's source generation ID, file dimensions, byte size, and checksum where available. Record whether the original binary lives in GitHub, the persistent Files Library, or only the current conversation. Never claim GitHub storage unless the binary itself has been committed and verified.

### E4. Consult and maintain the successful-prompt index

Before drafting a new image prompt, consult `ChatGPT/prompts/successful-image-prompts-index.md` first, then the full chronological image log. Reuse the strongest relevant successful prompt and its linked image assets as the starting point; do not elevate partial, rejected, or missed-target results into successful references.

After an attempt is finalized:
- If it is a genuine successful match, add it to the separate success-only index with a direct link to its prompt entry and the resulting image(s).
- If the user explicitly identifies an existing image as successful, add it to a distinct **user-approved successful outputs** section with a direct image link and a concise visual description. The user's assessment is sufficient to classify the image as user-approved; do not require the assistant to independently agree with every detail of the original prompt.
- Keep user-approved image outputs distinct from prompt-attributed successes. Link to an exact originating prompt only when the chronological record reliably establishes the relationship. If the mapping is uncertain, say so and do not invent an attempt number or prompt.
- If an existing successful image is renamed, update its direct links in both the prompt result and the success-only index.
- Do not add rejected, partial, or generated-but-missed-target results to the prompt-attributed success category. A user may nevertheless separately approve an image as a visual output; record that approval honestly without rewriting its historical prompt outcome.

### F. Inspect and classify
Evaluate the image against the actual brief. Check mode, subject count, character
continuity, pose direction, hands/fingers/wrists, clothing/colors, framing,
lighting, background, artifacts, and whether the source was actually used.

For clothing, inspect **garment construction and coverage**, not just fabric
material or neckline appearance. Verify that the fabric physically lies across
the body areas the brief says it should cover. An opaque garment draped below
the bust does not count as a covered wrap blouse simply because the material is
non-transparent. For wrap garments, check that the front panels visibly cross
and overlap in the intended place; check that the neckline opens above that
overlap. Compare the result with the user's approved reference when one exists.
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

Name the mismatch and retain a useful lesson for the next attempt.

## 5. Editing discipline

For any request to change one property, treat all unmentioned properties as
locked. State the single intended change near the beginning of the prompt.
Repeat critical locked details only where necessary. Prefer localized edits when
supported. Do not re-describe the entire scene in ways that invite composition
changes.

For a style-only transformation, freeze people, pose, hands, clothing, objects,
lighting, camera position, and crop. Change only the rendering treatment.

## 6. Continuity for the current cozy-bedroom artwork

The current target is a fully clothed, quiet comfort scene between two adults:

- The woman sits upright, supported by pillows and a headboard.
- The man lies on his side and rests against her upper shoulder/chest. He is the
  one resting; do not reverse the roles.
- Her left hand gently cradles or strokes his hair.
- Their other hands rest together on her lap: her right hand underneath and his
  left hand on top. Do not interlace fingers.
- The woman wears a soft cream knit cardigan over a modest top.
- The man wears a plain dark navy polo.
- Both have their established black-rimmed glasses; the woman's established
  short dark chin-length bob should be preserved.
- The atmosphere is warm, calm, safe, and reassuring.

The latest November 12, 2026 image is classified as **Vintage Mode → Painterly
Storybook**. It has not satisfied all composition requirements. Do not call
the artwork complete until the resting direction, hand arrangement, and selected
mode are visibly correct.

## 7. Response and delivery

Deliver images in the conversation. Briefly identify the selected mode when
helpful. Be candid about partial matches, failed edits, and source-reference
problems. Never claim repository storage of an image binary unless it was
actually uploaded and verified.

All repository work must use branch `chatgpt` and remain strictly inside
`ChatGPT/`.

## Supporting references
- `references/style-guide.md` — detailed mode definitions and visual cues.
- `references/image-editing-protocol.md` — source references, edit, and
  verification procedure.

 
## 8. WebP delivery copies and master-image preservation

The original PNG/JPEG in `ChatGPT/images/` is the master image. A WebP version is a delivery derivative, never a replacement.

- Keep the source image byte-for-byte unchanged and keep its original extension.
- Generated WebP companions live only in `ChatGPT/images/webp/`, with the source's relative path and full filename followed by `.webp`.
- PNG masters use exact lossless conversion; JPEG masters use the documented high-quality lossy profile. Do not describe JPEG-to-WebP as lossless.
- Keep every generated derivative even if it is larger than its source. The conversion report records the actual size difference; visual inspection by the user determines whether the derivative is suitable.
- ICC color profiles are copied. EXIF/XMP metadata are not copied by the current workflow. Original metadata remains in the untouched master.
- APNG files are reported as skipped rather than flattened into a single still frame.
- Do not edit, resize, crop, or otherwise transform either master or derivative during conversion. Any separate image edit requires the normal pre-generation archival and explicit workflow.
