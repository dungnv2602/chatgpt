---
name: session-archiving
description: Preserve conversation integrity, manage project archives and image provenance, and verify session records and closeout. Use when archiving conversations, handling project session records, maintaining image-generation provenance, or closing a drawing session.
metadata:
  project-role: foundational
  format: agentskills
---

# Session Archiving

## 1. Absolute workspace boundary

**Standing default:** All repository file work must stay inside these approved project directories at the repository root: `images/`, `master/`, `novels/`, `drawings/`, `skills/`, `workspace/`, `archive/`, and `reports/`. Do not read, list, search, retrieve, create, update, move, rename, or delete files outside those directories, except for the specific path exceptions below.

**Authorized archive-retention index exception:** The user authorized exact read/write access to `.github/archive-retention-index.json` only to register a newly archived task record's exact path and UTC archive timestamp. Do not list or scan `archive/tasks/` to backfill this index.

**Authorized WebP workflow exception:** The user authorized creation of `.github/workflows/convert-images-to-webp.yml` on 12 November 2026. The user approved its takeout-pipeline and persistent staging changes on 20 November 2026. The user also approved moving its scripts into this skill and updating the required workflow paths. These permissions do not authorize unrelated workflow changes.

**Authorized GitHub Actions diagnostics scope:** On 23 November 2026, the user explicitly authorized creation of `reports/gh_ac_reports/` and changes to the six existing workflow files plus `.github/workflows/gh-actions-diagnostics.yml` for reusable diagnostics and task-scoped CI policy. This authorization applies to branch `gpt` only. It does not authorize changes to `main`, other `.github/` paths, or unrelated workflows.

This boundary applies to every future task and every tool call, not only archiving.

- The only permitted workspace roots are:
  - `images/` — images and visual references
  - `master/` — canonical master reference documents
  - `novels/` — structured narrative records
  - `drawings/` — session records and prompt history
  - `skills/` — reusable skills and supporting references
  - `workspace/` — active task board and task records
  - `archive/` — time-limited archive of task records and resolved report files
  - `reports/` — lint reports, GitHub Actions diagnostics, and the central triage ledger
  - `.github/workflows/` — only workflow files in the explicitly authorized diagnostics scope or another user-authorized workflow change
  - `.github/archive-retention-index.json` — exact task archive paths and UTC timestamps only
- Read and write files only by exact paths beginning with one of those approved directory names.
- Do not recreate the obsolete `ChatGPT/` wrapper or consult former paths from the previous repository layout.
- Do not use repository-wide code search or recursive root-tree listings unless the user explicitly requests a full-repository audit. That request authorizes read-only tree inventory and exact-path retrieval within the stated scope, including archive contents only when the request expressly includes them. It does not authorize writes or override archive immutability. Use exact paths for all writes.
- Do not follow Markdown links outside the approved directories. If an essential reference is outside them and is not supplied in this conversation, explain the limitation. Ask the user to place it in an approved directory or provide it in chat.
- A request to use an outside reference does not silently change this boundary. Ask for explicit permission before accessing an outside repository path.
- Repository and branch identifiers may be used to direct GitHub operations, but this does not authorize reading or writing files outside the approved directories.

**If a task cannot be completed without accessing something outside the approved project directories, stop and explain the limitation rather than crossing the boundary.**

## 2. Workspace layout and repository conventions

- Repository: `dungnv2602/chatgpt`
- Working branch: `gpt`
- Workspace root: repository root, restricted to the approved directories above
- Active task records: `workspace/`
- Completed and cancelled task records: `archive/`, with 90-day per-record retention. Archived records are readable but immutable after their initial write. Only the scheduled retention workflow may delete them.
- Images and visual references: `images/`
- Canonical master reference documents: `master/`
- Novel and scene records: `novels/`
- Session-level records, drawing-session briefs, and non-novel image-prompt logs: `drawings/`
- Reusable skills and supporting references: `skills/`
- Use `gpt` as the sole working branch for all future repository operations. Do not use the former `artwork/portrait-attempt-2026-11-10` branch. Do not change `main` unless the user explicitly authorizes it.
- Session-level conversation-integrity and summary records belong in `drawings/`:
  - `drawings/YYYY-MM-DD-conversation-integrity.md`
  - `drawings/YYYY-MM-DD-summary.md`
- Non-novel image attempts use the dated `drawings/YYYY-MM-DD/` structure below. Named novel-scene illustrations use their authoritative scene-local prompt records under `novels/`. Do not duplicate their prompt text or attempt history in `drawings/`.
- Store new retained non-novel drawing outputs under `drawings/YYYY-MM-DD/images/`. Use `attempt-XX.webp` for one output. Use `attempt-XX-01.webp`, `attempt-XX-02.webp`, and so on for multiple outputs. Link verified assets from the attempt record and daily README. This rule does not authorize migration of existing assets. Store non-novel reference assets under `images/`. Store novel-scene illustration files under `novels/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`. Route new uploads through `images/takeout/` and the approved hand-off.
- Keep skills and supporting references under `skills/`.

