---
name: asd-ste100
description: "Use when English text needs clear wording without human clarification. Covers tool descriptions, errors, inter-agent instructions, system prompts, and status reports where misreading has a real cost. Triggers: disambiguate, STE100 rewrite, apply Simplified Technical English, plain-language rewrite, controlled-language rewrite, rewrite so an agent cannot misread this. Not for creative or marketing copy."
metadata:
  version: 0.4.0
  project-role: foundational
  format: agentskills
---

# Simplified Technical English (ASD-STE100)

ASD-STE100 is a controlled-language standard developed by the aerospace and defense industry (ASD, the AeroSpace and Defense Industries Association of Europe). It helps maintenance technicians interpret English instructions correctly. The standard addresses two major sources of misreading: words with more than one meaning and sentences with more than one possible structure.

This skill applies that discipline to a different reader: an **AI agent or a downstream system**. Such a system must parse an English string without a human to resolve ambiguity. Examples include an error message, a tool description, an inter-agent instruction, or a status report. A maintenance technician can misread "close the valve" as an adjective ("the valve that is near") instead of a command. A language model can make the same error.

## When to Use This Skill

- An agent's output (explanation, instruction, log message, tool description) reads as dense, jargon-heavy, or ambiguous.
- Text will be consumed by another agent, a translation pipeline, or a non-native English reader, and misparsing has a real cost.
- You are writing a prompt, system message, or tool description and want to remove ambiguity before a model ever sees it.
- You want a **before/after** comparison showing exactly which rule the original text violated and how the rewrite fixes it. Ask for it — the default output is the rewritten text alone (see Output Format).

This skill is not for creative or marketing copy — STE is deliberately flat and literal. Do not apply it to text where voice, nuance, or persuasion is the point.

## Two Modes

Pick a mode before rewriting. If the user does not say which, infer it from the text type. Keep the choice internal unless the user asks for the rule table (see Output Format).

**Strict** — procedures, error messages, tool and function descriptions, inter-agent instructions, safety text. Anywhere a wrong reading has a cost. Apply every rule below, including the hard length caps and one-word-one-meaning discipline.

**STE-flavored** — Use for READMEs, PR descriptions, changelogs, and explanatory prose. Apply the structural rules in full. Treat lexical rules as advisory (see Core Rewrite Rules for that split). Keep sentence-length caps, active voice, simple tenses, no phrasal verbs, no semicolons, no nominalization, and no marketing adjectives. Do not enforce the one-word-one-meaning lockdown. Prose needs some range. A strict rewrite of prose reads as a personality transplant rather than a clarification.

The two modes and the structural/lexical split are the same distinction seen from two directions. The split says which rules this skill can check without ASD's dictionary. The modes say which of them to enforce for a given kind of text.

## Source and Scope

This skill encodes the **rule categories** of ASD-STE100 Issue 9 (Jan 2025). The standard contains 53 writing rules across 9 sections. These rules cover word choice, grammar, sentence structure, and style. A dictionary supports them. It contains about 900 approved words (one meaning and one part of speech each) and about 1,200 words to avoid with suggested replacements. See `references/writing-rules.md` for the full rule summary and citations.

It does **not** reproduce ASD's ~900-word approved dictionary verbatim. ASD-STE100 is free to obtain, but not free to redistribute. Issue 9, page 2, states this restriction:

> "no reproduction or publication of it, in whole or in part, shall be made without the written authority of an officer of ASD."

It grants free reproduction rights to eight categories. These include ASD/AIA/AIAC member associations, their member companies and customers, and member-state defence ministries. They also include A4A, airworthiness authorities, and universities and research institutes for educational purposes. This project is not in any of those categories. Therefore, the dictionary stays out of this repository.

