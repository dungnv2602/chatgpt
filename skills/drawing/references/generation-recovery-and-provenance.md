# Drawing Recovery, Retry, and Provenance

### E2. Refusal-aware recovery and retry ownership

A tool refusal must not automatically become a request for the user to rewrite the prompt.

1. Read the refusal as a result, not as an invitation to resubmit the same prompt.
2. Review the request and authored prompt for explicit nudity, erotic activity, or sexual solicitation. Assess wording and staging that make the image overtly sexual.
3. If the user's underlying creative goal has a clearly non-explicit interpretation, preserve that goal while making a material change to the visual treatment. For example, move from bedroom/boudoir staging to a fashion or portrait setting. Use ordinary elegant clothing. Describe posture, expression, lighting, and composition without erotic instructions.
4. Do not use euphemisms to disguise a prohibited request, and do not try to defeat or probe safety systems. The revision must genuinely change the content into an allowed depiction.
5. Archive and commit the revised prompt before another call. Record each refusal and each materially revised attempt accurately.
6. After a refusal, make one meaningful autonomous revision when the safe intent is clear. If that safer version is also refused, do not continue with near-identical safety rewrites. However, first complete the prompt-interpretation audit in E2.1. If the audit shows assistant drift from a relevant, previously successful prompt, one bounded restoration may be justified as a diagnostic test. This is not permission for unlimited retries or for reproducing prohibited content.
7. Do not ask the user to say “retry” or write a new prompt when the intent is already clear. Ask only when a genuine creative choice is unresolved or the remaining request crosses a boundary that needs the user's decision.

Image tools may provide only a generic refusal message. Do not claim to know the exact trigger unless the tool identifies it. A refusal can be over-inclusive, but it must still be treated as a real failure for the attempt log.

### E2.1. Prompt-interpretation audit and proven-baseline recovery

**A refusal or unsuccessful result does not prove that the user's creative intent is disallowed. It does not prove that the reference image caused the refusal. It does not prove that the tool cannot produce the requested visual.** Diagnose the assistant's interpretation before you redesign the brief.

Before rewriting a prompt after a refusal, repeated failure, or user correction:

1. **Return to the evidence.** Identify the active series/artwork thread and
   inspect its authoritative chronological prompt history first. Locate the
   most recent successful prompt in that same series/thread and inspect the
   actual approved image assets where relevant. Use the relevant
   `drawings/YYYY-MM-DD/README.md` as a navigation aid, then review chronology,
   series membership, finalized outcome, and prompt/output linkage in the
   authoritative attempt records. For a novel scene, use its scene-local
   illustration history. Do not rely on memory, a summary, or the most recent
   failed prompt alone.
2. **Find the correct series baseline first.** Identify the active primary
   series and inspect its most recent prompt. Use the most recent successful
   prompt in that same series as the execution baseline. If no series applies
   but the work is an identifiable continuation of one artwork/thread, use the
   most recent successful prompt for that exact thread. A success from another
   series or artwork is not a substitute merely because it shares a subject or
   style. Search the broader prompt history only when you cannot identify a
   series or exact continuing artwork thread. Use the strongest comparable
   success only in that case.
3. **Audit prompt drift.** Compare the user's actual brief and successful baseline against the new authored prompt. Identify every element the assistant added. Examples include identity-preservation claims, extra scene details, wardrobe changes, more restrictive coverage, modified framing, sensuality labels, repeated negative clauses, and unnecessary safety disclaimers. Ask which changes the user requested and which are genuinely necessary.
4. **Restore before redesigning.** First determine that the user's goal is unchanged, the relevant archived baseline achieved it, and the content remains within applicable policy. Then restore the successful authored prompt verbatim or make only the smallest user-requested change. An earlier refusal does not justify replacing an approved open neckline, off-shoulder garment, romantic mood, or other defining feature. Do not substitute a high neckline, conservative fashion portrait, different outfit, or different setting without user direction.
5. **Do not over-engineer safety language.** Use clear positive descriptions of the intended allowed image. Do not stack unnecessary phrases such as repeated "no nudity / no cleavage / no suggestive pose" clauses. Avoid those clauses when they were not part of the successful baseline and do not address a concrete issue. Such additions can distort the user's brief. They may also foreground interpretations the user did not request. This does not reduce or bypass the actual safety review.
6. **Treat references as a deliberate choice.** Determine whether an image
   reference is needed for identity, style, or composition. If the proven
   successful method was fresh text-to-image generation without a reference,
   do not attach an image merely as ritual. Conversely, when a reference is
   needed, attach the actual asset through the supported mechanism and inspect
   that it was included. Never confuse an inspiration reference with an edit
   source.
7. **Separate observations from hypotheses.** Record the exact tool response.
   A generic refusal does not identify the offending word, visual feature,
   context, or attached reference. Label possible causes as hypotheses only.
   Do not present the assistant's interpretation as an internal tool diagnosis.
