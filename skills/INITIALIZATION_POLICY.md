# ChatGPT Initialization Policy

## Purpose

This file records the repository's conditional initialization policy. Operational instructions remain in the files listed below.

## Sources of truth

- Repository: `dungnv2602/chatgpt`
- Branch: `gpt`
- Foundational initialization: `skills/SESSION_START.md`
- Mandatory execution gate: `skills/session-archiving/SKILL.md`
- Agent Skills format: `skills/agent-skill-authoring/SKILL.md`
- Technical writing standard: `skills/asd-ste100/SKILL.md`
- Novelist initialization: `skills/novelist-initiation/SKILL.md`

This file does not replace an operational skill or initiation procedure.

## Current policy

Initialization is conditional. Do not load project instructions or skills at the start of a new conversation.

Wait for an explicit cue:

| Cue | Required behavior |
|---|---|
| `Follow instructions` | Read `skills/SESSION_START.md`. Complete the foundational execution gate. Do not activate a specialist role. |
| `Be the novelist` | Complete foundational initialization first. Then follow `skills/novelist-initiation/SKILL.md`. Load the novelist skills and review the active novel. |
| Both cues | Complete foundational initialization once. Then complete novelist initialization. |

## Operating rules

- Do not initialize automatically.
- Do not ask the user to give both cues when `Be the novelist` is sufficient.
- Load only the files required by the selected initialization path.
- Do not load unrelated skills or references.
- Report the exact path of a missing or unverified file.
- Do not claim initialization is complete until every required check passes.
- Treat the GitHub repository and branch `gpt` as the sole source of truth.

## Foundational standards

Foundational initialization loads these skills:

1. Session Archiving.
2. Conversation Mode.
3. Agent Skill Authoring.
4. ASD-STE100.
5. Drawing and its required foundational references.

The ASD-STE100 skill governs skill documentation and technical documentation. Use Strict mode for operational instructions. Use STE-flavored mode for technical explanations and READMEs.

Preserve facts, conditions, exceptions, scope, and modality. Do not apply the standard to creative writing, dialogue, marketing copy, or approved creative prompts.

The Agent Skill Authoring skill governs skill structure, metadata, validation, and activation. The ASD-STE100 skill governs technical language.

## Copyable Custom Instructions

Use this text when configuring the repository's project instructions:

```text
Repository: "dungnv2602/chatgpt"
Branch: "gpt"

Initialization is conditional. Do not load project instructions or skills at the start of a new conversation.

Wait for an explicit cue:

1. "Follow instructions"
   - Read "skills/SESSION_START.md".
   - Complete its foundational execution gate.
   - Do not activate a specialist role.

2. "Be the novelist"
   - Complete foundational initialization first.
   - Then follow "skills/novelist-initiation/SKILL.md".
   - Load the novelist skills and review the active novel.
   - Do not require me to give "Follow instructions" first.

3. Both cues
   - Complete foundational initialization once.
   - Then complete novelist initialization.

Do not load unrelated skills or references.
Report the exact path of any missing or unverified file.
Do not claim initialization is complete before all checks pass.

Use "skills/asd-ste100/SKILL.md" for all skill documentation and technical documentation.
Use Strict mode for operational instructions.
Use STE-flavored mode for technical explanations and READMEs.
Preserve meaning, conditions, scope, and modality.
Do not apply the standard to creative writing or approved creative prompts.

The GitHub repository "dungnv2602/chatgpt", branch "gpt", is the sole source of truth for project files, skills, prompts, references, and archives.
```

## Design principles

1. **On-demand loading:** Load only what the requested task requires.
2. **Single initialization authority:** `skills/SESSION_START.md` defines foundational initialization.
3. **Explicit dependency:** Novelist initialization requires foundational initialization first.
4. **No duplicate procedures:** Specialist initiation files link to the foundational procedure.
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
- **Reason:** Standardize metadata, structure, activation, progressive disclosure, and validation.
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

### Version 5 — First repository documentation audit pass

