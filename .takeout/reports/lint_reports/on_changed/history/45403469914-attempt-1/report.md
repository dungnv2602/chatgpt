# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#616](https://github.com/dungnv2602/chatgpt/actions/runs/45403469914)
- **Run ID / attempt:** 45403469914 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 74005ccb1afc79d21966112501baa39772905864
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** d66901394de689223394f990047705d42108cef0
- **Linter source SHA:** 74005ccb1afc79d21966112501baa39772905864
- **Generated (UTC):** 2026-11-24T13:27:30.895368+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 10 |
| Files that failed | 4 |
| Files with findings | 9 |
| Total findings | 104 |
| Hard findings | 52 |
| Advisory findings | 52 |
| New findings | 104 |
| Recurring findings | 0 |
| Resolved findings | 4 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/adr/README.md
- workspace/ADR_TEMPLATE.md
- skills/decision-governance/SKILL.md
- skills/document-standards/references/document-type-catalog.md
- workspace/task_board.md
- workspace/analysis/README.md
- workspace/ANALYSIS_TEMPLATE.md
- workspace/draft/README.md
- workspace/README.md
- workspace/DRAFT_TEMPLATE.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/adr/README.md | PASS | 1 | 0 | 0 | 390 | 0.3 | 0 |
| workspace/ADR_TEMPLATE.md | PASS | 2 | 0 | 0 | 275 | 0.7 | 0 |
| skills/decision-governance/SKILL.md | FAIL | 12 | 4 | 0 | 1394 | 0.9 | 1 |
| skills/document-standards/references/document-type-catalog.md | FAIL | 74 | 42 | 0 | 4581 | 1.6 | 1 |
| workspace/task_board.md | PASS | 3 | 0 | 0 | 1100 | 0.3 | 0 |
| workspace/analysis/README.md | FAIL | 1 | 1 | 0 | 272 | 0.4 | 1 |
| workspace/ANALYSIS_TEMPLATE.md | PASS | 1 | 0 | 0 | 384 | 0.3 | 0 |
| workspace/draft/README.md | PASS | 0 | 0 | 0 | 320 | 0.0 | 0 |
| workspace/README.md | FAIL | 9 | 5 | 0 | 762 | 1.2 | 1 |
| workspace/DRAFT_TEMPLATE.md | PASS | 1 | 0 | 0 | 348 | 0.3 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 48 |
| semicolon | 36 |
| long-sentence | 12 |
| present-perfect | 4 |
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
Ran 4 tests in 0.364s

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

- **passive-voice** · workspace/adr/README.md:54:38 · **new** · fingerprint: c5d87e6a30d090336e26669a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **passive-voice** · workspace/ADR_TEMPLATE.md:25:67 · **new** · fingerprint: 245ae5ff11bd1a7e1426ac61
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · workspace/ADR_TEMPLATE.md:49:57 · **new** · fingerprint: 7161ac8330313d0a21373d48
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implemented
- **synonym-rotation** · skills/decision-governance/SKILL.md:15:218 · **new** · fingerprint: 2624698c9e0a949a01e1c0be
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **passive-voice** · skills/decision-governance/SKILL.md:29:58 · **new** · fingerprint: 62ba07312f0098deae0d2084
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved
- **passive-voice** · skills/decision-governance/SKILL.md:29:82 · **new** · fingerprint: a461c9d33f692bb30c8d9e32
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **long-sentence** · skills/decision-governance/SKILL.md:102:1 · **new** · fingerprint: 67e6e60b02694f4e05350b74
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **synonym-rotation** · skills/decision-governance/SKILL.md:125:70 · **new** · fingerprint: 3d615dd307290c234941ee58
  - **Level:** advisory-free
  - **Message:** 'obtain' and 'fetch' name the same action. Pick one and use it every time.
  - **Matched text:** Obtain
