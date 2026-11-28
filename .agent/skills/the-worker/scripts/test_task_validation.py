"""Regression tests for the ADR-0008 typed task verifier."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import task_validation as verifier


class TaskValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.name", "Task verifier tests"], cwd=self.root, check=True)

        self.policy_path = self.root / "policy.json"
        self.schema_path = self.root / "schema.json"
        self.adapters_path = self.root / "adapters.json"
        self.contract_path = self.root / "contract.json"
        self.script_path = self.root / "checks" / "check.py"
        self.script_path.parent.mkdir()
        self.script_path.write_text("raise SystemExit(0)\n", encoding="utf-8")

        self.policy = {
            "policy_id": "chatgpt-task-validation",
            "repository": "dungnv2602/chatgpt",
            "coordinator": {"bind_source_sha": True, "bind_policy_revision": True},
            "mandatory_checks": [{"id": "required-check"}],
        }
        self.schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "additionalProperties": False,
        }
        self.registry = {
            "schema_version": 1,
            "adapters": {
                "python-script": {
                    "accepts_shell": False,
                    "runtime": "python3",
                }
            },
        }
        self.contract = {
            "schema_version": 1,
            "source_sha": "0" * 40,
            "checks": [{
                "id": "task-check",
                "adapter": "python-script",
                "entrypoint": "checks/check.py",
                "args": [],
                "timeout_minutes": 1,
            }],
        }
        self._write_inputs()
        self._commit()
        self.source_sha = self._git("rev-parse", "HEAD")
        self.contract["source_sha"] = self.source_sha
        self.contract_path.write_text(json.dumps(self.contract), encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _git(self, *args: str) -> str:
        result = subprocess.run(
            ["git", *args], cwd=self.root, check=True, capture_output=True, text=True
        )
        return result.stdout.strip()

    def _commit(self) -> None:
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "fixture"], cwd=self.root, check=True)

    def _write_inputs(self) -> None:
        self.policy_path.write_text(json.dumps(self.policy), encoding="utf-8")
        self.schema_path.write_text(json.dumps(self.schema), encoding="utf-8")
        self.adapters_path.write_text(json.dumps(self.registry), encoding="utf-8")
        self.contract_path.write_text(json.dumps(self.contract), encoding="utf-8")

    def _validate(self):
        return verifier.validate_contract(
            self.root,
            self.policy,
            self.schema,
            self.registry,
            self.contract,
            self.source_sha,
            verifier.git_blob_sha(self.policy_path),
            self.policy_path,
        )

    def test_accepts_valid_exact_sha_contract(self) -> None:
        checks = self._validate()
        self.assertEqual(len(checks), 1)
        self.assertEqual(checks[0]["_resolved"], "checks/check.py")

    def test_rejects_duplicate_json_keys(self) -> None:
        with self.assertRaises(verifier.ContractError):
            verifier._unique_object([("source_sha", "a"), ("source_sha", "b")])

    def test_rejects_parent_traversal(self) -> None:
        with self.assertRaises(verifier.ContractError):
            verifier.safe_repo_path(self.root, "../outside.py")

    def test_rejects_unknown_adapter(self) -> None:
        self.contract["checks"][0]["adapter"] = "shell"
        with self.assertRaises(verifier.ContractError):
            self._validate()

    def test_rejects_duplicate_check_ids(self) -> None:
        self.contract["checks"].append(dict(self.contract["checks"][0], entrypoint="checks/other.py"))
        with self.assertRaises(verifier.ContractError):
            self._validate()

    def test_rejects_mandatory_check_override(self) -> None:
        self.contract["checks"][0]["id"] = "required-check"
        with self.assertRaises(verifier.ContractError):
            self._validate()

    def test_rejects_unsafe_arguments(self) -> None:
        self.contract["checks"][0]["args"] = ["value;touch"]
        with self.assertRaises(verifier.ContractError):
            self._validate()

    def test_rejects_unknown_contract_property(self) -> None:
        self.contract["unexpected"] = True
        with self.assertRaises(verifier.ContractError):
            self._validate()

    def test_rejects_wrong_source_sha(self) -> None:
        self.contract["source_sha"] = "f" * 40
        with self.assertRaises(verifier.ContractError):
            self._validate()

    def test_rejects_wrong_policy_blob_sha(self) -> None:
        with self.assertRaises(verifier.ContractError):
            verifier.validate_contract(
                self.root, self.policy, self.schema, self.registry, self.contract,
                self.source_sha, "f" * 40, self.policy_path,
            )

    def test_rejects_symlink_escape(self) -> None:
        outside = Path(self.temp.name).parent / "outside-task-check.py"
        outside.write_text("pass\n", encoding="utf-8")
        link = self.root / "checks" / "outside.py"
        link.symlink_to(outside)
        with self.assertRaises(verifier.ContractError):
            verifier.safe_repo_path(self.root, "checks/outside.py")

    def test_command_never_uses_a_shell(self) -> None:
        check = {
            "adapter": "python-script",
            "_resolved": "checks/check.py",
            "args": ["--safe"],
        }
        self.assertEqual(
            verifier.command_for(check),
            [sys.executable, "checks/check.py", "--safe"],
        )


if __name__ == "__main__":
    unittest.main()
