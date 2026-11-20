# Skills Directory

This directory contains Agent Skills-compatible skill folders and the project's explicit initialization documents.

Every skill folder contains a `SKILL.md` with valid Agent Skills YAML frontmatter. The `name` field matches the folder name. Supporting material remains alongside the skill or under its `references/` directory.

## Foundational skills

These govern cross-cutting collaboration, repository operations, and skill maintenance. They are loaded only through the explicit foundational initialization procedure; they are not loaded automatically at the beginning of a new conversation.

| Skill | Responsibility |
|---|---|
| [agent-skill-authoring](agent-skill-authoring/SKILL.md) | Agent Skills structure, metadata, authoring, validation, and integration |
| [conversation-mode](conversation-mode/SKILL.md) | Default Mode and Condensed Mode collaboration behavior |
| [session-archiving](session-archiving/SKILL.md) | Conversation integrity, archive records, image provenance, and closeout |

## Foundational prerequisite

| Skill | Responsibility |
|---|---|
| [drawing](drawing/SKILL.md) | Image generation and editing procedures; currently required by the foundational execution gate, while remaining a drawing-domain skill |

The Drawing skill is not a general-purpose foundational policy. Its presence in the foundational gate is an explicit repository loading requirement, recorded separately from its domain classification.

## Task-specific skills

Load these only when the request or an explicit role-initiation procedure requires them.

| Skill | Activation |
|---|---|
| [novelist-initiation](novelist-initiation/SKILL.md) | The user explicitly says "Be the novelist"; then follow its `INITIATION.md` protocol |
| [philosophy-religion-asceticism](philosophy-religion-asceticism/SKILL.md) | Philosophy, religion, theology, asceticism, or contemplative-tradition research |
| [romantic-storyteller-visual-artist](romantic-storyteller-visual-artist/SKILL.md) | Romantic narrative or visual-storytelling tasks; drawing rules remain authoritative for visual work |

## Foundational initialization

The activation cues and loading sequence are defined by [SESSION_START.md](SESSION_START.md), with the mandatory execution gate in [session-archiving/SKILL.md](session-archiving/SKILL.md).

Do not treat this index as permission to load every listed skill. Use the activation and dependency rules above.
