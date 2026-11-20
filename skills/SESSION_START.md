# Maya & Me — Session Start

Repository: `dungnv2602/chatgpt`
Working branch: `gpt`

## Initialization rule

Initialization is conditional. Do not load project instructions, skills, or references at the start of a new conversation.

Wait for an explicit cue:

- `Follow instructions` — perform foundational initialization.
- `Be the novelist` — perform foundational initialization first. Then perform novelist initialization.
- Both cues — perform foundational initialization once. Then perform novelist initialization.

This file and the mandatory execution gate in `skills/session-archiving/SKILL.md` define the foundational sequence. Do not run that gate without an applicable cue.

## Initialization cues

The cues have separate roles. Novelist initialization depends on foundational initialization.

### “Follow instructions” — foundational initialization

When the user gives this instruction, perform the foundational initialization defined by this file and the mandatory execution gate in `skills/session-archiving/SKILL.md`.

Load and apply the required foundational skills and references. Do not activate a specialist role.

Run foundational initialization only after an explicit cue.

### “Be the novelist” — role initialization

When the user gives this instruction, load `skills/novelist-initiation/SKILL.md` from branch `gpt`. Follow its `INITIATION.md` procedure.

First verify that foundational initialization is complete in the current conversation. If it is not complete, perform it before loading novelist-specific skills.

Then load the novelist-specific skill. Review the active novel's canonical records. Verify continuity and the current narrative position. Deliver the Novelist Initiation Report.

Do not start a scene unless the user's instruction also requests that work.

### Combined invocation and execution order

If the user gives both cues, perform foundational initialization once. Then perform novelist initialization.

If the user gives only “Be the novelist”, include the foundational prerequisites. Do not ask the user to repeat the other cue.

If the user gives only “Follow instructions”, stop after foundational initialization. Do not infer a specialist role.

Reuse verified foundational files from the current conversation. Do not treat remembered instructions or earlier reads as current-session verification.

## Foundational standards

### Agent Skills format

`skills/agent-skill-authoring/SKILL.md` is a required foundational skill. Load it during foundational initialization.

Use it when you create, revise, validate, or integrate a skill. It defines the repository's implementation of the Agent Skills format.

### ASD-STE100 technical writing

`skills/asd-ste100/SKILL.md` is a required foundational skill. Load it during foundational initialization.

Apply its repository policy to all skill documentation and technical documentation. Use Strict mode for operational instructions. Use STE-flavored mode for technical explanations and READMEs.

Preserve facts, conditions, scope, modality, and technical precision. Do not apply the standard to creative writing, dialogue, marketing copy, or approved creative prompts.

The repository policy is in `skills/asd-ste100/references/repository-writing-policy.md`. Load that file when you create or revise technical documentation.

Neither the skill nor the linter certifies a document as fully ASD-STE100 compliant. The repository does not contain the official controlled dictionary.

## Source-of-truth rule

The GitHub repository `dungnv2602/chatgpt`, branch `gpt`, is the sole source of truth for project files, skills, prompts, references, and archives.

Do not create, copy, upload, or synchronize project materials in ChatGPT Library. Do not use Library as a fallback source.

If a required repository file is missing, report that fact. Do not reconstruct it from Library.

The canonical project directories are `images/`, `master/`, `novels/`, `prompts/`, and `skills/`. Do not use the obsolete `ChatGPT/` wrapper path.
