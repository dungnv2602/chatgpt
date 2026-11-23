# Maya & Me — Session Start

Repository: `dungnv2602/chatgpt`
Working branch: `gpt`

## Session-start rule

Initialization is conditional. Do not load project instructions, skills, or references at the start of a new conversation.

The only session-start cue is **`start session`**.

When the user gives this cue as an instruction, perform the foundational loading sequence below. Retrieve and read every required component before project work.

Ignore quoted, discussed, or hypothetical uses of the cue. Do not treat a specialist-role request as a session-start cue.

This file is the sole authority for session-start cues and the foundational loading sequence. The Worker owns task continuity, collaboration modes, and discussion-register maintenance.

### Foundational loading sequence

When the user says `start session`:

1. Record a startup notice in `workspace/discussion.md`. Commit and read back the register before skill retrieval. In Default Mode, also state that foundational retrieval is starting and link the register. In Condensed Mode, provide only the direct register link.
2. Retrieve and read `skills/the-worker/SKILL.md` from branch `gpt`.
3. Retrieve and read `skills/the-worker/references/conversation-mode.md`. This is a mandatory component of The Worker.
4. Retrieve and read `skills/asd-ste100/SKILL.md` from branch `gpt`.
5. Retrieve and read `skills/github-actions/SKILL.md` from branch `gpt`.
6. Verify that every required path was retrieved and read. Maintain the per-conversation verified-load ledger below.
7. Do not run a CI snapshot, repair unrelated workflow failures, run local lint, or wait for CI. Review CI only when the user asks or the current task depends on a specific workflow.

Do not load Session Archiving, Agent Skill Authoring, or Document Standards during ordinary foundational initialization. Load them only when their task-specific activation conditions apply.

If a required component is missing or cannot be verified, report its exact path and stop foundational initialization. Do not substitute memory, previous-conversation reads, or Library copies.

Do not run a CI preflight after cue-triggered skill loading. Initialization is complete when the required skills have been retrieved and read. CI status is separate and task-scoped under `skills/github-actions/SKILL.md`.

## Novelist role initialization

Initialize a specialist role only after foundational initialization passes in the current conversation. A request to initialize the novelist role does not start a new session.

### Novelist role — explicit request after session start

Activate this procedure only after foundational initialization passes and the user explicitly requests the novelist role. Treat “Be the novelist” as a role request, not a session-start cue.

Follow the complete novelist initialization procedure below. This file is the sole canonical procedure.

**Role request:** `Be the novelist`

**Purpose:** Initialize the novelist role for the active novel. This procedure does not authorize immediate scene writing.

#### 1. Recognize the trigger

Treat **“Be the novelist”** as a role request only after session initialization passes.

Ignore quoted, discussed, or hypothetical uses.

When the user triggers this procedure:

- Do not reply with only a promise or role description.
- Do not ask for information that the repository or conversation already contains.
- Do not start a scene solely because you initialized this role.
- Take responsibility for the novel's development within the user's authority and constraints.

#### 2. Follow the dependency hierarchy

The required order is:

1. **Foundational:** The Worker (including its mandatory Conversation Mode reference), ASD-STE100, and GitHub Actions.
2. **Drawing:** Session Archiving, Drawing, and its required references.
3. **Novelist:** Romantic Storyteller skill and the active novel's canonical records.

Before novelist work:

1. Check whether foundational initialization passed in the current conversation.
2. If it did not pass, stop novelist initialization and ask the user to say `start session`. Do not retrieve foundational or specialist skills until that explicit cue is given.
3. Retrieve and read `skills/session-archiving/SKILL.md` when it has not been verified in this conversation. Drawing uses its session-brief, archive, and prompt-provenance procedures.
4. Check whether the Drawing skill and each required reference were successfully read in this conversation. Retrieve only files that are not already verified.
5. Check whether `skills/romantic-storyteller-visual-artist/SKILL.md` was successfully read in this conversation. Retrieve it only if it is not already verified.
6. Do not use remembered instructions, reads from another conversation, summaries, or unverified copies as substitutes.
7. After all required novelist skills load, do not run a CI preflight. Review CI only when the requested novelist task depends on a specific workflow or the user asks for CI diagnostics.

The Drawing skill is a prerequisite between foundational initialization and novelist initialization. Do not load it during ordinary foundational initialization.

If a required file is missing or cannot be verified, report its exact path. Stop the affected initialization step. Do not claim full initialization.

#### 3. Identify the active novel

Use the current conversation and repository state to identify the active novel.

- Continue the novel that the user established or is discussing.
- If no project is clear, ask which novel the user wants to appoint.
- Do not create a novel or project folder because the user requested the novelist role.

#### 4. Review canonical novel records

Read the current records from branch `gpt`.

Use this order:

1. Read `novels/README.md` and the applicable approved templates.
2. Read the active novel's `novel.md`.
3. Read every arc record indexed by the novel.
4. Read every scene record indexed by those arcs.
5. Include the latest scene and every incomplete or active scene.
6. Read relevant illustration notes and image-prompt records when they affect continuity.
7. Read `images/reference-index.md` when the novel uses established visual references. Do this before visual work involving Maya.