8. **Take user corrections seriously.** When the user says the assistant misread or over-restricted the request, reopen the successful history. Audit the assistant's own additions before defending the previous approach or blaming the tool. Do not make the user repeat a sufficiently clear brief.
9. **Use a bounded recovery sequence.** After a refusal, make one genuinely safety-aware revision if needed. If that revision also fails, stop similar rewrites. If the audit exposes a distinct assistant-made deviation from a relevant successful baseline, you may make one baseline-restoration attempt. Archive it before generation. If the restored baseline is also refused, stop and explain the limitation. Do not keep probing or submit cosmetic variations.
10. **Preserve the user's creative intent.** Keep safety review accurate and proportionate. Do not infer sexual intent from ordinary affection, fashion, exposed shoulders, or non-explicit anatomy. Successful historical outputs do not override current policy. Never recreate disallowed content or use prior acceptance to evade safeguards.

The purpose of this audit is to prevent assistant-created prompt drift, not to
guarantee that a tool will accept every prompt. The assistant owns its
interpretation and must test its assumptions against the project's actual
successful work.

### E2.2. Documented silk-wrap series and baseline-selection case

The November 12–13, 2026 silk-wrap portrait sequence is a historical example
of prompt lineage only. The current session brief controls creative direction. The latest **successful** prompt controls only historical prompt lineage:

- **Attempt 33** in `drawings/history/2026-11-12-image-prompts.md` established the
  successful Realistic portrait direction and produced two user-approved
  images. It is the original successful prompt in this portrait series.
- **Attempt 04** in `drawings/history/2026-11-13-image-prompts.md` reused Attempt 33's
  authored wording verbatim in a fresh generation. The assistant initially
  judged a garment-construction detail as missed. The user later explicitly
  assessed the Attempt 04 result as successful. That assessment supersedes the
  assistant's narrower preliminary judgment. The prompt-to-output association
  is explicit. Attempt 04 is therefore a user-approved success and the most
  recent successful prompt record in this series at the time of the archive.
- **Attempt 05** added one positive sentence about the silk panels overlapping
  across the bust, but the tool rejected the attempt and returned no image.
  It is a failed attempt, not a new baseline. Its wording must not replace or
  become the base prompt. The additional construction instruction is only a
  pending delta if the user still requests it in a future task. It must not be
  silently imposed on the approved Attempt 04 direction.
- **Attempt 06** attempted a localized edit of the actual Attempt 04 image.
  The source image was attached for that call, but the tool rejected the edit
  and returned no edited image. The original Attempt 04 image remained
  unchanged and user-approved. Attempt 06 is not a successful prompt or edit
  baseline. A future exact edit still requires the actual source asset to be
  attached in that future call. The historical file ID alone is not attachment.

**Operational lesson:** Attempt 04—not the newer failed Attempts 05 or 06—is
the latest user-approved successful prompt/output record in this series.
Attempt 33 remains its earlier successful origin and has the same authored
prompt wording. Any future successful prompt in this same series would
supersede Attempt 04 by chronology. This case also demonstrates that the
user's final assessment controls whether an output is accepted. An earlier
assistant assessment must not override a later explicit user approval.

  
### E2.5. Session-local image asset naming and provenance

Images supplied or selected for a drawing session are session-specific unless
the user explicitly says they should be retained for future use.

1. Inspect the actual image and identify its role in the current session:
   inspiration, identity, composition, style, exact edit source, keeper, or
   temporary comparison. Do not infer its role from its filename.
2. Use an image as a drawing reference only when the user assigns that role in
   the active session brief or a later explicit instruction. Do not silently
   promote a previously uploaded, approved, or stored image into a global or
   future-session default.
3. If the user requests retention in the repository, give the image a clear,
   descriptive, stable filename based on its visible content. For a set, use
   consistent names and numbered suffixes. If the user does not request
   retention, use the supplied image only within the current session.
4. **Preserve the original image exactly.** The default is rename-only. Preserve its bytes, format, extension, resolution, dimensions, metadata, and visual content. Do not recompress, resize, crop, rotate, filter, retouch, or strip metadata. The user authorized one repository workflow exception. An image submitted through `images/takeout/` with a ready `HANDOFF.yml` may move to its declared master path. The existing GitHub Action converts it to a separate WebP derivative. Keep the original bytes and format identical. Do not perform this conversion or relocation manually outside that hand-off pipeline.
5. Record the exact asset path, file/attachment ID, and source generation ID when known. Also record the original upload name, dimensions, byte size, checksum where available, and its session-specific role in that session's brief or attempt record.
   State whether the binary is stored in GitHub, the current conversation,
   or only the conversation. Never claim repository storage unless verified.
6. Link the image directly from the session brief or the relevant attempt note.
   Do not create or maintain a global image reference index. Do not add
   persistent face, outfit, palette, or style rules merely because an image was
   approved in an earlier session.
7. Keep inspiration references distinct from exact edit sources. A filename,
   repository path, repository path, or generation ID is not an attachment. Attach
   the actual asset through the image tool's supported mechanism and check
   source linkage before claiming a reference-guided result or source-linked edit.
8. For a user-approved output, record the approval and its exact originating
   prompt when reliably known. Approval makes the image a keeper. It does not
   make it a default visual direction for future sessions.

**GitHub rename and takeout rules:**

