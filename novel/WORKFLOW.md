# Novel Production Workflow

**Current standard:** 1.1  
**Applies to:** All novel projects stored in this repository  
**Canonical workspace:** `novel/` on branch `gpt`

This document is the governing procedure for planning, structuring, writing, illustrating, revising, and maintaining a novel. The [workspace README](README.md) is the quick reference; the [Romantic Storyteller skill](../skills/romantic-storyteller-visual-artist/SKILL.md) supplies role-specific creative and visual procedures. Where this workflow and an older template disagree, use the current Version 1.1 template.

## 1. Governing principles

1. **The user's latest explicit instruction has priority.** Preserve all previously approved constraints unless the user explicitly changes them.
2. **The novel record is the central story index and continuity authority.** Detailed information belongs in its appropriate child or support record.
3. **Separate canon from proposals.** A suggestion, brainstorm, outline, draft, or unanswered question does not become approved story fact merely because it appears in a file.
4. **Approval is scoped.** When the user approves a proposal, promote only the decision actually presented and approved. Keep implementation details, scene choices, and adjacent questions open unless they were also approved.
5. **Do not force premature decisions.** Keep unresolved matters in the novel's `open-discussion.md`; revisit them when the next writing decision depends on them.
6. **Take creative responsibility when delegated.** Make low-risk craft decisions without asking the user to select every detail. Consult the user on consequential decisions that alter the premise, character identity, relationship direction, major plot causality, or ending.
7. **Do not create empty structure.** Create records when the story needs them, not merely because a template exists.
8. **Preserve provenance and truth.** Never claim that an image was generated, a reference was used, a file was stored, or an artifact was verified unless the relevant result supports that claim.

## 2. Authority and decision states

### 2.1 Source priority

Resolve conflicts in this order:

1. Applicable safety requirements and the user's latest explicit instruction.
2. User-approved decisions recorded in the novel's authoritative records.
3. Established facts in the relevant novel, character, arc, and scene records.
4. Proposals and working outlines, clearly marked as provisional.
5. The assistant's new creative suggestions.

A lower-priority source cannot silently overwrite a higher-priority one. When two approved facts conflict, preserve both in the audit trail and raise the conflict for resolution rather than guessing.

### 2.2 Canon state

Use these terms consistently in prose and metadata:

- **Approved / Established:** explicitly accepted by the user or otherwise directly established by the user's instruction.
- **Partly Established:** the broad direction is established, but material components remain proposed or open.
- **Proposed:** a suggested direction awaiting a decision.
- **Open:** intentionally undecided.
- **Superseded:** formerly approved or active, but replaced by a later decision. Preserve its history; do not continue treating it as current.

A working outline may contain a mixture of approved premises and proposed scene beats. Label the state of each material section. Do not label an entire outline canon merely because its broad direction was approved.

### 2.3 Approval procedure

When the user approves a proposal:

1. Identify the exact scope of approval.
2. Update the relevant detailed record.
3. Update the novel-level summary/continuity record where the decision changes the novel's governing facts.
4. Remove the resolved item from the open-question list or mark it resolved; retain genuinely open subquestions.
5. Add a dated decision/revision entry.
6. Read back every changed file and verify the links and status.

Approval of a direction does not automatically approve every example, line of dialogue, technical mechanism, or scene detail used to explain it.

## 3. Artifact system and hierarchy

### 3.1 Narrative hierarchy

**Novel → Story Arc → Scene → Illustration asset**

The illustration asset is a visual deliverable, not a prose level between scene and arc. Each illustration asset has two companion records: an **Illustration Note** and an **Illustration Prompt Record**.

A chapter is an optional editorial grouping of scenes for manuscript presentation. It is not a mandatory folder or additional hierarchy level. Create chapter records only when the project genuinely benefits from explicit chapter planning.

### 3.2 Core and supporting records

| Record | Requirement | Responsibility |
|---|---|---|
| `novel.md` | Required for each active novel | Foundation, macrostructure, indexes, timeline, continuity, status |
| `open-discussion.md` | Required for each active novel | Proposals, unresolved questions, decisions reserved for later consultation |
| Character profile | Optional, created when useful | Detailed biography, psychology, voice, goals, relationships, continuity |
| Development outline | Optional, created when useful | Relationship progression, plot mechanism, world/technology plan, thematic or other focused development |
| `arc.md` | Required when a story arc is created | Arc purpose, progression, turning points, outcome, scene index |
| `scene.md` | Required when a scene is created | Scene metadata, dramatic design, complete scene prose, continuity, illustration index |
| Illustration Note | Required for each generated illustration retained or reviewed as a scene deliverable | Actual visible content, narrative context, continuity, asset link |
| Illustration Prompt Record | Required before the first generation attempt for each planned illustration | Exact authored prompt, references, provenance, chronological attempts and outcomes |

