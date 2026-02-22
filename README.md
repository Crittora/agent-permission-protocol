# Agent Permission Protocol (APP)

The Agent Permission Protocol (APP) is a public specification defining a minimal, enforceable model for execution-time authority in agentic systems.

As AI systems increasingly act through autonomous agents—invoking tools, modifying systems, and triggering irreversible outcomes—existing governance, policy, and access-control models have proven insufficient. In most architectures today, authority is inferred from access rather than explicitly validated at the moment an action executes.

APP exists to address this structural gap.

---

## Problem statement

Agentic systems introduce a failure mode that is not caused by model behavior, but by authorization design.

In common implementations:

- Authority is granted implicitly through credentials, roles, or tool exposure
- Permissions are treated as static configuration rather than runtime-validated objects
- Execution proceeds even when scope, duration, or consequence is ambiguous
- Exceptions accumulate without enforced revocation

As a result, systems may appear compliant while authority silently expands over time.

This failure mode is difficult to detect, difficult to audit, and difficult to reverse.

---

## Core principle

**Authority must be explicit, bounded, and verified at execution time.**

Capability alone is not authorization.  
Access alone is not intent.  
Policy alone does not enforce invariants.

The Agent Permission Protocol formalizes authority as a first-class object that must be validated immediately before an agent action is permitted to execute.

---

## What APP defines

The Agent Permission Protocol specifies:

- Explicit authority grants for agent actions
- Scope constraints that limit what may be attempted
- Time bounds that restrict how long authority remains valid
- Predicate conditions that must be satisfied at execution
- Revocation semantics that fail closed
- Audit-safe validation independent of model reasoning

APP is concerned with whether an action may be attempted at all, not with how the action is carried out.

---

## Non-goals

APP does not attempt to:

- Define model alignment or safety techniques
- Replace identity or access management systems
- Provide agent orchestration frameworks
- Evaluate intent, reasoning quality, or output correctness
- Encode business logic or workflow design

The protocol is intentionally minimal. Its purpose is to define an invariant enforcement layer for agent authority.

---

## Why a protocol

Frameworks describe behavior.  
Policies document intent.  
Protocols define invariants.

Agentic systems operate at machine speed, across systems, and without continuous human oversight. In such environments, authority must be governed by rules that are deterministic, enforceable, composable, and independent of model behavior.

APP exists to provide that invariant layer.

---

## Status

- Current version: **v0.1**
- Status: **Draft / Public Review**

The protocol is published as a public specification and is versioned to enable precise reference and critique. Changes between versions are documented to preserve semantic stability.

---

## Stewardship

The Agent Permission Protocol is stewarded by **Crittora**.

Stewardship implies maintenance, versioning, and editorial responsibility. It does not imply exclusive ownership, implementation rights, or control over downstream use.

The protocol is intended to be examined, challenged, and implemented independently.

---

## Canonical specification

The authoritative specification of the Agent Permission Protocol is published in the accompanying whitepaper:

**https://www.crittora.com/app/whitepaper**

---

## Intended audience

This specification is written for:

- System architects designing agentic platforms
- Security engineers responsible for execution control
- Platform owners accountable for downstream outcomes
- Researchers evaluating agent governance primitives

It is not written for marketing, evangelism, or trend commentary.

---

## License

This repository is licensed under the Apache License, Version 2.0.

---

## Closing note

As agents gain the ability to act, the critical question is no longer what they can do.

It is:

**Who authorized this action — and under what constraints — at the moment it executed?**

The Agent Permission Protocol exists to make that question answerable by design.
