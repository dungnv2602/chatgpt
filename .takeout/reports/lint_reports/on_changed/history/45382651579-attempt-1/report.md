# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#601](https://github.com/dungnv2602/chatgpt/actions/runs/45382651579)
- **Run ID / attempt:** 45382651579 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 8adc48d1be4d4d659fba028d7cea8e76ddd9c9d9
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** e4c5bbaadbd2776d4259bd937e157b3cf12e034b
- **Linter source SHA:** 8adc48d1be4d4d659fba028d7cea8e76ddd9c9d9
- **Generated (UTC):** 2026-11-24T11:17:01.188237+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 2 |
| Files that failed | 1 |
| Files with findings | 2 |
| Total findings | 31 |
| Hard findings | 17 |
| Advisory findings | 14 |
| New findings | 28 |
| Recurring findings | 3 |
| Resolved findings | 94 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/task_board.md
- skills/the-worker/SKILL.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/task_board.md | PASS | 3 | 0 | 0 | 824 | 0.4 | 0 |
| skills/the-worker/SKILL.md | FAIL | 28 | 17 | 0 | 4771 | 0.6 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 13 |
| semicolon | 9 |
| long-sentence | 5 |
| synonym-rotation | 3 |
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
Ran 4 tests in 0.356s

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
- **passive-voice** · skills/the-worker/SKILL.md:61:61 · **new** · fingerprint: 0eebcb0484fe67c4e2017ecc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided
- **passive-voice** · skills/the-worker/SKILL.md:115:111 · **new** · fingerprint: d226740cae172dd2e1c78d14
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/the-worker/SKILL.md:304:178 · **new** · fingerprint: 48c926404290adf5d27a8438
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is marked
- **long-sentence** · skills/the-worker/SKILL.md:304:237 · **new** · fingerprint: 2a032b53781931d6c779e34b
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **semicolon** · skills/the-worker/SKILL.md:304:362 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/the-worker/SKILL.md:307:251 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/the-worker/SKILL.md:309:108 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/the-worker/SKILL.md:310:277 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/the-worker/SKILL.md:311:140 · **new** · fingerprint: f0690d035381adacbc37a83e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **semicolon** · skills/the-worker/SKILL.md:311:200 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/the-worker/SKILL.md:311:242 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/the-worker/SKILL.md:312:54 · **new** · fingerprint: 0888728fc5c2a25c2caac0be
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · skills/the-worker/SKILL.md:313:66 · **new** · fingerprint: 3003cdc6d38c0022f8be463c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **long-sentence** · skills/the-worker/SKILL.md:313:204 · **new** · fingerprint: ead8bfcb0c1049225be6ce1d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **passive-voice** · skills/the-worker/SKILL.md:313:330 · **new** · fingerprint: 59e52367ff4fbe890c502667
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are archived
- **long-sentence** · skills/the-worker/SKILL.md:315:188 · **new** · fingerprint: 1ca5b3d7c683e38db0ecafeb
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **synonym-rotation** · skills/the-worker/SKILL.md:323:3 · **new** · fingerprint: 6d31ffa74d22866fde26008b
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **passive-voice** · skills/the-worker/SKILL.md:325:90 · **new** · fingerprint: c2eadbfa652dd24c2decf4de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being removed
- **semicolon** · skills/the-worker/SKILL.md:325:103 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/the-worker/SKILL.md:328:120 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · skills/the-worker/SKILL.md:339:168 · **new** · fingerprint: 0e07f428da579362c55d461b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been verified
- **passive-voice** · skills/the-worker/SKILL.md:339:172 · **new** · fingerprint: b6cbb5b662b7ac93ef3ba05e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified
- **synonym-rotation** · skills/the-worker/SKILL.md:343:102 · **new** · fingerprint: b0d48c1fdb52aa58dc1b1908
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirm
- **long-sentence** · skills/the-worker/SKILL.md:344:4 · **new** · fingerprint: 2a032b53781931d6c779e34b
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **synonym-rotation** · skills/the-worker/SKILL.md:360:182 · **new** · fingerprint: 0564bcc241576c15bb1f3427
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

