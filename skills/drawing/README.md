# Drawing Skill

A two-mode visual creation skill for ChatGPT image generation and editing.

## Modes
- **Realistic:** lifelike photographic rendering, natural materials, plausible lighting and anatomy.
- **Vintage:** crafted, nostalgic rendering, including painterly storybook, oil, watercolor, gouache, editorial illustration, and selected retro-print treatments.

The latest cozy-bedroom artwork is classified as **Vintage Mode → Painterly Storybook**.

## Mode commands
- `Realistic mode`
- `Vintage mode`

The selected mode remains active for the current conversation or continuous
artwork task until explicitly changed. For a new unrelated task, infer from the
request or ask which mode the user prefers when the distinction is unclear.

## Mandatory prompt-fidelity standard

The full rule is maintained separately in
[Prompt Fidelity and Unrequested Restrictions](references/prompt-fidelity.md).
This is the authoritative, exhaustive reference for preserving the user's
approved prompt and creative direction, prohibiting unrequested restrictions
and additions, and auditing the complete prompt before every generation or
edit. Apply it together with the workflow in SKILL.md.

## Prompt interpretation and recovery

Before rewriting a refused or unsuccessful prompt, compare it with the project's
successful-prompt index and the full chronological history. Audit assistant-added
details and avoid unnecessarily redesigning the user's creative direction.
When a relevant successful baseline exists and the request remains allowed,
restore that wording or make only the smallest requested change. A generic
refusal does not reveal its exact trigger. After generation, inspect the actual
garment construction and physical coverage, not just fabric opacity or the
prompt's wording. See the core skill's **E2.1 Prompt-interpretation audit and
proven-baseline recovery**, **E2.2 Documented silk-wrap recovery case**, and
Section F's garment-construction checks for the full procedure.

## Files
- `SKILL.md` — core instructions and workflow.
- `references/style-guide.md` — visual style definitions and distinctions.
- `references/image-editing-protocol.md` — source handling and edit verification.
- `references/prompt-fidelity.md` — exhaustive prompt-fidelity standard and pre-generation audit.
