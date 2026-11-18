# Maya & Me — Session Start

Repository: `dungnv2602/chatgpt`
Working branch: `gpt`

At the beginning of every new chat:

1. Retrieve and read `skills/session-archiving/SKILL.md` from the `gpt` branch.
2. Follow its **Mandatory session-start execution gate** exactly, including retrieving and reading every file it specifies.
3. Verify each required retrieval before reporting completion.
4. If any required file cannot be retrieved or verified, report the exact failure and do not claim startup is complete.

## Initialization cues

The two cues have distinct responsibilities and a defined dependency order. They are independent commands from the user's perspective, but novelist initialization depends on foundational initialization.

### “Follow instructions” — foundational initialization

When the user says **“follow instructions”** as an instruction, execute or verify the foundational initialization procedure defined by this file and the **Mandatory session-start execution gate** in `skills/session-archiving/SKILL.md`. Load and apply the foundational skills and required references. This cue does not assign a specialist role or activate a task-specific skill by itself.

At the beginning of every new chat, foundational initialization is mandatory even if the user does not say “follow instructions”.

### “Be the novelist” — role initialization

When the user says **“be the novelist”** as an instruction, follow `skills/novelist-initiation/INITIATION.md` from the `gpt` branch. Novelist initialization must first verify that foundational initialization has been completed in the current conversation. If it has not, perform the complete foundational initialization before loading novelist-specific skills.

Then treat the cue as a formal role-and-project initialization: load the novelist-specific skill, identify and review the active novel's canonical records, verify continuity and current narrative position, and deliver the Novelist Initiation Report. Do not jump directly to writing a scene or ask whether to continue unless the user's same instruction also requests that work.

### Combined invocation and execution order

If both cues are given, execute foundational initialization once, then novelist initialization. If only “be the novelist” is given, it automatically includes its foundational prerequisites; the user does not need to issue “follow instructions” separately. If only “follow instructions” is given, stop after foundational initialization and do not infer a specialist role.

Reuse successful, verified foundational reads from the current conversation rather than loading them redundantly. Never treat remembered instructions or reads from an earlier conversation as current-session verification.

## Source-of-truth rule

The GitHub repository `dungnv2602/chatgpt`, branch `gpt`, is the sole authoritative source for project files, skills, prompts, references, and archives. Do not create, copy, upload, synchronize, or maintain project materials in ChatGPT Library. Do not use Library as a fallback or secondary source. If a required repository file is missing, report that fact rather than consulting or reconstructing it from Library.

The repository workspace is organized at its root. Canonical project directories are `images/`, `master/`, `novel/`, `prompts/`, and `skills/`. Do not prepend the obsolete `ChatGPT/` directory to paths.

Do not ask the user to activate the project or repeat these instructions. Do not create an archive merely because a chat has started.
