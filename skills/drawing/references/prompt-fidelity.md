---
title: Prompt Fidelity and Unrequested Restrictions
scope: Mandatory reference for every drawing prompt, revision, image edit, and generation.
updated: 2026-11-20
---

# Prompt Fidelity and Unrequested Restrictions

## 1. Purpose and governing standard

This note establishes the complete prompt-fidelity standard for drawing work. Its purpose is to ensure that the prompt expresses the user's intended image rather than an assistant-authored reinterpretation, redesign, precaution, or substitute.

The user's creative direction is authoritative. The assistant's role is to translate that direction into a clear and usable prompt, not to take ownership of the concept or silently add requirements. Prompt quality is measured by fidelity to the active brief, not by the number of details, warnings, exclusions, or stylistic flourishes added.

The following seven commitments are the user's governing rule. They are retained in full and expanded below. They must not be shortened, weakened, or treated as optional:

1. Use the user's approved prompt as the authoritative source.
2. Do not add unsolicited negative instructions, disclaimers, moralizing language, or restrictive boilerplate.
3. Never append phrases such as:
   - "Fully clothed"
   - "Conventional non-suggestive portrait"
   - "No nudity"
   - "No sexualized posing"
   - Or equivalent restrictions that the user did not request.
4. Do not introduce equivalent wording elsewhere in the prompt to circumvent this rule.
5. Preserve the user's specified scene, subject, face, outfit, pose, and artistic direction.
6. Add a restriction only when the user explicitly requests it or when it is genuinely required by applicable safety rules.
7. Before generation, inspect the complete prompt for unsolicited additions. Remove them before archiving and verification.

These seven commitments are the controlling standard. The detailed procedures in this note explain how to apply them consistently. They do not narrow, replace, or create exceptions to them.

## 2. Scope

This standard applies to all assistant-authored text that directs or materially influences an image, including:

- A new text-to-image prompt.
- A prompt copied, adapted, shortened, expanded, or otherwise derived from an earlier prompt.
- A redo, retry, or continuation of an earlier attempt.
- An image edit, inpainting instruction, or source-preserving revision.
- A style transfer or transformation.
- A prompt reconstructed from a successful image, historical record, character reference, or user-approved baseline.
- Any prompt field, appended instruction, or additional image-tool direction that can affect the resulting image.

It applies before every generation or edit attempt, not only at the beginning of a project. A new attempt is a new opportunity for drift and therefore requires a fresh check against the current brief and latest user instructions.

It governs both positive and negative wording. Positive wording is not automatically authorized merely because it is phrased affirmatively. An unrequested positive-sounding instruction can still add a scene element, style, limitation, or creative direction. Conversely, a negative instruction is not automatically prohibited when the user expressly requested it or an applicable safety rule genuinely requires it.

## 3. Source of truth and instruction authority

### 3.1 Use the approved prompt as the authoritative source

When the user approves a prompt and later asks for a revision, treat that wording as the authoritative baseline. Preserve all details that later instructions have not changed.

Do not replace the approved prompt with a newly invented version merely because the assistant prefers its own phrasing. Do not rewrite unrelated sentences, rearrange the concept, or insert additional instructions under the label of polishing, optimization, clarification, or improvement.

When no prompt has yet been approved, use the active session brief and the user's explicit instructions as the source of truth. Do not invent a supposed approved baseline.

### 3.2 Apply the user's latest instructions

The user's latest explicit correction or amendment controls the property it addresses. It supersedes conflicting wording in an older approved prompt, historical attempt, pattern, reference note, or assistant suggestion.

A phrase that the user has rejected, deleted, or instructed the assistant not to use must not reappear in a later draft. Do not restore it because it exists in an older prompt, even if that prompt was previously successful.

If the user asks for a specific, limited change, make that change and preserve the rest. Do not treat permission to revise one element as permission to redesign the entire prompt.

### 3.3 Use historical material only within the active authority

A successful historical prompt may serve as a wording or technical baseline only when the user authorizes its reuse. The active workflow may also establish it as the relevant baseline. Keep it subordinate to the current brief and the user's latest instructions.

A historical image, prompt, character sheet, pattern, or project convention does not independently authorize importing old creative choices into a new session. Reuse only the details that are compatible with and authorized by the current brief.

Pattern-library guidance can suggest ways to express an already requested feature. It cannot authorize a new feature, restriction, setting, style, pose, wardrobe decision, or other creative change.

## 4. Unrequested restrictions are prohibited

