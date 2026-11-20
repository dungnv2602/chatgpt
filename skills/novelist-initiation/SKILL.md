---
name: novelist-initiation
description: Initialize the novelist role and active novel project after the user requests formal novelist-role initialization and session startup has completed.
metadata:
  project-role: task-specific
  format: agentskills
---

# Novelist Initiation

This skill is the Agent Skills entry point for the repository's formal novelist-role initialization procedure.

## Activation

Activate only when the user explicitly requests formal novelist-role initialization after `start session` has completed. Do not treat this request as a session-start cue.

## Required order

1. Verify that foundational initialization has completed successfully in the current conversation.
2. If it has not, stop and ask the user to say `start session`. Do not begin novelist initialization.
3. Follow the complete canonical procedure in the Novelist role initialization section of `skills/SESSION_START.md`.
4. Do not infer permission to write a new scene or generate an illustration merely from role initialization. Follow the user's actual task instruction.

## Authority

- `skills/SESSION_START.md` defines foundational initialization.
- The Novelist role initialization section of `skills/SESSION_START.md` defines the complete role-and-project onboarding procedure.
- The active novel's canonical records govern story facts and continuity.
- User instructions and established project constraints remain authoritative.

This skill is task-specific. It is not part of universal foundational loading and must not be loaded automatically at the beginning of a conversation.


## Technical documentation standard

Apply the repository [ASD-STE100 policy](../asd-ste100/references/repository-writing-policy.md) when you revise this skill or its technical references. Use Strict mode for operational instructions. Use STE-flavored mode for explanations. Preserve meaning, scope, conditions, and modality. Do not rewrite creative content or approved prompts to satisfy a style check.
