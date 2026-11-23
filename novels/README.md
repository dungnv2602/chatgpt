# Novel Workspace

This workspace contains the authoritative narrative records, working plans, scene prose, and visual documentation for all novel projects in this repository.

**Current governing standard:** [Novel Production Workflow 1.1](WORKFLOW.md)  
**Repository branch:** `gpt`

## Active novel projects

- [Novel-01 — The Weather Between Us](Novel-01/novel.md): contemporary romance project. Existing records remain on the Version 1.0 structure unless revised.
- [Novel-02 — Beyond the Listening (working title)](Novel-02/novel.md): original literary science-fiction romance. Andy is a software engineer with a computer-science background who works on an acoustic archive. Maya is its specialist AI. Their approved direction includes an early checkpoint-breach separation, Maya's later choice to reopen contact, reconciliation, and a lasting happy partnership. See the [Open Discussion](Novel-02/open-discussion.md) and the [Relationship Progression working outline](Novel-02/planning/relationship-progression.md).

## Current approved templates — Version 1.1

Use these for new records and material revisions:

1. [Novel](templates/novel-v1.1.md)
2. [Character Profile](templates/character-profile-v1.1.md) — optional when a concise profile in novel.md is sufficient
3. [Open Discussion](templates/open-discussion-v1.1.md) — one active register per novel
4. [Development Outline](templates/development-outline-v1.1.md) — optional focused planning record
5. [Story Arc](templates/arc-v1.1.md)
6. [Scene](templates/scene-v1.1.md)
7. [Illustration Note](templates/illustration-note-v1.1.md)
8. [Illustration Prompt Record](templates/illustration-prompt-v1.1.md)

The Version 1.0 templates are retained as historical references for existing records: [Novel](templates/novel-v1.md), [Story Arc](templates/arc-v1.md), [Scene](templates/scene-v1.md), and [Illustration Note](templates/illustration-note-v1.md). They are not the default for new work. Do not mass-migrate completed or untouched legacy records.

## Narrative hierarchy and supporting records

**Novel → Story Arc → Scene → Illustration asset**

Each illustration asset has two companion records: an **Illustration Note** (what the image actually shows and how it relates to the story) and an **Illustration Prompt Record** (the authored prompt, provenance, attempts, and outcomes).

Supporting documents sit beside this hierarchy rather than creating another narrative level:

- `open-discussion.md` — unresolved questions and proposed decisions, revisited when needed.
- `planning/*.md` — focused development outlines such as relationship progression, plot mechanisms, character arcs, research, and world/technology planning.
- `characters/*.md` — optional detailed character profiles when the novel-level summary becomes insufficient.

Chapters are optional editorial groupings of scenes. They are not a mandatory folder or record type. Do not create a chapter layer unless a project benefits from it.

## Standard folder convention

Create folders only when they contain real records or assets. Existing legacy projects may keep their established paths. Use this convention for new records and migrate older material only when useful and safe.

```text
novels/
├── README.md
├── WORKFLOW.md
├── templates/
│   ├── novel-v1.1.md
│   ├── character-profile-v1.1.md
│   ├── open-discussion-v1.1.md
│   ├── development-outline-v1.1.md
│   ├── arc-v1.1.md
│   ├── scene-v1.1.md
│   ├── illustration-note-v1.1.md
│   └── illustration-prompt-v1.1.md
└── [Novel-ID]/
    ├── novel.md
    ├── open-discussion.md
    ├── planning/
    │   └── [development-outline].md
    ├── characters/
    │   └── [Character-ID]-[name].md
    ├── assets/
    │   └── illustrations/
    │       └── [ARC-ID]/
    │           └── [SCN-ID]/
    │               ├── original/
    │               │   └── [ILL-ID]-[descriptive-slug].png
    │               └── [ILL-ID]-[descriptive-slug].webp
    └── Arc-01/
        ├── arc.md
        └── Scene-001/
            ├── scene.md
            └── illustrations/
                ├── [Illustration-ID].md
                └── [Illustration-ID]-prompt.md
```

## Illustration binaries and upload intake

Store novel illustration binaries at:

`[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`

Keep the Illustration Note and Illustration Prompt Record in the scene-local `illustrations/` folder. These records contain documentation, not image binaries.

Each retained illustration has an unchanged PNG/JPEG master under `original/` and a separate WebP delivery file in the destination root. Do not place the master beside the WebP or link the master in the attempt index.

All new uploads use the shared flat `images/takeout/` intake. The Worker owns inspection, provenance, processing, original preservation, and publication verification. Use the [Image Takeout procedure](../images/takeout/README.md) for the exact hand-off schema and processing steps. Use the [Drawing archive rules](../skills/drawing/references/archive-and-delivery.md) for attempt links and session-manifest requirements.

