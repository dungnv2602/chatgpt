---
name: agent-skill-authoring
description: Create, revise, check, organize, and integrate Agent Skills-compatible skill folders. Use when you add or update a skill, edit its metadata or references, check it, or choose its initialization tier.
metadata:
  project-role: task-specific
  format: agentskills
  specification: https://agentskills.io/specification
---

# Agent Skill Authoring

## 1. Purpose and authority

Use this skill whenever a skill folder or any of its operational instructions are created, revised, reorganized, checked, or integrated into the repository's loading workflow.

The Agent Skills open specification is the format authority:
- Specification: https://agentskills.io/specification
- Source repository: https://github.com/agentskills/agentskills

The repository `dungnv2602/chatgpt`, branch `gpt`, is the sole source of truth for project files and decisions. The external specification defines the portable skill format. It does not override user instructions, repository policy, or activation cues.

Do not assume that placing a folder in `skills/` automatically makes a client load it. Format compliance, discoverability, activation, and foundational initialization are separate concerns and must each be handled explicitly.

## 2. Required skill structure

Every new or converted skill must be a directory whose name matches the required `name` field in its `SKILL.md`.

Minimum structure:

```text
skill-name/
└── SKILL.md
```

Optional resources may be included when they materially support the skill:

```text
skill-name/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

Use:
- `references/` for focused supporting documentation loaded when needed.
- `scripts/` for executable tools, with dependencies, invocation, and error behavior documented.
- `assets/` for static templates, examples, images, or other non-instructional resources.

Do not create empty or speculative directories. Add only the resources the skill actually needs.

## 3. Mandatory YAML frontmatter

The first content in every `SKILL.md` must be YAML frontmatter, delimited by `---`, followed by the Markdown instructions.

The required fields are:

- `name`
- `description`

Example:

```yaml
---
name: skill-name
description: Explains what the skill does and when an agent should use it.
---
```

### 3.1 Name rules

The `name` value must:

1. Be 1–64 characters long.
2. Contain only lowercase ASCII letters (`a-z`), numbers (`0-9`), and single hyphens.
3. Not start or end with a hyphen.
4. Not contain consecutive hyphens.
5. Match the containing skill directory name exactly.

A practical validation expression is:

```regex
^[a-z0-9]+(?:-[a-z0-9]+)*$
```

Do not use display titles, uppercase letters, spaces, underscores, or abbreviations that violate these rules in the `name` field. A human-readable heading may use normal title capitalization inside the Markdown body.

### 3.2 Description rules

The `description` value must:

1. Be non-empty and no longer than 1024 characters.
2. State what the skill does.
3. State when an agent should use it.
4. Include specific task terms that help identify relevant requests.

Avoid vague descriptions such as “Helps with writing” or descriptions that list capabilities without giving activation context.

### 3.3 Optional fields

Use optional frontmatter only when it provides real value:

- `license`: a license name or a reference to a bundled license file.
- `compatibility`: environment requirements, intended product, required packages, or network needs. Keep this field within the specification's 500-character limit.
- `metadata`: a YAML mapping of additional keys to string values. Prefer stable, namespaced or project-specific keys.
- `allowed-tools`: a space-separated tool list. This field is experimental. Client support varies. Do not rely on it for mandatory permissions or safety controls.

Do not invent a license, compatibility requirement, author, version, or tool grant. Omit fields that are not known or needed.

## 4. Write the skill for progressive disclosure

Agent Skills use three conceptual stages:

1. **Discovery:** the client can inspect the skill's name and description without loading the full body.
2. **Activation:** when the request matches, the client loads the full `SKILL.md`.
3. **Execution:** the agent follows the instructions and loads supporting resources only when needed.

Structure content accordingly:

- Put the core purpose, activation conditions, required workflow, critical constraints, and completion checks in `SKILL.md`.
- Move extensive examples, schemas, domain references, and long procedures into focused files under `references/`.
- Load a reference only when the task needs it.
- Do not make a critical rule discoverable only in an optional reference if the agent must know that rule to use the skill safely.
- Avoid duplicating the same operational rule across several skills. Keep one authoritative home and link to it.

Keep the main `SKILL.md` under 500 lines where practical. The specification recommends keeping the activated instruction body below roughly 5,000 tokens. These are design recommendations, not substitutes for completeness: retain every instruction necessary for reliable execution and move secondary detail into references.

## 5. Authoring workflow

For each new skill or material revision:

1. **Define scope.** State the capability, the user requests that activate it, its boundaries, and what it does not own.
2. **Identify authority.** Determine which user instructions, project policies, canonical records, and other skills govern the task. Do not invent a new authority hierarchy.
3. **Inspect existing material.** Read the exact current files and relevant links before changing them. Reuse established terminology and avoid creating a competing skill for an existing responsibility.
4. **Choose the directory name.** Use a concise, descriptive, lowercase hyphenated name that satisfies the specification.
5. **Write frontmatter first.** Check the name-directory match and the description before drafting the body. Start from `assets/SKILL_TEMPLATE.md` and remove sections that do not apply.
6. **Write executable instructions.** Use clear activation criteria, ordered steps, decision points, edge cases, and verification requirements. Distinguish mandatory rules from recommendations.
7. **Separate supporting material.** Add references, scripts, or assets only when needed. Keep references focused and avoid deep chains of linked references.
8. **Integrate activation.** Decide whether the skill is foundational or task-specific. Update only the appropriate initiation file, index, or dependency record.
9. **Check consistency.** Resolve contradictions with the authoritative project rules. Do not silently change user preferences, activation cues, or established workflow boundaries.
10. **Check.** Check frontmatter, paths, links, references, line length where relevant, and the complete operational logic.
11. **Commit and read back.** Follow repository write discipline, then fetch the exact committed path and check the final content.
12. **Report precisely.** Identify the created or changed paths, the commit result, the verification performed, and any limitation that remains.

## 6. Foundational versus task-specific skills

A skill's location under `skills/` does not decide whether it is foundational.

### Foundational skill

A skill is foundational only when it governs baseline collaboration, repository operation, initialization, or a cross-cutting rule required before specialist work.

To make a skill foundational:

1. Ask for explicit user direction when the classification is not already clear from the request.
2. Add the skill to the canonical loading sequence in `skills/SESSION_START.md` only when it must load before ordinary project work.
3. Record the dependency in `skills/INITIALIZATION_POLICY.md` when it changes the initialization contract.
4. Keep activation conditional on the project's explicit initialization cues. Do not introduce automatic loading at the beginning of every conversation unless the user explicitly requests that policy.
5. Define whether the skill is loaded once per conversation, refreshed only when changed, or consulted on demand. Avoid redundant retrievals.
6. Check that the new dependency does not activate a specialist role or load unrelated task-specific materials.

This skill is task-specific. Load it when you create, revise, check, reorganize, or integrate a skill. Do not load it during ordinary foundational initialization. The Worker owns the baseline session and collaboration rules.

### Task-specific skill

A task-specific skill is loaded when a request matches its description or when a relevant initiation procedure explicitly requires it. Do not add task-specific skills to universal startup merely to make them discoverable.

Agent Skill Authoring is task-specific. It applies to skill creation and maintenance. The Agent Skills format does not make the authoring skill a prerequisite for unrelated project work.

### Activation is not initialization

Agent Skills metadata helps a compatible client discover a skill. It does not itself change this repository's activation cues or prove that a skill has been loaded. Repository-specific loading must be explicitly connected to the authoritative initialization procedure.

## 7. ASD-STE100 technical writing standard

Use the [ASD-STE100 skill](../asd-ste100/SKILL.md) whenever you create or revise skill documentation. Use the [repository writing policy](../asd-ste100/references/repository-writing-policy.md) for technical documentation.

Choose the mode before you write:

- **Strict mode** applies to procedures, tool descriptions, system prompts, error messages, safety instructions, and inter-agent instructions.
- **STE-flavored mode** applies to READMEs, change logs, technical explanations, and reference prose.

Apply these rules in both modes:

1. Use active voice when the actor is known and relevant.
2. Put one instruction in each sentence.
3. Keep instructions within 20 words.
4. Keep descriptive sentences within 25 words.
5. Use no more than six sentences per paragraph.
6. Use a list for sequences with three or more steps or conditions.
7. Do not use semicolons.
8. Prefer clear verbs over phrasal verbs and nominalizations.
9. Keep noun clusters to three words or fewer.
10. Use consistent names for the same concept.

Strict mode also requires one clear meaning for each term. It requires simple words when they preserve technical meaning. STE-flavored mode treats those lexical rules as guidance.

Preserve all facts, conditions, exceptions, numbers, scope limits, and modality. Never turn an uncertain claim into a certain claim. Never add a cause or result that the source does not state.

Do not rewrite creative writing, dialogue, marketing copy, approved creative prompts, code, or examples that intentionally demonstrate a rule violation.

Do not run the linter or CI workflows locally. Push technical-document changes to branch `gpt`. Let GitHub Actions check them.

CI review is task-scoped. Inspect the relevant workflow only in these cases:

- The user requests it.
- The skill-authoring task changes validation or workflow configuration.
- A known result directly blocks the task.

Use `reports/gh_ac_reports/` for workflow evidence and `reports/lint_reports/` for lint findings. Track cross-family issues in `reports/triage/ledger.json`. Do not repair unrelated failures before handling a prompt. Never wait or poll. Let GitHub-hosted Actions run validation.

The linter checks only supported patterns. It cannot prove meaning or dictionary compliance.

Do not claim certified ASD-STE100 compliance. The repository does not contain the official controlled dictionary.

## 8. Reference and path rules

- Resolve relative file references from the skill root.
- Prefer direct references one level below the skill root, such as `references/guide.md`.
- Avoid long chains where one reference points to another reference that points elsewhere.
- Check every local link after moving or renaming files.
- Keep each canonical policy in one location. Other skills should link to that policy rather than copy it.
- Do not link to a file that has not been created and verified.
- If a skill depends on external standards, name the canonical source and summarize the rules needed for reliable local execution.

## 9. Validation checklist

Before considering a skill complete, check all of the following:

### Format
- [ ] The skill is a directory containing `SKILL.md`.
- [ ] The first content in `SKILL.md` must be valid YAML frontmatter.
- [ ] `name` and `description` are present and non-empty.
- [ ] The name is 1–64 characters, lowercase, validly hyphenated, and matches the directory.
- [ ] The description is no longer than 1024 characters and explains both purpose and activation.
- [ ] Optional fields are valid, useful, and not fabricated.
- [ ] Every `metadata` value is a string.

### Instruction quality
- [ ] Activation conditions are concrete and relevant.
- [ ] Authority, scope, workflow, boundaries, edge cases, and completion checks are clear.
- [ ] Mandatory instructions are distinguishable from recommendations.
- [ ] Critical instructions are in `SKILL.md`, not hidden in optional references.
- [ ] The main file is concise enough to activate without unnecessary context burden.
- [ ] Supporting resources are focused and loaded only as needed.
- [ ] No contradictory, duplicated, stale, or unrequested rules have been introduced.
- [ ] Use the applicable ASD-STE100 mode for skill and technical documentation.
- [ ] Sentence length, paragraph structure, and punctuation follow the repository writing policy.
- [ ] Every rewrite preserves facts, conditions, scope, and modality.
- [ ] Do not wait for CI, poll for results, or run lint and CI workflows locally.

### Integration and integrity
- [ ] The skill is connected to the intended activation path.
- [ ] Foundational loading remains conditional on the user's established cues.
- [ ] No unrelated specialist skill has been made foundational.
- [ ] Every referenced local file exists and every relative link resolves.
- [ ] The exact committed file has been read back and verified.
- [ ] The final report distinguishes completed checks from checks that were unavailable.

When the official `skills-ref` validator is available, run `skills-ref check path/to/skill-folder`. If it is unavailable, perform the checks above directly and state that the official validator was not run. Never claim tool-based validation that did not occur.

## 10. Repository write discipline

For this project:

- Work only in `dungnv2602/chatgpt`, branch `gpt`.
- Keep skill files within the approved `skills/` workspace.
- Fetch the exact current file before updating it and use its current blob SHA.
- Never overwrite existing content without inspecting it.
- Make sequential writes to the same path.
- Do not change `main` or unrelated files.
- After each important write, fetch the same path and check the expected content.
- Follow the task-scoped CI policy in `../github-actions/SKILL.md` when skill changes affect CI or the user requests CI diagnosis.
- Follow the repository execution efficiency workflow in `../the-worker/references/conversation-mode.md`. Batch related edits, avoid redundant tool calls, and preserve exact commit-to-check attribution.
- Do not report a commit or verification as successful unless the tool result and read-back support that statement.

## 11. Completion standard

A skill is complete only when its format is valid and its workflow is coherent. Its local dependencies must resolve. Its activation path must function. Read back and check the committed content.

A directory that contains only a Markdown file is not sufficient. Accurate metadata must make the skill discoverable. The activation path must load it at the required time. Its instructions must be executable and must not duplicate or contradict project policy.
