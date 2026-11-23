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
        self.write("skills/example/template.md")
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
        self.catalog.write_text(
            "## Initial inventory\n\n" + HEADER + "\n".join(rows) + "\n",
            encoding="utf-8",
        )

    def valid_rows(self):
        return [
            "| Example template | Template required | `skills/example/template.md` | Use it. |",
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

    def test_github_and_lint_report_roots_are_allowed(self):
        self.write(".github/scripts/cleanup-archive.py")
        self.write(".github/archive-retention-state.json")
        self.write(".github/workflows/ste-lint-full-docs.yml")
        self.write("lint_reports/latest-lint-report.md")
        rows = [
            "| Archive state | Embedded contract | "
            "`.github/scripts/cleanup-archive.py` and `.github/archive-retention-state.json` | Script-owned state. |",
            "| Lint report | Embedded contract | "
            "`.github/workflows/ste-lint-full-docs.yml` and `lint_reports/latest-lint-report.md` | Workflow-owned report. |",
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