### Recurring findings

- **passive-voice** · workspace/task_board.md:7:110 · **recurring** · fingerprint: cfe2615d32498b8cb18022ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed
- **passive-voice** · workspace/task_board.md:7:137 · **recurring** · fingerprint: e6baee8e949dc0ee0a1c0b34
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded
- **passive-voice** · workspace/task_board.md:7:162 · **recurring** · fingerprint: 86cd35c95eb6d5488c436e85
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved

### Resolved findings

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:36:64 · **resolved** · fingerprint: 04ec4f5fbb130c1324f44f00
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:77:41 · **resolved** · fingerprint: 5d7ba294a41810bbc4f7a8fe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was made
- **present-perfect** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:173:31 · **resolved** · fingerprint: 015ecb389e532dd8875c1837
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has presented
- **present-perfect** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:174:34 · **resolved** · fingerprint: 0f4521e8c2b440c5ef392f4b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has requested
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:176:23 · **resolved** · fingerprint: 852ed94029abbea4e6fab0f6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was created
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:197:14 · **resolved** · fingerprint: 8d81ddd804dfe2c99c883b3e
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:213:237 · **resolved** · fingerprint: 4c95c42ba0a8e33df95da64d
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begins
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:265:158 · **resolved** · fingerprint: a317f5b19e2ab5d770d78d2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is grandfathered
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:271:55 · **resolved** · fingerprint: 54ced16a4522c38f24c053a6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was implemented
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:273:21 · **resolved** · fingerprint: 469e1521575230ced366ea79
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:275:38 · **resolved** · fingerprint: 21fa99cd9adb2127f01fc204
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:277:132 · **resolved** · fingerprint: 101211397f76806715447ab0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:281:85 · **resolved** · fingerprint: befabfa16e1d11b4cc317bc3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implemented
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:291:42 · **resolved** · fingerprint: 063bc6652b2f8cba7e22ed0d
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:299:59 · **resolved** · fingerprint: 8ab2123627f631a8c49701db
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fixed
- **long-sentence** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:329:3 · **resolved** · fingerprint: 8bf6c58f1f0bd3c79519cfd1
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:351:45 · **resolved** · fingerprint: 7a97a9361b4bcc774d6f0ab9
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Validate
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:368:95 · **resolved** · fingerprint: e1b81119b147b4cb2485bf75
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:398:17 · **resolved** · fingerprint: 396aabeca89bdc013b3dc544
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **semicolon** · skills/document-standards/references/document-type-catalog.md:4:279 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:28:139 · **resolved** · fingerprint: 521a3f31bc54ec727caae5b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was found
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:33:453 · **resolved** · fingerprint: bcb83f45ddf38808e5512023
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being uploaded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:37:304 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **semicolon** · skills/document-standards/references/document-type-catalog.md:37:313 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:38:284 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:39:264 · **resolved** · fingerprint: bd13d200f2cd36d327625082
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preserved
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:47:276 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:48:207 · **resolved** · fingerprint: a41ef6bbf64045f943d2af47
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:50:139 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:52:358 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:54:336 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **synonym-rotation** · skills/document-standards/references/document-type-catalog.md:57:250 · **resolved** · fingerprint: 2822a6b08706709830f1f820
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:57:311 · **resolved** · fingerprint: 611e1aa7abfb794630cb37cf
  - **Level:** advisory-free
  - **Message:** Sentence has 29 words (cap 25). Split it.
  - **Matched text:** 29 words
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:59:651 · **resolved** · fingerprint: 64a21a094ac7cf2fa75992d0
  - **Level:** advisory-free
  - **Message:** Sentence has 43 words (cap 25). Split it.
  - **Matched text:** 43 words
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:60:435 · **resolved** · fingerprint: 4213736a472e3b847e27d1ae
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are archived
- **semicolon** · skills/document-standards/references/document-type-catalog.md:60:653 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:60:705 · **resolved** · fingerprint: 8e6ebb9019d53b6c90f1902c
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:61:546 · **resolved** · fingerprint: 199f2603ee3fb1c3abd18ce6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are skipped
- **semicolon** · skills/document-standards/references/document-type-catalog.md:61:568 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:69:165 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:69:176 · **resolved** · fingerprint: ea92de1fbbfc0e6cafa24f7b
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:74:257 · **resolved** · fingerprint: 6192a6cd4c83102388153572
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **semicolon** · skills/document-standards/references/document-type-catalog.md:74:306 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:74:363 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:74:509 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:76:117 · **resolved** · fingerprint: 6192a6cd4c83102388153572
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **semicolon** · skills/document-standards/references/document-type-catalog.md:76:219 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:76:316 · **resolved** · fingerprint: 4b99bc607f23d422ec3ca66d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are limited
- **semicolon** · skills/document-standards/references/document-type-catalog.md:80:233 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:81:198 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:82:257 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:84:265 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:85:184 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:86:188 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:90:101 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:91:131 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:92:135 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:94:180 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:95:231 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · skills/document-standards/references/document-type-catalog.md:95:268 · **resolved** · fingerprint: 028b84870f82ee2f98dcbf3b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has run
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:97:169 · **resolved** · fingerprint: bb8de6bc648079b20917fbff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are catalogued
- **semicolon** · skills/document-standards/references/document-type-catalog.md:106:207 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:107:215 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:108:227 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:108:263 · **resolved** · fingerprint: 305641bf283ed85e29efe674
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is published
- **semicolon** · skills/document-standards/references/document-type-catalog.md:109:227 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:110:267 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:112:242 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:113:223 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:118:223 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:120:188 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:120:251 · **resolved** · fingerprint: 195a2fd68103c17c8542eb26
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are covered
- **semicolon** · skills/document-standards/references/document-type-catalog.md:123:117 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · skills/document-standards/references/document-type-catalog.md:125:140 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:134:155 · **resolved** · fingerprint: 1ba4a4dabed935af86f226cb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:152:39 · **resolved** · fingerprint: 0c06b4bea825bbb8305e2205
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were reviewed
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:157:200 · **resolved** · fingerprint: ea92de1fbbfc0e6cafa24f7b
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **present-perfect** · skills/document-standards/references/document-type-catalog.md:157:479 · **resolved** · fingerprint: 5bfc1af36a470f1f001188ee
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been approved
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:157:483 · **resolved** · fingerprint: c8520603dffa16dea8ea3dc4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been approved
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:158:136 · **resolved** · fingerprint: 6046357fc6d15e771a97e487
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are established
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:160:131 · **resolved** · fingerprint: f99656c38dfabd9bba499a0e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:160:206 · **resolved** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:161:199 · **resolved** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:163:262 · **resolved** · fingerprint: 95aef61741aad14590481dc3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is uploaded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:173:230 · **resolved** · fingerprint: 446871a6fecc2890373b2df1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:181:129 · **resolved** · fingerprint: 521a3f31bc54ec727caae5b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was found
- **semicolon** · skills/document-standards/references/document-type-catalog.md:192:185 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:193:138 · **resolved** · fingerprint: d8738c991b456b6b6a7cdd80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reconstructed
- **semicolon** · skills/document-standards/references/document-type-catalog.md:193:174 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:196:203 · **resolved** · fingerprint: 32702bd5a2c5ca60292eca3a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are superseded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:205:57 · **resolved** · fingerprint: 9a67866b9f0335cac5eb0d64
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was required
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:209:189 · **resolved** · fingerprint: 7e6ec02ac376dc4e638ffc6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was warranted
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:217:32 · **resolved** · fingerprint: d5a3d56f7803c8bd7fe2f5bb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added
- **semicolon** · skills/document-standards/references/document-type-catalog.md:225:203 · **resolved** · fingerprint: 34b3ecad2f55b58c81da2ca0
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/task_board.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 3
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 824
- **Findings per 100 words:** 0.4