Do not add unsolicited negative instructions, disclaimers, moralizing language, or restrictive boilerplate. This is a substantive requirement, not a preference that can be overridden by a generic prompt-writing template or the assistant's judgment about what sounds prudent.

Do not add restrictions merely because they seem conventional, cautious, professional, tasteful, respectable, modest, or likely to avoid a hypothetical interpretation.

The prohibition includes, without being limited to:

- Unrequested clothing, coverage, modesty, wardrobe, or costume restrictions.
- Unrequested restrictions on pose, posture, gesture, body position, physical contact, expression, or interaction.
- Descriptions that recast the requested image as conventional, non-suggestive, restrained, sanitized, or otherwise socially modified when the user did not request that treatment.
- Generic declarations about what the image must not contain.
- Safety-sounding preambles or disclaimers that are not genuinely required by an applicable safety rule.
- Moral judgments or language implying that the user's requested artistic direction is improper.
- Negative lists copied from templates, unrelated prompts, earlier assistant responses, or previous sessions without current authorization.
- New restrictions introduced to compensate for uncertainty, model unpredictability, a prior failed output, or an assumed risk that has not been established.

The phrases listed in the seven commitments are explicit examples, not an exhaustive vocabulary list. Their synonyms, paraphrases, euphemisms, and functional equivalents are covered by the same prohibition.

Do not infer a need for restrictions merely from a person's presence, appearance, outfit, pose, setting, relationship, interaction, or selected artistic style. Assess the actual request under the applicable rules. Do not invent broader requirements.

## 5. No circumvention by equivalent wording

The rule applies to the meaning and effect of the prompt, not just to exact phrases.

Do not evade the prohibition by:

- Replacing a rejected phrase with a synonym, euphemism, or more polished-sounding expression.
- Moving the same restriction from the end of the prompt to its beginning, middle, scene description, style description, or closing sentence.
- Splitting one restriction across several sentences.
- Recasting a restriction as a positive-sounding aesthetic direction when it imposes the same unrequested limitation.
- Hiding it in parentheses, a quality-control statement, a technical instruction, a template, or a supposedly neutral descriptor.
- Placing it in a separate prompt field or additional image-tool instruction while removing it from the main prompt.
- Retaining the same limiting meaning after deleting only the words the user objected to.
- Adding the restriction to an edit instruction, reference instruction, or other image-controlling text rather than to the main prompt.

Before retaining a phrase that resembles a previously rejected instruction, ask whether it would impose substantially the same limitation in practice. If it would, remove it unless the user has explicitly requested that limitation or an applicable safety rule genuinely requires it.

A wording change is not a valid correction if the rejected restriction remains in substance.

## 6. Preserve the user's specified creative direction

Preserve every feature the user has specified, approved, or explicitly locked. This includes, whenever specified:

- **Scene and narrative moment:** the requested event, situation, setting, environment, time, atmosphere, and action.
- **Subject and identity:** who or what is depicted, identity, recognizable character features, and continuity.
- **Face and appearance:** facial structure, facial features, expression, hair, skin appearance, and other specified appearance details.
- **Outfit:** garment type, construction, cut, shape, fit, color, fabric, material, layering, accessories, and other specified wardrobe details.
- **Pose and action:** posture, body orientation, limb placement, hand placement, gesture, contact points, interaction, and the direction of the action.
- **Composition and camera:** framing, viewpoint, angle, orientation, perspective, distance, subject placement, visibility, and spatial relationships.
- **Artistic direction:** selected visual mode, medium, style, palette, texture, rendering treatment, lighting, atmosphere, and mood.
- **Other express requirements:** every additional detail the user identifies as important, required, or immutable.

This is a preservation checklist, not permission to fill every category with assistant-invented details. If a category is unspecified, it remains open unless the user has delegated that choice or a specific detail is necessary to execute the request.

A locked feature is not an invitation to suggest alternatives. Do not propose changing, simplifying, replacing, concealing, or redesigning a locked face, outfit, pose, scene, or other feature as a workaround for a difficult generation. Do not make a locked feature the presumed cause of a failure without evidence and without authorization to change it.

For an image edit, preserve all source-image content outside the user's requested change to the extent the requested operation and actual tool capability allow. Do not use an edit request as permission to make unrelated improvements or redesign unaffected elements.

## 7. Do not add unrequested creative content

Prompt fidelity also prohibits unsolicited creative additions, even when they are not framed as restrictions.

Do not independently add or change:

- People, characters, animals, or other subjects.
- Backgrounds, rooms, locations, architecture, scenery, props, furniture, or decorative objects.
- Clothing, accessories, hairstyles, makeup, facial details, or body characteristics.
- Pose, gesture, interaction, physical contact, or narrative action.
- Time of day, weather, season, lighting source, or environmental conditions.
- Camera angle, lens language, framing, perspective, depth of field, or composition.
- Mood, emotional tone, relationship interpretation, symbolism, or narrative implication.
- Color schemes, materials, textures, artistic media, stylistic references, or visual effects.
- Text, labels, captions, logos, watermarks, borders, panels, or layout treatments.

These are examples of possible creative additions, not a demand to mention or exclude each category in every prompt.

Do not add decorative details to complete a scene when the user has not requested them. Do not turn an open detail into a fixed creative decision unless the user has delegated creative discretion. An open detail may also become fixed when that choice is genuinely necessary to make the requested image coherent.

When the user expressly grants creative freedom, exercise it only within the scope of that permission. Creative freedom over one aspect does not authorize changing specified or locked elements, inserting restrictions, or expanding the task into a different concept.

## 8. Clarification, technical wording, and prompt optimization

A prompt may be clarified for accuracy and usability, but clarification must not change the user's intended content.

Permitted wording work includes these actions:

- Correct grammar.
- Resolve an unambiguous reference.
- Clarify an already specified spatial relationship.
- Remove accidental ambiguity.
- Organize the same authorized details into a clearer sequence.

A technical clarification must not:

- Add a new visual fact.
- Convert an optional detail into a mandatory requirement.
- Turn an unspecified choice into a permanent lock.
- Change the emotional, stylistic, narrative, or aesthetic meaning.
- Alter a specified face, outfit, pose, scene, or composition.
- Introduce a restriction that the user did not request.

Do not silently decide an ambiguous detail when different interpretations would materially change the image. Ask one concise question about the unresolved point. Do not ask the user to reconfirm details already specified or approved.

Do not use "prompt optimization" as a general license to add negative lists, generic safety language, extra scene details, or assistant preferences. Optimization is acceptable only when it improves the expression of the same authorized direction.

## 9. Reuse, redo, retry, and failure handling

Before reusing a prompt, compare it with the current brief and every relevant later instruction. An older prompt is not automatically safe to reuse in full.

When the user asks for a limited correction, preserve all unaffected wording and details. Do not make unrelated changes to the face, outfit, subject, scene, pose, style, or other elements.

A failed generation does not authorize the assistant to rewrite the user's concept. Do not respond to failure by adding boilerplate restrictions, sanitizing the image, changing locked features, or replacing the user's requested scene with a conventional alternative.

A prior refusal or generic error does not, by itself, identify which phrase or visual feature caused it. Do not claim a cause that the tool did not establish. Any revision must be grounded in an actual user instruction, a clearly identified technical problem, or a genuinely applicable safety requirement—not an unsupported guess.

If a requested element cannot be generated or edited because of a real tool limitation or applicable safety rule, state the specific limitation accurately. Do not disguise an unrelated redesign as a solution. Preserve all unaffected, permissible aspects of the user's direction.

## 10. Restrictions that are expressly authorized or genuinely required

A restriction may be included only in either of these circumstances:

1. The user explicitly requests it. Or
2. It is genuinely required by an applicable safety rule.

The exception is narrow. Prudence, inclusion in a template, and failure of a prior attempt do not make a restriction necessary. Assistant speculation that a restriction could prevent a refusal also does not make it necessary.

When the user requests a restriction, apply it to the scope the user specified. Do not expand it into additional restrictions or use it as authority to redesign unrelated parts of the image.

When an applicable safety rule genuinely requires a restriction, apply only what that rule requires. Do not add adjacent, speculative, or broader restrictions. The existence of one necessary restriction does not authorize a collection of unrelated restrictions.

Do not use the safety exception as a pretext to preserve wording the user has rejected. If a particular rejected instruction is genuinely mandatory, distinguish that specific requirement from optional wording and do not add anything beyond it.

## 11. Complete-prompt audit before every generation or edit

Before generation or editing, inspect the complete prompt—not just the newly edited sentence or the most visible paragraph.

Compare the full text against:

1. The user's approved prompt, where one exists.
2. The active session brief.
3. Every relevant later instruction, correction, and explicit lock.
4. The exact change requested for this attempt.
5. Any applicable safety requirement that genuinely affects the request.

