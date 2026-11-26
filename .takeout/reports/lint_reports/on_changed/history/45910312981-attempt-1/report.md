# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#853](https://github.com/dungnv2602/chatgpt/actions/runs/45910312981)
- **Run ID / attempt:** 45910312981 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / b5fe04bb56a6d499ebe0f2757160fe520c9210f9
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** b85adbc5028420661a3c7c69c477d64c4098d29d
- **Linter source SHA:** b5fe04bb56a6d499ebe0f2757160fe520c9210f9
- **Generated (UTC):** 2026-11-26T23:20:51.196584+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 3 |
| Files that failed | 2 |
| Files with findings | 2 |
| Total findings | 77 |
| Hard findings | 46 |
| Advisory findings | 31 |
| New findings | 76 |
| Recurring findings | 1 |
| Resolved findings | 45 |
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
- workspace/task_board.md
- workspace/draft/README.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md | FAIL | 76 | 45 | 0 | 4260 | 1.8 | 1 |
| workspace/task_board.md | FAIL | 1 | 1 | 0 | 418 | 0.2 | 1 |
| workspace/draft/README.md | PASS | 0 | 0 | 0 | 704 | 0.0 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| semicolon | 30 |
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
Ran 4 tests in 0.333s

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
Scanned 3 changed Markdown sources (343 available as link targets) and 18 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:1 · **new** · fingerprint: bcc3f5cbc1b36a79fcfd3820
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:88 · **new** · fingerprint: 5dbe85a2d279c9e37746c54f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:136 · **new** · fingerprint: 6632b8c3a3e24051ebb4fe6f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:192 · **new** · fingerprint: d80b27d8af07a4cd2dd2c3f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:401 · **new** · fingerprint: c97e767cb9843ded52e4fede
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:31:1 · **new** · fingerprint: 555b7d1b34070e0fcefba6fe
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:33:10 · **new** · fingerprint: d6b185b2e5bb512468c2157a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:46:32 · **new** · fingerprint: ed24b1a0740d9d55206dc200
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are returned
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:50:3 · **new** · fingerprint: a3aa8b746f180874d9b3c9c4
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:55:315 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:102:51 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:102:99 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:103:3 · **new** · fingerprint: a3aa8b746f180874d9b3c9c4
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:105:64 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:105:127 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:106:58 · **new** · fingerprint: 3f04a05c2e4ffc9df9aecbe0
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has validated
- **synonym-rotation** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:106:62 · **new** · fingerprint: 50fd0f89e13b2fbf3704e92e
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:106:119 · **new** · fingerprint: 8fa75e6dbb443176cb11ae03
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been replayed
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:106:123 · **new** · fingerprint: 9a037c3dfb0b87b2416b2d6c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been replayed
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:107:102 · **new** · fingerprint: 5cb4751a6d7a706b68f12c4a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were read
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:115:3 · **new** · fingerprint: a3aa8b746f180874d9b3c9c4
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:115:51 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:115:85 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:115:147 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:118:202 · **new** · fingerprint: c754123627116ff089527886
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:121:165 · **new** · fingerprint: 4a013c458f338e21fc2cb2ad
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has tested
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:122:110 · **new** · fingerprint: 210e1b3c071a67505270f98d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:129:128 · **new** · fingerprint: 079f0a3110d4ec8aa2d4cea4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are combined
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:134:173 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:139:216 · **new** · fingerprint: 2c2fa3d2f02ff411b4f673be
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:139:403 · **new** · fingerprint: d80b27d8af07a4cd2dd2c3f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:139:572 · **new** · fingerprint: c97e767cb9843ded52e4fede
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:141:146 · **new** · fingerprint: 5dbe85a2d279c9e37746c54f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:144:64 · **new** · fingerprint: 85d93bf35bb8290fcf54a490
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:144:97 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:144:159 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:144:284 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:145:218 · **new** · fingerprint: 7d8eca9780cbf3a0caf3f001
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added
- **synonym-rotation** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:146:205 · **new** · fingerprint: f32969cb9983abe468ae91b0
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:146:256 · **new** · fingerprint: 752674fcbab77386e46ebff5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived
- **synonym-rotation** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:147:49 · **new** · fingerprint: 7de773ca6e62e73114f05039
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirms
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:147:349 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:148:195 · **new** · fingerprint: ca93e4f6775c5cf5cea3ffee
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recommended
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:164:160 · **new** · fingerprint: 555b7d1b34070e0fcefba6fe
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:170:52 · **new** · fingerprint: c97e767cb9843ded52e4fede
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:170:84 · **new** · fingerprint: 5dbe85a2d279c9e37746c54f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:170:240 · **new** · fingerprint: e6bb5b60b326834b61ea7abc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:170:250 · **new** · fingerprint: 996bb414e149d2389d660cfc
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:170:269 · **new** · fingerprint: 8c15dd97dc803e7c655de541
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is represented
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:170:387 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:172:152 · **new** · fingerprint: 2cdbf09aa94c3b46ae7d0d99
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:188:157 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:188:213 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:190:22 · **new** · fingerprint: f55ef373734a566dd63dd73d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is consumed
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:191:72 · **new** · fingerprint: 2d4b741072c9fe1d5df25429
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are used
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:191:123 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:201:63 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:202:56 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:206:38 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:206:61 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:206:87 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:209:78 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:217:120 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:226:48 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:226:87 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:238:66 · **new** · fingerprint: a3ff8de2308d17a5e1829153
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:241:4 · **new** · fingerprint: 553855d05070d56a49f81ab7
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:243:91 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:248:111 · **new** · fingerprint: 528486d396f1e1c4cf4fc4df
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is claimed
- **synonym-rotation** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:253:163 · **new** · fingerprint: f1894d8d369e16bd231840cc
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repairs
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:261:68 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:269:265 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:275:276 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:284:240 · **new** · fingerprint: c754123627116ff089527886
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:289:56 · **new** · fingerprint: d6b185b2e5bb512468c2157a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved
- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:289:196 · **new** · fingerprint: 555b7d1b34070e0fcefba6fe
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

