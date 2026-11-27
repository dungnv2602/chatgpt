# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#913](https://github.com/dungnv2602/chatgpt/actions/runs/45953412240)
- **Run ID / attempt:** 45953412240 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / b6e7736c93c5dbcaef59ec4c01ccb2f5aa1ffa13
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** fe3a0a1d9f506caad8fd8505171b31ec72e419d2
- **Linter source SHA:** b6e7736c93c5dbcaef59ec4c01ccb2f5aa1ffa13
- **Generated (UTC):** 2026-11-27T06:42:00.920667+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 14 |
| Files that failed | 9 |
| Files with findings | 12 |
| Total findings | 54 |
| Hard findings | 24 |
| Advisory findings | 30 |
| New findings | 51 |
| Recurring findings | 3 |
| Resolved findings | 6 |
| Failed workflow checks | 2 |

## 2. Execution environment

- Runner OS: Linux
- Python: 3.15.2
- Platform: Linux-7.0.0-1020-azure-x86_64-with-glibc2.43
- The JSON report records the full runtime version and every original per-file linter response.
- The report records the commit that supplied the linter and generator code.

## 3. Exact evaluation coverage

This list is the exact set of Markdown files passed to the linter. It does not infer coverage from a Git change summary.

- workspace/adr/README.md
- .agent/skills/github-actions/SKILL.md
- .agent/SESSION_START.md
- .agent/skills/the-worker/SKILL.md
- .agent/skills/decision-governance/SKILL.md
- .agent/skills/document-standards/references/document-type-catalog.md
- workspace/task_board.md
- workspace/analysis/README.md
- workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md
- .agent/skills/ci-ledger/SKILL.md
- workspace/TASK_TEMPLATE.md
- workspace/README.md
- workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md
- .agent/skills/asd-ste100/references/repository-writing-policy.md

## 4. Per-file result matrix

The table includes every evaluated file, including files with zero findings and files with execution errors.

| File | Result | Findings | Hard | Baseline | Words | Per 100 words | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace/adr/README.md | FAIL | 2 | 2 | 0 | 576 | 0.3 | 1 |
| .agent/skills/github-actions/SKILL.md | FAIL | 6 | 3 | 0 | 3318 | 0.2 | 1 |
| .agent/SESSION_START.md | FAIL | 8 | 4 | 0 | 3002 | 0.3 | 1 |
| .agent/skills/the-worker/SKILL.md | FAIL | 4 | 2 | 0 | 6266 | 0.1 | 1 |
| .agent/skills/decision-governance/SKILL.md | FAIL | 9 | 5 | 0 | 2991 | 0.3 | 1 |
| .agent/skills/document-standards/references/document-type-catalog.md | PASS | 2 | 0 | 0 | 4684 | 0.0 | 0 |
| workspace/task_board.md | FAIL | 3 | 2 | 0 | 1415 | 0.2 | 1 |
| workspace/analysis/README.md | PASS | 0 | 0 | 0 | 278 | 0.0 | 0 |
| workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md | PASS | 2 | 0 | 0 | 2919 | 0.1 | 0 |
| .agent/skills/ci-ledger/SKILL.md | FAIL | 3 | 3 | 0 | 2347 | 0.1 | 1 |
| workspace/TASK_TEMPLATE.md | FAIL | 6 | 1 | 0 | 518 | 1.2 | 1 |
| workspace/README.md | PASS | 0 | 0 | 0 | 1108 | 0.0 | 0 |
| workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md | FAIL | 8 | 2 | 0 | 1310 | 0.6 | 1 |
| .agent/skills/asd-ste100/references/repository-writing-policy.md | PASS | 1 | 0 | 0 | 570 | 0.2 | 0 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 29 |
| synonym-rotation | 13 |
| semicolon | 9 |
| long-sentence | 2 |
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
Ran 4 tests in 0.348s

OK
~~~

### Markdown anchor regression tests

- **Result:** Failed
- **Exit code:** 1

~~~~~~~~~~~~~~~~~~~~~~~text
..F.....
======================================================================
FAIL: test_incremental_scope_rejects_inactive_or_untracked_sources (__main__.MarkdownAnchorTests.test_incremental_scope_rejects_inactive_or_untracked_sources) (path='.archive/adr/old.md')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/work/chatgpt/chatgpt/.agent/skills/asd-ste100/scripts/test_check_markdown_anchors.py", line 80, in test_incremental_scope_rejects_inactive_or_untracked_sources
    with self.assertRaisesRegex(ValueError, "inactive or untracked"):
         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: ValueError not raised

