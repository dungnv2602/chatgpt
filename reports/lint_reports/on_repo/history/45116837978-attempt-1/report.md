# Latest Repository-wide Lint Report

- **Run:** [#156](https://github.com/dungnv2602/chatgpt/actions/runs/45116837978)
- **Date (UTC):** 2026-11-23 05:17:49
- **Branch:** gpt
- **Commit:** [c7bf066b7fc27d57764467d0f038c1a3350201f2](https://github.com/dungnv2602/chatgpt/commit/c7bf066b7fc27d57764467d0f038c1a3350201f2)
- **Trigger:** push

This report is replaced by the next complete run. The generated report is excluded from subsequent lint source scans.

## Summary

### Linter self-test

**Status:** PASS

~~~text
selftest OK
~~~

### Markdown links and heading anchors

**Status:** FAIL (exit 1)

~~~text
  File "/home/runner/work/chatgpt/chatgpt/skills/asd-ste100/scripts/check_markdown_anchors.py", line 145
    return None
IndentationError: unexpected indent
~~~

- **Technical Markdown files scanned:** 49
- **Files with findings:** 39
- **Total STE findings (hard and advisory):** 456
- **Files failing the configured hard-finding threshold or execution:** 11
- **Overall result:** FAIL

## Exact Files Evaluated

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

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
skills/agent-skill-authoring/SKILL.md:136:110 synonym-rotation: 'start' and 'begin' name the same action. Pick one and use it every time. [Start]
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

17 violations (1 hard, baseline 6), 2259 words, 0.8 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md`

~~~text
skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md:38:8 synonym-rotation: 'verify' and 'check' name the same action. Pick one and use it every time. [Verify]

1 violations (1 hard, baseline 0), 166 words, 0.6 per 100 words
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
skills/conversation-mode/SKILL.md:94:157 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are ordered]
skills/conversation-mode/SKILL.md:100:230 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/conversation-mode/SKILL.md:101:60 synonym-rotation: 'verify' and 'check' name the same action. Pick one and use it every time. [verify]
skills/conversation-mode/SKILL.md:102:129 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/conversation-mode/SKILL.md:105:3 long-sentence: Sentence has 32 words (cap 25). Split it. [32 words]
skills/conversation-mode/SKILL.md:105:95 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is paused]
skills/conversation-mode/SKILL.md:105:112 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/conversation-mode/SKILL.md:110:41 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is unresolved]
skills/conversation-mode/SKILL.md:137:88 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is paused]
skills/conversation-mode/SKILL.md:138:78 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has stopped]
skills/conversation-mode/SKILL.md:138:108 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has proposed]
skills/conversation-mode/SKILL.md:139:61 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/conversation-mode/SKILL.md:139:272 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is resolved]
skills/conversation-mode/SKILL.md:154:63 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/conversation-mode/SKILL.md:159:36 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was encountered]
skills/conversation-mode/SKILL.md:161:106 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was verified]
skills/conversation-mode/SKILL.md:170:180 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is exceeded]
skills/conversation-mode/SKILL.md:196:260 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/conversation-mode/SKILL.md:211:94 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has approved]
skills/conversation-mode/SKILL.md:238:126 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has been given]
skills/conversation-mode/SKILL.md:238:130 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been given]
skills/conversation-mode/SKILL.md:259:75 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are governed]

22 violations (5 hard, baseline 3), 3081 words, 0.7 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/document-standards/SKILL.md`

~~~text
skills/document-standards/SKILL.md:63:4 synonym-rotation: 'confirm' and 'check' name the same action. Pick one and use it every time. [Confirm]
skills/document-standards/SKILL.md:75:47 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is created]
skills/document-standards/SKILL.md:180:327 long-sentence: Sentence has 28 words (cap 25). Split it. [28 words]
skills/document-standards/SKILL.md:180:450 synonym-rotation: 'validate' and 'check' name the same action. Pick one and use it every time. [validate]
skills/document-standards/SKILL.md:182:163 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/SKILL.md:197:37 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is defined]

