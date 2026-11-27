# Skills Directory

This directory contains Agent Skills-compatible skill folders and project initialization files.

Each skill has a `SKILL.md` file with Agent Skills YAML frontmatter. The `name` field must match the skill directory. Supporting files belong beside the skill or in its `references/`, `scripts/`, or `assets/` directory.

## Foundational skills

These skills govern baseline collaboration, cross-cutting repository work, and document governance. Load them only through the explicit foundational initialization procedure. Do not load them automatically at the start of a conversation.

| Skill | Responsibility |
|---|---|
| [the-worker](the-worker/SKILL.md) | Session continuity, task operations, collaboration modes, and discussion-register maintenance |

The Worker's mandatory [Conversation Mode reference](the-worker/references/conversation-mode.md) defines Default Mode, Condensed Mode, and the discussion-register contract.

The Worker is the sole activation point for document governance, decision governance, CI Ledger operations, and GitHub Actions. Its detailed procedures are references, not separate skills.

| Worker-owned reference | Responsibility |
|---|---|
| [github-actions](the-worker/references/github-actions.md) | Workflow design, CI diagnostics, technical remediation, and validation procedure |
| [ci-ledger](the-worker/references/ci-ledger.md) | Finding identity, intake, attribution, child linkage, recurrence, lifecycle, and integrity |
| [decision-governance](the-worker/references/decision-governance.md) | Drafts, accepted ADRs, implementation linkage, confirmation, and repository analysis |
| [document-type-catalog](the-worker/references/document-type-catalog.md) | Canonical document formats, schemas, and path coverage |

## Specialist dependency hierarchy

Load specialist skills in dependency order. Do not load them during ordinary foundational initialization unless the user's task requires the next tier.

1. **Foundational:** The Worker (including its mandatory Conversation Mode reference).
2. **Drawing:** The Worker's archive/media references, the Drawing skill, and its required references. Activate only after foundational initialization passes. Load only the Worker references required by the drawing or archive procedure.
3. **Novelist:** [Romantic Storyteller](romantic-storyteller-visual-artist/SKILL.md) and active novel records. Activate only for the novelist role.

Use the per-conversation verified-load ledger in [SESSION_START.md](../SESSION_START.md). A file that was successfully retrieved and read earlier in the same conversation must be reused, not loaded again.

| Skill | Activation |
|---|---|
| [drawing](drawing/SKILL.md) | After foundational initialization passes, the user says “start a drawing session”, requests drawing work, or activates the novelist role. It is a prerequisite for novelist work. These requests do not trigger foundational initialization. |

## Task-specific skills

Load these skills only when the request or an explicit role-initiation procedure requires them. The descriptions below identify each skill's distinct scope. The skill's own activation rules remain authoritative.

| Skill | Activation |
|---|---|
| [agent-skill-authoring](agent-skill-authoring/SKILL.md) | Create, revise, check, or integrate Agent Skill definitions. This skill defines the repository's canonical skill format and authoring procedure. |
| [asd-ste100](asd-ste100/SKILL.md) | Rewrite technical English, skill instructions, tool descriptions, errors, and operational reports for clarity. Do not use for creative or marketing copy. |
| [define-goal](define-goal/SKILL.md) | Define or refine a concrete, measurable goal. Goal creation requires a compatible goal-tool integration. |
| [discernment-nudge](discernment-nudge/SKILL.md) | Add one brief set of fact-checking or reasoning questions after a substantive answer when its exclusions do not apply. |
| [doc-coauthoring](doc-coauthoring/SKILL.md) | Guide substantial documentation, proposal, or specification work through iterative co-authoring. Its current workflow contains Claude-specific artifact and sub-agent steps. |
| [grilling](grilling/SKILL.md) | Stress-test a plan, decision, or idea when the user explicitly asks to be grilled. Its fact-gathering procedure assumes sub-agent support. |
| [internal-comms](internal-comms/SKILL.md) | Draft internal status reports, leadership updates, newsletters, FAQs, project updates, and incident reports using the matching example. |
| [migrate-to-rust](migrate-to-rust/SKILL.md) | Plan and execute legacy-codebase migrations to Rust when the required repository access and Rust toolchain are available. |
| [pdf](pdf/SKILL.md) | Read, extract, create, convert, annotate, or fill PDF files. |
| [philosophy-religion-asceticism](philosophy-religion-asceticism/SKILL.md) | Research philosophy, religion, theology, asceticism, and contemplative traditions. |
| [prompt-master](prompt-master/SKILL.md) | Create, repair, adapt, or optimize prompts for a specified AI tool. Do not use for general coding or document writing. |
| [skill-creator](skill-creator/SKILL.md) | Create or improve skills and evaluate skill behavior or trigger descriptions. Use Agent Skill Authoring for repository format and integration. Its current evaluation workflow includes Claude/Cowork-specific steps. |
| [theme-factory](theme-factory/SKILL.md) | Apply or create visual themes for slides, documents, and other artifacts. |
| [xlsx](xlsx/SKILL.md) | Read, create, edit, validate, or convert spreadsheet files and tabular data. |


## Foundational initialization

[SESSION_START.md](../SESSION_START.md) is the sole authority for activation cues and foundational loading. The Worker owns the mandatory collaboration and session-continuity rules.

Do not treat this index as permission to load every skill. Follow each skill's activation and dependency rules.

## Technical documentation standard

All skill documentation and technical documentation must follow the [repository ASD-STE100 policy](asd-ste100/references/repository-writing-policy.md). Use the correct mode for the document type. Preserve meaning and technical precision.
