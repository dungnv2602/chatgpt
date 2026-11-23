# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#474](https://github.com/dungnv2602/chatgpt/actions/runs/45159721991)
- **Run ID / attempt:** 45159721991 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 0e1fbb6b1dc7696a51badffe11e2f1b2a6ca4edc
- **Event:** push
- **Execution mode:** full-audit-fallback
- **Baseline SHA:** Not applicable
- **Linter source SHA:** 0e1fbb6b1dc7696a51badffe11e2f1b2a6ca4edc
- **Generated (UTC):** 2026-11-23T10:50:59.886634+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 49 |
| Files that failed | 4 |
| Files with findings | 39 |
| Total findings | 346 |
| Hard findings | 27 |
| Advisory findings | 319 |
| New findings | 0 |
| Recurring findings | 346 |
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

- skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md
- skills/philosophy-religion-asceticism/SKILL.md
- skills/session-archiving/assets/conversation-integrity-template.md
- skills/drawing/references/patterns/failure-patterns.md
- skills/agent-skill-authoring/SKILL.md
- skills/asd-ste100/references/repository-writing-policy.md
- skills/philosophy-religion-asceticism/references/source-standards.md
- skills/asd-ste100/README.md
- skills/asd-ste100/assets/lint-report-template.md
- skills/drawing/README.md
- skills/drawing/assets/pattern-entry-templates.md
- images/takeout/README.md
- images/README.md
- skills/asd-ste100/SKILL.md
- skills/philosophy-religion-asceticism/README.md
- skills/drawing/references/archive-and-delivery.md
- skills/README.md
- skills/github-actions/SKILL.md
- skills/drawing/assets/attempt-template.md
- skills/drawing/references/patterns/successful-patterns.md
- skills/drawing/references/generation-recovery-and-provenance.md
- skills/session-archiving/references/image-provenance-and-webp.md
- skills/conversation-mode/SKILL.md
- skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md
- skills/drawing/SKILL.md
- skills/document-standards/references/document-type-catalog.md
- workspace/task_board.md
- skills/drawing/references/style-guide.md
- skills/INITIALIZATION_POLICY.md
- skills/drawing/assets/daily-index-template.md
- skills/session-archiving/assets/session-summary-template.md
- workspace/TASK_TEMPLATE.md
- skills/drawing/references/series-continuity-and-iteration.md
- skills/asd-ste100/references/writing-rules.md
- skills/philosophy-religion-asceticism/references/answer-patterns.md
- workspace/README.md
- skills/session-archiving/references/image-processing-scripts.md
- skills/the-worker/SKILL.md
- skills/session-archiving/references/drawing-session-closeout.md
- skills/session-archiving/references/archive-records-and-image-prompts.md
- skills/drawing/references/prompt-fidelity.md
- skills/document-standards/SKILL.md
- skills/session-archiving/SKILL.md
- skills/drawing/references/image-editing-protocol.md
- skills/session-archiving/assets/session-brief-template.md
- skills/SESSION_START.md
- skills/drawing/references/patterns/README.md
- skills/philosophy-religion-asceticism/references/research-method.md
- skills/philosophy-religion-asceticism/CHANGELOG.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md | PASS | 0 | 0 | 0 | 166 | 0.0 | 0 |
| skills/philosophy-religion-asceticism/SKILL.md | PASS | 8 | 0 | 7 | 2387 | 0.3 | 0 |
| skills/session-archiving/assets/conversation-integrity-template.md | PASS | 0 | 0 | 0 | 192 | 0.0 | 0 |
| skills/drawing/references/patterns/failure-patterns.md | PASS | 25 | 0 | 0 | 2146 | 1.2 | 0 |
| skills/agent-skill-authoring/SKILL.md | PASS | 17 | 1 | 6 | 2259 | 0.8 | 0 |
| skills/asd-ste100/references/repository-writing-policy.md | PASS | 1 | 0 | 0 | 570 | 0.2 | 0 |
| skills/philosophy-religion-asceticism/references/source-standards.md | PASS | 2 | 0 | 1 | 1467 | 0.1 | 0 |
| skills/asd-ste100/README.md | PASS | 2 | 0 | 0 | 1534 | 0.1 | 0 |
| skills/asd-ste100/assets/lint-report-template.md | PASS | 0 | 0 | 0 | 385 | 0.0 | 0 |
| skills/drawing/README.md | PASS | 0 | 0 | 0 | 396 | 0.0 | 0 |
| skills/drawing/assets/pattern-entry-templates.md | PASS | 7 | 0 | 0 | 449 | 1.6 | 0 |
| images/takeout/README.md | PASS | 1 | 0 | 0 | 1397 | 0.1 | 0 |
| images/README.md | PASS | 1 | 0 | 0 | 584 | 0.2 | 0 |
| skills/asd-ste100/SKILL.md | PASS | 21 | 13 | 31 | 2609 | 0.8 | 0 |
| skills/philosophy-religion-asceticism/README.md | PASS | 1 | 0 | 0 | 471 | 0.2 | 0 |
| skills/drawing/references/archive-and-delivery.md | PASS | 20 | 0 | 7 | 2370 | 0.8 | 0 |
| skills/README.md | PASS | 0 | 0 | 0 | 371 | 0.0 | 0 |
| skills/github-actions/SKILL.md | PASS | 3 | 0 | 0 | 2534 | 0.1 | 0 |
| skills/drawing/assets/attempt-template.md | PASS | 1 | 0 | 0 | 593 | 0.2 | 0 |
| skills/drawing/references/patterns/successful-patterns.md | PASS | 6 | 0 | 0 | 816 | 0.7 | 0 |
| skills/drawing/references/generation-recovery-and-provenance.md | PASS | 19 | 0 | 17 | 2757 | 0.7 | 0 |
| skills/session-archiving/references/image-provenance-and-webp.md | PASS | 13 | 1 | 2 | 1710 | 0.8 | 0 |
| skills/conversation-mode/SKILL.md | PASS | 17 | 0 | 3 | 3080 | 0.6 | 0 |
| skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md | PASS | 8 | 0 | 7 | 2716 | 0.3 | 0 |
| skills/drawing/SKILL.md | PASS | 24 | 3 | 24 | 5082 | 0.5 | 0 |
| skills/document-standards/references/document-type-catalog.md | FAIL | 27 | 3 | 0 | 3060 | 0.9 | 1 |
| workspace/task_board.md | PASS | 3 | 0 | 0 | 249 | 1.2 | 0 |
| skills/drawing/references/style-guide.md | PASS | 1 | 0 | 0 | 462 | 0.2 | 0 |
| skills/INITIALIZATION_POLICY.md | PASS | 2 | 0 | 4 | 1180 | 0.2 | 0 |
| skills/drawing/assets/daily-index-template.md | FAIL | 1 | 1 | 0 | 210 | 0.5 | 1 |
| skills/session-archiving/assets/session-summary-template.md | PASS | 0 | 0 | 0 | 106 | 0.0 | 0 |
| workspace/TASK_TEMPLATE.md | FAIL | 5 | 1 | 0 | 385 | 1.3 | 1 |
| skills/drawing/references/series-continuity-and-iteration.md | PASS | 10 | 1 | 9 | 3262 | 0.3 | 0 |
| skills/asd-ste100/references/writing-rules.md | PASS | 8 | 0 | 6 | 706 | 1.1 | 0 |
| skills/philosophy-religion-asceticism/references/answer-patterns.md | PASS | 1 | 0 | 0 | 235 | 0.4 | 0 |
| workspace/README.md | PASS | 2 | 0 | 0 | 596 | 0.3 | 0 |
| skills/session-archiving/references/image-processing-scripts.md | PASS | 0 | 0 | 0 | 344 | 0.0 | 0 |
| skills/the-worker/SKILL.md | PASS | 5 | 0 | 0 | 3133 | 0.2 | 0 |
| skills/session-archiving/references/drawing-session-closeout.md | PASS | 1 | 0 | 0 | 612 | 0.2 | 0 |
| skills/session-archiving/references/archive-records-and-image-prompts.md | PASS | 28 | 1 | 20 | 4527 | 0.6 | 0 |
| skills/drawing/references/prompt-fidelity.md | PASS | 46 | 1 | 15 | 3676 | 1.3 | 0 |
| skills/document-standards/SKILL.md | PASS | 2 | 0 | 0 | 1612 | 0.1 | 0 |
| skills/session-archiving/SKILL.md | PASS | 3 | 0 | 7 | 2388 | 0.1 | 0 |
| skills/drawing/references/image-editing-protocol.md | PASS | 0 | 0 | 4 | 962 | 0.0 | 0 |
| skills/session-archiving/assets/session-brief-template.md | FAIL | 1 | 1 | 0 | 288 | 0.3 | 1 |
| skills/SESSION_START.md | PASS | 2 | 0 | 0 | 2275 | 0.1 | 0 |
| skills/drawing/references/patterns/README.md | PASS | 1 | 0 | 0 | 442 | 0.2 | 0 |
| skills/philosophy-religion-asceticism/references/research-method.md | PASS | 0 | 0 | 0 | 559 | 0.0 | 0 |
| skills/philosophy-religion-asceticism/CHANGELOG.md | PASS | 0 | 0 | 0 | 56 | 0.0 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 279 |
| present-perfect | 40 |
| synonym-rotation | 9 |
| long-sentence | 6 |
| marketing-adjective | 5 |
| phrasal-verb | 5 |
| nominalization | 2 |

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
Ran 4 tests in 0.369s

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

- **Result:** Passed
- **Exit code:** 0

~~~text
Scanned 625 active Markdown files (691 available as link targets) and 338 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

None.

### Recurring findings

- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:53:21 · **recurring** · fingerprint: fc114dacae449b7519133918
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:94:11 · **recurring** · fingerprint: 01b04df4a4d61aa32756adf1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is disputed
- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:144:43 · **recurring** · fingerprint: f05c498f9ee2269430ff8ada
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are related
- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:167:67 · **recurring** · fingerprint: c645e65b81e4110faf6f2062
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is contested
- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:178:68 · **recurring** · fingerprint: b1d63c43c6349bc6f120ce18
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is supported
- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:179:43 · **recurring** · fingerprint: 671a7eda510ef040edd3be61
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked
- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:291:3 · **recurring** · fingerprint: ac33fd0d35779883eb5af2cb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been excluded
- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:292:52 · **recurring** · fingerprint: cd2a130c88bf1b1de364eda1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been kept
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:3:126 · **recurring** · fingerprint: ba15e2b13749f7aad6447fc1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are indexed
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:5:65 · **recurring** · fingerprint: fb05b158f323ac0a88758170
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are kept
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:19:163 · **recurring** · fingerprint: 7cb850c3e4335a13e7519ba0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reversed
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:22:89 · **recurring** · fingerprint: ce25d5ad6ba4826e11264f32
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is observed
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:37:14 · **recurring** · fingerprint: 32467609b8c42805cbf2c5ad
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is concentrated
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:48:20 · **recurring** · fingerprint: e1de4bab2e607823412ffbc4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were described
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:51:37 · **recurring** · fingerprint: ac6348f1c31c27d904cb53b4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was modified
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:61:190 · **recurring** · fingerprint: b49561bafa5675d60cc907c5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was attached
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:61:219 · **recurring** · fingerprint: 346827f54f442c607e8b24a5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:85:19 · **recurring** · fingerprint: ede5e693c6707a81cfe3079a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:91:257 · **recurring** · fingerprint: 3c48312b0ae19adb3273832c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:120:226 · **recurring** · fingerprint: e0e662058459fdceb4c02481
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was identified
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:136:66 · **recurring** · fingerprint: 715e2eee6cf5d1784b75c730
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is prepared
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:154:172 · **recurring** · fingerprint: c5308af1d2f63badad79bd66
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was tested
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:165:92 · **recurring** · fingerprint: 74cd4ed7e5ca2631c57c069b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:168:20 · **recurring** · fingerprint: 3c48312b0ae19adb3273832c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:183:164 · **recurring** · fingerprint: ede5e693c6707a81cfe3079a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established
- **present-perfect** · skills/drawing/references/patterns/failure-patterns.md:194:52 · **recurring** · fingerprint: fca6bef2ba2e441b581fcc8d
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has corrected
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:209:228 · **recurring** · fingerprint: 75eccc37cbac9985f7061f82
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was removed
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:209:266 · **recurring** · fingerprint: e56ece3c0f60be33dac72d05
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was preserved
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:210:242 · **recurring** · fingerprint: 5b28443dc965cf5ab3378e12
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was adopted
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:214:32 · **recurring** · fingerprint: b35900a9da7c000de2e26e70
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is maintained
- **present-perfect** · skills/drawing/references/patterns/failure-patterns.md:218:179 · **recurring** · fingerprint: feb2d786d14c99b7e9fe9de0
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has rejected
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:224:30 · **recurring** · fingerprint: 0cae9b0c6170006a0e67edc2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is included
- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:250:20 · **recurring** · fingerprint: b35900a9da7c000de2e26e70
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is maintained
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:14:79 · **recurring** · fingerprint: cf9a19441f150cbc6e394584
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are created
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:160:29 · **recurring** · fingerprint: 6ffc592c0b6322b443496f66
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:163:106 · **recurring** · fingerprint: 6ffc592c0b6322b443496f66
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:167:23 · **recurring** · fingerprint: 6ffc592c0b6322b443496f66
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded
- **present-perfect** · skills/agent-skill-authoring/SKILL.md:171:149 · **recurring** · fingerprint: 2dddc1891d5710f75a1cc520
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been loaded
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:171:153 · **recurring** · fingerprint: f7fae0229a13471823102bb0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been loaded
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:184:36 · **recurring** · fingerprint: 0be774910939027b005107b8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:222:38 · **recurring** · fingerprint: 5eabd6169bec15a6fdfd2a80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been created
- **synonym-rotation** · skills/agent-skill-authoring/SKILL.md:231:18 · **recurring** · fingerprint: cdded221cb31c45f9059249a
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begins
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:244:28 · **recurring** · fingerprint: 0f053c89c3267998b6edc9d6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are focused
- **present-perfect** · skills/agent-skill-authoring/SKILL.md:245:65 · **recurring** · fingerprint: 70dc63b30d658452239a6cbe
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been introduced
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:245:70 · **recurring** · fingerprint: 2df378472bba68cfc7a25cbe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been introduced
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:253:17 · **recurring** · fingerprint: 8416fa6ec8b8068d6f7379c2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is connected
- **present-perfect** · skills/agent-skill-authoring/SKILL.md:255:37 · **recurring** · fingerprint: c26f9840d6188237d9689546
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been made
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:255:41 · **recurring** · fingerprint: 599292fe4dd9cfdbc4788ec9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been made
- **present-perfect** · skills/agent-skill-authoring/SKILL.md:257:32 · **recurring** · fingerprint: 4414015699cf2e3e269abe29
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read
- **passive-voice** · skills/agent-skill-authoring/SKILL.md:257:36 · **recurring** · fingerprint: 91d321a9405d06bea4b12487
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read
- **passive-voice** · skills/asd-ste100/references/repository-writing-policy.md:18:36 · **recurring** · fingerprint: 3ae757460d9b3aa9399e9808
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · skills/philosophy-religion-asceticism/references/source-standards.md:99:19 · **recurring** · fingerprint: ce4f5586a0c66bf136f1a181
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being discussed
- **passive-voice** · skills/philosophy-religion-asceticism/references/source-standards.md:194:41 · **recurring** · fingerprint: 16921dc530cca16c2f4562e8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being cited
- **passive-voice** · skills/asd-ste100/README.md:26:35 · **recurring** · fingerprint: dc6fc135735cd3aa5f4246ff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · skills/asd-ste100/README.md:40:109 · **recurring** · fingerprint: bdbff79e00c0aca5352dcc38
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved
- **passive-voice** · skills/drawing/assets/pattern-entry-templates.md:17:40 · **recurring** · fingerprint: 80ff0d75ee9e57c63a759659
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retired
- **passive-voice** · skills/drawing/assets/pattern-entry-templates.md:18:125 · **recurring** · fingerprint: e71b3a8ba6751987cf0fb966
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are verified
- **passive-voice** · skills/drawing/assets/pattern-entry-templates.md:22:67 · **recurring** · fingerprint: 4cca9a878a87bc55497611c8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **present-perfect** · skills/drawing/assets/pattern-entry-templates.md:100:246 · **recurring** · fingerprint: ad46045395dc40b74a35f499
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has tested
- **passive-voice** · skills/drawing/assets/pattern-entry-templates.md:111:20 · **recurring** · fingerprint: 92485eeff29784dba3505b2d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are separated
- **passive-voice** · skills/drawing/assets/pattern-entry-templates.md:113:15 · **recurring** · fingerprint: 3f5048026fc0041e11f90db1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are described
- **passive-voice** · skills/drawing/assets/pattern-entry-templates.md:115:19 · **recurring** · fingerprint: 9a512eba16db074bc582887d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · images/takeout/README.md:180:40 · **recurring** · fingerprint: bf5f3ed6bfe52608af6f2cbb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reserved
- **passive-voice** · images/README.md:94:54 · **recurring** · fingerprint: 03c08438c1205e007605fad3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reserved
- **passive-voice** · skills/asd-ste100/SKILL.md:21:69 · **recurring** · fingerprint: 7266e62fe12e7cc92f88c06b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was violated
- **passive-voice** · skills/asd-ste100/SKILL.md:49:227 · **recurring** · fingerprint: 4e26f8ad5ee76bbe5f532dd1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are defined
- **passive-voice** · skills/asd-ste100/SKILL.md:57:60 · **recurring** · fingerprint: 0447fbf776081d483d4a8de4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is removed
- **phrasal-verb** · skills/asd-ste100/SKILL.md:58:99 · **recurring** · fingerprint: bc3fa2e84f1094e34446f7f9
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** Spin up
- **passive-voice** · skills/asd-ste100/SKILL.md:73:118 · **recurring** · fingerprint: 081cea6a0061b9dd44d263e8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved
- **nominalization** · skills/asd-ste100/SKILL.md:74:53 · **recurring** · fingerprint: f17e13a684f76bb434777eb7
  - **Level:** advisory-free
  - **Message:** Action frozen into a noun. Use the verb (analyze, not perform an analysis of).
  - **Matched text:** Perform an analysis
- **present-perfect** · skills/asd-ste100/SKILL.md:79:203 · **recurring** · fingerprint: 97b0da1333b1090e07b7b8c2
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received
- **present-perfect** · skills/asd-ste100/SKILL.md:81:140 · **recurring** · fingerprint: 87ac5857a6a44a6085f99a33
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has completed
- **synonym-rotation** · skills/asd-ste100/SKILL.md:88:192 · **recurring** · fingerprint: ce5400ef29dc517a20f612fc
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete
- **nominalization** · skills/asd-ste100/SKILL.md:89:56 · **recurring** · fingerprint: b0f99a99288209b64ca87fa8
  - **Level:** advisory-free
  - **Message:** Action frozen into a noun. Use the verb (analyze, not perform an analysis of).
  - **Matched text:** perform an analysis
