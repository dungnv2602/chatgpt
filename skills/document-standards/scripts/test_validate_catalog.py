#!/usr/bin/env python3
"""Regression tests for the Document Type Catalog validator."""
import tempfile
import unittest
from pathlib import Path

from validate_catalog import validate_catalog


HEADER = (
    "| Document type | Class | Current canonical format | "
    "Inventory finding / next action |\n"
    "|---|---|---|---|\n"
)


class CatalogValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.catalog = (
            self.root
            / "skills/document-standards/references/document-type-catalog.md"
        )
        self.catalog.parent.mkdir(parents=True)
        self.write("skills/example/assets/template.md")
        self.write("skills/example/SKILL.md")
        self.write("workspace/example.md")
        self.write("skills/example/processor.py")
        self.write("images/example/README.md")
        self.write("skills/example/test_processor.py")
        self.write("skills/example/generator.py")
        self.write("skills/example/test_generator.py")
        self.write("master/Example.md")
        self.write("novels/WORKFLOW.md")
        self.write("skills/drawing/SKILL.md")

    def tearDown(self):
        self.temp.cleanup()

    def write(self, relative_path):
        target = self.root / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("# fixture\n", encoding="utf-8")
        return target

    def set_catalog(self, rows):
        coverage = (
            "\\n## Markdown inventory coverage\\n\\n"
            "| Path pattern | Class | Canonical authority | Coverage rationale |\\n"
            "|---|---|---|---|\\n"
            "| `skills/**/*.md` | Lightweight pattern | "
            "`skills/example/SKILL.md` | Skill fixture. |\\n"
            "| `workspace/*.md` | Embedded contract | "
            "`workspace/example.md` and `skills/example/SKILL.md` | Workspace fixture. |\\n"
            "| `images/**/*.md` | Embedded contract | "
            "`images/example/README.md` and `skills/example/SKILL.md` | Image fixture. |\\n"
            "| `novels/*.md` | Embedded contract | "
            "`novels/WORKFLOW.md` and `skills/example/SKILL.md` | Novel fixture. |\\n"
        )
        self.catalog.write_text(
            "## Initial inventory\\n\\n" + HEADER + "\\n".join(rows) + coverage,
            encoding="utf-8",
        )

    def valid_rows(self):
        return [
            "| Example template | Template required | `skills/example/assets/template.md` | Use it. |",
            "| Embedded example | Embedded contract | `skills/example/SKILL.md` and `workspace/example.md` | Live contract. |",
            "| Example schema | Schema required | `skills/example/processor.py` and `images/example/README.md` | Tests: `skills/example/test_processor.py`. |",
            "| Example generator | Generator-owned | `skills/example/generator.py` | Tests: `skills/example/test_generator.py`. |",
            "| Example pattern | Lightweight pattern | `master/Example.md` | Reusable pattern. |",
            "| Example prose | Exempt | `novels/WORKFLOW.md` and `skills/drawing/SKILL.md` | Preserve creative form. |",
        ]

    def test_valid_catalog_accepts_all_document_classes(self):
        self.set_catalog(self.valid_rows())
        errors, row_count, reference_count = validate_catalog(
            self.root, self.catalog
        )
        self.assertEqual(errors, [])
        self.assertEqual(row_count, 6)
        self.assertGreaterEqual(reference_count, 11)

    def test_skill_template_must_live_in_assets(self):
        self.write("skills/example/references/template.md")
        self.set_catalog([
            "| Example template | Template required | "
            "`skills/example/references/template.md` | Misplaced. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("invalid template location" in error for error in errors))
        self.assertTrue(any("Misplaced skill template" in error for error in errors))

    def test_misplaced_named_template_is_detected_without_catalog_row(self):
        self.write("skills/example/references/hidden-template-library.md")
        self.set_catalog(self.valid_rows())
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any(
            "Misplaced skill template under references/" in error
            for error in errors
        ))

    def test_project_and_workspace_template_locations_are_allowed(self):
        self.write("novels/templates/scene-template.md")
        self.write("workspace/TASK_TEMPLATE.md")
        self.set_catalog([
            "| Novel scene | Template required | "
            "`novels/templates/scene-template.md` | Project-owned. |",
            "| Workspace task | Template required | "
            "`workspace/TASK_TEMPLATE.md` | Shared workspace template. |",
        ])
        errors, row_count, _ = validate_catalog(self.root, self.catalog)
        self.assertEqual(errors, [])
        self.assertEqual(row_count, 2)

    def test_missing_canonical_path_fails(self):
        rows = self.valid_rows()
        rows[0] = (
            "| Example template | Template required | "
            "`skills/example/missing-template.md` | Use it. |"
        )
        self.set_catalog(rows)
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("does not exist" in error for error in errors))

    def test_duplicate_document_type_fails(self):
        rows = self.valid_rows()
        rows.append(rows[0])
        self.set_catalog(rows)
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("duplicate document type" in error for error in errors))

    def test_unknown_document_class_fails(self):
        rows = self.valid_rows()
        rows[0] = (
            "| Example template | Unknown class | "
            "`skills/example/template.md` | Use it. |"
        )
        self.set_catalog(rows)
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("unknown document class" in error for error in errors))

    def test_schema_class_requires_regression_test_reference(self):
        rows = self.valid_rows()
        rows[2] = (
            "| Example schema | Schema required | "
            "`skills/example/processor.py` and `images/example/README.md` | "
            "No test path. |"
        )
        self.set_catalog(rows)
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("must reference a regression test" in error for error in errors))

    def test_github_and_consolidated_report_roots_are_allowed(self):
        self.write(".github/scripts/cleanup-archive.py")
        self.write(".github/archive-retention-state.json")
        self.write(".github/workflows/ste-lint-full-docs.yml")
        self.write("reports/lint_reports/latest-lint-report.md")
        self.write("reports/gh_ac_reports/README.md")
        self.write("reports/triage/README.md")
        rows = [
            "| Archive state | Embedded contract | "
            "`.github/scripts/cleanup-archive.py` and `.github/archive-retention-state.json` | Script-owned state. |",
            "| Lint report | Embedded contract | "
            "`.github/workflows/ste-lint-full-docs.yml` and `reports/lint_reports/latest-lint-report.md` | Workflow-owned report. |",
            "| Workflow definition | Exempt | "
            "`.github/workflows/ste-lint-full-docs.yml` | External Actions schema. |",
        ]
        self.set_catalog(rows)
        errors, row_count, _ = validate_catalog(self.root, self.catalog)
        self.assertEqual(errors, [])
        self.assertEqual(row_count, 3)

    def test_malformed_inventory_row_fails(self):
        self.set_catalog([
            "| Broken row | Exempt | `workspace/example.md` |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("expected 4 table cells" in error for error in errors))

    def test_directory_reference_is_rejected(self):
        (self.root / "workspace" / "docs").mkdir(parents=True)
        self.set_catalog([
            "| Directory reference | Lightweight pattern | `workspace/docs` | Not a file. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("referenced file does not exist" in error for error in errors))

    def test_embedded_contract_requires_owner_and_live_record(self):
        self.set_catalog([
            "| Embedded contract | Embedded contract | `workspace/example.md` | Only one path. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("must name its owner and live record" in error for error in errors))

    def test_generator_owned_requires_regression_test_reference(self):
        self.set_catalog([
            "| Generator | Generator-owned | `skills/example/generator.py` | No test reference. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("must reference a regression test" in error for error in errors))

    def test_generator_owned_requires_python_authority(self):
        self.set_catalog([
            "| Generator | Generator-owned | `workspace/example.md` | Regression test: `skills/example/test_generator.py`; no Python authority. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("must reference its Python authority" in error for error in errors))

    def test_template_class_requires_named_template(self):
        self.set_catalog([
            "| Template | Template required | `skills/example/SKILL.md` | Wrong path. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("must point to a named template" in error for error in errors))


    def replace_coverage(self, rows):
        content = self.catalog.read_text(encoding="utf-8")
        prefix = content.split("## Markdown inventory coverage", 1)[0]
        coverage = (
            "## Markdown inventory coverage\\n\\n"
            "| Path pattern | Class | Canonical authority | Coverage rationale |\\n"
            "|---|---|---|---|\\n"
            + "\\n".join(rows)
            + "\\n"
        )
        self.catalog.write_text(prefix + coverage, encoding="utf-8")

    def test_uncovered_markdown_document_fails(self):
        self.set_catalog(self.valid_rows())
        self.replace_coverage([
            "| `workspace/*.md` | Embedded contract | "
            "`workspace/example.md` and `skills/example/SKILL.md` | Narrow fixture. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("not covered by the catalog" in error for error in errors))

    def test_master_and_archive_markdown_are_excluded_from_coverage(self):
        self.set_catalog(self.valid_rows())
        self.write("master/new-reference.md")
        self.write("archive/old-record.md")
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertEqual(errors, [])

    def test_coverage_pattern_must_match_a_current_document(self):
        self.set_catalog(self.valid_rows())
        self.replace_coverage([
            "| `workspace/not-present-*.md` | Lightweight pattern | "
            "`workspace/example.md` | Stale pattern. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("matches no in-scope document" in error for error in errors))

    def test_coverage_pattern_rejects_path_traversal(self):
        self.set_catalog(self.valid_rows())
        self.replace_coverage([
            "| `workspace/../*.md` | Lightweight pattern | "
            "`workspace/example.md` | Unsafe pattern. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("unsafe or excluded Markdown coverage pattern" in error for error in errors))

    def test_missing_markdown_coverage_section_fails(self):
        self.set_catalog(self.valid_rows())
        content = self.catalog.read_text(encoding="utf-8")
        self.catalog.write_text(content.split("## Markdown inventory coverage", 1)[0], encoding="utf-8")
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("no '## Markdown inventory coverage' section" in error for error in errors))

    def test_path_traversal_is_rejected(self):
        rows = self.valid_rows()
        rows[0] = (
            "| Example template | Template required | "
            "`skills/../archive/template.md` | Unsafe. |"
        )
        self.set_catalog(rows)
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("unsafe or out-of-scope path" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
