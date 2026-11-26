# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#854](https://github.com/dungnv2602/chatgpt/actions/runs/45910457111)
- **Run ID / attempt:** 45910457111 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 870f7248b0ed52c6b453d03bd4953bc947026821
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** b5fe04bb56a6d499ebe0f2757160fe520c9210f9
- **Linter source SHA:** 870f7248b0ed52c6b453d03bd4953bc947026821
- **Generated (UTC):** 2026-11-26T23:22:19.225390+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 1 |
| Files that failed | 1 |
| Files with findings | 1 |
| Total findings | 79 |
| Hard findings | 48 |
| Advisory findings | 31 |
| New findings | 0 |
| Recurring findings | 79 |
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

- workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md | FAIL | 79 | 48 | 0 | 4463 | 1.8 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| semicolon | 32 |
| passive-voice | 26 |
| long-sentence | 12 |
| present-perfect | 5 |
| synonym-rotation | 4 |

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
Ran 4 tests in 0.289s

OK
~~~

### Markdown anchor regression tests

- **Result:** Passed
- **Exit code:** 0

~~~text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.005s

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
Scanned 1 changed Markdown sources (344 available as link targets) and 0 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

None.

### Recurring findings

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:1 · **recurring** · fingerprint: bcc3f5cbc1b36a79fcfd3820
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:88 · **recurring** · fingerprint: 5dbe85a2d279c9e37746c54f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:136 · **recurring** · fingerprint: 6632b8c3a3e24051ebb4fe6f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:192 · **recurring** · fingerprint: d80b27d8af07a4cd2dd2c3f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:401 · **recurring** · fingerprint: c97e767cb9843ded52e4fede
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:31:1 · **recurring** · fingerprint: 555b7d1b34070e0fcefba6fe
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:33:10 · **recurring** · fingerprint: d6b185b2e5bb512468c2157a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:46:32 · **recurring** · fingerprint: ed24b1a0740d9d55206dc200
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are returned
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:50:3 · **recurring** · fingerprint: a3aa8b746f180874d9b3c9c4
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:56:315 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:104:51 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:104:99 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:105:3 · **recurring** · fingerprint: a3aa8b746f180874d9b3c9c4
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:107:64 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:107:127 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:108:58 · **recurring** · fingerprint: 3f04a05c2e4ffc9df9aecbe0
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has validated
- **synonym-rotation** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:108:62 · **recurring** · fingerprint: 50fd0f89e13b2fbf3704e92e
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:108:119 · **recurring** · fingerprint: 8fa75e6dbb443176cb11ae03
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been replayed
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:108:123 · **recurring** · fingerprint: 9a037c3dfb0b87b2416b2d6c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been replayed
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:109:102 · **recurring** · fingerprint: 5cb4751a6d7a706b68f12c4a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were read
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:117:3 · **recurring** · fingerprint: a3aa8b746f180874d9b3c9c4
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:117:51 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:117:85 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:117:147 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:120:202 · **recurring** · fingerprint: c754123627116ff089527886
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:123:165 · **recurring** · fingerprint: 4a013c458f338e21fc2cb2ad
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has tested
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:124:110 · **recurring** · fingerprint: 210e1b3c071a67505270f98d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:131:128 · **recurring** · fingerprint: 079f0a3110d4ec8aa2d4cea4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are combined
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:136:173 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:141:216 · **recurring** · fingerprint: 2c2fa3d2f02ff411b4f673be
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:141:403 · **recurring** · fingerprint: d80b27d8af07a4cd2dd2c3f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:141:572 · **recurring** · fingerprint: c97e767cb9843ded52e4fede
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:141:581 · **recurring** · fingerprint: 85d93bf35bb8290fcf54a490
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:141:693 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:143:146 · **recurring** · fingerprint: 5dbe85a2d279c9e37746c54f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:146:64 · **recurring** · fingerprint: 85d93bf35bb8290fcf54a490
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:146:97 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:146:159 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:146:284 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:147:218 · **recurring** · fingerprint: 7d8eca9780cbf3a0caf3f001
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added
- **synonym-rotation** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:148:205 · **recurring** · fingerprint: f32969cb9983abe468ae91b0
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:148:256 · **recurring** · fingerprint: 752674fcbab77386e46ebff5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived
- **synonym-rotation** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:149:49 · **recurring** · fingerprint: 7de773ca6e62e73114f05039
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirms
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:149:349 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:150:195 · **recurring** · fingerprint: ca93e4f6775c5cf5cea3ffee
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recommended
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:166:160 · **recurring** · fingerprint: 555b7d1b34070e0fcefba6fe
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:172:52 · **recurring** · fingerprint: c97e767cb9843ded52e4fede
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:172:84 · **recurring** · fingerprint: 5dbe85a2d279c9e37746c54f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:172:240 · **recurring** · fingerprint: e6bb5b60b326834b61ea7abc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:172:250 · **recurring** · fingerprint: 996bb414e149d2389d660cfc
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:172:269 · **recurring** · fingerprint: 8c15dd97dc803e7c655de541
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is represented
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:172:387 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:174:152 · **recurring** · fingerprint: 2cdbf09aa94c3b46ae7d0d99
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:190:157 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:190:213 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:192:22 · **recurring** · fingerprint: f55ef373734a566dd63dd73d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is consumed
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:193:72 · **recurring** · fingerprint: 2d4b741072c9fe1d5df25429
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are used
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:193:123 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:195:206 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:204:63 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:205:56 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:209:38 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:209:61 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:209:87 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:212:78 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:220:120 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:229:48 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:229:87 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:241:66 · **recurring** · fingerprint: a3ff8de2308d17a5e1829153
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:244:4 · **recurring** · fingerprint: 553855d05070d56a49f81ab7
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:246:91 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:251:111 · **recurring** · fingerprint: 528486d396f1e1c4cf4fc4df
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is claimed
- **synonym-rotation** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:257:163 · **recurring** · fingerprint: f1894d8d369e16bd231840cc
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repairs
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:266:68 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:274:265 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:280:276 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:289:240 · **recurring** · fingerprint: c754123627116ff089527886
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:294:56 · **recurring** · fingerprint: d6b185b2e5bb512468c2157a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:294:196 · **recurring** · fingerprint: 555b7d1b34070e0fcefba6fe
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