#### Complete diagnostics

- **passive-voice** · workspace/task_board.md:7:110 · **recurring** · fingerprint: cfe2615d32498b8cb18022ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are removed

- **passive-voice** · workspace/task_board.md:7:137 · **recurring** · fingerprint: e6baee8e949dc0ee0a1c0b34
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded

- **passive-voice** · workspace/task_board.md:7:162 · **recurring** · fingerprint: 86cd35c95eb6d5488c436e85
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved


### skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 28
- **Hard findings:** 17
- **Baseline:** 0
- **Words:** 4771
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

- **passive-voice** · skills/the-worker/SKILL.md:61:61 · **new** · fingerprint: 0eebcb0484fe67c4e2017ecc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided

- **passive-voice** · skills/the-worker/SKILL.md:115:111 · **new** · fingerprint: d226740cae172dd2e1c78d14
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · skills/the-worker/SKILL.md:304:178 · **new** · fingerprint: 48c926404290adf5d27a8438
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is marked

- **long-sentence** · skills/the-worker/SKILL.md:304:237 · **new** · fingerprint: 2a032b53781931d6c779e34b
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **semicolon** · skills/the-worker/SKILL.md:304:362 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/the-worker/SKILL.md:307:251 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/the-worker/SKILL.md:309:108 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/the-worker/SKILL.md:310:277 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/the-worker/SKILL.md:311:140 · **new** · fingerprint: f0690d035381adacbc37a83e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **semicolon** · skills/the-worker/SKILL.md:311:200 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/the-worker/SKILL.md:311:242 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · skills/the-worker/SKILL.md:312:54 · **new** · fingerprint: 0888728fc5c2a25c2caac0be
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived

- **passive-voice** · skills/the-worker/SKILL.md:313:66 · **new** · fingerprint: 3003cdc6d38c0022f8be463c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed

- **long-sentence** · skills/the-worker/SKILL.md:313:204 · **new** · fingerprint: ead8bfcb0c1049225be6ce1d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **passive-voice** · skills/the-worker/SKILL.md:313:330 · **new** · fingerprint: 59e52367ff4fbe890c502667
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are archived

- **long-sentence** · skills/the-worker/SKILL.md:315:188 · **new** · fingerprint: 1ca5b3d7c683e38db0ecafeb
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **synonym-rotation** · skills/the-worker/SKILL.md:323:3 · **new** · fingerprint: 6d31ffa74d22866fde26008b
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove

- **passive-voice** · skills/the-worker/SKILL.md:325:90 · **new** · fingerprint: c2eadbfa652dd24c2decf4de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being removed

- **semicolon** · skills/the-worker/SKILL.md:325:103 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · skills/the-worker/SKILL.md:328:120 · **new** · fingerprint: 3e9dae68ac0dc79de8ae5c41
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **present-perfect** · skills/the-worker/SKILL.md:339:168 · **new** · fingerprint: 0e07f428da579362c55d461b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been verified

- **passive-voice** · skills/the-worker/SKILL.md:339:172 · **new** · fingerprint: b6cbb5b662b7ac93ef3ba05e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified

- **synonym-rotation** · skills/the-worker/SKILL.md:343:102 · **new** · fingerprint: b0d48c1fdb52aa58dc1b1908
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirm

- **long-sentence** · skills/the-worker/SKILL.md:344:4 · **new** · fingerprint: 2a032b53781931d6c779e34b
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words

- **synonym-rotation** · skills/the-worker/SKILL.md:360:182 · **new** · fingerprint: 0564bcc241576c15bb1f3427
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