- **marketing-adjective** · skills/asd-ste100/SKILL.md:90:79 · **recurring** · fingerprint: e376f8090861f51701cf8a19
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** seamless
- **marketing-adjective** · skills/asd-ste100/SKILL.md:90:89 · **recurring** · fingerprint: 0f33fa33abea44edf29a8632
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** robust
- **marketing-adjective** · skills/asd-ste100/SKILL.md:90:107 · **recurring** · fingerprint: b483bbe719cbd32778da4137
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** cutting-edge
- **marketing-adjective** · skills/asd-ste100/SKILL.md:90:121 · **recurring** · fingerprint: ea81b9a88d6189c3e9903c71
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** effortless
- **marketing-adjective** · skills/asd-ste100/SKILL.md:90:133 · **recurring** · fingerprint: c3ddafa9275694f20a349624
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** blazing-fast
- **phrasal-verb** · skills/asd-ste100/SKILL.md:92:29 · **recurring** · fingerprint: 4b3269c887ff5c340b1876ec
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** spin up
- **phrasal-verb** · skills/asd-ste100/SKILL.md:92:38 · **recurring** · fingerprint: b1d1a41a0e596b342bab207e
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** reach out
- **phrasal-verb** · skills/asd-ste100/SKILL.md:92:49 · **recurring** · fingerprint: d9e6e08d672f564d722faa69
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** dive into
- **phrasal-verb** · skills/asd-ste100/SKILL.md:92:60 · **recurring** · fingerprint: a17ca63c1abfe64d5e677484
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** kick off
- **present-perfect** · skills/asd-ste100/SKILL.md:113:134 · **recurring** · fingerprint: 95fa90f026478e1c3824ab91
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped
- **passive-voice** · skills/asd-ste100/SKILL.md:146:58 · **recurring** · fingerprint: 8f0e185b12ebc8ed1b2a84fa
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were memorized
- **passive-voice** · skills/philosophy-religion-asceticism/README.md:17:11 · **recurring** · fingerprint: 10fe19e3d918086368f3fe12
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are enabled
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:20:59 · **recurring** · fingerprint: 7da75daf64549a13157f1e48
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are copied
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:22:23 · **recurring** · fingerprint: e6d836749364fb952eddfc7c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is moved
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:33:3 · **recurring** · fingerprint: 1ca6476f6144a140274847f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are grouped
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:34:36 · **recurring** · fingerprint: 6bdb7fc4f6e61f46efdcc945
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are processed
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:45:16 · **recurring** · fingerprint: 7bb3ef8e29cc2d62ee65f3a9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are paired
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:46:35 · **recurring** · fingerprint: d15ccec8d9ae7c220e7297be
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:47:52 · **recurring** · fingerprint: 5fd7aabe55ed535b8e321fa7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are verified
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:53:17 · **recurring** · fingerprint: 3f8fc33d65f0a6d46cb838c6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:57:59 · **recurring** · fingerprint: 07f09cee503710d3a9b04228
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are excluded
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:59:23 · **recurring** · fingerprint: af22c155e8e4b4f9c84b3f86
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is cleared
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:59:57 · **recurring** · fingerprint: 67f2ed0983a75668f4ce3020
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is converted
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:60:51 · **recurring** · fingerprint: 0d3df0958eac71ea42f42c9c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are written
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:93:17 · **recurring** · fingerprint: fafc7dc70cfb6b41e2ceac4c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are allowed
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:94:72 · **recurring** · fingerprint: c93d49b6dfa2883ae7732733
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unresolved
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:98:39 · **recurring** · fingerprint: 9e3799d7fdb927485334ac92
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been uploaded
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:177:400 · **recurring** · fingerprint: 20086aa45dcb5efbabf52350
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were expected
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:196:37 · **recurring** · fingerprint: b6e92fd2ee8e3800eabf5dcd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paired
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:197:76 · **recurring** · fingerprint: a753d9aa8cfa9ae159dfcd57
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:208:26 · **recurring** · fingerprint: c6565434b3298d6e8f59aec5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **passive-voice** · skills/drawing/references/archive-and-delivery.md:212:1 · **recurring** · fingerprint: 4c20f74831abf9722cfbae81
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is described
- **passive-voice** · skills/github-actions/SKILL.md:21:206 · **recurring** · fingerprint: 0dc1e5055d6ed33dfbc9b5d4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are permitted
- **passive-voice** · skills/github-actions/SKILL.md:23:59 · **recurring** · fingerprint: f81ea4b00301347b2d2f1455
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided
- **present-perfect** · skills/github-actions/SKILL.md:33:40 · **recurring** · fingerprint: 701a297d4776256937ee58f6
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached
- **passive-voice** · skills/drawing/assets/attempt-template.md:61:53 · **recurring** · fingerprint: 54bc3060d325ed44b8a62ae3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · skills/drawing/references/patterns/successful-patterns.md:3:121 · **recurring** · fingerprint: 5e242a061496f40752e20b1c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are indexed
- **present-perfect** · skills/drawing/references/patterns/successful-patterns.md:25:23 · **recurring** · fingerprint: 0c43c9aefcafc776120c4656
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been tested
- **passive-voice** · skills/drawing/references/patterns/successful-patterns.md:25:27 · **recurring** · fingerprint: ab5c52aeee06db5e4aedaddd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested
- **passive-voice** · skills/drawing/references/patterns/successful-patterns.md:29:218 · **recurring** · fingerprint: 34e6d8f4282135e9b79d9cf1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were returned
- **passive-voice** · skills/drawing/references/patterns/successful-patterns.md:30:188 · **recurring** · fingerprint: 637ad15324468536b31ecfe4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reused
- **passive-voice** · skills/drawing/references/patterns/successful-patterns.md:47:158 · **recurring** · fingerprint: 2936d742ababd61bba5196c3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being requested
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:13:135 · **recurring** · fingerprint: 79b0a68b86133eedb422b851
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unresolved
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:19:83 · **recurring** · fingerprint: be7d514944589a18a9f9db9c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is disallowed
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:42:73 · **recurring** · fingerprint: 9f97b1e41f33db726c88c333
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unchanged
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:45:14 · **recurring** · fingerprint: f96d7c6c45b4119df93b13ed
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:47:74 · **recurring** · fingerprint: f96d7c6c45b4119df93b13ed
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:49:12 · **recurring** · fingerprint: 8defbd478033ef0db3a0b656
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was included
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:86:20 · **recurring** · fingerprint: f92adcede423eda0ec4d1115
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was attached
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:97:52 · **recurring** · fingerprint: b63bcf77584105d5ad091e1c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:119:29 · **recurring** · fingerprint: 9e98e3f9c31cb275ce90f3ae
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:123:77 · **recurring** · fingerprint: 160e46128e327497aa2a3a64
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was approved
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:155:37 · **recurring** · fingerprint: 746f4f3fe8422ec0ab0dde68
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:159:37 · **recurring** · fingerprint: f47cc4296d9e8a5663c8308c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:181:62 · **recurring** · fingerprint: 9375e59fa41686a4eb0bad2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was delivered
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:182:28 · **recurring** · fingerprint: 4b6f194f46882ca644424605
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:184:296 · **recurring** · fingerprint: 01d3ba03570b64cfafb32a81
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was generated
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:184:336 · **recurring** · fingerprint: 88fe09b5c3b3525804ef713a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been uploaded
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:185:31 · **recurring** · fingerprint: 4b6f194f46882ca644424605
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:186:26 · **recurring** · fingerprint: 5511c926d5a7460dc6f46cb9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unconfirmed
- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:205:20 · **recurring** · fingerprint: 8f0edbc69c4e47b3297c86ae
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is finalized
- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:12:63 · **recurring** · fingerprint: beabe60324ae752ed917a331
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:21:59 · **recurring** · fingerprint: f0ad12d293bae6f6df55998b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are copied
- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:23:16 · **recurring** · fingerprint: 606c590b44260c445b3f05a1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is moved
- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:45:38 · **recurring** · fingerprint: 5e247f9b617820d66c4e5de3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved
- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:50:11 · **recurring** · fingerprint: db9467f618e5d7170b5770de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reserved
- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:73:215 · **recurring** · fingerprint: 6ad1c8a942b901eb141a0cdc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Verified
- **synonym-rotation** · skills/session-archiving/references/image-provenance-and-webp.md:103:200 · **recurring** · fingerprint: e6e912834a84809148a29b28
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checking
- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:105:12 · **recurring** · fingerprint: 3d2774d90e6346c9f479ca23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is intended
- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:113:276 · **recurring** · fingerprint: ebe274c396fc6f6265e97091
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is updated
- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:122:37 · **recurring** · fingerprint: 28344c784d287164c52cc81d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paired
- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:123:76 · **recurring** · fingerprint: a8745ab59e15a54323b8eb62
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:134:26 · **recurring** · fingerprint: 756755bb5f5f39c5e328e481
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained
- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:138:1 · **recurring** · fingerprint: a22a1b959ff468a81a8c41ae
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is described
- **passive-voice** · skills/conversation-mode/SKILL.md:94:157 · **recurring** · fingerprint: 6d637f1fa2db2d41a6d50ddc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are ordered
- **passive-voice** · skills/conversation-mode/SKILL.md:105:72 · **recurring** · fingerprint: 448cf9dfd90fe327096b71e5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paused
- **passive-voice** · skills/conversation-mode/SKILL.md:110:41 · **recurring** · fingerprint: 24000f0d039ebc991f65530c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unresolved
- **passive-voice** · skills/conversation-mode/SKILL.md:137:88 · **recurring** · fingerprint: 448cf9dfd90fe327096b71e5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paused
- **present-perfect** · skills/conversation-mode/SKILL.md:138:78 · **recurring** · fingerprint: 11522f9e8c67a502b19046c1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped
- **present-perfect** · skills/conversation-mode/SKILL.md:138:108 · **recurring** · fingerprint: fb6ab971291fabec8f04e13d
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has proposed
- **passive-voice** · skills/conversation-mode/SKILL.md:139:61 · **recurring** · fingerprint: a5afffbd39db7eee0657c03b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/conversation-mode/SKILL.md:139:272 · **recurring** · fingerprint: 7432ab5664bf24b78cc7ff00
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is resolved
- **passive-voice** · skills/conversation-mode/SKILL.md:154:63 · **recurring** · fingerprint: a5afffbd39db7eee0657c03b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/conversation-mode/SKILL.md:159:36 · **recurring** · fingerprint: 3a6c1312d7b45107dbc72a9d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was encountered
- **passive-voice** · skills/conversation-mode/SKILL.md:161:106 · **recurring** · fingerprint: f524e4cf6f61106be53e395c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was verified
- **passive-voice** · skills/conversation-mode/SKILL.md:170:180 · **recurring** · fingerprint: 30999b2a0d67c2a1670763ff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded
- **passive-voice** · skills/conversation-mode/SKILL.md:196:260 · **recurring** · fingerprint: a5afffbd39db7eee0657c03b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **present-perfect** · skills/conversation-mode/SKILL.md:211:94 · **recurring** · fingerprint: 5b8f9ac16a3f5a3fd92e7621
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved
- **present-perfect** · skills/conversation-mode/SKILL.md:238:126 · **recurring** · fingerprint: 7e130dc07470c4dfc1de436d
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been given
- **passive-voice** · skills/conversation-mode/SKILL.md:238:130 · **recurring** · fingerprint: ef15c6245f889cbfdb09d89a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been given
- **passive-voice** · skills/conversation-mode/SKILL.md:259:75 · **recurring** · fingerprint: 04de33177ef6c58de34b6fd5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are governed
- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:7:89 · **recurring** · fingerprint: cd523ffc146c3f6901de60f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is designed
- **present-perfect** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:15:1 · **recurring** · fingerprint: d30efb69e80e577256521942
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been completed
- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:15:5 · **recurring** · fingerprint: 6ff3e39160ad0dff0950e93f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been completed
- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:20:13 · **recurring** · fingerprint: 50a2d483f4875f3fb2b04103
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is built
- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:37:47 · **recurring** · fingerprint: 375845a698662aa8e2119fb5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is used
- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:39:38 · **recurring** · fingerprint: 375845a698662aa8e2119fb5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is used
- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:57:65 · **recurring** · fingerprint: 4b337153e373889fb349022d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being used
- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:268:11 · **recurring** · fingerprint: 4b337153e373889fb349022d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being used
- **passive-voice** · skills/drawing/SKILL.md:107:69 · **recurring** · fingerprint: 64d3910316c7c02208869eec
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is requested
- **passive-voice** · skills/drawing/SKILL.md:180:77 · **recurring** · fingerprint: 9a01e5392bd2f640fccc16f8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is listed
- **passive-voice** · skills/drawing/SKILL.md:189:31 · **recurring** · fingerprint: ae959494a55d88be42e4abf1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is packaged
- **passive-voice** · skills/drawing/SKILL.md:207:35 · **recurring** · fingerprint: d87f3bdb2e4a5cd311e567e0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · skills/drawing/SKILL.md:208:27 · **recurring** · fingerprint: d87f3bdb2e4a5cd311e567e0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · skills/drawing/SKILL.md:209:35 · **recurring** · fingerprint: 4a1561330f4473854edf7d68
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been loaded
- **passive-voice** · skills/drawing/SKILL.md:216:76 · **recurring** · fingerprint: 83aca3a3f45f79d0190f037b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is maintained
- **passive-voice** · skills/drawing/SKILL.md:255:21 · **recurring** · fingerprint: 4adc0f726bafb883a943a4c7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are wanted
- **passive-voice** · skills/drawing/SKILL.md:259:15 · **recurring** · fingerprint: 182721976b7c74744cfa668b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored
- **long-sentence** · skills/drawing/SKILL.md:261:4 · **recurring** · fingerprint: d81568a6e2238902ee0c2105
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · skills/drawing/SKILL.md:276:5 · **recurring** · fingerprint: 1da08cc0bf141330524bda57
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **passive-voice** · skills/drawing/SKILL.md:319:378 · **recurring** · fingerprint: 182721976b7c74744cfa668b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored
- **passive-voice** · skills/drawing/SKILL.md:319:553 · **recurring** · fingerprint: 108fef94cd85af0be9bae737
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · skills/drawing/SKILL.md:394:23 · **recurring** · fingerprint: c13b1ec0df584f1d71453752
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are governed
- **passive-voice** · skills/drawing/SKILL.md:400:60 · **recurring** · fingerprint: 828f9104eb1934f156af2c49
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was used
- **passive-voice** · skills/drawing/SKILL.md:407:216 · **recurring** · fingerprint: 856947d77008b1a8011c64b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied
- **passive-voice** · skills/drawing/SKILL.md:424:19 · **recurring** · fingerprint: f7c61d976e048fc4d2187457
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is refused
- **passive-voice** · skills/drawing/SKILL.md:456:42 · **recurring** · fingerprint: 108fef94cd85af0be9bae737
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · skills/drawing/SKILL.md:457:50 · **recurring** · fingerprint: d518259c92d98a763deb57db
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was produced
- **passive-voice** · skills/drawing/SKILL.md:458:42 · **recurring** · fingerprint: a9eeb0708efad4ad4ebac5a3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · skills/drawing/SKILL.md:462:11 · **recurring** · fingerprint: 2ebc7cf088303cbfd5592603
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **synonym-rotation** · skills/drawing/SKILL.md:470:15 · **recurring** · fingerprint: aa2b4a16cd7d5222231207e6
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · skills/drawing/SKILL.md:489:24 · **recurring** · fingerprint: f6cfabada63cd4b942c2fdab
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are determined
- **passive-voice** · skills/drawing/SKILL.md:515:13 · **recurring** · fingerprint: 9ce13cb184b2103476d72b72
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Closed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:4:162 · **recurring** · fingerprint: 305e0414169478f6e310d27a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was truncated
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:4:254 · **recurring** · fingerprint: 1b362583f0b6f9564bc66dd0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were inspected
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:28:139 · **recurring** · fingerprint: 521a3f31bc54ec727caae5b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was found
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:33:453 · **recurring** · fingerprint: bcb83f45ddf38808e5512023
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being uploaded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:42:276 · **recurring** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:43:214 · **recurring** · fingerprint: a41ef6bbf64045f943d2af47
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:45:139 · **recurring** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:47:358 · **recurring** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:49:307 · **recurring** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **synonym-rotation** · skills/document-standards/references/document-type-catalog.md:52:264 · **recurring** · fingerprint: 2822a6b08706709830f1f820
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:64:165 · **recurring** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:64:176 · **recurring** · fingerprint: ea92de1fbbfc0e6cafa24f7b
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:83:39 · **recurring** · fingerprint: 0c06b4bea825bbb8305e2205
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were reviewed
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:88:200 · **recurring** · fingerprint: ea92de1fbbfc0e6cafa24f7b
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **present-perfect** · skills/document-standards/references/document-type-catalog.md:88:479 · **recurring** · fingerprint: 5bfc1af36a470f1f001188ee
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been approved
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:88:483 · **recurring** · fingerprint: c8520603dffa16dea8ea3dc4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been approved
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:89:136 · **recurring** · fingerprint: 6046357fc6d15e771a97e487
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are established
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:91:131 · **recurring** · fingerprint: f99656c38dfabd9bba499a0e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:91:206 · **recurring** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:92:199 · **recurring** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:94:262 · **recurring** · fingerprint: 95aef61741aad14590481dc3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is uploaded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:104:230 · **recurring** · fingerprint: 446871a6fecc2890373b2df1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:112:129 · **recurring** · fingerprint: 521a3f31bc54ec727caae5b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was found
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:127:203 · **recurring** · fingerprint: 32702bd5a2c5ca60292eca3a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are superseded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:134:57 · **recurring** · fingerprint: 9a67866b9f0335cac5eb0d64
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was required
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:140:123 · **recurring** · fingerprint: ec9e446045dd985aa0b168c4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are permitted
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:144:32 · **recurring** · fingerprint: d5a3d56f7803c8bd7fe2f5bb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added
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
- **passive-voice** · skills/drawing/references/style-guide.md:60:31 · **recurring** · fingerprint: 581a2555fa37c98ab6bcfea3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was classified
- **present-perfect** · skills/INITIALIZATION_POLICY.md:36:53 · **recurring** · fingerprint: 4f9e87e44f34528956cbd2f3
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been retrieved
- **passive-voice** · skills/INITIALIZATION_POLICY.md:36:57 · **recurring** · fingerprint: 25393e4ca29211513c0ea122
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved
- **long-sentence** · skills/drawing/assets/daily-index-template.md:5:1 · **recurring** · fingerprint: f7683dcec815fe504f98befb
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **passive-voice** · workspace/TASK_TEMPLATE.md:18:108 · **recurring** · fingerprint: 5275280719ed16d2a5b7ad67
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is written
- **passive-voice** · workspace/TASK_TEMPLATE.md:46:21 · **recurring** · fingerprint: fdc561df7864672b424ed481
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was inspected
- **synonym-rotation** · workspace/TASK_TEMPLATE.md:57:58 · **recurring** · fingerprint: e37028ed88b119b98fe16981
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **passive-voice** · workspace/TASK_TEMPLATE.md:73:20 · **recurring** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **passive-voice** · workspace/TASK_TEMPLATE.md:74:23 · **recurring** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:44:40 · **recurring** · fingerprint: 1438a8fae83f4cef43ff111f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is inferred
- **present-perfect** · skills/drawing/references/series-continuity-and-iteration.md:50:245 · **recurring** · fingerprint: 8dcbbc229f60c870064ba1c1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has declared
- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:78:42 · **recurring** · fingerprint: 37314d6abfb814d104e0fd33
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is ordered
- **present-perfect** · skills/drawing/references/series-continuity-and-iteration.md:82:259 · **recurring** · fingerprint: fd585a05866ee7a0cfc00d99
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has established
- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:94:27 · **recurring** · fingerprint: eeef7c60d434b3d4f60ce329
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are locked
- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:134:15 · **recurring** · fingerprint: 0854ae12d93b6bb158c85528
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:140:14 · **recurring** · fingerprint: 0854ae12d93b6bb158c85528
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:164:73 · **recurring** · fingerprint: 602406a24344ba12b85a3c26
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being edited
- **synonym-rotation** · skills/drawing/references/series-continuity-and-iteration.md:177:31 · **recurring** · fingerprint: 284ad5169b785d0b95212ad0
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:177:77 · **recurring** · fingerprint: 6bead85653574df77128e560
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was attached
- **present-perfect** · skills/asd-ste100/references/writing-rules.md:7:511 · **recurring** · fingerprint: b41b3daad40ce14cd376bd73
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been
- **present-perfect** · skills/asd-ste100/references/writing-rules.md:26:84 · **recurring** · fingerprint: 4b5ee50f1aff2b6dcc346552
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received
- **passive-voice** · skills/asd-ste100/references/writing-rules.md:26:129 · **recurring** · fingerprint: bb10a66696f9dabc2249dc8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is allowed
- **passive-voice** · skills/asd-ste100/references/writing-rules.md:27:16 · **recurring** · fingerprint: ac3ecaa3996b4c54c0d3e834
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are permitted
- **passive-voice** · skills/asd-ste100/references/writing-rules.md:30:16 · **recurring** · fingerprint: 773da2a0fc01b2b8333a892c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · skills/asd-ste100/references/writing-rules.md:31:17 · **recurring** · fingerprint: bb10a66696f9dabc2249dc8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is allowed
- **passive-voice** · skills/asd-ste100/references/writing-rules.md:37:58 · **recurring** · fingerprint: 4905d0267d2de525570a8af5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are capped
- **passive-voice** · skills/asd-ste100/references/writing-rules.md:50:5 · **recurring** · fingerprint: 2b19e1e9387f5374b63a7c1f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was designed
- **passive-voice** · skills/philosophy-religion-asceticism/references/answer-patterns.md:29:14 · **recurring** · fingerprint: c179db648027812a0a97ede9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is contested
- **present-perfect** · workspace/README.md:25:469 · **recurring** · fingerprint: 4ad77a0e3e15f5d60871f4fe
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has triggered
- **present-perfect** · workspace/README.md:56:22 · **recurring** · fingerprint: 2769f0f695083967627c85d2
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has started
- **passive-voice** · skills/the-worker/SKILL.md:31:133 · **recurring** · fingerprint: 718d67ec20c921c3c043a464
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unverified
- **passive-voice** · skills/the-worker/SKILL.md:58:61 · **recurring** · fingerprint: 0eebcb0484fe67c4e2017ecc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided
- **passive-voice** · skills/the-worker/SKILL.md:75:111 · **recurring** · fingerprint: d226740cae172dd2e1c78d14
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **present-perfect** · skills/the-worker/SKILL.md:290:168 · **recurring** · fingerprint: 0e07f428da579362c55d461b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been verified
- **passive-voice** · skills/the-worker/SKILL.md:290:172 · **recurring** · fingerprint: b6cbb5b662b7ac93ef3ba05e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified
- **passive-voice** · skills/session-archiving/references/drawing-session-closeout.md:17:227 · **recurring** · fingerprint: 5c4029a4459ae6a7419ec7c9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Closed
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:13:64 · **recurring** · fingerprint: 57efc2fd300bb9b7a8310db5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is curated
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:29:8 · **recurring** · fingerprint: b42e4986c1414564f3a43dfe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was completed
- **synonym-rotation** · skills/session-archiving/references/archive-records-and-image-prompts.md:49:20 · **recurring** · fingerprint: 5d54d956f78d455711c2a358
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:84:21 · **recurring** · fingerprint: 1e36a113c65e15f12385ea65
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being discussed
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:93:11 · **recurring** · fingerprint: 23d11d13b31395d30d56f69c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are limited
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:121:164 · **recurring** · fingerprint: f5645cb699f537e6560fec11
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:124:130 · **recurring** · fingerprint: 27f21c0fcee319d11c62095b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:128:343 · **recurring** · fingerprint: c5e47aa80ee8e7135454cf5b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:186:170 · **recurring** · fingerprint: ba19e482eb53d060d32f3713
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was supplied
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:189:23 · **recurring** · fingerprint: 1d0aa41a6bd9ae288874e8d0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being tested
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:227:65 · **recurring** · fingerprint: 77657ae524bd6ec941b3e366
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:238:24 · **recurring** · fingerprint: 8c39463eb3e977779ed45cf7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:255:28 · **recurring** · fingerprint: 0fa85e814db12cfbf0b20231
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was attached
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:267:33 · **recurring** · fingerprint: ba19e482eb53d060d32f3713
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was supplied
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:282:44 · **recurring** · fingerprint: 9f3e8f0bc0fbdd6524b3656a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was created
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:292:68 · **recurring** · fingerprint: 493149180e6121959865622c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was delivered
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:293:36 · **recurring** · fingerprint: 77657ae524bd6ec941b3e366
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:293:58 · **recurring** · fingerprint: 2b09f88ca19a5527995c7947
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unverified
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:296:4 · **recurring** · fingerprint: b8f9a093dcad37186a759350
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is uploaded
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:297:78 · **recurring** · fingerprint: 0975b3ba84ad7cb994974ee5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:298:48 · **recurring** · fingerprint: e48495019965c18ff0c22b95
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was generated
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:299:75 · **recurring** · fingerprint: 77657ae524bd6ec941b3e366
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:300:68 · **recurring** · fingerprint: 55f138238adaad7251236fe2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unconfirmed
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:310:20 · **recurring** · fingerprint: 2868b703139e25825d4a9b8a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is finalized
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:314:53 · **recurring** · fingerprint: 009936d66fee55cde90f5887
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is renamed
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:336:242 · **recurring** · fingerprint: 80f2107125cb88de9fe1f2d7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:338:35 · **recurring** · fingerprint: 695e4b770f91de2ff1b14f54
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored
- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:385:69 · **recurring** · fingerprint: 424f162bb288d4ec5598118a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is based
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:13:215 · **recurring** · fingerprint: 404693192feb5c0a1bc279e9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is measured
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:15:69 · **recurring** · fingerprint: ccf5d0ae1e3ac5dfa3d81535
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are retained
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:46:115 · **recurring** · fingerprint: 620b7d7fd1d18757b7cf5e84
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is phrased
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:56:24 · **recurring** · fingerprint: dbd3657662996413f5b3e09d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been approved
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:62:24 · **recurring** · fingerprint: 0b65a30e1dc02ac864748bce
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has rejected
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:74:32 · **recurring** · fingerprint: f40577f4f87280d2bafbbb33
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are prohibited
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:80:35 · **recurring** · fingerprint: 1439db2c98d70c1af24c7cd4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being limited
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:89:141 · **recurring** · fingerprint: ca6cd5747867ae19c46def89
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been established
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:91:171 · **recurring** · fingerprint: f1f73777ecdc15c96cdcd383
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are covered
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:116:33 · **recurring** · fingerprint: c31471d539e8aa39ed2d47c3
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has specified
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:119:41 · **recurring** · fingerprint: 3238ce4831a0652078d996e0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is depicted
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:127:120 · **recurring** · fingerprint: 942e61ff7b0fb459a13ad0d1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unspecified
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:127:168 · **recurring** · fingerprint: af345c449e8933426d2e19fe
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has delegated
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:151:163 · **recurring** · fingerprint: af345c449e8933426d2e19fe
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has delegated
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:198:141 · **recurring** · fingerprint: b7f3317fff8f1ff3b74412df
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:225:75 · **recurring** · fingerprint: 0b65a30e1dc02ac864748bce
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has rejected
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:244:41 · **recurring** · fingerprint: 292fbd9b5ed50c5247cf2f53
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been restored
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:245:103 · **recurring** · fingerprint: 5ea0ac18f64fc9ba3c3b6b6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been added
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:246:33 · **recurring** · fingerprint: 8233e35bff35faaf38a980b8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been paraphrased
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:247:123 · **recurring** · fingerprint: 753e3e43156f685672332845
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been introduced
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:248:42 · **recurring** · fingerprint: 97a20fbdbe0577e454aefdc8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been preserved
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:249:26 · **recurring** · fingerprint: 13f4a5392eedebe0585ee245
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been limited
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:250:23 · **recurring** · fingerprint: b49d5e45b1b3b1c0140fab39
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been converted
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:265:66 · **recurring** · fingerprint: 278f5a301dede82f4c8ac412
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being submitted
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:268:30 · **recurring** · fingerprint: d88beccb64f34579d80979ff
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been archived
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:268:34 · **recurring** · fingerprint: 8e48ea2de3c2f37bc3a96546
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been archived
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:270:46 · **recurring** · fingerprint: 40f2dda08cf8d4e026bc1cf8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exposed
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:272:98 · **recurring** · fingerprint: 7166cf5d9d622916649b0f8d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was submitted
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:272:197 · **recurring** · fingerprint: 403d89805494afd57b827dee
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was authorized
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:289:87 · **recurring** · fingerprint: af345c449e8933426d2e19fe
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has delegated
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:300:57 · **recurring** · fingerprint: 4e3b443eb033832d17dc8545
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been checked
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:300:62 · **recurring** · fingerprint: bdcbc53fefbff59427750156
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been checked
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:301:99 · **recurring** · fingerprint: 8854a5a70b9be9bbffa72e61
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preserved
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:302:41 · **recurring** · fingerprint: 83c2d80059f94672d8a71141
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been introduced
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:302:46 · **recurring** · fingerprint: 753e3e43156f685672332845
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been introduced
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:303:106 · **recurring** · fingerprint: 3115ca2ae7a235e7560a1cbc
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been added
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:303:111 · **recurring** · fingerprint: 5ea0ac18f64fc9ba3c3b6b6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been added
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:304:31 · **recurring** · fingerprint: c60448dfacfff81b45010545
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been restored
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:304:35 · **recurring** · fingerprint: 292fbd9b5ed50c5247cf2f53
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been restored
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:306:58 · **recurring** · fingerprint: ebc3fe4b7983f2625cff09c5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been audited
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:306:62 · **recurring** · fingerprint: 847f9b53906e7b622acde414
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been audited
- **present-perfect** · skills/drawing/references/prompt-fidelity.md:307:27 · **recurring** · fingerprint: 1f52364af2f7476db43a8cf5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been removed
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:307:31 · **recurring** · fingerprint: 4fa531795b4f48c712cb9b8f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been removed
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:309:42 · **recurring** · fingerprint: dc5ac767caa168e0bfb3a0be
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is assigned
- **passive-voice** · skills/drawing/references/prompt-fidelity.md:309:73 · **recurring** · fingerprint: 2684dd7826880335bb93b3ce
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was copied
- **synonym-rotation** · skills/drawing/references/prompt-fidelity.md:315:156 · **recurring** · fingerprint: c784915b81aefed48004e9cb
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'retrieve' name the same action. Pick one and use it every time.
  - **Matched text:** fetch