6 violations (4 hard, baseline 0), 1606 words, 0.4 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/document-standards/references/document-type-catalog.md`

~~~text
skills/document-standards/references/document-type-catalog.md:4:162 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was truncated]
skills/document-standards/references/document-type-catalog.md:4:254 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [were inspected]
skills/document-standards/references/document-type-catalog.md:27:215 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:28:139 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was found]
skills/document-standards/references/document-type-catalog.md:29:196 long-sentence: Sentence has 27 words (cap 25). Split it. [27 words]
skills/document-standards/references/document-type-catalog.md:29:299 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:32:207 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:33:239 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:33:459 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [being uploaded]
skills/document-standards/references/document-type-catalog.md:36:277 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:42:155 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:42:276 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/document-standards/references/document-type-catalog.md:43:214 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is read]
skills/document-standards/references/document-type-catalog.md:43:330 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:44:264 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:45:139 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/document-standards/references/document-type-catalog.md:47:169 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:47:307 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/document-standards/references/document-type-catalog.md:48:174 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:49:290 synonym-rotation: 'check' and 'validate' name the same action. Pick one and use it every time. [checks]
skills/document-standards/references/document-type-catalog.md:57:382 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:58:302 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:59:406 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:60:165 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/document-standards/references/document-type-catalog.md:60:208 long-sentence: Sentence has 26 words (cap 25). Split it. [26 words]
skills/document-standards/references/document-type-catalog.md:79:39 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [were reviewed]
skills/document-standards/references/document-type-catalog.md:83:111 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:83:139 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:83:157 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:83:187 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:83:214 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:83:240 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:83:326 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:83:394 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:84:54 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:84:264 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:84:318 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:84:435 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:84:474 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has been approved]
skills/document-standards/references/document-type-catalog.md:84:478 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been approved]
skills/document-standards/references/document-type-catalog.md:85:136 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are established]
skills/document-standards/references/document-type-catalog.md:85:152 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:86:144 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:86:192 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:87:131 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is established]
skills/document-standards/references/document-type-catalog.md:87:146 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:87:206 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is planned]
skills/document-standards/references/document-type-catalog.md:87:217 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:88:199 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is planned]
skills/document-standards/references/document-type-catalog.md:88:222 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:89:73 long-sentence: Sentence has 27 words (cap 25). Split it. [27 words]
skills/document-standards/references/document-type-catalog.md:89:220 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:90:71 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:90:145 long-sentence: Sentence has 26 words (cap 25). Split it. [26 words]
skills/document-standards/references/document-type-catalog.md:90:196 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:90:261 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is uploaded]
skills/document-standards/references/document-type-catalog.md:90:368 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:98:293 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:100:41 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:100:60 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:100:226 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is justified]
skills/document-standards/references/document-type-catalog.md:102:62 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:102:110 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:103:58 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:103:136 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:103:251 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:105:79 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:105:189 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:107:88 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:108:129 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was found]
skills/document-standards/references/document-type-catalog.md:109:112 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:109:188 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:109:332 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:121:97 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:121:166 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:121:235 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:121:304 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:121:373 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:122:90 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:123:62 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:123:92 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:123:124 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:123:199 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are superseded]
skills/document-standards/references/document-type-catalog.md:123:287 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:124:173 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:125:80 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:125:128 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:125:332 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:126:113 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:126:189 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:126:298 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/document-standards/references/document-type-catalog.md:130:57 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was required]
skills/document-standards/references/document-type-catalog.md:135:73 synonym-rotation: 'repair' and 'fix' name the same action. Pick one and use it every time. [repair]
skills/document-standards/references/document-type-catalog.md:136:67 synonym-rotation: 'confirm' and 'validate' name the same action. Pick one and use it every time. [confirms]
skills/document-standards/references/document-type-catalog.md:136:124 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are permitted]
skills/document-standards/references/document-type-catalog.md:140:32 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is added]
skills/document-standards/references/document-type-catalog.md:148:185 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]

97 violations (74 hard, baseline 0), 2854 words, 3.4 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/drawing/SKILL.md`

