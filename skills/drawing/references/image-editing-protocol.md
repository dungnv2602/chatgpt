# Image Reference and Editing Protocol

## 1. Mandatory prompt-only adjustment

For every request to adjust, revise, refine, or change an existing result, use the **successful authored prompt that produced the target result** as the sole baseline. Revise that prompt and generate a fresh result. Never use the existing image itself as the editing source or as a visual reference.

- Locate the exact successful prompt assigned as the baseline.
- Verify that it produced the target result, or that the user approved it for the intended purpose.
- Copy the complete authored prompt verbatim. Do not paraphrase, summarize, reconstruct, or rewrite it.
- Apply only the requested change directly to the copied text. Preserve every other word, order, and detail.
- Keep archival metadata out of the submitted prompt. Never include attempt numbers, file names, paths, repository records, prompt-record references, generation IDs, or retrieval instructions.
- Keep image references and editing-operation language out of the submitted prompt. Describe the final visual result directly.
- Generate a fresh result from the revised prompt and assess it against the assigned prompt and the requested changes.

**Never ask the user to upload, attach, or reattach an image for an adjustment.** This applies even when the image is not available in the conversation.

**Never use an existing image as the base or reference.** Do not attach, pass, or otherwise supply the prior image to the image-generation tool for an adjustment. The successful authored prompt is the base.

**Never mention the image, image-editing operation, or workflow metadata in the next prompt.** Start with the exact successful authored prompt and retain it verbatim. Modify only the text needed for the requested change. Do not refer to an image, source image, uploaded image, previous image, reference image, attachment, or an edit. Do not mention attempt numbers, file names, paths, repository records, prompt records, prompt IDs, generation IDs, or instructions to retrieve another prompt. The submitted prompt must contain only direct visual instructions for the intended final result.

If the successful prompt is missing or incomplete, use the active session brief and the available authoritative attempt records. Disclose what prompt information could not be recovered. Do not ask for an image as a substitute. Ask a question only when an essential creative requirement cannot be resolved from the available written records.

## 2. Scope of the prompt-only rule

The prompt-only rule applies whenever the user asks to adjust an existing result. Do not use an image attachment for identity, composition, style, comparison, or direct-edit reference during that adjustment. Resolve the intended visual content from the successful authored prompt and the user's written change request.

Image references may be used for other drawing tasks only when the user explicitly assigns a reference role and the task is not an adjustment of an existing result. This does not create an exception to the prompt-only adjustment rule.

## 3. Revise the proven prompt, not the image

Copy the complete assigned successful authored prompt verbatim. Make the smallest possible in-place change to the exact words that must change. Do not retype it from memory, paraphrase it, summarize it, or replace it with a newly composed description.

- **Preserve:** every unrequested word and visual detail in the assigned prompt.
- **Change:** only the wording necessary to express the user's requested adjustment.
- **Exclude:** workflow metadata and all references to images or editing operations.
- Do not add decorative improvements or unrelated changes.
- Keep the original sentence order and structure unless the requested change makes a local wording adjustment necessary.

For a style-only change, revise only the rendering treatment. Preserve all scene and subject details.

## 4. Recovery when prompt reconstruction misses

If prompt reconstruction repeatedly misses the requested detail:

1. Stop repeating near-identical prompt revisions.
2. Recheck the exact successful baseline and identify assistant-added changes.
3. Reduce the revision to the requested change only.
4. Clarify the relevant spatial, anatomical, material, or compositional instruction in the prompt.
5. If needed, return to the last successful prompt and rebuild the revision in smaller steps.
6. If prompt-only reconstruction remains unreliable, explain the limitation and preserve the best successful result. Do not switch to image-based editing or request an image.

## 6. Prompt-before-generation archive

Follow `skills/session-archiving/SKILL.md` for every attempt:

1. Create or retrieve the current session-opening brief. Check its exact path.
2. For non-novel work, commit the authored prompt in its dated `drawings/YYYY-MM-DD/` attempt note. For a named novel scene, commit it in the authoritative scene-local illustration prompt record under `novels/[Novel-ID]/[Arc-Folder]/[Scene-Folder]/illustrations/`.
3. Treat the session brief as the visual authority. Use the most recent successful prompt in the explicitly active series only as a compatible text baseline. Do not treat it as authority over the current brief.
4. Treat later failed, rejected, partial, or missed-target prompts as diagnostic evidence only. Do not use them as the baseline.
5. Record the session ID or brief path. Record the series ID or theme when it is explicitly active. Record the selected baseline source, operation type, and attached source reference.
6. Derive three to five observable acceptance criteria from the brief. Mark critical criteria.
7. Record the prompt difference. State the baseline, preserved details, changed details, and excluded or omitted details.
8. Check the pre-attempt commit.
9. After the call, record the actual result, image ID, user assessment, and mismatch.
10. Do not store image binaries in Git unless the user requests storage and the operation completes.

## Technical documentation standard

This file defines operational instructions for image references and edits. Apply Strict mode from the repository [ASD-STE100 policy](../../asd-ste100/references/repository-writing-policy.md) when you revise it. Preserve source-verification, prompt-baseline, and user-authority requirements.