### Resolved findings

- **long-sentence** · workspace/task_board.md:21:1 · **resolved** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 79
- **Hard findings:** 48
- **Baseline:** 0
- **Words:** 4463
- **Findings per 100 words:** 1.8

#### Complete diagnostics

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:1 · **recurring** · fingerprint: bcc3f5cbc1b36a79fcfd3820
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:88 · **recurring** · fingerprint: 5dbe85a2d279c9e37746c54f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:136 · **recurring** · fingerprint: 6632b8c3a3e24051ebb4fe6f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:192 · **recurring** · fingerprint: d80b27d8af07a4cd2dd2c3f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:401 · **recurring** · fingerprint: c97e767cb9843ded52e4fede
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:31:1 · **recurring** · fingerprint: 555b7d1b34070e0fcefba6fe
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:33:10 · **recurring** · fingerprint: d6b185b2e5bb512468c2157a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:46:32 · **recurring** · fingerprint: ed24b1a0740d9d55206dc200
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are returned

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:50:3 · **recurring** · fingerprint: a3aa8b746f180874d9b3c9c4
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:56:315 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:104:51 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:104:99 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:105:3 · **recurring** · fingerprint: a3aa8b746f180874d9b3c9c4
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:107:64 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:107:127 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:108:58 · **recurring** · fingerprint: 3f04a05c2e4ffc9df9aecbe0
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has validated

- **synonym-rotation** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:108:62 · **recurring** · fingerprint: 50fd0f89e13b2fbf3704e92e
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated

- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:108:119 · **recurring** · fingerprint: 8fa75e6dbb443176cb11ae03
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been replayed

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:108:123 · **recurring** · fingerprint: 9a037c3dfb0b87b2416b2d6c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been replayed

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:109:102 · **recurring** · fingerprint: 5cb4751a6d7a706b68f12c4a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were read

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:117:3 · **recurring** · fingerprint: a3aa8b746f180874d9b3c9c4
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:117:51 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:117:85 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:117:147 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:120:202 · **recurring** · fingerprint: c754123627116ff089527886
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:123:165 · **recurring** · fingerprint: 4a013c458f338e21fc2cb2ad
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has tested

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:124:110 · **recurring** · fingerprint: 210e1b3c071a67505270f98d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:131:128 · **recurring** · fingerprint: 079f0a3110d4ec8aa2d4cea4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are combined

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:136:173 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:141:216 · **recurring** · fingerprint: 2c2fa3d2f02ff411b4f673be
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:141:403 · **recurring** · fingerprint: d80b27d8af07a4cd2dd2c3f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:141:572 · **recurring** · fingerprint: c97e767cb9843ded52e4fede
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:141:581 · **recurring** · fingerprint: 85d93bf35bb8290fcf54a490
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:141:693 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:143:146 · **recurring** · fingerprint: 5dbe85a2d279c9e37746c54f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:146:64 · **recurring** · fingerprint: 85d93bf35bb8290fcf54a490
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:146:97 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:146:159 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:146:284 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:147:218 · **recurring** · fingerprint: 7d8eca9780cbf3a0caf3f001
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added

- **synonym-rotation** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:148:205 · **recurring** · fingerprint: f32969cb9983abe468ae91b0
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:148:256 · **recurring** · fingerprint: 752674fcbab77386e46ebff5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived

- **synonym-rotation** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:149:49 · **recurring** · fingerprint: 7de773ca6e62e73114f05039
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirms

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:149:349 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:150:195 · **recurring** · fingerprint: ca93e4f6775c5cf5cea3ffee
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recommended

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:166:160 · **recurring** · fingerprint: 555b7d1b34070e0fcefba6fe
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:172:52 · **recurring** · fingerprint: c97e767cb9843ded52e4fede
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:172:84 · **recurring** · fingerprint: 5dbe85a2d279c9e37746c54f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:172:240 · **recurring** · fingerprint: e6bb5b60b326834b61ea7abc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:172:250 · **recurring** · fingerprint: 996bb414e149d2389d660cfc
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:172:269 · **recurring** · fingerprint: 8c15dd97dc803e7c655de541
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is represented

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:172:387 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:174:152 · **recurring** · fingerprint: 2cdbf09aa94c3b46ae7d0d99
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:190:157 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:190:213 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:192:22 · **recurring** · fingerprint: f55ef373734a566dd63dd73d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is consumed

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:193:72 · **recurring** · fingerprint: 2d4b741072c9fe1d5df25429
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are used

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:193:123 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:195:206 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:204:63 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:205:56 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:209:38 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:209:61 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:209:87 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:212:78 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:220:120 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:229:48 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:229:87 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:241:66 · **recurring** · fingerprint: a3ff8de2308d17a5e1829153
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:244:4 · **recurring** · fingerprint: 553855d05070d56a49f81ab7
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:246:91 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:251:111 · **recurring** · fingerprint: 528486d396f1e1c4cf4fc4df
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is claimed

- **synonym-rotation** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:257:163 · **recurring** · fingerprint: f1894d8d369e16bd231840cc
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repairs

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:266:68 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:274:265 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:280:276 · **recurring** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:289:240 · **recurring** · fingerprint: c754123627116ff089527886
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:294:56 · **recurring** · fingerprint: d6b185b2e5bb512468c2157a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:294:196 · **recurring** · fingerprint: 555b7d1b34070e0fcefba6fe
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
