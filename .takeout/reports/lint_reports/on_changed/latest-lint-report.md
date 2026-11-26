# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#840](https://github.com/dungnv2602/chatgpt/actions/runs/45904670122)
- **Run ID / attempt:** 45904670122 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 4ed128e01cfd36a97ccb1a8541abd10124879893
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 7b94e6e2759540fd70a6c92496fd44e3251b0d07
- **Linter source SHA:** 4ed128e01cfd36a97ccb1a8541abd10124879893
- **Generated (UTC):** 2026-11-26T22:27:57.020756+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 3 |
| Files that failed | 2 |
| Files with findings | 3 |
| Total findings | 29 |
| Hard findings | 15 |
| Advisory findings | 14 |
| New findings | 13 |
| Recurring findings | 16 |
| Resolved findings | 5 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/INITIALIZATION_POLICY.md
- .agent/skills/github-actions/SKILL.md
- .agent/SESSION_START.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/INITIALIZATION_POLICY.md | PASS | 4 | 1 | 4 | 1655 | 0.2 | 0 |
| .agent/skills/github-actions/SKILL.md | FAIL | 16 | 11 | 0 | 3165 | 0.5 | 1 |
| .agent/SESSION_START.md | FAIL | 9 | 3 | 0 | 2812 | 0.3 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 10 |
| synonym-rotation | 8 |
| long-sentence | 5 |
| present-perfect | 4 |
| semicolon | 2 |

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
Ran 4 tests in 0.341s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

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
Scanned 3 changed Markdown sources (336 available as link targets) and 1 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **present-perfect** · .agent/INITIALIZATION_POLICY.md:38:53 · **new** · fingerprint: a68d4b2091de8244b08b0984
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been retrieved
- **passive-voice** · .agent/INITIALIZATION_POLICY.md:38:57 · **new** · fingerprint: cc8f76f7786acf5d8492b443
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved
- **long-sentence** · .agent/INITIALIZATION_POLICY.md:151:3 · **new** · fingerprint: 18db183bae30a8739132c97b
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **passive-voice** · .agent/INITIALIZATION_POLICY.md:160:154 · **new** · fingerprint: 0bd04eaf142f6db0f46ab9bd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were restored
- **present-perfect** · .agent/SESSION_START.md:33:114 · **new** · fingerprint: 7e401b80fb2469d88b8b16c6
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been retrieved
- **passive-voice** · .agent/SESSION_START.md:33:119 · **new** · fingerprint: 65e01e8ee980bec2c691cd07
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved
- **synonym-rotation** · .agent/SESSION_START.md:44:31 · **new** · fingerprint: 0934ec0e9cbf6427170b249c
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **passive-voice** · .agent/SESSION_START.md:84:161 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · .agent/SESSION_START.md:85:63 · **new** · fingerprint: 8e21e03238dfdcddd1f2d77d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified
- **passive-voice** · .agent/SESSION_START.md:229:167 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **present-perfect** · .agent/SESSION_START.md:245:154 · **new** · fingerprint: 89880d1a1650656e6b26d226
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have passed
- **long-sentence** · .agent/SESSION_START.md:270:1 · **new** · fingerprint: 85322c6fe1ce661af2777338
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **synonym-rotation** · .agent/SESSION_START.md:284:146 · **new** · fingerprint: 7c9bb193d72e7abcbed9fe07
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validates

### Recurring findings

- **passive-voice** · .agent/skills/github-actions/SKILL.md:21:206 · **recurring** · fingerprint: ce5c879312639d5e4a37c1f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are permitted
- **passive-voice** · .agent/skills/github-actions/SKILL.md:23:59 · **recurring** · fingerprint: 5ef6ce13baf5600a1694be8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided
- **present-perfect** · .agent/skills/github-actions/SKILL.md:33:40 · **recurring** · fingerprint: e8019ef8bf6c31ab6be19a58
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:62:156 · **recurring** · fingerprint: cffdf948bb88f727bace9878
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fix
- **passive-voice** · .agent/skills/github-actions/SKILL.md:69:39 · **recurring** · fingerprint: c6e235b6dc722173c0472c52
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **long-sentence** · .agent/skills/github-actions/SKILL.md:69:59 · **recurring** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · .agent/skills/github-actions/SKILL.md:76:1 · **recurring** · fingerprint: 4baec72a55fa29cd2e674673
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **semicolon** · .agent/skills/github-actions/SKILL.md:80:240 · **recurring** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:81:106 · **recurring** · fingerprint: 585f1dd2fc6ade752cecb1db
  - **Level:** advisory-free
  - **Message:** 'correct' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** corrected
- **long-sentence** · .agent/skills/github-actions/SKILL.md:82:63 · **recurring** · fingerprint: 069c795a0a52ebd5721e8aa1
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **semicolon** · .agent/skills/github-actions/SKILL.md:82:305 · **recurring** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:83:6 · **recurring** · fingerprint: da3efccaf70f209c43bc39f7
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:84:50 · **recurring** · fingerprint: ef1c126313fcc76c2583dac7
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm
- **passive-voice** · .agent/skills/github-actions/SKILL.md:86:105 · **recurring** · fingerprint: cd7ba366b1a6c942aa7fd8b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:86:130 · **recurring** · fingerprint: 82d53272cc36ef4ea58a00e3
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:158:42 · **recurring** · fingerprint: 7f75534bb1aa53c4310430aa
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'obtain' name the same action. Pick one and use it every time.
  - **Matched text:** fetch

