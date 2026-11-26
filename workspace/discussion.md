# Discussion Register

## Current Step

- **2026-11-26 06:29 UTC:** Static path and link verification is complete for the scoped files. Pause pending the user's decision on whether to dispatch the hosted image-processing regression workflow. Do not run scripts locally or poll CI.
- **Active task:** [20261126-055004 — Adapt repository workflows to the refactor](tasks/20261126-055004-adapt-workflows-and-repair-refactor-breakage.md)

## Open Discussions

### Hosted regression validation

The image processor, regression fixtures, and GitHub Action now target `.takeout/images/`, but the test suite has not been executed. The GitHub Actions skill prohibits local execution and requires explicit user authorization for manual dispatch.

**Decision needed:** Should the hosted image-processing regression workflow be dispatched on branch `gpt`?

## Reports

_No reports._
