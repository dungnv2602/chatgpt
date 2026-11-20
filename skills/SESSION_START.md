# Maya & Me — Session Start

Repository: `dungnv2602/chatgpt`
Working branch: `gpt`

## Initialization rule

Initialization is conditional. Do not retrieve or load project instructions, skills, or references automatically at the beginning of a new conversation.

Wait for an explicit cue:

- `Follow instructions` — perform foundational initialization.
- `Be the novelist` — perform foundational initialization first, then novelist-specific initialization.
- Both cues — perform foundational initialization once, then novelist-specific initialization.

The foundational execution sequence is defined by this file together with the **Mandatory session-start execution gate** in `skills/session-archiving/SKILL.md`. Do not run that gate without an applicable explicit cue.

## Initialization cues

The two cues have distinct responsibilities and a defined dependency order. They are independent commands from the user's perspective, but novelist initialization depends on foundational initialization.

### “Follow instructions” — foundational initialization

When the user says **“follow instructions”** as an instruction, execute or verify the foundational initialization procedure defined by this file and the **Mandatory session-start execution gate** in `skills/session-archiving/SKILL.md`. Load and apply the foundational skills and required references. This cue does not assign a specialist role or activate a task-specific skill by itself.

Foundational initialization is not automatic. Run it only when one of the explicit cues above is invoked.

### “Be the novelist” — role initialization

When the user says **“be the novelist”** as an instruction, load `skills/novelist-initiation/SKILL.md` from the `gpt` branch and follow its `INITIATION.md` protocol. Novelist initialization must first verify that foundational initialization has been completed in the current conversation. If it has not, perform the complete foundational initialization before loading novelist-specific skills.

Then treat the cue as a formal role-and-project initialization: load the novelist-specific skill, identify and review the active novel's canonical records, verify continuity and current narrative position, and deliver the Novelist Initiation Report. Do not jump directly to writing a scene or ask whether to continue unless the user's same instruction also requests that work.

### Combined invocation and execution order

If both cues are given, execute foundational initialization once, then novelist initialization. If only “be the novelist” is given, it automatically includes its foundational prerequisites; the user does not need to issue “follow instructions” separately. If only “follow instructions” is given, stop after foundational initialization and do not infer a specialist role.

Reuse successful, verified foundational reads from the current conversation rather than loading them redundantly. Never treat remembered instructions or reads from an earlier conversation as current-session verification.

## Foundational Agent Skills standard

`skills/agent-skill-authoring/SKILL.md` is a required foundational skill. Load and apply it during foundational initialization, and use it whenever a skill is created, revised, validated, or integrated. It defines the repository's implementation of the Agent Skills open format. Its inclusion does not activate a specialist role or authorize automatic initialization without an explicit cue.

## Source-of-truth rule

The GitHub repository `dungnv2602/chatgpt`, branch `gpt`, is the sole authoritative source for project files, skills, prompts, references, and archives. Do not create, copy, upload, synchronize, or maintain project materials in ChatGPT Library. Do not use Library as a fallback or secondary source. If a required repository file is missing, report that fact rather than consulting or reconstructing it from Library.

The repository workspace is organized at its root. Canonical project directories are `images/`, `master/`, `novels/`, `prompts/`, and `skills/`. Do not prepend the obsolete `ChatGPT/` directory to paths.

Do not ask the user to issue both cues when one cue is sufficient. Do not create an archive merely because a chat has started.
