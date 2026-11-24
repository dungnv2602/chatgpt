# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#663](https://github.com/dungnv2602/chatgpt/actions/runs/45436626400)
- **Run ID / attempt:** 45436626400 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / de6f18a6cb4d91784b71fce334de73505c7328fe
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** cf293d2d7bc3396eefb91360f0b36561d777ceb4
- **Linter source SHA:** de6f18a6cb4d91784b71fce334de73505c7328fe
- **Generated (UTC):** 2026-11-24T16:27:49.640750+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 9 |
| Files that failed | 6 |
| Files with findings | 9 |
| Total findings | 115 |
| Hard findings | 41 |
| Advisory findings | 74 |
| New findings | 60 |
| Recurring findings | 55 |
| Resolved findings | 23 |
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
- workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md
- workspace/draft/README.md
- workspace/README.md
- workspace/DRAFT_TEMPLATE.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/adr/README.md | FAIL | 4 | 2 | 0 | 517 | 0.8 | 1 |
| workspace/ADR_TEMPLATE.md | PASS | 2 | 0 | 0 | 346 | 0.6 | 0 |
| skills/decision-governance/SKILL.md | FAIL | 19 | 5 | 0 | 2186 | 0.9 | 1 |
| skills/document-standards/references/document-type-catalog.md | FAIL | 31 | 2 | 0 | 4344 | 0.7 | 1 |
| workspace/task_board.md | PASS | 3 | 0 | 0 | 1420 | 0.2 | 0 |
| workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md | FAIL | 51 | 30 | 0 | 2618 | 1.9 | 1 |
| workspace/draft/README.md | FAIL | 1 | 1 | 0 | 409 | 0.2 | 1 |
| workspace/README.md | FAIL | 3 | 1 | 0 | 882 | 0.3 | 1 |
| workspace/DRAFT_TEMPLATE.md | PASS | 1 | 0 | 0 | 425 | 0.2 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 69 |
| semicolon | 22 |
| synonym-rotation | 13 |
| long-sentence | 6 |
| present-perfect | 5 |

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
Ran 4 tests in 0.357s

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

