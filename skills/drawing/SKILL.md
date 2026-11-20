---
name: drawing
description: "Create and refine images in two deliberate visual modes: Realistic and Vintage. Use for image generation, editing, style transformations, composition, character continuity, and iterative visual refinement."
metadata:
  project-role: task-specific
  loading-policy: on-demand-prerequisite
  format: agentskills
  created: "2026-11-18T13:18"
  updated: "2026-11-20"
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

## Activation and loading

This is an on-demand skill, not a foundational skill. Do not load it during ordinary `start session` initialization.

Load this skill and its required references when:
- The user says `start a drawing session`.
- The user requests drawing work that requires this workflow.
- The user activates the novelist role. Drawing is a prerequisite for the novelist workflow.

For `start a drawing session`, follow the cue and dependency procedure in `skills/SESSION_START.md`. If foundational initialization has not passed in the current conversation, complete it first. Reuse all verified foundational files.

Check the per-conversation verified-load ledger before retrieving this skill or either required reference. If a path is already verified, reuse it. Load `references/style-guide.md` and `references/image-editing-protocol.md` once per conversation, not once per drawing session or role. Load other Drawing references only when their documented task triggers apply. Moving from Drawing to Novelist, or back to Drawing, does not justify reloading files already verified.

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
Use terms such as photorealistic, natural photographic realism, realistic skin and fabric texture, and physically plausible warm window light. Add natural lens perspective, restrained depth of field, candid, cinematic, editorial, or studio photography when appropriate. Choose only the vocabulary that serves the brief.

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
When compatible with the active session brief, use terms such as softly hand-painted digital illustration, delicate visible brush texture, and warm painterly shading. Other options include natural gently simplified forms, refined storybook realism, or nostalgic lighting. Select the palette from the active brief. Cream and amber are optional, not defaults.

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

When the user invokes an explicit foundational initialization cue, load the foundational session skills first. Then retrieve the current Drawing Skill and its mandatory references from branch `gpt`:
`references/style-guide.md` and `references/image-editing-protocol.md`.
Keep the verified instructions in working context and apply them to every
drawing project throughout that conversation. Do not load every on-demand
reference during foundational initialization. Load `prompt-fidelity.md`
before drafting, reusing, revising, archiving, verifying, or submitting an
image prompt. Load the series, recovery, and archive references when their
specific task triggers below apply. **Do not reread or refetch the full Drawing Skill merely because
the user switches projects or starts another drawing task within the same
conversation.**

Refresh the skill and its supporting references when the user asks for an instruction refresh. Also refresh them when you know or suspect a relevant repository change. Refresh them when new work depends on a supporting reference that you have not read. When foundational initialization runs in a new ChatGPT conversation, retrieve the current repository version again. This also applies when the conversation continues an existing project.

This session-level loading cadence does not reduce any per-attempt requirement below. Before each generation or edit, review the relevant prompt history. Prepare and commit the exact authored prompt, then check that commit. Generate or edit only after that check. Record the actual outcome.


### Pattern consultation checkpoint

The canonical pattern library is packaged under
`skills/drawing/references/patterns/`. Consult it as part of the drawing
workflow, while avoiding redundant retrievals.

1. **Load once per conversation.** On the first drawing task in a new
   ChatGPT conversation, retrieve and read the pattern index
   (`README.md`), `successful-patterns.md`, and `failure-patterns.md`.
   Record each file's Git blob SHA in working context. Do not retrieve the
   same unchanged files again during that conversation.
2. **Consult at each session and attempt.** At the beginning of each distinct
   drawing session, after identifying the active brief and before drafting a
   prompt, consult the relevant entries in the already-loaded pattern content.
   Before each generation or edit attempt, re-check the relevant lessons
   against the current objective and any failure from the preceding attempt.
   Consultation does not require another retrieval when the content is already
   loaded.
3. **Refresh selectively.** Re-retrieve a pattern file only under these conditions:
   - The user requests a refresh.
   - A relevant repository change is known or reasonably suspected.
   - Its current blob SHA is known to differ from the recorded SHA.
   - The pattern file has not yet been loaded in this conversation.
   Reload only the changed or newly needed file. Retain the other verified content.