- **passive-voice** · skills/decision-governance/SKILL.md:137:89 · **new** · fingerprint: a461c9d33f692bb30c8d9e32
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **passive-voice** · skills/decision-governance/SKILL.md:144:50 · **new** · fingerprint: e1b2426fdfb12ab8d8076ca7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implemented
- **long-sentence** · skills/decision-governance/SKILL.md:161:1 · **new** · fingerprint: e796326c114da8d22d0a70f2
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · skills/decision-governance/SKILL.md:173:72 · **new** · fingerprint: 3b0fa6154ecfe49591695005
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being worked
- **present-perfect** · skills/decision-governance/SKILL.md:183:22 · **new** · fingerprint: 7481ea9586cd9998cf136bf1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read
- **passive-voice** · skills/decision-governance/SKILL.md:183:26 · **new** · fingerprint: 50eae35fe6ca9a2e19bff9a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read
- **passive-voice** · skills/decision-governance/SKILL.md:184:38 · **new** · fingerprint: 58b03457b929a04127a23698
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **semicolon** · skills/document-standards/references/document-type-catalog.md:4:279 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:28:139 · **new** · fingerprint: 521a3f31bc54ec727caae5b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was found
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:33:453 · **new** · fingerprint: bcb83f45ddf38808e5512023
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being uploaded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:37:304 · **new** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **semicolon** · skills/document-standards/references/document-type-catalog.md:37:313 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:38:284 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:39:264 · **new** · fingerprint: bd13d200f2cd36d327625082
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preserved
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:48:276 · **new** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:49:207 · **new** · fingerprint: a41ef6bbf64045f943d2af47
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:51:139 · **new** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:53:358 · **new** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:55:336 · **new** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **synonym-rotation** · skills/document-standards/references/document-type-catalog.md:58:250 · **new** · fingerprint: 2822a6b08706709830f1f820
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:58:311 · **new** · fingerprint: 611e1aa7abfb794630cb37cf
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:60:651 · **new** · fingerprint: 64a21a094ac7cf2fa75992d0
  - **Level:** advisory-free
  - **Message:** Sentence has 43 words (cap 25). Split it.
  - **Matched text:** 43 words
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:61:435 · **new** · fingerprint: 4213736a472e3b847e27d1ae
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are archived
- **semicolon** · skills/document-standards/references/document-type-catalog.md:61:653 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:61:705 · **new** · fingerprint: 8e6ebb9019d53b6c90f1902c
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:62:546 · **new** · fingerprint: 199f2603ee3fb1c3abd18ce6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are skipped
- **semicolon** · skills/document-standards/references/document-type-catalog.md:62:568 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:70:165 · **new** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:70:176 · **new** · fingerprint: ea92de1fbbfc0e6cafa24f7b
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:75:257 · **new** · fingerprint: 6192a6cd4c83102388153572
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **semicolon** · skills/document-standards/references/document-type-catalog.md:75:306 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:75:363 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:75:509 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:77:117 · **new** · fingerprint: 6192a6cd4c83102388153572
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **semicolon** · skills/document-standards/references/document-type-catalog.md:77:219 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:77:316 · **new** · fingerprint: 4b99bc607f23d422ec3ca66d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are limited
- **semicolon** · skills/document-standards/references/document-type-catalog.md:81:233 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:82:198 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:83:257 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:85:265 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:86:184 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:87:188 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:91:101 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:92:131 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:93:135 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:95:180 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:96:231 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · skills/document-standards/references/document-type-catalog.md:96:268 · **new** · fingerprint: 028b84870f82ee2f98dcbf3b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has run
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:98:169 · **new** · fingerprint: bb8de6bc648079b20917fbff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are catalogued
- **semicolon** · skills/document-standards/references/document-type-catalog.md:107:207 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:108:215 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:109:227 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:109:263 · **new** · fingerprint: 305641bf283ed85e29efe674
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is published
- **semicolon** · skills/document-standards/references/document-type-catalog.md:110:227 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:111:267 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:113:242 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:114:223 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:119:223 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:121:188 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:121:251 · **new** · fingerprint: 195a2fd68103c17c8542eb26
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are covered
- **semicolon** · skills/document-standards/references/document-type-catalog.md:124:117 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:126:140 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:156:39 · **new** · fingerprint: 0c06b4bea825bbb8305e2205
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were reviewed
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:161:200 · **new** · fingerprint: ea92de1fbbfc0e6cafa24f7b
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **present-perfect** · skills/document-standards/references/document-type-catalog.md:161:479 · **new** · fingerprint: 5bfc1af36a470f1f001188ee
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been approved
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:161:483 · **new** · fingerprint: c8520603dffa16dea8ea3dc4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been approved
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:162:136 · **new** · fingerprint: 6046357fc6d15e771a97e487
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are established
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:164:131 · **new** · fingerprint: f99656c38dfabd9bba499a0e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:164:206 · **new** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:165:199 · **new** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:167:262 · **new** · fingerprint: 95aef61741aad14590481dc3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is uploaded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:177:230 · **new** · fingerprint: 446871a6fecc2890373b2df1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:185:129 · **new** · fingerprint: 521a3f31bc54ec727caae5b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was found
- **semicolon** · skills/document-standards/references/document-type-catalog.md:196:185 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:197:138 · **new** · fingerprint: d8738c991b456b6b6a7cdd80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reconstructed
- **semicolon** · skills/document-standards/references/document-type-catalog.md:197:174 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:200:203 · **new** · fingerprint: 32702bd5a2c5ca60292eca3a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are superseded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:209:57 · **new** · fingerprint: 9a67866b9f0335cac5eb0d64
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was required
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:213:189 · **new** · fingerprint: 7e6ec02ac376dc4e638ffc6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was warranted
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:221:32 · **new** · fingerprint: d5a3d56f7803c8bd7fe2f5bb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added
- **semicolon** · skills/document-standards/references/document-type-catalog.md:229:203 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/task_board.md:7:110 · **new** · fingerprint: cfe2615d32498b8cb18022ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **passive-voice** · workspace/task_board.md:7:137 · **new** · fingerprint: e6baee8e949dc0ee0a1c0b34
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded
- **passive-voice** · workspace/task_board.md:7:162 · **new** · fingerprint: 86cd35c95eb6d5488c436e85
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved
- **long-sentence** · workspace/analysis/README.md:29:1 · **new** · fingerprint: ede7c80d580fbd07ebbe04bd
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **passive-voice** · workspace/ANALYSIS_TEMPLATE.md:53:50 · **new** · fingerprint: 6065ee744d87e9ee28f540f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **semicolon** · workspace/README.md:36:113 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/README.md:40:4 · **new** · fingerprint: 850ad36627f5885d916de296
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **passive-voice** · workspace/README.md:40:64 · **new** · fingerprint: f9374751a535ad58835e814f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **passive-voice** · workspace/README.md:40:110 · **new** · fingerprint: 28231427e3d00c582576f2b4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is updated
- **passive-voice** · workspace/README.md:40:140 · **new** · fingerprint: 6e067aa5c3c536cd323a5c6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is removed
- **passive-voice** · workspace/README.md:52:108 · **new** · fingerprint: 4a500644b11ea45e7a256ac0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **synonym-rotation** · workspace/README.md:52:364 · **new** · fingerprint: 01eb48b1e6acd03619987cff
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete
- **long-sentence** · workspace/README.md:56:139 · **new** · fingerprint: a222143dea70fba6ab12863a
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · workspace/README.md:56:223 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · workspace/DRAFT_TEMPLATE.md:43:106 · **new** · fingerprint: 19ad35858d820c065c7de6e1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has mixed

