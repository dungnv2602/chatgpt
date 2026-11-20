# Latest Repository-wide Lint Report

- **Run:** [#101](https://github.com/dungnv2602/chatgpt/actions/runs/44779673108)
- **Date (UTC):** 2026-11-20 17:04:36
- **Branch:** gpt
- **Commit:** [27050bb8e076efa047c901ecd1ae36a88a5c68ba](https://github.com/dungnv2602/chatgpt/commit/27050bb8e076efa047c901ecd1ae36a88a5c68ba)
- **Trigger:** workflow_dispatch

This report is replaced by the next complete run. The generated report is excluded from subsequent lint source scans.

## Summary

### Linter self-test

**Status:** PASS

~~~text
selftest OK
~~~

### Markdown links and heading anchors

**Status:** PASS

~~~text
Scanned 122 active Markdown files (180 available as link targets) and 287 local Markdown links.
Found 0 unresolved local Markdown targets or anchors.
~~~

- **Technical Markdown files scanned:** 40
- **Files with findings:** 32
- **Total STE findings (hard and advisory):** 295
- **Files failing the configured hard-finding threshold or execution:** 1
- **Overall result:** FAIL

## STE-100 Findings by File

#### `images/README.md`

~~~text
images/README.md:94:54 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are reserved]

1 violations (0 hard, baseline 0), 584 words, 0.2 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `images/takeout/README.md`

~~~text
images/takeout/README.md:180:40 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are reserved]

1 violations (0 hard, baseline 0), 1397 words, 0.1 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/agent-skill-authoring/SKILL.md`

~~~text
skills/agent-skill-authoring/SKILL.md:14:79 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are created]
skills/agent-skill-authoring/SKILL.md:160:29 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is loaded]
skills/agent-skill-authoring/SKILL.md:163:106 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is loaded]
skills/agent-skill-authoring/SKILL.md:167:23 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is loaded]
skills/agent-skill-authoring/SKILL.md:171:149 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has been loaded]
skills/agent-skill-authoring/SKILL.md:171:153 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been loaded]
skills/agent-skill-authoring/SKILL.md:184:36 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is known]
skills/agent-skill-authoring/SKILL.md:216:38 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been created]
skills/agent-skill-authoring/SKILL.md:238:28 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are focused]
skills/agent-skill-authoring/SKILL.md:239:65 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [have been introduced]
skills/agent-skill-authoring/SKILL.md:239:70 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been introduced]
skills/agent-skill-authoring/SKILL.md:247:17 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is connected]
skills/agent-skill-authoring/SKILL.md:249:37 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has been made]
skills/agent-skill-authoring/SKILL.md:249:41 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been made]
skills/agent-skill-authoring/SKILL.md:251:32 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has been read]
skills/agent-skill-authoring/SKILL.md:251:36 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been read]

16 violations (0 hard, baseline 6), 2250 words, 0.7 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/asd-ste100/README.md`

~~~text
skills/asd-ste100/README.md:26:35 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is known]
skills/asd-ste100/README.md:40:109 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is approved]

