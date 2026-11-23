# Skills Directory

This directory contains Agent Skills-compatible skill folders and project initialization files.

Each skill has a `SKILL.md` file with Agent Skills YAML frontmatter. The `name` field must match the skill directory. Supporting files belong beside the skill or in its `references/`, `scripts/`, or `assets/` directory.

## Foundational skills

These skills govern baseline collaboration and cross-cutting repository work. Load them only through the explicit foundational initialization procedure. Do not load them automatically at the start of a conversation.

| Skill | Responsibility |
|---|---|
| [the-worker](the-worker/SKILL.md) | Session continuity, task operations, collaboration modes, and discussion-register maintenance |
| [asd-ste100](asd-ste100/SKILL.md) | Controlled-language rules for skill and technical documentation |
| [github-actions](github-actions/SKILL.md) | GitHub Actions workflow design, optimization, security, and verification |

The Worker's mandatory [Conversation Mode reference](the-worker/references/conversation-mode.md) defines Default Mode, Condensed Mode, and the discussion-register contract.

## Specialist dependency hierarchy

Load specialist skills in dependency order. Do not load them during ordinary foundational initialization unless the user's task requires the next tier.

1. **Foundational:** The Worker (including its mandatory Conversation Mode reference), ASD-STE100, and GitHub Actions.
2. **Drawing:** the Drawing skill and its required references. Activate for drawing sessions or as a novelist prerequisite.
3. **Novelist:** Romantic Storyteller and active novel records. Activate only for the novelist role.

Use the per-conversation verified-load ledger in [SESSION_START.md](SESSION_START.md). A file that was successfully retrieved and read earlier in the same conversation must be reused, not loaded again.

| Skill | Activation |
|---|---|
| [drawing](drawing/SKILL.md) | The user says “start a drawing session”, requests drawing work, or activates the novelist role. It is a prerequisite for novelist work. |

## Task-specific skills

Load these skills only when the request or an explicit role-initiation procedure requires them.

| Skill | Activation |
|---|---|
| [philosophy-religion-asceticism](philosophy-religion-asceticism/SKILL.md) | Philosophy, religion, theology, asceticism, or contemplative-tradition research |
| [prompt-master](prompt-master/SKILL.md) | Prompt analysis, design, adaptation, or optimization |
| [session-archiving](session-archiving/SKILL.md) | Conversation archives, drawing-session closeout, image provenance, and media workflows |
| [agent-skill-authoring](agent-skill-authoring/SKILL.md) | Creating, revising, checking, or integrating Agent Skills definitions |
| [romantic-storyteller-visual-artist](romantic-storyteller-visual-artist/SKILL.md) | Romantic narrative or visual storytelling. The Drawing skill is a prerequisite for novelist-role initialization and governs visual work. |
| [document-standards](document-standards/SKILL.md) | Template-first document authoring, canonical formats, structural validation, and migration |

## Foundational initialization

[SESSION_START.md](SESSION_START.md) is the sole authority for activation cues and foundational loading. The Worker owns the mandatory collaboration and session-continuity rules.

Do not treat this index as permission to load every skill. Follow each skill's activation and dependency rules.

## Compatibility entry points

[conversation-mode/SKILL.md](conversation-mode/SKILL.md) remains as a compatibility pointer. Its operational rules are part of The Worker and must not be loaded separately.

## Technical documentation standard

All skill documentation and technical documentation must follow the [repository ASD-STE100 policy](asd-ste100/references/repository-writing-policy.md). Use the correct mode for the document type. Preserve meaning and technical precision.