### Recurring findings

None.

### Resolved findings

- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:34:64 · **resolved** · fingerprint: fbe6150d9b5e8dab3b1e43a3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:47:41 · **resolved** · fingerprint: 8d3ad3a1e3838d879ee9b85a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was made
- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:111:44 · **resolved** · fingerprint: e871aaaf906a610ac0db5605
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are implemented
- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:160:67 · **resolved** · fingerprint: 2eafa78f211213b12b14d4d5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/adr/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 390
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · workspace/adr/README.md:54:38 · **new** · fingerprint: c5d87e6a30d090336e26669a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done


### workspace/ADR_TEMPLATE.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 2
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 275
- **Findings per 100 words:** 0.7

#### Complete diagnostics

- **passive-voice** · workspace/ADR_TEMPLATE.md:25:67 · **new** · fingerprint: 245ae5ff11bd1a7e1426ac61
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **passive-voice** · workspace/ADR_TEMPLATE.md:49:57 · **new** · fingerprint: 7161ac8330313d0a21373d48
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implemented


### skills/decision-governance/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 12
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 1394
- **Findings per 100 words:** 0.9

#### Complete diagnostics

- **synonym-rotation** · skills/decision-governance/SKILL.md:15:218 · **new** · fingerprint: 2624698c9e0a949a01e1c0be
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks

- **passive-voice** · skills/decision-governance/SKILL.md:29:58 · **new** · fingerprint: 62ba07312f0098deae0d2084
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved

- **passive-voice** · skills/decision-governance/SKILL.md:29:82 · **new** · fingerprint: a461c9d33f692bb30c8d9e32
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **long-sentence** · skills/decision-governance/SKILL.md:102:1 · **new** · fingerprint: 67e6e60b02694f4e05350b74
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **synonym-rotation** · skills/decision-governance/SKILL.md:125:70 · **new** · fingerprint: 3d615dd307290c234941ee58
  - **Level:** advisory-free
  - **Message:** 'obtain' and 'fetch' name the same action. Pick one and use it every time.
  - **Matched text:** Obtain