2 violations (0 hard, baseline 0), 1534 words, 0.1 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/asd-ste100/SKILL.md`

~~~text
skills/asd-ste100/SKILL.md:21:69 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was violated]
skills/asd-ste100/SKILL.md:39:133 long-sentence: Sentence has 28 words (cap 25). Split it. [28 words]
skills/asd-ste100/SKILL.md:45:227 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are defined]
skills/asd-ste100/SKILL.md:53:60 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is removed]
skills/asd-ste100/SKILL.md:54:99 phrasal-verb: Soft phrasal verb. Use the single plain verb (start, contact, read, begin). [Spin up]
skills/asd-ste100/SKILL.md:69:118 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is approved]
skills/asd-ste100/SKILL.md:70:53 nominalization: Action frozen into a noun. Use the verb (analyze, not perform an analysis of). [Perform an analysis]
skills/asd-ste100/SKILL.md:75:203 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [have received]
skills/asd-ste100/SKILL.md:77:140 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has completed]
skills/asd-ste100/SKILL.md:84:192 synonym-rotation: 'delete' and 'remove' name the same action. Pick one and use it every time. [delete]
skills/asd-ste100/SKILL.md:85:56 nominalization: Action frozen into a noun. Use the verb (analyze, not perform an analysis of). [perform an analysis]
skills/asd-ste100/SKILL.md:86:79 marketing-adjective: Marketing adjective. Delete, or replace with the measurement that earns the claim. [seamless]
skills/asd-ste100/SKILL.md:86:89 marketing-adjective: Marketing adjective. Delete, or replace with the measurement that earns the claim. [robust]
skills/asd-ste100/SKILL.md:86:107 marketing-adjective: Marketing adjective. Delete, or replace with the measurement that earns the claim. [cutting-edge]
skills/asd-ste100/SKILL.md:86:121 marketing-adjective: Marketing adjective. Delete, or replace with the measurement that earns the claim. [effortless]
skills/asd-ste100/SKILL.md:86:133 marketing-adjective: Marketing adjective. Delete, or replace with the measurement that earns the claim. [blazing-fast]
skills/asd-ste100/SKILL.md:88:29 phrasal-verb: Soft phrasal verb. Use the single plain verb (start, contact, read, begin). [spin up]
skills/asd-ste100/SKILL.md:88:38 phrasal-verb: Soft phrasal verb. Use the single plain verb (start, contact, read, begin). [reach out]
skills/asd-ste100/SKILL.md:88:49 phrasal-verb: Soft phrasal verb. Use the single plain verb (start, contact, read, begin). [dive into]
skills/asd-ste100/SKILL.md:88:60 phrasal-verb: Soft phrasal verb. Use the single plain verb (start, contact, read, begin). [kick off]
skills/asd-ste100/SKILL.md:109:134 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has stopped]
skills/asd-ste100/SKILL.md:142:58 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [were memorized]
skills/asd-ste100/SKILL.md:156:440 synonym-rotation: 'confirm' and 'check' name the same action. Pick one and use it every time. [confirms]

23 violations (15 hard, baseline 31), 2600 words, 0.9 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/asd-ste100/references/repository-writing-policy.md`

~~~text
skills/asd-ste100/references/repository-writing-policy.md:18:36 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is known]

1 violations (0 hard, baseline 0), 564 words, 0.2 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/asd-ste100/references/writing-rules.md`

~~~text
skills/asd-ste100/references/writing-rules.md:7:511 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has been]
skills/asd-ste100/references/writing-rules.md:26:84 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [have received]
skills/asd-ste100/references/writing-rules.md:26:129 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is allowed]
skills/asd-ste100/references/writing-rules.md:27:16 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are permitted]
skills/asd-ste100/references/writing-rules.md:30:16 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is required]
skills/asd-ste100/references/writing-rules.md:31:17 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is allowed]
skills/asd-ste100/references/writing-rules.md:37:58 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are capped]
skills/asd-ste100/references/writing-rules.md:50:5 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was designed]

8 violations (0 hard, baseline 6), 706 words, 1.1 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/conversation-mode/SKILL.md`

~~~text
skills/conversation-mode/SKILL.md:88:91 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is ordered]
skills/conversation-mode/SKILL.md:92:41 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is unresolved]
skills/conversation-mode/SKILL.md:111:175 synonym-rotation: 'fix' and 'correct' name the same action. Pick one and use it every time. [fix]
skills/conversation-mode/SKILL.md:111:195 synonym-rotation: 'confirm' and 'check' name the same action. Pick one and use it every time. [confirm]
skills/conversation-mode/SKILL.md:119:88 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is paused]
skills/conversation-mode/SKILL.md:120:78 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has stopped]
skills/conversation-mode/SKILL.md:120:108 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has proposed]
skills/conversation-mode/SKILL.md:121:61 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/conversation-mode/SKILL.md:121:213 synonym-rotation: 'verify' and 'check' name the same action. Pick one and use it every time. [verify]
skills/conversation-mode/SKILL.md:121:260 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is resolved]
skills/conversation-mode/SKILL.md:136:63 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/conversation-mode/SKILL.md:141:36 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was encountered]
skills/conversation-mode/SKILL.md:141:69 synonym-rotation: 'repair' and 'correct' name the same action. Pick one and use it every time. [repaired]
skills/conversation-mode/SKILL.md:143:106 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was verified]
skills/conversation-mode/SKILL.md:152:180 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is exceeded]
skills/conversation-mode/SKILL.md:174:260 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/conversation-mode/SKILL.md:188:94 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has approved]
skills/conversation-mode/SKILL.md:234:75 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are governed]