### Resolved findings

- **passive-voice** · .agent/skills/the-worker/SKILL.md:37:84 · **resolved** · fingerprint: c154d25ce626bcc916fa24de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is governed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:260:144 · **resolved** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized
- **long-sentence** · .agent/skills/the-worker/SKILL.md:262:124 · **resolved** · fingerprint: d12eb5aac33ab414d203a6d5
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:265:3 · **resolved** · fingerprint: bca5f43ed3545a47de04d134
  - **Level:** advisory-free
  - **Message:** Sentence has 44 words (cap 25). Split it.
  - **Matched text:** 44 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:348:361 · **resolved** · fingerprint: ca1db01f7b11a29a176a2e86
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/INITIALIZATION_POLICY.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 4
- **Hard findings:** 1
- **Baseline:** 4
- **Words:** 1655
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **present-perfect** · .agent/INITIALIZATION_POLICY.md:38:53 · **new** · fingerprint: a68d4b2091de8244b08b0984
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been retrieved

- **passive-voice** · .agent/INITIALIZATION_POLICY.md:38:57 · **new** · fingerprint: cc8f76f7786acf5d8492b443
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved

- **long-sentence** · .agent/INITIALIZATION_POLICY.md:151:3 · **new** · fingerprint: 18db183bae30a8739132c97b
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **passive-voice** · .agent/INITIALIZATION_POLICY.md:160:154 · **new** · fingerprint: 0bd04eaf142f6db0f46ab9bd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were restored


### .agent/skills/github-actions/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 16
- **Hard findings:** 11
- **Baseline:** 0
- **Words:** 3165
- **Findings per 100 words:** 0.5

#### Complete diagnostics

- **passive-voice** · .agent/skills/github-actions/SKILL.md:21:206 · **recurring** · fingerprint: ce5c879312639d5e4a37c1f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are permitted

- **passive-voice** · .agent/skills/github-actions/SKILL.md:23:59 · **recurring** · fingerprint: 5ef6ce13baf5600a1694be8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided

- **present-perfect** · .agent/skills/github-actions/SKILL.md:33:40 · **recurring** · fingerprint: e8019ef8bf6c31ab6be19a58
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:62:156 · **recurring** · fingerprint: cffdf948bb88f727bace9878
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fix

- **passive-voice** · .agent/skills/github-actions/SKILL.md:69:39 · **recurring** · fingerprint: c6e235b6dc722173c0472c52
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed

- **long-sentence** · .agent/skills/github-actions/SKILL.md:69:59 · **recurring** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **long-sentence** · .agent/skills/github-actions/SKILL.md:76:1 · **recurring** · fingerprint: 4baec72a55fa29cd2e674673
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **semicolon** · .agent/skills/github-actions/SKILL.md:80:240 · **recurring** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:81:106 · **recurring** · fingerprint: 585f1dd2fc6ade752cecb1db
  - **Level:** advisory-free
  - **Message:** 'correct' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** corrected

- **long-sentence** · .agent/skills/github-actions/SKILL.md:82:63 · **recurring** · fingerprint: 069c795a0a52ebd5721e8aa1
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **semicolon** · .agent/skills/github-actions/SKILL.md:82:305 · **recurring** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:83:6 · **recurring** · fingerprint: da3efccaf70f209c43bc39f7
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:84:50 · **recurring** · fingerprint: ef1c126313fcc76c2583dac7
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm

- **passive-voice** · .agent/skills/github-actions/SKILL.md:86:105 · **recurring** · fingerprint: cd7ba366b1a6c942aa7fd8b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:86:130 · **recurring** · fingerprint: 82d53272cc36ef4ea58a00e3
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:158:42 · **recurring** · fingerprint: 7f75534bb1aa53c4310430aa
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'obtain' name the same action. Pick one and use it every time.
  - **Matched text:** fetch


### .agent/SESSION_START.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 9
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 2812
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **present-perfect** · .agent/SESSION_START.md:33:114 · **new** · fingerprint: 7e401b80fb2469d88b8b16c6
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been retrieved

- **passive-voice** · .agent/SESSION_START.md:33:119 · **new** · fingerprint: 65e01e8ee980bec2c691cd07
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved

- **synonym-rotation** · .agent/SESSION_START.md:44:31 · **new** · fingerprint: 0934ec0e9cbf6427170b249c
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check

- **passive-voice** · .agent/SESSION_START.md:84:161 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **passive-voice** · .agent/SESSION_START.md:85:63 · **new** · fingerprint: 8e21e03238dfdcddd1f2d77d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified

- **passive-voice** · .agent/SESSION_START.md:229:167 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **present-perfect** · .agent/SESSION_START.md:245:154 · **new** · fingerprint: 89880d1a1650656e6b26d226
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have passed

- **long-sentence** · .agent/SESSION_START.md:270:1 · **new** · fingerprint: 85322c6fe1ce661af2777338
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **synonym-rotation** · .agent/SESSION_START.md:284:146 · **new** · fingerprint: 7c9bb193d72e7abcbed9fe07
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validates

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
