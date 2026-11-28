# Novel Production Workflow

**Current standard:** 1.1  
**Applies to:** All novel projects stored in this repository  
**Canonical workspace:** `area/novel/` on branch `gpt`

This document governs novel planning, structure, writing, illustration, revision, and maintenance. The [workspace README](README.md) is the quick reference. The [Romantic Storyteller skill](../../.agent/skills/romantic-storyteller-visual-artist/SKILL.md) defines role-specific creative and visual procedures. Reusable templates live in that skill's `assets/` directory. If this workflow conflicts with an older template, use the current Version 1.1 template.

## 1. Governing principles

1. **The user's latest explicit instruction has priority.** Preserve approved constraints unless the user changes them.
2. **The novel record is the central story index and continuity authority.** Store detailed information in the appropriate child or support record.
3. **Separate canon from proposals.** A suggestion, brainstorm, outline, draft, or unanswered question is not approved story fact merely because it appears in a file.
4. **Approval is scoped.** Promote only the decision that the user presented and approved. Keep unapproved implementation details, scene choices, and adjacent questions open.
5. **Do not force premature decisions.** Keep unresolved matters in the novel's `open-discussion.md`. Revisit them when a writing decision depends on them.
6. **Take creative responsibility when delegated.** Make low-risk craft decisions without asking the user to select every detail. Consult the user about consequential changes to the premise, identity, relationship direction, major plot causality, or ending.
7. **Do not create empty structure.** Create records when the story needs them, not merely because a template exists.
8. **Preserve provenance and truth.** Never claim that an image was generated, a reference was used, a file was stored, or an artifact was verified without supporting evidence.

## 2. Authority and decision states

### 2.1 Source priority

Resolve conflicts in this order:

1. Applicable safety requirements and the user's latest explicit instruction.
2. User-approved decisions in the novel's authoritative records.
3. Established facts in relevant novel, character, arc, and scene records.
4. Proposals and working outlines that are clearly marked as provisional.
5. The assistant's new creative suggestions.

A lower-priority source cannot silently overwrite a higher-priority source. If approved facts conflict, preserve both in the audit trail. Raise the conflict for resolution instead of guessing.

### 2.2 Canon state

Use these terms consistently in prose and metadata:

- **Approved / Established:** The user explicitly accepted it or directly established it.
- **Partly Established:** The broad direction is established. Material components remain proposed or open.
- **Proposed:** A suggested direction that awaits a decision.
- **Open:** Intentionally undecided.
- **Superseded:** A later decision replaced the former approved or active state. Preserve its history. Do not treat it as current.

A working outline may contain approved premises and proposed scene beats. Label each material section. Do not label the entire outline as canon because the user approved its broad direction.

### 2.3 Approval procedure

When the user approves a proposal:

1. Identify the exact scope of approval.
2. Update the relevant detailed record.
3. Update the novel-level summary or continuity record when the decision changes governing facts.
4. Remove the resolved item from the open-question list or mark it resolved. Keep any open subquestions.
5. Add a dated decision or revision entry.
6. Read back every changed file. Verify its links and status.

Approval of a direction does not approve every example, dialogue line, technical mechanism, or scene detail used to explain it.

## 3. Artifact system and hierarchy

### 3.1 Narrative hierarchy

**Novel → Story Arc → Scene → Illustration asset**

An illustration asset is a visual deliverable. It is not a prose level between scene and arc. Each illustration asset has two companion records: an **Illustration Note** and an **Illustration Prompt Record**.

A chapter is an optional editorial grouping of scenes for manuscript presentation. It is not a mandatory folder or hierarchy level. Create chapter records only when the project benefits from explicit chapter planning.

### 3.2 Core and supporting records

