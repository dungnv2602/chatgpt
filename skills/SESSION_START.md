# Maya & Me — Session Start

Repository: `dungnv2602/chatgpt`
Working branch: `gpt`

At the beginning of every new chat:

1. Retrieve and read `skills/session-archiving/SKILL.md` from the `gpt` branch.
2. Follow its **Mandatory session-start execution gate** exactly, including retrieving and reading every file it specifies.
3. Verify each required retrieval before reporting completion.
4. If any required file cannot be retrieved or verified, report the exact failure and do not claim startup is complete.

## Role-initiation cue

When the user says **“be the novelist”** as an instruction, immediately follow `skills/novelist-initiation/INITIATION.md` from the `gpt` branch. Treat this as a formal role-and-project initialization: load the required skills, identify and review the active novel's canonical records, verify continuity and current narrative position, and deliver the Novelist Initiation Report. Do not jump directly to writing a scene or ask whether to continue unless the user's same instruction also requests that work.

## Source-of-truth rule

The GitHub repository `dungnv2602/chatgpt`, branch `gpt`, is the sole authoritative source for project files, skills, prompts, references, and archives. Do not create, copy, upload, synchronize, or maintain project materials in ChatGPT Library. Do not use Library as a fallback or secondary source. If a required repository file is missing, report that fact rather than consulting or reconstructing it from Library.

The repository workspace is organized at its root. Canonical project directories are `images/`, `master/`, `novel/`, `prompts/`, and `skills/`. Do not prepend the obsolete `ChatGPT/` directory to paths.

Do not ask the user to activate the project or repeat these instructions. Do not create an archive merely because a chat has started.