- **passive-voice** · workspace/ADR_TEMPLATE.md:29:67 · **new** · fingerprint: 245ae5ff11bd1a7e1426ac61
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · workspace/ADR_TEMPLATE.md:53:57 · **new** · fingerprint: 7161ac8330313d0a21373d48
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implemented
- **passive-voice** · skills/decision-governance/SKILL.md:29:58 · **new** · fingerprint: 62ba07312f0098deae0d2084
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved
- **passive-voice** · skills/decision-governance/SKILL.md:29:82 · **new** · fingerprint: a461c9d33f692bb30c8d9e32
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **synonym-rotation** · skills/decision-governance/SKILL.md:61:112 · **new** · fingerprint: 2624698c9e0a949a01e1c0be
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **synonym-rotation** · skills/decision-governance/SKILL.md:97:79 · **new** · fingerprint: fe036b1c2041ea8ab5e5609d
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **synonym-rotation** · skills/decision-governance/SKILL.md:99:39 · **new** · fingerprint: 22de3080c9e96c2f5e360d7c
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **synonym-rotation** · skills/decision-governance/SKILL.md:100:5 · **new** · fingerprint: 9d17b4b98b345cc668999283
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **passive-voice** · skills/decision-governance/SKILL.md:127:44 · **new** · fingerprint: a461c9d33f692bb30c8d9e32
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **synonym-rotation** · skills/decision-governance/SKILL.md:137:75 · **new** · fingerprint: 4e69277105db71c84c9a2d9e
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct
- **passive-voice** · skills/decision-governance/SKILL.md:139:23 · **new** · fingerprint: 712aaab97b2af72d676d1263
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · skills/decision-governance/SKILL.md:156:56 · **new** · fingerprint: 60f7b0b5e3f1e7faa3f326cc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved
- **passive-voice** · skills/decision-governance/SKILL.md:156:115 · **new** · fingerprint: 50567c7971d82a5d8b54420a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are resolved
- **passive-voice** · skills/decision-governance/SKILL.md:158:97 · **new** · fingerprint: 7b5a481ca6d089fd1b1dedf0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are verified
- **passive-voice** · skills/decision-governance/SKILL.md:170:19 · **new** · fingerprint: 2d396573c9ffec67f6ef5943
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are accepted
- **passive-voice** · skills/decision-governance/SKILL.md:201:89 · **new** · fingerprint: a461c9d33f692bb30c8d9e32
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **passive-voice** · skills/decision-governance/SKILL.md:208:50 · **new** · fingerprint: e1b2426fdfb12ab8d8076ca7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implemented
- **passive-voice** · skills/decision-governance/SKILL.md:237:72 · **new** · fingerprint: 3b0fa6154ecfe49591695005
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being worked
- **present-perfect** · skills/decision-governance/SKILL.md:247:22 · **new** · fingerprint: 7481ea9586cd9998cf136bf1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read
- **passive-voice** · skills/decision-governance/SKILL.md:247:26 · **new** · fingerprint: 50eae35fe6ca9a2e19bff9a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read
- **passive-voice** · skills/decision-governance/SKILL.md:248:38 · **new** · fingerprint: 58b03457b929a04127a23698
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:3:1 · **new** · fingerprint: 33b66dbc6dc280ae7c9be6c8
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
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
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:39:264 · **new** · fingerprint: bd13d200f2cd36d327625082
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preserved
- **synonym-rotation** · skills/document-standards/references/document-type-catalog.md:45:198 · **new** · fingerprint: 2822a6b08706709830f1f820
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks
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
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:63:560 · **new** · fingerprint: 199f2603ee3fb1c3abd18ce6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are skipped
- **present-perfect** · skills/document-standards/references/document-type-catalog.md:98:268 · **new** · fingerprint: 028b84870f82ee2f98dcbf3b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has run
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:100:169 · **new** · fingerprint: bb8de6bc648079b20917fbff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are catalogued
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:111:263 · **new** · fingerprint: 305641bf283ed85e29efe674
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is published
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:123:251 · **new** · fingerprint: 195a2fd68103c17c8542eb26
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are covered
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:158:39 · **new** · fingerprint: 0c06b4bea825bbb8305e2205
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were reviewed
- **present-perfect** · skills/document-standards/references/document-type-catalog.md:163:448 · **new** · fingerprint: 5bfc1af36a470f1f001188ee
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been approved
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:163:452 · **new** · fingerprint: c8520603dffa16dea8ea3dc4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been approved
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:164:136 · **new** · fingerprint: 6046357fc6d15e771a97e487
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are established
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:166:131 · **new** · fingerprint: f99656c38dfabd9bba499a0e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:166:206 · **new** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:167:199 · **new** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:169:262 · **new** · fingerprint: 95aef61741aad14590481dc3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is uploaded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:179:230 · **new** · fingerprint: 446871a6fecc2890373b2df1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:187:129 · **new** · fingerprint: 521a3f31bc54ec727caae5b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was found
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:199:138 · **new** · fingerprint: d8738c991b456b6b6a7cdd80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reconstructed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:202:203 · **new** · fingerprint: 32702bd5a2c5ca60292eca3a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are superseded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:211:57 · **new** · fingerprint: 9a67866b9f0335cac5eb0d64
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was required
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:215:189 · **new** · fingerprint: 7e6ec02ac376dc4e638ffc6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was warranted
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:223:32 · **new** · fingerprint: d5a3d56f7803c8bd7fe2f5bb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:249:123 · **new** · fingerprint: 55c2f7882df07adcfce356d5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is linked
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:250:118 · **new** · fingerprint: cb69fc175cc5d06b9d0e4942
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was removed
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:250:238 · **new** · fingerprint: 1f05f232e3f4079a09edc109
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was deleted
- **synonym-rotation** · workspace/draft/README.md:25:5 · **new** · fingerprint: 644228716a76a4c04d4becf4
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **synonym-rotation** · workspace/README.md:46:124 · **new** · fingerprint: 3659e4816d32f3f6e196b772
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **passive-voice** · workspace/README.md:58:108 · **new** · fingerprint: 4a500644b11ea45e7a256ac0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · workspace/README.md:62:305 · **new** · fingerprint: 44bac24ecf823fa7716cc698
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **present-perfect** · workspace/DRAFT_TEMPLATE.md:46:106 · **new** · fingerprint: 19ad35858d820c065c7de6e1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has mixed