The novel file may contain concise character profiles. Create separate character files when detail becomes too extensive for the novel record or when a character needs independent continuity tracking. Do not create a separate character file merely to satisfy a template field.

A development outline is a planning aid, not a new hierarchy level. Examples include a relationship progression, separation mechanism, character arc, research brief, or technology design. Its proposals remain provisional until approved.

### 3.3 Information ownership

- `novel.md` owns the novel-wide summary, master indexes, approved decisions, and continuity overview.
- `open-discussion.md` owns unresolved questions and the record of what remains open. It links to proposals rather than duplicating entire outlines.
- Character profiles own detailed character information; `novel.md` keeps the concise summary and link.
- Development outlines own focused planning work; approved decisions are promoted to the novel or relevant arc/character record.
- `arc.md` owns arc-level design and indexes its scenes.
- `scene.md` owns the actual scene prose and scene-specific continuity.
- Illustration Notes describe the actual image; Prompt Records document how it was authored and generated.

Do not duplicate full scene prose in an arc or novel summary, full character biographies across multiple records, or full prompt histories in a global prompt archive.

### 3.4 Illustration binary storage and takeout hand-off

Keep illustration documentation beside its scene, but store binary image assets in one central library per novel:

`novel/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`

Each retained illustration has two binary files beside one another: the original PNG/JPEG master and its WebP delivery derivative. The master is the source of truth; WebP is a separate derivative. Stable illustration IDs do not change when titles or filenames are refined.

All user-uploaded images, whether novel or non-novel, first enter the single flat intake at `images/takeout/`. Incoming filenames may be arbitrary. The assistant inspects the image, determines its descriptive title and intended destination from the conversation and project records, and writes `images/takeout/HANDOFF.yml`. A novel-illustration entry identifies its `ILL-NNN` ID, title, exact uploaded filename, and destination directory under the appropriate novel asset library. Non-novel retained images use a destination under `images/`.

The existing GitHub Action reads the hand-off; it does not infer image contents, IDs, or story destinations. It slugifies the supplied title, prefixes the optional stable ID, converts PNG/JPEG to WebP, moves the original bytes unchanged to the named master location, and puts the WebP beside it. It refuses to overwrite an existing destination. All items must pass validation and conversion before any original is relocated.

Every attempt, successful or failed, produces an archived hand-off, `conversion-report.csv`, and `verification-report.md` under `images/takeout/history/[batch-id]/attempt-NNN/`. The report records file paths, sizes, encoder profile/version, SHA-256 values, and verification outcomes. History is excluded from future intake detection. The active hand-off is reset to empty only after every master and WebP is verified and the archived records have been written. A failed batch retains its ready hand-off and source images for correction and retry.

For every stored illustration, link the central master and WebP paths from its Illustration Note and scene index. Keep the Illustration Note and Prompt Record in the scene-local `illustrations/` directory; do not store the image binary there.

## 4. File and folder conventions

Use one folder per novel, one folder per arc, and one folder per scene.