- **passive-voice** · skills/decision-governance/SKILL.md:137:89 · **new** · fingerprint: a461c9d33f692bb30c8d9e32
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **passive-voice** · skills/decision-governance/SKILL.md:144:50 · **new** · fingerprint: e1b2426fdfb12ab8d8076ca7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implemented

- **long-sentence** · skills/decision-governance/SKILL.md:161:1 · **new** · fingerprint: e796326c114da8d22d0a70f2
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **passive-voice** · skills/decision-governance/SKILL.md:173:72 · **new** · fingerprint: 3b0fa6154ecfe49591695005
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being worked

- **present-perfect** · skills/decision-governance/SKILL.md:183:22 · **new** · fingerprint: 7481ea9586cd9998cf136bf1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read

- **passive-voice** · skills/decision-governance/SKILL.md:183:26 · **new** · fingerprint: 50eae35fe6ca9a2e19bff9a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read

- **passive-voice** · skills/decision-governance/SKILL.md:184:38 · **new** · fingerprint: 58b03457b929a04127a23698
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded


### skills/document-standards/references/document-type-catalog.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 74
- **Hard findings:** 42
- **Baseline:** 0
- **Words:** 4581
- **Findings per 100 words:** 1.6

#### Complete diagnostics

- **semicolon** · skills/document-standards/references/document-type-catalog.md:4:279 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:28:139 · **new** · fingerprint: 521a3f31bc54ec727caae5b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was found

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:33:453 · **new** · fingerprint: bcb83f45ddf38808e5512023
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being uploaded

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:37:304 · **new** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **semicolon** · skills/document-standards/references/document-type-catalog.md:37:313 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:38:284 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:39:264 · **new** · fingerprint: bd13d200f2cd36d327625082
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preserved

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:48:276 · **new** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:49:207 · **new** · fingerprint: a41ef6bbf64045f943d2af47
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:51:139 · **new** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:53:358 · **new** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:55:336 · **new** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **synonym-rotation** · skills/document-standards/references/document-type-catalog.md:58:250 · **new** · fingerprint: 2822a6b08706709830f1f820
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks

- **long-sentence** · skills/document-standards/references/document-type-catalog.md:58:311 · **new** · fingerprint: 611e1aa7abfb794630cb37cf
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words

- **long-sentence** · skills/document-standards/references/document-type-catalog.md:60:651 · **new** · fingerprint: 64a21a094ac7cf2fa75992d0
  - **Level:** advisory-free
  - **Message:** Sentence has 43 words (cap 25). Split it.
  - **Matched text:** 43 words

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:61:435 · **new** · fingerprint: 4213736a472e3b847e27d1ae
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are archived

- **semicolon** · skills/document-standards/references/document-type-catalog.md:61:653 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · skills/document-standards/references/document-type-catalog.md:61:705 · **new** · fingerprint: 8e6ebb9019d53b6c90f1902c
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:62:546 · **new** · fingerprint: 199f2603ee3fb1c3abd18ce6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are skipped

- **semicolon** · skills/document-standards/references/document-type-catalog.md:62:568 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:70:165 · **new** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **long-sentence** · skills/document-standards/references/document-type-catalog.md:70:176 · **new** · fingerprint: ea92de1fbbfc0e6cafa24f7b
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **long-sentence** · skills/document-standards/references/document-type-catalog.md:75:257 · **new** · fingerprint: 6192a6cd4c83102388153572
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **semicolon** · skills/document-standards/references/document-type-catalog.md:75:306 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:75:363 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:75:509 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · skills/document-standards/references/document-type-catalog.md:77:117 · **new** · fingerprint: 6192a6cd4c83102388153572
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **semicolon** · skills/document-standards/references/document-type-catalog.md:77:219 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:77:316 · **new** · fingerprint: 4b99bc607f23d422ec3ca66d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are limited

- **semicolon** · skills/document-standards/references/document-type-catalog.md:81:233 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:82:198 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:83:257 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:85:265 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:86:184 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:87:188 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:91:101 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:92:131 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:93:135 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:95:180 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:96:231 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **present-perfect** · skills/document-standards/references/document-type-catalog.md:96:268 · **new** · fingerprint: 028b84870f82ee2f98dcbf3b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has run

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:98:169 · **new** · fingerprint: bb8de6bc648079b20917fbff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are catalogued

- **semicolon** · skills/document-standards/references/document-type-catalog.md:107:207 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:108:215 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:109:227 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:109:263 · **new** · fingerprint: 305641bf283ed85e29efe674
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is published

