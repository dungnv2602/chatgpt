# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#915](https://github.com/dungnv2602/chatgpt/actions/runs/45957997543)
- **Run ID / attempt:** 45957997543 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 62d27d93857812c7340ad3afce23ba435af0cf55
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** cf40560361853df9a6b2550e72e55d236a1aace9
- **Linter source SHA:** 62d27d93857812c7340ad3afce23ba435af0cf55
- **Generated (UTC):** 2026-11-27T07:23:28.635629+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 2 |
| Files that failed | 2 |
| Files with findings | 2 |
| Total findings | 13 |
| Hard findings | 9 |
| Advisory findings | 4 |
| New findings | 2 |
| Recurring findings | 11 |
| Resolved findings | 21 |
| Failed workflow checks | 1 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/skills/the-worker/SKILL.md
- .agent/skills/ci-ledger/SKILL.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/the-worker/SKILL.md | FAIL | 8 | 4 | 0 | 5186 | 0.2 | 1 |
| .agent/skills/ci-ledger/SKILL.md | FAIL | 5 | 5 | 0 | 2255 | 0.2 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| synonym-rotation | 5 |
| passive-voice | 4 |
| semicolon | 3 |
| long-sentence | 1 |

## 6. Workflow and validation checks

Each check includes its observed result, exit code, and complete captured output. A skipped check is not a pass.

### Wrapper shell syntax

- **Result:** Passed
- **Exit code:** 0

~~~text
No output captured.
~~~

### Python report tooling compilation

- **Result:** Passed
- **Exit code:** 0

~~~text
No output captured.
~~~

### Lint report regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
....
----------------------------------------------------------------------
Ran 4 tests in 0.336s

OK
~~~

### Markdown anchor regression tests

- **Result:** Failed
- **Exit code:** 1

~~~~~~~~~~~~~~~~~~~~~~~text
..F.....
======================================================================
FAIL: test_incremental_scope_rejects_inactive_or_untracked_sources (__main__.MarkdownAnchorTests.test_incremental_scope_rejects_inactive_or_untracked_sources) (path='.archive/adr/old.md')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/work/chatgpt/chatgpt/.agent/skills/asd-ste100/scripts/test_check_markdown_anchors.py", line 80, in test_incremental_scope_rejects_inactive_or_untracked_sources
    with self.assertRaisesRegex(ValueError, "inactive or untracked"):
         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: ValueError not raised

----------------------------------------------------------------------
Ran 8 tests in 0.143s

FAILED (failures=1)
~~~~~~~~~~~~~~~~~~~~~~~

### STE linter self-test

- **Result:** Passed
- **Exit code:** 0

~~~text
selftest OK
~~~

### Markdown links and heading anchors

- **Result:** Passed
- **Exit code:** 0

~~~text
Scanned 2 changed Markdown sources (365 available as link targets) and 7 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:401:33 · **new** · fingerprint: 952a5f851897b7d21a178421
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirm
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:44:118 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

### Recurring findings

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:135:79 · **recurring** · fingerprint: 1ead56a935297678d525088d
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **passive-voice** · .agent/skills/the-worker/SKILL.md:142:40 · **recurring** · fingerprint: 58a47654e8fe2ff210753ac7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **semicolon** · .agent/skills/the-worker/SKILL.md:143:136 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:229:91 · **recurring** · fingerprint: 448e62e062b885437ed3015e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **passive-voice** · .agent/skills/the-worker/SKILL.md:277:144 · **recurring** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized
- **passive-voice** · .agent/skills/the-worker/SKILL.md:369:196 · **recurring** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **semicolon** · .agent/skills/the-worker/SKILL.md:405:317 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:67:5 · **recurring** · fingerprint: ca9ad71bde9bdef6b1180213
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changed
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:121:24 · **recurring** · fingerprint: b15b11ac85d2fcdf68c941a9
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** removes
- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:139:61 · **recurring** · fingerprint: 6f358d459967131650a4170d
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:150:36 · **recurring** · fingerprint: 489f962a46e94a58519c7e2a
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