~~~text
skills/drawing/SKILL.md:107:69 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is requested]
skills/drawing/SKILL.md:166:1 long-sentence: Sentence has 32 words (cap 25). Split it. [32 words]
skills/drawing/SKILL.md:166:376 long-sentence: Sentence has 29 words (cap 25). Split it. [29 words]
skills/drawing/SKILL.md:166:449 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/drawing/SKILL.md:166:827 long-sentence: Sentence has 29 words (cap 25). Split it. [29 words]
skills/drawing/SKILL.md:166:1076 long-sentence: Sentence has 27 words (cap 25). Split it. [27 words]
skills/drawing/SKILL.md:166:1100 synonym-rotation: 'verify' and 'check' name the same action. Pick one and use it every time. [verify]
skills/drawing/SKILL.md:166:1151 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is listed]
skills/drawing/SKILL.md:171:31 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is packaged]
skills/drawing/SKILL.md:189:35 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is known]
skills/drawing/SKILL.md:190:27 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is known]
skills/drawing/SKILL.md:191:35 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been loaded]
skills/drawing/SKILL.md:198:76 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is maintained]
skills/drawing/SKILL.md:237:21 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are wanted]
skills/drawing/SKILL.md:241:15 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is stored]
skills/drawing/SKILL.md:243:4 long-sentence: Sentence has 28 words (cap 25). Split it. [28 words]
skills/drawing/SKILL.md:257:5 long-sentence: Sentence has 34 words (cap 25). Split it. [34 words]
skills/drawing/SKILL.md:274:36 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/drawing/SKILL.md:305:378 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is stored]
skills/drawing/SKILL.md:305:553 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is verified]
skills/drawing/SKILL.md:353:46 synonym-rotation: 'confirm' and 'check' name the same action. Pick one and use it every time. [Confirm]
skills/drawing/SKILL.md:379:1 long-sentence: Sentence has 33 words (cap 25). Split it. [33 words]
skills/drawing/SKILL.md:384:23 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are governed]
skills/drawing/SKILL.md:390:60 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was used]
skills/drawing/SKILL.md:397:216 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are satisfied]
skills/drawing/SKILL.md:414:19 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is refused]
skills/drawing/SKILL.md:446:42 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is verified]
skills/drawing/SKILL.md:447:50 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was produced]
skills/drawing/SKILL.md:448:42 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was returned]
skills/drawing/SKILL.md:452:11 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/drawing/SKILL.md:458:1 long-sentence: Sentence has 27 words (cap 25). Split it. [27 words]
skills/drawing/SKILL.md:464:73 long-sentence: Sentence has 27 words (cap 25). Split it. [27 words]
skills/drawing/SKILL.md:465:131 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/drawing/SKILL.md:479:24 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are determined]
skills/drawing/SKILL.md:505:13 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is Closed]

35 violations (14 hard, baseline 24), 5064 words, 0.7 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/drawing/assets/attempt-template.md`

~~~text
skills/drawing/assets/attempt-template.md:61:53 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was returned]

1 violations (0 hard, baseline 0), 593 words, 0.2 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/drawing/assets/daily-index-template.md`

~~~text
skills/drawing/assets/daily-index-template.md:5:1 long-sentence: Sentence has 26 words (cap 25). Split it. [26 words]
skills/drawing/assets/daily-index-template.md:28:28 synonym-rotation: 'verify' and 'check' name the same action. Pick one and use it every time. [verify]