- **passive-voice** · skills/document-standards/SKILL.md:75:47 · **recurring** · fingerprint: f02e1c27fdc79f6921bf2e16
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **passive-voice** · skills/document-standards/SKILL.md:197:37 · **recurring** · fingerprint: da830431b494f6dd663885a4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is defined
- **passive-voice** · skills/session-archiving/SKILL.md:80:90 · **recurring** · fingerprint: 038292fe0c13c6199af4bf3a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known
- **passive-voice** · skills/session-archiving/SKILL.md:134:41 · **recurring** · fingerprint: 99dd9dc8b35e76013c9dd169
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is mentioned
- **passive-voice** · skills/session-archiving/SKILL.md:142:408 · **recurring** · fingerprint: 2779f560ab6e00a4b9a36994
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided
- **long-sentence** · skills/session-archiving/assets/session-brief-template.md:5:1 · **recurring** · fingerprint: 9edc4fb8b393050df4a8fe30
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words
- **present-perfect** · skills/SESSION_START.md:18:114 · **recurring** · fingerprint: 9acf80e5a2b48047e9dd619f
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been retrieved
- **passive-voice** · skills/SESSION_START.md:18:119 · **recurring** · fingerprint: fec2fb4fa450910b68502f34
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved
- **passive-voice** · skills/drawing/references/patterns/README.md:34:143 · **recurring** · fingerprint: f9d42240cfb6f779e60dcd02
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded

### Resolved findings

- **semicolon** · skills/INITIALIZATION_POLICY.md:132:288 · **resolved** · fingerprint: b28796101e8a0d8165b3d79b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 166
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/philosophy-religion-asceticism/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 8
- **Hard findings:** 0
- **Baseline:** 7
- **Words:** 2387
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:53:21 · **recurring** · fingerprint: fc114dacae449b7519133918
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:94:11 · **recurring** · fingerprint: 01b04df4a4d61aa32756adf1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is disputed

- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:144:43 · **recurring** · fingerprint: f05c498f9ee2269430ff8ada
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are related

- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:167:67 · **recurring** · fingerprint: c645e65b81e4110faf6f2062
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is contested

- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:178:68 · **recurring** · fingerprint: b1d63c43c6349bc6f120ce18
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is supported

- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:179:43 · **recurring** · fingerprint: 671a7eda510ef040edd3be61
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being asked

- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:291:3 · **recurring** · fingerprint: ac33fd0d35779883eb5af2cb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been excluded

- **passive-voice** · skills/philosophy-religion-asceticism/SKILL.md:292:52 · **recurring** · fingerprint: cd2a130c88bf1b1de364eda1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been kept


### skills/session-archiving/assets/conversation-integrity-template.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 192
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/drawing/references/patterns/failure-patterns.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 25
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 2146
- **Findings per 100 words:** 1.2

#### Complete diagnostics

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:3:126 · **recurring** · fingerprint: ba15e2b13749f7aad6447fc1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are indexed

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:5:65 · **recurring** · fingerprint: fb05b158f323ac0a88758170
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are kept

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:19:163 · **recurring** · fingerprint: 7cb850c3e4335a13e7519ba0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is reversed

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:22:89 · **recurring** · fingerprint: ce25d5ad6ba4826e11264f32
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is observed

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:37:14 · **recurring** · fingerprint: 32467609b8c42805cbf2c5ad
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is concentrated

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:48:20 · **recurring** · fingerprint: e1de4bab2e607823412ffbc4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were described

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:51:37 · **recurring** · fingerprint: ac6348f1c31c27d904cb53b4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was modified

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:61:190 · **recurring** · fingerprint: b49561bafa5675d60cc907c5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was attached

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:61:219 · **recurring** · fingerprint: 346827f54f442c607e8b24a5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:85:19 · **recurring** · fingerprint: ede5e693c6707a81cfe3079a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:91:257 · **recurring** · fingerprint: 3c48312b0ae19adb3273832c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:120:226 · **recurring** · fingerprint: e0e662058459fdceb4c02481
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was identified

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:136:66 · **recurring** · fingerprint: 715e2eee6cf5d1784b75c730
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is prepared

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:154:172 · **recurring** · fingerprint: c5308af1d2f63badad79bd66
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was tested

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:165:92 · **recurring** · fingerprint: 74cd4ed7e5ca2631c57c069b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:168:20 · **recurring** · fingerprint: 3c48312b0ae19adb3273832c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:183:164 · **recurring** · fingerprint: ede5e693c6707a81cfe3079a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established

- **present-perfect** · skills/drawing/references/patterns/failure-patterns.md:194:52 · **recurring** · fingerprint: fca6bef2ba2e441b581fcc8d
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has corrected

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:209:228 · **recurring** · fingerprint: 75eccc37cbac9985f7061f82
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was removed

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:209:266 · **recurring** · fingerprint: e56ece3c0f60be33dac72d05
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was preserved

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:210:242 · **recurring** · fingerprint: 5b28443dc965cf5ab3378e12
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was adopted

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:214:32 · **recurring** · fingerprint: b35900a9da7c000de2e26e70
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is maintained

- **present-perfect** · skills/drawing/references/patterns/failure-patterns.md:218:179 · **recurring** · fingerprint: feb2d786d14c99b7e9fe9de0
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has rejected

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:224:30 · **recurring** · fingerprint: 0cae9b0c6170006a0e67edc2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is included

- **passive-voice** · skills/drawing/references/patterns/failure-patterns.md:250:20 · **recurring** · fingerprint: b35900a9da7c000de2e26e70
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is maintained


### skills/agent-skill-authoring/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 17
- **Hard findings:** 1
- **Baseline:** 6
- **Words:** 2259
- **Findings per 100 words:** 0.8

#### Complete diagnostics

- **passive-voice** · skills/agent-skill-authoring/SKILL.md:14:79 · **recurring** · fingerprint: cf9a19441f150cbc6e394584
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are created

- **passive-voice** · skills/agent-skill-authoring/SKILL.md:160:29 · **recurring** · fingerprint: 6ffc592c0b6322b443496f66
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded

- **passive-voice** · skills/agent-skill-authoring/SKILL.md:163:106 · **recurring** · fingerprint: 6ffc592c0b6322b443496f66
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded

- **passive-voice** · skills/agent-skill-authoring/SKILL.md:167:23 · **recurring** · fingerprint: 6ffc592c0b6322b443496f66
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is loaded

- **present-perfect** · skills/agent-skill-authoring/SKILL.md:171:149 · **recurring** · fingerprint: 2dddc1891d5710f75a1cc520
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been loaded

- **passive-voice** · skills/agent-skill-authoring/SKILL.md:171:153 · **recurring** · fingerprint: f7fae0229a13471823102bb0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been loaded

- **passive-voice** · skills/agent-skill-authoring/SKILL.md:184:36 · **recurring** · fingerprint: 0be774910939027b005107b8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known

- **passive-voice** · skills/agent-skill-authoring/SKILL.md:222:38 · **recurring** · fingerprint: 5eabd6169bec15a6fdfd2a80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been created

- **synonym-rotation** · skills/agent-skill-authoring/SKILL.md:231:18 · **recurring** · fingerprint: cdded221cb31c45f9059249a
  - **Level:** advisory-free
  - **Message:** 'begin' and 'start' name the same action. Pick one and use it every time.
  - **Matched text:** begins

- **passive-voice** · skills/agent-skill-authoring/SKILL.md:244:28 · **recurring** · fingerprint: 0f053c89c3267998b6edc9d6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are focused

- **present-perfect** · skills/agent-skill-authoring/SKILL.md:245:65 · **recurring** · fingerprint: 70dc63b30d658452239a6cbe
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been introduced

- **passive-voice** · skills/agent-skill-authoring/SKILL.md:245:70 · **recurring** · fingerprint: 2df378472bba68cfc7a25cbe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been introduced

- **passive-voice** · skills/agent-skill-authoring/SKILL.md:253:17 · **recurring** · fingerprint: 8416fa6ec8b8068d6f7379c2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is connected

- **present-perfect** · skills/agent-skill-authoring/SKILL.md:255:37 · **recurring** · fingerprint: c26f9840d6188237d9689546
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been made

- **passive-voice** · skills/agent-skill-authoring/SKILL.md:255:41 · **recurring** · fingerprint: 599292fe4dd9cfdbc4788ec9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been made

- **present-perfect** · skills/agent-skill-authoring/SKILL.md:257:32 · **recurring** · fingerprint: 4414015699cf2e3e269abe29
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read

- **passive-voice** · skills/agent-skill-authoring/SKILL.md:257:36 · **recurring** · fingerprint: 91d321a9405d06bea4b12487
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read


### skills/asd-ste100/references/repository-writing-policy.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 570
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · skills/asd-ste100/references/repository-writing-policy.md:18:36 · **recurring** · fingerprint: 3ae757460d9b3aa9399e9808
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known


### skills/philosophy-religion-asceticism/references/source-standards.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 2
- **Hard findings:** 0
- **Baseline:** 1
- **Words:** 1467
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **passive-voice** · skills/philosophy-religion-asceticism/references/source-standards.md:99:19 · **recurring** · fingerprint: ce4f5586a0c66bf136f1a181
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being discussed

- **passive-voice** · skills/philosophy-religion-asceticism/references/source-standards.md:194:41 · **recurring** · fingerprint: 16921dc530cca16c2f4562e8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being cited


### skills/asd-ste100/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 2
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 1534
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **passive-voice** · skills/asd-ste100/README.md:26:35 · **recurring** · fingerprint: dc6fc135735cd3aa5f4246ff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known

- **passive-voice** · skills/asd-ste100/README.md:40:109 · **recurring** · fingerprint: bdbff79e00c0aca5352dcc38
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved


### skills/asd-ste100/assets/lint-report-template.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 385
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/drawing/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 396
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/drawing/assets/pattern-entry-templates.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 7
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 449
- **Findings per 100 words:** 1.6

#### Complete diagnostics

- **passive-voice** · skills/drawing/assets/pattern-entry-templates.md:17:40 · **recurring** · fingerprint: 80ff0d75ee9e57c63a759659
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retired

- **passive-voice** · skills/drawing/assets/pattern-entry-templates.md:18:125 · **recurring** · fingerprint: e71b3a8ba6751987cf0fb966
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are verified

- **passive-voice** · skills/drawing/assets/pattern-entry-templates.md:22:67 · **recurring** · fingerprint: 4cca9a878a87bc55497611c8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **present-perfect** · skills/drawing/assets/pattern-entry-templates.md:100:246 · **recurring** · fingerprint: ad46045395dc40b74a35f499
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has tested

- **passive-voice** · skills/drawing/assets/pattern-entry-templates.md:111:20 · **recurring** · fingerprint: 92485eeff29784dba3505b2d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are separated

- **passive-voice** · skills/drawing/assets/pattern-entry-templates.md:113:15 · **recurring** · fingerprint: 3f5048026fc0041e11f90db1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are described

- **passive-voice** · skills/drawing/assets/pattern-entry-templates.md:115:19 · **recurring** · fingerprint: 9a512eba16db074bc582887d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded


### images/takeout/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 1397
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **passive-voice** · images/takeout/README.md:180:40 · **recurring** · fingerprint: bf5f3ed6bfe52608af6f2cbb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reserved


### images/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 584
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · images/README.md:94:54 · **recurring** · fingerprint: 03c08438c1205e007605fad3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reserved


### skills/asd-ste100/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 21
- **Hard findings:** 13
- **Baseline:** 31
- **Words:** 2609
- **Findings per 100 words:** 0.8

#### Complete diagnostics

- **passive-voice** · skills/asd-ste100/SKILL.md:21:69 · **recurring** · fingerprint: 7266e62fe12e7cc92f88c06b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was violated

- **passive-voice** · skills/asd-ste100/SKILL.md:49:227 · **recurring** · fingerprint: 4e26f8ad5ee76bbe5f532dd1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are defined

- **passive-voice** · skills/asd-ste100/SKILL.md:57:60 · **recurring** · fingerprint: 0447fbf776081d483d4a8de4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is removed

- **phrasal-verb** · skills/asd-ste100/SKILL.md:58:99 · **recurring** · fingerprint: bc3fa2e84f1094e34446f7f9
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** Spin up

- **passive-voice** · skills/asd-ste100/SKILL.md:73:118 · **recurring** · fingerprint: 081cea6a0061b9dd44d263e8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved

- **nominalization** · skills/asd-ste100/SKILL.md:74:53 · **recurring** · fingerprint: f17e13a684f76bb434777eb7
  - **Level:** advisory-free
  - **Message:** Action frozen into a noun. Use the verb (analyze, not perform an analysis of).
  - **Matched text:** Perform an analysis

- **present-perfect** · skills/asd-ste100/SKILL.md:79:203 · **recurring** · fingerprint: 97b0da1333b1090e07b7b8c2
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received

- **present-perfect** · skills/asd-ste100/SKILL.md:81:140 · **recurring** · fingerprint: 87ac5857a6a44a6085f99a33
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has completed

- **synonym-rotation** · skills/asd-ste100/SKILL.md:88:192 · **recurring** · fingerprint: ce5400ef29dc517a20f612fc
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** delete

- **nominalization** · skills/asd-ste100/SKILL.md:89:56 · **recurring** · fingerprint: b0f99a99288209b64ca87fa8
  - **Level:** advisory-free
  - **Message:** Action frozen into a noun. Use the verb (analyze, not perform an analysis of).
  - **Matched text:** perform an analysis