Instead, this skill applies the *underlying principle*: choose the plainest, most common word available and use it consistently. It does not check words against a fixed list. When exact ASD-approved wording matters, such as in aircraft maintenance documentation, obtain the standard and check each word against the official dictionary. Use the [official ASD-STE100 site](https://www.asd-ste100.org/) to request the current standard. The [official Issue 9 PDF](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf) is also available directly.

## Core Rewrite Rules

STE's rules divide into two kinds, and this skill can only fully deliver one of them. **Structural rules** are self-contained: they describe sentence shape, and you can apply them from the description alone. The official ~900-word dictionary defines **lexical rules**. This skill deliberately does not reproduce that dictionary (see Source and Scope). Without that dictionary, the lexical rules degrade from a checkable standard into a preference for plain words.

Apply the structural rules with confidence. Apply the lexical rules as a direction of travel, and say so in your output rather than implying dictionary compliance you cannot establish.

### Structural rules — apply these

| Rule | Do | Don't |
|---|---|---|
| Active voice | "The agent removes the file." | "A sentence that hides the actor." — unless the actor is genuinely unknown or irrelevant |
| No phrasal verbs (Rule 9.3) | "Remove the panel." / "Start the job." | "Use a verb plus a particle for the job." — a multiword verb can have a meaning the parts do not predict |
| One instruction per sentence | "Open the file. Read line 3." | "Open the file and read line 3, then check if it matches." |
| Sentence length | ≤20 words for instructions/procedures, ≤25 words for descriptions | Long compound/subordinate-clause sentences |
| No semicolons (Rule 8.1) | Split into separate sentences | Any semicolon at all — STE bans the mark outright, not only as a clause join. (Rule 8.1 permits every other standard punctuation mark. The em dash is *not* banned by STE, though it often signals a sentence that should be split.) |
| Noun clusters | ≤3 words stacked as a noun phrase ("fuel pump valve") | 4+ word noun stacks ("high pressure fuel pump inlet valve assembly") |
| No ellipsis | Keep the subject, verb, and article explicit even if it reads longer | Drop words to save space ("Files not backed up will be lost" → ambiguous which files) |
| Keep modality | "The request **may have** failed." stays "may have" | Promote a hedge to a fact ("The request failed.") or invent a certainty the source did not state |
| Paragraph limits | One topic per paragraph, ≤6 sentences | Multi-topic paragraphs |
| Lists for sequences | Use a numbered or bulleted list for 3+ steps or conditions | Bury a sequence inside one prose sentence |

### Lexical rules — direction of travel only

| Rule | Do | Don't | Why it is weaker here |
|---|---|---|---|
| One word, one meaning | Pick one verb for one action and reuse it every time (e.g. always "check", never use a different verb for the same action) | Rotate synonyms for the same idea across a document | Consistency within a document is checkable. Which word is the *approved* one is not, without the dictionary. |
| One part of speech per word | "Apply oil to the valve" (oil = noun) | "Oil the valve" (oil = verb) | Only the dictionary can confirm whether it lists "oil" as a noun. Prefer the noun form when both read equally well. Do not claim compliance. |
| Verb, not noun (Rule 3.7) | "Analyze the log." | "Perform an analysis of the log." — a noun form of an action makes the sentence longer and hides who acts | Rule 3.7 says "use an **approved** verb to describe an action." Preferring the verb form is safe to apply anywhere. Knowing which verb is the approved one needs the dictionary. |
| Domain terms | Keep necessary technical nouns/verbs, but define them once if not common English (STE allows a project-specific glossary beyond its base dictionary) | Use jargon without ever defining it | The glossary allowance is real STE, but the base dictionary it extends is absent. |

### Simple tenses — apply with one exception

STE permits infinitive, imperative, simple present, simple past, simple future, and past participle as adjective. It excludes present perfect and other compound forms: "we received the report", not "we have received the report".

Aircraft manuals do not need the present perfect, so the exclusion does not reduce the standard's value. Other text is different. "The job has completed" (and its output is available now) and "the job completed" (at some past point) express different meanings. Status text often needs the first form. Keep the compound form when it carries information the simple form cannot, such as current relevance or a hedge in "may have failed". Flag the departure. Elsewhere, follow the rule.

## Scan Checklist

These six habits cover most of what makes machine-written English hard to parse. Each one is mechanical: you can point at the exact word or punctuation mark that breaks the rule, with no judgment call. Scan for all six before you rewrite anything.

1. **Synonym rotation** — the same thing uses several names in one document ("the user", "the customer", "the client"). The reader cannot tell whether they are one thing or three. Fix: pick one name, use it every time.
2. **Hedge stacking** — helper verbs and qualifiers pile up until the sentence asserts nothing ("it is important to note that this may potentially help to improve"). Fix: state the claim, or remove it.
3. **Nominalization** — an action frozen into a noun ("perform an analysis of", "provides assistance to"). Fix: use the verb ("analyze", "helps").
4. **Marketing adjectives** — words that claim quality instead of showing it: seamless, robust, powerful, cutting-edge, effortless, blazing-fast. Fix: remove, or replace with the measurement that earns the claim.
5. **Run-on sentences** — several ideas joined by semicolons or em dashes. Fix: one idea per sentence.
6. **Soft phrasal verbs** — multiword verb forms that add a meaning beyond their component words. Fix: use one plain verb, such as start, contact, or read.

## Process

1. Pick the mode (Strict or STE-flavored). Say which only when the user asked for the rule table — see Output Format.
2. Read the input text once for meaning — do not start rewriting before you understand what it must still say afterward.
3. Walk the text sentence by sentence.
   - Flag violations from the Core Rewrite Rules and the Scan Checklist.
   - In STE-flavored mode, flag lexical rules. Do not enforce them in the rewrite.
   - The linter has no STE-flavored mode. Synonym rotation remains a hard finding.
   - Use `--disable synonym-rotation` to disable that check.
   - Do not run the linter or CI workflows locally. Push the changes to branch `gpt` and let GitHub Actions check them. Do not wait for or poll CI results.
   - Follow the task-scoped CI policy in `../the-worker/references/github-actions.md` only when the requested work changes or depends on CI.
   - The `ste-lint-changed.yml` workflow checks changed Markdown files outside `.agent/skills/asd-ste100/`. The `ste-lint-full-docs.yml` workflow checks the technical documentation when files in `.agent/skills/asd-ste100/` change.
   - The workflows call `scripts/ste-lint-repository.sh`, which runs the linter. Use stdin or file arguments and `--json` only when you need to understand the linter interface or interpret workflow output.
   - The linter checks semicolons, sentence length, phrasal verbs, nominalization, marketing adjectives, synonym rotation, supported dangling conjunctions, passive voice, and compound tenses.
   - The linter does not flag hedges or modality.
   - Use `--baseline N` to allow N hard findings when you adopt an existing document.
   - Use `--disable rule1,rule2` to disable named checks.
4. Rewrite each flagged sentence. Preserve the original meaning exactly. If a rewrite would drop necessary precision, keep the longer phrasing and flag it instead of simplifying it. Necessary precision includes a safety condition, a scope qualifier, or a number.
   - **Check modality before you commit to a rewrite.** Hedges such as "may", "could", "sometimes", and "is likely to" carry the author's confidence. Confidence is content. A shorter sentence that upgrades a hedge to a fact makes a different claim. This is a common failure in well-intentioned STE rewrites. Length caps can tempt the writer to cut hedges.
   - Never add a fact the source did not state. A rewrite that reads better because it supplies a cause, a frequency, or a mechanism has stopped being a rewrite.
5. Output the rewritten text (see Output Format). Keep the mode choice and the rule analysis internal unless the user asked to see them.
6. If the input already complies, say so — do not force changes onto compliant text.

## Output Format

**Default: the rewritten text, and nothing else.** Most callers want text they can paste into a tool description, an error string, or a prompt. Print the simplified text on its own. Do not add a preamble about this skill, a mode announcement, or a violation count. Do not add a summary of changes, a rule table, or a closing offer to explain further.

The one permitted addition applies when step 4 keeps a longer phrasing on purpose. Add one line after the text. Prefix it with `Kept as-is:`. Name the phrase and the precision that would be lost. Omit this line when there is nothing to report.

**On request: the rule table.** When the user asks to see the reasoning — "show the diff", "which rules did it break", "explain the changes", "before/after" — output this table instead:

```markdown
| Rule violated | Original | Simplified |
|---|---|---|
| Present perfect tense | "We have received your request." | "We received your request." |
| Noun cluster (4+ words) | "the agent task queue priority handler" | "the handler that sets task-queue priority" |

Mode: Strict. 7 violations found.
```

Follow the table with a one-line note on anything you deliberately did **not** simplify, and why (usually: simplifying would lose required precision).

## Boundaries

**Will:**
- Rewrite ambiguous or dense English into short, single-meaning, active-voice sentences.
- Return the rewritten text alone by default, and name the rules it applied when the user asks.
- Preserve every fact, condition, and scope qualifier in the original.
- Preserve the strength of every hedge, and add no claim the source did not make.
- Suggest a one-line glossary entry for domain terms that must stay.

**Will not:**
- Present ASD's official ~900-word dictionary as if the skill memorized it verbatim. Always treat the official download as the source of truth for exact approved wording.
- Simplify creative, marketing, or persuasive copy where voice and nuance are the point.
- Silently drop a safety condition, exception, or scope qualifier to shorten a sentence — it will flag the trade-off instead.
- Convert "may have failed" into "failed", or "could be caused by X" into "X is the cause" — losing a hedge changes the claim.
- Guarantee an aerospace/defense-grade STE-compliant document. This is a general-purpose clarity tool inspired by STE, not a certified STE authoring tool.
- Make weak content true or useful. STE fixes the *form* of a text, not its substance. A hollow paragraph rewritten under these rules becomes a clean, short, well-punctuated hollow paragraph. If the text has nothing to say, no rewrite fixes that — say so instead of polishing it.
- Do not shorten text past the point of clarity. Cutting words is not the goal. Removing ambiguity is the goal. Compression can eventually cost the reader time instead of saving it. Stop when the sentence is unambiguous, not when it is shortest.

## Additional Resources

- **`references/repository-writing-policy.md`** — repository-wide rules for skill and technical documentation. It defines Strict and STE-flavored modes.

- **`references/writing-rules.md`** — fuller summary of the 9 rule sections and dictionary structure, with citations to the official standard and secondary sources.
- **`examples/before-after.md`** — worked examples: rule illustrations, and agent-output examples built for this skill.
- **`scripts/ste-lint.py`** — deterministic, standard-library-only linter for selected structural rules. It checks supported dangling conjunctions and synonym rotation within each file. It exits with code 1 when hard findings exceed `--baseline` (default 0). Advisory findings for passive voice and compound tenses do not fail the run. Use `--disable` to silence named checks. The linter does not flag hedges or modality. Its `--selftest` shows that "may have failed" passes clean.