### Recurring findings

- **long-sentence** · workspace/task_board.md:21:1 · **recurring** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words

### Resolved findings

- **present-perfect** · .agent/INITIALIZATION_POLICY.md:40:53 · **resolved** · fingerprint: a68d4b2091de8244b08b0984
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been retrieved
- **passive-voice** · .agent/INITIALIZATION_POLICY.md:40:57 · **resolved** · fingerprint: cc8f76f7786acf5d8492b443
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved
- **long-sentence** · .agent/INITIALIZATION_POLICY.md:157:3 · **resolved** · fingerprint: 18db183bae30a8739132c97b
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **passive-voice** · .agent/INITIALIZATION_POLICY.md:166:154 · **resolved** · fingerprint: 0bd04eaf142f6db0f46ab9bd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were restored
- **passive-voice** · .agent/INITIALIZATION_POLICY.md:201:94 · **resolved** · fingerprint: 0d79d452758ac898f00007d1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is handled
- **long-sentence** · .agent/INITIALIZATION_POLICY.md:202:3 · **resolved** · fingerprint: 33a3f9c5452d51f7c5c89fda
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **synonym-rotation** · .agent/INITIALIZATION_POLICY.md:202:215 · **resolved** · fingerprint: 88ebd6db25291d630f2b140f
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** confirms
- **synonym-rotation** · .agent/SESSION_START.md:29:137 · **resolved** · fingerprint: 77f3c453c24559d624144da4
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** confirm
- **present-perfect** · .agent/SESSION_START.md:41:114 · **resolved** · fingerprint: 7e401b80fb2469d88b8b16c6
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been retrieved
- **passive-voice** · .agent/SESSION_START.md:41:119 · **resolved** · fingerprint: 65e01e8ee980bec2c691cd07
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved
- **synonym-rotation** · .agent/SESSION_START.md:53:31 · **resolved** · fingerprint: 0934ec0e9cbf6427170b249c
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **passive-voice** · .agent/SESSION_START.md:93:161 · **resolved** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · .agent/SESSION_START.md:94:63 · **resolved** · fingerprint: 8e21e03238dfdcddd1f2d77d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified
- **passive-voice** · .agent/SESSION_START.md:238:167 · **resolved** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **present-perfect** · .agent/SESSION_START.md:254:154 · **resolved** · fingerprint: 89880d1a1650656e6b26d226
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have passed
- **long-sentence** · .agent/SESSION_START.md:279:1 · **resolved** · fingerprint: 85322c6fe1ce661af2777338
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **synonym-rotation** · .agent/SESSION_START.md:293:146 · **resolved** · fingerprint: 7c9bb193d72e7abcbed9fe07
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validates
- **passive-voice** · .agent/skills/the-worker/SKILL.md:37:84 · **resolved** · fingerprint: c154d25ce626bcc916fa24de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is governed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:50:16 · **resolved** · fingerprint: 680438813b21edc564ef265e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:61:137 · **resolved** · fingerprint: 952a5f851897b7d21a178421
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirm
- **passive-voice** · .agent/skills/the-worker/SKILL.md:65:103 · **resolved** · fingerprint: 680438813b21edc564ef265e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **passive-voice** · .agent/skills/the-worker/SKILL.md:75:15 · **resolved** · fingerprint: c154d25ce626bcc916fa24de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is governed
- **passive-voice** · .agent/skills/the-worker/SKILL.md:294:144 · **resolved** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized
- **long-sentence** · .agent/skills/the-worker/SKILL.md:296:124 · **resolved** · fingerprint: d12eb5aac33ab414d203a6d5
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:299:3 · **resolved** · fingerprint: bca5f43ed3545a47de04d134
  - **Level:** advisory-free
  - **Message:** Sentence has 44 words (cap 25). Split it.
  - **Matched text:** 44 words
