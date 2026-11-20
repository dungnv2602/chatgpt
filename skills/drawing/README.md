# Drawing Skill

Use this skill for ChatGPT image generation and image editing.

## Visual modes

- **Realistic:** photographic rendering, natural materials, plausible lighting, and natural anatomy.
- **Vintage:** painterly or print-inspired rendering. This mode includes storybook, oil, watercolor, gouache, editorial illustration, and selected retro-print styles.

The latest cozy-bedroom artwork uses **Vintage Mode → Painterly Storybook**.

## Mode commands

- `Realistic mode`
- `Vintage mode`

The selected mode remains active during the current conversation or continuous artwork task. Change it only when the user requests a change.

For an unrelated task, infer the mode from the request. Ask one concise question when the mode is unclear and materially affects the result.

## Prompt fidelity

The [Prompt Fidelity and Unrequested Restrictions](references/prompt-fidelity.md) file is the complete authority for prompt fidelity.

Read it before you draft, reuse, revise, archive, verify, or submit an image prompt.

Preserve the user's approved prompt and creative direction. Do not add unrequested restrictions or creative details. Audit the complete prompt before every generation or edit.

## Prompt interpretation and recovery

Before you revise a refused or unsuccessful prompt, inspect the successful-prompt index and the full chronological history.

Check for assistant-added details. Avoid unnecessary changes to the user's creative direction.

When a relevant successful baseline exists and the request remains allowed, restore that wording or make only the requested change.

A generic refusal does not identify its exact trigger.

After generation, inspect the actual garment construction and physical coverage. Do not rely only on fabric opacity or prompt wording.

For the full process, read these sections in `SKILL.md`:

- E2.1 Prompt-interpretation audit and proven-baseline recovery.
- E2.2 Documented silk-wrap recovery case.
- Section F garment-construction checks.

## Files

- `SKILL.md` — core instructions and workflow.
- `references/style-guide.md` — visual-mode definitions and distinctions.
- `references/image-editing-protocol.md` — source handling and edit verification.
- `references/prompt-fidelity.md` — prompt-fidelity rules and pre-generation audit.
- `references/patterns/README.md` — canonical pattern index.
- `references/patterns/successful-patterns.md` — successful techniques.
- `references/patterns/failure-patterns.md` — failures and tested countermeasures.
- `references/patterns/PATTERN-TEMPLATES.md` — templates for new or revised patterns.

On the first drawing task in a conversation, read the pattern index and both pattern files. Consult the loaded patterns at each drawing session and relevant attempt. Record their blob SHAs. Refresh only changed or newly needed files. Load templates only when you create or revise a pattern.

## Technical documentation standard

Apply the repository [ASD-STE100 writing policy](../asd-ste100/references/repository-writing-policy.md) when you revise this README or other Drawing documentation. Preserve all user-approved creative content.