- **semicolon** · skills/document-standards/references/document-type-catalog.md:110:227 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:111:267 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:113:242 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:114:223 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:119:223 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:121:188 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:121:251 · **new** · fingerprint: 195a2fd68103c17c8542eb26
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are covered

- **semicolon** · skills/document-standards/references/document-type-catalog.md:124:117 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/document-standards/references/document-type-catalog.md:126:140 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:156:39 · **new** · fingerprint: 0c06b4bea825bbb8305e2205
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were reviewed

- **long-sentence** · skills/document-standards/references/document-type-catalog.md:161:200 · **new** · fingerprint: ea92de1fbbfc0e6cafa24f7b
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **present-perfect** · skills/document-standards/references/document-type-catalog.md:161:479 · **new** · fingerprint: 5bfc1af36a470f1f001188ee
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been approved

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:161:483 · **new** · fingerprint: c8520603dffa16dea8ea3dc4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been approved

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:162:136 · **new** · fingerprint: 6046357fc6d15e771a97e487
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are established

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:164:131 · **new** · fingerprint: f99656c38dfabd9bba499a0e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:164:206 · **new** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:165:199 · **new** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:167:262 · **new** · fingerprint: 95aef61741aad14590481dc3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is uploaded

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:177:230 · **new** · fingerprint: 446871a6fecc2890373b2df1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:185:129 · **new** · fingerprint: 521a3f31bc54ec727caae5b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was found

- **semicolon** · skills/document-standards/references/document-type-catalog.md:196:185 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:197:138 · **new** · fingerprint: d8738c991b456b6b6a7cdd80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reconstructed

- **semicolon** · skills/document-standards/references/document-type-catalog.md:197:174 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:200:203 · **new** · fingerprint: 32702bd5a2c5ca60292eca3a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are superseded

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:209:57 · **new** · fingerprint: 9a67866b9f0335cac5eb0d64
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was required

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:213:189 · **new** · fingerprint: 7e6ec02ac376dc4e638ffc6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was warranted

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:221:32 · **new** · fingerprint: d5a3d56f7803c8bd7fe2f5bb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added

- **semicolon** · skills/document-standards/references/document-type-catalog.md:229:203 · **new** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### workspace/task_board.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 3
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 1100
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · workspace/task_board.md:7:110 · **new** · fingerprint: cfe2615d32498b8cb18022ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed

- **passive-voice** · workspace/task_board.md:7:137 · **new** · fingerprint: e6baee8e949dc0ee0a1c0b34
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded

- **passive-voice** · workspace/task_board.md:7:162 · **new** · fingerprint: 86cd35c95eb6d5488c436e85
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved


### workspace/analysis/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 272
- **Findings per 100 words:** 0.4

#### Complete diagnostics

- **long-sentence** · workspace/analysis/README.md:29:1 · **new** · fingerprint: ede7c80d580fbd07ebbe04bd
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words


### workspace/ANALYSIS_TEMPLATE.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 384
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · workspace/ANALYSIS_TEMPLATE.md:53:50 · **new** · fingerprint: 6065ee744d87e9ee28f540f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified


### workspace/draft/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 320
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 9
- **Hard findings:** 5
- **Baseline:** 0
- **Words:** 762
- **Findings per 100 words:** 1.2

#### Complete diagnostics

- **semicolon** · workspace/README.md:36:113 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · workspace/README.md:40:4 · **new** · fingerprint: 850ad36627f5885d916de296
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words

- **passive-voice** · workspace/README.md:40:64 · **new** · fingerprint: f9374751a535ad58835e814f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created

- **passive-voice** · workspace/README.md:40:110 · **new** · fingerprint: 28231427e3d00c582576f2b4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is updated

- **passive-voice** · workspace/README.md:40:140 · **new** · fingerprint: 6e067aa5c3c536cd323a5c6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is removed

- **passive-voice** · workspace/README.md:52:108 · **new** · fingerprint: 4a500644b11ea45e7a256ac0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived

- **synonym-rotation** · workspace/README.md:52:364 · **new** · fingerprint: 01eb48b1e6acd03619987cff
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete

- **long-sentence** · workspace/README.md:56:139 · **new** · fingerprint: a222143dea70fba6ab12863a
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · workspace/README.md:56:223 · **new** · fingerprint: 99ddd247f24032b76e53f957
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### workspace/DRAFT_TEMPLATE.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 348
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **present-perfect** · workspace/DRAFT_TEMPLATE.md:43:106 · **new** · fingerprint: 19ad35858d820c065c7de6e1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has mixed

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