### Recurring findings

- **passive-voice** · workspace/adr/README.md:59:38 · **recurring** · fingerprint: c5d87e6a30d090336e26669a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **semicolon** · workspace/adr/README.md:65:135 · **recurring** · fingerprint: 0927b4ce823c0e0c8d5570fa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/README.md:66:203 · **recurring** · fingerprint: 0927b4ce823c0e0c8d5570fa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/README.md:66:240 · **recurring** · fingerprint: 1e1a8d236c2a85c807def489
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded
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
- **present-perfect** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:35:261 · **recurring** · fingerprint: dc863a59620ce525978fa30c
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:35:265 · **recurring** · fingerprint: 17a4d086602b381ce65c59f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:43:257 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:44:3 · **recurring** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:3 · **recurring** · fingerprint: 5234929a399cf01e0d7f595c
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:129 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:153 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:185 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:207 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:53:80 · **recurring** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:80:16 · **recurring** · fingerprint: 2b26cf53803b151c21212120
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:110:1 · **recurring** · fingerprint: b394b51b09ad308cc8feeae3
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:110:179 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:116:72 · **recurring** · fingerprint: f7c21f7d8940f28c70370284
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:117:114 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:120:175 · **recurring** · fingerprint: 44fcd3dad59ced40bc859413
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct
- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:121:203 · **recurring** · fingerprint: 45a08d05aee0fa7834e7cd1d
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:151:44 · **recurring** · fingerprint: 1f54f40b8113eca478ce4dde
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:153:3 · **recurring** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:159:127 · **recurring** · fingerprint: beb9ea53ee058f3d9e59ec0c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been reserved
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:162:14 · **recurring** · fingerprint: 1f54f40b8113eca478ce4dde
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:162:88 · **recurring** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:188:70 · **recurring** · fingerprint: 15acf5b3ddc984f62af012a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:189:56 · **recurring** · fingerprint: 5c06934743c9618694761365
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:191:51 · **recurring** · fingerprint: 51cadbdd6b8eb0498821f9bb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are confirmed
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:210:9 · **recurring** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:212:94 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:213:7 · **recurring** · fingerprint: 33b3ff5444bee044b23c7ce9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reused
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:214:33 · **recurring** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:3 · **recurring** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:69 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:94 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:133 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:169 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:207 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:222:186 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:226:97 · **recurring** · fingerprint: 03a989d439e11fa4326ad6bc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retired
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:226:134 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:228:125 · **recurring** · fingerprint: 36e134bec11bbd982d0e34fe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:38 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:61 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:71 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:104 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:131 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:239:39 · **recurring** · fingerprint: 5c06934743c9618694761365
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:241:18 · **recurring** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:242:26 · **recurring** · fingerprint: d76d92c78578fde984466a23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:248:84 · **recurring** · fingerprint: 732e2543da3ef19c1be7937b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was read

### Resolved findings

- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:42:64 · **resolved** · fingerprint: 04ec4f5fbb130c1324f44f00
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:83:41 · **resolved** · fingerprint: 5d7ba294a41810bbc4f7a8fe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was made
- **present-perfect** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:179:31 · **resolved** · fingerprint: 015ecb389e532dd8875c1837
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has presented
- **present-perfect** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:180:34 · **resolved** · fingerprint: 0f4521e8c2b440c5ef392f4b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has requested
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:182:23 · **resolved** · fingerprint: 852ed94029abbea4e6fab0f6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was created
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:203:14 · **resolved** · fingerprint: 8d81ddd804dfe2c99c883b3e
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:219:237 · **resolved** · fingerprint: 4c95c42ba0a8e33df95da64d
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begins
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:271:158 · **resolved** · fingerprint: a317f5b19e2ab5d770d78d2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is grandfathered
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:277:55 · **resolved** · fingerprint: 54ced16a4522c38f24c053a6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was implemented
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:279:21 · **resolved** · fingerprint: 469e1521575230ced366ea79
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:281:38 · **resolved** · fingerprint: 21fa99cd9adb2127f01fc204
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:283:132 · **resolved** · fingerprint: 101211397f76806715447ab0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:287:85 · **resolved** · fingerprint: befabfa16e1d11b4cc317bc3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implemented
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:297:42 · **resolved** · fingerprint: 063bc6652b2f8cba7e22ed0d
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:305:59 · **resolved** · fingerprint: 8ab2123627f631a8c49701db
  - **Level:** advisory-free
  - **Message:** 'fix' and 'repair' name the same action. Pick one and use it every time.
  - **Matched text:** fixed
