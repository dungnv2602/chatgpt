---
name: document-standards
description: Apply the repository's template-first policy when creating, revising, reviewing, or migrating recurring documents and structured records. Use when selecting templates, defining document types, checking structure, or preventing document-format drift.
metadata:
  project-role: task-specific
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

## Document type classes

Assign each document type one class in the [Document Type Catalog](references/document-type-catalog.md).

| Class | Use |
|---|---|
| Template required | A person creates the document repeatedly from a canonical template. |
| Schema required | A machine-readable record requires a defined field schema and allowed values. |
| Embedded contract | A single live file follows a structure defined by its owning skill or README. |
| Generator-owned | A script creates the output. The generator and its tests define the format. |
| Lightweight pattern | A one-off or low-risk note needs consistent basic fields, not a full template. |
| Exempt | A rigid template would conflict with creative freedom or an external format. |

Use a template for optional document types when the user or workflow creates them. Do not create optional records solely to satisfy the catalog.

## Authoring procedure

1. Identify the document type and its owning project workflow.
2. Read the matching entry in the Document Type Catalog.
3. Retrieve the exact canonical template, schema, or format contract.
4. Copy the template into the new document. Never edit the canonical template as the document itself.
5. Preserve required section names, order, field names, and allowed values.
6. Complete all required fields. Use the documented value for missing, unknown, or inapplicable information.
7. Include conditional sections only when their stated condition applies.
8. Keep optional sections when they add useful information. Do not invent content to fill them.
9. Remove unused placeholders before you commit the document.
10. Check the result against the template and its owning workflow.
11. Update the parent index and catalog when the document type or canonical format changes.
12. Commit the result and read back every changed path.

## When no template exists

Do not silently create a new recurring format.

1. Check whether the document type already exists under another name.
2. Check whether an owning skill defines an embedded contract or generator schema.
3. If the type is recurring or carries approval, status, provenance, safety, or audit data, define its template or schema first.
4. Add the new type and its canonical path to the catalog.
5. If the document is genuinely one-off, use a lightweight pattern and record the reason when the format affects later work.
6. Do not create a template for creative prose solely to constrain style or narrative form.

Create the template and first document in the same change set when the new type is already understood. If its requirements remain unclear, define the type before creating repeated examples.

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

## Validation

Check each document for:

- Correct document type and canonical template.
- Required sections and their order.
- Required fields and valid values.
- Removal of unused placeholders.
- Correct links, identifiers, and parent indexes.
- Accurate approval, status, and provenance.
- Compliance with the owning project's writing or data standard.

Add automated validation when a structural rule can be checked reliably.

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
