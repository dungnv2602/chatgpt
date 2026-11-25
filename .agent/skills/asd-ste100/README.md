# ASD-STE100 Skill

This skill applies [ASD-STE100 Simplified Technical English](https://www.asd-ste100.org/) to English text.

It helps readers and agents interpret technical text without guessing its meaning.

## Purpose

ASD-STE100 is a controlled-language standard for technical documentation. The aerospace and defense industry developed it to reduce ambiguity in aircraft maintenance instructions.

This skill applies the same discipline to agent output. Examples include tool descriptions, error messages, system prompts, and instructions between agents.

## Modes

Choose a mode before you revise text.

- **Strict:** Use for procedures, error messages, tool descriptions, inter-agent instructions, and safety text. Apply the structural and lexical rules.
- **STE-flavored:** Use for READMEs, change logs, PR descriptions, and explanatory prose. Apply the structural rules. Treat lexical rules as guidance.

Do not use this skill to rewrite creative writing, marketing copy, or persuasive text. Do not remove voice or nuance when those features are important.

## Core rules

Apply these structural rules:

- Use active voice when the actor is known and relevant.
- Put one instruction in each sentence.
- Keep instructions to 20 words or fewer.
- Keep descriptions to 25 words or fewer.
- Do not use semicolons.
- Avoid phrasal verbs when a clear single verb exists.
- Keep noun clusters to three words or fewer.
- Use explicit subjects, verbs, and articles.
- Keep each paragraph to one topic and six sentences or fewer.
- Use a vertical list for three or more steps or conditions.
- Preserve modality and uncertainty.

Use simple tense forms when they preserve the source meaning.

Apply lexical rules as guidance when the official ASD dictionary is not available. Do not claim that a word is approved without checking the official dictionary.

## Rewrite process

1. Select Strict or STE-flavored mode.
2. Read the source for meaning before you edit it.
3. Identify structural and lexical issues.
4. Rewrite each affected sentence without changing its meaning.
5. Keep longer wording when a shorter version would remove precision.
6. Report a kept phrase only when the user asks for the rule table or when the output format requires it.

Never remove a fact, condition, scope limit, number, or exception.

Never change a hedge into a fact. Never add a cause or result that the source does not state.

By default, return only the revised text. Do not add a preamble, mode announcement, violation count, or summary.

When the user asks for a diff or explanation, show a table with the rule, original text, and revised text.

## Linter

The skill includes `scripts/ste-lint.py`. It performs deterministic checks for selected structural patterns.

Do not run the linter locally. Push technical-document changes to branch `gpt` and let the existing GitHub Actions workflows run the linter and its self-test. The workflows apply the repository wrapper and configured per-file baselines.

The changed-document workflow uses GitHub Actions concurrency to cancel superseded runs. Do not add a separate run-list preflight that cancels the current run. GitHub may not list a newly started run before its first job checks the run list.

Use `--json` to interpret structured output when reviewing a workflow result. Use `--baseline N` only when you adopt an existing document with known findings. Use `--disable rule1,rule2` only when the repository wrapper or an authorized workflow requires it.

The linter does not prove that a rewrite preserves meaning. It does not verify modality or approved dictionary terms. It does not check every rule.

### List-item checks

The linter checks list markers at the start of a line. It accepts zero to three leading spaces and ASCII spaces after the marker.

It supports these unordered markers:

- `-`
- `*`
- `+`

It supports ordered markers such as `1.` and `1)`.

It checks indented continuation lines through the last meaningful line. It does not parse list syntax inside blockquotes, lazy continuation, or full nested-list semantics.

A line with four or more leading spaces is not a list marker. Inside an active item, indentation at the computed content column is continuation text.

### Fence checks

The linter follows CommonMark fence rules for blockquotes and fenced code.

A fence opens with three or more backticks or tildes. It can open inside a blockquote.

A closing fence uses the same character. Its run must be at least as long as the opening run. Only spaces or tabs can follow it.

A fence inside a blockquote closes when the quote ends.

The main pass accepts a fence at any indentation. It accepts a top-level closing fence up to three columns deeper than the opening fence.

The main pass can detect a fence on a list-marker line. The marker can have up to three leading spaces. A space or tab must follow the marker.

The main pass reads text after a closing fence. The dangling-conjunction pass also detects fences after tabs and inside empty list items.

A fence inside an empty item ends when the item ends. A fence on a marker line changes how later fences inside list items end.

### HTML checks

The linter recognizes HTML blocks that begin with a block tag, such as `<div>`. It also recognizes a complete tag on its own line when the tag does not continue a paragraph.

Inline HTML, such as `<span>` inside a text line, does not start an HTML block.

A line beginning with `>` inside an HTML block is text. It does not open a fence.

The main pass does not open fences inside HTML blocks. This rule applies at every quote depth.

The dangling-conjunction pass also tracks HTML blocks inside list items and on list-marker lines.

An HTML block ends when its blockquote ends. In a list item, a line with less indentation than the item ends that item and its HTML block.

GitHub treats these blocks as code or hidden text:

- `<pre>`
- HTML comments
- `<?` blocks
- `<!X` blocks
- CDATA blocks

When one of these blocks spans multiple lines, lines before the closing line are not item text. A list item does not start on those lines.

An open comment inside a list item hides text through `-->`. The text after `-->` joins the current item. This behavior also applies across later items.

Outside list items, the linter does not start a list item inside an HTML block.

Inside a list item, another HTML block, such as `<div>`, counts as item text with its tags.

GitHub displays the text of `<script>`, `<style>`, and `<textarea>` blocks because it escapes these tags. A list marker inside one of these blocks starts an item. A fence line there remains text.

The dangling-conjunction pass does not track HTML blocks inside blockquotes.

### Test fixtures

The file `examples/linter-edge-cases.md` contains intentionally incomplete list items.

The fixture records edge cases for the linter. Do not execute it locally. GitHub Actions runs the linter's built-in self-test. Do not use the fixture as compliant technical prose.

The skill's own rule tables and examples contain intentional violations. The skill README and `SKILL.md` therefore do not pass the linter with its default baseline. The upstream skill uses baseline 36 for its own `SKILL.md`. Read findings as examples where appropriate, not as proof of defects.

## Dictionary and certification limits

The skill does not reproduce ASD's official approved dictionary. Issue 9 restricts reproduction without written authority, except for specified eligible organizations.

This skill applies the underlying principle. It chooses plain words and uses each term consistently. It does not check every word against the official dictionary.

For certified ASD-STE100 documentation, obtain the official standard and check each term against its dictionary.

See [the writing-rule summary](references/writing-rules.md) for the rule categories and sources.

## Use in this repository

This skill is foundational. The repository loads it during explicit foundational initialization.

Use the [repository technical writing policy](references/repository-writing-policy.md) when you create or revise skill documentation or technical documentation.

Use Strict mode for operational instructions. Use STE-flavored mode for READMEs and explanatory technical prose.

Do not apply this policy to creative writing, dialogue, marketing copy, approved creative prompts, or examples that intentionally demonstrate a rule violation.

## Installation outside this repository

### Skills CLI

Run this command from your project root:

```bash
npx skills add danyuchn/asd-ste100-skill
```

The CLI installs the skill in the current project. It sends anonymous installation telemetry with the skill name and timestamp.

Set `DISABLE_TELEMETRY=1` to disable this telemetry.

Run `npx skills update` to update installed skills.

### Clone

Clone the source repository into the Claude Code skills directory:

```bash
git clone https://github.com/danyuchn/asd-ste100-skill ~/.claude/skills/asd-ste100
```

This installation makes the skill available in Claude Code projects.

## Usage

Ask the agent to simplify or clarify English text.

Examples:

```text
Disambiguate this tool description.
Rewrite this error message so an agent cannot misread it.
Apply ASD-STE100 to this instruction.
```

By default, the skill returns the rewritten text only.

Ask for a diff or explanation to see the rules that the source text violated.

## Scope

Use this skill for:

- Agent-to-agent messages.
- Tool and function descriptions.
- Error messages.
- System prompts.
- Inter-agent instructions.
- Technical text for machine or non-native readers.

Do not use it for creative writing, marketing copy, or text where voice and nuance are the main goal.

The skill improves the form of text. It does not improve weak or empty content.

## Other languages

These projects adapt the method for other languages. Their rules are not official ASD-STE100 rules.

- **Hebrew:** [g4lb/asd-ste100-hebrew-skill](https://github.com/g4lb/asd-ste100-hebrew-skill).
- **Indonesian:** [jshsinaga/asd-ste100-indonesian-skill](https://github.com/jshsinaga/asd-ste100-indonesian-skill).
- **Russian:** [erwinete/asd-ste100-ru](https://github.com/erwinete/asd-ste100-ru).

## Related tool

[Rewrite Fidelity Skill](https://github.com/meiluosi/rewrite-fidelity-skill) compares source text with a rewrite. It flags possible changes in meaning and modality. It uses pattern matching, so review every finding.

## Sources

- [ASD-STE100 official site](https://www.asd-ste100.org/)
- [ASD-STE100 official FAQ](https://www.asd-ste100.org/STE_faq.html)
- [ASD Europe — Simplified Technical English](https://www.asd-europe.org/standards-specifications/simplified-technical-english/)
- [Simplified Technical English — Wikipedia](https://en.wikipedia.org/wiki/Simplified_Technical_English)
- [TechScribe — ASD-STE100 Simplified Technical English](https://www.techscribe.co.uk/techw/asd-simplified-technical-english.htm)

## License

MIT. See [LICENSE](LICENSE).
