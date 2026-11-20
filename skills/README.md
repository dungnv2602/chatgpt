# Skills Directory

This directory contains Agent Skills-compatible skill folders and project initialization files.

Each skill has a `SKILL.md` file with Agent Skills YAML frontmatter. The `name` field must match the skill directory. Supporting files belong beside the skill or in its `references/`, `scripts/`, or `assets/` directory.

## Foundational skills

These skills govern cross-project work. Load them only through the explicit foundational initialization procedure. Do not load them automatically at the start of a conversation.

| Skill | Responsibility |
|---|---|
| [agent-skill-authoring](agent-skill-authoring/SKILL.md) | Agent Skills structure, metadata, authoring, validation, and integration |
| [asd-ste100](asd-ste100/SKILL.md) | Controlled-language rules for skill and technical documentation |
| [conversation-mode](conversation-mode/SKILL.md) | Default Mode and Condensed Mode collaboration behavior |
| [github-actions](github-actions/SKILL.md) | GitHub Actions workflow design, optimization, security, and verification |
| [session-archiving](session-archiving/SKILL.md) | Conversation integrity, archive records, image provenance, and closeout |

## Foundational prerequisite

| Skill | Responsibility |
|---|---|
| [drawing](drawing/SKILL.md) | Image generation and editing procedures. The foundational execution gate also requires this skill. |

The Drawing skill remains a domain skill. The execution gate lists it as a required prerequisite.

## Task-specific skills

Load these skills only when the request or an explicit role-initiation procedure requires them.

| Skill | Activation |
|---|---|
| [novelist-initiation](novelist-initiation/SKILL.md) | The user says “Be the novelist”. Follow its `INITIATION.md` procedure. |
| [philosophy-religion-asceticism](philosophy-religion-asceticism/SKILL.md) | Philosophy, religion, theology, asceticism, or contemplative-tradition research |
| [prompt-master](prompt-master/SKILL.md) | Prompt analysis, design, adaptation, or optimization |
| [romantic-storyteller-visual-artist](romantic-storyteller-visual-artist/SKILL.md) | Romantic narrative or visual storytelling. The Drawing skill governs visual work. |

## Foundational initialization

[SESSION_START.md](SESSION_START.md) defines the activation cues and loading sequence. The mandatory execution gate is in [session-archiving/SKILL.md](session-archiving/SKILL.md).

Do not treat this index as permission to load every skill. Follow each skill's activation and dependency rules.

## Technical documentation standard

All skill documentation and technical documentation must follow the [repository ASD-STE100 policy](asd-ste100/references/repository-writing-policy.md). Use the correct mode for the document type. Preserve meaning and technical precision.