### Resolved findings

- **passive-voice** · .agent/skills/github-actions/SKILL.md:47:209 · **resolved** · fingerprint: de2e6ff859150e25d2ddbdf7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/github-actions/SKILL.md:47:236 · **resolved** · fingerprint: 67be1862f0bcd76c81a66643
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read
- **passive-voice** · .agent/skills/github-actions/SKILL.md:47:284 · **resolved** · fingerprint: ebe73caf7cb37aa94e730288
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **long-sentence** · .agent/skills/github-actions/SKILL.md:55:1 · **resolved** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · .agent/skills/github-actions/SKILL.md:63:351 · **resolved** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/github-actions/SKILL.md:71:3 · **resolved** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:395:513 · **resolved** · fingerprint: 6e2f9b805be9c08510010f85
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:397:717 · **resolved** · fingerprint: 9cca8e1414feae74d470296b
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirms
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:145:143 · **resolved** · fingerprint: 42f86e8fba1534a97a0dd2a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are completed
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:145:228 · **resolved** · fingerprint: de21f21791e1cf986fde4201
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are accepted
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:213:89 · **resolved** · fingerprint: ac368e93f103960466ae58d7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:213:179 · **resolved** · fingerprint: ac368e93f103960466ae58d7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **synonym-rotation** · .agent/skills/document-standards/references/document-type-catalog.md:213:206 · **resolved** · fingerprint: 4fc10f3be849a3fb43a60d2a
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **passive-voice** · workspace/task_board.md:5:556 · **resolved** · fingerprint: 091688e97ff44b87f3a1d264
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **synonym-rotation** · workspace/TASK_TEMPLATE.md:24:136 · **resolved** · fingerprint: 3a0997aa00ae589847e48a35
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **passive-voice** · workspace/TASK_TEMPLATE.md:52:32 · **resolved** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **passive-voice** · workspace/TASK_TEMPLATE.md:78:20 · **resolved** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **passive-voice** · workspace/TASK_TEMPLATE.md:79:23 · **resolved** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **semicolon** · workspace/TASK_TEMPLATE.md:95:110 · **resolved** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/TASK_TEMPLATE.md:95:247 · **resolved** · fingerprint: f89fcc99c66cd06012ce7d5a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted
- **synonym-rotation** · workspace/README.md:46:200 · **resolved** · fingerprint: d8d5bdd914126f90076410ea
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 8
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 5186
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:135:79 · **recurring** · fingerprint: 1ead56a935297678d525088d
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove

- **passive-voice** · .agent/skills/the-worker/SKILL.md:142:40 · **recurring** · fingerprint: 58a47654e8fe2ff210753ac7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted

- **semicolon** · .agent/skills/the-worker/SKILL.md:143:136 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:229:91 · **recurring** · fingerprint: 448e62e062b885437ed3015e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted

- **passive-voice** · .agent/skills/the-worker/SKILL.md:277:144 · **recurring** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized

- **passive-voice** · .agent/skills/the-worker/SKILL.md:369:196 · **recurring** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:401:33 · **new** · fingerprint: 952a5f851897b7d21a178421
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirm

- **semicolon** · .agent/skills/the-worker/SKILL.md:405:317 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### .agent/skills/ci-ledger/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 5
- **Hard findings:** 5
- **Baseline:** 0
- **Words:** 2255
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:44:118 · **new** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:67:5 · **recurring** · fingerprint: ca9ad71bde9bdef6b1180213
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changed

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:121:24 · **recurring** · fingerprint: b15b11ac85d2fcdf68c941a9
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** removes

- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:139:61 · **recurring** · fingerprint: 6f358d459967131650a4170d
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:150:36 · **recurring** · fingerprint: 489f962a46e94a58519c7e2a
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
