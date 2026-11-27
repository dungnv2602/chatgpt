# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#868](https://github.com/dungnv2602/chatgpt/actions/runs/45915952464)
- **Run ID / attempt:** 45915952464 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 80670bb8b8536256419b5b2372076357da62d2ac
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 470b32f24310969cc6e0856cfc744ffc8db5e31e
- **Linter source SHA:** 80670bb8b8536256419b5b2372076357da62d2ac
- **Generated (UTC):** 2026-11-27T00:18:55.700106+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 1 |
| Files that failed | 1 |
| Files with findings | 1 |
| Total findings | 31 |
| Hard findings | 11 |
| Advisory findings | 20 |
| New findings | 0 |
| Recurring findings | 31 |
| Resolved findings | 0 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- .agent/skills/the-worker/SKILL.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| .agent/skills/the-worker/SKILL.md | FAIL | 31 | 11 | 0 | 5993 | 0.5 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 20 |
| semicolon | 5 |
| long-sentence | 4 |
| synonym-rotation | 2 |

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
Ran 4 tests in 0.340s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.036s

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
Scanned 1 changed Markdown sources (363 available as link targets) and 7 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

None.

### Recurring findings

- **passive-voice** · .agent/skills/the-worker/SKILL.md:37:84 · **recurring** · fingerprint: c154d25ce626bcc916fa24de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is governed
- **long-sentence** · .agent/skills/the-worker/SKILL.md:39:1 · **recurring** · fingerprint: 678ab67701d0d18a96087add
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:50 · **recurring** · fingerprint: 2a95aa3417dfc57540b6934b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:98 · **recurring** · fingerprint: 5136594700cf7f963a8796c4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:125 · **recurring** · fingerprint: b31436362c5e38fa10263166
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:177 · **recurring** · fingerprint: 59b99e3464ed064af8bfc971
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **semicolon** · .agent/skills/the-worker/SKILL.md:39:229 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:359 · **recurring** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · .agent/skills/the-worker/SKILL.md:50:16 · **recurring** · fingerprint: 680438813b21edc564ef265e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:61:137 · **recurring** · fingerprint: 952a5f851897b7d21a178421
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirm
- **passive-voice** · .agent/skills/the-worker/SKILL.md:65:103 · **recurring** · fingerprint: 680438813b21edc564ef265e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **passive-voice** · .agent/skills/the-worker/SKILL.md:75:15 · **recurring** · fingerprint: c154d25ce626bcc916fa24de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is governed
- **semicolon** · .agent/skills/the-worker/SKILL.md:86:70 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · .agent/skills/the-worker/SKILL.md:146:48 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:295:144 · **recurring** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized
- **long-sentence** · .agent/skills/the-worker/SKILL.md:297:124 · **recurring** · fingerprint: d12eb5aac33ab414d203a6d5
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:300:3 · **recurring** · fingerprint: bca5f43ed3545a47de04d134
  - **Level:** advisory-free
  - **Message:** Sentence has 44 words (cap 25). Split it.
  - **Matched text:** 44 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:386:96 · **recurring** · fingerprint: 5136594700cf7f963a8796c4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/the-worker/SKILL.md:386:165 · **recurring** · fingerprint: 59b99e3464ed064af8bfc971
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · .agent/skills/the-worker/SKILL.md:387:126 · **recurring** · fingerprint: 30a5f5010d39a09d4d44c82a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded
- **passive-voice** · .agent/skills/the-worker/SKILL.md:387:215 · **recurring** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · .agent/skills/the-worker/SKILL.md:388:332 · **recurring** · fingerprint: 0903f3b4306b2fc6c361a363
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived
- **semicolon** · .agent/skills/the-worker/SKILL.md:390:393 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · .agent/skills/the-worker/SKILL.md:412:1 · **recurring** · fingerprint: 12a0c65c6ffb1f23bd33659b
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:67 · **recurring** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:101 · **recurring** · fingerprint: b7a2bc4c1fde83c1a7f84a08
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:152 · **recurring** · fingerprint: f2c0edb97a4132169f97b4ea
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are indexed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:184 · **recurring** · fingerprint: 1b18d543a8c344d3fcfffc26
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reconciled
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:414:513 · **recurring** · fingerprint: 6e2f9b805be9c08510010f85
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **semicolon** · .agent/skills/the-worker/SKILL.md:420:175 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:435:200 · **recurring** · fingerprint: a67c2e85b92372da8a36a067
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is expected