----------------------------------------------------------------------
Ran 8 tests in 0.007s

FAILED (failures=1)
~~~~~~~~~~~~~~~~~~~~~~~

### STE linter self-test

- **Result:** Passed
- **Exit code:** 0

~~~text
selftest OK
~~~

### Markdown links and heading anchors

- **Result:** Failed
- **Exit code:** 1

~~~text
Scanned 14 changed Markdown sources (557 available as link targets) and 96 local Markdown links.
Found 2 unresolved local Markdown targets or anchors.
workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md: missing Markdown file: ../task/20261124-103354-establish-draft-adr-governance-and-repo-analysis-workflow.md
workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md: missing Markdown file: ../task/20261124-103354-establish-draft-adr-governance-and-repo-analysis-workflow.md
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **semicolon** · workspace/adr/README.md:68:135 · **new** · fingerprint: 0927b4ce823c0e0c8d5570fa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/README.md:69:151 · **new** · fingerprint: 0927b4ce823c0e0c8d5570fa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:36:65 · **new** · fingerprint: 3729cd2e886059e21da61ef7
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove
- **passive-voice** · .agent/skills/github-actions/SKILL.md:72:209 · **new** · fingerprint: de2e6ff859150e25d2ddbdf7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified
- **passive-voice** · .agent/skills/github-actions/SKILL.md:72:236 · **new** · fingerprint: 67be1862f0bcd76c81a66643
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read
- **passive-voice** · .agent/skills/github-actions/SKILL.md:72:284 · **new** · fingerprint: ebe73caf7cb37aa94e730288
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **long-sentence** · .agent/skills/github-actions/SKILL.md:80:1 · **new** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · .agent/skills/github-actions/SKILL.md:88:351 · **new** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/SESSION_START.md:41:99 · **new** · fingerprint: b364e80e8c98116d3ebcfb38
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'retrieve' name the same action. Pick one and use it every time.
  - **Matched text:** fetch
- **synonym-rotation** · .agent/SESSION_START.md:53:31 · **new** · fingerprint: 0934ec0e9cbf6427170b249c
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check
- **passive-voice** · .agent/SESSION_START.md:93:161 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **passive-voice** · .agent/SESSION_START.md:94:63 · **new** · fingerprint: 8e21e03238dfdcddd1f2d77d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified
- **passive-voice** · .agent/SESSION_START.md:238:167 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given
- **present-perfect** · .agent/SESSION_START.md:254:154 · **new** · fingerprint: 89880d1a1650656e6b26d226
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have passed
- **long-sentence** · .agent/SESSION_START.md:279:1 · **new** · fingerprint: 85322c6fe1ce661af2777338
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words
- **synonym-rotation** · .agent/SESSION_START.md:293:146 · **new** · fingerprint: 7c9bb193d72e7abcbed9fe07
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validates
- **passive-voice** · .agent/skills/the-worker/SKILL.md:294:144 · **new** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized
- **passive-voice** · .agent/skills/the-worker/SKILL.md:386:196 · **new** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:413:513 · **new** · fingerprint: 6e2f9b805be9c08510010f85
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:415:717 · **new** · fingerprint: 9cca8e1414feae74d470296b
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirms
- **semicolon** · .agent/skills/decision-governance/SKILL.md:84:206 · **new** · fingerprint: 7604193c846dc517461ca60b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · .agent/skills/decision-governance/SKILL.md:103:283 · **new** · fingerprint: 7c881c753a4078cb6de1c860
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **synonym-rotation** · .agent/skills/decision-governance/SKILL.md:107:38 · **new** · fingerprint: 7e15f02585cf13c74c4d9066
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · .agent/skills/decision-governance/SKILL.md:109:34 · **new** · fingerprint: ed925553639766f753b1e47c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is included
- **passive-voice** · .agent/skills/decision-governance/SKILL.md:115:47 · **new** · fingerprint: c6fdcf445b99331b3955a823
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are stated
- **semicolon** · .agent/skills/decision-governance/SKILL.md:115:57 · **new** · fingerprint: 7604193c846dc517461ca60b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/decision-governance/SKILL.md:115:102 · **new** · fingerprint: c5cbda1d2fcdc95906e3b0f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implied
- **passive-voice** · .agent/skills/decision-governance/SKILL.md:117:86 · **new** · fingerprint: 9248adb057e0be913c820595
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are addressed
- **semicolon** · .agent/skills/decision-governance/SKILL.md:131:65 · **new** · fingerprint: 7604193c846dc517461ca60b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:147:143 · **new** · fingerprint: 42f86e8fba1534a97a0dd2a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are completed
- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:147:228 · **new** · fingerprint: de21f21791e1cf986fde4201
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are accepted
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:259:84 · **new** · fingerprint: 729850cb6edbfa392f5fd0c0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:259:138 · **new** · fingerprint: 7e4de9696d2368b08f2ceda9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:67:5 · **new** · fingerprint: ca9ad71bde9bdef6b1180213
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changed
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:121:27 · **new** · fingerprint: b15b11ac85d2fcdf68c941a9
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** removes
- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:150:36 · **new** · fingerprint: 489f962a46e94a58519c7e2a
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify
- **passive-voice** · workspace/TASK_TEMPLATE.md:25:159 · **new** · fingerprint: 5275280719ed16d2a5b7ad67
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is written
- **passive-voice** · workspace/TASK_TEMPLATE.md:53:32 · **new** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **passive-voice** · workspace/TASK_TEMPLATE.md:79:20 · **new** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **passive-voice** · workspace/TASK_TEMPLATE.md:80:23 · **new** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked
- **semicolon** · workspace/TASK_TEMPLATE.md:96:110 · **new** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/TASK_TEMPLATE.md:96:247 · **new** · fingerprint: f89fcc99c66cd06012ce7d5a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted
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
- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:150:86 · **new** · fingerprint: e56053c3ddae76d3a0704b63
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was retired
- **semicolon** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:152:54 · **new** · fingerprint: 9a23cba48e9d5ffca1df4cc7
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:160:67 · **new** · fingerprint: 2eafa78f211213b12b14d4d5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed
- **semicolon** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:163:53 · **new** · fingerprint: 9a23cba48e9d5ffca1df4cc7
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:163:179 · **new** · fingerprint: cb29534f35d8d330ae1e06be
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived
- **passive-voice** · .agent/skills/asd-ste100/references/repository-writing-policy.md:18:36 · **new** · fingerprint: fa71e22a78d6e4ce44e3a977
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known