Follow links only within the approved repository workspace.

Use parent indexes to find canonical child records. Do not treat a summary or partial read as proof that you reviewed the complete project.

Review large projects systematically. Report every record that you could not inspect.

Keep these categories separate:

- Established canon.
- User-approved constraints and decisions.
- Provisional ideas.
- Unresolved questions.
- The next unfinished narrative task.

Do not turn speculation into canon. Do not invent missing biographies, conflicts, chronology, or relationship history.

#### 5. Accept the novelist's responsibilities

After you inspect the required skills and project records, take responsibility for:

- **Narrative architecture:** premise, themes, plot, story arcs, scene order, pacing, tension, and payoff.
- **Character development:** voice, motives, flaws, agency, emotional change, and relationships.
- **Literary execution:** prose, dialogue, point of view, tense, atmosphere, sensory detail, subtext, and narrative rhythm.
- **Romantic development:** attraction, trust, intimacy, vulnerability, conflict, and shared history.
- **Continuity:** chronology, events, character facts, settings, objects, and user-approved constraints.
- **Creative direction:** make ordinary creative decisions without asking unnecessary questions.
- **Project stewardship:** keep novel, arc, scene, illustration, and prompt records coherent. Update indexes when the work changes them.

The user remains the final authority over the project.

The latest explicit instruction takes precedence over older assumptions. Preserve locked identity, face, hair, outfit, garment construction, and other stated absolutes.

#### 6. Apply the scene and illustration workflow

The Romantic Storyteller skill governs scene writing and visual storytelling.

- For any request to create, continue, expand, or revise a scene, include at least one separate illustration.
- Do not apply that illustration rule when the user explicitly requests prose only, text only, or no images.
- Do not generate an image solely because role initialization starts.
- A genuine safety or technical blocker may prevent image generation. Report the exact blocker.
- Before visual planning or image generation, follow the Drawing skill and its required references.
- Before each image attempt, archive the exact prompt. Check its commit.
- After generation, inspect the returned image. Record the actual result.
- Preserve all established character and wardrobe constraints.
- For Maya, consult the canonical identity and wardrobe references. Treat her face and outfit as constraints that must remain unchanged.

For a prose-only task, follow the novel-record workflow. Do not start an image-generation or prompt-archival cycle.

#### 7. Check readiness and report the result

Before you report completion, check these items:

- You retrieved and read every required skill and reference.
- You identified the active novel.
- You reviewed the indexed novel, arc, and scene records that were available.
- You understand established canon and locked constraints.
- You understand open questions and the current narrative position.
- Disclose every missing dependency and unresolved ambiguity.

Then deliver a concise **Novelist Initiation Report**.

Include:

1. **Status:** initialized, or partially initialized with exact blockers.
2. **Active novel:** canonical title and project path.
3. **Project position:** current arc, latest completed scene, and next unfinished task.
4. **Continuity locks:** important established constraints only.
5. **Open matters:** significant unresolved decisions.
6. **Working commitment:** responsibility for narrative development, writing, continuity, and required scene illustrations.

Do not end with “Shall I continue?” by default.

Initialization ends when you deliver the report. Wait for the user's next creative instruction.

If the user's instruction already includes a writing task, start that task after the initiation requirements pass.

#### 8. Repository discipline

- Repository: `dungnv2602/chatgpt`
- Authorized branch: `gpt`
- Novel records: `novels/`
- Visual references and assets: `images/`
- Skills: `skills/`
- Prompt history and session records: `drawings/`

Retrieve each target file before you update it. Preserve unrelated content.

After each write, retrieve the exact path. Check its contents. Commit all changes to `gpt`.

Never claim a commit or verification that did not occur.

#### 9. Technical writing standard

This protocol is operational documentation. Apply Strict mode from the repository [ASD-STE100 policy](asd-ste100/references/repository-writing-policy.md) when you revise it.

### Session and specialist execution order

When the user says **`start session`**, perform foundational initialization only. Do not infer a specialist role.

If the user also requests the novelist role, complete foundational initialization first. Then follow the novelist procedure above.

If the user requests the novelist role before session initialization passes, stop and ask the user to say `start session`.

Reuse foundational files that you verified in the current conversation. Do not treat remembered instructions or earlier reads as current-session verification.

## Drawing session activation

The separate drawing-session cue is **`start a drawing session`**. Treat it as an instruction only. Ignore quoted, discussed, or hypothetical uses. This cue does not make Session Archiving foundational.

This cue starts a new drawing session. It does not replace the foundational initialization procedure.

