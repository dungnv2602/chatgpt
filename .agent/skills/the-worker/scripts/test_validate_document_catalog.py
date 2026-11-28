#!/usr/bin/env python3
"""Regression tests for the Document Type Catalog validator."""
import tempfile
import unittest
from pathlib import Path

from validate_document_catalog import (
    find_external_templates,
    find_misplaced_skill_templates,
    template_location_error,
    validate_catalog,
)


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
            / ".agent/skills/the-worker/references/document-type-catalog.md"
        )
        self.catalog.parent.mkdir(parents=True)
        self.write(".agent/skills/example/assets/template.md")
        self.write(".agent/skills/example/SKILL.md")
        self.write(".agent/skills/the-worker/SKILL.md")
        self.write("workspace/example.md")
        self.write(".agent/skills/example/processor.py")
        self.write("images/example/README.md")
        self.write(".agent/skills/example/test_processor.py")
        self.write(".agent/skills/example/generator.py")
        self.write(".agent/skills/example/test_generator.py")
        self.write(".agent/skills/the-worker/scripts/process_takeout.py")
        self.write(".agent/skills/the-worker/scripts/test_process_takeout_unittest.py")
        self.write("master/Example.md")
        self.write("area/novel/WORKFLOW.md")
        self.write(".agent/skills/drawing/SKILL.md")

    def tearDown(self):
        self.temp.cleanup()

    def write(self, relative_path):
        target = self.root / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("# fixture\n", encoding="utf-8")
        return target

    def default_non_markdown_rows(self):
        return [
            "| `.agent/skills/example/*.py` | Python script | Active | "
            "`.agent/skills/example/SKILL.md` | skill-root | Fixture skill code. |",
            "| `.agent/skills/the-worker/scripts/*.py` | Python script | Active | "
            "`.agent/skills/the-worker/SKILL.md` | skill-scripts | Worker scripts and tests. |",
        ]

    def set_catalog(self, rows, extra_coverage=(), non_markdown_rows=None):
        coverage = (
            "\n## Markdown inventory coverage\n\n"
            "| Path pattern | Class | Coverage status | Canonical authority | Coverage rationale |\n"
            "|---|---|---|---|---|\n"
            "| `.agent/skills/**/*.md` | Lightweight pattern | Active |"
            "`.agent/skills/example/SKILL.md` | Skill fixture. |\n"
            "| `workspace/*.md` | Embedded contract | Active |"
            "`workspace/example.md` and `.agent/skills/example/SKILL.md` | Workspace fixture. |\n"
            "| `images/**/*.md` | Embedded contract | Active |"
            "`images/example/README.md` and `.agent/skills/example/SKILL.md` | Image fixture. |\n"
            "| `area/novel/*.md` | Embedded contract | Active |"
            "`area/novel/WORKFLOW.md` and `.agent/skills/example/SKILL.md` | Novel fixture. |\n"
            + "\n".join(extra_coverage)
            + ("\n" if extra_coverage else "")
        )
        artifact_rows = (
            self.default_non_markdown_rows()
            if non_markdown_rows is None else non_markdown_rows
        )
        non_markdown = (
            "\n## Governed non-Markdown artifact coverage\n\n"
            "| Path pattern | Artifact type | Coverage status | Canonical owner | Placement rule | Coverage rationale |\n"
            "|---|---|---|---|---|---|\n"
            + "\n".join(artifact_rows)
            + "\n"
        )
        self.catalog.write_text(
            "## Initial inventory\n\n" + HEADER + "\n".join(rows)
            + coverage + non_markdown,
            encoding="utf-8",
        )

    def valid_rows(self):
        return [
            "| Example template | Template required | `.agent/skills/example/assets/template.md` | Use it. |",
            "| Embedded example | Embedded contract | `.agent/skills/example/SKILL.md` and `workspace/example.md` | Live contract. |",
            "| Example schema | Schema required | `.agent/skills/example/processor.py` and `images/example/README.md` | Tests: `.agent/skills/example/test_processor.py`. |",
            "| Example generator | Generator-owned | `.agent/skills/example/generator.py` | Tests: `.agent/skills/example/test_generator.py`. |",
            "| Example pattern | Lightweight pattern | `master/Example.md` | Reusable pattern. |",
            "| Example prose | Exempt | `area/novel/WORKFLOW.md` and `.agent/skills/drawing/SKILL.md` | Preserve creative form. |",
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
        self.write(".agent/skills/example/references/template.md")
        self.set_catalog([
            "| Example template | Template required | "
            "`.agent/skills/example/references/template.md` | Misplaced. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("invalid template location" in error for error in errors))
        self.assertTrue(any("Misplaced skill template" in error for error in errors))

    def test_misplaced_named_template_is_detected_without_catalog_row(self):
        self.write(".agent/skills/example/references/hidden-template-library.md")
        self.set_catalog(self.valid_rows())
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any(
            "Misplaced skill template outside assets/" in error
            for error in errors
        ))

    def test_templates_must_live_in_owning_skill_assets(self):
        self.assertIsNone(
            template_location_error(".agent/skills/example/assets/template.md")
        )
        self.assertIsNone(
            template_location_error(".agent/skills/example/assets/templates/novel.md")
        )
        for path in (
            "area/novel/templates/scene-template.md",
            "workspace/TASK_TEMPLATE.md",
        ):
            self.assertIn("owning skill's assets/", template_location_error(path))

    def test_external_template_files_and_directories_are_detected(self):
        self.write("area/novel/templates/scene-template.md")
        self.write("workspace/TASK_TEMPLATE.md")
        self.write("workspace/tasks/example/subtasks/02-audit-document-template-coverage.md")
        self.write("workspace/tasks/example/subtasks/TASK_TEMPLATE.md")
        self.write("workspace/archive/TASK_TEMPLATE.md")
        self.write("master/template.md")
        errors = find_external_templates(self.root)
        self.assertEqual(len(errors), 3)
        self.assertTrue(all("Misplaced template outside skills" in error for error in errors))
        self.assertTrue(any("workspace/tasks/example/subtasks/TASK_TEMPLATE.md" in error for error in errors))
        self.assertFalse(any("02-audit-document-template-coverage.md" in error for error in errors))
        self.assertFalse(any("workspace/archive" in error for error in errors))
        self.assertFalse(any("master/" in error for error in errors))

    def test_empty_external_template_directory_is_detected(self):
        (self.root / "area" / "novel" / "templates").mkdir(parents=True)
        errors = find_external_templates(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("area/novel/templates", errors[0])

    def test_misplaced_skill_template_directory_is_detected(self):
        (self.root / ".agent" / "skills" / "example" / "references" / "templates").mkdir(parents=True)
        errors = find_misplaced_skill_templates(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("references/templates", errors[0])

    def test_missing_canonical_path_fails(self):
        rows = self.valid_rows()
        rows[0] = (
            "| Example template | Template required | "
            "`.agent/skills/example/missing-template.md` | Use it. |"
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
            "`.agent/skills/example/template.md` | Use it. |"
        )
        self.set_catalog(rows)
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("unknown document class" in error for error in errors))

    def test_schema_class_requires_regression_test_reference(self):
        rows = self.valid_rows()
        rows[2] = (
            "| Example schema | Schema required | "
            "`.agent/skills/example/processor.py` and `images/example/README.md` | "
            "No test path. |"
        )
        self.set_catalog(rows)
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("must reference a regression test" in error for error in errors))

    def test_github_workflows_are_covered_but_unowned_config_is_rejected(self):
        self.write(".github/task-validation-policy.json")
        self.write(".github/workflows/ste-lint-full-docs.yml")
        self.write(".takeout/reports/lint_reports/latest-lint-report.md")
        self.write(".takeout/reports/gh_ac_reports/README.md")
        self.write(".takeout/reports/triage/README.md")
        rows = [
            "| Lint report | Embedded contract | "
            "`.github/workflows/ste-lint-full-docs.yml` and "
            "`.takeout/reports/lint_reports/latest-lint-report.md` | "
            "Workflow-owned report. |",
            "| Workflow definition | Exempt | "
            "`.github/workflows/ste-lint-full-docs.yml` | External Actions schema. |",
        ]
        markdown_rows = [
            "| `.takeout/reports/lint_reports/*.md` | Lightweight pattern | Active |"
            "`.takeout/reports/lint_reports/latest-lint-report.md` | Lint fixture. |",
            "| `.takeout/reports/gh_ac_reports/*.md` | Lightweight pattern | Active |"
            "`.takeout/reports/gh_ac_reports/README.md` | Actions fixture. |",
            "| `.takeout/reports/triage/*.md` | Lightweight pattern | Active |"
            "`.takeout/reports/triage/README.md` | Ledger fixture. |",
        ]
        non_markdown_rows = self.default_non_markdown_rows() + [
            "| `.github/workflows/*.yml` | GitHub Actions workflow | Active | "
            "external: GitHub Actions workflow syntax | github-workflows | "
            "Workflow execution files. |",
        ]
        self.set_catalog(rows, markdown_rows, non_markdown_rows)
        errors, row_count, _ = validate_catalog(self.root, self.catalog)
        self.assertEqual(row_count, 2)
        self.assertEqual(len(errors), 1)
        self.assertIn(".github/task-validation-policy.json", errors[0])
        self.assertIn("not covered by the catalog", errors[0])

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
            "| Generator | Generator-owned | `.agent/skills/example/generator.py` | No test reference. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("must reference a regression test" in error for error in errors))

    def test_generator_owned_requires_python_authority(self):
        self.set_catalog([
            "| Generator | Generator-owned | `workspace/example.md` | Regression test: `.agent/skills/example/test_generator.py`; no Python authority. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("must reference its Python authority" in error for error in errors))

    def test_template_class_requires_named_template(self):
        self.set_catalog([
            "| Template | Template required | `.agent/skills/example/SKILL.md` | Wrong path. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("must point to a named template" in error for error in errors))


    def replace_coverage(self, rows):
        content = self.catalog.read_text(encoding="utf-8")
        prefix = content.split("## Markdown inventory coverage", 1)[0]
        remainder = content.split("## Governed non-Markdown artifact coverage", 1)
        if len(remainder) != 2:
            raise AssertionError("non-Markdown coverage section is missing")
        suffix = remainder[1]
        coverage = (
            "## Markdown inventory coverage\n\n"
            "| Path pattern | Class | Coverage status | Canonical authority | Coverage rationale |\n"
            "|---|---|---|---|---|\n"
            + "\n".join(rows)
            + "\n\n"
        )
        self.catalog.write_text(
            prefix + coverage + "## Governed non-Markdown artifact coverage" + suffix,
            encoding="utf-8",
        )

    def replace_non_markdown_coverage(self, rows):
        content = self.catalog.read_text(encoding="utf-8")
        prefix = content.split("## Governed non-Markdown artifact coverage", 1)[0]
        section = (
            "## Governed non-Markdown artifact coverage\n\n"
            "| Path pattern | Artifact type | Coverage status | Canonical owner | Placement rule | Coverage rationale |\n"
            "|---|---|---|---|---|---|\n"
            + "\n".join(rows)
            + "\n"
        )
        self.catalog.write_text(prefix + section, encoding="utf-8")

    def test_uncovered_markdown_document_fails(self):
        self.set_catalog(self.valid_rows())
        self.replace_coverage([
            "| `workspace/*.md` | Embedded contract | Active |"
            "`workspace/example.md` and `.agent/skills/example/SKILL.md` | Narrow fixture. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("not covered by the catalog" in error for error in errors))

    def test_master_and_archive_markdown_are_excluded_from_coverage(self):
        self.set_catalog(self.valid_rows())
        self.write("master/new-reference.md")
        self.write("workspace/archive/old-record.md")
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertEqual(errors, [])

    def test_historical_adrs_remain_in_workspace_adr_and_task_archives_are_excluded(self):
        self.write("workspace/adr/README.md")
        self.write("workspace/adr/0001-historical-decision.md")
        self.write("workspace/archive/task/20261124-103354/task.md")
        self.write(".agent/skills/example/assets/ADR_TEMPLATE.md")
        self.set_catalog(self.valid_rows(), [
            "| `workspace/adr/*.md` | Template required | Active |"
            "`.agent/skills/example/assets/ADR_TEMPLATE.md` | Historical and active ADRs share one flat folder. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertEqual(errors, [])

    def test_two_digit_task_subtask_pattern_covers_child_records(self):
        self.write("workspace/tasks/example/subtasks/02-child.md")
        self.set_catalog(self.valid_rows(), [
            "| `workspace/tasks/*/subtasks/??-*.md` | Template required | Active | "
            "`.agent/skills/example/assets/template.md` | Two-digit child IDs. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertEqual(errors, [])

    def test_coverage_pattern_must_match_a_current_document(self):
        self.set_catalog(self.valid_rows())
        self.replace_coverage([
            "| `workspace/not-present-*.md` | Lightweight pattern | Active |"
            "`workspace/example.md` | Stale pattern. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("matches no in-scope document" in error for error in errors))

    def test_reserved_coverage_pattern_allows_new_family_before_first_record(self):
        self.set_catalog(self.valid_rows(), [
            "| `area/drawing/new-family/*.md` | Template required | Reserved | "
            "`.agent/skills/example/assets/template.md` | New family is registered before its first record. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertEqual(errors, [])

    def test_reserved_coverage_pattern_must_activate_with_first_record(self):
        self.write("area/drawing/new-family/first-record.md")
        self.set_catalog(self.valid_rows(), [
            "| `area/drawing/new-family/*.md` | Template required | Reserved | "
            "`.agent/skills/example/assets/template.md` | First record now exists. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("Reserved Markdown coverage pattern already matches" in error for error in errors))

    def test_reserved_coverage_pattern_passes_after_activation(self):
        self.write("area/drawing/new-family/first-record.md")
        self.set_catalog(self.valid_rows(), [
            "| `area/drawing/new-family/*.md` | Template required | Active | "
            "`.agent/skills/example/assets/template.md` | First record now exists. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertEqual(errors, [])

    def test_optional_generator_output_pattern_allows_empty_family_after_reset(self):
        self.set_catalog(self.valid_rows(), [
            "| `.takeout/reports/lint_reports/on_*/history/**/*.md` | Generator-owned | Optional | "
            "`.agent/skills/example/generator.py` and `.agent/skills/example/test_generator.py` | "
            "Generated lint history may be empty immediately after a clean reset. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertEqual(errors, [])

    def test_optional_generator_output_pattern_covers_files_when_present(self):
        self.write(".takeout/reports/lint_reports/on_changed/history/run-1/report.md")
        self.set_catalog(self.valid_rows(), [
            "| `.takeout/reports/lint_reports/on_*/history/**/*.md` | Generator-owned | Optional | "
            "`.agent/skills/example/generator.py` and `.agent/skills/example/test_generator.py` | "
            "Generated lint history may be empty immediately after a clean reset. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertEqual(errors, [])

    def set_takeout_history_coverage(self):
        self.set_catalog(self.valid_rows())
        self.replace_coverage([
            "| `.agent/skills/**/*.md` | Lightweight pattern | Active |"
            "`.agent/skills/example/SKILL.md` | Skill fixture. |",
            "| `workspace/*.md` | Embedded contract | Active |"
            "`workspace/example.md` and `.agent/skills/example/SKILL.md` | Workspace fixture. |",
            "| `images/example/README.md` | Embedded contract | Active |"
            "`images/example/README.md` and `.agent/skills/example/SKILL.md` | Image fixture. |",
            "| `images/takeout/history/**/*.md` | Generator-owned | Optional |"
            "`.agent/skills/the-worker/scripts/process_takeout.py` and "
            "`.agent/skills/the-worker/scripts/test_process_takeout_unittest.py` | "
            "Generated verification reports may be absent after a clean reset. |",
            "| `area/novel/*.md` | Embedded contract | Active |"
            "`area/novel/WORKFLOW.md` and `.agent/skills/example/SKILL.md` | Novel fixture. |",
        ])

    def test_optional_takeout_history_coverage_allows_empty_family(self):
        self.set_takeout_history_coverage()
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertEqual(errors, [])

    def test_optional_takeout_history_coverage_covers_nested_reports(self):
        self.write(
            "images/takeout/history/2026-11-20-001/attempt-001/verification-report.md"
        )
        self.set_takeout_history_coverage()
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertEqual(errors, [])

    def test_optional_coverage_is_limited_to_generator_owned_outputs(self):
        self.set_catalog(self.valid_rows(), [
            "| `area/drawing/new-family/*.md` | Lightweight pattern | Optional | "
            "`.agent/skills/example/SKILL.md` | Optional is only for generated outputs. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("Optional Markdown coverage is limited" in error for error in errors))

    def test_unknown_coverage_status_fails(self):
        self.set_catalog(self.valid_rows(), [
            "| `area/drawing/new-family/*.md` | Template required | Pending | "
            "`.agent/skills/example/assets/template.md` | Invalid state. |",
        ])
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("unknown Markdown coverage status" in error for error in errors))

    def test_coverage_pattern_rejects_path_traversal(self):
        self.set_catalog(self.valid_rows())
        self.replace_coverage([
            "| `workspace/../*.md` | Lightweight pattern | Active |"
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


    def test_single_star_does_not_cross_directory(self):
        self.set_catalog(self.valid_rows())
        self.write("workspace/tasks/nested.md")
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("not covered by the catalog" in error for error in errors))

    def test_double_star_covers_nested_markdown(self):
        self.set_catalog(self.valid_rows())
        self.write(".agent/skills/example/nested/guide.md")
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertEqual(errors, [])

    def test_path_traversal_is_rejected(self):
        rows = self.valid_rows()
        rows[0] = (
            "| Example template | Template required | "
            "`.agent/skills/../workspace/archive/template.md` | Unsafe. |"
        )
        self.set_catalog(rows)
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("unsafe or out-of-scope path" in error for error in errors))


    def test_worker_policy_in_skill_assets_is_accepted(self):
        self.write(".agent/skills/the-worker/assets/task-validation/policy.json")
        rows = self.default_non_markdown_rows() + [
            "| `.agent/skills/the-worker/assets/task-validation/*.json` | "
            "Worker policy and schema | Active | `.agent/skills/the-worker/SKILL.md` | "
            "skill-assets | Canonical Worker policy assets. |",
        ]
        self.set_catalog(self.valid_rows(), non_markdown_rows=rows)
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertEqual(errors, [])

    def test_worker_policy_misplaced_in_github_fails_placement(self):
        self.write(".github/task-validation-policy.json")
        rows = self.default_non_markdown_rows() + [
            "| `.github/task-validation-policy.json` | Worker policy and schema | "
            "Active | `.agent/skills/the-worker/SKILL.md` | skill-assets | "
            "Misplaced Worker policy. |",
        ]
        self.set_catalog(self.valid_rows(), non_markdown_rows=rows)
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("invalid placement" in error for error in errors))

    def test_unregistered_non_markdown_artifact_fails_closed(self):
        self.write(".agent/skills/example/assets/new-policy.toml")
        self.set_catalog(self.valid_rows())
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any(
            "new-policy.toml" in error and "not covered by the catalog" in error
            for error in errors
        ))

    def test_duplicate_non_markdown_rules_fail(self):
        rows = self.default_non_markdown_rows() + [
            "| `.agent/skills/example/processor.py` | Python script | Active | "
            "`.agent/skills/example/SKILL.md` | skill-root | Duplicate rule. |",
        ]
        self.set_catalog(self.valid_rows(), non_markdown_rows=rows)
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("duplicate canonical ownership" in error for error in errors))

    def test_unknown_non_markdown_artifact_type_fails(self):
        rows = self.default_non_markdown_rows()
        rows[0] = rows[0].replace("Python script", "Unknown artifact")
        self.set_catalog(self.valid_rows(), non_markdown_rows=rows)
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("unknown non-Markdown artifact type" in error for error in errors))

    def test_non_markdown_artifact_type_must_match_file_suffix(self):
        rows = self.default_non_markdown_rows()
        rows[0] = rows[0].replace("Python script", "JSON schema")
        self.set_catalog(self.valid_rows(), non_markdown_rows=rows)
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("file type does not match" in error for error in errors))

    def test_stale_non_markdown_owner_fails(self):
        rows = self.default_non_markdown_rows()
        rows[0] = rows[0].replace(
            ".agent/skills/example/SKILL.md",
            ".agent/skills/example/missing-owner.md",
        )
        self.set_catalog(self.valid_rows(), non_markdown_rows=rows)
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("canonical owner does not match" in error for error in errors))

    def test_active_non_markdown_rule_must_match_a_file(self):
        rows = self.default_non_markdown_rows() + [
            "| `.agent/skills/example/assets/*.json` | JSON schema | Active | "
            "`.agent/skills/example/SKILL.md` | skill-assets | Stale family. |",
        ]
        self.set_catalog(self.valid_rows(), non_markdown_rows=rows)
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("Active non-Markdown pattern matches no file" in error for error in errors))

    def test_non_markdown_path_traversal_is_rejected(self):
        rows = self.default_non_markdown_rows() + [
            "| `.agent/skills/../workspace/*.json` | JSON schema | Active | "
            "`.agent/skills/example/SKILL.md` | skill-assets | Unsafe pattern. |",
        ]
        self.set_catalog(self.valid_rows(), non_markdown_rows=rows)
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any("unsafe or out-of-scope non-Markdown pattern" in error for error in errors))

    def test_valid_github_workflow_uses_external_schema_exemption(self):
        self.write(".github/workflows/validate.yml")
        rows = self.default_non_markdown_rows() + [
            "| `.github/workflows/*.yml` | GitHub Actions workflow | Active | "
            "external: GitHub Actions workflow syntax | github-workflows | "
            "Workflow definitions use GitHub's schema. |",
        ]
        self.set_catalog(self.valid_rows(), non_markdown_rows=rows)
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertEqual(errors, [])

    def test_missing_non_markdown_coverage_section_fails(self):
        self.set_catalog(self.valid_rows())
        content = self.catalog.read_text(encoding="utf-8")
        self.catalog.write_text(
            content.split("## Governed non-Markdown artifact coverage", 1)[0],
            encoding="utf-8",
        )
        errors, _, _ = validate_catalog(self.root, self.catalog)
        self.assertTrue(any(
            "no '## Governed non-Markdown artifact coverage' section" in error
            for error in errors
        ))

if __name__ == "__main__":
    unittest.main()
