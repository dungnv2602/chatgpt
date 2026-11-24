# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#679](https://github.com/dungnv2602/chatgpt/actions/runs/45460721790)
- **Run ID / attempt:** 45460721790 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / fa59f9861823ce4d3ab11a69a8d4461339e9e47c
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** ae1ae3420409c2031ad8aa34f75121dead98b4a6
- **Linter source SHA:** fa59f9861823ce4d3ab11a69a8d4461339e9e47c
- **Generated (UTC):** 2026-11-24T18:33:55.462636+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 3 |
| Files that failed | 1 |
| Files with findings | 1 |
| Total findings | 34 |
| Hard findings | 19 |
| Advisory findings | 15 |
| New findings | 34 |
| Recurring findings | 0 |
| Resolved findings | 1 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- skills/document-standards/references/document-type-catalog.md
- workspace/task_board.md
- skills/the-worker/SKILL.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| skills/document-standards/references/document-type-catalog.md | PASS | 0 | 0 | 0 | 4396 | 0.0 | 0 |
| workspace/task_board.md | PASS | 0 | 0 | 0 | 1377 | 0.0 | 0 |
| skills/the-worker/SKILL.md | FAIL | 34 | 19 | 0 | 5264 | 0.6 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 14 |
| semicolon | 9 |
| long-sentence | 5 |
| synonym-rotation | 5 |
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
Ran 4 tests in 0.345s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
~~~

### STE linter self-test

- **Result:** Passed
- **Exit code:** 0

~~~text
selftest OK
~~~

### Markdown links and heading anchors

- **Result:** Skipped
- **Exit code:** Unknown

~~~text
Not required for this incremental run.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **long-sentence** · skills/the-worker/SKILL.md:15:1 · **new** · fingerprint: 8f5fb40f1456d6cdee279897
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **semicolon** · skills/the-worker/SKILL.md:19:127 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/the-worker/SKILL.md:23:310 · **new** · fingerprint: 8df02bfe022ca25e5787bc55
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed
- **synonym-rotation** · skills/the-worker/SKILL.md:43:62 · **new** · fingerprint: 648105621f69f0a2eab8c4ca
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repair
- **passive-voice** · skills/the-worker/SKILL.md:43:69 · **new** · fingerprint: a77a13700790965f7ca5bd58
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is authorized
- **synonym-rotation** · skills/the-worker/SKILL.md:43:142 · **new** · fingerprint: ebf7ebd75ee02f5ebcf4f9b1
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirmed
- **synonym-rotation** · skills/the-worker/SKILL.md:43:258 · **new** · fingerprint: 2c5bb767053a4621c95e8b51
  - **Level:** advisory-free
  - **Message:** 'obtain' and 'retrieve' name the same action. Pick one and use it every time.
  - **Matched text:** obtain
- **passive-voice** · skills/the-worker/SKILL.md:49:53 · **new** · fingerprint: 3003cdc6d38c0022f8be463c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **passive-voice** · skills/the-worker/SKILL.md:49:140 · **new** · fingerprint: 6bb1ff312cdf0aaf3392ffe4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is observed
- **passive-voice** · skills/the-worker/SKILL.md:76:61 · **new** · fingerprint: 0eebcb0484fe67c4e2017ecc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided
- **passive-voice** · skills/the-worker/SKILL.md:134:111 · **new** · fingerprint: d226740cae172dd2e1c78d14
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/the-worker/SKILL.md:306:46 · **new** · fingerprint: 0cad62406c2cc07deb479985
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **passive-voice** · skills/the-worker/SKILL.md:338:178 · **new** · fingerprint: 48c926404290adf5d27a8438
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is marked
- **long-sentence** · skills/the-worker/SKILL.md:338:237 · **new** · fingerprint: 2a032b53781931d6c779e34b
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **semicolon** · skills/the-worker/SKILL.md:338:362 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/the-worker/SKILL.md:341:251 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/the-worker/SKILL.md:343:108 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/the-worker/SKILL.md:344:277 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/the-worker/SKILL.md:345:140 · **new** · fingerprint: f0690d035381adacbc37a83e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **semicolon** · skills/the-worker/SKILL.md:345:200 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/the-worker/SKILL.md:345:242 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/the-worker/SKILL.md:346:54 · **new** · fingerprint: 0888728fc5c2a25c2caac0be
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · skills/the-worker/SKILL.md:347:66 · **new** · fingerprint: 3003cdc6d38c0022f8be463c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **long-sentence** · skills/the-worker/SKILL.md:347:204 · **new** · fingerprint: ead8bfcb0c1049225be6ce1d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **passive-voice** · skills/the-worker/SKILL.md:347:330 · **new** · fingerprint: 59e52367ff4fbe890c502667
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are archived
- **long-sentence** · skills/the-worker/SKILL.md:349:188 · **new** · fingerprint: 1ca5b3d7c683e38db0ecafeb
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **synonym-rotation** · skills/the-worker/SKILL.md:357:3 · **new** · fingerprint: 6d31ffa74d22866fde26008b
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **passive-voice** · skills/the-worker/SKILL.md:359:90 · **new** · fingerprint: c2eadbfa652dd24c2decf4de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being removed
- **semicolon** · skills/the-worker/SKILL.md:359:103 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/the-worker/SKILL.md:362:120 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · skills/the-worker/SKILL.md:373:168 · **new** · fingerprint: 0e07f428da579362c55d461b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been verified
- **passive-voice** · skills/the-worker/SKILL.md:373:172 · **new** · fingerprint: b6cbb5b662b7ac93ef3ba05e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified
- **long-sentence** · skills/the-worker/SKILL.md:378:4 · **new** · fingerprint: 2a032b53781931d6c779e34b
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **synonym-rotation** · skills/the-worker/SKILL.md:394:182 · **new** · fingerprint: 0564bcc241576c15bb1f3427
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

