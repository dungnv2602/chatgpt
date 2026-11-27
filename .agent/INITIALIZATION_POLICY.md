# ChatGPT Initialization Policy

## Purpose

This file records the repository's conditional initialization policy. Operational instructions remain in the files listed below.

## Sources of truth

- Repository: `dungnv2602/chatgpt`
- Branch: `gpt`
- Foundational initialization: `.agent/SESSION_START.md`
- Foundational collaboration and task continuity: `.agent/skills/the-worker/SKILL.md`
- Mandatory Conversation Mode component: `.agent/skills/the-worker/references/conversation-mode.md`
- Agent Skills format, loaded on demand: `.agent/skills/agent-skill-authoring/SKILL.md`
- Technical writing standard: `.agent/skills/asd-ste100/SKILL.md`
- Document governance: `.agent/skills/the-worker/SKILL.md` and `.agent/skills/the-worker/references/document-type-catalog.md`
- Canonical novelist procedure: the Novelist role initialization section in `.agent/SESSION_START.md`
- Drawing tier: The Worker's archive/media references and `.agent/skills/drawing/SKILL.md`, loaded for a drawing session or novelist initialization

This file does not replace an operational skill or initiation procedure.

## Current policy

Initialization is conditional. Do not load project instructions or skills at the start of a new conversation.

The only session-start cue is `/start`. Read `.agent/SESSION_START.md` and follow its complete procedure when the user gives that cue as an instruction.

Every `/start` also triggers the CI-generated P0 batch after baseline initialization. Before batch inspection or execution, send the mandatory wait notice in every conversation mode. Execute all eligible CI Ledger-generated P0 tasks before accepting the user's substantive prompt. Stop before hosted CI results review until the user triggers that phase. After the batch, tell the user that you are ready to take the prompt.

A specialist-role request does not change or satisfy the `/start` cue. It does not authorize foundational initialization. If initialization has not passed in the current conversation, stop and ask the user to say `/start`. After that explicit initialization passes, load the missing specialist tiers required by the role.

## Operating rules

- Do not initialize automatically.
- Do not treat specialist-role requests as session-start cues.
- Specialist-role requests never trigger foundational initialization. Ask for `/start` when it has not passed in the current conversation.
- Load only the files required by the session-start procedure or the requested specialist task.
- Do not load unrelated skills or references.
- Report the exact path of a missing or unverified file.
- Complete initialization after you fetch and read every required skill. CI status is separate from initialization.
- Do not run a CI snapshot or repair unrelated workflow failures before handling a prompt.
- After `/start` baseline initialization, run the mandatory CI Ledger-generated P0 batch before accepting the user's substantive prompt.
- Send the pre-batch wait notice in Default Mode and Condensed Mode. Do not suppress it under the Condensed Mode single-link rule.
- Stop before hosted CI results review. Do not poll, dispatch, rerun, or inspect hosted results until the user triggers results review.
- After the batch ends, tell the user: "Ready to take your prompt."
- Review CI only when the user asks or the current task changes or depends on a specific validation workflow.
- Never wait for or poll CI. Never run the linter or CI workflows locally. Let GitHub Actions execute validation.
- Treat the GitHub repository and branch `gpt` as the sole source of truth.

## Baseline and progressive loading

`/start` loads only:

1. The Worker.
2. The Worker's mandatory Conversation Mode reference.

Load domain skills progressively when the task activates them:

- ASD-STE100 for skill or technical documentation.
- Agent Skill Authoring for skill maintenance.

Load Worker-owned references only when the task requires them:

- `references/ci-ledger.md` and `references/github-actions.md` for the startup P0 batch and other CI work.
- `references/decision-governance.md` for Drafts, ADRs, and repository analysis.
- The Worker's document-governance procedure and catalog for recurring documents and structured records.

Do not activate separate CI Ledger, GitHub Actions, decision-governance, or document-governance skills.

Fetch supporting catalogs, references, templates, and schemas only when required. This preserves the template-first and writing standards without loading unrelated skills at startup.

The Drawing tier is tier 2, not foundational. It includes the Drawing skill and its required references. Load it only after foundational initialization passes. The Worker owns the archive/media procedures used by Drawing. A drawing-session or novelist request does not trigger foundational initialization. Its required references are `.agent/skills/drawing/references/style-guide.md` and `.agent/skills/drawing/references/image-editing-protocol.md`.

Novelist initialization is tier 3. Load `.agent/skills/romantic-storyteller-visual-artist/SKILL.md` only for the explicit novelist role request, after foundational and Drawing tiers are ready.

