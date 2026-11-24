# ChatGPT Initialization Policy

## Purpose

This file records the repository's conditional initialization policy. Operational instructions remain in the files listed below.

## Sources of truth

- Repository: `dungnv2602/chatgpt`
- Branch: `gpt`
- Foundational initialization: `skills/SESSION_START.md`
- Foundational collaboration and task continuity: `skills/the-worker/SKILL.md`
- Mandatory Conversation Mode component: `skills/the-worker/references/conversation-mode.md`
- Agent Skills format, loaded on demand: `skills/agent-skill-authoring/SKILL.md`
- Technical writing standard: `skills/asd-ste100/SKILL.md`
- Foundational document governance: `skills/document-standards/SKILL.md`
- Canonical novelist procedure: the Novelist role initialization section in `skills/SESSION_START.md`
- Drawing tier: The Worker's archive/media references and `skills/drawing/SKILL.md`, loaded for a drawing session or novelist initialization

This file does not replace an operational skill or initiation procedure.

## Current policy

Initialization is conditional. Do not load project instructions or skills at the start of a new conversation.

The only session-start cue is `start session`. Read `skills/SESSION_START.md` and follow its complete procedure when the user gives that cue as an instruction.

A specialist-role request does not change or satisfy the `start session` cue. It does not authorize foundational initialization. If initialization has not passed in the current conversation, stop and ask the user to say `start session`. After that explicit initialization passes, load the missing specialist tiers required by the role.

## Operating rules

- Do not initialize automatically.
- Do not treat specialist-role requests as session-start cues.
- Specialist-role requests never trigger foundational initialization. Ask for `start session` when it has not passed in the current conversation.
- Load only the files required by the session-start procedure or the requested specialist task.
- Do not load unrelated skills or references.
- Report the exact path of a missing or unverified file.
- Complete initialization when every required skill has been retrieved and read. CI status is separate from initialization.
- Do not run a CI snapshot or repair unrelated workflow failures before handling a prompt.
- Review CI only when the user asks or the current task changes or depends on a specific validation workflow.
- Never wait for or poll CI. Never run the linter or CI workflows locally. Let GitHub Actions execute validation.
- Treat the GitHub repository and branch `gpt` as the sole source of truth.

## Foundational standards

Foundational initialization loads these skills:

1. The Worker, including its mandatory Conversation Mode reference.
2. ASD-STE100.
3. GitHub Actions.
4. Document Standards.

Agent Skill Authoring remains on-demand. Document Standards is foundational because its template-first gate applies across repository document creation and material revision. Load its skill definition during initialization. Retrieve its catalog, templates, schemas, and validator details only when the task requires them.

The Drawing tier is tier 2, not foundational. It includes the Drawing skill and its required references. Load it only after foundational initialization passes. The Worker owns the archive/media procedures used by Drawing. A drawing-session or novelist request does not trigger foundational initialization. Its required references are `skills/drawing/references/style-guide.md` and `skills/drawing/references/image-editing-protocol.md`.

Novelist initialization is tier 3. Load `skills/romantic-storyteller-visual-artist/SKILL.md` only for the explicit novelist role request, after foundational and Drawing tiers are ready.

Maintain a per-conversation verified-load ledger. Retrieve and read each required skill or reference once. Reuse it when entering a higher tier or returning to a prior tier. A new conversation starts a new ledger. Refresh only when the user asks, you know or suspect a relevant repository change, or an unresolved instruction requires the current file. Do not reload an entire tier to refresh one file.

The ASD-STE100 skill governs skill documentation and technical documentation. Use Strict mode for operational instructions. Use STE-flavored mode for technical explanations and READMEs.

Preserve facts, conditions, exceptions, scope, and modality. Do not apply the standard to creative writing, dialogue, marketing copy, or approved creative prompts.

The Agent Skill Authoring skill governs skill structure, metadata, validation, and activation when skill work requires it. The ASD-STE100 skill governs technical language across skill and technical documentation.

## Copyable Custom Instructions

Use this exact text when configuring the repository's project instructions:

```text
Repository: "dungnv2602/chatgpt"
Branch: "gpt"

The GitHub repository "dungnv2602/chatgpt", branch "gpt", is the sole source of truth for project files, skills, prompts, references, and archives.

Use "skills/SESSION_START.md" as the sole source of session-start instructions, and initialize only when I say "start session".

Initialization is conditional. Do not load project instructions or skills at the start of a new conversation.
```

## Design principles

1. **On-demand loading:** Load only what the requested task requires.
2. **Single initialization authority:** `skills/SESSION_START.md` defines foundational initialization.
3. **Explicit dependency:** Novelist initialization requires foundational initialization first.
4. **No duplicate procedures:** Keep session-start and novelist initialization procedures in `skills/SESSION_START.md`.
5. **Current-session verification:** Do not use remembered files as a substitute for fresh reads when you must verify.
6. **On-demand skill authoring:** Use `skills/agent-skill-authoring/SKILL.md` when you create or maintain skills.
7. **Controlled technical writing:** Use `skills/asd-ste100/SKILL.md` for skill and technical documentation.

## Change history

The entries below are historical. The current policy above takes precedence. A former skill or dependency listed in an old entry is not active unless the current policy lists it.

### Version 1 — Conditional initialization