18 violations (4 hard, baseline 3), 2689 words, 0.7 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/drawing/SKILL.md`

~~~text
skills/drawing/SKILL.md:107:69 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is requested]
skills/drawing/SKILL.md:159:31 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is packaged]
skills/drawing/SKILL.md:177:35 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is known]
skills/drawing/SKILL.md:178:27 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is known]
skills/drawing/SKILL.md:179:35 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been loaded]
skills/drawing/SKILL.md:186:76 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is maintained]
skills/drawing/SKILL.md:225:21 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are wanted]
skills/drawing/SKILL.md:229:15 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is stored]
skills/drawing/SKILL.md:259:378 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is stored]
skills/drawing/SKILL.md:259:553 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is verified]
skills/drawing/SKILL.md:334:15 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is used]
skills/drawing/SKILL.md:339:22 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was edited]
skills/drawing/SKILL.md:349:216 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are satisfied]
skills/drawing/SKILL.md:366:19 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is refused]
skills/drawing/SKILL.md:398:42 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is verified]
skills/drawing/SKILL.md:399:50 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was produced]
skills/drawing/SKILL.md:400:42 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was returned]
skills/drawing/SKILL.md:404:11 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/drawing/SKILL.md:415:122 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is preserved]
skills/drawing/SKILL.md:428:24 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are determined]
skills/drawing/SKILL.md:454:13 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is Closed]

21 violations (0 hard, baseline 24), 4400 words, 0.5 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/drawing/references/archive-and-delivery.md`

~~~text
skills/drawing/references/archive-and-delivery.md:20:59 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are copied]
skills/drawing/references/archive-and-delivery.md:22:23 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is moved]
skills/drawing/references/archive-and-delivery.md:33:3 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are grouped]
skills/drawing/references/archive-and-delivery.md:34:36 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are processed]
skills/drawing/references/archive-and-delivery.md:45:16 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are paired]
skills/drawing/references/archive-and-delivery.md:46:35 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is recorded]
skills/drawing/references/archive-and-delivery.md:47:52 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are verified]
skills/drawing/references/archive-and-delivery.md:53:17 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is archived]
skills/drawing/references/archive-and-delivery.md:57:59 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are excluded]
skills/drawing/references/archive-and-delivery.md:59:23 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is cleared]
skills/drawing/references/archive-and-delivery.md:59:57 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is converted]
skills/drawing/references/archive-and-delivery.md:60:51 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are written]
skills/drawing/references/archive-and-delivery.md:66:70 synonym-rotation: 'check' and 'validate' name the same action. Pick one and use it every time. [checks]
skills/drawing/references/archive-and-delivery.md:76:74 synonym-rotation: 'verify' and 'validate' name the same action. Pick one and use it every time. [verify]
skills/drawing/references/archive-and-delivery.md:138:400 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [were expected]
skills/drawing/references/archive-and-delivery.md:157:37 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is paired]
skills/drawing/references/archive-and-delivery.md:158:76 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is verified]
skills/drawing/references/archive-and-delivery.md:169:26 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is retained]
skills/drawing/references/archive-and-delivery.md:173:1 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is described]

19 violations (2 hard, baseline 7), 2015 words, 0.9 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/drawing/references/generation-recovery-and-provenance.md`

~~~text
skills/drawing/references/generation-recovery-and-provenance.md:13:135 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is unresolved]
skills/drawing/references/generation-recovery-and-provenance.md:19:83 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is disallowed]
skills/drawing/references/generation-recovery-and-provenance.md:42:73 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is unchanged]
skills/drawing/references/generation-recovery-and-provenance.md:45:14 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/drawing/references/generation-recovery-and-provenance.md:47:74 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/drawing/references/generation-recovery-and-provenance.md:49:12 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was included]
skills/drawing/references/generation-recovery-and-provenance.md:86:20 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was attached]
skills/drawing/references/generation-recovery-and-provenance.md:97:52 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is accepted]
skills/drawing/references/generation-recovery-and-provenance.md:119:29 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is stored]
skills/drawing/references/generation-recovery-and-provenance.md:123:77 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was approved]
skills/drawing/references/generation-recovery-and-provenance.md:155:37 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is archived]
skills/drawing/references/generation-recovery-and-provenance.md:159:37 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are read]
skills/drawing/references/generation-recovery-and-provenance.md:181:62 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was delivered]
skills/drawing/references/generation-recovery-and-provenance.md:182:28 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was returned]
skills/drawing/references/generation-recovery-and-provenance.md:184:296 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was generated]
skills/drawing/references/generation-recovery-and-provenance.md:184:336 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been uploaded]
skills/drawing/references/generation-recovery-and-provenance.md:185:31 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was returned]
skills/drawing/references/generation-recovery-and-provenance.md:186:26 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is unconfirmed]
skills/drawing/references/generation-recovery-and-provenance.md:205:20 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is finalized]

19 violations (0 hard, baseline 17), 2757 words, 0.7 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/drawing/references/image-editing-protocol.md`

