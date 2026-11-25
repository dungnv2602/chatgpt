# Drawing Skill

Use this skill for image generation, image editing, and visual iteration.

## Visual modes

- **Realistic:** photographic rendering, natural materials, plausible lighting, and anatomy.
- **Vintage:** painterly, illustrative, or print-inspired rendering.

The active session brief selects the mode. A new drawing session starts with a new brief and does not inherit the previous session's mode. Use Realistic mode or Vintage mode to change it within the active session.

## Choose the operation

- Create a new scene or variation with fresh image generation.
- Modify a specific existing image with a direct edit. The exact source image must be available to the image tool.
- When the source is unavailable, disclose the limit. Do not describe a fresh reconstruction as an edit.

For fresh generation, use the latest successful prompt in the same series or artwork thread as the text baseline. For a direct edit, use the supplied source as the visual baseline and change only the requested details.

## Standard workflow

1. Read the active session brief and applicable project records.
2. Read the prompt-fidelity and image-operation references.
3. Create an attempt record from the canonical attempt template. Record the operation, source when applicable, prompt, and observable acceptance criteria.
4. Commit and read back the attempt record before the image operation.
5. Inspect every returned image against the criteria. Record the actual operation, outcome, user approval, and provenance separately.
6. Retain repository assets through the shared image intake. The Worker owns generic intake, original preservation, WebP processing, and provenance checks.

## Canonical files

- SKILL.md — full Drawing workflow.
- assets/attempt-template.md — one record per attempt.
- assets/daily-index-template.md — six-field daily attempt index.
- assets/pattern-entry-templates.md — templates for reusable pattern entries.
- references/style-guide.md — Realistic and Vintage modes.
- references/image-editing-protocol.md — operation selection and source-image rules.
- references/prompt-fidelity.md — prompt authorship and change control.
- references/series-continuity-and-iteration.md — series identity and prompt lineage.
- references/generation-recovery-and-provenance.md — refusal recovery and evidence.
- references/archive-and-delivery.md — Drawing-specific paths and manifest rules.
- references/patterns/README.md — index of successful and failed techniques.
- ../the-worker/references/archive-records-and-image-prompts.md — session records and prompt history.
- ../the-worker/references/image-provenance-and-webp.md — shared asset intake and delivery authority.
- ../the-worker/references/drawing-session-closeout.md — explicit session closeout.

Load the pattern index and its two evidence files once per conversation. Consult relevant entries before each attempt. Refresh only when the files change or the user requests it.

## Documentation

Apply the repository ASD-STE100 policy to technical revisions. Preserve approved creative content.