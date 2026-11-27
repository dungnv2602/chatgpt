# Maya & Me — Session Start

Repository: `dungnv2602/chatgpt`
Working branch: `gpt`

## Session-start rule

Initialization is conditional. Do not load project instructions, skills, or references at the start of a new conversation.

The only session-start cue is **`/start`**.

When the user gives this cue as an instruction, perform the baseline initialization sequence below. Load only its required baseline components. Load domain skills when the requested work activates them.

Ignore quoted, discussed, or hypothetical uses of the cue. Do not treat a specialist-role request as a session-start cue.

This file is the sole authority for session-start cues and the foundational loading sequence. The Worker owns task continuity, collaboration modes, and discussion-register maintenance.

### Material recovery and cleanup

For task-required materials, recover them autonomously within the approved task scope. Do not ask for permission solely to retrieve materials. Treat downloaded, extracted, copied, or staged recovery artifacts as temporary and delete them immediately after their last necessary use. At closeout, verify and record cleanup. Never delete canonical repository files, user-owned originals, retained evidence, or material protected by governance or explicit instructions. Preserve canonical and retention-controlled material; resolve any material uncertainty before deletion.

## Foundational loading sequence

When the user says `/start`:

1. Record a startup notice in `workspace/discussion.md`. Commit and read back the register before fetching the required skills. In Default Mode, also state that the Worker and Conversation Mode reference are being fetched and link the register. In Condensed Mode, provide only the direct register link.
2. Fetch and read `.agent/skills/the-worker/SKILL.md` from branch `gpt`.
3. Fetch and read `.agent/skills/the-worker/references/conversation-mode.md`. This is a mandatory component of The Worker.
4. Verify the two baseline components and record them in the per-conversation verified-load ledger below.
5. Load the Worker's `references/ci-ledger.md` and `references/github-actions.md` for the mandatory startup batch. Load other Worker references and domain skills only when the tasks require them.
6. Before you inspect or execute CI-generated P0 tasks, send the user this notice in every conversation mode:

   **CI P0 batch execution starting.** I’m processing all eligible CI-generated P0 tasks before taking your prompt. Please wait until I say I am ready.

7. Use The Worker's batch procedure to identify and execute every eligible CI Ledger-generated P0 task. Do not process the user's substantive prompt until the batch ends.
8. Run the Worker's queue-draining loop. After each task completes or becomes ineligible, update its records and rebuild the full eligible queue. A blocker on one task never ends the batch while another independent eligible task remains. Record the blocker, skip that task, and execute the next eligible task. Do not send task-level blocker or progress pings while eligible work remains. At quiescence, ask at most one essential question for the first user-resolvable blocker. Resume the queue after the user answers.
9. After the Worker commits all eligible remediation changes, stop before hosted CI results review. Do not poll, dispatch, rerun, or inspect hosted CI results until the user explicitly requests results review.
10. After the batch ends, tell the user: **Ready to take your prompt.** Do not bundle blocker questions or enumerate later input requests. Ask about another blocker only after the user answers the first question and the Worker drains the newly eligible queue. Do not claim hosted validation or task closeout.
11. Do not run a CI snapshot, repair unrelated workflow failures, run local lint, or wait for CI. Use existing Ledger records for batch selection. Review hosted CI results only under the rule in step 9.

Baseline initialization is The Worker and its mandatory Conversation Mode reference only. Load ASD-STE100 when revising technical or skill documentation. Load GitHub Actions when CI or workflow work activates it. Load Agent Skill Authoring only when skill creation or maintenance activates it. Fetch supporting references only when needed. The Worker's archive and media references remain task-triggered components.

If a required component is missing or cannot be verified, report its exact path and stop foundational initialization. Do not substitute memory, previous-conversation reads, or Library copies.

Do not run a CI preflight after cue-triggered skill loading. Initialization is complete after you fetch and read the required skills. CI status is separate and task-scoped under `.agent/skills/the-worker/references/github-actions.md`.

## Domain skill activation after baseline initialization

After `/start` passes, load domain skills only as the task requires:

- **Worker-owned CI Ledger:** Load `.agent/skills/the-worker/references/ci-ledger.md` during every `/start` before selecting CI-generated P0 tasks.
- **Worker-owned GitHub Actions:** Load `.agent/skills/the-worker/references/github-actions.md` during every `/start` before executing the P0 batch. It governs CI diagnostics, workflow changes, recurrence prevention, and validation procedures.
- **ASD-STE100:** skill or technical-document authoring/revision, including when a domain skill requires its writing standard.
- **Agent Skill Authoring:** skill creation, revision, integration, or validation.

Do not load unrelated skills. Verify the current-session verified-load ledger first and refresh only when justified.

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

