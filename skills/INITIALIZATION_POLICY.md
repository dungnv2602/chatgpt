# ChatGPT Initialization Policy — Maintenance Note

## Purpose

Track the design, current behavior, and revision history of ChatGPT's conditional initialization instructions. This note is a maintenance record; the operational instructions remain in the files listed below.

## Source of truth

- **Repository:** `dungnv2602/chatgpt`
- **Branch:** `gpt`
- **Foundational initiation:** `skills/SESSION_START.md`
- **Foundational skill-authoring standard:** `skills/agent-skill-authoring/SKILL.md`
- **Novelist initiation:** `skills/novelist-initiation/INITIATION.md`

Do not treat this note as a replacement for either operational file.

## Current policy

**Initialization is conditional.** Do not retrieve or load project instructions, skills, or references automatically at the beginning of a new conversation.

Wait for an explicit cue:

| Cue | Required behavior |
|---|---|
| `Follow instructions` | Retrieve and read `skills/SESSION_START.md`; execute its complete foundational initialization process, including the mandatory session-start execution gate. Do not initialize a specialist role. |
| `Be the novelist` | Complete and verify foundational initialization first; then follow `skills/novelist-initiation/INITIATION.md`, load the novelist-specific skills, and review the active novel as instructed. |
| Both cues | Complete foundational initialization once, then complete novelist initialization. |

### Operating rules

- Do not initialize automatically at the start of a conversation.
- Do not require the user to say both cues when they say `Be the novelist`; that cue includes the foundational prerequisites.
- Load only the files required by the applicable initiation process.
- Do not load unrelated skills, references, or specialist roles.
- If a required file cannot be retrieved or verified, report its exact path.
- Never claim initialization is complete unless the required retrievals and checks have succeeded.
- The GitHub repository and the `gpt` branch are the sole source of truth for project files, skills, prompts, and references.

## Copyable Custom Instructions

The following is the current Custom Instructions text. Copy this block when configuring ChatGPT, and update it whenever the policy changes.

```text
Repository: "dungnv2602/chatgpt"

Branch: "gpt"

Initialization is conditional. Do not retrieve or load project instructions, skills, or references automatically at the beginning of a new conversation.

Wait until I explicitly use one of these cues:

1. "Follow instructions"
   - Retrieve and read "skills/SESSION_START.md".
   - Execute the complete foundational initialization process defined there, including its mandatory session-start execution gate.
   - Do not initialize a specialist role.

2. "Be the novelist"
   - First complete and verify the foundational initialization process defined in "skills/SESSION_START.md".
   - Then follow "skills/novelist-initiation/INITIATION.md".
   - Load the novelist-specific skills and review the active novel as instructed.
   - Do not require me to say "Follow instructions" first.

3. Both cues
   - Complete foundational initialization only once.
   - Then complete novelist initialization.

Do not load unrelated skills or references. Load only what the applicable initiation instructions require.

If a required file cannot be retrieved or verified, report its exact path. Never claim initialization is complete when it is not.

The GitHub repository "dungnv2602/chatgpt", branch "gpt", is the sole source of truth for project files, skills, prompts, and references.
```

## Design principles

1. **On-demand loading:** Avoid unnecessary retrieval and initialization.
2. **Single foundational authority:** `skills/SESSION_START.md` defines the foundational process.
3. **Explicit dependency:** Novelist initialization must complete foundational prerequisites before loading novelist-specific materials.
4. **No duplicated procedures:** Specialist initiation notes should reference the foundational process rather than maintain a competing checklist.
5. **Current-session verification:** Do not substitute remembered instructions, summaries, or reads from a previous conversation for required verification in the current conversation.
6. **Standardized skills:** Create and maintain skill folders using the Agent Skills format defined in `skills/agent-skill-authoring/SKILL.md`; load that standard during foundational initialization.

## Change history

### Version 1 — Conditional, cue-based initialization

- **Date:** 2026-11-18
- **Change:** Initialization is performed only after an explicit activation cue; automatic startup loading is disabled.
- **Dependency:** `Be the novelist` automatically includes foundational initialization before novelist-specific initialization.
- **Duplicate prevention:** When both cues are used, foundational initialization runs only once.
- **Reason:** Prevent unnecessary loading while preserving the foundational prerequisites for specialist work.
- **Operational files:**
  - `skills/SESSION_START.md`
  - `skills/novelist-initiation/INITIATION.md`

### Version 2 — Agent Skills format made foundational

- **Date:** 2026-11-20
- **Requested change:** Adopt the Agent Skills open format for project skills and establish a foundational skill-authoring standard.
- **Reason:** Make skill metadata, structure, activation, progressive disclosure, and validation consistent and portable.
- **Behavioral impact:** `skills/agent-skill-authoring/SKILL.md` is loaded during explicit foundational initialization and governs skill creation and maintenance. Initialization remains conditional on the established cues.
- **Files modified:** 
  - `skills/agent-skill-authoring/SKILL.md`
  - `skills/SESSION_START.md`
  - `skills/session-archiving/SKILL.md`
  - `skills/INITIALIZATION_POLICY.md`
- **Verification:** Pending read-back verification.
- **Commit(s):** Pending.

## Future revision log

Append a new entry whenever the policy or its activation cues change.

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

Before approving a future change, verify:

- [ ] Initialization remains conditional unless explicitly changed by the user.
- [ ] The activation cues and their distinct responsibilities are unambiguous.
- [ ] Foundational initialization precedes novelist-specific initialization.
- [ ] Foundational initialization is not duplicated when both cues are used.
- [ ] The Agent Skill Authoring skill is loaded during foundational initialization.
- [ ] New or revised skills satisfy the Agent Skills frontmatter, naming, structure, and validation requirements.
- [ ] Only necessary files are loaded.
- [ ] Missing or unverifiable prerequisites stop initialization and are reported by exact path.
- [ ] Operational instructions remain consistent across the two initiation files.
- [ ] The change is committed to the `gpt` branch and verified after writing.

---

**Maintenance rule:** Update this note whenever the initialization policy, activation cues, dependencies, or verification requirements change. Keep executable instructions in the operational files; use this note to track why and how they evolve.