| Record | Requirement | Responsibility |
|---|---|---|
| `novel.md` | Required for each active novel | Foundation, macrostructure, indexes, timeline, continuity, status |
| `open-discussion.md` | Required for each active novel | Proposals, unresolved questions, decisions reserved for later consultation |
| Character profile | Optional, created when useful | Detailed biography, psychology, voice, goals, relationships, continuity |
| Development outline | Optional, created when useful | Focused planning for relationships, plot mechanisms, world, technology, or themes |
| `arc.md` | Required when a story arc is created | Arc purpose, progression, turning points, outcome, scene index |
| `scene.md` | Required when a scene is created | Scene metadata, dramatic design, complete scene prose, continuity, illustration index |
| Illustration Note | Required for each generated illustration retained or reviewed as a scene deliverable | Visible content, narrative context, continuity, asset link |
| Illustration Prompt Record | Required before the first generation attempt for each planned illustration | Exact authored prompt, references, provenance, attempts, and outcomes |

The novel file may contain concise character profiles. Create separate character files when the detail exceeds the novel record or needs independent continuity tracking. Do not create a character file only to satisfy a template field.

A development outline is a planning aid, not a new hierarchy level. Examples include relationship progression, a separation mechanism, a character arc, a research brief, or technology design. Its proposals remain provisional until approved.

### 3.3 Information ownership

- `novel.md` owns the novel-wide summary, master indexes, approved decisions, and continuity overview.
- `open-discussion.md` owns unresolved questions and their current status. It links to proposals instead of duplicating full outlines.
- Character profiles own detailed character information. `novel.md` keeps the concise summary and link.
- Development outlines own focused planning work. Promote approved decisions to the novel or relevant arc or character record.
- `arc.md` owns arc-level design and indexes its scenes.
- `scene.md` owns the scene prose and scene-specific continuity.
- Illustration Notes describe the actual image. Prompt Records document its authorship and generation.

Do not duplicate full scene prose in an arc or novel summary. Do not duplicate full character biographies across records. Do not copy full prompt histories into a global prompt archive.

### 3.4 Illustration binary storage and takeout hand-off

Keep illustration documentation beside its scene. Store binary image assets in one central library per novel:

`area/novel/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`

Each retained illustration has two binary files beside one another. The original PNG or JPEG is the master. The WebP file is its delivery derivative. The master is the source of truth. WebP is a separate derivative. Stable illustration IDs do not change when titles or filenames change.

All user-uploaded images enter the single flat intake at `.takeout/images/`. This rule applies to novel and non-novel images. Incoming filenames may be arbitrary. The assistant inspects each image and determines its descriptive title and destination from the conversation and project records. The assistant then writes `.takeout/images/HANDOFF.yml`.

A novel-illustration entry identifies its `ILL-NNN` ID, title, exact uploaded filename, and destination directory. The destination must be inside the appropriate novel asset library. Non-novel retained images use the shared destination `.takeout/images`.

The existing GitHub Action reads the hand-off. It does not infer image contents, IDs, or story destinations. It converts the supplied title to a slug. It prefixes the optional stable ID and converts PNG or JPEG to WebP.

Before relocation, the Action stages each derivative under `.takeout/images/webp/[batch-id]/attempt-NNN/`. It appends `.webp` to the exact incoming filename. For example, it converts `IMG_001.png` to `IMG_001.png.webp`.

The Action validates every staged file before it moves any original. It moves the original bytes unchanged to the named master location. It moves each staged WebP beside its master. It refuses to overwrite an existing destination.

Every successful or failed attempt produces an archived hand-off, `conversion-report.csv`, and `verification-report.md`. The archive path is `.takeout/images/history/[batch-id]/attempt-NNN/`. The report records source, staging, and final paths. It also records sizes, encoder profile and version, SHA-256 values, and verification outcomes.

The `history/`, `original/`, and `webp/` directories are reserved. The intake detector excludes them from future intake detection. On success, the Action moves staged files to their permanent destinations. It then removes the empty successful staging directory.

On failure, original uploads and the ready hand-off remain available. Successfully converted WebPs stay in that attempt's staging folder for inspection. A retry uses a new attempt number. It does not overwrite previous staging.