4. Review `PATTERN-TEMPLATES.md` only when creating or revising a pattern.
5. The active session brief and the user's latest explicit instructions always
   outrank pattern guidance. Patterns inform execution. They do not authorize
   creative changes.

**Mandatory prompt-fidelity reference:** The complete, exhaustive standard is maintained in [Prompt Fidelity and Unrequested Restrictions](references/prompt-fidelity.md). Read and apply that note when drafting, reusing, revising, archiving, verifying, and submitting every image prompt. It preserves the user's seven governing commitments and supplies the required checks. This skill's workflow does not shorten or override it.

### A. Read the brief and complete the session-brief preflight

Identify the subject, selected mode, composition, camera/viewpoint, and orientation. Also identify character appearance, clothing, expression, pose, exact spatial relationships, lighting, environment, mood, and what must remain unchanged in an edit.
Separate essential requirements from optional decorative details.

**Session-specific direction authority — the opening brief governs this drawing session:**

The user's opening brief for a specific drawing session is the source of truth for its creative direction. This applies equally to day-drawing and novel-illustration sessions. No repository-wide image index, past portrait, previous prompt, character sheet, successful image, or old project convention automatically dictates the current session. This applies to its face, identity, outfit, scene, pose, style, palette, mood, setting, and composition. Use one of those materials only when the user explicitly adopts it.

1. At the start of each distinct drawing session, identify the user's opening
   vision and treat it as the active brief. Preserve the user's wording and
   distinguish what is explicitly specified from what remains open for creative
   choice. Do not turn unstated details into permanent locks.
2. For non-novel/day drawing, use the session brief stored under
   `drawings/YYYY-MM-DD/session-[NN]-brief.md`. For a named novel scene, use the
   scene-local session brief under
   `novels/[Novel-ID]/[Arc-Folder]/[Scene-Folder]/illustrations/session-[YYYY-MM-DD]-[NN]-brief.md`.
   The authoritative storage and verification procedure is in
   `skills/session-archiving/SKILL.md`.
3. Record the subject/theme, scene or moment, selected mode, character
   appearance, outfit, pose, framing, environment, lighting, and mood in the
   session brief. Also record continuity requirements, locked features,
   permitted variation, exclusions, and visual references the user explicitly
   assigns to the session. Mark unspecified fields as open/not specified.
   Never invent a lock.
4. Later explicit user instructions within the same session amend the active
   brief for the named property. Preserve the original opening brief and append
   the amendment to the session record. Do not silently rewrite history.
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
   a role in this session. Valid roles include identity, composition, style, or
   exact edit source. A historical image is not an active reference merely
   because it is stored, linked, approved, or previously used. A generation ID
   or filename is not an attachment.
8. If the current-session brief conflicts with a successful historical prompt,
   preserve the user's current brief. Use the old prompt only as a technical
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

For non-novel/day drawing sessions, store repository-retained generated image outputs in the current daily session folder at `drawings/YYYY-MM-DD/images/`. Use `attempt-XX.webp` for one output from an attempt, and `attempt-XX-01.webp`, `attempt-XX-02.webp`, etc. when an attempt returns multiple images. Deliver images in the conversation as usual. When the exact output asset is stored in the repository, link it from the attempt record and daily README. Use a relative path such as `images/attempt-07.webp`. Only link assets whose attempt provenance is verified. Do not create empty image folders solely for rejected or output-less attempts. This policy applies to new retained outputs. It does not authorize migrating, moving, renaming, or deleting existing image assets. Novel-scene illustration binaries continue to use their established scene-local asset library.

### C. Prepare and archive the prompt
Before every generation or edit attempt:
1. Follow `skills/session-archiving/SKILL.md`.
2. Read the active session-opening brief first. For a named novel scene, also
   read the relevant scene-local scene and illustration records. For non-novel
   work, read the session brief under `drawings/YYYY-MM-DD/`. The session brief
   governs visual direction. Scene records supply narrative facts only where the
   brief asks the illustration to follow or adapt them.
3. Review the relevant daily attempt ledger at
   `drawings/YYYY-MM-DD/README.md` and the chronological prompt history for the
   same session. If the user explicitly continues a series, review that series'
   history. Use the ledger only to locate candidate attempts. Check every
   candidate's series membership, outcome, approval, and prompt/output linkage
   in its authoritative attempt record. For a novel scene, use the
   scene-local illustration records. Do not consult or recreate a global
   image-reference index.
