---
description: "Frequently asked questions about the Agent Permission Protocol (APP), execution-time authority, and ambient authority."
---

# FAQ

## What is the Agent Permission Protocol (APP)?

The Agent Permission Protocol (APP) is a protocol that requires explicit, cryptographically verifiable permission policies to gate agent execution at runtime.

## What is execution-time authority?

Execution-time authority is authorization that is validated immediately before an agent action occurs. Under APP, no action is permitted unless a valid permission policy is verified at execution.

## What is ambient authority in agentic systems?

Ambient authority occurs when agents inherit permissions implicitly through tool availability or credentials rather than explicit authorization. APP eliminates ambient authority by requiring sealed permission policies.