Check every sentence, clause, adjective, negative instruction, parenthetical, appended line, and image-controlling field.

Ask all of the following:

- Is each visual detail traceable to the user's brief, an approved prompt, an explicitly authorized reference, or an authorized creative choice?
- Has any earlier user-rejected wording been restored?
- Has any unsolicited negative instruction, disclaimer, moralizing phrase, or restrictive boilerplate been added?
- Has an equivalent restriction been paraphrased, relocated, split up, or hidden elsewhere?
- Has any new scene, subject, prop, setting, pose, expression, outfit, face, style, lighting, mood, or composition detail been introduced?
- Have all specified and locked features been preserved?
- Has a requested change been limited to the scope the user authorized?
- Has any open detail been converted into an unrequested requirement?
- Is every restriction present because the user requested it or because an applicable safety rule genuinely requires it?
- Does the complete prompt still describe the image the user asked for, rather than an assistant-modified alternative?

If any wording fails this audit, remove or correct it before archiving and verification. Do not proceed by leaving the wording in place and promising to ignore it later.

## 12. Archiving, verification, and actual submission

The prompt-fidelity audit is a mandatory pre-generation gate.

1. Draft from the active brief and the authorized prompt baseline.
2. Perform the complete-prompt audit described above.
3. Remove every unsupported addition and every unauthorized restriction, including disguised equivalents.
4. Only then archive and commit the exact authored prompt under the drawing workflow.
5. Fetch or otherwise read back the committed prompt and verify that it matches the audited text.
6. Immediately before generation or editing, confirm that the text being submitted is the same as the verified prompt.
7. Generate or edit only after these checks pass.

If the text changes after it has been archived or verified, repeat the audit and update and verify the record before generation. A previously verified version does not authorize submitting a modified version.

If the image tool's actual submitted payload is exposed, record it accurately. If it is not exposed, do not claim that the authored prompt is verbatim internal tool wording. Keep the authored prompt distinct from any known compiled or submitted payload.

Do not retroactively alter the archived authored prompt to make it appear that a different text was submitted. Record any actual deviation separately, identify what changed, and state whether it was authorized. A materially different submitted prompt is not a faithful execution of the archived prompt.

## 13. Responsibilities after generation

Evaluate the returned image against the user's actual brief and the specific objective of the attempt. A successful tool call does not establish that the image followed the prompt.

Do not justify an unwanted result by claiming that an unrequested restriction or creative addition was necessary when it was not. Do not silently modify the original brief to make the result appear compliant.

If the output exposes a prompt-fidelity error, record the error and correct the workflow for the next attempt. Do not repeat the unauthorized wording. Do not treat the failure as permission to alter the user's locked features.

## 14. Required decision rule

When deciding whether to retain any phrase or detail, use this test:

- **User specified or approved it:** retain it unless a later instruction changes it or an applicable safety requirement prevents it.
- **User explicitly rejected or removed it:** do not restore it.
- **It is a restriction the user did not request:** omit it unless an applicable safety rule genuinely requires it.
- **It is a creative detail the user did not specify:** include it only when the user has delegated that choice. You may also include it when the detail is genuinely necessary to execute the request.
- **It merely reflects the assistant's preference, template, assumption, or speculation:** omit it.
- **Its status is materially ambiguous:** ask one concise question instead of inventing an answer.

The prompt author must justify every addition. Use the active brief, the user's authorization, or a genuinely applicable safety requirement as the basis. The absence of an objection is not approval.

## 15. Compact pre-generation checklist

Use this checklist before every image generation or edit:

- [ ] The user's approved prompt is the authoritative baseline, where one exists.
- [ ] The active brief and latest explicit instructions have been checked.
- [ ] All specified and locked scene, subject, face, outfit, pose, and artistic-direction details are preserved.
- [ ] No unrequested creative additions have been introduced.
- [ ] No unsolicited negative instructions, disclaimers, moralizing language, or restrictive boilerplate have been added.
- [ ] No rejected restriction has been restored or disguised through equivalent wording elsewhere.
- [ ] Every restriction present was explicitly requested by the user or is genuinely required by an applicable safety rule.
- [ ] The complete prompt—not merely the changed passage—has been audited.
- [ ] Unsupported wording has been removed before archiving and verification.
- [ ] The archived and verified prompt is the exact authored text that will be submitted.

**Generation gate:** Do not generate or edit until every applicable item passes. If an item does not pass, correct the prompt first. Do not weaken the rule to get an attempt through.