Maintain a per-conversation verified-load ledger for baseline and task-activated skills. Fetch and read each file once. Refresh only when the user asks, you know or suspect a relevant repository change, or an unresolved instruction requires the current file. Do not reload unrelated files.

The ASD-STE100 skill governs skill documentation and technical documentation. Use Strict mode for operational instructions. Use STE-flavored mode for technical explanations and READMEs.

Preserve facts, conditions, exceptions, scope, and modality. Do not apply the standard to creative writing, dialogue, marketing copy, or approved creative prompts.

The Agent Skill Authoring skill governs skill structure, metadata, validation, and activation when skill work requires it. The ASD-STE100 skill governs technical language across skill and technical documentation.

## Copyable Custom Instructions

Use this exact text when configuring the repository's project instructions:

```text
Repository: "dungnv2602/chatgpt"
Branch: "gpt"

The GitHub repository "dungnv2602/chatgpt", branch "gpt", is the sole source of truth for project files, skills, prompts, references, and archives.

Use ".agent/SESSION_START.md" as the sole source of session-start instructions, and initialize only when I say "/start".

Initialization is conditional. Do not load project instructions or skills at the start of a new conversation.
```

## Design principles

1. **On-demand loading:** Load only what the requested task requires.
2. **Single initialization authority:** `.agent/SESSION_START.md` defines foundational initialization.
3. **Explicit dependency:** Novelist initialization requires foundational initialization first.
4. **No duplicate procedures:** Keep session-start and novelist initialization procedures in `.agent/SESSION_START.md`.
5. **Current-session verification:** Do not use remembered files as a substitute for fresh reads when you must verify.
6. **On-demand skill authoring:** Use `.agent/skills/agent-skill-authoring/SKILL.md` when you create or maintain skills.
7. **Controlled technical writing:** Use `.agent/skills/asd-ste100/SKILL.md` for skill and technical documentation.

## Change history

The entries below are historical. The current policy above takes precedence. A former skill or dependency listed in an old entry is not active unless the current policy lists it.

### Version 1 — Conditional initialization

- **Date:** 2026-11-18
- **Change:** Initialization requires an explicit activation cue.
- **Dependency:** `Be the novelist` includes foundational initialization.
- **Duplicate prevention:** Both cues trigger foundational initialization only once.
- **Reason:** Avoid unnecessary loading while preserving specialist prerequisites.
- **Operational files:** `.agent/SESSION_START.md` and `skills/novelist-initiation/SKILL.md`.

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
- **Behavioral impact:** Initialization depends on successful skill retrieval. CI review and repair apply only when the user asks or the current task depends on a relevant workflow. Use `.takeout/reports/` as the single CI evidence root. The unified `index.json`, `history/`, `latest-lint-report.json`, and `ledger.json` are authoritative.
- **Files modified:** Session Start, Session Archiving, The Worker, GitHub Actions, Agent Skill Authoring, ASD-STE100, and this policy file.
- **Verification:** Pending hosted workflow validation and exact read-back.

### Version 6 — Consolidated foundational collaboration

- **Date:** 2026-11-23
- **Requested change:** Consolidate foundational collaboration and session-start responsibilities into The Worker. Keep ASD-STE100 and GitHub Actions separate.
- **Reason:** Reduce the foundational loading set without losing baseline session, mode, task, or register behavior.
- **Behavioral impact:** Foundational initialization loads The Worker and its mandatory Conversation Mode reference, ASD-STE100, and GitHub Actions. Session Archiving, Agent Skill Authoring, and Document Standards load on demand.
- **Files modified:** The Worker, Conversation Mode compatibility entry point, Session Archiving, Agent Skill Authoring, and Session Start. The change also updated this policy, the skills index, the document-type catalog, and the workspace index.
- **Verification:** Pending exact read-back.


### Version 7 — Relocated workflow paths and cue alignment

- **Date:** 2026-11-26
- **Requested change:** Adapt initialization policy to the reconstructed `.agent/` layout and the user's `/start` cue.
- **Reason:** The former root `skills/` paths and `start session` cue conflicted with the current repository layout and user configuration.
- **Behavioral impact:** Current path references use `.agent/SESSION_START.md` and `.agent/skills/`. The initialization cue is `/start`. The migration did not restore any former files.
- **Files modified:** `.agent/INITIALIZATION_POLICY.md`, `.agent/SESSION_START.md`.
- **Verification:** Pending committed read-back.
- **Commit(s):** Read-back verified.

