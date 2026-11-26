# Novel Project Structure and Production Workflow

## 10. Novel project structure and production workflow

Store all durable novel records in the repository's `area/novel/` workspace on branch `gpt`.

The governing standard is [`area/novel/WORKFLOW.md`](../../../area/novel/WORKFLOW.md). The quick reference and active templates are in [`area/novel/README.md`](../../../area/novel/README.md).

**Current format standard: Version 1.1.** Use these templates for new records and material revisions:

- Novel: `area/novel/templates/novel-v1.1.md`
- Character Profile (optional): `area/novel/templates/character-profile-v1.1.md`
- Open Discussion: `area/novel/templates/open-discussion-v1.1.md`
- Development Outline (optional): `area/novel/templates/development-outline-v1.1.md`
- Story Arc: `area/novel/templates/arc-v1.1.md`
- Scene: `area/novel/templates/scene-v1.1.md`
- Illustration Note: `area/novel/templates/illustration-note-v1.1.md`
- Illustration Prompt Record: `area/novel/templates/illustration-prompt-v1.1.md`

Version 1.0 templates remain as historical references for existing records. Do not mass-migrate untouched legacy documents.

When a governing format changes, update the templates, Workflow, README, and this skill together.

### Narrative hierarchy and supporting records

The narrative hierarchy is:

**Novel → Story Arc → Scene → Illustration asset**

Each illustration asset has two companion records:

- **Illustration Note:** records what the image shows and its narrative context.
- **Illustration Prompt Record:** records the exact authored prompt, provenance, attempts, and outcomes.

Store novel illustration binaries in the central asset library:

`area/novel/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`

Keep both Markdown records in the scene-local `illustrations/` folder. Do not store image binaries there.

Each retained image has an original PNG/JPEG master and a same-stem WebP derivative beside it.

All new retained uploads use the single flat `images/takeout/` intake. This rule applies to novel and non-novel assets.

Inspect the actual image. Prepare `images/takeout/HANDOFF.yml` with its original filename, descriptive title, optional stable asset ID, and destination directory.

Do not rename or move the upload manually. The existing GitHub Action stages WebP derivatives under `images/takeout/webp/[batch-id]/attempt-NNN/`. It appends `.webp` to the exact incoming filename. It verifies each derivative and routes it beside its byte-identical original master.

Failed attempts retain the ready hand-off, source images, and successfully converted staged WebPs. Use a new attempt number for each retry. Successful attempts move WebPs to their permanent destinations and remove the empty staging folder.

The Action archives the hand-off snapshot, `conversion-report.csv`, and `verification-report.md` under `images/takeout/history/[batch-id]/attempt-NNN/`. It clears the active hand-off only after it completes the required checks and archive steps.

Supporting documents do not create extra narrative levels:

- `open-discussion.md` records proposed directions and unresolved questions.
- `planning/*.md` stores focused development outlines. Examples include relationship progression, plot mechanisms, character arcs, and world or technology plans.
- `characters/*.md` stores optional detailed character profiles when the novel-level summary is insufficient.

Chapters are optional editorial groupings of scenes. They are not a mandatory folder or record type.

### Authority and canon control

Use the user's latest explicit instruction first. Then use user-approved decisions in the novel records, established continuity, labelled proposals, and new creative suggestions in that order.

Keep these states distinct:

- **Approved / Established:** explicitly accepted or directly established.
- **Proposed:** suggested, not yet decided.
- **Open:** deliberately undecided.
- **Superseded:** replaced by a later decision. Retain its history.

Approval is scoped. Promote only the exact decision the user accepted. Keep unmentioned implementation details open.

A draft or outline does not become canon merely because it exists. When approval changes story facts, update the novel summary, relevant character, arc, or scene record, decision record, and open questions.

Do not force every unanswered question to be resolved during foundation work. Create a Development Outline when a consequential topic needs a durable plan.

Consult the user about premise-level, character-defining, relationship, causal, or ending decisions. Take the creative lead on minor craft decisions when the intent is clear.

### Scene-writing and repository workflow

When the user asks you to write, create, continue, revise, or expand a scene:

1. Identify the target novel and arc. Read the novel, relevant character records, open decisions, parent arc, and existing scene before writing.
2. Decide whether the request continues the same event or creates a distinct scene. Do not create duplicate records.
3. Save the complete scene in the Scene Prose section of `scene.md`. Planning headings do not replace narrative prose, dialogue, action, sensory detail, or subtext.
4. Update the scene's continuity and its parent arc and novel indexes as needed.
5. Keep draft, revised, approved, and complete statuses accurate.
6. Apply the automatic scene-illustration default. It applies to a specific scene-writing task. It does not apply to discussion, brainstorming, or outline planning. Explicit prose-only, text-only, or no-images instructions override the default. Report genuine safety or technical blockers.
7. For each planned image, create its scene-local Illustration Prompt Record before the generation attempt. Record the exact authored prompt, references actually attached, acceptance criteria, and attempt history. Do not claim access to a compiled prompt payload that is not exposed.
8. After generation, inspect each returned image separately. Record the actual output and assessment. Create or update an Illustration Note for each generated image retained or reviewed as a scene deliverable. Link its image asset, relevant prompt attempt, and scene.
9. For repository retention, use the universal `images/takeout/` intake. Prepare its structured hand-off. Route novel masters and WebP files to the central `assets/illustrations/[ARC-ID]/[SCN-ID]/` library. Link both files from the Illustration Note and scene index after the Action verifies them. Keep the Note and Prompt Record beside the scene.
10. If an image exists only in the conversation, state that fact. Do not invent a repository asset path.
11. Follow the Drawing Skill for visual mode, image references, prompt archival, generation and editing, inspection, recovery, and asset integrity.
12. Fetch the current target file before updating it. Preserve unrelated material. Update affected parent indexes and links.
13. Read back each changed path. Verify the expected content before you report commits or completion.

Ordinary discussion or brainstorming does not require a scene, arc, or image record. Create one only when the user requests a durable record or the approved project workflow requires it.

An image-only request does not automatically create a prose scene.

For the full project stages, deliverable matrix, file conventions, statuses, quality gates, versioning, and definition of done, follow [`area/novel/WORKFLOW.md`](../../../area/novel/WORKFLOW.md).

## Technical documentation standard

Apply the repository [ASD-STE100 policy](../../asd-ste100/references/repository-writing-policy.md) when you revise this workflow. Use Strict mode for procedures. Preserve novel canon, approvals, conditions, and narrative meaning.
