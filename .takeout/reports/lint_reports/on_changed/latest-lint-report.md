# On Changed STE Lint Evidence Report

- **Result:** Failed
- **Schema version:** 1.1.0
- **Run:** [#921](https://github.com/dungnv2602/chatgpt/actions/runs/45961810447)
- **Run ID / attempt:** 45961810447 / 1
- **Workflow:** STE Lint Changed Documentation
- **Branch / commit:** gpt / 6e6d035a10b63f2f8f4426e12f1441e023785318
- **Event:** push
- **Execution mode:** incremental
- **Baseline SHA:** 72ff6007b8bc12adc0fdd2eecf1163402c6c0a3d
- **Linter source SHA:** 6e6d035a10b63f2f8f4426e12f1441e023785318
- **Generated (UTC):** 2026-11-27T07:56:05.589282+00:00

## 1. Executive summary

| Measure | Result |
|---|---:|
| Files evaluated | 1 |
| Files that failed | 1 |
| Files with findings | 1 |
| Total findings | 9 |
| Hard findings | 5 |
| Advisory findings | 4 |
| New findings | 9 |
| Recurring findings | 0 |
| Resolved findings | 82 |
| Failed workflow checks | 1 |

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
| .agent/skills/the-worker/SKILL.md | FAIL | 9 | 5 | 0 | 5260 | 0.2 | 1 |

## 5. Findings by rule

Counts include hard and advisory findings.

| Rule | Findings |
|---|---:|
| passive-voice | 4 |
| semicolon | 2 |
| synonym-rotation | 2 |
| long-sentence | 1 |

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
Ran 4 tests in 0.367s

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

- **Result:** Passed
- **Exit code:** 0

~~~text
Scanned 1 changed Markdown sources (367 available as link targets) and 7 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

## 7. Baseline comparison

Fingerprints use the file path, rule, matched text, and diagnostic message. They support correlation across runs. They do not prove that two findings have identical meaning.

### New findings

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:135:79 · **new** · fingerprint: 1ead56a935297678d525088d
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove
- **passive-voice** · .agent/skills/the-worker/SKILL.md:142:40 · **new** · fingerprint: 58a47654e8fe2ff210753ac7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **semicolon** · .agent/skills/the-worker/SKILL.md:143:136 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · .agent/skills/the-worker/SKILL.md:229:91 · **new** · fingerprint: 448e62e062b885437ed3015e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **passive-voice** · .agent/skills/the-worker/SKILL.md:277:144 · **new** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized
- **long-sentence** · .agent/skills/the-worker/SKILL.md:282:3 · **new** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words
- **passive-voice** · .agent/skills/the-worker/SKILL.md:370:196 · **new** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:402:33 · **new** · fingerprint: 952a5f851897b7d21a178421
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirm
- **semicolon** · .agent/skills/the-worker/SKILL.md:406:317 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

### Recurring findings

None.

### Resolved findings

- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:33:125 · **resolved** · fingerprint: 23ba89c188bd721485225ac0
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:33:205 · **resolved** · fingerprint: 71fd369fd4ce87f3145d3f61
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are contained
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:37:57 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:42:32 · **resolved** · fingerprint: 0b78e160768da5f8fc81245e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are surfaced
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:46:184 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:50:263 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:72:40 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:72:92 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:74:105 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:76:181 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:80:163 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:83:120 · **resolved** · fingerprint: f344f235da524619c5f3958e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are represented
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:84:107 · **resolved** · fingerprint: b6f783768f9aa08d96bf979c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:84:247 · **resolved** · fingerprint: 9997ef7899ffcdb243897741
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are reviewed
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:86:3 · **resolved** · fingerprint: 8d237e4d80507b6e1ceceb31
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:90:177 · **resolved** · fingerprint: b29e4df2ee98e11a4663446d
  - **Level:** advisory-free
  - **Message:** Sentence has 34 words (cap 25). Split it.
  - **Matched text:** 34 words
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:90:364 · **resolved** · fingerprint: 9943dcb3a220dcbe0a08ff17
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:90:533 · **resolved** · fingerprint: 3d99cf816793019bd73c4f70
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:93:131 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:95:345 · **resolved** · fingerprint: 6ecaad7e08b08c8dc23c4ac5
  - **Level:** advisory-free
  - **Message:** 'delete' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** deletes
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:96:215 · **resolved** · fingerprint: d88c984bfabc22fedfc1df95
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is required
- **present-perfect** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:97:86 · **resolved** · fingerprint: 6a157062d0e778513b660642
  - **Level:** advisory
  - **Message:** Compound tense. Use simple past/present unless current relevance is the point (then keep and flag).
  - **Matched text:** has validated
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:111:162 · **resolved** · fingerprint: 8d237e4d80507b6e1ceceb31
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:115:3 · **resolved** · fingerprint: 95b3ae27d255dd6d3908c02c
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:115:67 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:115:115 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:116:3 · **resolved** · fingerprint: 23ba89c188bd721485225ac0
  - **Level:** advisory-free
  - **Message:** Sentence has 30 words (cap 25). Split it.
  - **Matched text:** 30 words
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:118:95 · **resolved** · fingerprint: e9a8ebb703f48aa4c6b3f8f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were inspected
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:119:24 · **resolved** · fingerprint: 87531091dab5fb40e4c2d4ea
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were run
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:119:83 · **resolved** · fingerprint: dfff58b82bd3b79192dfa4bf
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** was replayed
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:119:118 · **resolved** · fingerprint: e9a8ebb703f48aa4c6b3f8f5
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** were inspected
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:125:143 · **resolved** · fingerprint: 298a9b83f5adba5f46527b78
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are Done
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:126:57 · **resolved** · fingerprint: 0ed0ae36b993057bc70765a0
  - **Level:** advisory-free
  - **Message:** 'verify' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** Verify
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:127:21 · **resolved** · fingerprint: f85e8d2b3bb15312e48006c0
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is confused
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:128:107 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:128:181 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:130:22 · **resolved** · fingerprint: 3c01363d8fccb6632309a933
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is consumed
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:131:41 · **resolved** · fingerprint: 0a8fdd51c323d7e6c5184e93
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is accepted
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:133:109 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:134:122 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:145:206 · **resolved** · fingerprint: 579e397c39954135265f1d98
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is recorded
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:146:81 · **resolved** · fingerprint: 3d99cf816793019bd73c4f70
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:154:95 · **resolved** · fingerprint: 3d99cf816793019bd73c4f70
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:155:4 · **resolved** · fingerprint: 911fad1e156f4210f836f36c
  - **Level:** advisory-free
  - **Message:** Sentence has 36 words (cap 25). Split it.
  - **Matched text:** 36 words
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:155:69 · **resolved** · fingerprint: 14114c25a67a248bad384f1b
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is committed
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:155:214 · **resolved** · fingerprint: 9943dcb3a220dcbe0a08ff17
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are recorded
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:158:54 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:158:198 · **resolved** · fingerprint: 8b94e2d2ab83e942a9c53498
  - **Level:** advisory-free
  - **Message:** 'erase' and 'remove' name the same action. Pick one and use it every time.
  - **Matched text:** erase
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:165:76 · **resolved** · fingerprint: 4ac51bf8e7d9a3a6a83ec070
  - **Level:** advisory-free
  - **Message:** 'check' and 'validate' name the same action. Pick one and use it every time.
  - **Matched text:** checks
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:174:3 · **resolved** · fingerprint: 95b3ae27d255dd6d3908c02c
  - **Level:** advisory-free
  - **Message:** Sentence has 26 words (cap 25). Split it.
  - **Matched text:** 26 words
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:175:95 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:175:109 · **resolved** · fingerprint: b6f783768f9aa08d96bf979c
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is blocked
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:177:75 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:180:85 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:184:44 · **resolved** · fingerprint: d221a492c282d7321d65e77a
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:184:113 · **resolved** · fingerprint: e034604c115f5b656a6c5ab9
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is created
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:186:100 · **resolved** · fingerprint: e9365b9cbb59d135219ec64e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is claimed
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:201:81 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:206:85 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:3 · **resolved** · fingerprint: a05003d9352cc224b471287c
  - **Level:** advisory-free
  - **Message:** Sentence has 41 words (cap 25). Split it.
  - **Matched text:** 41 words
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:43 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:71 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:89 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:149 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:233 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:270 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:293 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:211:329 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:212:3 · **resolved** · fingerprint: 13f3933d006440387035088b
  - **Level:** advisory-free
  - **Message:** Sentence has 47 words (cap 25). Split it.
  - **Matched text:** 47 words
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:212:63 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:212:199 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:212:279 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:212:353 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:212:385 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:215:125 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **passive-voice** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:219:98 · **resolved** · fingerprint: 1667b4bb6e8771c9446dd6e3
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:219:135 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **long-sentence** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:220:3 · **resolved** · fingerprint: 8d237e4d80507b6e1ceceb31
  - **Level:** advisory-free
  - **Message:** Sentence has 28 words (cap 25). Split it.
  - **Matched text:** 28 words
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:221:71 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **synonym-rotation** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:221:140 · **resolved** · fingerprint: dbe769c0dba8d9167f6f8147
  - **Level:** advisory-free
  - **Message:** 'alter' and 'change' name the same action. Pick one and use it every time.
  - **Matched text:** altering
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:245:312 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;
- **semicolon** · workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md:250:164 · **resolved** · fingerprint: 235b8a3528fa8a066c7b86a4
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

## 8. Complete per-file diagnostics

This section includes every normalized finding with its rule, level, source location, message, matched text, fingerprint, and baseline classification. It also records file metrics and execution errors.

### .agent/skills/the-worker/SKILL.md

- **Result:** FAIL
- **Exit code:** 1
- **Findings:** 9
- **Hard findings:** 5
- **Baseline:** 0
- **Words:** 5260
- **Findings per 100 words:** 0.2

#### Complete diagnostics

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:135:79 · **new** · fingerprint: 1ead56a935297678d525088d
  - **Level:** advisory-free
  - **Message:** 'remove' and 'delete' name the same action. Pick one and use it every time.
  - **Matched text:** Remove

- **passive-voice** · .agent/skills/the-worker/SKILL.md:142:40 · **new** · fingerprint: 58a47654e8fe2ff210753ac7
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are deleted

- **semicolon** · .agent/skills/the-worker/SKILL.md:143:136 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

- **passive-voice** · .agent/skills/the-worker/SKILL.md:229:91 · **new** · fingerprint: 448e62e062b885437ed3015e
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is deleted

- **passive-voice** · .agent/skills/the-worker/SKILL.md:277:144 · **new** · fingerprint: 857e0d2fef3568ba9dff44ac
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** are authorized

- **long-sentence** · .agent/skills/the-worker/SKILL.md:282:3 · **new** · fingerprint: 6ceec6aac665e34ceb1f916d
  - **Level:** advisory-free
  - **Message:** Sentence has 33 words (cap 25). Split it.
  - **Matched text:** 33 words

- **passive-voice** · .agent/skills/the-worker/SKILL.md:370:196 · **new** · fingerprint: ce2bd2aefd327fda5d21b1cd
  - **Level:** advisory
  - **Message:** Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant.
  - **Matched text:** is Done

- **synonym-rotation** · .agent/skills/the-worker/SKILL.md:402:33 · **new** · fingerprint: 952a5f851897b7d21a178421
  - **Level:** advisory-free
  - **Message:** 'confirm' and 'check' name the same action. Pick one and use it every time.
  - **Matched text:** confirm

- **semicolon** · .agent/skills/the-worker/SKILL.md:406:317 · **new** · fingerprint: c9f0d9a4ac52efda5b4f9aea
  - **Level:** advisory-free
  - **Message:** STE bans the semicolon (Rule 8.1). Split into separate sentences.
  - **Matched text:** ;

## 9. Structured evidence and integrity

- **report.json:** Complete machine-readable run metadata, exact evaluated paths, original per-file JSON records, normalized findings, check output, and baseline comparisons.
- **integrity.json:** SHA-256 checksums for this Markdown report and report.json.
- **index.json:** Run locator and summary metadata, ordered newest first.
- **history:** Immutable report files for each run ID and attempt.
- Scope latest pointers advance only when a run number and attempt are not older than the current pointer.

A successful report-generation step does not mean the lint checks passed. The result above reflects the recorded file and check outcomes.