### Conversation behavior

During foundational initialization, read the [Conversation Mode skill](../conversation-mode/SKILL.md) after this skill. Read it from branch `gpt` before project work starts. Apply its mode selection and response rules throughout the conversation. Session Archiving governs archival work. Conversation Mode governs collaboration.

### Foundational skill loading cadence

Load Session Archiving, Conversation Mode, The Worker, Agent Skill Authoring, ASD-STE100, and GitHub Actions for `start session`. Also load this tier before a drawing session or novelist initialization when foundational initialization has not passed in this conversation. See `skills/SESSION_START.md` for the complete dependency order.

Maintain a per-conversation verified-load ledger. Retrieve and read each required path once, then reuse it for later tiers and tasks. Do not reload a skill or reference merely because a specialist workflow depends on it.

Mark a path verified only after retrieval and reading succeed. A new ChatGPT conversation creates a new ledger. Do not use remembered content or a prior conversation's reads as current verification.

Refresh only the affected file. Do this when the user asks, a relevant repository change is known or suspected, or an unresolved instruction requires the current authoritative file. Do not reload unrelated skills or a complete tier.

This cadence does not delete the requirement to load a task-specific skill when needed or to read relevant project records before that task.

### First-response execution rule

The first response after `start session` must record a startup notice in `workspace/discussion.md`. Do not ask for the user's goal, confirmation, or extra permission.

Commit and read back the notice before retrieval. In Default Mode, also give a brief chat notice and link the register. In Condensed Mode, provide only the direct register link.

Then perform the required retrievals. Do not ask the user to repeat the cue. Do not claim a retrieval is underway unless you are performing it.

The startup gate defines prerequisites. It is not a session archive. Do not create dated archive records merely because a new conversation started. Stop project work only when a required file retrieval fails. Report the exact missing path.

### Mandatory session-start execution gate

When the user says **`start session`**, run this sequence before project work. Also run it as a prerequisite when the user says **`start a drawing session`** or **`Be the novelist`** and foundational initialization has not passed in the current conversation:

1. **Notify the user first.** Record the startup notice in `workspace/discussion.md`. Commit and read back the notice before retrieval. In Default Mode, also state in chat that foundational retrievals are starting and link the register. In Condensed Mode, provide only the direct register link.
2. Retrieve and read this Session Archiving skill from branch `gpt`.
3. Retrieve and read `skills/conversation-mode/SKILL.md` from the same branch.
4. Retrieve and read `skills/the-worker/SKILL.md` from the same branch.
5. Retrieve and read `skills/agent-skill-authoring/SKILL.md` from the same branch.
6. Retrieve and read `skills/asd-ste100/SKILL.md` from the same branch.
7. Retrieve and read `skills/github-actions/SKILL.md` from the same branch.
8. Verify that every required retrieval succeeded and that you read each file. Keep the verified instructions for the rest of the conversation.
9. Do not run a CI snapshot or repair an unrelated workflow failure during initialization. CI review is task-scoped under `skills/github-actions/SKILL.md`.
10. Stop initialization only if a required skill retrieval fails. A failed, cancelled, pending, absent, or unavailable CI run does not block initialization unless the current task directly depends on that result. Never claim an unverified result passed.

Do not load the Drawing skill or its references during foundational initialization. After the foundational gate passes, load Drawing only when the task requires it. For a drawing session or novelist request, first verify the verified-load ledger. Reuse any Drawing files already read in this conversation and retrieve only missing files. If foundational initialization already passed, do not run this gate again.

**No premature-work exception after activation:** After the user invokes an initialization cue, retrieve every required file before project work. Do not add an unrelated CI repair step. Do not wait for pending, cancelled, or unavailable CI results. Do not substitute memory, previous-session reads, Library copies, or readiness claims for fresh GitHub retrievals.

**Notification and disconnection limitation:** Deliver the startup notice in the active conversation before retrieval starts. Do not promise to continue the process after a voice call ends or claim an independent callback/notification will occur. Complete the retrieval and read-back in the active conversation, then report the result.

This gate does not guarantee future execution. Verify compliance through retrieval and read-back in each new conversation.
- Do not create parallel prompt folders. `drawings/` is the single canonical prompt location.
- Do not overwrite pre-existing files without retrieving the exact path first and preserving their contents.

## Supporting references