~~~text
skills/drawing/references/image-editing-protocol.md:26:193 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has approved]
skills/drawing/references/image-editing-protocol.md:28:82 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/drawing/references/image-editing-protocol.md:50:57 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is unconfirmed]

3 violations (0 hard, baseline 4), 913 words, 0.3 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/drawing/references/patterns/PATTERN-TEMPLATES.md`

~~~text
skills/drawing/references/patterns/PATTERN-TEMPLATES.md:15:40 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is retired]
skills/drawing/references/patterns/PATTERN-TEMPLATES.md:16:125 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are verified]
skills/drawing/references/patterns/PATTERN-TEMPLATES.md:20:67 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/drawing/references/patterns/PATTERN-TEMPLATES.md:98:246 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has tested]
skills/drawing/references/patterns/PATTERN-TEMPLATES.md:109:20 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are separated]
skills/drawing/references/patterns/PATTERN-TEMPLATES.md:111:15 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are described]
skills/drawing/references/patterns/PATTERN-TEMPLATES.md:113:19 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are recorded]

7 violations (0 hard, baseline 0), 446 words, 1.6 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/drawing/references/patterns/README.md`

~~~text
skills/drawing/references/patterns/README.md:34:143 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is superseded]

1 violations (0 hard, baseline 0), 442 words, 0.2 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/drawing/references/patterns/failure-patterns.md`

~~~text
skills/drawing/references/patterns/failure-patterns.md:3:126 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are indexed]
skills/drawing/references/patterns/failure-patterns.md:5:65 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are kept]
skills/drawing/references/patterns/failure-patterns.md:19:163 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is reversed]
skills/drawing/references/patterns/failure-patterns.md:22:89 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is observed]
skills/drawing/references/patterns/failure-patterns.md:37:14 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is concentrated]
skills/drawing/references/patterns/failure-patterns.md:48:20 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [were described]
skills/drawing/references/patterns/failure-patterns.md:51:37 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was modified]
skills/drawing/references/patterns/failure-patterns.md:61:190 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was attached]
skills/drawing/references/patterns/failure-patterns.md:61:219 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was rejected]
skills/drawing/references/patterns/failure-patterns.md:85:19 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is established]
skills/drawing/references/patterns/failure-patterns.md:91:257 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was returned]
skills/drawing/references/patterns/failure-patterns.md:120:226 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was identified]
skills/drawing/references/patterns/failure-patterns.md:136:66 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is prepared]
skills/drawing/references/patterns/failure-patterns.md:154:172 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was tested]
skills/drawing/references/patterns/failure-patterns.md:165:92 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is retained]
skills/drawing/references/patterns/failure-patterns.md:168:20 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was returned]
skills/drawing/references/patterns/failure-patterns.md:183:164 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is established]
skills/drawing/references/patterns/failure-patterns.md:194:52 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has corrected]
skills/drawing/references/patterns/failure-patterns.md:209:228 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was removed]
skills/drawing/references/patterns/failure-patterns.md:209:266 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was preserved]
skills/drawing/references/patterns/failure-patterns.md:210:242 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was adopted]
skills/drawing/references/patterns/failure-patterns.md:214:32 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is maintained]
skills/drawing/references/patterns/failure-patterns.md:218:179 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has rejected]

23 violations (0 hard, baseline 0), 1738 words, 1.3 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/drawing/references/patterns/successful-patterns.md`

