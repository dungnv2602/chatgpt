# Drawing-Session Closeout

## 8. Drawing-session closeout — user cue required

**The only closeout trigger is the user's direct cue: `end session`.**

Recognize this cue only as a standalone instruction. Match it without regard to case. Allow surrounding punctuation. A quoted mention or discussion of the phrase does not invoke closeout.

Do not infer closeout from a pause, goodbye, or topic change. Do not infer it from an apparently final image, a new session, or the end of a chat.

### Active-session closeout reminder

At the end of each response about an Active or Paused drawing session, add a brief reminder. State that the session remains open. State that the user can say `end session` to request formal closeout.

This reminder must not interrupt drawing. It must not require a reply or pressure the user to close the session.

When the user invokes `end session`, suppress the reminder during closeout. If closeout cannot be completed and the session remains open, resume reminders in later responses about that session. Stop reminders when the session is Closed. The reminder does not trigger closeout.

Until the user gives the cue:

- Keep the drawing session marked `Active` or `Paused`. Never mark it `Closed` only because work stopped temporarily.
- Preserve its current brief, prompt lineage, attempt outcomes, unresolved criteria, and next step.
- A new drawing session may start with a new brief. This does not close the preceding session. Mark the preceding `Active` session `Paused` and the new session `Active`.
- When the user resumes a paused session, mark it `Active`. Pause any other session that is currently `Active`.

When the user sends `end session`, close the current drawing session under discussion. Apply this rule to sessions marked `Active` or `Paused`. Do not ask for a second confirmation.

If multiple non-closed sessions could be the target, ask one concise question to identify the session. Ask before changing any record. This is target clarification, not a second approval.

1. Stop further image generation or editing for that session.
2. Verify the opening brief and every amendment. Confirm that all attempts appear in their authoritative locations. For non-novel work, verify that the daily `README.md` indexes every attempt in one continuous table. Update the success-only prompt index when the final classification or approved-output list requires it. For a named novel scene, verify its scene-local prompt and attempt records. Do not create a duplicate daily log.
3. Verify each generated output separately. Check its acceptance criteria, outcome, image or source ID, and user approval status.
4. Confirm that each attempt records its prompt-baseline source and prompt differences. Record what the prompt preserves, changes, and excludes.
5. Identify the final approved images and their exact source prompts. Identify only storage locations that you verified. Do not label an unapproved or uncertain output as final.
6. Record unresolved requirements, failed attempts, missing source links, technical gaps, and intentionally incomplete work. Do not erase failures or mark them successful without evidence.
7. Update the session brief status to `Closed`. Prepare or update the relevant session summary or hand-off. Record completed work, approved outputs, unresolved items, and the next possible task.
8. Read back every changed record. Include the applicable daily index, daily README, attempt records, scene-local records, and session summary or hand-off. Verify all links and statuses. If verification fails, report the exact gap. Do not claim a fully verified closeout.

The session brief remains `Closed` even when requirements remain unresolved. Record those items in the closeout summary or hand-off. Closure records the session's state. It does not mean that every image succeeded.

## Documentation standard

This file is operational documentation. Apply Strict mode from the repository [ASD-STE100 policy](../../asd-ste100/references/repository-writing-policy.md) when you revise it. Preserve every trigger, state transition, exception, record, and verification requirement.
