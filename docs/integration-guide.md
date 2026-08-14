---
description: "Implementation guide for integrating APP v0.4.0 with agent runtimes, API gateways, MCP servers, and approval systems."
---

# Integration Guide

APP is an execution-time authority layer. It complements identity systems,
agent runtimes, and tool protocols by deciding whether a proposed action may
be attempted at all.

## Runtime Placement

Use one of three enforcement placements:

- Agent runtime: verify the sealed policy before constructing the tool surface.
- API gateway: verify the sealed policy before forwarding tool or API requests.
- Orchestrator: verify each workflow step before dispatching to a worker agent.

The verifier must run outside model reasoning. The model may propose an action,
but the verifier decides whether the action can execute.

## MCP And Tool-Calling Systems

APP does not replace OAuth or MCP authorization. OAuth and MCP authorize client
and resource access. APP authorizes the specific agent action at execution
time.

Recommended MCP mapping:

- MCP server or gateway receives a tool-call request.
- Verifier decrypts and validates the sealed APP policy.
- Verifier checks revocation, derivation, approval receipts, and limits.
- Verifier resolves APP capabilities to allowed tool operations.
- Runtime exposes only the policy-derived execution surface.

If an MCP or agent framework already supports tool-call approvals, treat the
framework approval as a source for an APP approval receipt. The receipt remains
the portable evidence artifact.

## Approval Flow

For high-consequence actions:

1. Policy declares `approval_gate`.
2. Verifier detects that the requested capability triggers approval.
3. Verifier denies in `sync` mode or suspends in `async` mode when no valid
   receipt is present.
4. Approval service emits a signed receipt bound to `policy_id` and
   `challenge_id`.
5. Verifier validates the receipt before capability resolution.
6. Execution proceeds only within the sealed policy scope.

Approval receipts must not expand scope, limits, audience, subject, or
delegation authority. Expanded authority requires a newly issued sealed policy.

## Implementer Assets

- `schemas/app-permission-policy.schema.json`
- `schemas/approval-challenge.schema.json`
- `schemas/approval-receipt.schema.json`
- `examples/payment-approval.yaml`
- `examples/email-external-send-approval.yaml`
- `examples/derived-policy-with-approval.yaml`
- `examples/approval-challenge.yaml`
- `examples/approval-receipt.yaml`
- `conformance/v0.4.0/approval-receipts.json`
- `conformance/v0.4.0/README.md`

The schemas validate document shape only. A conformant verifier must still
perform cryptographic verification, trust evaluation, replay protection,
revocation checking, derivation-chain validation, approval-scope subset
checks, and runtime limit enforcement.
