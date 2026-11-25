# Conversation Integrity — YYYY-MM-DD

**Template version:** 1.1

**Project:** [Project name or Not applicable]
**Branch:** `gpt`
**Companion files:** [Session summary path] · [Prompt history path or scene-local prompt record]

## Integrity policy

[State the record's source, coverage, and known limitations.]

## Chronological record

### YYYY-MM-DD HH:MM UTC — User message

> [Preserve the relevant user wording verbatim.]

### YYYY-MM-DD HH:MM UTC — Assistant response

[Preserve the relevant visible response.]

### YYYY-MM-DD HH:MM UTC — Tool event

- **Action:** [Describe the tool action.]
- **Observed result:** [Record the returned result.]
- **Reference:** [Exact path, commit, or source.]

[Repeat entries in chronological order. Label tool activity as a tool event, not dialogue.]

## Gaps and editorial summaries

- **Unavailable material:** [Identify the missing range or source.]
- **Editorial summary:** [Summarize unavailable material. Do not present it as a quote.]
- **Basis:** [State the available evidence used for the summary.]

[Write Not applicable when no gap exists.]

## Image source mapping

Record one row for every image output retained through the takeout workflow. Use the exact uploaded filename. Record the session attempt and source/platform Asset ID where applicable. This is distinct from the optional repository asset_id used to prefix a stored filename. Use the native Generation ID when exposed; otherwise use the recorded internal Output ID. Write `Not applicable` when a field does not apply. Do not infer or fabricate an identifier.

| Source filename | Attempt | Asset ID | Generation / Output ID |
|---|---|---|---|
| [exact filename] | [NN or Not applicable] | [exact ID or Not applicable] | [recorded ID or Not applicable] |

## Integrity and completeness notes

- **Coverage:** [Complete / Partial / Curated]
- **Transcription uncertainty:** [Details or None]
- **Omissions:** [Details or None]
- **Unverified details:** [Details or None]
- **Completeness limitation:** [State what this record does not establish.]