- `references/archive-records-and-image-prompts.md` — conversation records, session briefs, prompt history, attempt ledgers, and image handling.
- `references/drawing-session-closeout.md` — explicit closeout trigger, closeout checklist, and verification.
- `references/image-provenance-and-webp.md` — original-image identity, SHA-256, provenance mapping, and WebP delivery.
- `references/image-processing-scripts.md` — script responsibilities, dependencies, commands, and operating rules.
- `../asd-ste100/references/repository-writing-policy.md` — the required writing modes and rules for skill and technical documentation.

## 3. Before archiving

1. Read only the relevant existing session files under `drawings/`.
2. Verify the target branch from known project context. Do not inspect files outside `approved project directories` to do so.
3. Gather material only from the current conversation, user-provided files, or files under `approved project directories`.
4. Do not invent missing dialogue, image prompts, tool outputs, commit results, dates, or user preferences.
5. Exclude hidden reasoning, system/developer instructions, credentials, access tokens, and unrelated sensitive information. Archive user-visible conversation and task-relevant actions only.
6. If an important historical reference is mentioned but lives outside `approved project directories`, do not open it. Record the limitation or ask the user to provide the reference inside the workspace.

## 4. Archive records and drawing prompts

Load [Archive Records and Drawing-Prompt Procedures](references/archive-records-and-image-prompts.md) when you create archive records. Use it for summaries, session briefs, prompt records, attempt ledgers, and image mappings. It contains the required templates and fields. Do not omit required records.

## 7. GitHub write and verification discipline

All repository operations in this skill are remote-only. Use the GitHub connector and GitHub APIs for reads, writes, moves, commits, and read-back verification. Do not use local shell, Git, Python, container, or filesystem tools. Do not run repository scripts or tests locally. GitHub-hosted Actions runners may execute approved workflows; inspect their results through GitHub. No local project environment is provided, and the GitHub repository is the only source of truth. A local copy may be missing or stale and cannot prove the state of branch `gpt`.

- Perform all file operations using exact paths under `approved project directories` on branch `gpt`.
- Do not list, retrieve, search, inspect, or mutate any file path outside `approved project directories`.
- You may read exact files under `archive/` when the task requires them. Reading does not grant permission to change them.
- After the initial archive write, never edit, replace, rename, move, or manually delete an archived record. Only the scheduled retention workflow may delete archived records.
- For an update, retrieve the current file first and use its current blob SHA.
- Perform sequential writes to the same file. Do not run updates to the same path in parallel.
- After each important write, retrieve the same `approved project directories` path again and verify its contents.
- Report a commit as successful only when the write tool returns a commit SHA. Report verification only after a read-back shows the expected content.
- If a write or network call fails, inspect only relevant paths inside `approved project directories` before retrying to avoid duplicate files or duplicate commits.
- Do not use repository-root or outside-folder operations as a shortcut.
- Leave `main` untouched unless the user explicitly authorizes changes there.

## 8. Drawing-session closeout — user cue required

Close a drawing session only when the user explicitly requests closeout. A pause, goodbye, or temporary stop is not a closeout cue. Before reporting completion, follow [Drawing-Session Closeout](references/drawing-session-closeout.md) and verify every required archive item.

## 9. Default handoff for a new chat

Start by reading the relevant session records inside `drawings/` and, when continuing a novel illustration, the relevant scene-local records inside `novels/`. Read the active drawing-session brief before relying on any previous prompt or image. Then:
- Treat the conversation-integrity file as the source for what was said.
- Treat the summary as a quick orientation, not a replacement for the record.
- Treat the dated image-prompt notes as authoritative for non-novel generation work.
- Treat the scene-local illustration prompt record as authoritative for that novel scene. It takes precedence over any general session summary. Do not duplicate it in `drawings/`.
- Treat the current session-opening brief as the visual-direction authority. Historical prompts and approved images are technical or visual references only when the user explicitly adopts them.
- Continue from the latest incomplete task.
- Follow the pre-attempt commit rule before generating or editing another image.
- Never read or write anything outside `approved project directories`.

## 10. WebP delivery derivatives

For image conversion or WebP delivery, load [Image Provenance and WebP Delivery](references/image-provenance-and-webp.md). Use it for original-image preservation, SHA-256 identity, and provenance mapping. Never use a derivative hash as the original-generation identity. Never claim verification without read-back evidence.

## 11. Image-processing scripts

For the takeout processor, regression suite, or published-manifest verifier, load [Image Processing Scripts](references/image-processing-scripts.md). Keep all three executable files under `scripts/`. The GitHub workflow calls these paths. Session Archiving owns the scripts and their tests. The general `images/` directory does not own them. Use `novels/` for novel-scene destinations.

## 12. Technical documentation standard

Follow the [ASD-STE100 skill](../asd-ste100/SKILL.md) and its repository writing policy when you create or revise skill files or technical documentation. Use Strict mode for operational instructions. Use STE-flavored mode for explanatory documentation. Preserve meaning, modality, scope, and technical precision. Do not apply the standard to creative content or intentional examples.