2 violations (2 hard, baseline 0), 214 words, 0.9 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/drawing/assets/pattern-entry-templates.md`

~~~text
skills/drawing/assets/pattern-entry-templates.md:17:40 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is retired]
skills/drawing/assets/pattern-entry-templates.md:18:125 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are verified]
skills/drawing/assets/pattern-entry-templates.md:22:67 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/drawing/assets/pattern-entry-templates.md:100:246 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has tested]
skills/drawing/assets/pattern-entry-templates.md:106:43 synonym-rotation: 'verify' and 'validate' name the same action. Pick one and use it every time. [verify]
skills/drawing/assets/pattern-entry-templates.md:111:20 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are separated]
skills/drawing/assets/pattern-entry-templates.md:113:15 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are described]
skills/drawing/assets/pattern-entry-templates.md:115:19 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are recorded]

8 violations (1 hard, baseline 0), 449 words, 1.8 per 100 words
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
skills/drawing/references/archive-and-delivery.md:78:4 long-sentence: Sentence has 28 words (cap 25). Split it. [28 words]
skills/drawing/references/archive-and-delivery.md:88:4 long-sentence: Sentence has 33 words (cap 25). Split it. [33 words]
skills/drawing/references/archive-and-delivery.md:96:17 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are allowed]
skills/drawing/references/archive-and-delivery.md:97:72 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is unresolved]
skills/drawing/references/archive-and-delivery.md:101:39 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been uploaded]
skills/drawing/references/archive-and-delivery.md:105:22 synonym-rotation: 'verify' and 'validate' name the same action. Pick one and use it every time. [verify]
skills/drawing/references/archive-and-delivery.md:168:47 synonym-rotation: 'correct' and 'repair' name the same action. Pick one and use it every time. [correct]
skills/drawing/references/archive-and-delivery.md:180:400 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [were expected]
skills/drawing/references/archive-and-delivery.md:199:37 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is paired]
skills/drawing/references/archive-and-delivery.md:200:76 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is verified]
skills/drawing/references/archive-and-delivery.md:211:26 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is retained]
skills/drawing/references/archive-and-delivery.md:215:1 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is described]

25 violations (5 hard, baseline 7), 2365 words, 1.1 per 100 words
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
skills/drawing/references/image-editing-protocol.md:5:1 long-sentence: Sentence has 26 words (cap 25). Split it. [26 words]
skills/drawing/references/image-editing-protocol.md:11:57 long-sentence: Sentence has 27 words (cap 25). Split it. [27 words]
skills/drawing/references/image-editing-protocol.md:28:1 long-sentence: Sentence has 29 words (cap 25). Split it. [29 words]
skills/drawing/references/image-editing-protocol.md:57:58 synonym-rotation: 'check' and 'verify' name the same action. Pick one and use it every time. [Check]

4 violations (4 hard, baseline 4), 965 words, 0.4 per 100 words
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
skills/drawing/references/patterns/failure-patterns.md:224:30 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is included]
skills/drawing/references/patterns/failure-patterns.md:250:20 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is maintained]

25 violations (0 hard, baseline 0), 2146 words, 1.2 per 100 words
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
skills/drawing/references/prompt-fidelity.md:182:140 synonym-rotation: 'modify' and 'change' name the same action. Pick one and use it every time. [modify]
skills/drawing/references/prompt-fidelity.md:198:63 synonym-rotation: 'confirm' and 'check' name the same action. Pick one and use it every time. [Confirm]
skills/drawing/references/prompt-fidelity.md:198:143 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is required]
skills/drawing/references/prompt-fidelity.md:225:75 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has rejected]
skills/drawing/references/prompt-fidelity.md:244:41 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been restored]
skills/drawing/references/prompt-fidelity.md:245:103 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been added]
skills/drawing/references/prompt-fidelity.md:246:33 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been paraphrased]
skills/drawing/references/prompt-fidelity.md:247:123 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been introduced]
skills/drawing/references/prompt-fidelity.md:248:42 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been preserved]
skills/drawing/references/prompt-fidelity.md:249:26 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been limited]
skills/drawing/references/prompt-fidelity.md:250:23 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been converted]
skills/drawing/references/prompt-fidelity.md:264:4 synonym-rotation: 'fetch' and 'retrieve' name the same action. Pick one and use it every time. [Fetch]
skills/drawing/references/prompt-fidelity.md:265:66 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [being submitted]
skills/drawing/references/prompt-fidelity.md:268:30 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has been archived]
skills/drawing/references/prompt-fidelity.md:268:34 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been archived]
skills/drawing/references/prompt-fidelity.md:270:46 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is exposed]
skills/drawing/references/prompt-fidelity.md:272:98 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was submitted]
skills/drawing/references/prompt-fidelity.md:272:197 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was authorized]
skills/drawing/references/prompt-fidelity.md:289:87 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has delegated]
skills/drawing/references/prompt-fidelity.md:300:57 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [have been checked]
skills/drawing/references/prompt-fidelity.md:300:62 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been checked]
skills/drawing/references/prompt-fidelity.md:301:99 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are preserved]
skills/drawing/references/prompt-fidelity.md:302:41 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [have been introduced]
skills/drawing/references/prompt-fidelity.md:302:46 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been introduced]
skills/drawing/references/prompt-fidelity.md:303:106 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [have been added]
skills/drawing/references/prompt-fidelity.md:303:111 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been added]
skills/drawing/references/prompt-fidelity.md:304:31 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has been restored]
skills/drawing/references/prompt-fidelity.md:304:35 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been restored]
skills/drawing/references/prompt-fidelity.md:306:58 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has been audited]
skills/drawing/references/prompt-fidelity.md:306:62 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been audited]
skills/drawing/references/prompt-fidelity.md:307:27 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has been removed]
skills/drawing/references/prompt-fidelity.md:307:31 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been removed]
skills/drawing/references/prompt-fidelity.md:309:42 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is assigned]
skills/drawing/references/prompt-fidelity.md:309:73 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was copied]

48 violations (3 hard, baseline 15), 3676 words, 1.3 per 100 words
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

#### `skills/github-actions/SKILL.md`

~~~text
skills/github-actions/SKILL.md:21:206 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are permitted]
skills/github-actions/SKILL.md:23:59 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is provided]
skills/github-actions/SKILL.md:33:40 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [have reached]
skills/github-actions/SKILL.md:33:62 synonym-rotation: 'remove' and 'delete' name the same action. Pick one and use it every time. [Remove]

4 violations (1 hard, baseline 0), 2481 words, 0.2 per 100 words
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
skills/session-archiving/SKILL.md:71:90 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is known]
skills/session-archiving/SKILL.md:125:41 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is mentioned]
skills/session-archiving/SKILL.md:133:339 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/session-archiving/SKILL.md:133:408 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is provided]

4 violations (1 hard, baseline 7), 2299 words, 0.2 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/session-archiving/assets/session-brief-template.md`

