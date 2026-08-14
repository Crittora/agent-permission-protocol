#!/usr/bin/env python3
"""Validate non-normative APP implementer assets."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]


SCHEMAS = {
    "policy": ROOT / "schemas" / "app-permission-policy.schema.json",
    "challenge": ROOT / "schemas" / "approval-challenge.schema.json",
    "receipt": ROOT / "schemas" / "approval-receipt.schema.json",
}

POLICY_EXAMPLES = [
    ROOT / "examples" / "payment-approval.yaml",
    ROOT / "examples" / "email-external-send-approval.yaml",
    ROOT / "examples" / "derived-policy-with-approval.yaml",
]

CHALLENGE_EXAMPLES = [
    ROOT / "examples" / "approval-challenge.yaml",
]

RECEIPT_EXAMPLES = [
    ROOT / "examples" / "approval-receipt.yaml",
]

CONFORMANCE_FILES = [
    ROOT / "conformance" / "v0.4.0" / "approval-receipts.json",
]

REQUIRED_RECEIPT_FIELDS = {
    "receipt_id",
    "challenge_id",
    "policy_id",
    "approver_subject",
    "approver_authority",
    "decision",
    "approved_scope",
    "issued_at",
    "expires_at",
    "nonce",
    "signature",
}

EXPECTED_REASONS = {
    "approval_receipt_expired",
    "approval_receipt_policy_mismatch",
    "approval_receipt_scope_expansion",
    "approval_receipt_replay",
    "approval_receipt_untrusted_authority",
}


def read_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def read_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def validator(name: str) -> Draft202012Validator:
    schema = read_json(SCHEMAS[name])
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def assert_valid(instance: Any, schema_validator: Draft202012Validator, path: Path) -> None:
    errors = sorted(schema_validator.iter_errors(instance), key=lambda error: list(error.path))
    if errors:
        rendered = "\n".join(f"- {list(error.path)}: {error.message}" for error in errors)
        raise AssertionError(f"{path} failed schema validation:\n{rendered}")


def validate_examples() -> None:
    policy_validator = validator("policy")
    challenge_validator = validator("challenge")
    receipt_validator = validator("receipt")

    for path in POLICY_EXAMPLES:
        assert_valid(read_yaml(path), policy_validator, path)

    for path in CHALLENGE_EXAMPLES:
        assert_valid(read_yaml(path), challenge_validator, path)

    for path in RECEIPT_EXAMPLES:
        assert_valid(read_yaml(path), receipt_validator, path)


def validate_conformance_vectors() -> None:
    for path in CONFORMANCE_FILES:
        suite = read_json(path)
        if suite.get("protocol_version") != "0.4.0":
            raise AssertionError(f"{path} must declare protocol_version 0.4.0")

        vectors = suite.get("vectors")
        if not isinstance(vectors, list) or not vectors:
            raise AssertionError(f"{path} must contain a non-empty vectors array")

        names: set[str] = set()
        seen_allow = False
        seen_denies: set[str] = set()

        for vector in vectors:
            name = vector.get("name")
            if not isinstance(name, str) or not name:
                raise AssertionError(f"{path} contains a vector without a name")
            if name in names:
                raise AssertionError(f"{path} contains duplicate vector name: {name}")
            names.add(name)

            decision = vector.get("expected_decision")
            if decision not in {"allow", "deny"}:
                raise AssertionError(f"{path}:{name} has invalid expected_decision: {decision}")

            receipt = vector.get("receipt")
            if not isinstance(receipt, dict):
                raise AssertionError(f"{path}:{name} must contain receipt object")
            missing = REQUIRED_RECEIPT_FIELDS - receipt.keys()
            if missing:
                raise AssertionError(f"{path}:{name} receipt missing fields: {sorted(missing)}")

            if decision == "allow":
                seen_allow = True
                if "expected_reason" in vector:
                    raise AssertionError(f"{path}:{name} allow vector must not include expected_reason")
            else:
                reason = vector.get("expected_reason")
                if reason not in EXPECTED_REASONS:
                    raise AssertionError(f"{path}:{name} has invalid expected_reason: {reason}")
                seen_denies.add(reason)

        missing_denies = EXPECTED_REASONS - seen_denies
        if missing_denies:
            raise AssertionError(f"{path} missing deny vectors for: {sorted(missing_denies)}")
        if not seen_allow:
            raise AssertionError(f"{path} must include at least one allow vector")


def main() -> None:
    validate_examples()
    validate_conformance_vectors()
    print("APP implementer assets validated.")


if __name__ == "__main__":
    main()
