#!/usr/bin/env python3
"""Validate and execute a typed ADR-0008 task-validation contract."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


class ContractError(ValueError):
    """Raised when policy, registry, or task contract data is invalid."""


class InfrastructureError(RuntimeError):
    """Raised when the verifier cannot establish or execute its environment."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ContractError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_object)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ContractError(f"Cannot read valid JSON from {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ContractError(f"Expected a JSON object in {path}")
    return value


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    payload = b"blob " + str(len(data)).encode("ascii") + b"\0" + data
    return hashlib.sha1(payload).hexdigest()


def git_head(root: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
            env={"PATH": os.environ.get("PATH", "/usr/bin:/bin")},
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise InfrastructureError(f"Cannot resolve checked-out source SHA: {exc}") from exc
    value = result.stdout.strip()
    if not re.fullmatch(r"[0-9a-f]{40}", value):
        raise InfrastructureError("Git returned an invalid source SHA")
    return value


def safe_repo_path(root: Path, value: str, *, must_exist: bool = True) -> Path:
    if not isinstance(value, str) or not value or len(value) > 240:
        raise ContractError("Entrypoint must be a non-empty repository-relative path")
    if value.startswith("/") or "\\" in value or "\x00" in value:
        raise ContractError(f"Unsafe entrypoint path: {value!r}")
    parts = value.split("/")
    if any(part in ("", ".", "..") for part in parts):
        raise ContractError(f"Unsafe entrypoint path: {value!r}")
    candidate = root.joinpath(*parts)
    try:
        resolved = candidate.resolve(strict=must_exist)
        resolved.relative_to(root)
    except (OSError, RuntimeError, ValueError) as exc:
        raise ContractError(f"Entrypoint escapes the repository or is unavailable: {value!r}") from exc
    if must_exist and (not resolved.is_file() and not resolved.is_dir()):
        raise ContractError(f"Entrypoint is not a file or directory: {value!r}")
    return resolved


def validate_contract(
    root: Path,
    policy: dict[str, Any],
    schema: dict[str, Any],
    registry: dict[str, Any],
    contract: dict[str, Any],
    expected_source_sha: str,
    expected_policy_blob_sha: str,
    policy_path: Path,
) -> list[dict[str, Any]]:
    if not re.fullmatch(r"[0-9a-f]{40}", expected_source_sha):
        raise ContractError("Expected source SHA must be 40 lowercase hexadecimal characters")
    if not re.fullmatch(r"[0-9a-f]{40}", expected_policy_blob_sha):
        raise ContractError("Expected policy blob SHA must be 40 lowercase hexadecimal characters")

    actual_source_sha = git_head(root)
    if actual_source_sha != expected_source_sha:
        raise ContractError("Checked-out commit does not match the coordinator source SHA")
    if git_blob_sha(policy_path) != expected_policy_blob_sha:
        raise ContractError("Policy blob does not match the coordinator's pinned policy revision")

    if policy.get("policy_id") != "chatgpt-task-validation":
        raise ContractError("Unexpected validation policy")
    if policy.get("repository") != "dungnv2602/chatgpt":
        raise ContractError("Policy repository does not match this repository")
    if policy.get("coordinator", {}).get("bind_source_sha") is not True:
        raise ContractError("Policy does not require exact source-SHA binding")
    if policy.get("coordinator", {}).get("bind_policy_revision") is not True:
        raise ContractError("Policy does not require policy-revision binding")
    if policy.get("coordinator", {}).get("activation_status") != "enabled":
        raise ContractError("Coordinator activation is not enabled")
    if policy.get("protection", {}).get("enforcement_status") != "verified":
        raise ContractError("Protected policy enforcement is not verified")

    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise ContractError("Unsupported task-contract schema")
    if schema.get("additionalProperties") is not False:
        raise ContractError("Task-contract schema must reject unknown top-level properties")
    schema_properties = schema.get("properties", {})
    check_schema = schema.get("$defs", {}).get("check", {})
    if not isinstance(schema_properties, dict) or not isinstance(check_schema, dict):
        raise ContractError("Task-contract schema is missing its property definitions")
    if schema_properties.get("source_sha", {}).get("pattern") != "^[0-9a-f]{40}$":
        raise ContractError("Task-contract schema does not enforce exact source SHA values")
    if check_schema.get("additionalProperties") is not False:
        raise ContractError("Task check schema must reject unknown properties")
    if registry.get("schema_version") != 1 or not isinstance(registry.get("adapters"), dict):
        raise ContractError("Invalid adapter registry")
    schema_adapters = set(check_schema.get("properties", {}).get("adapter", {}).get("enum", []))
    if schema_adapters != set(registry["adapters"]):
        raise ContractError("Schema adapter enum and registered adapters do not match")

    if set(contract) - {"schema_version", "source_sha", "contract_revision", "checks"}:
        raise ContractError("Task contract contains unsupported top-level properties")
    if contract.get("schema_version") != 1:
        raise ContractError("Unsupported task-contract version")
    if contract.get("source_sha") != expected_source_sha:
        raise ContractError("Task contract source SHA does not match the exact checked-out commit")
    revision = contract.get("contract_revision")
    if revision is not None and (not isinstance(revision, str) or not 1 <= len(revision) <= 128):
        raise ContractError("Invalid contract_revision")
    checks = contract.get("checks")
    if not isinstance(checks, list) or len(checks) > 32:
        raise ContractError("Task contract checks must be an array with at most 32 entries")

    mandatory = policy.get("mandatory_checks")
    if not isinstance(mandatory, list) or not mandatory:
        raise ContractError("Policy has no mandatory check manifest")
    mandatory_ids = {item.get("id") for item in mandatory if isinstance(item, dict)}
    adapters = registry["adapters"]
    seen: set[str] = set()
    validated: list[dict[str, Any]] = []

    for index, item in enumerate(checks):
        if not isinstance(item, dict):
            raise ContractError(f"Check {index} must be an object")
        if set(item) - {"id", "adapter", "entrypoint", "args", "timeout_minutes"}:
            raise ContractError(f"Check {index} contains unsupported properties")
        check_id = item.get("id")
        adapter = item.get("adapter")
        entrypoint = item.get("entrypoint")
        args = item.get("args", [])
        timeout = item.get("timeout_minutes", 10)
        if not isinstance(check_id, str) or not re.fullmatch(r"[a-z][a-z0-9-]{0,62}", check_id):
            raise ContractError(f"Check {index} has an invalid id")
        if check_id in seen or check_id in mandatory_ids:
            raise ContractError(f"Check id is duplicated or conflicts with a mandatory check: {check_id}")
        seen.add(check_id)
        if not isinstance(adapter, str) or adapter not in adapters:
            raise ContractError(f"Check {check_id} uses an unregistered adapter")
        if not isinstance(entrypoint, str) or not re.fullmatch(r"[A-Za-z0-9_./-]{1,240}", entrypoint):
            raise ContractError(f"Check {check_id} has an invalid entrypoint")
        if not isinstance(args, list) or len(args) > 32:
            raise ContractError(f"Check {check_id} has invalid arguments")
        if any(not isinstance(arg, str) or len(arg) > 256 or not re.fullmatch(r"[A-Za-z0-9_./:=,@+-]*", arg) for arg in args):
            raise ContractError(f"Check {check_id} contains an unsafe argument")
        if not isinstance(timeout, int) or isinstance(timeout, bool) or not 1 <= timeout <= 30:
            raise ContractError(f"Check {check_id} timeout must be between 1 and 30 minutes")

        adapter_config = adapters[adapter]
        if not isinstance(adapter_config, dict) or adapter_config.get("accepts_shell") is not False:
            raise ContractError(f"Adapter {adapter} is not registered as shell-free")
        if adapter == "python-module":
            allowed_modules = adapter_config.get("allowed_modules")
            if not isinstance(allowed_modules, list) or entrypoint not in allowed_modules:
                raise ContractError(f"Python module is not explicitly allowlisted: {entrypoint}")
        validated.append({
            "id": check_id,
            "adapter": adapter,
            "entrypoint": entrypoint,
            "args": args,
            "timeout_minutes": timeout,
        })

    # Resolve every entrypoint before running any task-supplied code.
    for check in validated:
        adapter = check["adapter"]
        entrypoint = check["entrypoint"]
        if adapter == "python-module":
            if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*", entrypoint):
                raise ContractError(f"Check {check['id']} has an invalid Python module name")
            module_path = root.joinpath(*entrypoint.split("."))
            candidates = [module_path.with_suffix(".py"), module_path / "__init__.py"]
            if not any(candidate.is_file() and candidate.resolve().is_relative_to(root) for candidate in candidates):
                raise ContractError(f"Python module is not present in the checked-out repository: {entrypoint}")
            check["_resolved"] = entrypoint
        else:
            resolved = safe_repo_path(root, entrypoint)
            if adapter == "python-script" and (not resolved.is_file() or resolved.suffix != ".py"):
                raise ContractError(f"Check {check['id']} must point to a Python script")
            check["_resolved"] = resolved.relative_to(root).as_posix()
    return validated


def command_for(check: dict[str, Any]) -> list[str]:
    adapter = check["adapter"]
    entrypoint = check["_resolved"]
    args = list(check["args"])
    if adapter == "python-script":
        return [sys.executable, entrypoint, *args]
    if adapter == "python-module":
        return [sys.executable, "-m", entrypoint, *args]
    if adapter == "pytest":
        return [sys.executable, "-m", "pytest", entrypoint, *args]
    if adapter == "unittest":
        if entrypoint.endswith(".py"):
            module_name = entrypoint[:-3].replace("/", ".")
            return [sys.executable, "-m", "unittest", module_name, *args]
        return [sys.executable, "-m", "unittest", "discover", "-s", entrypoint, *args]
    raise ContractError(f"Unsupported adapter: {adapter}")


def safe_environment() -> dict[str, str]:
    keys = ("PATH", "HOME", "SYSTEMROOT", "WINDIR", "TMP", "TEMP", "LANG", "LC_ALL")
    env = {key: os.environ[key] for key in keys if key in os.environ}
    env.update({
        "PYTHONNOUSERSITE": "1",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONUNBUFFERED": "1",
    })
    return env


def execute_checks(root: Path, checks: list[dict[str, Any]]) -> tuple[str, list[dict[str, Any]]]:
    results: list[dict[str, Any]] = []
    outcome = "success"
    for check in checks:
        try:
            if check["adapter"] == "pytest":
                import importlib.util
                if importlib.util.find_spec("pytest") is None:
                    raise InfrastructureError("The pytest adapter is not installed in the verifier environment")
            completed = subprocess.run(
                command_for(check),
                cwd=root,
                shell=False,
                capture_output=True,
                text=True,
                timeout=check["timeout_minutes"] * 60,
                env=safe_environment(),
                check=False,
            )
            status = "passed" if completed.returncode == 0 else "failed"
            if status == "failed" and outcome == "success":
                outcome = "check_failure"
            results.append({
                "id": check["id"],
                "adapter": check["adapter"],
                "status": status,
                "exit_code": completed.returncode,
                "stdout": completed.stdout[-65536:],
                "stderr": completed.stderr[-65536:],
            })
        except subprocess.TimeoutExpired as exc:
            outcome = "infrastructure_failure"
            results.append({
                "id": check["id"],
                "adapter": check["adapter"],
                "status": "timeout",
                "exit_code": None,
                "stdout": (exc.stdout or "")[-65536:] if isinstance(exc.stdout, str) else "",
                "stderr": (exc.stderr or "")[-65536:] if isinstance(exc.stderr, str) else "",
            })
        except (OSError, InfrastructureError) as exc:
            outcome = "infrastructure_failure"
            results.append({
                "id": check["id"],
                "adapter": check["adapter"],
                "status": "infrastructure_failure",
                "exit_code": None,
                "stdout": "",
                "stderr": str(exc),
            })
    return outcome, results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--policy", type=Path, required=True)
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--adapters", type=Path, required=True)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--expected-source-sha", required=True)
    parser.add_argument("--expected-policy-blob-sha", required=True)
    args = parser.parse_args()

    try:
        root = args.root.resolve(strict=True)
        policy_path = safe_repo_path(root, args.policy.as_posix())
        schema_path = safe_repo_path(root, args.schema.as_posix())
        adapters_path = safe_repo_path(root, args.adapters.as_posix())
        contract_path = safe_repo_path(root, args.contract.as_posix())
        policy = read_json(policy_path)
        schema = read_json(schema_path)
        registry = read_json(adapters_path)
        contract = read_json(contract_path)
        if policy.get("task_contract", {}).get("schema") != args.schema.as_posix():
            raise ContractError("Policy schema path does not match the verifier input")
        if policy.get("generic_verifier", {}).get("registered_adapters") != args.adapters.as_posix():
            raise ContractError("Policy adapter-registry path does not match the verifier input")
        checks = validate_contract(
            root, policy, schema, registry, contract,
            args.expected_source_sha, args.expected_policy_blob_sha, policy_path,
        )
        outcome, results = execute_checks(root, checks)
        print(json.dumps({
            "source_sha": args.expected_source_sha,
            "policy_blob_sha": args.expected_policy_blob_sha,
            "outcome": outcome,
            "expected_check_count": len(checks),
            "results": results,
        }, ensure_ascii=False))
        return 0 if outcome == "success" else 1
    except ContractError as exc:
        print(json.dumps({"outcome": "coverage_failure", "error": str(exc)}))
        return 2
    except (InfrastructureError, OSError) as exc:
        print(json.dumps({"outcome": "infrastructure_failure", "error": str(exc)}))
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