~~~text
skills/session-archiving/assets/session-brief-template.md:5:1 long-sentence: Sentence has 32 words (cap 25). Split it. [32 words]

1 violations (1 hard, baseline 0), 288 words, 0.3 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `skills/session-archiving/references/archive-records-and-image-prompts.md`

~~~text
skills/session-archiving/references/archive-records-and-image-prompts.md:13:64 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is curated]
skills/session-archiving/references/archive-records-and-image-prompts.md:29:8 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was completed]
skills/session-archiving/references/archive-records-and-image-prompts.md:49:20 synonym-rotation: 'verify' and 'confirm' name the same action. Pick one and use it every time. [verify]
skills/session-archiving/references/archive-records-and-image-prompts.md:84:21 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [being discussed]
skills/session-archiving/references/archive-records-and-image-prompts.md:93:11 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are limited]
skills/session-archiving/references/archive-records-and-image-prompts.md:121:164 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is added]
skills/session-archiving/references/archive-records-and-image-prompts.md:124:130 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is established]
skills/session-archiving/references/archive-records-and-image-prompts.md:128:343 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was rejected]
skills/session-archiving/references/archive-records-and-image-prompts.md:186:170 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was supplied]
skills/session-archiving/references/archive-records-and-image-prompts.md:189:23 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [being tested]
skills/session-archiving/references/archive-records-and-image-prompts.md:227:65 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was returned]
skills/session-archiving/references/archive-records-and-image-prompts.md:238:24 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is known]
skills/session-archiving/references/archive-records-and-image-prompts.md:255:28 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was attached]
skills/session-archiving/references/archive-records-and-image-prompts.md:267:33 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was supplied]
skills/session-archiving/references/archive-records-and-image-prompts.md:282:44 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was created]
skills/session-archiving/references/archive-records-and-image-prompts.md:292:68 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was delivered]
skills/session-archiving/references/archive-records-and-image-prompts.md:293:36 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was returned]
skills/session-archiving/references/archive-records-and-image-prompts.md:293:58 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is unverified]
skills/session-archiving/references/archive-records-and-image-prompts.md:296:4 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is uploaded]
skills/session-archiving/references/archive-records-and-image-prompts.md:297:78 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is recorded]
skills/session-archiving/references/archive-records-and-image-prompts.md:298:48 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was generated]
skills/session-archiving/references/archive-records-and-image-prompts.md:299:75 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was returned]
skills/session-archiving/references/archive-records-and-image-prompts.md:300:68 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is unconfirmed]
skills/session-archiving/references/archive-records-and-image-prompts.md:310:20 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is finalized]
skills/session-archiving/references/archive-records-and-image-prompts.md:314:53 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is renamed]
skills/session-archiving/references/archive-records-and-image-prompts.md:336:242 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is verified]
skills/session-archiving/references/archive-records-and-image-prompts.md:338:35 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is stored]
skills/session-archiving/references/archive-records-and-image-prompts.md:385:69 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is based]

