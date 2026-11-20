---
name: novelist-initiation
description: Initialize the novelist role and active novel project. Use when the user explicitly says "Be the novelist" or requests formal novelist-role initialization, after foundational initialization has completed.
metadata:
  project-role: task-specific
  activation-cue: "Be the novelist"
  format: agentskills
---

# Novelist Initiation

This skill is the Agent Skills entry point for the repository's formal novelist-role initialization procedure.

## Activation

Activate only when the user uses **"Be the novelist"** as an instruction or explicitly requests formal novelist-role initialization. Do not activate when the phrase is merely quoted, discussed, or hypothetical.

## Required order

1. Verify that foundational initialization has completed successfully in the current conversation.
2. If it has not, complete the foundational procedure in `skills/SESSION_START.md` first. Do not skip or duplicate its required steps.
3. Follow the complete canonical procedure in the “Be the novelist” section of `skills/SESSION_START.md`.
4. Do not infer permission to write a new scene or generate an illustration merely from role initialization. Follow the user's actual task instruction.

## Authority

- `skills/SESSION_START.md` defines foundational initialization.
- The “Be the novelist” section of `skills/SESSION_START.md` defines the complete role-and-project onboarding procedure.
- The active novel's canonical records govern story facts and continuity.
- User instructions and established project constraints remain authoritative.

This skill is task-specific. It is not part of universal foundational loading and must not be loaded automatically at the beginning of a conversation.


## Technical documentation standard

Apply the repository [ASD-STE100 policy](../asd-ste100/references/repository-writing-policy.md) when you revise this skill or its technical references. Use Strict mode for operational instructions. Use STE-flavored mode for explanations. Preserve meaning, scope, conditions, and modality. Do not rewrite creative content or approved prompts to satisfy a style check.