The Action resets the active hand-off only after it verifies every master and WebP. It must also write the archived records before it clears the hand-off.

For every stored illustration, link the central master and WebP paths from its Illustration Note and scene index. Keep the Illustration Note and Prompt Record in the scene-local `illustrations/` directory. Do not store image binaries there.

## 4. File and folder conventions

Use one folder per novel, one folder per arc, and one folder per scene. Use the [skill-owned template index](../../.agent/skills/romantic-storyteller-visual-artist/assets/README.md) for canonical templates. Do not create a project-local `templates/` directory.

```text
area/novel/
├── README.md
├── WORKFLOW.md
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
    │               ├── [ILL-ID]-[descriptive-slug].png
    │               └── [ILL-ID]-[descriptive-slug].webp
    └── Arc-01/
        ├── arc.md
        └── Scene-001/
            ├── scene.md
            └── illustrations/
                ├── [Illustration-ID].md
                └── [Illustration-ID]-prompt.md
```

The scene-local `illustrations/` folder stores documentation only. Image binaries use the central `assets/illustrations/[ARC-ID]/[SCN-ID]/` path shown above. All user uploads enter through `.takeout/images/` and its structured hand-off. Do not upload directly into a final asset directory.

Create optional `planning/`, `characters/`, arc, scene, and illustration folders only when they contain real records or assets. Existing projects may retain their current paths. Use the standard structure for new records. Migrate old paths only when useful and safe.

### 4.1 IDs and names

Use stable IDs:

- Novel: `NOV-001`
- Character: `CH-001`
- Story arc: `ARC-001`
- Scene: `SCN-001`
- Illustration: `ILL-001`
- Development outline: `OUT-001`
- Decision: `DEC-001` when a decision register needs stable references

IDs are unique within their project. They do not change when a title or filename changes. Folder sequence labels may use `Arc-01` and `Scene-001`. The record itself retains its stable ID.

Use descriptive, stable filenames and relative Markdown links. Update all inbound links and parent indexes when you move or rename a file.

## 5. Workflow stages

### Stage A — Project foundation

1. Create the novel folder only for a real project.
2. Create `novel.md` and `open-discussion.md` from the current templates.
3. Record the premise, intended genre, core reader experience, main characters, central relationship, stakes, and ending direction. Record only what is known.
4. Mark the title, setting, character details, plot mechanisms, and other undecided elements as open. Do not invent them as facts.
5. Establish stable IDs. Link the project from `area/novel/README.md`.

**Foundation deliverable:** a usable novel foundation and an open-discussion register. A complete biography, world encyclopedia, or chapter plan is not required.

### Stage B — Focused development

1. Identify the next consequential story question.
2. Create a Development Outline only when a focused plan needs a durable record.
3. Distinguish approved direction from proposed beats and unresolved implementation questions.
4. Explore causality, character agency, emotional credibility, technical consistency, and consequences.
5. When the user approves a direction, promote only that decision to the appropriate authoritative records.

**Development deliverable:** the focused outline, updated novel summary, and accurate open-discussion note.

### Stage C — Macrostructure and arc planning

1. Define the novel's large movements only as far as the premise requires.
2. Create an `arc.md` when the arc has a clear purpose and enough direction for planning.
3. Give each arc a beginning condition, character or relationship movement, escalation, turning point, climax, resolution, and carry-forward consequence.
4. Create scene records only when scenes are ready for planning or drafting.
5. Update the novel's arc directory and the arc's scene directory.

**Arc deliverable:** an arc outline with a coherent scene sequence. Do not mark it complete while major sections remain proposed.

### Stage D — Scene design and prose

1. Read the current novel record, relevant character records, parent arc, open decisions, and target scene before writing.
2. Decide whether the task continues the same event or needs a new scene. Do not split or merge scenes only to fit a chapter count.
3. Draft the scene brief. Write the **complete scene prose** in the Scene Prose section of `scene.md`. Planning headings do not replace narrative prose.
4. Use action, dialogue, sensory detail, subtext, and a clear emotional or dramatic turn. Do not replace a requested scene with a synopsis or outline.
5. Update continuity and parent indexes only where needed.
6. Keep scene status accurate: Planned → Outlined → Drafted → Revised → Approved/Complete. Do not call a draft approved without the required approval.