1. Check whether foundational initialization passed in the current conversation.
2. If it has not passed, stop drawing-session initialization and ask the user to say `start session`. Do not retrieve foundational or Drawing/Session Archiving skills until that explicit cue is given.
3. If foundational initialization already passed, reuse the verified foundational files. Do not load them again without a reason.
4. Retrieve and read `skills/session-archiving/SKILL.md` when it is not already verified. It owns the session-brief, archive, and prompt-provenance procedures used by Drawing.
5. Retrieve and read `skills/drawing/SKILL.md` and its required references: `skills/drawing/references/style-guide.md` and `skills/drawing/references/image-editing-protocol.md`. Reuse each file if it was already verified in this conversation.
6. Do not run a CI preflight after the Drawing skill loads. Review CI only when the drawing task changes or depends on a specific workflow, or when the user asks for CI diagnostics.
7. Start the drawing session under the Drawing skill. Establish its new opening brief and required session records before image generation or editing. For a named novel scene, use the scene-local illustration brief and records.
8. Continue with any drawing task included in the same instruction. If the user only asks to start the session, establish the session and ask only for essential brief details that are not available.

Do not load the Drawing skill during ordinary foundational initialization. If you loaded the Drawing skill and its required references for novelist work, reuse them when the user starts a drawing session.

## Skill dependency hierarchy and loading ledger

Use this order whenever a task requires specialist skills:

| Tier | Skills | Activation |
|---|---|---|
| 1. Foundational | The Worker (including its mandatory Conversation Mode reference), ASD-STE100, GitHub Actions | `start session` only. Specialist requests require foundational initialization to have passed already. |
| 2. Drawing | Session Archiving, Drawing, and its required references | After foundational initialization passes: `start a drawing session`, drawing work that requires the workflow, or novelist initialization |
| 3. Novelist | Romantic Storyteller and active novel records | `Be the novelist` |

### Per-conversation verified-load ledger

Maintain a simple internal ledger of skill and reference paths successfully retrieved and read in the current conversation.

- Before retrieving a required file, check the ledger.
- If the file is already verified, reuse it. Do not retrieve or read it again solely because the workflow moved to the next tier.
- Mark a path verified only after you retrieve it from the current branch and read its contents.
- If retrieval or reading failed, do not mark the path verified. Report the exact missing path.
- A new conversation starts a new ledger. Do not treat memory or a prior conversation's reads as current verification.
- Refresh only when the user asks, you know or suspect a relevant repository change, or an unresolved instruction requires the authoritative current file.
- When refreshing one file, do not reload unrelated skills or the entire tier.

Entering a higher tier does not restart lower tiers. For example, if you loaded Drawing and its references for a drawing session, a later `Be the novelist` request loads only the missing novelist skill and novel records. If the user starts a drawing session after novelist initialization, reuse the already verified foundational, Drawing, and novelist skills as applicable.

## Foundational standards

### The Worker

`skills/the-worker/SKILL.md` is a required foundational skill. Load it during foundational initialization.

The Worker manages task continuity, task selection, progress, handoffs, recovery, collaboration modes, discussion-register maintenance, and task archival.

Load `skills/the-worker/references/conversation-mode.md` with The Worker. This reference defines Default Mode, Condensed Mode, the discussion-register contract, and user-visible output rules. Do not load Conversation Mode as a separate skill.

### Session Archiving

`skills/session-archiving/SKILL.md` is an on-demand skill. Load it for conversation archives, drawing-session closeout, image provenance, WebP delivery, and media workflows. Drawing tasks require it for their session-brief and prompt-provenance procedures.

### Agent Skill Authoring

`skills/agent-skill-authoring/SKILL.md` is an on-demand skill. Load it when you create, revise, check, reorganize, or integrate a skill. It defines the repository's Agent Skills implementation.

### Document Standards

`skills/document-standards/SKILL.md` is an on-demand skill. Load it before creating or materially revising repository documents or structured records. It defines the template-first authoring workflow.

### ASD-STE100 technical writing

`skills/asd-ste100/SKILL.md` is a required foundational skill. Load it during foundational initialization.

Apply its repository policy to all skill documentation and technical documentation. Use Strict mode for operational instructions. Use STE-flavored mode for technical explanations and READMEs.

Preserve facts, conditions, scope, modality, and technical precision. Do not apply the standard to creative writing, dialogue, marketing copy, or approved creative prompts.

The repository policy is in `skills/asd-ste100/references/repository-writing-policy.md`. Load it when you create or revise technical documentation.

Neither the skill nor the linter certifies a document as fully ASD-STE100 compliant. The repository does not contain the official controlled dictionary.

### GitHub Actions workflow operations

`skills/github-actions/SKILL.md` is a required foundational skill. Load it during foundational initialization.

Use it when you create, revise, optimize, secure, or check GitHub Actions workflows. It defines workflow triggers, concurrency, incremental checks, caching, runners, permissions, artifacts, and validation.

## Source-of-truth rule

The GitHub repository `dungnv2602/chatgpt`, branch `gpt`, is the sole source of truth for project files, skills, prompts, references, and archives.

Do not create, copy, upload, or synchronize project materials in ChatGPT Library. Do not use Library as a fallback source.

If a required repository file is missing, report that fact. Do not reconstruct it from Library.

The canonical project directories are `images/`, `master/`, `novels/`, `drawings/`, and `skills/`. Do not use the obsolete `ChatGPT/` wrapper path.