- **marketing-adjective** · skills/asd-ste100/SKILL.md:90:79 · **recurring** · fingerprint: e376f8090861f51701cf8a19
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** seamless

- **marketing-adjective** · skills/asd-ste100/SKILL.md:90:89 · **recurring** · fingerprint: 0f33fa33abea44edf29a8632
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** robust

- **marketing-adjective** · skills/asd-ste100/SKILL.md:90:107 · **recurring** · fingerprint: b483bbe719cbd32778da4137
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** cutting-edge

- **marketing-adjective** · skills/asd-ste100/SKILL.md:90:121 · **recurring** · fingerprint: ea81b9a88d6189c3e9903c71
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** effortless

- **marketing-adjective** · skills/asd-ste100/SKILL.md:90:133 · **recurring** · fingerprint: c3ddafa9275694f20a349624
  - **Level:** advisory-free
  - **Message:** Marketing adjective. Delete, or replace with the measurement that earns the claim.
  - **Matched text:** blazing-fast

- **phrasal-verb** · skills/asd-ste100/SKILL.md:92:29 · **recurring** · fingerprint: 4b3269c887ff5c340b1876ec
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** spin up

- **phrasal-verb** · skills/asd-ste100/SKILL.md:92:38 · **recurring** · fingerprint: b1d1a41a0e596b342bab207e
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** reach out

- **phrasal-verb** · skills/asd-ste100/SKILL.md:92:49 · **recurring** · fingerprint: d9e6e08d672f564d722faa69
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** dive into

- **phrasal-verb** · skills/asd-ste100/SKILL.md:92:60 · **recurring** · fingerprint: a17ca63c1abfe64d5e677484
  - **Level:** advisory-free
  - **Message:** Soft phrasal verb. Use the single plain verb (start, contact, read, begin).
  - **Matched text:** kick off

- **present-perfect** · skills/asd-ste100/SKILL.md:113:134 · **recurring** · fingerprint: 95fa90f026478e1c3824ab91
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped

- **passive-voice** · skills/asd-ste100/SKILL.md:146:58 · **recurring** · fingerprint: 8f0e185b12ebc8ed1b2a84fa
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were memorized


### skills/philosophy-religion-asceticism/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 471
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · skills/philosophy-religion-asceticism/README.md:17:11 · **recurring** · fingerprint: 10fe19e3d918086368f3fe12
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are enabled


### skills/drawing/references/archive-and-delivery.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 20
- **Hard findings:** 0
- **Baseline:** 7
- **Words:** 2370
- **Findings per 100 words:** 0.8

#### Complete diagnostics

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:20:59 · **recurring** · fingerprint: 7da75daf64549a13157f1e48
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are copied

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:22:23 · **recurring** · fingerprint: e6d836749364fb952eddfc7c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is moved

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:33:3 · **recurring** · fingerprint: 1ca6476f6144a140274847f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are grouped

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:34:36 · **recurring** · fingerprint: 6bdb7fc4f6e61f46efdcc945
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are processed

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:45:16 · **recurring** · fingerprint: 7bb3ef8e29cc2d62ee65f3a9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are paired

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:46:35 · **recurring** · fingerprint: d15ccec8d9ae7c220e7297be
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:47:52 · **recurring** · fingerprint: 5fd7aabe55ed535b8e321fa7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are verified

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:53:17 · **recurring** · fingerprint: 3f8fc33d65f0a6d46cb838c6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:57:59 · **recurring** · fingerprint: 07f09cee503710d3a9b04228
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are excluded

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:59:23 · **recurring** · fingerprint: af22c155e8e4b4f9c84b3f86
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is cleared

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:59:57 · **recurring** · fingerprint: 67f2ed0983a75668f4ce3020
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is converted

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:60:51 · **recurring** · fingerprint: 0d3df0958eac71ea42f42c9c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are written

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:93:17 · **recurring** · fingerprint: fafc7dc70cfb6b41e2ceac4c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are allowed

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:94:72 · **recurring** · fingerprint: c93d49b6dfa2883ae7732733
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unresolved

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:98:39 · **recurring** · fingerprint: 9e3799d7fdb927485334ac92
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been uploaded

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:177:400 · **recurring** · fingerprint: 20086aa45dcb5efbabf52350
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were expected

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:196:37 · **recurring** · fingerprint: b6e92fd2ee8e3800eabf5dcd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paired

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:197:76 · **recurring** · fingerprint: a753d9aa8cfa9ae159dfcd57
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:208:26 · **recurring** · fingerprint: c6565434b3298d6e8f59aec5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained

- **passive-voice** · skills/drawing/references/archive-and-delivery.md:212:1 · **recurring** · fingerprint: 4c20f74831abf9722cfbae81
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is described


### skills/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 371
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/github-actions/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 3
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 2534
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **passive-voice** · skills/github-actions/SKILL.md:21:206 · **recurring** · fingerprint: 0dc1e5055d6ed33dfbc9b5d4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are permitted

- **passive-voice** · skills/github-actions/SKILL.md:23:59 · **recurring** · fingerprint: f81ea4b00301347b2d2f1455
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided

- **present-perfect** · skills/github-actions/SKILL.md:33:40 · **recurring** · fingerprint: 701a297d4776256937ee58f6
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have reached


### skills/drawing/assets/attempt-template.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 593
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · skills/drawing/assets/attempt-template.md:61:53 · **recurring** · fingerprint: 54bc3060d325ed44b8a62ae3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned


### skills/drawing/references/patterns/successful-patterns.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 6
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 816
- **Findings per 100 words:** 0.7

#### Complete diagnostics

- **passive-voice** · skills/drawing/references/patterns/successful-patterns.md:3:121 · **recurring** · fingerprint: 5e242a061496f40752e20b1c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are indexed

- **present-perfect** · skills/drawing/references/patterns/successful-patterns.md:25:23 · **recurring** · fingerprint: 0c43c9aefcafc776120c4656
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been tested

- **passive-voice** · skills/drawing/references/patterns/successful-patterns.md:25:27 · **recurring** · fingerprint: ab5c52aeee06db5e4aedaddd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been tested

- **passive-voice** · skills/drawing/references/patterns/successful-patterns.md:29:218 · **recurring** · fingerprint: 34e6d8f4282135e9b79d9cf1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were returned

- **passive-voice** · skills/drawing/references/patterns/successful-patterns.md:30:188 · **recurring** · fingerprint: 637ad15324468536b31ecfe4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reused

- **passive-voice** · skills/drawing/references/patterns/successful-patterns.md:47:158 · **recurring** · fingerprint: 2936d742ababd61bba5196c3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being requested


### skills/drawing/references/generation-recovery-and-provenance.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 19
- **Hard findings:** 0
- **Baseline:** 17
- **Words:** 2757
- **Findings per 100 words:** 0.7

#### Complete diagnostics

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:13:135 · **recurring** · fingerprint: 79b0a68b86133eedb422b851
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unresolved

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:19:83 · **recurring** · fingerprint: be7d514944589a18a9f9db9c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is disallowed

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:42:73 · **recurring** · fingerprint: 9f97b1e41f33db726c88c333
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unchanged

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:45:14 · **recurring** · fingerprint: f96d7c6c45b4119df93b13ed
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:47:74 · **recurring** · fingerprint: f96d7c6c45b4119df93b13ed
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:49:12 · **recurring** · fingerprint: 8defbd478033ef0db3a0b656
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was included

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:86:20 · **recurring** · fingerprint: f92adcede423eda0ec4d1115
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was attached

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:97:52 · **recurring** · fingerprint: b63bcf77584105d5ad091e1c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:119:29 · **recurring** · fingerprint: 9e98e3f9c31cb275ce90f3ae
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:123:77 · **recurring** · fingerprint: 160e46128e327497aa2a3a64
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was approved

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:155:37 · **recurring** · fingerprint: 746f4f3fe8422ec0ab0dde68
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is archived

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:159:37 · **recurring** · fingerprint: f47cc4296d9e8a5663c8308c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:181:62 · **recurring** · fingerprint: 9375e59fa41686a4eb0bad2a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was delivered

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:182:28 · **recurring** · fingerprint: 4b6f194f46882ca644424605
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:184:296 · **recurring** · fingerprint: 01d3ba03570b64cfafb32a81
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was generated

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:184:336 · **recurring** · fingerprint: 88fe09b5c3b3525804ef713a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been uploaded

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:185:31 · **recurring** · fingerprint: 4b6f194f46882ca644424605
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:186:26 · **recurring** · fingerprint: 5511c926d5a7460dc6f46cb9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unconfirmed

- **passive-voice** · skills/drawing/references/generation-recovery-and-provenance.md:205:20 · **recurring** · fingerprint: 8f0edbc69c4e47b3297c86ae
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is finalized


### skills/session-archiving/references/image-provenance-and-webp.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 13
- **Hard findings:** 1
- **Baseline:** 2
- **Words:** 1710
- **Findings per 100 words:** 0.8

#### Complete diagnostics

- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:12:63 · **recurring** · fingerprint: beabe60324ae752ed917a331
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:21:59 · **recurring** · fingerprint: f0ad12d293bae6f6df55998b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are copied

- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:23:16 · **recurring** · fingerprint: 606c590b44260c445b3f05a1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is moved

- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:45:38 · **recurring** · fingerprint: 5e247f9b617820d66c4e5de3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is preserved

- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:50:11 · **recurring** · fingerprint: db9467f618e5d7170b5770de
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reserved

- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:73:215 · **recurring** · fingerprint: 6ad1c8a942b901eb141a0cdc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Verified

- **synonym-rotation** · skills/session-archiving/references/image-provenance-and-webp.md:103:200 · **recurring** · fingerprint: e6e912834a84809148a29b28
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checking

- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:105:12 · **recurring** · fingerprint: 3d2774d90e6346c9f479ca23
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is intended

- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:113:276 · **recurring** · fingerprint: ebe274c396fc6f6265e97091
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is updated

- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:122:37 · **recurring** · fingerprint: 28344c784d287164c52cc81d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paired

- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:123:76 · **recurring** · fingerprint: a8745ab59e15a54323b8eb62
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:134:26 · **recurring** · fingerprint: 756755bb5f5f39c5e328e481
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is retained

- **passive-voice** · skills/session-archiving/references/image-provenance-and-webp.md:138:1 · **recurring** · fingerprint: a22a1b959ff468a81a8c41ae
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is described


### skills/conversation-mode/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 17
- **Hard findings:** 0
- **Baseline:** 3
- **Words:** 3080
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **passive-voice** · skills/conversation-mode/SKILL.md:94:157 · **recurring** · fingerprint: 6d637f1fa2db2d41a6d50ddc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are ordered

- **passive-voice** · skills/conversation-mode/SKILL.md:105:72 · **recurring** · fingerprint: 448cf9dfd90fe327096b71e5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paused

- **passive-voice** · skills/conversation-mode/SKILL.md:110:41 · **recurring** · fingerprint: 24000f0d039ebc991f65530c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unresolved

- **passive-voice** · skills/conversation-mode/SKILL.md:137:88 · **recurring** · fingerprint: 448cf9dfd90fe327096b71e5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is paused

- **present-perfect** · skills/conversation-mode/SKILL.md:138:78 · **recurring** · fingerprint: 11522f9e8c67a502b19046c1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has stopped

- **present-perfect** · skills/conversation-mode/SKILL.md:138:108 · **recurring** · fingerprint: fb6ab971291fabec8f04e13d
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has proposed

- **passive-voice** · skills/conversation-mode/SKILL.md:139:61 · **recurring** · fingerprint: a5afffbd39db7eee0657c03b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · skills/conversation-mode/SKILL.md:139:272 · **recurring** · fingerprint: 7432ab5664bf24b78cc7ff00
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is resolved

- **passive-voice** · skills/conversation-mode/SKILL.md:154:63 · **recurring** · fingerprint: a5afffbd39db7eee0657c03b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · skills/conversation-mode/SKILL.md:159:36 · **recurring** · fingerprint: 3a6c1312d7b45107dbc72a9d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was encountered

- **passive-voice** · skills/conversation-mode/SKILL.md:161:106 · **recurring** · fingerprint: f524e4cf6f61106be53e395c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was verified

- **passive-voice** · skills/conversation-mode/SKILL.md:170:180 · **recurring** · fingerprint: 30999b2a0d67c2a1670763ff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exceeded

- **passive-voice** · skills/conversation-mode/SKILL.md:196:260 · **recurring** · fingerprint: a5afffbd39db7eee0657c03b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **present-perfect** · skills/conversation-mode/SKILL.md:211:94 · **recurring** · fingerprint: 5b8f9ac16a3f5a3fd92e7621
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has approved