**Scene deliverable:** the complete scene file, including actual prose, metadata, continuity, and the correct parent index.

### Stage E — Illustration and visual records

The current default for novel scene work includes at least one standalone illustration. This applies when the user asks to create, write, draft, continue, expand, or substantially revise a specific scene.

Exceptions:

- The user explicitly requests prose-only, text-only, or no images.
- The task is discussion, brainstorming, structural planning, or outline work. It does not write or revise a scene.
- A genuine safety or technical prerequisite blocks image generation.

A missing optional inspiration image is not a blocker for fresh text-to-image generation. This applies when the written brief and continuity are sufficient.

For every planned illustration:

1. Select the most meaningful visual beat from the scene and continuity context.
2. Create its scene-local Illustration Prompt Record **before** the generation attempt.
3. Record the exact authored prompt, acceptance criteria, references actually attached, and intended changes. Do not claim access to a hidden compiled payload.
4. Generate or edit under the Drawing Skill's rules.
5. Inspect each returned image separately against the brief. Classify each result honestly.
6. Create or update an Illustration Note for each generated image retained or reviewed as a scene deliverable. Record visible facts separately from interpretation.
7. Record every attempt and outcome in the Prompt Record. Include failed and partial attempts. Preserve the accepted baseline and the exact changes in later attempts.
8. For repository retention, place the uploaded image in `.takeout/images/`. Prepare its `HANDOFF.yml` entry with the incoming filename, descriptive title, stable illustration ID, and central asset destination. Do not rename or move the upload manually. The existing Action performs the validated master rename, WebP conversion, relocation, and verification.
9. Link the verified master and WebP assets, Illustration Note, Prompt Record, and scene. If an image exists only in the conversation, state that clearly. Do not invent a repository path.
10. Update the scene's illustration index. A generated image does not create a new scene automatically.

The Drawing Skill governs visual mode, reference handling, prompt archival, image generation and editing, inspection, and recovery. It requires prompt archival before each attempt. The Romantic Storyteller skill must not override it.

**Visual deliverable:** image output, scene-local prompt record, Illustration Note, and updated scene index, unless an exception applies. If blocked, report the blocker. Leave the visual deliverable outstanding.

### Stage F — Revision, continuity, and completion

Before marking an arc or scene complete:

1. Check character motivation, agency, voice, relationship progression, chronology, location, world rules, and cause and effect.
2. Check that all approved facts and locked constraints remain intact.
3. Check that no proposal became canon without approval.
4. Check that scene, arc, and novel summaries agree. Do not duplicate full prose.
5. Check illustration links, prompt history, image provenance, and visual continuity where relevant.
6. Update statuses and parent indexes.
7. Read back every changed repository file. Verify its contents and links.

A project is **Completed** only when the planned narrative has been delivered. Review the ending and continuity. Complete outstanding deliverables or record them as waived or not applicable.

## 6. Deliverables by request type

| User request | Normal deliverable | Do not create by default |
|---|---|---|
| Brainstorm or discuss | Direct response. Optionally identify a proposal and its open points | New scene, arc, or image |
| Save a decision or discussion | Updated `open-discussion.md` and relevant authoritative summary | Unrequested prose scene |
| Develop a focused plot, relationship, or world question | Development Outline when a durable plan helps, plus updated open questions | Locked arc or scene without approval |
| Approve a proposal | Decision promoted to canon in relevant records. Retain open subquestions | Approval of adjacent details not presented |
| Plan a story arc | `arc.md`, scene sequence, and parent index update | Full scene prose unless requested |
| Write, continue, or revise a specific scene | Complete `scene.md` prose and continuity updates. At least one illustration by default | New arc or chapter unless needed |
| Explicit prose-only scene request | Complete scene prose and continuity updates | Image generation, prompt log, illustration note |
| Request an illustration for an existing scene | Image generation or edit, prompt record, note, and scene index update | New scene unless requested |
| Character development | Updated novel summary or character profile. Optional development outline | Fixed biography from a passing possibility |
| Review or audit the novel workflow | Updated workflow documentation and affected templates or records | Story scenes or illustrations |

