# Governance of the Agent Permission Protocol

The Agent Permission Protocol (APP) is a stewarded public specification.

This repository exists to support rigorous review, contribution, and evolution
of the protocol while preserving semantic clarity, interoperability, and
security invariants.

---

## 1. Canonical publication

The canonical specification of APP is the published whitepaper at:

**https://www.crittora.com/app/whitepaper**

The public source repository is:

**https://github.com/Crittora/agent-permission-protocol**

This repository is the public contribution and release mirror.

If wording in this repository diverges from the canonical whitepaper, the
whitepaper is authoritative until the repository is updated to match it.

---

## 2. Stewardship model

APP is stewarded by **Crittora**.

The steward is responsible for:

- maintaining protocol coherence
- deciding when a proposal is accepted, deferred, or rejected
- determining release timing and version boundaries
- preserving semantic stability across versions
- resolving disputes where protocol correctness or interoperability is at risk

Stewardship does not prevent outside contribution. It exists to ensure that the
protocol remains implementable, internally consistent, and defensible as a
security specification.

---

## 3. What contributors may propose

Contributors are encouraged to propose:

- clarifications to ambiguous language
- corrections to inconsistent or incomplete semantics
- threat model expansions
- conformance refinements
- verification algorithm improvements
- interoperability improvements
- versioning and governance refinements

Contributors should avoid proposals framed primarily as:

- product positioning
- vendor preference
- implementation-specific ergonomics unrelated to protocol semantics
- marketing or branding changes

---

## 4. Contribution path

Substantive protocol changes should follow this sequence:

1. Open an issue.
2. Describe the ambiguity, failure mode, or proposed semantic change.
3. Identify whether the proposal is normative or non-normative.
4. Explain interoperability, conformance, and security impact.
5. Submit a narrowly scoped pull request once the proposal is concrete.

For substantial changes, contributors should include:

- the affected section or sections
- the current behavior or ambiguity
- the proposed new behavior or wording
- expected implementation impact
- whether existing implementations would become non-conformant
- any security or downgrade risks introduced by the change

---

## 5. Normative vs non-normative changes

APP distinguishes sharply between editorial clarification and protocol change.

### Non-normative changes

These include:

- grammar and wording improvements
- readability improvements
- explanatory examples
- formatting corrections
- editorial restructuring that does not alter meaning

These changes do not alter conformance behavior.

### Normative changes

These include:

- new required fields
- changed verifier ordering
- revised conformance requirements
- new delegation semantics
- changed replay rules
- modified cryptographic requirements
- any change that alters interoperable behavior

These changes may require a version change and explicit release note entry.

---

## 6. Decision criteria

The steward evaluates proposals primarily on:

- semantic correctness
- fail-closed behavior
- interoperability impact
- compatibility with existing invariants
- clarity of implementation consequences
- resistance to ambiguity or unsafe interpretation

Consensus is valuable, but correctness and protocol integrity take precedence.

---

## 7. External review

Security researchers, implementers, and protocol reviewers are encouraged to
participate through issues and pull requests.

For material normative changes, the steward may request additional expert
review before acceptance.

Reviewers do not need to agree on all design choices, but proposals must be
specific enough to evaluate security, interoperability, and conformance
implications.

---

## 8. Versioning policy

APP uses semantic versioning for released protocol documents.

- Patch releases clarify or correct non-normative material.
- Minor releases may add or refine normative semantics.
- Major releases indicate a stable baseline with explicit compatibility
  commitments.

All accepted changes with release impact must be reflected in:

- the canonical whitepaper
- `CHANGELOG.md`
- any mirrored documentation that describes current protocol behavior

---

## 9. Release discipline

A release should not be treated as published until:

- the canonical whitepaper reflects the released version
- the public mirror reflects the same version
- the changelog records the semantic delta

Where repository discussion and canonical publication are temporarily out of
sync, the whitepaper remains authoritative.

---

## 10. Conduct expectations

Technical disagreement is expected.

Contributors are expected to:

- critique ideas directly
- ground objections in protocol semantics or security impact
- avoid rhetorical or dismissive argumentation
- prefer precise examples over broad claims

The standard for acceptance is not enthusiasm.

It is defensible protocol language.
