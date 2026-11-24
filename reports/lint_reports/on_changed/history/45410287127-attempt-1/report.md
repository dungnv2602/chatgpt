# On Changed STE Lint Evidence Report

- **Result:** Passed
- **Schema version:** 1.1.0
- **Run:** [#622](https://github.com/dungnv2602/chatgpt/actions/runs/45410287127)
- **Run ID / attempt:** 45410287127 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / aa5b968b2ed0d13f86d061da9a9217b0a5a86196
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 7fa7483122c074c48e8d0b82ea65d59f4aca37f4
- **Linter source SHA:** aa5b968b2ed0d13f86d061da9a9217b0a5a86196
- **Generated (UTC):** 2026-11-24T14:06:35.370181+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 1 |
| Files that failed | 0 |
| Files with findings | 1 |
| Total findings | 4 |
| Hard findings | 0 |
| Advisory findings | 4 |
| New findings | 4 |
| Recurring findings | 0 |
| Resolved findings | 41 |
| Failed workflow checks | 0 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md | PASS | 4 | 0 | 0 | 1216 | 0.3 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 4 |

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
Ran 4 tests in 0.360s

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

- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:34:64 · **new** · fingerprint: fbe6150d9b5e8dab3b1e43a3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:47:41 · **new** · fingerprint: 8d3ad3a1e3838d879ee9b85a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was made
- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:111:44 · **new** · fingerprint: e871aaaf906a610ac0db5605
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are implemented
- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:160:67 · **new** · fingerprint: 2eafa78f211213b12b14d4d5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed

### Recurring findings

None.

### Resolved findings

- **passive-voice** · skills/decision-governance/SKILL.md:29:58 · **resolved** · fingerprint: 62ba07312f0098deae0d2084
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is approved
- **passive-voice** · skills/decision-governance/SKILL.md:29:82 · **resolved** · fingerprint: a461c9d33f692bb30c8d9e32
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **passive-voice** · skills/decision-governance/SKILL.md:137:89 · **resolved** · fingerprint: a461c9d33f692bb30c8d9e32
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **passive-voice** · skills/decision-governance/SKILL.md:144:50 · **resolved** · fingerprint: e1b2426fdfb12ab8d8076ca7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implemented
- **synonym-rotation** · skills/decision-governance/SKILL.md:147:92 · **resolved** · fingerprint: 2624698c9e0a949a01e1c0be
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **passive-voice** · skills/decision-governance/SKILL.md:173:72 · **resolved** · fingerprint: 3b0fa6154ecfe49591695005
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** being worked
- **present-perfect** · skills/decision-governance/SKILL.md:183:22 · **resolved** · fingerprint: 7481ea9586cd9998cf136bf1
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been read
- **passive-voice** · skills/decision-governance/SKILL.md:183:26 · **resolved** · fingerprint: 50eae35fe6ca9a2e19bff9a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been read
- **passive-voice** · skills/decision-governance/SKILL.md:184:38 · **resolved** · fingerprint: 58b03457b929a04127a23698
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
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
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:39:264 · **resolved** · fingerprint: bd13d200f2cd36d327625082
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are preserved
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:48:276 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:49:207 · **resolved** · fingerprint: a41ef6bbf64045f943d2af47
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is read
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:51:139 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:53:358 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:55:336 · **resolved** · fingerprint: 8aaaeb4dae872360fad1cb7e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is needed
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:61:314 · **resolved** · fingerprint: 8e6ebb9019d53b6c90f1902c
  - **Level:** advisory-free
  - **Message:** Sentence has 35 words (cap 25). Split it.
  - **Matched text:** 35 words
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:62:546 · **resolved** · fingerprint: 199f2603ee3fb1c3abd18ce6
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are skipped
- **long-sentence** · skills/document-standards/references/document-type-catalog.md:70:117 · **resolved** · fingerprint: ea92de1fbbfc0e6cafa24f7b
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **present-perfect** · skills/document-standards/references/document-type-catalog.md:96:268 · **resolved** · fingerprint: 028b84870f82ee2f98dcbf3b
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has run
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:98:169 · **resolved** · fingerprint: bb8de6bc648079b20917fbff
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are catalogued
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:109:263 · **resolved** · fingerprint: 305641bf283ed85e29efe674
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is published
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:121:251 · **resolved** · fingerprint: 195a2fd68103c17c8542eb26
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are covered
- **synonym-rotation** · skills/document-standards/references/document-type-catalog.md:142:298 · **resolved** · fingerprint: 2822a6b08706709830f1f820
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:156:39 · **resolved** · fingerprint: 0c06b4bea825bbb8305e2205
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were reviewed
- **present-perfect** · skills/document-standards/references/document-type-catalog.md:161:448 · **resolved** · fingerprint: 5bfc1af36a470f1f001188ee
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has been approved
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:161:452 · **resolved** · fingerprint: c8520603dffa16dea8ea3dc4
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been approved
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:162:136 · **resolved** · fingerprint: 6046357fc6d15e771a97e487
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are established
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:164:131 · **resolved** · fingerprint: f99656c38dfabd9bba499a0e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is established
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:164:206 · **resolved** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:165:199 · **resolved** · fingerprint: 2d052b2c33e7ba911021d0e1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is planned
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:167:262 · **resolved** · fingerprint: 95aef61741aad14590481dc3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is uploaded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:177:230 · **resolved** · fingerprint: 446871a6fecc2890373b2df1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is justified
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:185:129 · **resolved** · fingerprint: 521a3f31bc54ec727caae5b1
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was found
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:197:138 · **resolved** · fingerprint: d8738c991b456b6b6a7cdd80
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was reconstructed
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:200:203 · **resolved** · fingerprint: 32702bd5a2c5ca60292eca3a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are superseded
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:209:57 · **resolved** · fingerprint: 9a67866b9f0335cac5eb0d64
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was required
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:213:189 · **resolved** · fingerprint: 7e6ec02ac376dc4e638ffc6d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was warranted
- **passive-voice** · skills/document-standards/references/document-type-catalog.md:221:32 · **resolved** · fingerprint: d5a3d56f7803c8bd7fe2f5bb
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is added

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 4
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 1216
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:34:64 · **new** · fingerprint: fbe6150d9b5e8dab3b1e43a3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required

- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:47:41 · **new** · fingerprint: 8d3ad3a1e3838d879ee9b85a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was made

- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:111:44 · **new** · fingerprint: e871aaaf906a610ac0db5605
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are implemented

- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:160:67 · **new** · fingerprint: 2eafa78f211213b12b14d4d5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