Deliver only records relevant to the task. Do not create an artifact only because a template exists.

## 7. Status conventions

Keep progress status separate from canon status.

### Novel
`Concept` · `Planning` · `In Progress` · `Completed` · `On Hold`

### Arc
`Planned` · `Outlined` · `In Progress` · `Completed` · `Superseded`

### Scene
`Planned` · `Outlined` · `Drafted` · `Revised` · `Approved` · `Complete` · `Superseded`

### Character profile
`Working` · `Ready for Review` · `Approved` · `Superseded`

### Development outline
`Working` · `Ready for Review` · `Approved Direction` · `Superseded`

### Open discussion
`Active` · `Archived`

### Illustration
`Planned` · `Generated` · `Reviewed` · `Approved` · `Superseded`

### Illustration Prompt Record
`Prepared` · `Attempts in Progress` · `Reviewed` · `Approved` · `Superseded`

Use lowercase kebab-case equivalents in YAML frontmatter. Examples: `ready-for-review` and `attempts-in-progress`. A template's frontmatter status indicates its approval. When you copy a template, set the new record's status to its correct starting state.

Use a separate canon-state label when needed. A drafted scene may contain provisional story details. Its existence does not make every detail approved canon.

## 8. Quality gates

### Story gate

- The scene or arc changes something. It is not merely decorative.
- Character choices arise from established motives and pressures.
- Maya or AI characters retain agency and distinct interiority where applicable.
- Actions and consequences earn emotional development.
- Major turns have credible causes and lasting effects.
- The ending follows the approved direction.

### Continuity gate

- Names, identities, ages, relationships, appearances, abilities, and world rules match approved records.
- Chronology and geography remain coherent.
- No unresolved question is treated as fact.
- No higher-level summary contradicts a detailed approved record.

### Visual gate

- The chosen moment belongs to the scene.
- Locked identity, face, hair, wardrobe, and other constraints remain intact.
- Visible facts and interpretive meaning remain distinct.
- Prompt, references, output, and assessment have honest provenance.

### Repository gate

- Use the correct branch and path.
- Fetch the current file before replacement.
- Preserve existing material unless the task requires a change.
- Update parent links and indexes.
- Read back each file after writing.
- Report commit IDs and file paths only after verification.

## 9. Versioning and legacy records

Version 1.1 is the current standard. Version 1.0 templates remain as historical references for records created under that format.

- Use Version 1.1 templates for new records.
- When you materially revise an existing record, migrate it to 1.1 if the new structure applies. Do not force migration of untouched legacy records.
- Never mass-rewrite completed scenes or approved artwork only to change a template version.
- If a template change affects the workflow, update this document, `README.md`, and the Romantic Storyteller skill in the same change set.
- Record format and version metadata in each document. Preserve stable IDs and approved content during migration.

## 10. Definition of done for repository work

A documentation or story-record task is complete only when:

- The correct artifacts are created or updated.
- Every new document uses the current template or records a justified exception.
- Statuses distinguish drafts, proposals, and approved material.
- All affected parent and cross-document links are updated.
- Stale statements and contradictory instructions are removed.
- You fetch the changed files again from the target branch. Verify their critical content.
- The final report names the updated files and any remaining open questions accurately.

## Technical documentation standard

This workflow contains operational instructions. Apply Strict mode from the repository [ASD-STE100 policy](../../.agent/skills/asd-ste100/references/repository-writing-policy.md) when you revise it. Preserve novel canon, approval scope, and narrative meaning.
