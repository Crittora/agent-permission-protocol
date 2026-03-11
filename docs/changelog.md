---
description: "Changelog for the Agent Permission Protocol (APP), including versions, status, and semantic updates."
---

# Changelog

All notable changes to the Agent Permission Protocol (APP) are documented in this file.

The format of this changelog is intentionally explicit. The protocol is versioned to preserve semantic clarity, enable precise reference, and support rigorous critique.

---

## [0.2.0] — Implementable draft

**Status:** Draft / Public Review

This release advances APP from a foundational draft to an implementable protocol draft.

### Added

- Formal permission policy field semantics including issuer, subject, audience, intent, scope, issuance time, activation time, and expiration
- Deterministic verifier algorithm with explicit fail-closed validation order
- Capability resolution semantics that map abstract authority to allowed operations
- Ephemeral execution surfaces derived from policy rather than pre-mounted tools
- Delegation controls for bounded multi-agent authority propagation
- Conformance classes for issuer, verifier, and executor responsibilities
- Minimum audit evidence model for authorization decisions
- Release semantics clarifying the meaning of patch, minor, and major protocol versions

### Clarifications

- The canonical whitepaper is the authoritative publication surface; this repository is the public release mirror
- Scope is an allowlist-derived capability set, not an inferred permission universe
- Predicates, limits, and replay controls are part of execution-time authorization semantics, not optional documentation hints
- Executors may not widen authority beyond the verifier-derived allowlist

### Notes

- `v0.2.0` is intended to be the first version that independent teams can implement against with materially similar verifier behavior
- Backward compatibility remains conservative and will continue to be evaluated as a protocol property

---

## [0.1.0] — Initial draft

**Status:** Draft / Public Review

This is the initial public draft of the Agent Permission Protocol.

### Added

- Formal definition of execution-time authority as a first-class protocol concern
- Core invariant: authority must be explicit, bounded, and verified at execution
- Conceptual separation between capability, access, and authorization
- Model for explicit authority grants independent of model behavior
- Scope constraints limiting what actions may be attempted
- Time-bounded authority semantics
- Predicate conditions evaluated at execution
- Fail-closed revocation semantics
- Audit-safe validation external to the model

### Clarifications

- Authority enforcement is distinct from model intent or reasoning
- Policy documentation alone is insufficient without runtime enforcement
- APP governs whether an action may be attempted, not how it is performed
- The protocol is intentionally minimal and does not prescribe implementation details

### Non-goals

- Model alignment, safety tuning, or behavioral control
- Identity and access management replacement
- Agent orchestration or workflow definition
- Business logic enforcement
- Evaluation of correctness or outcome quality

### Notes

- This version establishes the foundational vocabulary and invariants
- Subsequent versions may refine definitions, introduce additional constraints, or clarify semantics based on public review
- Backward compatibility will be considered a protocol property and treated conservatively

---