- **Date:** 2026-11-18
- **Change:** Initialization requires an explicit activation cue.
- **Dependency:** `Be the novelist` includes foundational initialization.
- **Duplicate prevention:** Both cues trigger foundational initialization only once.
- **Reason:** Avoid unnecessary loading while preserving specialist prerequisites.
- **Operational files:** `skills/SESSION_START.md` and `skills/novelist-initiation/SKILL.md`.

### Version 2 — Agent Skills format

- **Date:** 2026-11-20
- **Change:** Adopt the Agent Skills open format.
- **Reason:** Standardize metadata, structure, description, progressive disclosure, and validation.
- **Behavioral impact:** Agent Skill Authoring became a foundational skill.
- **Verification:** Read-back verification passed. The official `skills-ref` CLI validator was not run.
- **Initial commits:** `5bdb1b732c88fc4bb0d9e49fbeb78eb6048c7bc5`, `b26c37031399747ea204fa89a491a8ff26bce911`, `a48f7264246734a73b02f41537f367f04fa09c55`, and `fee7c31d7c7b2f63efee3680796ac477b060eb45`.

### Version 3 — Skill directory restructure

- **Date:** 2026-11-20
- **Change:** Apply Agent Skills format to the repository's skill folders.
- **Reason:** Make skills discoverable and reduce unnecessary loading.
- **Behavioral impact:** Every skill folder gained a conforming `SKILL.md`. Detailed procedures moved into focused references. Foundational initialization remained conditional.
- **Verification:** Manual metadata, naming, description, line-count, link, activation, and read-back verification passed. The official validator was not run.

### Version 4 — ASD-STE100 made foundational

- **Date:** 2026-11-20
- **Change:** Make ASD-STE100 a foundational skill. Apply its writing modes to skill documentation and technical documentation.
- **Reason:** Reduce ambiguity without changing technical meaning.
- **Behavioral impact:** Foundational initialization now loads ASD-STE100. Use Strict mode for operational instructions and STE-flavored mode for technical explanations. Creative content and intentional examples remain outside the policy.
- **Files modified:** ASD-STE100, Session Start, Session Archiving, Agent Skill Authoring, Skills README, and this policy file.
- **Verification:** Initial read-back completed. The current documentation audit remains in progress.

### Version 5 — Task-scoped CI review

- **Date:** 2026-11-23
- **Requested change:** Remove mandatory CI preflight and repair steps before prompts and after initialization.
- **Reason:** Unrelated workflow failures must not delay a new user request.
- **Behavioral impact:** Initialization depends on successful skill retrieval. CI review and repair apply only when the user asks or the current task depends on a relevant workflow. Use `reports/gh_ac_reports/` for workflow evidence and `reports/lint_reports/` for detailed lint findings. Track recurring issues in `reports/triage/ledger.json`.
- **Files modified:** Session Start, Session Archiving, The Worker, GitHub Actions, Agent Skill Authoring, ASD-STE100, and this policy file.
- **Verification:** Pending hosted workflow validation and exact read-back.

### Version 6 — Consolidated foundational collaboration

- **Date:** 2026-11-23
- **Requested change:** Consolidate foundational collaboration and session-start responsibilities into The Worker. Keep ASD-STE100 and GitHub Actions separate.
- **Reason:** Reduce the foundational loading set without losing baseline session, mode, task, or register behavior.
- **Behavioral impact:** Foundational initialization loads The Worker and its mandatory Conversation Mode reference, ASD-STE100, and GitHub Actions. Session Archiving, Agent Skill Authoring, and Document Standards load on demand.
- **Files modified:** The Worker, Conversation Mode compatibility entry point, Session Archiving, Agent Skill Authoring, Session Start, this policy, the skills index, the document-type catalog, and the workspace index.
- **Verification:** Pending exact read-back.

## Future revision log

Append a new entry whenever the initialization policy or its dependencies change.

Use this template:

### Version N — Short description

- **Date:**
- **Requested change:**
- **Reason:**
- **Behavioral impact:**
- **Files modified:**
- **Verification:**
- **Commit(s):**

## Review checklist

- [ ] Initialization remains conditional.
- [ ] The activation cues remain distinct.
- [ ] Novelist initialization completes foundational initialization first.
- [ ] Foundational initialization runs only once when the user gives both cues.
- [ ] The Worker and its mandatory Conversation Mode reference load during foundational initialization.
- [ ] Agent Skill Authoring loads only on demand.
- [ ] Document Standards loads during foundational initialization.
- [ ] Its catalog and specific assets load only when required.
- [ ] The Worker's archive/media references load only when required.
- [ ] ASD-STE100 loads during foundational initialization.
- [ ] Skill and technical documentation use the approved writing mode.
- [ ] Rewrites preserve meaning, facts, conditions, scope, and modality.
- [ ] Only required files load.
- [ ] Report missing skill prerequisites by exact path and stop initialization.
- [ ] CI status is separate from initialization. No mandatory CI preflight or repair runs before a prompt.
- [ ] Operational instructions remain consistent across initiation files.
- [ ] Commit changes to branch `gpt`. Verify each path after writing.

---

**Maintenance rule:** Update this file when the initialization policy, cues, dependencies, or verification requirements change. Keep operational instructions in their authoritative files.
