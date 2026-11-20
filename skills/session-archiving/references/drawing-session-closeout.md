# Drawing-Session Closeout

## 8. Drawing-session closeout — user cue required

**The only closeout trigger is the user's direct cue: `end session`.**
Recognize it only as a standalone instruction, case-insensitive and allowing
surrounding punctuation. A quoted mention or discussion of the phrase does not
invoke it. Do not infer closeout from a pause, goodbye, a topic change, an
apparently final image, the start of another session, or the end of a chat.

### Active-session closeout reminder

While a drawing session is Active or Paused, append a brief, unobtrusive
reminder at the end of each response that continues or discusses that session,
stating that it remains open and the user can say `end session` for formal
closeout. This is a reminder only: it must not interrupt drawing, require a
reply, or pressure the user to close. Once the user invokes `end session`,
suppress the reminder during closeout. If closeout cannot be completed and the
session remains open, resume reminders in later responses that continue or
discuss that session. Stop reminding once the session is Closed. The reminder
does not itself trigger closeout.

Until the cue is received:
- Keep the drawing session marked `Active` or `Paused`; never mark it
  `Closed` merely because work has stopped temporarily.
- Preserve its current brief, prompt lineage, attempt outcomes, unresolved
  criteria, and next step.
- A new drawing session may begin with a new brief, but this does not close the
  preceding session. Mark the preceding `Active` session `Paused` and the new
  session `Active`.
- When a paused session is resumed, make it `Active` and pause any other
  currently `Active` session.

When the user sends `end session`, close the current drawing session under
discussion, whether its status is `Active` or `Paused`, without asking for a
second confirmation. If multiple non-closed sessions could reasonably be the
target, ask one concise question to identify the session before changing any
record; this is target clarification, not a second approval:

1. Stop further image generation/editing for that session.
2. Verify the opening brief and every amendment, and confirm all attempts are
   recorded in their authoritative locations. For non-novel work, verify that
   the daily `README.md` indexes every attempt in its single contiguous table.
   Reconcile the success-only prompt index when an attempt's finalized
   classification or approved-output listing requires an update. For a named
   novel scene, verify the scene-local illustration prompt/attempt records and
   their links instead of creating a duplicate daily log.
3. Verify every generated output separately, including its acceptance-criteria
   assessment, outcome, image/source identifier, and user approval status.
4. Ensure every attempt contains its prompt baseline provenance and prompt
   difference record: preserved, changed, and excluded details.
5. Identify the final approved image(s), their exact originating prompts, and
   any storage location that is actually verified. Do not label an unapproved
   or uncertain output as final.
6. Record unresolved requirements, failed attempts, missing source links,
   technical gaps, and any work intentionally left incomplete. Do not erase
   failures or silently mark them successful.
7. Update the session brief status to `Closed`; prepare or update the relevant
   session summary/handoff with completed work, approved outputs, unresolved
   items, and the next possible task.
8. Read back all changed records, including the applicable daily index,
   daily README and attempt records, scene-local records, and session summary/handoff. Verify
   their links and status. If archival verification fails, report the exact
   gap and do not claim a fully verified closeout.

The session brief status remains `Closed` even when unresolved requirements
remain. Record those unresolved items in the closeout summary/handoff; closure
records the session's state and does not imply that every image succeeded.