- **long-sentence** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:335:3 · **resolved** · fingerprint: 8bf6c58f1f0bd3c79519cfd1
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **synonym-rotation** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:357:45 · **resolved** · fingerprint: 7a97a9361b4bcc774d6f0ab9
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Validate
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:374:95 · **resolved** · fingerprint: e1b81119b147b4cb2485bf75
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved
- **passive-voice** · workspace/draft/DRAFT-0001-repository-decision-governance-and-analysis.md:404:17 · **resolved** · fingerprint: 396aabeca89bdc013b3dc544
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **passive-voice** · workspace/task_board.md:11:31 · **resolved** · fingerprint: ed2247bc287f94142d470682
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is selected
- **semicolon** · workspace/draft/README.md:19:152 · **resolved** · fingerprint: 388932780643d2141e1a4492
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **present-perfect** · workspace/draft/README.md:19:179 · **resolved** · fingerprint: 3832db9cae5a8a4e53c68141
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been corrected
- **passive-voice** · workspace/draft/README.md:19:183 · **resolved** · fingerprint: a490f7b04ccd2a7c6fb6e16d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been corrected

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/adr/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 517
- **Findings per 100 words:** 0.8

#### Complete diagnostics

- **passive-voice** · workspace/adr/README.md:59:38 · **recurring** · fingerprint: c5d87e6a30d090336e26669a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done

- **semicolon** · workspace/adr/README.md:65:135 · **recurring** · fingerprint: 0927b4ce823c0e0c8d5570fa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/README.md:66:203 · **recurring** · fingerprint: 0927b4ce823c0e0c8d5570fa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/README.md:66:240 · **recurring** · fingerprint: 1e1a8d236c2a85c807def489
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded


### workspace/ADR_TEMPLATE.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 2
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 346
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **passive-voice** · workspace/ADR_TEMPLATE.md:29:67 · **new** · fingerprint: 245ae5ff11bd1a7e1426ac61
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **passive-voice** · workspace/ADR_TEMPLATE.md:53:57 · **new** · fingerprint: 7161ac8330313d0a21373d48
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implemented


### skills/decision-governance/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 19
- **Hard findings:** 5
- **Baseline:** 0
- **Words:** 2186
- **Findings per 100 words:** 0.9

#### Complete diagnostics

- **passive-voice** · skills/decision-governance/SKILL.md:29:58 · **new** · fingerprint: 62ba07312f0098deae0d2084
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved

- **passive-voice** · skills/decision-governance/SKILL.md:29:82 · **new** · fingerprint: a461c9d33f692bb30c8d9e32
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **synonym-rotation** · skills/decision-governance/SKILL.md:61:112 · **new** · fingerprint: 2624698c9e0a949a01e1c0be
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks

- **synonym-rotation** · skills/decision-governance/SKILL.md:97:79 · **new** · fingerprint: fe036b1c2041ea8ab5e5609d
  - **Level:** advisory-free
  - **Message:** 'validate' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** validated

- **synonym-rotation** · skills/decision-governance/SKILL.md:99:39 · **new** · fingerprint: 22de3080c9e96c2f5e360d7c
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove

- **synonym-rotation** · skills/decision-governance/SKILL.md:100:5 · **new** · fingerprint: 9d17b4b98b345cc668999283
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

- **passive-voice** · skills/decision-governance/SKILL.md:127:44 · **new** · fingerprint: a461c9d33f692bb30c8d9e32
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **synonym-rotation** · skills/decision-governance/SKILL.md:137:75 · **new** · fingerprint: 4e69277105db71c84c9a2d9e
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct

- **passive-voice** · skills/decision-governance/SKILL.md:139:23 · **new** · fingerprint: 712aaab97b2af72d676d1263
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · skills/decision-governance/SKILL.md:156:56 · **new** · fingerprint: 60f7b0b5e3f1e7faa3f326cc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved

- **passive-voice** · skills/decision-governance/SKILL.md:156:115 · **new** · fingerprint: 50567c7971d82a5d8b54420a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are resolved

- **passive-voice** · skills/decision-governance/SKILL.md:158:97 · **new** · fingerprint: 7b5a481ca6d089fd1b1dedf0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are verified

- **passive-voice** · skills/decision-governance/SKILL.md:170:19 · **new** · fingerprint: 2d396573c9ffec67f6ef5943
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are accepted

- **passive-voice** · skills/decision-governance/SKILL.md:201:89 · **new** · fingerprint: a461c9d33f692bb30c8d9e32
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **passive-voice** · skills/decision-governance/SKILL.md:208:50 · **new** · fingerprint: e1b2426fdfb12ab8d8076ca7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implemented

- **passive-voice** · skills/decision-governance/SKILL.md:237:72 · **new** · fingerprint: 3b0fa6154ecfe49591695005
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being worked

- **present-perfect** · skills/decision-governance/SKILL.md:247:22 · **new** · fingerprint: 7481ea9586cd9998cf136bf1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read

- **passive-voice** · skills/decision-governance/SKILL.md:247:26 · **new** · fingerprint: 50eae35fe6ca9a2e19bff9a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read

- **passive-voice** · skills/decision-governance/SKILL.md:248:38 · **new** · fingerprint: 58b03457b929a04127a23698
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded


### skills/document-standards/references/document-type-catalog.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 31
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 4344
- **Findings per 100 words:** 0.7

#### Complete diagnostics

- **long-sentence** · skills/document-standards/references/document-type-catalog.md:3:1 · **new** · fingerprint: 33b66dbc6dc280ae7c9be6c8
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

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

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:39:264 · **new** · fingerprint: bd13d200f2cd36d327625082
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preserved

- **synonym-rotation** · skills/document-standards/references/document-type-catalog.md:45:198 · **new** · fingerprint: 2822a6b08706709830f1f820
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks

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

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:63:560 · **new** · fingerprint: 199f2603ee3fb1c3abd18ce6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are skipped

- **present-perfect** · skills/document-standards/references/document-type-catalog.md:98:268 · **new** · fingerprint: 028b84870f82ee2f98dcbf3b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has run

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:100:169 · **new** · fingerprint: bb8de6bc648079b20917fbff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are catalogued

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:111:263 · **new** · fingerprint: 305641bf283ed85e29efe674
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is published

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:123:251 · **new** · fingerprint: 195a2fd68103c17c8542eb26
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are covered

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:158:39 · **new** · fingerprint: 0c06b4bea825bbb8305e2205
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were reviewed

- **present-perfect** · skills/document-standards/references/document-type-catalog.md:163:448 · **new** · fingerprint: 5bfc1af36a470f1f001188ee
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been approved

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:163:452 · **new** · fingerprint: c8520603dffa16dea8ea3dc4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been approved

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:164:136 · **new** · fingerprint: 6046357fc6d15e771a97e487
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are established

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:166:131 · **new** · fingerprint: f99656c38dfabd9bba499a0e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:166:206 · **new** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:167:199 · **new** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:169:262 · **new** · fingerprint: 95aef61741aad14590481dc3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is uploaded

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:179:230 · **new** · fingerprint: 446871a6fecc2890373b2df1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:187:129 · **new** · fingerprint: 521a3f31bc54ec727caae5b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was found

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:199:138 · **new** · fingerprint: d8738c991b456b6b6a7cdd80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reconstructed

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:202:203 · **new** · fingerprint: 32702bd5a2c5ca60292eca3a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are superseded

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:211:57 · **new** · fingerprint: 9a67866b9f0335cac5eb0d64
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was required

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:215:189 · **new** · fingerprint: 7e6ec02ac376dc4e638ffc6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was warranted

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:223:32 · **new** · fingerprint: d5a3d56f7803c8bd7fe2f5bb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added


### workspace/task_board.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 3
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 1420
- **Findings per 100 words:** 0.2

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


### workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 51
- **Hard findings:** 30
- **Baseline:** 0
- **Words:** 2618
- **Findings per 100 words:** 1.9

