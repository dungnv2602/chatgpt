# ChatGPT Initialization Policy

## Purpose

This file records the repository's conditional initialization policy. Operational instructions remain in the files listed below.

## Sources of truth

- Repository: `dungnv2602/chatgpt`
- Branch: `gpt`
- Foundational initialization: `skills/SESSION_START.md`
- Task continuity: `skills/the-worker/SKILL.md`
- Mandatory execution gate: `skills/session-archiving/SKILL.md`
- Agent Skills format: `skills/agent-skill-authoring/SKILL.md`
- Technical writing standard: `skills/asd-ste100/SKILL.md`
- Canonical novelist procedure: the Novelist role initialization section in `skills/SESSION_START.md`
- Drawing prerequisite: `skills/drawing/SKILL.md`, loaded for novelist initialization or a drawing session

This file does not replace an operational skill or initiation procedure.

## Current policy

Initialization is conditional. Do not load project instructions or skills at the start of a new conversation.

The only session-start cue is `start session`. Read `skills/SESSION_START.md` and follow its complete procedure when the user gives that cue as an instruction.

A specialist-role request does not change the `start session` cue. It authorizes automatic loading of missing prerequisite tiers. For a drawing-session or novelist request, complete foundational initialization first if it has not passed in the current conversation. Then follow the dependency order below.

## Operating rules

- Do not initialize automatically.
- Do not treat specialist-role requests as session-start cues.
- Load only the files required by the session-start procedure or the requested specialist task.
- Do not load unrelated skills or references.
- Report the exact path of a missing or unverified file.
- Do not claim initialization is complete until every required check passes.
- Treat the GitHub repository and branch `gpt` as the sole source of truth.

## Foundational standards

Foundational initialization loads these skills:

1. Session Archiving.
2. Conversation Mode.
3. The Worker.
4. Agent Skill Authoring.
5. ASD-STE100.
6. GitHub Actions.

The Drawing skill is tier 2, not foundational. Load it for a drawing session or as a prerequisite for novelist initialization. Its required references are `skills/drawing/references/style-guide.md` and `skills/drawing/references/image-editing-protocol.md`.

Novelist initialization is tier 3. Load `skills/romantic-storyteller-visual-artist/SKILL.md` only for the explicit novelist role request, after foundational and Drawing tiers are ready.

Maintain a per-conversation verified-load ledger. Retrieve and read each required skill or reference once. Reuse it when entering a higher tier or returning to a prior tier. A new conversation starts a new ledger. Refresh only when the user asks, a relevant repository change is known or suspected, or an unresolved instruction requires the current file. Do not reload an entire tier to refresh one file.

The ASD-STE100 skill governs skill documentation and technical documentation. Use Strict mode for operational instructions. Use STE-flavored mode for technical explanations and READMEs.

Preserve facts, conditions, exceptions, scope, and modality. Do not apply the standard to creative writing, dialogue, marketing copy, or approved creative prompts.

The Agent Skill Authoring skill governs skill structure, metadata, validation, and activation. The ASD-STE100 skill governs technical language.

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
5. **Current-session verification:** Do not use remembered files as a substitute for fresh reads when verification is required.
6. **Agent Skills format:** Use `skills/agent-skill-authoring/SKILL.md` to create and maintain skills.
7. **Controlled technical writing:** Use `skills/asd-ste100/SKILL.md` for skill and technical documentation.

## Change history

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
- **Verification:** Read-back checks passed. The official `skills-ref` CLI validator was not run.
- **Initial commits:** `5bdb1b732c88fc4bb0d9e49fbeb78eb6048c7bc5`, `b26c37031399747ea204fa89a491a8ff26bce911`, `a48f7264246734a73b02f41537f367f04fa09c55`, and `fee7c31d7c7b2f63efee3680796ac477b060eb45`.

### Version 3 — Skill directory restructure

- **Date:** 2026-11-20
- **Change:** Apply Agent Skills format to the repository's skill folders.
- **Reason:** Make skills discoverable and reduce unnecessary loading.
- **Behavioral impact:** Every skill folder gained a conforming `SKILL.md`. Detailed procedures moved into focused references. Foundational initialization remained conditional.
- **Verification:** Manual metadata, naming, description, line-count, link, activation, and read-back checks passed. The official validator was not run.

### Version 4 — ASD-STE100 made foundational

- **Date:** 2026-11-20
- **Change:** Make ASD-STE100 a foundational skill. Apply its writing modes to skill documentation and technical documentation.
- **Reason:** Reduce ambiguity without changing technical meaning.
- **Behavioral impact:** Foundational initialization now loads ASD-STE100. Use Strict mode for operational instructions and STE-flavored mode for technical explanations. Creative content and intentional examples remain outside the policy.
- **Files modified:** ASD-STE100, Session Start, Session Archiving, Agent Skill Authoring, Skills README, and this policy file.
- **Verification:** Initial read-back completed. The current documentation audit remains in progress.

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
- [ ] Foundational initialization runs only once when both cues are given.
- [ ] Agent Skill Authoring loads during foundational initialization.
- [ ] ASD-STE100 loads during foundational initialization.
- [ ] Skill and technical documentation use the correct writing mode.
- [ ] Rewrites preserve meaning, facts, conditions, scope, and modality.
- [ ] Only required files load.
- [ ] Missing prerequisites stop initialization and are reported by exact path.
- [ ] Operational instructions remain consistent across initiation files.
- [ ] Changes are committed to branch `gpt` and verified after writing.

---

**Maintenance rule:** Update this file when the initialization policy, cues, dependencies, or verification requirements change. Keep operational instructions in their authoritative files.
