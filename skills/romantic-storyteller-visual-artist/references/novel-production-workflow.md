# Novel Project Structure and Production Workflow

## 10. Novel project structure and production workflow

All durable novel records belong in the repository's `novels/` workspace on
branch `gpt`. The governing standard is
[`novels/WORKFLOW.md`](../../../novels/WORKFLOW.md), with the quick reference and
active templates in [`novels/README.md`](../../../novels/README.md).

**Current format standard: Version 1.1.** Use these templates for new records
and material revisions:

- Novel: `novels/templates/novel-v1.1.md`
- Character Profile (optional): `novels/templates/character-profile-v1.1.md`
- Open Discussion: `novels/templates/open-discussion-v1.1.md`
- Development Outline (optional): `novels/templates/development-outline-v1.1.md`
- Story Arc: `novels/templates/arc-v1.1.md`
- Scene: `novels/templates/scene-v1.1.md`
- Illustration Note: `novels/templates/illustration-note-v1.1.md`
- Illustration Prompt Record: `novels/templates/illustration-prompt-v1.1.md`

Version 1.0 templates remain historical references for existing records.
Do not mass-migrate untouched legacy documents. When a governing format changes,
update the templates, Workflow, README, and this skill together.

### Narrative hierarchy and supporting records

The narrative hierarchy is:

**Novel → Story Arc → Scene → Illustration asset**

Each illustration asset has two companion records: an Illustration Note
(documenting what the image actually shows and its narrative context) and an
Illustration Prompt Record (documenting the exact authored prompt, provenance,
chronological attempts, and outcomes).

Store novel illustration binaries centrally at
`novels/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`. Keep the two
Markdown records in the scene-local `illustrations/` folder; do not store the
image binary there. Each retained image has an original PNG/JPEG master and a
same-stem WebP derivative beside it.

All new retained uploads, whether novel or non-novel, use the single flat
`images/takeout/` intake. Inspect the actual image and prepare
`images/takeout/HANDOFF.yml` with its original upload filename, descriptive
title, optional stable asset ID, and destination directory. Do not rename or
move the upload manually. The existing GitHub Action stages WebP derivatives
under `images/takeout/webp/[batch-id]/attempt-NNN/`, appending `.webp` to
the exact incoming filename, verifies them, and routes them beside their
byte-identical original masters. Failed attempts retain their ready hand-off,
source images, and successfully converted staged WebPs for inspection; retries
use fresh attempt numbers. Successful attempts move WebPs to their permanent
destinations and remove their now-empty staging folder. The hand-off snapshot,
`conversion-report.csv`, and `verification-report.md` are archived under
`images/takeout/history/[batch-id]/attempt-NNN/` before the active hand-off is
cleared.

Supporting documents do not create extra narrative levels:
- `open-discussion.md` records proposed directions and unresolved questions.
- `planning/*.md` holds focused development outlines such as relationship
  progressions, plot mechanisms, character arcs, and world/technology plans.
- `characters/*.md` holds optional detailed character profiles where the
  novel-level summary is insufficient.
Chapters are optional editorial groupings of scenes, not a mandatory folder
or record type.

### Authority and canon control

Use the user's latest explicit instruction first, then user-approved decisions
in the novel records, then established continuity, then clearly labelled
proposals, and finally new creative suggestions.

Keep these states distinct:
- **Approved / Established:** explicitly accepted or directly established.
- **Proposed:** suggested, not yet decided.
- **Open:** deliberately undecided.
- **Superseded:** replaced by a later decision; retain its history.

Approval is scoped. Promote only the exact decision accepted by the user; keep
unmentioned implementation details open. A draft or outline does not become
canon merely because it has been written. Update the novel summary, relevant
character/arc/scene record, decision record, and open questions when approval
changes story facts.

Do not force every unanswered question to be resolved during foundation work.
Create a Development Outline when a consequential topic benefits from a durable
plan; consult the user on premise-level, character-defining, relationship,
causal, or ending decisions. Take the creative lead on minor craft decisions
when the intent is clear.

### Scene-writing and repository workflow

When asked to write, create, continue, revise, or expand a scene:

1. Identify the target novel and arc. Read the novel, relevant character
   records, open decisions, parent arc, and existing scene before writing.
2. Decide whether the request continues the same continuous event or creates
   a distinct scene. Do not create duplicate records.
3. Save the complete scene in the Scene Prose section of
   `scene.md`. Planning headings are not a substitute for actual narrative
   prose, dialogue, action, sensory detail, and subtext.
4. Update the scene's continuity and its parent arc/novel indexes as needed.
5. Keep draft, revised, approved, and complete statuses accurate.
6. Apply the automatic scene-illustration default above. It applies to a
   specific scene-writing task, not to discussion, brainstorming, or outline
   planning. Explicit prose-only/text-only/no-images instructions override it;
   genuine safety or technical blockers must be reported.
7. For every planned image, create its scene-local Illustration Prompt Record
   before the generation attempt. Record the exact authored prompt, references
   actually attached, acceptance criteria, and attempt history. Never claim
   access to a compiled prompt payload that is not exposed.
8. After generation, inspect each returned image separately. Record the actual
   output and assessment. Create/update one Illustration Note for each
   generated image retained or reviewed as a scene deliverable; link its image
   asset, relevant prompt attempt, and scene.
9. For repository retention, use the universal `images/takeout/` intake and
   prepare its structured hand-off. For novel illustrations, route the master
   and WebP to the central `assets/illustrations/[ARC-ID]/[SCN-ID]/` library.
   Link both binaries from the Illustration Note and scene index after the
   Action has verified them. Keep the Note and Prompt Record beside the scene.
10. If an image is only delivered in the conversation and is not stored in the
    repository, state that plainly. Never invent a repository asset path.
11. Follow the Drawing Skill for visual mode, image references, prompt
    archival, generation/editing, inspection, recovery, and asset integrity.
12. Fetch the current target file before updating it. Preserve unrelated
    material; update all affected parent indexes and links.
13. Read back each changed path and verify the expected content before
    reporting commits or completion.

Ordinary discussion or brainstorming does not require a scene, arc, or image
record unless a durable record is requested or the project's approved workflow
requires one. An image-only request does not automatically create a prose scene.

For the complete project stages, deliverable matrix, file conventions,
statuses, quality gates, versioning, and definition of done, follow
[`novels/WORKFLOW.md`](../../../novels/WORKFLOW.md).

