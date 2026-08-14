# APP v0.4.0 Conformance Vectors

This directory contains non-cryptographic conformance vectors for implementers.
The vectors define expected verifier decisions and reason codes for
APP-Approval-1 approval receipt handling.

## Result Format

Implementations should evaluate each vector and return:

```json
{
  "decision": "allow",
  "reason": null
}
```

or:

```json
{
  "decision": "deny",
  "reason": "approval_receipt_expired"
}
```

The `decision` value must be `allow` or `deny`. Deny vectors include an
`expected_reason` that implementations should preserve or map to a documented
equivalent.

## Coverage

`approval-receipts.json` covers:

- valid approval receipt
- expired receipt
- mismatched `policy_id`
- scope expansion attempt
- replayed nonce
- untrusted approver authority

These vectors do not prove cryptographic correctness. A conformant verifier
must still validate signatures, trust anchors, revocation status, derivation
chains, replay state, scope subset relationships, and runtime limits.