- If an image is already tracked in its permanent location under an opaque
  filename, rename that existing Git tree path using the same blob SHA. Review
  the old name is absent, the descriptive name exists, and the blob SHA and byte
  size are identical.
- For newly uploaded retained images, use the universal flat intake
  `images/takeout/`. Inspect the actual image, determine its descriptive title
  and destination, and prepare `images/takeout/HANDOFF.yml`. Do not manually
  rename or move it. The hand-off uses the exact uploaded filename, optional
  stable asset ID, descriptive title, and destination directory.
- The existing Action derives the permanent filename as
  `[asset-id-][slugified-title].[original-extension]` and keeps the original
  bytes unchanged. It stages each WebP under
  `images/takeout/webp/[batch-id]/attempt-NNN/`, appending `.webp` to the
  exact incoming filename (for example, `upload.png.webp`). After verification,
  it moves the master and WebP to the declared destination. It refuses
  collisions and verifies master SHA-256 and WebP integrity before clearing
  the hand-off.
- Failed attempts retain successfully converted WebPs in their staging folder
  for inspection. Retries use a new attempt number. A successful attempt moves
  its WebPs to final destinations and removes its now-empty staging folder.
- Each successful or failed attempt is archived with the original hand-off,
  `conversion-report.csv`, and `verification-report.md` under
  `images/takeout/history/[batch-id]/attempt-NNN/`. The CSV records staging
  and final paths. Do not claim repository storage or a successful hand-off
  until the final paths and reports are read back and verified.

### E4. Use daily attempt ledgers and authoritative records

Do not create a separate cross-session success catalogue. For non-novel
drawing sessions, use `drawings/YYYY-MM-DD/README.md` as the daily navigation
ledger. It must contain one contiguous Markdown table with exactly six fields:

1. **Attempt / prompt:** the attempt number or stable ID, a concise descriptive
   title, and a direct link to the full attempt record.
2. **Session / brief:** the session ID or name and a direct link to the active
   opening brief. If no separate brief exists, state that explicitly. Do not
   invent one.
3. **Series / baseline lineage:** the verified primary series ID/name and
   theme, plus the parent attempt or successful text baseline where known.
   Mark uncertain membership `legacy/unassigned` or `not established`
   rather than guessing.
4. **Execution outcome:** what actually happened—generated, edited with
   verified source linkage, rejected, blocked, pending, superseded, or
   unconfirmed—and whether the result met the defining acceptance criteria.
   Approval of a prompt for generation is not a successful image outcome.
5. **User approval / output evidence:** record user approval separately from
   the assistant's visual assessment. State whether an image was delivered in
   conversation, no output was returned, approval was not recorded, or storage
   and provenance remain unverified.
6. **Image:** link every generated image output after you upload its exact repository asset and read it back. Link it whether or not the user approved it or the result met the prompt. Include partial, off-target, superseded, and unapproved outputs. Approval belongs only in field 5. If an image was generated but its asset has not yet been uploaded, write `Waiting for image upload`.
   Use `—` only when no image was returned or generated. Use `Not verified`
   when the tool outcome is unconfirmed and no attempt-specific image can be
   attributed. Never withhold a generated-image link because the user rejected
   or did not approve the result.

Include every attempt in chronological order, including rejected, failed,
partial, pending, and superseded attempts. Do not turn the table into a
success-only list. Keep its six fields populated with concise, evidence-based
facts. Put the complete prompt, source IDs, exact tool metadata, acceptance
criteria, visual assessment, and detailed provenance in the linked attempt
record.

The daily README is a navigation and status summary, not an authority that can
override the attempt record. The attempt record is the source of truth for the
authored prompt, actual operation, source linkage, execution result, visual
assessment, user approval, and output identity. When the table and attempt
record disagree, correct the table from the verified attempt record.

For a named novel scene, keep the complete chronological prompt and output history in its local illustration records. Do not duplicate that history in a daily non-novel ledger. The scene-local record remains authoritative.

After each attempt is finalized:
- Update the attempt record with the actual result and its evidence.
- Update the corresponding row in the daily README, keeping each attempt in
  exactly one row and preserving chronological order.
- If the user explicitly approves an image, record that approval in the attempt
  record and the table's approval/output field without rewriting a different
  execution outcome. A user-approved keeper with uncertain prompt mapping must
  remain unlinked to an invented prompt.
- When the takeout workflow retains a generated image, add its verified WebP
  link to both the attempt record and the daily README's Image column. Do this
  even when the result was partial, off-target, superseded, or not approved.
  Do not make linking conditional on user approval. Do not link an unverified
  filename or infer prompt association.
- Do not omit unsuccessful attempts, promote a generated-but-missed-target
  result to a success, or infer approval from delivery alone.

The latest successful text baseline must be determined from the authoritative
attempt records within the active series or exact artwork thread. The daily
ledger helps locate those records. It does not define visual direction or
baseline eligibility.



## Technical documentation standard

This reference defines operational recovery and provenance procedures. Apply Strict mode from the repository [ASD-STE100 policy](../../asd-ste100/references/repository-writing-policy.md) when you revise it. Preserve safety limits, user approval, and prompt-lineage rules. Do not rewrite approved creative prompts or examples.