### Recurring findings

None.

### Resolved findings

- **present-perfect** · workspace/adr/README.md:65:25 · **resolved** · fingerprint: 4cf7287eb4ee4aa665924a57
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have completed

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### skills/document-standards/references/document-type-catalog.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 4396
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/task_board.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 1377
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 34
- **Hard findings:** 19
- **Baseline:** 0
- **Words:** 5264
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **long-sentence** · skills/the-worker/SKILL.md:15:1 · **new** · fingerprint: 8f5fb40f1456d6cdee279897
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **semicolon** · skills/the-worker/SKILL.md:19:127 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/the-worker/SKILL.md:23:310 · **new** · fingerprint: 8df02bfe022ca25e5787bc55
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed

- **synonym-rotation** · skills/the-worker/SKILL.md:43:62 · **new** · fingerprint: 648105621f69f0a2eab8c4ca
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repair

- **passive-voice** · skills/the-worker/SKILL.md:43:69 · **new** · fingerprint: a77a13700790965f7ca5bd58
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is authorized

- **synonym-rotation** · skills/the-worker/SKILL.md:43:142 · **new** · fingerprint: ebf7ebd75ee02f5ebcf4f9b1
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirmed

- **synonym-rotation** · skills/the-worker/SKILL.md:43:258 · **new** · fingerprint: 2c5bb767053a4621c95e8b51
  - **Level:** advisory-free
  - **Message:** 'obtain' and 'retrieve' name the same action. Pick one and use it every time.
  - **Matched text:** obtain

- **passive-voice** · skills/the-worker/SKILL.md:49:53 · **new** · fingerprint: 3003cdc6d38c0022f8be463c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed

- **passive-voice** · skills/the-worker/SKILL.md:49:140 · **new** · fingerprint: 6bb1ff312cdf0aaf3392ffe4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is observed

- **passive-voice** · skills/the-worker/SKILL.md:76:61 · **new** · fingerprint: 0eebcb0484fe67c4e2017ecc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided

- **passive-voice** · skills/the-worker/SKILL.md:134:111 · **new** · fingerprint: d226740cae172dd2e1c78d14
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · skills/the-worker/SKILL.md:306:46 · **new** · fingerprint: 0cad62406c2cc07deb479985
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done

- **passive-voice** · skills/the-worker/SKILL.md:338:178 · **new** · fingerprint: 48c926404290adf5d27a8438
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is marked

- **long-sentence** · skills/the-worker/SKILL.md:338:237 · **new** · fingerprint: 2a032b53781931d6c779e34b
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **semicolon** · skills/the-worker/SKILL.md:338:362 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/the-worker/SKILL.md:341:251 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/the-worker/SKILL.md:343:108 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/the-worker/SKILL.md:344:277 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/the-worker/SKILL.md:345:140 · **new** · fingerprint: f0690d035381adacbc37a83e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **semicolon** · skills/the-worker/SKILL.md:345:200 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/the-worker/SKILL.md:345:242 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/the-worker/SKILL.md:346:54 · **new** · fingerprint: 0888728fc5c2a25c2caac0be
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived

- **passive-voice** · skills/the-worker/SKILL.md:347:66 · **new** · fingerprint: 3003cdc6d38c0022f8be463c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed

- **long-sentence** · skills/the-worker/SKILL.md:347:204 · **new** · fingerprint: ead8bfcb0c1049225be6ce1d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **passive-voice** · skills/the-worker/SKILL.md:347:330 · **new** · fingerprint: 59e52367ff4fbe890c502667
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are archived

- **long-sentence** · skills/the-worker/SKILL.md:349:188 · **new** · fingerprint: 1ca5b3d7c683e38db0ecafeb
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **synonym-rotation** · skills/the-worker/SKILL.md:357:3 · **new** · fingerprint: 6d31ffa74d22866fde26008b
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove

- **passive-voice** · skills/the-worker/SKILL.md:359:90 · **new** · fingerprint: c2eadbfa652dd24c2decf4de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being removed

- **semicolon** · skills/the-worker/SKILL.md:359:103 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/the-worker/SKILL.md:362:120 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **present-perfect** · skills/the-worker/SKILL.md:373:168 · **new** · fingerprint: 0e07f428da579362c55d461b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been verified

- **passive-voice** · skills/the-worker/SKILL.md:373:172 · **new** · fingerprint: b6cbb5b662b7ac93ef3ba05e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified

- **long-sentence** · skills/the-worker/SKILL.md:378:4 · **new** · fingerprint: 2a032b53781931d6c779e34b
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **synonym-rotation** · skills/the-worker/SKILL.md:394:182 · **new** · fingerprint: 0564bcc241576c15bb1f3427
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
