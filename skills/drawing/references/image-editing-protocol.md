# Image Reference and Editing Protocol

## 1. Mandatory prompt-only adjustment

For every request to adjust, revise, refine, or change an existing result, use the **successful authored prompt that produced the target result** as the sole baseline. Revise that prompt and generate a fresh result. Never use the existing image itself as the editing source or as a visual reference.

- Locate the exact successful prompt in the authoritative attempt record.
- Verify that it produced the target result, or that the user approved that specific attempt for its intended purpose.
- Recover the complete authored prompt. If it is unavailable, disclose the gap. Do not fabricate wording or silently substitute an unrelated prompt.
- Preserve all unrequested visual content specified by the successful prompt.
- Revise only the requested details. Keep all other details unchanged.
- Generate a fresh result from the revised prompt and assess it against the successful baseline and the requested changes.

**Never ask the user to upload, attach, or reattach an image for an adjustment.** This applies even when the image is not available in the conversation.

**Never use an existing image as the base or reference.** Do not attach, pass, or otherwise supply the prior image to the image-generation tool for an adjustment. The successful authored prompt is the base.

**Never mention the image or image-editing operation in the next prompt.** Write a self-contained generation prompt that describes the desired final subject and scene directly. Do not refer to an image, source image, uploaded image, previous image, reference image, attachment, or an edit. Avoid wording such as "edit this image", "based on the image", "use the attached image", or "preserve the image". Describe the visual content from the successful prompt in direct scene language, then incorporate only the requested changes.

If the successful prompt is missing or incomplete, use the active session brief and the available authoritative attempt records. Disclose what prompt information could not be recovered. Do not ask for an image as a substitute. Ask a question only when an essential creative requirement cannot be resolved from the available written records.

## 2. Scope of the prompt-only rule

The prompt-only rule applies whenever the user asks to adjust an existing result. Do not use an image attachment for identity, composition, style, comparison, or direct-edit reference during that adjustment. Resolve the intended visual content from the successful authored prompt and the user's written change request.

Image references may be used for other drawing tasks only when the user explicitly assigns a reference role and the task is not an adjustment of an existing result. This does not create an exception to the prompt-only adjustment rule.

## 3. Revise the proven prompt, not the image

Start with the single requested change. Use the verified successful authored prompt as the baseline. Make only the necessary revision.

- **Preserve:** every unrequested visual element. This includes identity and face, hairstyle, wardrobe, pose, and body geometry. It also includes composition, camera, lighting, background, environment, mood, and rendering style when the baseline specifies them.
- **Change:** only the element the user requested.
- **Exclude:** unwanted additions, text, boxes, artifacts, or other details that the user identified or that appear only in unsuccessful attempts.
- Do not add decorative improvements. Do not substitute clothing, change faces, or change scenes to solve an unrelated issue.
- Avoid wholesale rewording of a successful prompt. Unnecessary prompt changes can affect more than the requested target.

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
