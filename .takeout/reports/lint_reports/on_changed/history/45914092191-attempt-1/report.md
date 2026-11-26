# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#865](https://github.com/dungnv2602/chatgpt/actions/runs/45914092191)
- **Run ID / attempt:** 45914092191 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 4226404667c584fe1bc9cf4f0b8d81fb9e8bec18
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** d050a9807fcc65ce39953a78ae7392a8c04f5032
- **Linter source SHA:** 4226404667c584fe1bc9cf4f0b8d81fb9e8bec18
- **Generated (UTC):** 2026-11-26T23:59:59.760833+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 1 |
| Files that failed | 1 |
| Files with findings | 1 |
| Total findings | 18 |
| Hard findings | 9 |
| Advisory findings | 9 |
| New findings | 0 |
| Recurring findings | 18 |
| Resolved findings | 22 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/skills/ci-ledger/SKILL.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/ci-ledger/SKILL.md | FAIL | 18 | 9 | 0 | 1860 | 1.0 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 8 |
| semicolon | 4 |
| synonym-rotation | 3 |
| long-sentence | 2 |
| present-perfect | 1 |

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
Ran 4 tests in 0.398s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.008s

OK
~~~

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
Scanned 1 changed Markdown sources (360 available as link targets) and 0 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

None.

### Recurring findings

- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:15:1 · **recurring** · fingerprint: e33864bf535bd38a67ecac68
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:19:244 · **recurring** · fingerprint: b21e8e6015efba9bf5396408
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:31:92 · **recurring** · fingerprint: 0f6a0a839cf9723f76ad08cf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are retained
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:48:90 · **recurring** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:50:119 · **recurring** · fingerprint: c6700813c1ef8a45b5212e0b
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** change
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:60:57 · **recurring** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:102:66 · **recurring** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:103:132 · **recurring** · fingerprint: 5cf426c5bfea3e66e249b0eb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:109:156 · **recurring** · fingerprint: 75a6091a01c4060c972ae09a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:111:4 · **recurring** · fingerprint: 06781e91b8c02b9bfbcc5637
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:114:165 · **recurring** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:116:27 · **recurring** · fingerprint: b15b11ac85d2fcdf68c941a9
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** removes
- **present-perfect** · .agent/skills/ci-ledger/SKILL.md:118:91 · **recurring** · fingerprint: e9e6a23d2f10dd7ba3a83f2d
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has started
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:118:151 · **recurring** · fingerprint: c1fc8e55e266407cd9fce7f0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded
- **semicolon** · .agent/skills/ci-ledger/SKILL.md:118:162 · **recurring** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:124:20 · **recurring** · fingerprint: 4b1b6661164047c147b88a63
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is consumed
- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:134:61 · **recurring** · fingerprint: e33864bf535bd38a67ecac68
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:143:95 · **recurring** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

### Resolved findings

- **passive-voice** · .agent/skills/github-actions/SKILL.md:21:206 · **resolved** · fingerprint: ce5c879312639d5e4a37c1f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are permitted
- **passive-voice** · .agent/skills/github-actions/SKILL.md:23:59 · **resolved** · fingerprint: 5ef6ce13baf5600a1694be8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided
- **present-perfect** · .agent/skills/github-actions/SKILL.md:33:40 · **resolved** · fingerprint: e8019ef8bf6c31ab6be19a58
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:69:35 · **resolved** · fingerprint: cffdf948bb88f727bace9878
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fix
- **passive-voice** · .agent/skills/github-actions/SKILL.md:69:205 · **resolved** · fingerprint: de2e6ff859150e25d2ddbdf7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/github-actions/SKILL.md:69:254 · **resolved** · fingerprint: ebe73caf7cb37aa94e730288
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **long-sentence** · .agent/skills/github-actions/SKILL.md:77:1 · **resolved** · fingerprint: 4baec72a55fa29cd2e674673
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **semicolon** · .agent/skills/github-actions/SKILL.md:81:240 · **resolved** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:82:106 · **resolved** · fingerprint: 585f1dd2fc6ade752cecb1db
  - **Level:** advisory-free
  - **Message:** 'correct' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** corrected
- **long-sentence** · .agent/skills/github-actions/SKILL.md:83:63 · **resolved** · fingerprint: 069c795a0a52ebd5721e8aa1
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **semicolon** · .agent/skills/github-actions/SKILL.md:83:305 · **resolved** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/github-actions/SKILL.md:84:204 · **resolved** · fingerprint: 70d702d2f48b407e4ddfc138
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · .agent/skills/github-actions/SKILL.md:84:283 · **resolved** · fingerprint: ebe73caf7cb37aa94e730288
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **semicolon** · .agent/skills/github-actions/SKILL.md:84:362 · **resolved** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:85:50 · **resolved** · fingerprint: ef1c126313fcc76c2583dac7
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm
- **semicolon** · .agent/skills/github-actions/SKILL.md:85:353 · **resolved** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/github-actions/SKILL.md:87:105 · **resolved** · fingerprint: cd7ba366b1a6c942aa7fd8b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:87:130 · **resolved** · fingerprint: 82d53272cc36ef4ea58a00e3
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:159:42 · **resolved** · fingerprint: 7f75534bb1aa53c4310430aa
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'obtain' name the same action. Pick one and use it every time.
  - **Matched text:** fetch
- **semicolon** · workspace/task_board.md:3:146 · **resolved** · fingerprint: 0141c0cfbe133e92bf61057a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/task_board.md:3:159 · **resolved** · fingerprint: 2e2452378860adcb5f140771
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored
- **long-sentence** · workspace/task_board.md:22:1 · **resolved** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/ci-ledger/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 18
- **Hard findings:** 9
- **Baseline:** 0
- **Words:** 1860
- **Findings per 100 words:** 1.0

#### Complete diagnostics

- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:15:1 · **recurring** · fingerprint: e33864bf535bd38a67ecac68
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:19:244 · **recurring** · fingerprint: b21e8e6015efba9bf5396408
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:31:92 · **recurring** · fingerprint: 0f6a0a839cf9723f76ad08cf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are retained

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:48:90 · **recurring** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:50:119 · **recurring** · fingerprint: c6700813c1ef8a45b5212e0b
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** change

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:60:57 · **recurring** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:102:66 · **recurring** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:103:132 · **recurring** · fingerprint: 5cf426c5bfea3e66e249b0eb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:109:156 · **recurring** · fingerprint: 75a6091a01c4060c972ae09a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:111:4 · **recurring** · fingerprint: 06781e91b8c02b9bfbcc5637
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:114:165 · **recurring** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:116:27 · **recurring** · fingerprint: b15b11ac85d2fcdf68c941a9
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** removes

- **present-perfect** · .agent/skills/ci-ledger/SKILL.md:118:91 · **recurring** · fingerprint: e9e6a23d2f10dd7ba3a83f2d
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has started

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:118:151 · **recurring** · fingerprint: c1fc8e55e266407cd9fce7f0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded

- **semicolon** · .agent/skills/ci-ledger/SKILL.md:118:162 · **recurring** · fingerprint: 0ae22a9c140235350291bdfa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:124:20 · **recurring** · fingerprint: 4b1b6661164047c147b88a63
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is consumed

- **long-sentence** · .agent/skills/ci-ledger/SKILL.md:134:61 · **recurring** · fingerprint: e33864bf535bd38a67ecac68
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **passive-voice** · .agent/skills/ci-ledger/SKILL.md:143:95 · **recurring** · fingerprint: bbd8f7f08837e2060f7f4d03
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