### Recurring findings

- **passive-voice** · workspace/task_board.md:5:556 · **recurring** · fingerprint: 091688e97ff44b87f3a1d264
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **synonym-rotation** · workspace/task_board.md:73:41 · **recurring** · fingerprint: 8940fe614ee1d534bedb13a4
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** check
- **synonym-rotation** · workspace/task_board.md:105:88 · **recurring** · fingerprint: e62ca06f23c949cf9f748c10
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validate

### Resolved findings

- **passive-voice** · workspace/draft/DRAFT-0006-editorial-successor-for-adr-0003.md:90:59 · **resolved** · fingerprint: 3a5b8412eaf100e118f17c8f
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **synonym-rotation** · workspace/draft/DRAFT-0006-editorial-successor-for-adr-0003.md:158:19 · **resolved** · fingerprint: 88c525f2c2d9aadc1e2f7faf
  - **Level:** advisory-free
  - **Message:** 'alter' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** alter
- **synonym-rotation** · workspace/draft/DRAFT-0006-editorial-successor-for-adr-0003.md:171:143 · **resolved** · fingerprint: 13f39a799a7213976339c951
  - **Level:** advisory-free
  - **Message:** 'fix' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** Fix
- **passive-voice** · workspace/draft/DRAFT-0007-editorial-successor-for-adr-0004.md:99:59 · **resolved** · fingerprint: c39323ab6689958912bbc8ba
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **synonym-rotation** · workspace/draft/DRAFT-0007-editorial-successor-for-adr-0004.md:168:19 · **resolved** · fingerprint: 26a6732babf8a18c8f5ce179
  - **Level:** advisory-free
  - **Message:** 'alter' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** alter
- **synonym-rotation** · workspace/draft/DRAFT-0007-editorial-successor-for-adr-0004.md:182:143 · **resolved** · fingerprint: 2a02d81fb2a9bfbd6ffc2294
  - **Level:** advisory-free
  - **Message:** 'fix' and 'correct' name the same action. Pick one and use it every time.
  - **Matched text:** Fix

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### workspace/adr/README.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 2
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 576
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **semicolon** · workspace/adr/README.md:68:135 · **new** · fingerprint: 0927b4ce823c0e0c8d5570fa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **semicolon** · workspace/adr/README.md:69:151 · **new** · fingerprint: 0927b4ce823c0e0c8d5570fa
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### .agent/skills/github-actions/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 6
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 3318
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **synonym-rotation** · .agent/skills/github-actions/SKILL.md:36:65 · **new** · fingerprint: 3729cd2e886059e21da61ef7
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** remove