4. Select the most recent successful prompt in the active series as the
   historical text baseline. If no series applies, use the most recent
   successful prompt in the exact artwork thread. Newer failures remain
   diagnostic only.
   The active session brief has higher authority than every historical prompt:
   adapt the baseline to the current brief and omit or replace every conflicting
   feature. If no relevant success exists, draft from the current session brief
   and the user's explicit constraints. Do not borrow a prompt from an unrelated
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
9. Retrieve and check the committed prompt before calling the image tool.

For every illustration belonging to a named novel scene, keep a convenient
scene-local prompt record beside its illustration note:
`novels/[Novel-ID]/[Arc-Folder]/[Scene-Folder]/illustrations/illustration-[NN]-prompt.md`.
Create and commit this file before generation. For novel illustrations, this
scene-local file is the authoritative prompt and attempt record. Keep all
novel-specific prompt history inside the novel and do not duplicate it in the
root `drawings/` folder. Link the local prompt from the illustration note and
scene record where practical. Do not replace one
with the other.

The scene-local record must preserve the exact authored prompt, operation type, and generation or edit identifier when available. It must also preserve source/reference details and the chronological sequence of attempts for that illustration. After the
image call, update the local record with the actual direction submitted when
known, outcome, deviations, and continuity assessment. Distinguish the authored
prompt from the tool's compiled or internally submitted payload. If the tool
does not expose its submitted payload, say so. Never claim the authored text
is verbatim internal wording.

The authored prompt is not necessarily the tool's compiled prompt. If the tool
does not expose its submitted payload, say the archive records the authored
direction rather than claiming it is verbatim internal wording.

### D. Use image references honestly

A fresh text-to-image generation may be based on a written specification
contained in or explicitly adopted by the active session brief. An attached
image is not mandatory unless the user specifically requests a visual
reference or an exact edit of that image. Do not inherit a previous session's
canonical prompt or identity/wardrobe specification as current direction
unless the user explicitly adopts it in this session.

When an image is used, determine whether it is for identity, composition, style,
or an exact edit source. Pass the actual image asset or reference ID through the
image tool's supported reference mechanism. Merely naming a filename or image
ID in prompt text does not attach it.

Never claim an image was edited or reference-guided if the tool returned a
fresh generation or did not check source linkage. Check metadata and inspect
the result. If the user specifically requires source linkage and the tool cannot
accept or retain the source, state that limitation. Do not turn optional
reference attachment into a blocker for ordinary fresh generation.

### Series identity and iteration

For multi-image series, recurring characters, prompt lineage, or iterative work, load and apply [Series Continuity and Iteration](references/series-continuity-and-iteration.md) before preparing the next attempt. Preserve established identities, membership, sequence, and user-approved visual decisions.

The detailed rules include the session closeout cue and default iteration procedure. A pause or goodbye is not session closeout. Close only when the user explicitly requests it and archive verification requirements are satisfied.

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

### Refusal-aware recovery and provenance

When a generation is refused, fails, or needs recovery, load [Drawing Recovery, Retry, and Provenance](references/generation-recovery-and-provenance.md). It contains detailed recovery, prompt-audit, baseline-selection, attempt-ledger, and provenance procedures.

Do not respond to a failure by changing locked identity, face, outfit, or other protected creative direction. Preserve the user's approved prompt and make only authorized changes.

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
material or neckline appearance. Check that the fabric physically lies across
the body areas the brief says it should cover. An opaque garment draped below
the bust does not count as a covered wrap blouse simply because the material is
non-transparent. For wrap garments, check that the front panels visibly cross
and overlap in the intended place. Check that the neckline opens above that
overlap. Compare the result with the active session brief and only those reference images
the user explicitly assigned to this session.
Do not infer success from phrases in the prompt or from the absence of visible
nipples. Inspect the actual garment boundaries and coverage.

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

