---
description: "Frequently asked questions about the Agent Permission Protocol (APP), execution-time authority, and ambient authority."
---

# FAQ

## What is the Agent Permission Protocol (APP)?

The Agent Permission Protocol (APP) is a protocol for explicit, cryptographically verifiable authority in agentic AI systems. It requires a signed and encrypted permission policy before any action-capable execution.

## What is execution-time authority?

Execution-time authority is authorization that is validated immediately before an agent action occurs. Under APP, no action is permitted unless a valid permission policy is verified at execution.

## What is ambient authority in agentic systems?

Ambient authority occurs when agents inherit permissions implicitly through tool availability or credentials rather than explicit authorization. APP eliminates ambient authority by requiring sealed permission policies.

## Why is authority different from identity for agents?

Identity proves who is calling a system, but authority defines what actions are allowed in a specific context. APP formalizes authority as a first-class object so that the question "who authorized this action — and under what constraints — at the moment it executed?" is answerable by design.

## What does APP verification enforce?

A compliant APP verifier performs a 13-step deterministic, fail-closed pipeline that includes decryption, signature validation, issuer trust, required fields, time bounds, replay protection, audience binding, revocation checking, derivation chain verification (for delegated policies), approval receipt validation when an approval gate applies, capability resolution, execution surface construction, and typed limit evaluation.

## How does APP prevent replay and ambient authority?

APP uses time-bounded policies and optional nonces to prevent reuse, and denies tool exposure unless a sealed policy is presented and verified at execution time. The ephemeral execution surface means tools outside the policy are not available to the agent, even if they are mounted in the runtime.

## How does APP integrate with existing systems?

APP is enforced in agent runtimes, API gateways, or orchestrators to gate tool exposure and request forwarding. It complements OAuth, RBAC, and IAM by providing an explicit authority object for agent actions.

## Does APP support revocation of in-flight policies?

Yes. APP requires every sealed policy to declare a `revocation_endpoint`. Verifiers check revocation status per the policy's `revocation_mode` — `online`, `cached`, or `stapled` — and fail closed when an `online` check cannot complete.

## How does APP prove the lineage of delegated policies?

Derived policies must carry a `derivation_chain` that cryptographically binds them to the parent policy hash and increments delegation depth. A single audit record for a terminal action can reconstruct the full authorization path back to the original issuer.

## How does APP handle human or service approval?

APP v0.4.0 defines `APP-Approval-1`: policies may include an `approval_gate`, and verifiers validate signed approval receipts before exposing gated authority. Approval can unlock authority already declared in a sealed policy, but expanded authority requires a new sealed policy.

## What remains on the APP roadmap?

`suspendable` for in-flight policy suspension and `content_integrity` for input attestation remain under review. Cross-domain trust federation is being scoped as a separate `APP-Federation-1` companion spec.