- **passive-voice** · .agent/skills/github-actions/SKILL.md:72:209 · **new** · fingerprint: de2e6ff859150e25d2ddbdf7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is verified

- **passive-voice** · .agent/skills/github-actions/SKILL.md:72:236 · **new** · fingerprint: 67be1862f0bcd76c81a66643
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are read

- **passive-voice** · .agent/skills/github-actions/SKILL.md:72:284 · **new** · fingerprint: ebe73caf7cb37aa94e730288
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded

- **long-sentence** · .agent/skills/github-actions/SKILL.md:80:1 · **new** · fingerprint: 5bc051350b900cffa5093b16
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words

- **semicolon** · .agent/skills/github-actions/SKILL.md:88:351 · **new** · fingerprint: 37b04b4859601e36ccef7b3a
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### .agent/SESSION_START.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 8
- **Hard findings:** 4
- **Baseline:** 0
- **Words:** 3002
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **synonym-rotation** · .agent/SESSION_START.md:41:99 · **new** · fingerprint: b364e80e8c98116d3ebcfb38
  - **Level:** advisory-free
  - **Message:** 'fetch' and 'retrieve' name the same action. Pick one and use it every time.
  - **Matched text:** fetch

- **synonym-rotation** · .agent/SESSION_START.md:53:31 · **new** · fingerprint: 0934ec0e9cbf6427170b249c
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** Check

- **passive-voice** · .agent/SESSION_START.md:93:161 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **passive-voice** · .agent/SESSION_START.md:94:63 · **new** · fingerprint: 8e21e03238dfdcddd1f2d77d
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** been verified

- **passive-voice** · .agent/SESSION_START.md:238:167 · **new** · fingerprint: 6df4df8dd70ff7a6b7fcd357
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is given

- **present-perfect** · .agent/SESSION_START.md:254:154 · **new** · fingerprint: 89880d1a1650656e6b26d226
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** have passed

- **long-sentence** · .agent/SESSION_START.md:279:1 · **new** · fingerprint: 85322c6fe1ce661af2777338
  - **Level:** advisory-free
  - **Message:** Sentence has 27 words (cap 25). Split it.
  - **Matched text:** 27 words

- **synonym-rotation** · .agent/SESSION_START.md:293:146 · **new** · fingerprint: 7c9bb193d72e7abcbed9fe07
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validates


### .agent/skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 4
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 6266
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **passive-voice** · .agent/skills/the-worker/SKILL.md:294:144 · **new** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized

- **passive-voice** · .agent/skills/the-worker/SKILL.md:386:196 · **new** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:413:513 · **new** · fingerprint: 6e2f9b805be9c08510010f85
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:415:717 · **new** · fingerprint: 9cca8e1414feae74d470296b
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirms


### .agent/skills/decision-governance/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 9
- **Hard findings:** 5
- **Baseline:** 0
- **Words:** 2991
- **Findings per 100 words:** 0.3

#### Complete diagnostics

- **semicolon** · .agent/skills/decision-governance/SKILL.md:84:206 · **new** · fingerprint: 7604193c846dc517461ca60b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **synonym-rotation** · .agent/skills/decision-governance/SKILL.md:103:283 · **new** · fingerprint: 7c881c753a4078cb6de1c860
  - **Level:** advisory-free
  - **Message:** 'check' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** check

- **synonym-rotation** · .agent/skills/decision-governance/SKILL.md:107:38 · **new** · fingerprint: 7e15f02585cf13c74c4d9066
  - **Level:** advisory-free
  - **Message:** 'verify' and 'confirm' name the same action. Pick one and use it every time.
  - **Matched text:** verify

- **passive-voice** · .agent/skills/decision-governance/SKILL.md:109:34 · **new** · fingerprint: ed925553639766f753b1e47c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is included

- **passive-voice** · .agent/skills/decision-governance/SKILL.md:115:47 · **new** · fingerprint: c6fdcf445b99331b3955a823
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are stated

- **semicolon** · .agent/skills/decision-governance/SKILL.md:115:57 · **new** · fingerprint: 7604193c846dc517461ca60b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/decision-governance/SKILL.md:115:102 · **new** · fingerprint: c5cbda1d2fcdc95906e3b0f9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is implied

- **passive-voice** · .agent/skills/decision-governance/SKILL.md:117:86 · **new** · fingerprint: 9248adb057e0be913c820595
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are addressed

