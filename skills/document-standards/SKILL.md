---
name: document-standards
description: Apply the repository's template-first policy when creating, revising, reviewing, or migrating recurring documents and structured records. Use when selecting templates, defining document types, checking structure, or preventing document-format drift.
metadata:
  project-role: foundational
  format: agentskills
---

# Document Standards

## Purpose

This skill defines one canonical format for each recurring document type. It governs document format, not the owning workflow or document meaning.

## Document classes

Use the Document Type Catalog to assign one class:

| Class | Use |
|---|---|
| Template required | Copy a canonical template for each new record. |
| Schema required | Validate a structured record against its schema. |
| Embedded contract | Follow the format in one live owner file, workflow, or script. |
| Generator-owned | The generator and its tests define the output format. |
| Lightweight pattern | Use a small structure for a low-risk or one-off note. |
| Exempt | Preserve creative freedom or an external format. |

Do not create a separate template when an embedded contract or generator already owns the format.

## Repository-wide authoring gate

The catalog contains a Markdown path-coverage register. The hosted validator checks every Markdown file outside the root master and archive directories against that register. This check classifies paths. It does not prove that a document follows its template or is factually correct.

For JSON, YAML, CSV, and other structured files, use the exact schema, processor, generator, and tests listed in the catalog.

## Authoring transaction

Before creating, moving, renaming, or materially revising a document:

1. Identify its exact destination path and owner.
2. Match Markdown files to a narrow path rule. Match structured files to their catalogued schema or generator.
3. Read the document-type row and the owner's current instructions.
4. Retrieve the exact template, schema, or embedded contract and its relevant tests.
5. If the format or coverage rule is missing, define it first. Place the asset in the owner's canonical directory. Update the catalog, owner workflow, and parent index. Commit and read back these changes before editing the target.
6. Create or revise the target from the canonical authority. Keep required fields and sections. Include conditional content only when its condition applies. Remove unused placeholders. Do not invent values or approvals.
7. Update parent indexes and cross-links. Check the document against its format, workflow, and writing or data standard.
8. Commit and read back every changed path. Run structural validation only through the authorized GitHub-hosted workflow.

For an existing document, update its canonical format before migrating the target. Preserve approved content, provenance, and chronology. Do not mass-migrate untouched historical records.

For a one-off or exempt document, use a lightweight structure and record the reason when it affects later maintenance. Do not create templates solely to constrain creative prose.

## Canonical asset placement

- Skill-owned templates and static schemas belong in the owner's assets directory.
- Explanatory policies and references belong in references.
- Generators, processors, validators, and tests belong in scripts.
- Project templates belong in the project's designated directory, such as novels/templates.
- Shared workspace templates remain in workspace.
- Do not put copy-ready templates in references.

The catalog and owner indexes must link to the same exact canonical asset.

## Template and schema requirements

Define these items when they apply:

- Purpose and document type.
- Required, conditional, optional, and repeatable fields.
- Field names, types, formats, and allowed values.
- Status, approval, and provenance rules.
- Stable identifiers and parent links.
- Version, migration, and validation rules.
- Owning workflow and canonical asset path.

Treat unmarked fields as required. Mark optional fields with Optional:. Mark conditional fields with Conditional: and state the condition. Use Unknown for information that is not established. Use Not applicable when a field does not apply. Use another missing-value token only when the format permits it.

Do not use blank fields to imply approval, completion, or verification. Keep workflow metadata out of creative prompts and other user-facing fields.

## Versioning and migration

Use the owning project's version scheme. Otherwise, increment the major version for breaking changes and the minor version for compatible additions.

Update the canonical format, catalog, and owner workflow together. Migrate a record when you materially revise it or when a known risk requires migration. Do not rewrite historical records only to match a newer version.

## Generator-owned formats

Treat parsing and generation code as the authority when it defines a structured format.

- Record the exact script, schema function or constant, and regression test in the catalog.
- Do not create a second schema unless the processor consumes it or another system requires it.
- Update the generator, tests, catalog, and owner documentation together.
- Treat generated reports as read-only outputs.

## Validation and limits

The catalog validator at scripts/validate_catalog.py checks catalog rows, classes, exact references, canonical template placement, and Markdown path coverage. Its tests are in scripts/test_validate_catalog.py. It does not prove that an author copied a template, that every document conforms semantically, or that facts are correct.

The hosted workflow .github/workflows/validate-document-standards.yml runs the validator and tests for in-scope document and workflow changes. Do not run repository scripts locally. Do not claim hosted validation until a result is observed.

Use owner-specific schema or generator tests for structured data. Do not weaken coverage or validation to make a document pass.

## Ownership

The owning skill or project maintains its canonical formats and validation. This skill owns document classification, catalog integrity, and the authoring gate. The Worker enforces the gate during repository task execution.