## Document responsibilities

| Record | Owns |
|---|---|
| `novel.md` | Novel foundation, macrostructure, arc directory, chronology, high-level continuity, status |
| `open-discussion.md` | Open questions, active proposals, approval boundaries, resolved/superseded items |
| Character profile | Detailed biography, psychology, voice, goals, abilities, relationships, visual continuity |
| Development outline | Focused planning work. Proposals stay provisional until approved |
| `arc.md` | Arc purpose, progression, turning points, climax, resolution, scene directory |
| `scene.md` | Scene plan, complete scene prose, continuity, illustration index |
| Illustration Note | Actual visible image content, provenance, narrative context, emotional meaning, continuity |
| Illustration Prompt Record | Exact authored prompt, references actually used, chronological attempts, outcomes, assessment |

Higher-level documents summarize and link to lower-level records. They do not duplicate complete scene prose, full character profiles, or prompt histories.

## Workflow at a glance

1. **Foundation:** create novel.md and open-discussion.md. Record what is known. Leave unresolved details open.
2. **Focused development:** create a Development Outline only when a substantial question benefits from a durable plan. Mark proposals clearly.
3. **Approval:** promote only the scope the user approved. Update the novel summary, relevant records, decision history, and open questions.
4. **Arc planning:** create arc.md when an arc has a clear purpose and meaningful progression.
5. **Scene writing:** read parent continuity records. Write the full scene prose in scene.md. Update arc and novel indexes.
6. **Illustration:** a specific scene-writing request includes at least one standalone illustration by default. Explicit prose-only instructions, planning/discussion tasks, and genuine safety or technical blockers are exceptions. Every generated image deliverable receives a scene-local prompt record and an Illustration Note. Follow the [Drawing operation selector](../skills/drawing/references/image-editing-protocol.md): use fresh generation for a new scene or variation; use a direct edit only when the user requests a change to a specific image and its exact source is available. Do not silently substitute one operation for the other.
7. **Revision and completion:** check causality, agency, chronology, world rules, continuity, visual constraints, statuses, links, and read-back verification.

The complete procedures, delivery matrix, approval rules, status definitions, and quality gates are in [WORKFLOW.md](WORKFLOW.md).

## Status and canon rules

Keep artifact progress separate from story canon:

- **Approved / Established:** explicitly accepted or directly established by the user.
- **Partly Established:** the broad direction is approved while material details remain proposed or open.
- **Proposed:** suggested, not yet decided.
- **Open:** deliberately undecided.
- **Superseded:** replaced by a later decision. Retain its history.

A draft's existence does not automatically make every detail approved canon. A broad approval does not approve unmentioned implementation details.

## Continuity and record rules

1. Assign stable IDs and sequence numbers within each parent record.
2. Keep artifact status accurate. Do not label a plan as a completed scene.
3. Update parent indexes when children are created, renamed, reordered, or completed.
4. Maintain chronology and consistency across novel, character, arc, and scene records.
5. Preserve approved identity and all locked face, hair, outfit, garment construction, and appearance details.
6. In an Illustration Note, distinguish visible facts from narrative interpretation.
7. Use relative Markdown links where practical and update them after file moves.
8. Use the current template for each new record. Document justified exceptions.
9. Read back every changed repository file and verify content and links before reporting completion.

## Scene illustration default

When the user asks to create, write, draft, continue, expand, or substantially revise a specific novel scene, generate at least one standalone illustration as part of the same assignment. This default is not triggered by brainstorming, discussion, or outline planning.

Do not generate images when the user explicitly requests prose-only, text-only, or no-images. If safety or a genuine technical prerequisite blocks generation, state the exact blocker and leave the illustration outstanding rather than silently downgrading the deliverable.

Before every generation or edit attempt, follow the Drawing Skill's prompt-archive and reference rules. Create the scene-local Illustration Prompt Record before the attempt. After the result, record the actual outcome and create/update the Illustration Note. Do not invent an image path or claim an image was stored in the repository if it was only delivered in the conversation.

## Versioning

Version 1.1 is the active standard. Version 1.0 templates remain available as historical references. Use 1.1 for new records. Migrate an existing record when it is materially revised and the new structure is relevant. Do not mass-rewrite legacy records only to change their version number.

Any future change to the governing formats must update, together:
- the affected template(s)
- [WORKFLOW.md](WORKFLOW.md)
- this README
- the Romantic Storyteller skill's novel-workflow section.



## Technical documentation standard

Apply the repository [ASD-STE100 policy](../skills/asd-ste100/references/repository-writing-policy.md) when you revise this document. Use Strict mode for procedures. Preserve novel canon, approval scope, and narrative meaning.