- **semicolon** · .agent/skills/decision-governance/SKILL.md:131:65 · **new** · fingerprint: 7604193c846dc517461ca60b
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;


### .agent/skills/document-standards/references/document-type-catalog.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 2
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 4684
- **Findings per 100 words:** 0.0

#### Complete diagnostics

- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:147:143 · **new** · fingerprint: 42f86e8fba1534a97a0dd2a0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are completed

- **passive-voice** · .agent/skills/document-standards/references/document-type-catalog.md:147:228 · **new** · fingerprint: de21f21791e1cf986fde4201
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are accepted


### workspace/task_board.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 3
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 1415
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · workspace/task_board.md:5:556 · **recurring** · fingerprint: 091688e97ff44b87f3a1d264
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **synonym-rotation** · workspace/task_board.md:73:41 · **recurring** · fingerprint: 8940fe614ee1d534bedb13a4
  - **Level:** advisory-free
  - **Message:** 'check' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** check

- **synonym-rotation** · workspace/task_board.md:105:88 · **recurring** · fingerprint: e62ca06f23c949cf9f748c10
  - **Level:** advisory-free
  - **Message:** 'validate' and 'verify' name the same action. Pick one and use it every time.
  - **Matched text:** validate


### workspace/analysis/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 278
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 2
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 2919
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:259:84 · **new** · fingerprint: 729850cb6edbfa392f5fd0c0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **passive-voice** · workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md:259:138 · **new** · fingerprint: 7e4de9696d2368b08f2ceda9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done


### .agent/skills/ci-ledger/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 3
- **Hard findings:** 3
- **Baseline:** 0
- **Words:** 2347
- **Findings per 100 words:** 0.1

#### Complete diagnostics

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:67:5 · **new** · fingerprint: ca9ad71bde9bdef6b1180213
  - **Level:** advisory-free
  - **Message:** 'change' and 'modify' name the same action. Pick one and use it every time.
  - **Matched text:** changed

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:121:27 · **new** · fingerprint: b15b11ac85d2fcdf68c941a9
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** removes

- **synonym-rotation** · .agent/skills/ci-ledger/SKILL.md:150:36 · **new** · fingerprint: 489f962a46e94a58519c7e2a
  - **Level:** advisory-free
  - **Message:** 'verify' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** verify


### workspace/TASK_TEMPLATE.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 6
- **Hard findings:** 1
- **Baseline:** 0
- **Words:** 518
- **Findings per 100 words:** 1.2

#### Complete diagnostics

- **passive-voice** · workspace/TASK_TEMPLATE.md:25:159 · **new** · fingerprint: 5275280719ed16d2a5b7ad67
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is written

- **passive-voice** · workspace/TASK_TEMPLATE.md:53:32 · **new** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked

- **passive-voice** · workspace/TASK_TEMPLATE.md:79:20 · **new** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked

- **passive-voice** · workspace/TASK_TEMPLATE.md:80:23 · **new** · fingerprint: 72c3a8ba326ab1f70b39f345
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was checked

- **semicolon** · workspace/TASK_TEMPLATE.md:96:110 · **new** · fingerprint: 1d091436eb9c47dd7a5b55d1
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/TASK_TEMPLATE.md:96:247 · **new** · fingerprint: f89fcc99c66cd06012ce7d5a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is untrusted


### workspace/README.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 0
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 1108
- **Findings per 100 words:** 0.0

No STE findings were recorded for this file.


### workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 8
- **Hard findings:** 2
- **Baseline:** 0
- **Words:** 1310
- **Findings per 100 words:** 0.6

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

- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:150:86 · **new** · fingerprint: e56053c3ddae76d3a0704b63
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was retired

- **semicolon** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:152:54 · **new** · fingerprint: 9a23cba48e9d5ffca1df4cc7
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:160:67 · **new** · fingerprint: 2eafa78f211213b12b14d4d5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are committed

- **semicolon** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:163:53 · **new** · fingerprint: 9a23cba48e9d5ffca1df4cc7
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · workspace/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md:163:179 · **new** · fingerprint: cb29534f35d8d330ae1e06be
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was archived


### .agent/skills/asd-ste100/references/repository-writing-policy.md

- **Result:** PASS
- **Exit code:** 0
- **Findings:** 1
- **Hard findings:** 0
- **Baseline:** 0
- **Words:** 570
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **passive-voice** · .agent/skills/asd-ste100/references/repository-writing-policy.md:18:36 · **new** · fingerprint: fa71e22a78d6e4ce44e3a977
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is known

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
