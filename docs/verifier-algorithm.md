---
description: "Reference verifier algorithm for APP v0.4.0, including APP-Approval-1 approval receipt validation."
---

# Verifier Algorithm

This page restates the APP v0.4.0 verifier flow as implementation-oriented
pseudocode. The whitepaper remains authoritative.

## Inputs

- `sealed_policy`: signed and encrypted APP permission policy
- `execution_context`: runtime identity, audience, trusted clock, requested
  capability, requested operation, request correlation ID, and replay state
- `approval_receipt`: optional signed APP-Approval-1 receipt
- `capability_registry`: verifier-controlled capability-to-operation mapping

## Fail-Closed Flow

```text
function verify_app_execution(sealed_policy, execution_context, approval_receipt):
  plaintext_policy = decrypt(sealed_policy)
  if decrypt failed:
    deny("policy_decryption_failed")

  if signature_invalid(plaintext_policy):
    deny("policy_signature_invalid")

  policy = parse_and_validate_required_fields(plaintext_policy)
  if invalid:
    deny("policy_invalid")

  if unsupported_policy_version(policy.policy_version):
    deny("policy_version_unsupported")

  if trusted_clock < policy.not_before:
    deny("policy_not_yet_valid")

  if trusted_clock > policy.expires_at:
    deny("policy_expired")

  if replay_protection_present(policy) and replay_seen(policy.nonce):
    deny("policy_replay")

  if policy.audience != execution_context.audience:
    deny("audience_mismatch")

  revocation = check_revocation(policy)
  if revocation is revoked or indeterminate:
    deny("policy_revoked_or_revocation_indeterminate")

  if policy.derivation_chain is present:
    if derivation_chain_invalid(policy):
      deny("derivation_chain_invalid")

  if approval_gate_applies(policy.approval_gate, execution_context):
    if approval_receipt is missing:
      if policy.approval_gate.mode == "async":
        suspend("approval_required")
      deny("approval_required")

    if approval_receipt_signature_invalid(approval_receipt):
      deny("approval_receipt_signature_invalid")

    if approval_receipt.policy_id != policy.policy_id:
      deny("approval_receipt_policy_mismatch")

    if challenge_binding_invalid(approval_receipt, execution_context):
      deny("approval_receipt_challenge_mismatch")

    if approval_receipt.decision != "approved":
      deny("approval_receipt_denied")

    if trusted_clock > approval_receipt.expires_at:
      deny("approval_receipt_expired")

    if replay_seen(approval_receipt.nonce):
      deny("approval_receipt_replay")

    if approver_not_trusted(policy.approval_gate, approval_receipt.approver_authority):
      deny("approval_receipt_untrusted_authority")

    if not subset(approval_receipt.approved_scope, policy.scope):
      deny("approval_receipt_scope_expansion")

  capabilities = resolve_capabilities(policy.scope, capability_registry)
  if resolution_failed:
    deny("capability_resolution_failed")

  execution_surface = construct_execution_surface(capabilities)
  if execution_surface_invalid:
    deny("execution_surface_invalid")

  if limits_invalid_or_exceeded(policy.limits, execution_context):
    deny("limits_invalid_or_exceeded")

  audit_decision(policy, execution_context, approval_receipt, "allow")
  allow(execution_surface)
```

## Required Denial Behavior

Verifiers must deny when any required field is absent, cryptographic checks
fail, trust roots are unavailable, revocation is indeterminate under the
selected mode, derivation expands authority, approval receipts are invalid, or
runtime context is missing.

Approval receipts do not create authority. They only unlock gated authority
already declared in the sealed policy. Expanded authority requires a newly
issued sealed policy.

## Assets

- Policy schema: `schemas/app-permission-policy.schema.json`
- Approval challenge schema: `schemas/approval-challenge.schema.json`
- Approval receipt schema: `schemas/approval-receipt.schema.json`
- Approval receipt vectors: `conformance/v0.4.0/approval-receipts.json`
