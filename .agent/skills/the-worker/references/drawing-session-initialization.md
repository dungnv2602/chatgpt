# Drawing-session Initialization

The Worker owns activation and prerequisite checks. This reference contains the drawing-session procedure only.

## Drawing session activation

The separate drawing-session cue is **`start a drawing session`**. Treat it as an instruction only. Ignore quoted, discussed, or hypothetical uses. This cue does not change foundational loading. It activates The Worker's drawing-session procedures after foundational initialization.

This cue starts a new drawing session. It does not replace the foundational initialization procedure.

1. Verify whether foundational initialization passed in the current conversation.
2. If it has not passed, stop drawing-session initialization and ask the user to say `/start`. Do not fetch foundational or Drawing skills until the user gives that explicit cue.
3. If foundational initialization already passed, reuse the verified foundational files. Do not load them again without a reason.
4. Load The Worker's `references/archive-records-and-image-prompts.md` and any other required archive/media references when they are not already verified. The Worker owns the session-brief, archive, and prompt-provenance procedures used by Drawing.
5. Fetch and read `.agent/skills/drawing/SKILL.md` and its required references: `.agent/skills/drawing/references/style-guide.md` and `.agent/skills/drawing/references/image-editing-protocol.md`. Reuse each file if it was already verified in this conversation.
6. Do not run a CI preflight after the Drawing skill loads. Review CI only when the drawing task changes or depends on a specific workflow, or when the user asks for CI diagnostics.
7. Start the drawing session under the Drawing skill. Establish its new opening brief and required session records before image generation or editing. For a named novel scene, use the scene-local illustration brief and records.
8. Continue with any drawing task included in the same instruction. If the user only asks to start the session, establish the session and ask only for essential brief details that are not available.

Do not load the Drawing skill during ordinary foundational initialization. If you loaded the Drawing skill and its required references for novelist work, reuse them when the user starts a drawing session.