- **present-perfect** · skills/conversation-mode/SKILL.md:238:126 · **recurring** · fingerprint: 7e130dc07470c4dfc1de436d
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been given

- **passive-voice** · skills/conversation-mode/SKILL.md:238:130 · **recurring** · fingerprint: ef15c6245f889cbfdb09d89a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been given

- **passive-voice** · skills/conversation-mode/SKILL.md:259:75 · **recurring** · fingerprint: 04de33177ef6c58de34b6fd5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are governed


### skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 8
- **Hard findings:** 0
- **Baseline:** 7
- **Words:** 2716
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:7:89 · **recurring** · fingerprint: cd523ffc146c3f6901de60f2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is designed

- **present-perfect** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:15:1 · **recurring** · fingerprint: d30efb69e80e577256521942
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been completed

- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:15:5 · **recurring** · fingerprint: 6ff3e39160ad0dff0950e93f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been completed

- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:20:13 · **recurring** · fingerprint: 50a2d483f4875f3fb2b04103
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is built

- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:37:47 · **recurring** · fingerprint: 375845a698662aa8e2119fb5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is used

- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:39:38 · **recurring** · fingerprint: 375845a698662aa8e2119fb5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is used

- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:57:65 · **recurring** · fingerprint: 4b337153e373889fb349022d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being used

- **passive-voice** · skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:268:11 · **recurring** · fingerprint: 4b337153e373889fb349022d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being used


### skills/drawing/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 24
- **Hard findings:** 3
- **Baseline:** 24
- **Words:** 5082
- **Findings per 100 words:** 0.5

#### Complete diagnostics

- **passive-voice** · skills/drawing/SKILL.md:107:69 · **recurring** · fingerprint: 64d3910316c7c02208869eec
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is requested

- **passive-voice** · skills/drawing/SKILL.md:180:77 · **recurring** · fingerprint: 9a01e5392bd2f640fccc16f8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is listed

- **passive-voice** · skills/drawing/SKILL.md:189:31 · **recurring** · fingerprint: ae959494a55d88be42e4abf1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is packaged

- **passive-voice** · skills/drawing/SKILL.md:207:35 · **recurring** · fingerprint: d87f3bdb2e4a5cd311e567e0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known

- **passive-voice** · skills/drawing/SKILL.md:208:27 · **recurring** · fingerprint: d87f3bdb2e4a5cd311e567e0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known

- **passive-voice** · skills/drawing/SKILL.md:209:35 · **recurring** · fingerprint: 4a1561330f4473854edf7d68
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been loaded

- **passive-voice** · skills/drawing/SKILL.md:216:76 · **recurring** · fingerprint: 83aca3a3f45f79d0190f037b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is maintained

- **passive-voice** · skills/drawing/SKILL.md:255:21 · **recurring** · fingerprint: 4adc0f726bafb883a943a4c7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are wanted

- **passive-voice** · skills/drawing/SKILL.md:259:15 · **recurring** · fingerprint: 182721976b7c74744cfa668b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored

- **long-sentence** · skills/drawing/SKILL.md:261:4 · **recurring** · fingerprint: d81568a6e2238902ee0c2105
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words

- **long-sentence** · skills/drawing/SKILL.md:276:5 · **recurring** · fingerprint: 1da08cc0bf141330524bda57
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **passive-voice** · skills/drawing/SKILL.md:319:378 · **recurring** · fingerprint: 182721976b7c74744cfa668b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored

- **passive-voice** · skills/drawing/SKILL.md:319:553 · **recurring** · fingerprint: 108fef94cd85af0be9bae737
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · skills/drawing/SKILL.md:394:23 · **recurring** · fingerprint: c13b1ec0df584f1d71453752
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are governed

- **passive-voice** · skills/drawing/SKILL.md:400:60 · **recurring** · fingerprint: 828f9104eb1934f156af2c49
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was used

- **passive-voice** · skills/drawing/SKILL.md:407:216 · **recurring** · fingerprint: 856947d77008b1a8011c64b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are satisfied

- **passive-voice** · skills/drawing/SKILL.md:424:19 · **recurring** · fingerprint: f7c61d976e048fc4d2187457
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is refused

- **passive-voice** · skills/drawing/SKILL.md:456:42 · **recurring** · fingerprint: 108fef94cd85af0be9bae737
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · skills/drawing/SKILL.md:457:50 · **recurring** · fingerprint: d518259c92d98a763deb57db
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was produced

- **passive-voice** · skills/drawing/SKILL.md:458:42 · **recurring** · fingerprint: a9eeb0708efad4ad4ebac5a3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned

- **passive-voice** · skills/drawing/SKILL.md:462:11 · **recurring** · fingerprint: 2ebc7cf088303cbfd5592603
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **synonym-rotation** · skills/drawing/SKILL.md:470:15 · **recurring** · fingerprint: aa2b4a16cd7d5222231207e6
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **passive-voice** · skills/drawing/SKILL.md:489:24 · **recurring** · fingerprint: f6cfabada63cd4b942c2fdab
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are determined

- **passive-voice** · skills/drawing/SKILL.md:515:13 · **recurring** · fingerprint: 9ce13cb184b2103476d72b72
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Closed


### skills/document-standards/references/document-type-catalog.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 27
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 3060
- **Findings per 100 words:** 0.9

#### Complete diagnostics

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:4:162 · **recurring** · fingerprint: 305e0414169478f6e310d27a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was truncated

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:4:254 · **recurring** · fingerprint: 1b362583f0b6f9564bc66dd0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were inspected

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:28:139 · **recurring** · fingerprint: 521a3f31bc54ec727caae5b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was found

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:33:453 · **recurring** · fingerprint: bcb83f45ddf38808e5512023
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being uploaded

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:42:276 · **recurring** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:43:214 · **recurring** · fingerprint: a41ef6bbf64045f943d2af47
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:45:139 · **recurring** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:47:358 · **recurring** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:49:307 · **recurring** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **synonym-rotation** · skills/document-standards/references/document-type-catalog.md:52:264 · **recurring** · fingerprint: 2822a6b08706709830f1f820
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:64:165 · **recurring** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **long-sentence** · skills/document-standards/references/document-type-catalog.md:64:176 · **recurring** · fingerprint: ea92de1fbbfc0e6cafa24f7b
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:83:39 · **recurring** · fingerprint: 0c06b4bea825bbb8305e2205
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were reviewed

- **long-sentence** · skills/document-standards/references/document-type-catalog.md:88:200 · **recurring** · fingerprint: ea92de1fbbfc0e6cafa24f7b
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **present-perfect** · skills/document-standards/references/document-type-catalog.md:88:479 · **recurring** · fingerprint: 5bfc1af36a470f1f001188ee
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been approved

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:88:483 · **recurring** · fingerprint: c8520603dffa16dea8ea3dc4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been approved

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:89:136 · **recurring** · fingerprint: 6046357fc6d15e771a97e487
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are established

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:91:131 · **recurring** · fingerprint: f99656c38dfabd9bba499a0e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:91:206 · **recurring** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:92:199 · **recurring** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:94:262 · **recurring** · fingerprint: 95aef61741aad14590481dc3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is uploaded

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:104:230 · **recurring** · fingerprint: 446871a6fecc2890373b2df1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:112:129 · **recurring** · fingerprint: 521a3f31bc54ec727caae5b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was found

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:127:203 · **recurring** · fingerprint: 32702bd5a2c5ca60292eca3a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are superseded

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:134:57 · **recurring** · fingerprint: 9a67866b9f0335cac5eb0d64
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was required

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:140:123 · **recurring** · fingerprint: ec9e446045dd985aa0b168c4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are permitted

- **passive-voice** · skills/document-standards/references/document-type-catalog.md:144:32 · **recurring** · fingerprint: d5a3d56f7803c8bd7fe2f5bb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added


### workspace/task_board.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 3
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 249
- **Findings per 100 words:** 1.2

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


### skills/drawing/references/style-guide.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 462
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · skills/drawing/references/style-guide.md:60:31 · **recurring** · fingerprint: 581a2555fa37c98ab6bcfea3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was classified


### skills/INITIALIZATION_POLICY.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 2
- **Hard findings:** 0
- **Baseline:** 4
- **Words:** 1180
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **present-perfect** · skills/INITIALIZATION_POLICY.md:36:53 · **recurring** · fingerprint: 4f9e87e44f34528956cbd2f3
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been retrieved

- **passive-voice** · skills/INITIALIZATION_POLICY.md:36:57 · **recurring** · fingerprint: 25393e4ca29211513c0ea122
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved


### skills/drawing/assets/daily-index-template.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 210
- **Findings per 100 words:** 0.5

#### Complete diagnostics

- **long-sentence** · skills/drawing/assets/daily-index-template.md:5:1 · **recurring** · fingerprint: f7683dcec815fe504f98befb
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words


### skills/session-archiving/assets/session-summary-template.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 106
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/TASK_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 5
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 385
- **Findings per 100 words:** 1.3

#### Complete diagnostics

- **passive-voice** · workspace/TASK_TEMPLATE.md:18:108 · **recurring** · fingerprint: 5275280719ed16d2a5b7ad67
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is written

- **passive-voice** · workspace/TASK_TEMPLATE.md:46:21 · **recurring** · fingerprint: fdc561df7864672b424ed481
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was inspected

- **synonym-rotation** · workspace/TASK_TEMPLATE.md:57:58 · **recurring** · fingerprint: e37028ed88b119b98fe16981
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** checks

- **passive-voice** · workspace/TASK_TEMPLATE.md:73:20 · **recurring** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked

- **passive-voice** · workspace/TASK_TEMPLATE.md:74:23 · **recurring** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked


### skills/drawing/references/series-continuity-and-iteration.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 10
- **Hard findings:** 1
- **Baseline:** 9
- **Words:** 3262
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:44:40 · **recurring** · fingerprint: 1438a8fae83f4cef43ff111f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is inferred

- **present-perfect** · skills/drawing/references/series-continuity-and-iteration.md:50:245 · **recurring** · fingerprint: 8dcbbc229f60c870064ba1c1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has declared

- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:78:42 · **recurring** · fingerprint: 37314d6abfb814d104e0fd33
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is ordered

- **present-perfect** · skills/drawing/references/series-continuity-and-iteration.md:82:259 · **recurring** · fingerprint: fd585a05866ee7a0cfc00d99
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has established

- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:94:27 · **recurring** · fingerprint: eeef7c60d434b3d4f60ce329
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are locked

- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:134:15 · **recurring** · fingerprint: 0854ae12d93b6bb158c85528
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:140:14 · **recurring** · fingerprint: 0854ae12d93b6bb158c85528
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:164:73 · **recurring** · fingerprint: 602406a24344ba12b85a3c26
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being edited

- **synonym-rotation** · skills/drawing/references/series-continuity-and-iteration.md:177:31 · **recurring** · fingerprint: 284ad5169b785d0b95212ad0
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** Check

- **passive-voice** · skills/drawing/references/series-continuity-and-iteration.md:177:77 · **recurring** · fingerprint: 6bead85653574df77128e560
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was attached


### skills/asd-ste100/references/writing-rules.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 8
- **Hard findings:** 0
- **Baseline:** 6
- **Words:** 706
- **Findings per 100 words:** 1.1

#### Complete diagnostics

- **present-perfect** · skills/asd-ste100/references/writing-rules.md:7:511 · **recurring** · fingerprint: b41b3daad40ce14cd376bd73
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been

- **present-perfect** · skills/asd-ste100/references/writing-rules.md:26:84 · **recurring** · fingerprint: 4b5ee50f1aff2b6dcc346552
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have received

- **passive-voice** · skills/asd-ste100/references/writing-rules.md:26:129 · **recurring** · fingerprint: bb10a66696f9dabc2249dc8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is allowed

- **passive-voice** · skills/asd-ste100/references/writing-rules.md:27:16 · **recurring** · fingerprint: ac3ecaa3996b4c54c0d3e834
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are permitted

- **passive-voice** · skills/asd-ste100/references/writing-rules.md:30:16 · **recurring** · fingerprint: 773da2a0fc01b2b8333a892c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **passive-voice** · skills/asd-ste100/references/writing-rules.md:31:17 · **recurring** · fingerprint: bb10a66696f9dabc2249dc8b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is allowed

- **passive-voice** · skills/asd-ste100/references/writing-rules.md:37:58 · **recurring** · fingerprint: 4905d0267d2de525570a8af5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are capped

- **passive-voice** · skills/asd-ste100/references/writing-rules.md:50:5 · **recurring** · fingerprint: 2b19e1e9387f5374b63a7c1f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was designed


### skills/philosophy-religion-asceticism/references/answer-patterns.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 235
- **Findings per 100 words:** 0.4

#### Complete diagnostics

