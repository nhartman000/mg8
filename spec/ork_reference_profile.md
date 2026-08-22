# ORK Reference Profile v0.1

**Status:** interim reference profile, not a universal final grammar  
**Author:** Nicholas Hartman / American Milestone Inc.

## Purpose

`.ork` carries orchestration: execution order, dependencies, branches, loops, entry flow, retry/failure policy, and other topology that should remain separate from state (`.gst`), gate definitions (`.g8son`), and trace records (`.qson`).

Two established scopes are:

- `system.ork` — package-level orchestration across `.mg8` units;
- `flow.ork` — unit-level orchestration inside one `.mg8` unit.

## Minimal reference representation

A simple deterministic runtime profile may represent a unit flow as:

```json
{
  "ork_version": "0.1-reference",
  "flow": ["gate_a", "gate_b", "gate_c"]
}
```

The values are stable gate identifiers resolved from the `.g8son` resources bound by the containing `.mg8` unit.

This JSON shape is a reference profile only. The canonical architectural requirement is the orchestration role and deterministic semantics, not this exact serialization.

## Deterministic requirements

An ORK profile intended for reproducible execution must define any semantics it uses for:

1. entry point;
2. sequencing;
3. dependency resolution;
4. branch selection;
5. tie-breaking;
6. loop bounds;
7. retry policy;
8. failure/indeterminate handling;
9. human-review transitions where applicable;
10. trace-emission points.

Unspecified ordering should not be relied on when deterministic execution is claimed.

## Separation of responsibility

`.ork` should not become a second state store or a second audit ledger.

```text
.gst   = what state/context exists
.g8son = what conditional gate/operator is evaluated
.ork   = when/where execution proceeds
.qson  = what actually occurred
```

## Package scope

At package scope, `system.ork` may order or connect multiple `.mg8` units. Exact package-graph serialization remains an open versioned-specification task.

## Status boundary

This document exists because the role of `.ork` is established but a standalone canonical `.ork` repository/complete grammar has not yet been published. Implementations should declare the ORK profile/version they support rather than assuming this minimal JSON form is universal.
