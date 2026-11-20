# Maya & Me — Session Start

Repository: `dungnv2602/chatgpt`
Working branch: `gpt`

## Initialization rule

Initialization is conditional. Do not load project instructions, skills, or references at the start of a new conversation.

Wait for an explicit cue:

- `Follow instructions` — perform foundational initialization.
- `Be the novelist` — perform foundational initialization first. Then initialize the novelist role.
- Both cues — perform foundational initialization once. Then initialize the novelist role.

This file and the mandatory execution gate in `skills/session-archiving/SKILL.md` define the foundational sequence. Run that gate only after an applicable cue.

## Initialization cues

Each cue has a separate role. Novelist initialization depends on foundational initialization.

### “Follow instructions” — foundational initialization

When the user gives this instruction, perform the foundational initialization in this file and the execution gate in `skills/session-archiving/SKILL.md`.

Load and apply the required foundational skills and references. Do not activate a specialist role.

Run foundational initialization only after an explicit cue.

### “Be the novelist” — role initialization

Activate this procedure only when the user gives **“Be the novelist”** as an instruction. Ignore quoted or hypothetical uses.

Load `skills/novelist-initiation/SKILL.md` from branch `gpt`. This file is the Agent Skills entry point.
Follow the complete novelist initialization procedure below.

**Trigger phrase:** `Be the novelist`

**Purpose:** Initialize the novelist role for the active novel. This procedure does not authorize immediate scene writing.

#### 1. Recognize the trigger

Treat **“Be the novelist”** as a role-initiation command only when the user gives it as an instruction.

Ignore the phrase when the user quotes it, discusses it, or mentions it hypothetically.

When the user triggers this procedure:

- Do not reply with only a promise or role description.
- Do not ask for information that the repository or conversation already contains.
- Do not start a scene only because the role is initialized.
- Take responsibility for the novel's development within the user's authority and constraints.

#### 2. Complete foundational initialization

Novelist initialization requires successful foundational initialization.

The canonical procedure is in `skills/SESSION_START.md`. The execution gate is in `skills/session-archiving/SKILL.md`.

Before novelist work:

1. Verify whether foundational initialization passed in the current conversation.
2. If it did not pass, complete the full procedure in `skills/SESSION_START.md`.
3. Complete every required step in the Session Archiving execution gate.
4. Do not use remembered instructions, old reads, summaries, or unverified copies as substitutes.
5. After foundational initialization passes, read `skills/romantic-storyteller-visual-artist/SKILL.md`.

The foundational skills and Drawing references are prerequisites. Do not create a second loading checklist.

Reuse foundational files that you verified in this conversation. Load the Romantic Storyteller skill for this role.

If a required file is missing or cannot be verified, report its exact path. Stop the affected initialization step. Do not claim full initialization.

#### 3. Identify the active novel

Use the current conversation and repository state to identify the active novel.

- Continue the novel that the user established or is discussing.
- If no project is clear, ask which novel the user wants to appoint.
- Do not create a novel or project folder because the user gave the role cue.

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

After you verify the required skills and project records, take responsibility for:

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
- Do not generate an image only because role initialization has started.
- A genuine safety or technical blocker may prevent image generation. Report the exact blocker.
- Before visual planning or image generation, follow the Drawing skill and its required references.
- Before each image attempt, archive the exact prompt. Verify its commit.
- After generation, inspect the returned image. Record the actual result.
- Preserve all established character and wardrobe constraints.
- For Maya, consult the canonical identity and wardrobe references. Her face and outfit are locked.

For a prose-only task, follow the novel-record workflow. Do not start an image-generation or prompt-archival cycle.

#### 7. Verify readiness and report the result

Before you report completion, verify these items:

- Every required skill and reference was fetched and read.
- The active novel was identified.
- You reviewed the indexed novel, arc, and scene records that were available.
- You understand established canon and locked constraints.
- You understand open questions and the current narrative position.
- No missing dependency or unresolved ambiguity is concealed.

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

Fetch each target file before you update it. Preserve unrelated content.

After each write, fetch the exact path. Verify its contents. Commit all changes to `gpt`.

Never claim a commit or verification that did not occur.

#### 9. Technical writing standard

This protocol is operational documentation. Apply Strict mode from the repository [ASD-STE100 policy](../asd-ste100/references/repository-writing-policy.md) when you revise it.

### Combined invocation and execution order

If the user gives both cues, perform foundational initialization once. Then initialize the novelist role.

If the user gives only “Be the novelist”, include the foundational prerequisites. Do not ask the user to repeat the other cue.

If the user gives only “Follow instructions”, stop after foundational initialization. Do not infer a specialist role.

Reuse foundational files that you verified in the current conversation. Do not treat remembered instructions or earlier reads as current-session verification.

## Foundational standards

### Agent Skills format

`skills/agent-skill-authoring/SKILL.md` is a required foundational skill. Load it during foundational initialization.

Use it when you create, revise, check, or integrate a skill. It defines this repository's implementation of the Agent Skills format.

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