Use this order:

1. **Baseline:** The Worker (including its mandatory Conversation Mode reference). Load ASD-STE100 and GitHub Actions when their task-specific activation conditions apply. The Worker owns document governance.
2. **Drawing:** The Worker's archive/media references, Drawing, and its required references.
3. **Novelist:** Romantic Storyteller skill and the active novel's canonical records.

Before novelist work:

1. Verify whether foundational initialization passed in the current conversation.
2. If it did not pass, stop novelist initialization and ask the user to say `/start`. Do not fetch foundational or specialist skills until the user gives that explicit cue.
3. Fetch the relevant Worker references if you have not verified them in this conversation: `.agent/skills/the-worker/references/archive-records-and-image-prompts.md` and, when needed, `drawing-session-closeout.md` and `image-provenance-and-webp.md`. These define the session-brief, archive, and prompt-provenance procedures.
4. Verify whether the Drawing skill and each required reference were successfully read in this conversation. Fetch only files that are not already verified.
5. Verify whether `.agent/skills/romantic-storyteller-visual-artist/SKILL.md` was successfully read in this conversation. Fetch it only if it is not already verified.
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

1. Read `area/novel/README.md` and the applicable approved templates.
2. Read the active novel's `novel.md`.
3. Read every arc record indexed by the novel.
4. Read every scene record indexed by those arcs.
5. Include the latest scene and every incomplete or active scene.
6. Read relevant illustration notes and image-prompt records when they affect continuity.
7. For visual work involving Maya, inspect the exact reference images and project records that exist under the relevant `area/novel/` project and `.takeout/images/original/`. The global image reference index is absent and must not be recreated.

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
- Before each image attempt, archive the exact prompt. Verify its commit.
- After generation, inspect the returned image. Record the actual result.
- Preserve all established character and wardrobe constraints.
- For Maya, consult the canonical identity and wardrobe references. Treat her face and outfit as constraints that must remain unchanged.

For a prose-only task, follow the novel-record workflow. Do not start an image-generation or prompt-archival cycle.

#### 7. Verify readiness and report the result

Before you report completion, verify these items:

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
- Novel records: `area/novel/`
- Shared visual references and assets: `.takeout/images/`. Project-specific assets remain under their `area/` project folders.
- Skills: `.agent/skills/`
- Prompt history and session records: `area/drawing/`

Fetch each target file before you update it. Preserve unrelated content.

After each write, fetch the exact path. Verify its contents. Commit all changes to `gpt`.

Never claim a commit or verification that did not occur.

#### 9. Technical writing standard

This protocol is operational documentation. Apply Strict mode from the repository [ASD-STE100 policy](skills/asd-ste100/references/repository-writing-policy.md) when you revise it.

### Session and specialist execution order

When the user says **`/start`**, perform foundational initialization only. Do not infer a specialist role.

If the user also requests the novelist role, complete foundational initialization first. Then follow the novelist procedure above.

If the user requests the novelist role before session initialization passes, stop and ask the user to say `/start`.

Reuse foundational files after you verify them in the current conversation. Do not treat remembered instructions or earlier reads as current-session verification.

## Drawing session activation

The separate drawing-session cue is **`start a drawing session`**. Treat it as an instruction only. Ignore quoted, discussed, or hypothetical uses. This cue does not change foundational loading. It activates The Worker's drawing-session procedures after foundational initialization.

This cue starts a new drawing session. It does not replace the foundational initialization procedure.

1. Verify whether foundational initialization passed in the current conversation.
2. If it has not passed, stop drawing-session initialization and ask the user to say `/start`. Do not fetch foundational or Drawing skills until the user gives that explicit cue.
3. If foundational initialization already passed, reuse the verified foundational files. Do not load them again without a reason.
4. Load The Worker's `references/archive-records-and-image-prompts.md` and any other required archive/media references when they are not already verified. The Worker owns the session-brief, archive, and prompt-provenance procedures used by Drawing.
5. Fetch and read `.agent/skills/drawing/SKILL.md` and its required references: `.agent/skills/drawing/references/style-guide.md` and `.agent/skills/drawing/references/image-editing-protocol.md`. Reuse each file if it was already verified in this conversation.
6. Do not run a CI preflight after the Drawing skill loads. Review CI only when the drawing task changes or depends on a specific workflow, or when the user asks for CI diagnostics.
7. Start the drawing session under the Drawing skill. Establish its new opening brief and required session records before image generation or editing. For a named novel scene, use the scene-local illustration brief and records.
8. Continue with any drawing task included in the same instruction. If the user only asks to start the session, establish the session and ask only for essential brief details that are not available.

