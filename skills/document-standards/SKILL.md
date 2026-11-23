---
name: document-standards
description: Apply the repository's template-first policy when creating, revising, reviewing, or migrating recurring documents and structured records. Use when selecting templates, defining document types, checking structure, or preventing document-format drift.
metadata:
  project-role: foundational
  format: agentskills
---

# Document Standards

## Purpose

This skill enforces one documented format for each recurring document type.

It applies to documents, structured records, and generated reports in the approved project directories.

It supplements the workflow owned by each project skill. It does not replace that workflow.

## Core rule

Every recurring document type must use one canonical template, schema, or embedded format contract.

A template governs a document type. It does not require a separate template for every file.

Do not invent a new structure when the catalog identifies an approved format.

Do not create an empty document only because a template exists.

## Repository-wide Markdown inventory gate

The Document Type Catalog contains a Markdown inventory coverage register. The hosted validator scans every repository Markdown file outside the root `master/` and `archive/` directories and requires each path to match a documented family rule.

Before creating, moving, renaming, or materially revising a Markdown document:

1. Identify its exact destination path and match it to the coverage register.
2. Read the corresponding document-type row and its canonical authority.
3. If no coverage rule matches, add a narrow rule and classify the family before creating the document. Do not use a broad wildcard as a shortcut.
4. If the family is recurring or carries status, approval, provenance, or audit data, create or update its canonical template/schema first.
5. Update the owning index and workflow to reference the canonical format.

After the document change, check its structure against the canonical authority and run the hosted Document Standards workflow. Path coverage proves that a file belongs to a documented family; it does not prove that the file follows its template or is factually correct.

## Document type classes

Assign each document type one class in the [Document Type Catalog](references/document-type-catalog.md).

| Class | Use |
|---|---|
| Template required | A person creates the document repeatedly from a canonical template. |
| Schema required | A machine-readable record requires a defined field schema and allowed values. |
| Embedded contract | A single live file follows a structure defined by its owning skill, README, workflow, or script. |
| Generator-owned | A script creates the output. The generator and its tests define the format. |
| Lightweight pattern | A one-off or low-risk note needs consistent basic fields, not a full template. |
| Exempt | A rigid template would conflict with creative freedom or an external format. |

Use a template for optional document types when the user or workflow creates them. Do not create optional records solely to satisfy the catalog.

## Canonical asset placement

Use the owning workflow's canonical directory.

- Put skill-owned copy-ready templates and static schemas in the owning skill's `assets/` directory.
- Put explanatory references, policies, and research notes in `references/`.
- Put executable generators, processors, validators, and tests in `scripts/`.
- Keep project-level templates in the project's designated template directory, such as `novels/templates/`.
- Keep shared workspace templates in their canonical workspace location, such as `workspace/TASK_TEMPLATE.md`.
- Do not store copy-ready templates in a skill's `references/` directory.
- Do not create a second template when a generator, schema, or embedded contract already owns the format.

The catalog must point to the exact canonical asset. The owner skill and its indexes must use the same path.

## Authoring procedure

1. Identify the document type and its owning project workflow.
2. Match the destination path to the Markdown inventory coverage register and read the matching Document Type Catalog entry.
3. If no coverage rule matches, add a narrow family rule and classify the document type before creating the file.
4. Retrieve the exact canonical template, schema, or format contract.
5. Check that the canonical asset is in the correct owner directory.
6. If the format is missing, stop before creating or editing the governed document. Create the template or schema first.
7. Update the catalog and the owning workflow or index to point to the new format.
8. Commit and read back the canonical template, schema, coverage rule, catalog entry, and owner instructions.
9. Only after that read-back succeeds, create or revise the governed document.
10. Copy the template into a new document. Never edit the canonical template as the document itself.
11. Preserve required section names, order, field names, and allowed values.
12. Complete all required fields. Use the documented value for missing, unknown, or inapplicable information.
13. Include conditional sections only when their stated condition applies.
14. Keep optional sections when they add useful information. Do not invent content to fill them.
15. Remove unused placeholders before you commit the document.
16. Check the result against the template and its owning workflow.
17. Update the parent index when the document is created, renamed, reordered, or completed.
18. Commit the document and read back every changed path.

## When no template exists

Do not silently create a new recurring format.

1. Check whether the document type already exists under another name.
2. Check whether an owning skill defines an embedded contract or generator schema.
3. If the type is recurring or carries approval, status, provenance, safety, or audit data, define its template or schema first.
4. Put a skill-owned template in the owning skill's `assets/` directory.
5. Add the new type and its exact canonical path to the catalog.
6. Update the owning workflow and index.
7. Commit and read back those format changes.
8. Only then create or edit the governed document.
9. If the document is genuinely one-off, use a lightweight pattern and record the reason when the format affects later work.
10. Do not create a template for creative prose solely to constrain style or narrative form.

