# Changelog

All notable changes to the Agent Permission Protocol (APP) are documented in this file.

The format of this changelog is intentionally explicit. The protocol is versioned to preserve semantic clarity, enable precise reference, and support rigorous critique.

---

## [0.4.0] — Approval gates and signed approval receipts

**Status:** Draft / Public Review
**Release date:** 2026-08-14
**Previous version:** v0.3.0 (2026-05-21)

This release adds `APP-Approval-1`, a normative approval gate and signed
approval receipt model for high-consequence agent actions. Approval can unlock
gated authority that is already declared in a sealed policy. Expanded authority
requires issuance of a new sealed policy.

### Added

- **`approval_gate` optional policy field** (§6) — policies may declare human
  or service approval requirements for gated capabilities.
- **`APP-Approval-1` approval flow** (§7.6) — defines approval challenges,
  signed approval receipts, receipt validation, timeout handling, replay
  protection, and fail-closed denial semantics.
- **Approval receipt minimum fields** (§7.6) — `receipt_id`, `challenge_id`,
  `policy_id`, `approver_subject`, `approver_authority`, `decision`,
  `approved_scope`, `issued_at`, `expires_at`, `nonce`, and `signature`.
- **Expanded 13-step verifier pipeline** (§7) — adds approval receipt
  validation after revocation and derivation checks and before capability
  resolution.
- **Audit evidence update** (§8) — audit records should include approval
  challenge ID, receipt ID, approver authority, approval decision, and receipt
  validation outcome when an approval gate applies.
- **Updated verifier compliance checklist** (§13) — requires fail-closed
  approval receipt validation for expired, replayed, malformed, mismatched,
  denied, or untrusted receipts.

### Changed

- Whitepaper status, conclusion, roadmap, and diagrams updated to v0.4.0.
- `approval_gate` moved from future roadmap item to delivered v0.4.0 protocol
  capability.

### Notes

- Approval receipts do not create authority. They unlock gated authority
  already declared in a sealed policy.
- Any expansion of scope, limits, audience, subject, or delegation authority
  requires a newly issued sealed policy.

---

## [0.3.0] — Revocation, derivation chain, and typed limits

**Status:** Draft / Public Review
**Release date:** 2026-05-21
**Previous version:** v0.2.0 (2026-03-11)

This release advances APP from an implementable draft to a draft that is
implementable with explicit revocation, cryptographic delegation lineage, and
a typed limit schema. It introduces several new required and optional policy
fields, expands the verifier pipeline, and adds a roadmap for the next
release.

### Added

- **`revocation_endpoint` REQUIRED in every sealed policy** (§6) — every
  v0.3.0 policy must declare the URI from which a verifier can query
  revocation status.
- **Normative `limits` schema with typed primitives** (§6.1) — new typed
  primitives for `call_count`, `token_budget`, `rate`, `data_volume`,
  `network_zone`, and `time_of_day`, with optional `strict_limits` to require
  fail-closed behavior on unknown limit types.
- **Cryptographic `derivation_chain` for derived policies** (§7.4) — derived
  policies must carry `parent_policy_id`, `parent_policy_hash`,
  `delegation_depth`, and `max_depth`; the verifier must validate the parent
  hash and depth increment.
- **Revocation interface and modes** (§7.5) — `online`, `cached`, and
  `stapled` modes; default freshness of five minutes; fail-closed semantics
  for `online` checks.
- **Expanded 12-step verifier pipeline** (§7) — adds revocation and
  derivation chain checks before capability resolution.
- **Audit evidence update** (§8) — audit records should include the full
  `derivation_chain` and the revocation check outcome, sufficient to
  reconstruct authorization lineage from a single terminal action.
- **Updated verifier compliance checklist** (§13) — reflects revocation,
  derivation chain, and typed limits obligations.
- **v0.4.0 roadmap and `APP-Federation-1` companion spec** (§18) — scopes
  `approval_gate`, `suspendable`, `content_integrity`, and cross-domain
  trust federation.
- **New optional policy fields** — `strict_limits`, `derivation_chain`, and
  `revocation_mode`.

### Changed

- Conformance classes (§9) and the §14 versioning section refer to v0.3.0.
- Whitepaper exec summary and §17 conclusion updated to reflect v0.3.0
  additions.

### Notes

- v0.3.0 is backward-compatible at the wire level with v0.2.0 for policies
  that do not declare `revocation_endpoint` — but such policies are NOT
  v0.3.0 conformant and will be denied by a v0.3.0 verifier.
- Implementers should treat the revocation endpoint as a first-class
  issuance-time dependency, not an optional integration.

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