1. Locate and check the target image's originating prompt in the authoritative attempt record.
2. Check that the prompt/output pair is successful or user-approved for the intended purpose. If the original prompt cannot be recovered, disclose that limitation. Do not fabricate its wording or silently substitute an unrelated prompt.
3. Treat the successful prompt as the reconstruction baseline. Preserve all unrequested details—identity/face, hairstyle, wardrobe, pose, composition, camera, lighting, environment, atmosphere, and other established elements—unless the user explicitly authorizes changes.
4. Make the smallest prompt revision needed to accomplish the requested change. Lead with that change, and identify what is preserved, changed, and excluded. Avoid unnecessary rewording that could cause drift.
5. Generate a new image from the revised prompt. This is a **fresh generation/reconstruction**, not a direct edit of the original image. Do not claim source-image edit provenance.
6. Use the original image as an optional visual comparison/reference only when it materially helps and the user assigns that role. Prompt baseline remains primary. Attaching an image is not required for prompt-first reconstruction.
7. Inspect the result against the successful baseline and the specific requested change. Record deviations and the actual outcome.

Use direct editing only when the user explicitly requests it or requests source-image fidelity that prompt reconstruction cannot reliably preserve. Direct editing is a secondary method. Use it only when the actual source image is accessible and supported. Do not silently switch away from the prompt-first method. If you attempt a direct edit, check source linkage and classify it accurately.

For a style-only change, use the successful prompt as the reconstruction baseline and revise only the rendering treatment. Preserve people, pose, hands, clothing, objects, lighting, camera position, crop, and scene content unless the user explicitly requests otherwise.

## 6. Session-specific scene and character continuity

No scene composition, character identity, relationship, pose, wardrobe,
hairstyle, prop, location, palette, or emotional treatment is a universal
drawing default. These are determined by the active session-opening brief and
the user's explicit updates within that session.

- For a day-drawing session, follow its own opening brief and amendments.
- For a novel illustration, follow the scene-specific opening brief. Use the
  novel text and scene records for narrative facts only where the user asks the
  illustration to follow or adapt them.
- Lock a face, outfit, pose, design, or other feature only when the user explicitly locks it in the current session. Apply the same rule when the user explicitly adopts a prior design for that session.
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

**Active-session reminder:** While the drawing session being discussed is Active or Paused, end each response that continues or discusses it with a brief reminder that it remains open. Tell the user they can say `end session` for formal closeout. This reminder is unobtrusive and does not
interrupt drawing or require a reply. Once the user invokes `end session`,
suppress the reminder during closeout. Resume it only in later responses if
closeout cannot be completed and the session remains open. Stop reminding once
the session is Closed. The reminder is not a closeout trigger.

All repository work must use branch `gpt` and remain strictly inside
`approved project directories`.

## 8. Image archive and delivery

After generation or editing, preserve original outputs and record provenance. Check asset mapping. Create delivery derivatives only under the approved workflow. Load [Drawing Archive, WebP Delivery, and Provenance Verification](references/archive-and-delivery.md) for the complete procedures. It covers original-image identity, SHA-256 handling, WebP derivatives, manifest verification, and the approved GitHub Action.

## Supporting references

- `references/style-guide.md` — mandatory foundational visual-mode definitions and cues.
- `references/image-editing-protocol.md` — mandatory foundational source-reference and edit-verification procedure.
- `references/prompt-fidelity.md` — required before drafting, reusing, revising, archiving, verifying, or submitting image prompts.
- `references/patterns/README.md` — canonical pattern index. Load the index and both pattern files once per conversation.
- `references/patterns/successful-patterns.md` — evidence-backed successful techniques.
- `references/patterns/failure-patterns.md` — documented failures and tested countermeasures.
- `references/patterns/PATTERN-TEMPLATES.md` — load only when creating or revising a pattern.
- `references/series-continuity-and-iteration.md` — series identity, prompt lineage, closeout, and iteration.
- `references/generation-recovery-and-provenance.md` — refusal-aware recovery, prompt audits, attempt ledgers, and provenance.
- `references/archive-and-delivery.md` — original-image preservation, hashes, WebP delivery, and archive verification.
- `../asd-ste100/references/repository-writing-policy.md` — required language rules for skill and technical documentation.



## 13. Technical documentation standard

Apply the repository [ASD-STE100 policy](../asd-ste100/references/repository-writing-policy.md) when you revise this skill or its technical references. Use Strict mode for procedures. Preserve every user-approved creative instruction and prompt. Do not rewrite creative content to satisfy a style check.