If the requirements remain unclear, define the document type and its field contract before creating the first record.

## Before editing an existing document

Treat a template change as a prerequisite, not as a later cleanup step.

1. Retrieve the current canonical template and the target document.
2. Check whether the target still follows the current format.
3. If the template needs a change, update the canonical template first.
4. Update the catalog and owner workflow in the same format-change step.
5. Commit and read back the format changes.
6. Only then edit the target document.
7. Preserve its approved content, provenance, and history. Do not mass-migrate unrelated records.

If the target uses an embedded contract or generator-owned format, retrieve that authority and its tests first. Do not create a duplicate template.

## Template design requirements

Every template or schema must define, as applicable:

- Document type and purpose.
- Required sections or fields.
- Conditional sections and their activation conditions.
- Optional sections.
- Field names, formats, and allowed values.
- Status and approval distinctions.
- Rules for missing, unknown, and inapplicable values.
- Stable identifiers and parent/child links.
- Version and migration rules.
- The owning workflow and validation method.

Keep required, conditional, and optional content visibly distinct.

- Treat every unmarked field as required.
- Mark an optional field with `Optional:`.
- Mark a conditional field with `Conditional:` and state its activation condition.
- Keep conditional sections only when their condition applies.
- Unless a type-specific schema defines another value, use `Unknown` when information is not established or cannot be verified, and `Not applicable` when the field does not apply.
- Do not use a blank value, `-`, `N/A`, or `TBD` as a substitute unless the template explicitly permits it.

Do not use a blank field to imply approval, completion, or verification.

Do not place workflow metadata inside a creative prompt or other user-facing content field.

## Versioning and migration

Use the version scheme already defined by the owning project when one exists.

Otherwise, use a simple major.minor version:

- Increment the major version when a change breaks the existing format.
- Increment the minor version when a change adds compatible fields or sections.
- Correct spelling or clarify instructions without changing the format without a version increment.

Update the canonical template, catalog, and owning workflow together when the format changes.

Migrate an existing document when you materially revise it or when a known risk requires migration.

Do not mass-rewrite historical or approved records only to change their template version.

Preserve user wording, creative content, approvals, provenance, and chronology during migration.

## Generator-owned formats and schemas

When code already parses or generates a structured format, treat that implementation as its schema authority.

- Record the exact script path and relevant schema constant or validation function in this catalog.
- Record the test file that covers the format.
- Do not create a second schema document unless the processor consumes it or another system requires it.
- Update the generator, its tests, and this catalog together when the format changes.
- Treat generated reports as read-only outputs. Do not maintain a manually edited template that duplicates their generator.

## Validation

Check each document for:

- Correct document type and canonical template.
- Correct template placement under its owning skill or project.
- Required sections and their order.
- Required fields and valid values.
- Removal of unused placeholders.
- Correct links, identifiers, and parent indexes.
- Accurate approval, status, and provenance.
- Compliance with the owning project's writing or data standard.

Add automated validation when a structural rule can be checked reliably.

The catalog integrity validator at `scripts/validate_catalog.py` checks inventory row structure, document-type classes, class-specific references, exact path existence, canonical template placement, and repository-wide Markdown path coverage. Its tests live at `scripts/test_validate_catalog.py`. It also detects named template files in skill reference directories. It does not prove that an agent copied the template when it authored a document. It does not compare every document with its template. It does not check semantic quality or duplicate processor schemas. The Worker enforces the authoring sequence. The hosted workflow `.github/workflows/validate-document-standards.yml` runs these checks for changes under `skills/**`, `novels/templates/**`, and the shared workspace template and owner files.

Run the validator and its tests only on GitHub-hosted Actions runners. Do not run repository scripts locally. Workflow integration requires explicit authorization. Until Actions runs both checks, treat execution as unverified.

Use the schema or generator tests for structured and machine-generated data.

Do not treat structural validation as proof of factual accuracy, user approval, or correct interpretation.

Do not weaken existing CI coverage to make a new template pass.

## Exceptions

Do not impose a rigid template when it conflicts with:

- Creative prose, dialogue, or an approved creative prompt.
- A one-off exploratory note with no repeated lifecycle.
- A format controlled by an external specification.
- A generated artifact whose format is defined by its generator.

Use the owning workflow's rules in those cases. Record a justified exception in the catalog when the exception is recurring.

## Ownership

The owning project skill maintains its templates and schemas.

The Document Type Catalog records their canonical paths and validation methods.

When a template changes, update its index and any workflow instructions that depend on it. Read back all changed paths before reporting completion.