~~~text
skills/drawing/references/patterns/successful-patterns.md:3:121 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are indexed]
skills/drawing/references/patterns/successful-patterns.md:25:23 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has been tested]
skills/drawing/references/patterns/successful-patterns.md:25:27 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been tested]
skills/drawing/references/patterns/successful-patterns.md:29:218 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [were returned]
skills/drawing/references/patterns/successful-patterns.md:30:188 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was reused]
skills/drawing/references/patterns/successful-patterns.md:47:158 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [being requested]

6 violations (0 hard, baseline 0), 816 words, 0.7 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/drawing/references/prompt-fidelity.md`

~~~text
skills/drawing/references/prompt-fidelity.md:13:215 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is measured]
skills/drawing/references/prompt-fidelity.md:15:69 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are retained]
skills/drawing/references/prompt-fidelity.md:46:115 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is phrased]
skills/drawing/references/prompt-fidelity.md:56:24 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been approved]
skills/drawing/references/prompt-fidelity.md:62:24 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has rejected]
skills/drawing/references/prompt-fidelity.md:74:32 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are prohibited]
skills/drawing/references/prompt-fidelity.md:80:35 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [being limited]
skills/drawing/references/prompt-fidelity.md:89:141 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been established]
skills/drawing/references/prompt-fidelity.md:91:171 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are covered]
skills/drawing/references/prompt-fidelity.md:116:33 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has specified]
skills/drawing/references/prompt-fidelity.md:119:41 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is depicted]
skills/drawing/references/prompt-fidelity.md:127:120 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is unspecified]
skills/drawing/references/prompt-fidelity.md:127:168 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has delegated]
skills/drawing/references/prompt-fidelity.md:151:163 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has delegated]
skills/drawing/references/prompt-fidelity.md:205:75 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has rejected]
skills/drawing/references/prompt-fidelity.md:224:41 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been restored]
skills/drawing/references/prompt-fidelity.md:225:103 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been added]
skills/drawing/references/prompt-fidelity.md:226:33 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been paraphrased]
skills/drawing/references/prompt-fidelity.md:227:123 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been introduced]
skills/drawing/references/prompt-fidelity.md:228:42 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been preserved]
skills/drawing/references/prompt-fidelity.md:229:26 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been limited]
skills/drawing/references/prompt-fidelity.md:230:23 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been converted]
skills/drawing/references/prompt-fidelity.md:245:66 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [being submitted]
skills/drawing/references/prompt-fidelity.md:248:30 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has been archived]
skills/drawing/references/prompt-fidelity.md:248:34 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been archived]
skills/drawing/references/prompt-fidelity.md:250:46 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is exposed]
skills/drawing/references/prompt-fidelity.md:252:98 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was submitted]
skills/drawing/references/prompt-fidelity.md:252:197 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was authorized]
skills/drawing/references/prompt-fidelity.md:269:87 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has delegated]
skills/drawing/references/prompt-fidelity.md:280:57 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [have been checked]
skills/drawing/references/prompt-fidelity.md:280:62 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been checked]
skills/drawing/references/prompt-fidelity.md:281:99 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are preserved]
skills/drawing/references/prompt-fidelity.md:282:41 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [have been introduced]
skills/drawing/references/prompt-fidelity.md:282:46 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been introduced]
skills/drawing/references/prompt-fidelity.md:283:106 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [have been added]
skills/drawing/references/prompt-fidelity.md:283:111 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been added]
skills/drawing/references/prompt-fidelity.md:284:31 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has been restored]
skills/drawing/references/prompt-fidelity.md:284:35 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been restored]
skills/drawing/references/prompt-fidelity.md:286:58 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has been audited]
skills/drawing/references/prompt-fidelity.md:286:62 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been audited]
skills/drawing/references/prompt-fidelity.md:287:27 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has been removed]
skills/drawing/references/prompt-fidelity.md:287:31 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been removed]

42 violations (0 hard, baseline 15), 3314 words, 1.3 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/drawing/references/series-continuity-and-iteration.md`