- **long-sentence** · .agent/skills/the-worker/SKILL.md:382:361 · **resolved** · fingerprint: ca1db01f7b11a29a176a2e86
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **long-sentence** · .agent/skills/the-worker/references/conversation-mode.md:68:60 · **resolved** · fingerprint: d6fb83cbafb61644c729d606
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · .agent/skills/the-worker/references/conversation-mode.md:68:162 · **resolved** · fingerprint: 7b11bbeb7d4a010ad6e77377
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:84:157 · **resolved** · fingerprint: 50194bcb1c09593a6b8df74f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are ordered
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:96:72 · **resolved** · fingerprint: 51c26b485146b0f7ad913711
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paused
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:101:41 · **resolved** · fingerprint: 01c59b00a54bee35fe1936cf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unresolved
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:129:88 · **resolved** · fingerprint: 51c26b485146b0f7ad913711
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paused
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:130:78 · **resolved** · fingerprint: 13168d32e5aeb357a6f05047
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:130:108 · **resolved** · fingerprint: 2d62a35466a8134401aac697
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has proposed
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:131:61 · **resolved** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:131:272 · **resolved** · fingerprint: a49119a4bb942d7711bad4ec
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is resolved
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:146:63 · **resolved** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:151:36 · **resolved** · fingerprint: 3ca196dd83b56964e6c9c511
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was encountered
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:153:106 · **resolved** · fingerprint: 4012e882a41727aa31e45e80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was verified
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:162:180 · **resolved** · fingerprint: 8b93e6445dd13d5345069497
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:190:260 · **resolved** · fingerprint: 2deb4746f57db62d7bedde8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:206:94 · **resolved** · fingerprint: b8c8647d519418bedc546521
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved
- **present-perfect** · .agent/skills/the-worker/references/conversation-mode.md:233:126 · **resolved** · fingerprint: f70f53510f186a20aefa39a5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been given
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:233:130 · **resolved** · fingerprint: 9c5f95ce73981d93b428a229
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been given
- **passive-voice** · .agent/skills/the-worker/references/conversation-mode.md:254:75 · **resolved** · fingerprint: d3280be9a8e338d6afc3f804
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are governed

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 76
- **Hard findings:** 45
- **Baseline:** 0
- **Words:** 4260
- **Findings per 100 words:** 1.8

#### Complete diagnostics

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:1 · **new** · fingerprint: bcc3f5cbc1b36a79fcfd3820
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:88 · **new** · fingerprint: 5dbe85a2d279c9e37746c54f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:136 · **new** · fingerprint: 6632b8c3a3e24051ebb4fe6f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:192 · **new** · fingerprint: d80b27d8af07a4cd2dd2c3f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:29:401 · **new** · fingerprint: c97e767cb9843ded52e4fede
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:31:1 · **new** · fingerprint: 555b7d1b34070e0fcefba6fe
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:33:10 · **new** · fingerprint: d6b185b2e5bb512468c2157a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:46:32 · **new** · fingerprint: ed24b1a0740d9d55206dc200
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are returned

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:50:3 · **new** · fingerprint: a3aa8b746f180874d9b3c9c4
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:55:315 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:102:51 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:102:99 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:103:3 · **new** · fingerprint: a3aa8b746f180874d9b3c9c4
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:105:64 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:105:127 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:106:58 · **new** · fingerprint: 3f04a05c2e4ffc9df9aecbe0
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has validated

