# Repository Technical Writing Policy

## Scope

This policy governs English-language skill files and technical documentation in this repository.

Use **Strict mode** for procedures, system prompts, tool descriptions, error messages, safety instructions, and inter-agent instructions.

Use **STE-flavored mode** for READMEs, change logs, technical explanations, and reference prose.

Do not apply controlled-language rules to creative writing, dialogue, marketing copy, or approved creative prompts. Do not rewrite quoted examples that intentionally show a violation.

Do not rewrite task records under `workspace/tasks/` or `archive/tasks/`. Do not rewrite `workspace/discussion.md`. These files preserve user prompts, decisions, and historical records. Exclude them from lint and active link-source scans. Keep them available as link targets.

## Writing rules

1. Write one instruction in each sentence.
2. Use active voice when the actor is known and relevant.
3. Keep instructions to 20 words or fewer.
4. Keep descriptive sentences to 25 words or fewer.
5. Use one topic in each paragraph. Use no more than six sentences per paragraph.
6. Use a numbered or bulleted list for sequences with three or more steps or conditions.
7. Do not use semicolons.
8. Avoid phrasal verbs when a clear single verb exists.
9. Avoid noun clusters with more than three words.
10. Prefer verbs over nominalizations.
11. Use simple tense forms when they preserve the original meaning.
12. Use consistent names for the same concept within each document.
13. Define necessary domain terms before relying on them.
14. Remove marketing adjectives unless a measurement supports the claim.

These rules improve clarity. They do not authorize shorter text at the cost of accuracy.

## Meaning and evidence

Preserve every fact, condition, exception, number, and scope limit in the source.

Preserve the strength of each hedge. Do not change a possibility into a fact.

Do not add a cause, mechanism, frequency, result, or recommendation that the source does not state.

Keep a longer sentence when a shorter sentence would remove necessary precision. Record the reason during a review when that trade-off matters.

Do not treat a linter result as proof that a document is accurate. A linter checks only the patterns that it supports.

## Validation

Do not run the linter locally. Push changes to branch `gpt` and let GitHub Actions validate them.

The repository has two lint workflows:

- `.github/workflows/ste-lint-changed.yml` checks changed Markdown files outside `skills/asd-ste100/`.
- `.github/workflows/ste-lint-full-docs.yml` checks the technical documentation when files in `skills/asd-ste100/` change. It also runs when either lint workflow file changes.

Both workflows use `skills/asd-ste100/scripts/ste-lint-repository.sh`. The wrapper applies the recorded mode and per-file baseline. Use `--json` to interpret structured linter output. Use `--baseline N` only when you adopt an existing document with known findings. Record the baseline and reason. Do not raise the baseline to hide new violations.

The linter does not check meaning, terminology approval, modality, or all grammar rules. Review every rewrite against the source.

The repository does not include ASD's controlled dictionary. Do not claim certified ASD-STE100 compliance. Describe the result as STE-based or STE-flavored unless you checked the official standard and dictionary.

## Maintenance

Apply this policy whenever you create or revise a skill or technical document.

Review the complete changed document. Do not limit the review to the new paragraph.

Preserve deliberate examples, code, data, and user-approved creative content. Do not change their meaning to satisfy a style check.