Do not load the Drawing skill during ordinary foundational initialization. If you loaded the Drawing skill and its required references for novelist work, reuse them when the user starts a drawing session.

## Skill dependency hierarchy and loading ledger

Use this order whenever a task requires specialist skills:

| Tier | Skills | Activation |
|---|---|---|
| 1. Baseline | The Worker (including its mandatory Conversation Mode reference) | `/start` only. Specialist requests require baseline initialization to have passed already. |
| 1a. Domain skills | ASD-STE100, GitHub Actions, Agent Skill Authoring | Load only when task activation conditions apply. |
| 2. Drawing | The Worker's archive/media references, Drawing, and its required references | After baseline initialization passes: `start a drawing session`, drawing work that requires the workflow, or novelist initialization |
| 3. Novelist | Romantic Storyteller and active novel records | `Be the novelist` |

### Per-conversation verified-load ledger

Maintain a simple internal ledger of skill and reference paths successfully retrieved and read in the current conversation.

- Before retrieving a required file, verify the ledger.
- If the file is already verified, reuse it. Do not fetch or read it again solely because the workflow moved to the next tier.
- Mark a path verified only after you fetch it from the current branch and read its contents.
- If fetching or reading failed, do not mark the path verified. Report the exact missing path.
- A new conversation starts a new ledger. Do not treat memory or a prior conversation's reads as current verification.
- Refresh only when the user asks, you know or suspect a relevant repository change, or an unresolved instruction requires the authoritative current file.
- When refreshing one file, do not reload unrelated skills or the entire tier.

Entering a higher tier does not restart lower tiers. For example, you may load Drawing and its references for a drawing session. If the user later requests the novelist role, load only the missing novelist skill and novel records. If the user starts a drawing session after novelist initialization, reuse the foundational, Drawing, and novelist skills that you already verified.

## Foundational standards

### The Worker

`.agent/skills/the-worker/SKILL.md` is the required baseline skill. Load it during `/start` initialization.

The Worker manages task continuity, selection, progress, handoffs, recovery, and collaboration modes.

It maintains the discussion register and archives task records.

It also manages conversation and drawing-session records, image provenance, WebP delivery, and media workflows.

Load `.agent/skills/the-worker/references/conversation-mode.md` with The Worker. This reference defines Default Mode, Condensed Mode, the discussion-register contract, and user-visible output rules. Do not load Conversation Mode as a separate skill.

### The Worker's archive and media procedures

The Worker owns conversation archives, drawing-session closeout, image provenance, WebP delivery, and media workflows. Load its relevant archive/media references only when the task requires them. Drawing tasks use these references for session briefs, prompt provenance, and closeout.

### Agent Skill Authoring

`.agent/skills/agent-skill-authoring/SKILL.md` is an on-demand skill. Load it when you create, revise, verify, reorganize, or integrate a skill. It defines the repository's Agent Skills implementation.

### ASD-STE100 technical writing

`.agent/skills/asd-ste100/SKILL.md` is task-activated. Load it when you create or revise skill or technical documentation.

Apply its repository policy to all skill documentation and technical documentation. Use Strict mode for operational instructions. Use STE-flavored mode for technical explanations and READMEs.

Preserve facts, conditions, scope, modality, and technical precision. Do not apply the standard to creative writing, dialogue, marketing copy, or approved creative prompts.

The repository policy is in `.agent/skills/asd-ste100/references/repository-writing-policy.md`. Load it when you create or revise technical documentation.

Neither the skill nor the linter certifies a document as fully ASD-STE100 compliant. The repository does not contain the official controlled dictionary.

### Worker-owned GitHub Actions operations

`.agent/skills/the-worker/references/github-actions.md` is an on-demand Worker reference. Load it for CI diagnostics, workflow changes, CI-generated remediation, recurrence prevention, or workflow validation.

Use it when you create, revise, optimize, secure, or verify GitHub Actions workflows. It defines workflow triggers, concurrency, incremental validation, caching, runners, permissions, artifacts, and validation.

## Source-of-truth rule

The GitHub repository `dungnv2602/chatgpt`, branch `gpt`, is the sole source of truth for project files, skills, prompts, references, and archives.

Do not create, copy, upload, or synchronize project materials in ChatGPT Library. Do not use Library as a fallback source.

If a required repository file is missing, report that fact. Do not reconstruct it from Library.

The current repository roots used by the workflows are `.agent/skills/`, `workspace/archive/`, `.takeout/images/`, `.takeout/reports/`, `area/`, `master/`, and `workspace/`. Novel and drawing records live under `area/novel/` and `area/drawing/`. Do not use the obsolete root paths `images/`, `archive/`, `reports/`, or the `ChatGPT/` wrapper.