- **synonym-rotation** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:106:62 · **new** · fingerprint: 50fd0f89e13b2fbf3704e92e
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated

- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:106:119 · **new** · fingerprint: 8fa75e6dbb443176cb11ae03
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been replayed

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:106:123 · **new** · fingerprint: 9a037c3dfb0b87b2416b2d6c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been replayed

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:107:102 · **new** · fingerprint: 5cb4751a6d7a706b68f12c4a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were read

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:115:3 · **new** · fingerprint: a3aa8b746f180874d9b3c9c4
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:115:51 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:115:85 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:115:147 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:118:202 · **new** · fingerprint: c754123627116ff089527886
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:121:165 · **new** · fingerprint: 4a013c458f338e21fc2cb2ad
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has tested

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:122:110 · **new** · fingerprint: 210e1b3c071a67505270f98d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:129:128 · **new** · fingerprint: 079f0a3110d4ec8aa2d4cea4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are combined

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:134:173 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:139:216 · **new** · fingerprint: 2c2fa3d2f02ff411b4f673be
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:139:403 · **new** · fingerprint: d80b27d8af07a4cd2dd2c3f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:139:572 · **new** · fingerprint: c97e767cb9843ded52e4fede
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:141:146 · **new** · fingerprint: 5dbe85a2d279c9e37746c54f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:144:64 · **new** · fingerprint: 85d93bf35bb8290fcf54a490
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:144:97 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:144:159 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:144:284 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:145:218 · **new** · fingerprint: 7d8eca9780cbf3a0caf3f001
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added

- **synonym-rotation** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:146:205 · **new** · fingerprint: f32969cb9983abe468ae91b0
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:146:256 · **new** · fingerprint: 752674fcbab77386e46ebff5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived

- **synonym-rotation** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:147:49 · **new** · fingerprint: 7de773ca6e62e73114f05039
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirms

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:147:349 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:148:195 · **new** · fingerprint: ca93e4f6775c5cf5cea3ffee
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recommended

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:164:160 · **new** · fingerprint: 555b7d1b34070e0fcefba6fe
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:170:52 · **new** · fingerprint: c97e767cb9843ded52e4fede
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:170:84 · **new** · fingerprint: 5dbe85a2d279c9e37746c54f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:170:240 · **new** · fingerprint: e6bb5b60b326834b61ea7abc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:170:250 · **new** · fingerprint: 996bb414e149d2389d660cfc
  - **Level:** advisory-free
  - **Message:** Sentence has 31 words (cap 25). Split it.
  - **Matched text:** 31 words

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:170:269 · **new** · fingerprint: 8c15dd97dc803e7c655de541
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is represented

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:170:387 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:172:152 · **new** · fingerprint: 2cdbf09aa94c3b46ae7d0d99
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:188:157 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:188:213 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:190:22 · **new** · fingerprint: f55ef373734a566dd63dd73d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is consumed

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:191:72 · **new** · fingerprint: 2d4b741072c9fe1d5df25429
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are used

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:191:123 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:201:63 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:202:56 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:206:38 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:206:61 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:206:87 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:209:78 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:217:120 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:226:48 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:226:87 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:238:66 · **new** · fingerprint: a3ff8de2308d17a5e1829153
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:241:4 · **new** · fingerprint: 553855d05070d56a49f81ab7
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:243:91 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:248:111 · **new** · fingerprint: 528486d396f1e1c4cf4fc4df
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is claimed

- **synonym-rotation** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:253:163 · **new** · fingerprint: f1894d8d369e16bd231840cc
  - **Level:** advisory-free
  - **Message:** 'repair' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** repairs

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:261:68 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:269:265 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:275:276 · **new** · fingerprint: d3a49d96b2c17affd57ea894
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:284:240 · **new** · fingerprint: c754123627116ff089527886
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **present-perfect** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:289:56 · **new** · fingerprint: d6b185b2e5bb512468c2157a
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved

- **long-sentence** · workspace/draft/DRAFT-0005-task-folders-subtasks-and-ci-ledger-lifecycle.md:289:196 · **new** · fingerprint: 555b7d1b34070e0fcefba6fe
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 418
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **long-sentence** · workspace/task_board.md:21:1 · **recurring** · fingerprint: 8647e8d8e7c0939979ecdb3d
  - **Level:** advisory-free
  - **Message:** Sentence has 98 words (cap 25). Split it.
  - **Matched text:** 98 words


### workspace/draft/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 704
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