- **Date:** 2026-11-20
- **Change:** Rewrite five technical documents under the repository ASD-STE100 policy.
- **Files modified:**
  - `skills/session-archiving/references/image-processing-scripts.md`
  - `skills/session-archiving/references/drawing-session-closeout.md`
  - `novels/README.md`
  - `novels/WORKFLOW.md`
  - `images/takeout/README.md`
- **Verification:** Retrieved each changed path from branch `gpt` after the write. Read-back confirmed the committed content and required sections.
- **Validation limit:** The ASD-STE100 linter and the full repository audit have not run. The audit remains in progress.
- **Commits:** `683d0367f0fd171403990189dca0e2169b8f491e`, `8dd008db79fe086728d97cf85802e40ebc1b8fc1`, `44a624833db2e82f86da0dd34c140ee5eb5cffbf`, `8832f92875c057c1d4903f6ed800eb9481830e11`, and `48fd5805622c66f1a27786ee1640a1929cc5e479`.

### Version 6 — Second repository documentation audit pass

- **Date:** 2026-11-20
- **Change:** Revise additional skill instructions, references, image documentation, and current novel templates.
- **Files modified:**
  - `skills/SESSION_START.md`
  - `skills/novelist-initiation/INITIATION.md`
  - `skills/drawing/SKILL.md` (reviewed, not rewritten)
  - `skills/drawing/references/image-editing-protocol.md`
  - `skills/drawing/references/archive-and-delivery.md`
  - `skills/drawing/references/generation-recovery-and-provenance.md`
  - `skills/drawing/references/series-continuity-and-iteration.md`
  - `skills/conversation-mode/SKILL.md`
  - `skills/agent-skill-authoring/SKILL.md`
  - `skills/session-archiving/SKILL.md`
  - `skills/session-archiving/references/image-provenance-and-webp.md`
  - `skills/session-archiving/references/archive-records-and-image-prompts.md`
  - `skills/romantic-storyteller-visual-artist/references/novel-production-workflow.md`
  - `skills/philosophy-religion-asceticism/README.md`
  - `skills/philosophy-religion-asceticism/SKILL.md`
  - `skills/philosophy-religion-asceticism/references/research-method.md`
  - `skills/philosophy-religion-asceticism/references/source-standards.md`
  - `skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md`
  - `images/README.md`
  - `novels/templates/scene-v1.1.md`
  - `novels/templates/illustration-prompt-v1.1.md`
  - `novels/README.md`
