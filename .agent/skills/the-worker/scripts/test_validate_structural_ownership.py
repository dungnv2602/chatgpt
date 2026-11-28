import tempfile
import unittest
from pathlib import Path

from validate_structural_ownership import CHECKS, validate


class StructuralOwnershipTests(unittest.TestCase):
    def make_root(self, root: Path) -> None:
        for rel, _markers in CHECKS.values():
            (root / rel).parent.mkdir(parents=True, exist_ok=True)

        (root / ".agent/SESSION_START.md").write_text(
            "# Session Start\n"
            "The sole session-start cue is /start.\n"
            "[The Worker](skills/the-worker/SKILL.md)\n",
            encoding="utf-8",
        )
        (root / ".agent/skills/the-worker/SKILL.md").write_text(
            "# The Worker\n## Authority and scope\n## Activation\n",
            encoding="utf-8",
        )
        (
            root / ".agent/skills/the-worker/references/conversation-mode.md"
        ).write_text(
            "# Conversation Mode\n"
            "## Presentation settings\n"
            "The selected mode controls presentation only.\n",
            encoding="utf-8",
        )
        (root / ".agent/INITIALIZATION_POLICY.md").write_text(
            "# Initialization Policy\n"
            "The Worker is the sole operational authority.\n"
            ".agent/SESSION_START.md\n"
            ".agent/skills/the-worker/SKILL.md\n"
            ".agent/skills/the-worker/references/conversation-mode.md\n",
            encoding="utf-8",
        )

    def test_valid_fixture(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_root(root)
            self.assertEqual(validate(root), [])

    def test_missing_required_markers_for_every_canonical_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_root(root)

            for rule, (relative_path, markers) in CHECKS.items():
                for marker in markers:
                    with self.subTest(rule=rule, marker=marker):
                        path = root / relative_path
                        original = path.read_text(encoding="utf-8")
                        self.assertIn(marker, original)
                        path.write_text(
                            original.replace(marker, "", 1), encoding="utf-8"
                        )
                        try:
                            errors = validate(root)
                            self.assertTrue(
                                any(
                                    f"{relative_path}: missing structural marker: {marker}"
                                    in error
                                    for error in errors
                                ),
                                errors,
                            )
                        finally:
                            path.write_text(original, encoding="utf-8")

    def test_missing_each_canonical_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_root(root)

            for rule, (relative_path, _markers) in CHECKS.items():
                with self.subTest(rule=rule, path=relative_path):
                    path = root / relative_path
                    path.unlink()
                    try:
                        errors = validate(root)
                        self.assertTrue(
                            any(
                                f"{rule}: missing canonical path: {relative_path}"
                                in error
                                for error in errors
                            ),
                            errors,
                        )
                    finally:
                        path.write_text("", encoding="utf-8")

    def test_extra_session_start_link(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_root(root)
            path = root / ".agent/SESSION_START.md"
            path.write_text(
                path.read_text(encoding="utf-8") + "[extra](other.md)\n",
                encoding="utf-8",
            )
            self.assertTrue(
                any("exactly one Worker pointer" in error for error in validate(root))
            )

    def test_unresolved_worker_pointer_target(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_root(root)
            path = root / ".agent/SESSION_START.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "skills/the-worker/SKILL.md", "skills/the-worker/MISSING.md"
                ),
                encoding="utf-8",
            )
            self.assertTrue(
                any("unresolved pointer target" in error for error in validate(root))
            )

    def test_forbidden_conversation_mode_sections(self):
        forbidden_sections = ("## Execution", "## Operating rules")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_root(root)
            path = (
                root / ".agent/skills/the-worker/references/conversation-mode.md"
            )
            original = path.read_text(encoding="utf-8")
            for section in forbidden_sections:
                with self.subTest(section=section):
                    path.write_text(
                        original + f"\n{section}\n", encoding="utf-8"
                    )
                    self.assertTrue(
                        any(
                            "unexpected operational section marker" in error
                            for error in validate(root)
                        )
                    )
            path.write_text(original, encoding="utf-8")

    def test_missing_worker_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_root(root)
            (root / ".agent/skills/the-worker/SKILL.md").unlink()
            self.assertTrue(
                any("missing canonical path" in error for error in validate(root))
            )


if __name__ == "__main__":
    unittest.main()