## Future revision log

### Version 8 — Progressive baseline initialization

- **Date:** 2026-11-27
- **Requested change:** Keep `/start` working while reducing unnecessary skill retrieval. Make GitHub Actions domain-foundational, not universally loaded.
- **Reason:** Baseline initialization should establish collaboration and continuity without loading domain skills that are not relevant to the current task.
- **Behavioral impact:** `/start` loads The Worker and Conversation Mode only. CI, document governance, technical writing, and skill authoring load on demand. The GitHub Actions skill is task-activated and remains authoritative for CI work.
- **Files modified:** `.agent/SESSION_START.md`, `.agent/INITIALIZATION_POLICY.md`, `.agent/skills/github-actions/SKILL.md`.
- **Verification:** Committed read-back verification pending.
- **Commit(s):** `764d771`, `f9a3e2f`, `11a5475`, `7bcb449`.

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

### Version 10 — Queue-draining execution and one-at-a-time blockers

- **Date:** 2026-11-28
- **Requested change:** Continue independent eligible work when one task blocks. Ask the user about one essential blocker at a time.
- **Reason:** Existing guidance did not require immediate queue reselection or clearly prohibit routine blocker notifications before quiescence.
- **Behavioral impact:** The Worker rebuilds the full eligible queue after task-state, approval, and dependency changes. It skips isolated blockers and continues independent work. Conversation Mode suppresses routine task-level pings. Session Start applies the same rule to the mandatory P0 batch.
- **Files modified:** `.agent/skills/the-worker/SKILL.md`, `.agent/skills/the-worker/references/conversation-mode.md`, `.agent/SESSION_START.md`, `.agent/INITIALIZATION_POLICY.md`, and `workspace/task_board.md`.
- **Verification:** Pending committed read-back.
- **Commit(s):** Pending.

### Version 9 — CI P0 batch during session startup

- **Date:** 2026-11-27
- **Requested change:** Run the eligible CI-generated P0 batch after every successful `/start` initialization and before accepting the user's substantive prompt. Send a mandatory pre-batch wait notice.
- **Reason:** The user wants the Worker to complete all eligible CI P0 remediation before the next prompt arrives.
- **Behavioral impact:** Session Start activates CI Ledger and GitHub Actions. It sends the notice in every conversation mode and runs all eligible Ledger-generated P0 tasks. It stops before hosted results review and then tells the user that it is ready. The Worker owns batch orchestration. Conversation Mode permits the required notice and readiness message in Condensed Mode.
- **Files modified:** `.agent/SESSION_START.md`, `.agent/INITIALIZATION_POLICY.md`, `.agent/skills/the-worker/SKILL.md`, `.agent/skills/the-worker/references/conversation-mode.md`.
- **Verification:** Pending committed read-back.
- **Commit(s):** Pending.

## Review checklist

- [ ] Initialization remains conditional.
- [ ] The activation cues remain distinct.
- [ ] Novelist initialization completes foundational initialization first.
- [ ] Foundational initialization runs only once when the user gives both cues.
- [ ] Baseline initialization loads only The Worker and its mandatory Conversation Mode reference.
- [ ] After baseline initialization, every `/start` activates CI Ledger and GitHub Actions for the mandatory P0 batch.
- [ ] The pre-batch notice and readiness message appear in both conversation modes.
- [ ] Other domain skills activate only when the current task requires them.
- [ ] Agent Skill Authoring loads only on demand.
- [ ] Document governance runs through The Worker without a separate skill activation.
- [ ] The Worker loads its CI Ledger and GitHub Actions references for the startup P0 batch.
- [ ] The Worker loads its decision-governance reference only when required.
- [ ] The Worker's archive/media references load only when required.
- [ ] ASD-STE100 loads only when skill or technical documentation activates.
- [ ] Skill and technical documentation use the approved writing mode.
- [ ] Rewrites preserve meaning, facts, conditions, scope, and modality.
- [ ] Only required files load.
- [ ] Report missing skill prerequisites by exact path and stop initialization.
- [ ] CI status is separate from initialization. No mandatory CI preflight or repair runs before a prompt.
- [ ] Operational instructions remain consistent across initiation files.
- [ ] Commit changes to branch `gpt`. Verify each path after writing.

---

**Maintenance rule:** Update this file when the initialization policy, cues, dependencies, or verification requirements change. Keep operational instructions in their authoritative files.