```text
novel/
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

The scene-local `illustrations/` folder stores documentation only. Image binaries use the central `assets/illustrations/[ARC-ID]/[SCN-ID]/` path shown above. All user uploads enter through `images/takeout/` and are routed by its structured hand-off; do not upload directly into a final asset directory.

Only create the optional `planning/`, `characters/`, arc, scene, and illustration folders when they contain real records or assets. Existing projects may retain their current paths; use the standard structure for new records and migrate old paths only when useful and safe.

### 4.1 IDs and names

Use stable IDs:

- Novel: `NOV-001`
- Character: `CH-001`
- Story arc: `ARC-001`
- Scene: `SCN-001`
- Illustration: `ILL-001`
- Development outline: `OUT-001`
- Decision: `DEC-001` (when a decision register needs stable references)

IDs are unique within their project and do not change when a title or filename changes. Folder sequence labels may use `Arc-01` and `Scene-001`; the record itself retains its stable ID.

Use descriptive, stable filenames and relative Markdown links. Update all inbound links and parent indexes when a file is moved or renamed.

## 5. Workflow stages

### Stage A — Project foundation

1. Create the novel folder only for a real project.
2. Create `novel.md` and `open-discussion.md` from the current templates.
3. Record the premise, intended genre, core reader experience, main characters, central relationship, stakes, and ending direction to the extent known.
4. Mark the title, setting, character details, plot mechanics, and other undecided elements as open; do not invent them as facts.
5. Establish stable IDs and link the project from `novel/README.md`.

**Foundation deliverable:** a usable novel foundation and an open-discussion register. A complete biography, world encyclopedia, or chapter plan is not a prerequisite.

### Stage B — Focused development

1. Identify the next consequential story question.
2. Create a Development Outline only when a focused plan benefits from a durable record.
3. Clearly distinguish approved direction from proposed beats and unresolved implementation questions.
4. Explore causality, character agency, emotional credibility, technical/world consistency, and consequences.
5. When the user approves a direction, promote only the approved decision to the appropriate authoritative records.

**Development deliverable:** the focused outline, updated novel summary, and an accurate open-discussion note.

### Stage C — Macrostructure and arc planning

1. Define the novel's large movements only as far as the premise requires.
2. Create an `arc.md` when the arc has a clear narrative purpose and enough direction to plan.
3. Give each arc a beginning condition, character/relationship movement, escalation, turning point, climax, resolution, and carry-forward consequence.
4. Create scene records only when scenes are ready to be planned or drafted.
5. Update the novel's arc directory and the arc's scene directory.

**Arc deliverable:** an arc outline with a coherent scene sequence. Do not mark it complete while major sections are still only proposed.

### Stage D — Scene design and prose

1. Read the current novel record, relevant character records, parent arc, open decisions, and existing target scene before writing.
2. Decide whether the task continues the same continuous event or requires a new scene. Do not split or merge scenes merely to fit a chapter count.
3. Draft the scene brief and write the **complete scene prose** in the Scene Prose section of `scene.md`. Planning headings are not a substitute for narrative prose.
4. Use action, dialogue, sensory detail, subtext, and a clear emotional/dramatic turn. Do not replace a requested scene with a synopsis or outline.
5. Update continuity and parent indexes only where affected.
6. Keep scene status accurate: Planned → Outlined → Drafted → Revised → Approved/Complete. Do not call a draft approved without the relevant approval.

**Scene deliverable:** the complete scene file with its actual prose, scene metadata, continuity, and correct parent index.

### Stage E — Illustration and visual records

The current default for novel scene work is that a scene-writing request also includes at least one standalone illustration. The default applies when the user asks to create, write, draft, continue, expand, or substantially revise a specific scene in an established novel.

Exceptions:

- The user explicitly requests prose-only, text-only, or no images.
- The task is discussion, brainstorming, structural planning, or outline work rather than writing/revising a scene.
- A genuine safety or technical prerequisite blocks image generation.

A missing optional inspiration image is not, by itself, a blocker for fresh text-to-image generation when the written brief and continuity are sufficient.

For every planned illustration:

1. Select the most meaningful visual beat from the scene and continuity context.
2. Create its scene-local Illustration Prompt Record **before** the generation attempt.
3. Record the exact authored prompt, acceptance criteria, references actually attached, and intended changes. Do not claim access to a hidden compiled payload.
4. Generate/edit under the Drawing Skill's rules.
5. Inspect each returned image separately against the brief; classify the result honestly.
6. Create or update an Illustration Note for each generated image retained or reviewed as a scene deliverable. Record visible facts separately from interpretation.
7. Record every attempt and outcome in the Prompt Record, including failed or partial attempts. Preserve the accepted baseline and the precise changes made in later attempts.
8. For repository retention, place the uploaded image in `images/takeout/` and prepare its `HANDOFF.yml` entry with the incoming filename, descriptive title, stable illustration ID, and central asset destination. Do not rename or relocate the upload manually; the existing Action performs the validated master rename, WebP conversion, relocation, and verification.
9. Link the verified master and WebP assets, Illustration Note, Prompt Record, and scene. If an image is only conversation-delivered and not stored in the repository, state that plainly and do not invent a repository path.
10. Update the scene's illustration index. A generated image does not create a new scene automatically.

The Drawing Skill governs visual mode, reference handling, prompt archival before each attempt, image generation/editing, inspection, and recovery. The Romantic Storyteller skill must not override it.

**Visual deliverable:** image output, scene-local prompt record, Illustration Note, and updated scene index, unless a stated exception applies. If blocked, report the blocker and leave the visual deliverable outstanding.

### Stage F — Revision, continuity, and completion

Before marking an arc or scene complete:

1. Check character motivation, agency, voice, relationship progression, chronology, location, world rules, and cause/effect.
2. Check that all approved facts and locked constraints remain intact.
3. Check that no proposal was silently promoted to canon.
4. Check that scene, arc, and novel summaries agree without duplicating full prose.
5. Check illustration links, prompt history, image provenance, and visual continuity where applicable.
6. Update statuses and parent indexes.
7. Read back every changed repository file and verify its contents and links.

A project is **Completed** only when the planned narrative has been delivered, the ending and continuity are reviewed, and outstanding deliverables are either completed or explicitly recorded as waived/not applicable.

## 6. Deliverables by request type

| User request | Normal deliverable | Do not create by default |
|---|---|---|
| Brainstorm or discuss | A direct response; optionally identify a proposal and its open points | New scene, arc, or image |
| Save a decision or discussion | Updated `open-discussion.md` and relevant authoritative summary | Unrequested prose scene |
| Develop a focused plot/relationship/world question | A Development Outline when a durable plan is useful, plus updated open questions | A locked arc or scene without approval |
| Approve a proposal | Decision promoted to canon in relevant records; open subquestions retained | Approval of adjacent details not presented |
| Plan a story arc | `arc.md`, scene sequence, parent index update | Full scene prose unless requested |
| Write/continue/revise a specific scene | Complete `scene.md` prose and continuity updates; at least one illustration by default | A new arc or chapter unless needed |
| Explicit prose-only scene request | Complete scene prose and continuity updates | Image generation, prompt log, illustration note |
| Request an illustration for an existing scene | Image generation/edit, prompt record, note, and scene index update | A new scene unless requested |
| Character development | Update novel summary or character profile; optional development outline | A fixed biography from a passing possibility |
| Review/audit the novel workflow | Updated workflow documentation and affected templates/records | Story scenes or illustrations |

Deliver only the records relevant to the task. Do not create an artifact just because a template exists.

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

Use lowercase kebab-case equivalents in YAML frontmatter (for example,
`ready-for-review` and `attempts-in-progress`). A template's own
frontmatter status indicates the template's approval; when copying it, set
the new record's status to the appropriate starting state.

Use a separate canon-state label when needed. A scene can be a drafted document containing provisional story details; its existence does not make every detail approved canon.

## 8. Quality gates

### Story gate
- The scene or arc changes something; it is not merely decorative.
- Character choices arise from established motives and pressures.
- Maya/AI characters retain agency and a distinct interiority where applicable.
- Emotional development is earned through actions and consequences.
- Major turns have credible causes and lasting effects.
- The ending follows the approved direction.

### Continuity gate
- Names, identities, ages, relationships, appearances, abilities, and world rules match approved records.
- Chronology and geography remain coherent.
- No unresolved question is accidentally treated as fact.
- No higher-level summary contradicts a detailed approved record.

### Visual gate
- The chosen moment actually belongs to the scene.
- Locked identity, face, hair, wardrobe, and other constraints are preserved.
- Visible facts and interpretive meaning are clearly separated.
- Prompt, references, output, and assessment have honest provenance.

### Repository gate
- The correct branch and path are used.
- The relevant current file is fetched before replacement.
- Existing material is preserved unless intentionally revised.
- Parent links and indexes are updated.
- Each write is followed by read-back verification.
- Report commit IDs and file paths only after verification.

## 9. Versioning and legacy records

Version 1.1 is the current standard. Version 1.0 templates remain in the repository as historical references for records created under that format.

- Use Version 1.1 templates for new records.
- When materially revising an existing record, migrate it to 1.1 if the revised structure is relevant; do not force a migration of untouched legacy records.
- Never mass-rewrite completed scenes or approved artwork solely to change a template version.
- If a template changes in a way that affects the workflow, update this document, `README.md`, and the Romantic Storyteller skill in the same change set.
- Record format/version metadata in each document. Preserve stable IDs and approved content through migration.

## 10. Definition of done for repository work

A documentation or story-record task is complete only when:

- the correct artifact(s) are created or updated;
- every new document uses the current template or documents a justified exception;
- statuses distinguish draft, proposal, and approved material;
- all affected parent and cross-document links are updated;
- stale statements and contradictory instructions are removed;
- files are fetched again from the target branch and the critical changes are verified;
- the final report names the updated files and any remaining open questions accurately.