~~~text
skills/drawing/references/series-continuity-and-iteration.md:44:40 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is inferred]
skills/drawing/references/series-continuity-and-iteration.md:50:245 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has declared]
skills/drawing/references/series-continuity-and-iteration.md:78:42 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is ordered]
skills/drawing/references/series-continuity-and-iteration.md:82:259 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has established]
skills/drawing/references/series-continuity-and-iteration.md:94:27 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are locked]
skills/drawing/references/series-continuity-and-iteration.md:134:15 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is given]
skills/drawing/references/series-continuity-and-iteration.md:140:14 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is given]
skills/drawing/references/series-continuity-and-iteration.md:164:73 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [being edited]
skills/drawing/references/series-continuity-and-iteration.md:177:31 synonym-rotation: 'check' and 'confirm' name the same action. Pick one and use it every time. [Check]
skills/drawing/references/series-continuity-and-iteration.md:177:77 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was attached]

10 violations (1 hard, baseline 9), 3262 words, 0.3 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/drawing/references/style-guide.md`

~~~text
skills/drawing/references/style-guide.md:60:31 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was classified]

1 violations (0 hard, baseline 0), 462 words, 0.2 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/philosophy-religion-asceticism/README.md`

~~~text
skills/philosophy-religion-asceticism/README.md:17:11 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are enabled]

1 violations (0 hard, baseline 0), 471 words, 0.2 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/philosophy-religion-asceticism/SKILL.md`

~~~text
skills/philosophy-religion-asceticism/SKILL.md:53:21 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/philosophy-religion-asceticism/SKILL.md:94:11 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is disputed]
skills/philosophy-religion-asceticism/SKILL.md:144:43 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are related]
skills/philosophy-religion-asceticism/SKILL.md:167:67 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is contested]
skills/philosophy-religion-asceticism/SKILL.md:178:68 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is supported]
skills/philosophy-religion-asceticism/SKILL.md:179:43 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [being asked]
skills/philosophy-religion-asceticism/SKILL.md:291:3 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been excluded]
skills/philosophy-religion-asceticism/SKILL.md:292:52 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been kept]

8 violations (0 hard, baseline 7), 2387 words, 0.3 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/philosophy-religion-asceticism/references/answer-patterns.md`

~~~text
skills/philosophy-religion-asceticism/references/answer-patterns.md:29:14 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is contested]

1 violations (0 hard, baseline 0), 235 words, 0.4 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md`

~~~text
skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:7:89 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is designed]
skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:15:1 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has been completed]
skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:15:5 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been completed]
skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:20:13 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is built]
skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:37:47 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is used]
skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:39:38 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is used]
skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:57:65 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [being used]
skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md:268:11 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [being used]

8 violations (0 hard, baseline 7), 2716 words, 0.3 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/philosophy-religion-asceticism/references/source-standards.md`

~~~text
skills/philosophy-religion-asceticism/references/source-standards.md:99:19 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [being discussed]
skills/philosophy-religion-asceticism/references/source-standards.md:194:41 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [being cited]

2 violations (0 hard, baseline 1), 1467 words, 0.1 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/session-archiving/SKILL.md`

~~~text
skills/session-archiving/SKILL.md:68:90 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is known]
skills/session-archiving/SKILL.md:122:41 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is mentioned]

2 violations (0 hard, baseline 7), 2041 words, 0.1 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/session-archiving/references/archive-records-and-image-prompts.md`

