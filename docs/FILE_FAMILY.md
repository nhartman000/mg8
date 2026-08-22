# MG8 File-Family Registry

**Nicholas Hartman / American Milestone Inc.**

This document is the cross-file registry for the current MG8 public baseline.

## Canonical family

| Extension | Role | Current public authority |
|---|---|---|
| `.mg8pk` | package/composition container for one or more `.mg8` units | interim specification in this repository |
| `.mg8` | bounded execution unit/container | this repository |
| `.ork` | orchestration, ordering, dependencies, branches, loops | interim reference profile in this repository |
| `.gst` | structured state/context/constraints and continuity | `nhartman000/gst` |
| `.g8son` | bounded conditional gate/operator file, 1–3 gates | `nhartman000/g8son` |
| `.qson` | auditable event-level execution trace | `nhartman000/qson-` |

Auxiliary / historical formats such as `.gitson` are not required members of the current core family.

## Package-to-trace relationship

```text
.mg8pk
  ↓
system.ork
  ↓
.mg8 unit
  ↓
flow.ork
  ├── .gst state/context
  ├── .g8son bounded gates
  └── .qson trace destination
```

## Identity boundaries

The family intentionally keeps several identities distinct:

```text
package identity
unit identity
state identity
gate-file identity
gate identity
run identity
execution-event trace identity
```

Conflating these identities makes audit and provenance ambiguous.

## Authority rule

When an implementation conflicts with a dedicated current format repository, the dedicated current specification should control unless the implementation explicitly declares itself a legacy/reference profile.

## Current incompleteness

The standalone repositories for `.ork` and `.mg8pk` do not yet exist in the connected GitHub account. Their documents here are therefore interim public specifications:

- [`../spec/ork_reference_profile.md`](../spec/ork_reference_profile.md)
- [`../spec/mg8pk_v1.md`](../spec/mg8pk_v1.md)

The `.ork` document is deliberately a **reference profile**. It does not claim that all future ORK implementations must use one JSON grammar.
