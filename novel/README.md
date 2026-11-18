# Novel Workspace

This directory contains the structured narrative records for Maya & Me novels.

## Approved format set

The following formats are approved as **Version 1.0** for now:

1. Novel — [template](templates/novel-v1.md)
2. Story Arc — [template](templates/arc-v1.md)
3. Scene — [template](templates/scene-v1.md)
4. Illustration Note — [template](templates/illustration-note-v1.md)

These formats are stable starting points, not immutable schemas. Revise them deliberately when a real writing need emerges. Record the version and update the Romantic Storyteller skill when the governing workflow changes.

## Narrative hierarchy

**Novel → Story Arc → Scene → Illustration → Illustration Note**

- A novel contains multiple story arcs.
- A story arc contains multiple scenes.
- A scene may have multiple illustrations, and every worked scene is illustrated by default: when the user asks to create, write, continue, expand, or substantially revise a specific novel scene, generate at least one standalone illustration without waiting for a separate drawing request.
- Every illustration note belongs to one specific scene.
- A new illustration does not automatically create a new scene. Explicit prose-only requests, discussion/brainstorming that does not work on a scene, and genuine safety or technical blockers are exceptions to automatic generation; report any blocker plainly.

## Information ownership

Each document owns its detailed information. Higher-level documents summarize and link to lower-level records rather than duplicating them. The novel document is the central index and continuity reference for the complete novel.

## Folder convention

Create one folder per novel. Within each novel, create one folder per arc; within each arc, one folder per scene. Store a scene's illustration notes in that scene's illustrations subfolder.

```text
ChatGPT/
└── novel/
    ├── README.md
    ├── templates/
    │   ├── novel-v1.md
    │   ├── arc-v1.md
    │   ├── scene-v1.md
    │   └── illustration-note-v1.md
    ├── Novel-01/
    │   ├── novel.md
    │   ├── Arc-01/
    │   │   ├── arc.md
    │   │   └── Scene-001/
    │   │       ├── scene.md
    │   │       └── illustrations/
    │   │           ├── illustration-01.md
    │   │           └── illustration-01-prompt.md
    │   └── Arc-02/
    │       ├── arc.md
    │       └── ...
    └── Novel-02/
        └── novel.md
```

The example novel, arc, scene, and illustration names are placeholders. Do not create empty novel folders or fictional story records until a real novel is started.

## Document responsibilities

- **novel.md:** identity, premise, themes, narrative approach, characters, story world, central conflict and stakes, overall structure, arc directory, timeline, continuity, visual direction, and progress.
- **arc.md:** the arc's purpose, starting point, character development, progression, turning points, climax, resolution, scene directory, and connection to the novel.
- **scene.md:** one continuous narrative event, its purpose, opening situation, development, central moment, ending, continuity, and its illustrations.
- **illustration note:** image provenance and prompt link, objective visual description, narrative context, emotional meaning, continuity, and connection to the scene.

## Record and continuity rules

1. Assign stable IDs and sequence numbers within their parent record.
2. Keep status values current; do not mark planned material as completed.
3. Distinguish observable visual facts from narrative interpretation. The Visual Description section of an illustration note records only what is visible; Narrative Context and Emotional Meaning record interpretation.
4. Preserve established character identity and all locked appearance and wardrobe details.
5. Link records using relative Markdown links where practical.
6. Update parent indexes when child records are created, renamed, reordered, or completed.
7. Keep chronology coherent across novel, arc, and scene records.
8. Do not duplicate full scene prose in an arc summary or full arc summaries in the novel overview.
9. Use the relevant template as the starting point for every new record.


## Automatic scene illustration

Illustration is a default deliverable of scene work, not an optional follow-up.
When the user asks to create, write, continue, expand, or substantially revise
a specific scene in an established novel, autonomously select and generate at
least one standalone illustration as part of the same assignment. Do not wait
for a separate request to draw or illustrate the scene. Choose the most
meaningful visual beat from the scene and its continuity context. If several
distinct moments materially benefit from illustration, use creative judgment
to create a small set of separate images; do not combine them into a collage
or comic page unless explicitly requested.

This default is waived only for an explicit prose-only/text-only/no-images
instruction, a discussion or brainstorming task that is not actually working
on a scene, or a genuine safety or technical blocker.
When blocked, state the exact reason and leave illustration clearly marked as
outstanding rather than silently delivering text alone.

Every generated image receives its own illustration note in that scene's
`illustrations/` subfolder, using the approved Illustration Note v1.0
template, and its own scene-local prompt record named
`[Illustration-ID]-prompt.md` in the same folder. The local prompt record
keeps the exact authored prompt and links to the dated chronological attempt
in `prompts/`; the illustration note links to both. Keep the chronological
log as the project-wide history rather than moving or replacing it. After
generation, update both prompt records with the actual direction submitted
when known, outcome, deviations, and continuity assessment. Clearly
distinguish authored prompt text from any compiled tool payload that is not
exposed. Follow the Drawing Skill's mandatory pre-attempt prompt archival,
continuity, generation, inspection, and outcome-recording workflow. An
attached character image is optional for fresh text-to-image generation when
the approved written prompt fully specifies the locked character design.