### Resolved findings

None.

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 31
- **Hard findings:** 11
- **Baseline:** 0
- **Words:** 5993
- **Findings per 100 words:** 0.5

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/SKILL.md:37:84 · **recurring** · fingerprint: c154d25ce626bcc916fa24de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is governed

- **long-sentence** · .agent/skills/the-worker/SKILL.md:39:1 · **recurring** · fingerprint: 678ab67701d0d18a96087add
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:50 · **recurring** · fingerprint: 2a95aa3417dfc57540b6934b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed

- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:98 · **recurring** · fingerprint: 5136594700cf7f963a8796c4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:125 · **recurring** · fingerprint: b31436362c5e38fa10263166
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read

- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:177 · **recurring** · fingerprint: 59b99e3464ed064af8bfc971
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **semicolon** · .agent/skills/the-worker/SKILL.md:39:229 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:39:359 · **recurring** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **passive-voice** · .agent/skills/the-worker/SKILL.md:50:16 · **recurring** · fingerprint: 680438813b21edc564ef265e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:61:137 · **recurring** · fingerprint: 952a5f851897b7d21a178421
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirm

- **passive-voice** · .agent/skills/the-worker/SKILL.md:65:103 · **recurring** · fingerprint: 680438813b21edc564ef265e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked

- **passive-voice** · .agent/skills/the-worker/SKILL.md:75:15 · **recurring** · fingerprint: c154d25ce626bcc916fa24de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is governed

- **semicolon** · .agent/skills/the-worker/SKILL.md:86:70 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · .agent/skills/the-worker/SKILL.md:146:48 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:295:144 · **recurring** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized

- **long-sentence** · .agent/skills/the-worker/SKILL.md:297:124 · **recurring** · fingerprint: d12eb5aac33ab414d203a6d5
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **long-sentence** · .agent/skills/the-worker/SKILL.md:300:3 · **recurring** · fingerprint: bca5f43ed3545a47de04d134
  - **Level:** advisory-free
  - **Message:** Sentence has 44 words (cap 25). Split it.
  - **Matched text:** 44 words

- **passive-voice** · .agent/skills/the-worker/SKILL.md:386:96 · **recurring** · fingerprint: 5136594700cf7f963a8796c4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · .agent/skills/the-worker/SKILL.md:386:165 · **recurring** · fingerprint: 59b99e3464ed064af8bfc971
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **passive-voice** · .agent/skills/the-worker/SKILL.md:387:126 · **recurring** · fingerprint: 30a5f5010d39a09d4d44c82a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded

- **passive-voice** · .agent/skills/the-worker/SKILL.md:387:215 · **recurring** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **passive-voice** · .agent/skills/the-worker/SKILL.md:388:332 · **recurring** · fingerprint: 0903f3b4306b2fc6c361a363
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived

- **semicolon** · .agent/skills/the-worker/SKILL.md:390:393 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · .agent/skills/the-worker/SKILL.md:412:1 · **recurring** · fingerprint: 12a0c65c6ffb1f23bd33659b
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words

- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:67 · **recurring** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:101 · **recurring** · fingerprint: b7a2bc4c1fde83c1a7f84a08
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived

- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:152 · **recurring** · fingerprint: f2c0edb97a4132169f97b4ea
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are indexed

- **passive-voice** · .agent/skills/the-worker/SKILL.md:412:184 · **recurring** · fingerprint: 1b18d543a8c344d3fcfffc26
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reconciled

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:414:513 · **recurring** · fingerprint: 6e2f9b805be9c08510010f85
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **semicolon** · .agent/skills/the-worker/SKILL.md:420:175 · **recurring** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:435:200 · **recurring** · fingerprint: a67c2e85b92372da8a36a067
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is expected

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