28 violations (1 hard, baseline 20), 4527 words, 0.6 per 100 words
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
skills/the-worker/SKILL.md:54:61 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is provided]
skills/the-worker/SKILL.md:54:234 synonym-rotation: 'validate' and 'verify' name the same action. Pick one and use it every time. [validate]
skills/the-worker/SKILL.md:71:56 synonym-rotation: 'check' and 'verify' name the same action. Pick one and use it every time. [check]
skills/the-worker/SKILL.md:71:111 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is needed]
skills/the-worker/SKILL.md:212:86 synonym-rotation: 'remove' and 'delete' name the same action. Pick one and use it every time. [Remove]
skills/the-worker/SKILL.md:282:168 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has been verified]
skills/the-worker/SKILL.md:282:172 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [been verified]
skills/the-worker/SKILL.md:282:273 semicolon: STE bans the semicolon (Rule 8.1). Split into separate sentences. [;]
skills/the-worker/SKILL.md:300:5 synonym-rotation: 'fetch' and 'retrieve' name the same action. Pick one and use it every time. [Fetch]
skills/the-worker/SKILL.md:301:188 synonym-rotation: 'modify' and 'change' name the same action. Pick one and use it every time. [modify]

10 violations (6 hard, baseline 0), 3060 words, 0.3 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `workspace/README.md`

~~~text
workspace/README.md:45:22 present-perfect: Compound tense. Use simple past/present unless current relevance is the point (then keep and flag). [has started]

1 violations (0 hard, baseline 0), 436 words, 0.2 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `workspace/TASK_TEMPLATE.md`

~~~text
workspace/TASK_TEMPLATE.md:18:108 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is written]
workspace/TASK_TEMPLATE.md:46:21 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was inspected]
workspace/TASK_TEMPLATE.md:57:58 synonym-rotation: 'check' and 'verify' name the same action. Pick one and use it every time. [checks]
workspace/TASK_TEMPLATE.md:73:20 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was checked]
workspace/TASK_TEMPLATE.md:74:23 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [was checked]

5 violations (1 hard, baseline 0), 385 words, 1.3 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

#### `workspace/task_board.md`

~~~text
workspace/task_board.md:7:110 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [are removed]
workspace/task_board.md:7:137 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is exceeded]
workspace/task_board.md:7:162 passive-voice: Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant. [is preserved]
workspace/task_board.md:47:21 synonym-rotation: 'fix' and 'repair' name the same action. Pick one and use it every time. [Fix]

4 violations (1 hard, baseline 0), 274 words, 1.5 per 100 words
Hedges/modality (may, might, could) are never flagged: confidence is content.
~~~