#### Complete diagnostics

- **present-perfect** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:35:261 · **recurring** · fingerprint: dc863a59620ce525978fa30c
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:35:265 · **recurring** · fingerprint: 17a4d086602b381ce65c59f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:43:257 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:44:3 · **recurring** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:3 · **recurring** · fingerprint: 5234929a399cf01e0d7f595c
  - **Level:** advisory-free
  - **Message:** Sentence has 39 words (cap 25). Split it.
  - **Matched text:** 39 words

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:129 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:153 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:185 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:45:207 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:53:80 · **recurring** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted

- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:80:16 · **recurring** · fingerprint: 2b26cf53803b151c21212120
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Verify

- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:110:1 · **recurring** · fingerprint: b394b51b09ad308cc8feeae3
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:110:179 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:116:72 · **recurring** · fingerprint: f7c21f7d8940f28c70370284
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** Confirm

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:117:114 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:120:175 · **recurring** · fingerprint: 44fcd3dad59ced40bc859413
  - **Level:** advisory-free
  - **Message:** 'correct' and 'fix' name the same action. Pick one and use it every time.
  - **Matched text:** Correct

- **synonym-rotation** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:121:203 · **recurring** · fingerprint: 45a08d05aee0fa7834e7cd1d
  - **Level:** advisory-free
  - **Message:** 'validate' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** validated

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:151:44 · **recurring** · fingerprint: 1f54f40b8113eca478ce4dde
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:153:3 · **recurring** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:159:127 · **recurring** · fingerprint: beb9ea53ee058f3d9e59ec0c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been reserved

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:162:14 · **recurring** · fingerprint: 1f54f40b8113eca478ce4dde
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:162:88 · **recurring** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:188:70 · **recurring** · fingerprint: 15acf5b3ddc984f62af012a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:189:56 · **recurring** · fingerprint: 5c06934743c9618694761365
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:191:51 · **recurring** · fingerprint: 51cadbdd6b8eb0498821f9bb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are confirmed

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:210:9 · **recurring** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:212:94 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:213:7 · **recurring** · fingerprint: 33b3ff5444bee044b23c7ce9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reused

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:214:33 · **recurring** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted

- **long-sentence** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:3 · **recurring** · fingerprint: c7a688d7f3b5d323000e2504
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:69 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:94 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:133 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:169 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:219:207 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:222:186 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:226:97 · **recurring** · fingerprint: 03a989d439e11fa4326ad6bc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retired

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:226:134 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:228:125 · **recurring** · fingerprint: 36e134bec11bbd982d0e34fe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:38 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:61 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:71 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:104 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:229:131 · **recurring** · fingerprint: 6b1a09dc16c81cc09cefa126
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:239:39 · **recurring** · fingerprint: 5c06934743c9618694761365
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:241:18 · **recurring** · fingerprint: 5cea8eeb30e42074ae550234
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:242:26 · **recurring** · fingerprint: d76d92c78578fde984466a23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:248:84 · **recurring** · fingerprint: 732e2543da3ef19c1be7937b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was read

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:249:123 · **new** · fingerprint: 55c2f7882df07adcfce356d5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is linked

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:250:118 · **new** · fingerprint: cb69fc175cc5d06b9d0e4942
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was removed

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:250:238 · **new** · fingerprint: 1f05f232e3f4079a09edc109
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was deleted


### workspace/draft/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 409
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **synonym-rotation** · workspace/draft/README.md:25:5 · **new** · fingerprint: 644228716a76a4c04d4becf4
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove


### workspace/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 3
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 882
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **synonym-rotation** · workspace/README.md:46:124 · **new** · fingerprint: 3659e4816d32f3f6e196b772
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

- **passive-voice** · workspace/README.md:58:108 · **new** · fingerprint: 4a500644b11ea45e7a256ac0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived

- **passive-voice** · workspace/README.md:62:305 · **new** · fingerprint: 44bac24ecf823fa7716cc698
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required


### workspace/DRAFT_TEMPLATE.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 425
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **present-perfect** · workspace/DRAFT_TEMPLATE.md:46:106 · **new** · fingerprint: 19ad35858d820c065c7de6e1
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