- **passive-voice** · skills/philosophy-religion-asceticism/references/answer-patterns.md:29:14 · **recurring** · fingerprint: c179db648027812a0a97ede9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is contested


### workspace/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 2
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 596
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **present-perfect** · workspace/README.md:25:469 · **recurring** · fingerprint: 4ad77a0e3e15f5d60871f4fe
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has triggered

- **present-perfect** · workspace/README.md:56:22 · **recurring** · fingerprint: 2769f0f695083967627c85d2
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has started


### skills/session-archiving/references/image-processing-scripts.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 344
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/the-worker/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 5
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 3133
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · skills/the-worker/SKILL.md:31:133 · **recurring** · fingerprint: 718d67ec20c921c3c043a464
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unverified

- **passive-voice** · skills/the-worker/SKILL.md:58:61 · **recurring** · fingerprint: 0eebcb0484fe67c4e2017ecc
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided

- **passive-voice** · skills/the-worker/SKILL.md:75:111 · **recurring** · fingerprint: d226740cae172dd2e1c78d14
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed

- **present-perfect** · skills/the-worker/SKILL.md:290:168 · **recurring** · fingerprint: 0e07f428da579362c55d461b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been verified

- **passive-voice** · skills/the-worker/SKILL.md:290:172 · **recurring** · fingerprint: b6cbb5b662b7ac93ef3ba05e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified


### skills/session-archiving/references/drawing-session-closeout.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 612
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · skills/session-archiving/references/drawing-session-closeout.md:17:227 · **recurring** · fingerprint: 5c4029a4459ae6a7419ec7c9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Closed


### skills/session-archiving/references/archive-records-and-image-prompts.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 28
- **Hard findings:** 1
- **Baseline:** 20
- **Words:** 4527
- **Findings per 100 words:** 0.6

#### Complete diagnostics

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:13:64 · **recurring** · fingerprint: 57efc2fd300bb9b7a8310db5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is curated

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:29:8 · **recurring** · fingerprint: b42e4986c1414564f3a43dfe
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was completed

- **synonym-rotation** · skills/session-archiving/references/archive-records-and-image-prompts.md:49:20 · **recurring** · fingerprint: 5d54d956f78d455711c2a358
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:84:21 · **recurring** · fingerprint: 1e36a113c65e15f12385ea65
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being discussed

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:93:11 · **recurring** · fingerprint: 23d11d13b31395d30d56f69c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are limited

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:121:164 · **recurring** · fingerprint: f5645cb699f537e6560fec11
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:124:130 · **recurring** · fingerprint: 27f21c0fcee319d11c62095b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:128:343 · **recurring** · fingerprint: c5e47aa80ee8e7135454cf5b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was rejected

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:186:170 · **recurring** · fingerprint: ba19e482eb53d060d32f3713
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was supplied

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:189:23 · **recurring** · fingerprint: 1d0aa41a6bd9ae288874e8d0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being tested

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:227:65 · **recurring** · fingerprint: 77657ae524bd6ec941b3e366
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:238:24 · **recurring** · fingerprint: 8c39463eb3e977779ed45cf7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:255:28 · **recurring** · fingerprint: 0fa85e814db12cfbf0b20231
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was attached

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:267:33 · **recurring** · fingerprint: ba19e482eb53d060d32f3713
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was supplied

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:282:44 · **recurring** · fingerprint: 9f3e8f0bc0fbdd6524b3656a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was created

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:292:68 · **recurring** · fingerprint: 493149180e6121959865622c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was delivered

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:293:36 · **recurring** · fingerprint: 77657ae524bd6ec941b3e366
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:293:58 · **recurring** · fingerprint: 2b09f88ca19a5527995c7947
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unverified

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:296:4 · **recurring** · fingerprint: b8f9a093dcad37186a759350
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is uploaded

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:297:78 · **recurring** · fingerprint: 0975b3ba84ad7cb994974ee5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:298:48 · **recurring** · fingerprint: e48495019965c18ff0c22b95
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was generated

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:299:75 · **recurring** · fingerprint: 77657ae524bd6ec941b3e366
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was returned

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:300:68 · **recurring** · fingerprint: 55f138238adaad7251236fe2
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unconfirmed

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:310:20 · **recurring** · fingerprint: 2868b703139e25825d4a9b8a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is finalized

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:314:53 · **recurring** · fingerprint: 009936d66fee55cde90f5887
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is renamed

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:336:242 · **recurring** · fingerprint: 80f2107125cb88de9fe1f2d7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:338:35 · **recurring** · fingerprint: 695e4b770f91de2ff1b14f54
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is stored

- **passive-voice** · skills/session-archiving/references/archive-records-and-image-prompts.md:385:69 · **recurring** · fingerprint: 424f162bb288d4ec5598118a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is based


### skills/drawing/references/prompt-fidelity.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 46
- **Hard findings:** 1
- **Baseline:** 15
- **Words:** 3676
- **Findings per 100 words:** 1.3

#### Complete diagnostics

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:13:215 · **recurring** · fingerprint: 404693192feb5c0a1bc279e9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is measured

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:15:69 · **recurring** · fingerprint: ccf5d0ae1e3ac5dfa3d81535
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are retained

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:46:115 · **recurring** · fingerprint: 620b7d7fd1d18757b7cf5e84
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is phrased

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:56:24 · **recurring** · fingerprint: dbd3657662996413f5b3e09d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been approved

- **present-perfect** · skills/drawing/references/prompt-fidelity.md:62:24 · **recurring** · fingerprint: 0b65a30e1dc02ac864748bce
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has rejected

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:74:32 · **recurring** · fingerprint: f40577f4f87280d2bafbbb33
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are prohibited

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:80:35 · **recurring** · fingerprint: 1439db2c98d70c1af24c7cd4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being limited

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:89:141 · **recurring** · fingerprint: ca6cd5747867ae19c46def89
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been established

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:91:171 · **recurring** · fingerprint: f1f73777ecdc15c96cdcd383
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are covered

- **present-perfect** · skills/drawing/references/prompt-fidelity.md:116:33 · **recurring** · fingerprint: c31471d539e8aa39ed2d47c3
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has specified

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:119:41 · **recurring** · fingerprint: 3238ce4831a0652078d996e0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is depicted

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:127:120 · **recurring** · fingerprint: 942e61ff7b0fb459a13ad0d1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is unspecified

- **present-perfect** · skills/drawing/references/prompt-fidelity.md:127:168 · **recurring** · fingerprint: af345c449e8933426d2e19fe
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has delegated

- **present-perfect** · skills/drawing/references/prompt-fidelity.md:151:163 · **recurring** · fingerprint: af345c449e8933426d2e19fe
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has delegated

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:198:141 · **recurring** · fingerprint: b7f3317fff8f1ff3b74412df
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **present-perfect** · skills/drawing/references/prompt-fidelity.md:225:75 · **recurring** · fingerprint: 0b65a30e1dc02ac864748bce
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has rejected

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:244:41 · **recurring** · fingerprint: 292fbd9b5ed50c5247cf2f53
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been restored

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:245:103 · **recurring** · fingerprint: 5ea0ac18f64fc9ba3c3b6b6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been added

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:246:33 · **recurring** · fingerprint: 8233e35bff35faaf38a980b8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been paraphrased

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:247:123 · **recurring** · fingerprint: 753e3e43156f685672332845
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been introduced

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:248:42 · **recurring** · fingerprint: 97a20fbdbe0577e454aefdc8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been preserved

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:249:26 · **recurring** · fingerprint: 13f4a5392eedebe0585ee245
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been limited

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:250:23 · **recurring** · fingerprint: b49d5e45b1b3b1c0140fab39
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been converted

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:265:66 · **recurring** · fingerprint: 278f5a301dede82f4c8ac412
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being submitted

- **present-perfect** · skills/drawing/references/prompt-fidelity.md:268:30 · **recurring** · fingerprint: d88beccb64f34579d80979ff
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been archived

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:268:34 · **recurring** · fingerprint: 8e48ea2de3c2f37bc3a96546
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been archived

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:270:46 · **recurring** · fingerprint: 40f2dda08cf8d4e026bc1cf8
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is exposed

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:272:98 · **recurring** · fingerprint: 7166cf5d9d622916649b0f8d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was submitted

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:272:197 · **recurring** · fingerprint: 403d89805494afd57b827dee
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was authorized

- **present-perfect** · skills/drawing/references/prompt-fidelity.md:289:87 · **recurring** · fingerprint: af345c449e8933426d2e19fe
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has delegated

- **present-perfect** · skills/drawing/references/prompt-fidelity.md:300:57 · **recurring** · fingerprint: 4e3b443eb033832d17dc8545
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been checked

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:300:62 · **recurring** · fingerprint: bdcbc53fefbff59427750156
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been checked

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:301:99 · **recurring** · fingerprint: 8854a5a70b9be9bbffa72e61
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preserved

- **present-perfect** · skills/drawing/references/prompt-fidelity.md:302:41 · **recurring** · fingerprint: 83c2d80059f94672d8a71141
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been introduced

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:302:46 · **recurring** · fingerprint: 753e3e43156f685672332845
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been introduced

- **present-perfect** · skills/drawing/references/prompt-fidelity.md:303:106 · **recurring** · fingerprint: 3115ca2ae7a235e7560a1cbc
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been added

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:303:111 · **recurring** · fingerprint: 5ea0ac18f64fc9ba3c3b6b6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been added

- **present-perfect** · skills/drawing/references/prompt-fidelity.md:304:31 · **recurring** · fingerprint: c60448dfacfff81b45010545
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been restored

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:304:35 · **recurring** · fingerprint: 292fbd9b5ed50c5247cf2f53
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been restored

- **present-perfect** · skills/drawing/references/prompt-fidelity.md:306:58 · **recurring** · fingerprint: ebc3fe4b7983f2625cff09c5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been audited

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:306:62 · **recurring** · fingerprint: 847f9b53906e7b622acde414
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been audited

- **present-perfect** · skills/drawing/references/prompt-fidelity.md:307:27 · **recurring** · fingerprint: 1f52364af2f7476db43a8cf5
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been removed

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:307:31 · **recurring** · fingerprint: 4fa531795b4f48c712cb9b8f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been removed

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:309:42 · **recurring** · fingerprint: dc5ac767caa168e0bfb3a0be
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is assigned

- **passive-voice** · skills/drawing/references/prompt-fidelity.md:309:73 · **recurring** · fingerprint: 2684dd7826880335bb93b3ce
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was copied

- **synonym-rotation** · skills/drawing/references/prompt-fidelity.md:315:156 · **recurring** · fingerprint: c784915b81aefed48004e9cb
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'retrieve' name the same action. Pick one and use it every time.
  - **Matched text:** fetch


### skills/document-standards/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 2
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 1612
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **passive-voice** · skills/document-standards/SKILL.md:75:47 · **recurring** · fingerprint: f02e1c27fdc79f6921bf2e16
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created

- **passive-voice** · skills/document-standards/SKILL.md:197:37 · **recurring** · fingerprint: da830431b494f6dd663885a4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is defined


### skills/session-archiving/SKILL.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 3
- **Hard findings:** 0
- **Baseline:** 7
- **Words:** 2388
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **passive-voice** · skills/session-archiving/SKILL.md:80:90 · **recurring** · fingerprint: 038292fe0c13c6199af4bf3a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known

- **passive-voice** · skills/session-archiving/SKILL.md:134:41 · **recurring** · fingerprint: 99dd9dc8b35e76013c9dd169
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is mentioned

- **passive-voice** · skills/session-archiving/SKILL.md:142:408 · **recurring** · fingerprint: 2779f560ab6e00a4b9a36994
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is provided


### skills/drawing/references/image-editing-protocol.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 4
- **Words:** 962
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/session-archiving/assets/session-brief-template.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 1
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 288
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **long-sentence** · skills/session-archiving/assets/session-brief-template.md:5:1 · **recurring** · fingerprint: 9edc4fb8b393050df4a8fe30
  - **Level:** advisory-free
  - **Message:** Sentence has 32 words (cap 25). Split it.
  - **Matched text:** 32 words


### skills/SESSION_START.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 2
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 2275
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **present-perfect** · skills/SESSION_START.md:18:114 · **recurring** · fingerprint: 9acf80e5a2b48047e9dd619f
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have been retrieved

- **passive-voice** · skills/SESSION_START.md:18:119 · **recurring** · fingerprint: fec2fb4fa450910b68502f34
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been retrieved


### skills/drawing/references/patterns/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 442
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · skills/drawing/references/patterns/README.md:34:143 · **recurring** · fingerprint: f9d42240cfb6f779e60dcd02
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is superseded


### skills/philosophy-religion-asceticism/references/research-method.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 559
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### skills/philosophy-religion-asceticism/CHANGELOG.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 56
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