- **Verification:** Fetched changed paths from branch `gpt` after each write. Read-back confirmed committed content.
- **Validation limit:** The repository linter has not run. This environment has no repository shell or GitHub Action dispatch tool. Manual screening does not replace the linter.
- **Manual screening:** Scans checked semicolons, selected phrasal verbs, marketing adjectives, selected nominalizations, and instruction sentence length in revised files. The scans found two semicolons, one missing sentence boundary, one nominalized verb phrase, and several long instructions. Those findings were corrected and read back.
- **Latest reference scan:** A targeted scan of four Drawing, archive, and curriculum references found no semicolons, selected phrasal verbs, marketing adjectives, or tested nominalization patterns. The scans do not test every STE rule.
- **Path-policy conflict:** The Session Archiving skill lists five approved roots: `images/`, `master/`, `novels/`, `drawings/`, and `skills/`. The same skill and its references also direct non-novel drawing assets to `drawings/YYYY-MM-DD/images/`. That path is outside the listed roots. I did not change the boundary or access the `drawings/` path. Resolve this conflict before further work in that path.
- **Master inventory:** The initial fetch of `master/README.md` returned 404. A later read-only directory listing found `master/Images.md`, `master/Poses.md`, and `master/Prompts.md`. The directory has no README. Review classified these files as prompt, pose, and creative source material. They remain unchanged.
- **Remaining work:** Continue auditing any unreviewed technical documents. Run the official linter in a repository execution environment and review its findings. Resolve the `drawings/` workspace conflict before following historical archive links. The `drawings/` directory listing returned 404, so its contents remain unverified.
- **Commits:** `1cc5e5d623e8200316d009dc2219a74287c591fc`, `f898c0bd2fc68a123df16f1b0b6ce44d13ba7e9d`, `82df4add11b03428ac1a49ba948e24ccf9e78e35`, `5bf95f28bc4cbbd645ae86fc4407fbdc32826b01`, `29a58b17304c56e986e39af15d2867b955e17665`, `2333a0378f0f6aebad5bdd7b31801d57ee04dfb0`, `5f1a78b68e655e10160d852fd81be65d937f4111`, `f47d07242b7605dded9d17b2ba82425e34e48cd2`, `3f223f69f1aaff0da7643f81ea58ce950746085d`, `11752c6e9eeaabe66580ae3d69de46e3ef6f649a`, `29103811aba608d25914d699473685f6b06cebc3`, `f56f8385c2f96ca0f8a29e64f925071511aa8363`, `91e427e1f4a63246a78b1c0eab596d2abb649284`, `01fde065c45c98b4ee7b4cce399417cfc2595e85`, `50a972bbbaa0a84231cc0dfeaf9b0305f3a19374`, `0e5e4d60adcd319fa0ad252d6bebed7e06b02122`, `2b3e4591b72bb32b61707c1e73efef4f03a99cf9`, `eae21daa515a6c6838259e72722f773c698c3d2e`, `055ee65bfe5b288100a69ea9087b7cbee469da88`, `cd8764c39910e6fd84e00824b4d506fa0408a80b`, `7071f87b33911da4f76a59aca9ffd64226b78a47`, `bfb881d37aa96b3efffcbe628053cc235ea1fbac`, `9dc453ea7df070edaa5a38bd5fa49b4459631a11`, `548fe068a33a5be753b55f0f04b96268c990b871`, `7148f3a9218845fc46a55d7d461c6b252fb73442`, `dcc8f6cc9eef17ae14babc2d9d7ee2cea398452d`, `248e444a8a8865b7e77efa0f89f63848f7cbe93b`, `2e68385e3cf4d8c9c8a8ac57c3e78f3cdd467b87`, `703e9f258adc015d76962f7e8484313cea6e0fbb`, `dbab4dbb61a714d53962cd2968e331ca9b61325c`, and `af6fac5b108cdfa061e72ee4f75f4837fb4b3f1c`.
 
### Version 7 — Third repository documentation audit pass

- **Date:** 2026-11-20
- **Change:** Revise Prompt Master, Romantic Storyteller, and Drawing pattern documentation. Expand read-only directory inventory for approved repository roots.
- **Files modified:**
  - `skills/romantic-storyteller-visual-artist/SKILL.md`
  - `skills/prompt-master/SKILL.md`
  - `skills/prompt-master/references/templates.md`
  - `skills/drawing/references/patterns/README.md`
  - `skills/drawing/references/patterns/PATTERN-TEMPLATES.md`
  - `skills/drawing/references/patterns/failure-patterns.md`
  - `skills/drawing/references/patterns/successful-patterns.md`