~~~text
skills/session-archiving/references/archive-records-and-image-prompts.md:13:64 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is curated]
skills/session-archiving/references/archive-records-and-image-prompts.md:47:8 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was completed]
skills/session-archiving/references/archive-records-and-image-prompts.md:67:20 synonym-rotation: 'verify' and 'confirm' name the same action. Pick one and use it every time. [verify]
skills/session-archiving/references/archive-records-and-image-prompts.md:152:21 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [being discussed]
skills/session-archiving/references/archive-records-and-image-prompts.md:161:11 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are limited]
skills/session-archiving/references/archive-records-and-image-prompts.md:189:164 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is added]
skills/session-archiving/references/archive-records-and-image-prompts.md:191:130 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is established]
skills/session-archiving/references/archive-records-and-image-prompts.md:195:343 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was rejected]
skills/session-archiving/references/archive-records-and-image-prompts.md:253:170 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was supplied]
skills/session-archiving/references/archive-records-and-image-prompts.md:256:23 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [being tested]
skills/session-archiving/references/archive-records-and-image-prompts.md:294:65 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was returned]
skills/session-archiving/references/archive-records-and-image-prompts.md:305:24 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is known]
skills/session-archiving/references/archive-records-and-image-prompts.md:322:28 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was attached]
skills/session-archiving/references/archive-records-and-image-prompts.md:334:33 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was supplied]
skills/session-archiving/references/archive-records-and-image-prompts.md:349:44 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was created]
skills/session-archiving/references/archive-records-and-image-prompts.md:359:68 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was delivered]
skills/session-archiving/references/archive-records-and-image-prompts.md:360:36 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was returned]
skills/session-archiving/references/archive-records-and-image-prompts.md:360:58 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is unverified]
skills/session-archiving/references/archive-records-and-image-prompts.md:363:4 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is uploaded]
skills/session-archiving/references/archive-records-and-image-prompts.md:364:78 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is recorded]
skills/session-archiving/references/archive-records-and-image-prompts.md:365:48 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was generated]
skills/session-archiving/references/archive-records-and-image-prompts.md:366:75 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was returned]
skills/session-archiving/references/archive-records-and-image-prompts.md:367:68 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is unconfirmed]
skills/session-archiving/references/archive-records-and-image-prompts.md:377:20 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is finalized]
skills/session-archiving/references/archive-records-and-image-prompts.md:381:53 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is renamed]
skills/session-archiving/references/archive-records-and-image-prompts.md:403:242 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is verified]
skills/session-archiving/references/archive-records-and-image-prompts.md:405:35 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is stored]
skills/session-archiving/references/archive-records-and-image-prompts.md:452:69 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is based]

28 violations (1 hard, baseline 20), 4447 words, 0.6 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/session-archiving/references/drawing-session-closeout.md`

~~~text
skills/session-archiving/references/drawing-session-closeout.md:17:227 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is Closed]

1 violations (0 hard, baseline 0), 612 words, 0.2 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/session-archiving/references/image-provenance-and-webp.md`

~~~text
skills/session-archiving/references/image-provenance-and-webp.md:12:63 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is required]
skills/session-archiving/references/image-provenance-and-webp.md:21:59 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are copied]
skills/session-archiving/references/image-provenance-and-webp.md:23:16 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is moved]
skills/session-archiving/references/image-provenance-and-webp.md:45:38 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is preserved]
skills/session-archiving/references/image-provenance-and-webp.md:50:11 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are reserved]
skills/session-archiving/references/image-provenance-and-webp.md:73:215 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are Verified]
skills/session-archiving/references/image-provenance-and-webp.md:94:206 synonym-rotation: 'verify' and 'validate' name the same action. Pick one and use it every time. [Verify]
skills/session-archiving/references/image-provenance-and-webp.md:94:241 synonym-rotation: 'check' and 'validate' name the same action. Pick one and use it every time. [checking]
skills/session-archiving/references/image-provenance-and-webp.md:105:12 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is intended]
skills/session-archiving/references/image-provenance-and-webp.md:113:276 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is updated]
skills/session-archiving/references/image-provenance-and-webp.md:122:37 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is paired]
skills/session-archiving/references/image-provenance-and-webp.md:123:76 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is verified]
skills/session-archiving/references/image-provenance-and-webp.md:134:26 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is retained]
skills/session-archiving/references/image-provenance-and-webp.md:138:1 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is described]

14 violations (2 hard, baseline 2), 1712 words, 0.8 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/the-worker/SKILL.md`

~~~text
skills/the-worker/SKILL.md:23:70 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has finished]

1 violations (0 hard, baseline 0), 1798 words, 0.1 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `workspace/README.md`

~~~text
workspace/README.md:45:22 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has started]

1 violations (0 hard, baseline 0), 394 words, 0.3 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `workspace/TASK_TEMPLATE.md`

~~~text
workspace/TASK_TEMPLATE.md:43:21 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was inspected]
workspace/TASK_TEMPLATE.md:70:20 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was checked]
workspace/TASK_TEMPLATE.md:71:23 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was checked]

3 violations (0 hard, baseline 0), 277 words, 1.1 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `workspace/task_board.md`

~~~text
workspace/task_board.md:7:110 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are removed]
workspace/task_board.md:7:137 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is exceeded]
workspace/task_board.md:7:162 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is preserved]

3 violations (0 hard, baseline 0), 272 words, 1.1 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