- **Review-only files:** `skills/prompt-master/references/patterns.md`, `skills/drawing/README.md`, `skills/asd-ste100/README.md`, `skills/philosophy-religion-asceticism/CHANGELOG.md`, and `skills/prompt-master/README.md`. The Prompt Master README contains marketing copy and product examples. The policy excludes marketing copy and approved examples from controlled-language rewrites.
- **Preserved source material:** `master/Images.md`, `master/Poses.md`, and `master/Prompts.md` contain prompts, pose ideas, and creative text. They were inspected and left unchanged. Prompt templates, worked examples, and historical pattern evidence were also preserved except for nearby explanatory prose.
- **Inventory:** Read-only listings verified the contents of `skills/`, `skills/*/references/`, `skills/drawing/references/patterns/`, and `master/`. The root `drawings/` listing returned 404. Do not infer that the directory is empty.
- **Drawing archive links:** The pattern indexes contain historical links into `drawings/`. That root remains outside the approved workspace roots listed by Session Archiving. I did not follow or modify those links. Their targets remain unverified.
- **Link checks:** Internal links in the revised Prompt Master, Romantic Storyteller, and Drawing pattern files point to existing repository paths. Historical `drawings/` links remain unverified.
- **Manual screening:** The edited prose was checked for semicolons and selected sentence-length, phrasal-verb, and structural patterns. The identified findings were revised and read back. These checks are limited and do not replace the official linter.
- **Validation limit:** The official `skills/asd-ste100/scripts/ste-lint.py` was not run. This environment provides repository file and read-only GitHub API operations, but no repository shell or workflow-dispatch action.
- **Read-back verification:** Every changed file was fetched from branch `gpt` after its write. The returned content matched the submitted content.
- **Commits:** `67d88bab7ae188d7c4c5651ebce2e631e88cdda1`, `b7c6d71540efa42d6537cb26cf4ff289a7d69691`, `67ef8472779deac010ba294650fbaa708dab1db1`, `9fa6cbaf7251014a84de3d6f90fda9a1602b467b`, `32d2b9b28e43e9166149bb9e8614ee46ec1b90f4`, `b9f1a49c61e5523eaa1f07d8f22d366869fda82d`, `7157070e5fc3182140ae2bfb5a43ef9d16f96030`, `75b7a9a9c577e48c2fa76b149c6328fbd4e88f4a`, `0a07bcedfa8d1f08a57885c68006dc418cfd1e70`, `b45db648a96f7043de442c5749ecf6b2eab169dc`, `3c5ef19ffc65eeadacad930e916eb90c40b62903`, and `07b42dad84ddda25eb14f242d62850918e876dc0`.

### Version 8 — Active novel template review

- **Date:** 2026-11-20
- **Change:** Complete the review of the active v1.1 novel templates. Remove semicolons from two template placeholder fields.
- **Files modified:**
  - `novels/templates/novel-v1.1.md`
  - `novels/templates/illustration-note-v1.1.md`
- **Review-only files:** `novels/templates/arc-v1.1.md`, `novels/templates/character-profile-v1.1.md`, `novels/templates/development-outline-v1.1.md`, and `novels/templates/open-discussion-v1.1.md` had no identified findings. The v1.1 scene and illustration-prompt templates were reviewed in the earlier pass. Their apparent long lines contain multiple short sentences or creative-writing placeholders.
- **Preserved files:** The v1.0 templates remain historical references. No mass migration or rewrite was performed.
- **Validation:** The two edited files were fetched after each write. Their read-back content matched the submitted text. Both now contain zero semicolons. The official ASD-STE100 linter has not run.
- **Commits:** `0f0a381d042d08aaf3afe29cd8647c1f35d2ea9a` and `2acb3b2511aa8dcd3cd27c5f5574967805877888`.

### Version 9 — Linter and CI capability review

- **Date:** 2026-11-20
- **Change:** Review the official linter source and existing GitHub Actions workflows to identify a valid execution route.
- **Files reviewed:** `skills/asd-ste100/scripts/ste-lint.py`, `.github/workflows/convert-images-to-webp.yml`, and `.github/workflows/notification.yml`.
- **Linter scope:** The linter checks semicolons, selected phrasal verbs, marketing adjectives, nominalizations, long sentences, synonym rotation, and dangling conjunctions. Passive voice and present-perfect findings are advisory. It protects hedges and does not claim to check noun clusters.
- **Self-test:** Not run. This environment cannot execute the repository script.
- **CI review:** Existing workflows process image takeout and send tag notifications. Neither runs the STE linter. No workflow-dispatch action is available through the connected GitHub tools.
- **Next validation step:** Run `python3 skills/asd-ste100/scripts/ste-lint.py --selftest` in a repository shell. Then run it against the applicable operational files and review each finding.
- **Validation status:** Source review only. The linter remains unexecuted.

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
