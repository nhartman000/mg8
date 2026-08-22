# MG8 Provenance and Scope

**Author:** Nicholas Hartman / American Milestone Inc.

This document records the current repository baseline for the MG8 file/container architecture.

## Canonical file family

The established file family is:

```text
.mg8pk
.mg8
.ork
.gst
.g8son
.qson
```

The roles represented in this repository baseline are:

- `.mg8pk` — package/composition layer for one or more `.mg8` units.
- `.mg8` — bounded execution unit/container binding state, orchestration, gates, and trace output.
- `.ork` — orchestration/topology/order/branches/loops, including package-level `system.ork` and unit-level `flow.ork` roles.
- `.gst` — structured state, contextual constraints, and state-detection layer.
- `.g8son` — bounded conditional gate/operator definitions; a file may contain 1–3 gates.
- `.qson` — immutable/auditable execution and transformation trace records.

## Identity semantics

MG8 distinguishes:

```text
file identity != gate identity != execution identity
```

Each gate execution attempt receives a unique event-level `trace_id`.

## State semantics

The `.gst` layer is the semantic state center of the architecture. Prior and current state support temporal continuity and memory. Internal/external state-detection profiles and higher-order awareness, intent, and outcome-expectation concepts belong to the state layer rather than the gate syntax.

The exact quantitative/formal definition of those higher-order state semantics is intentionally not invented in this repository where no versioned schema has yet been established.

## Repository correction note

Earlier repository placeholder material described `.mg8` primarily as a Boolean-gate configuration language using AND/OR/NOT/NAND/NOR/XOR/XNOR. That description did not represent the canonical MG8 architecture and has been replaced in the `mg8-canonical-v1` baseline with the bounded unit/container model.

## Scope boundary

This repository currently establishes the `.mg8` unit and its relationship to the wider file family. It does not claim that the independent grammars for `.mg8pk`, `.ork`, `.gst`, `.g8son`, and `.qson` are fully specified here.

Those artifacts should receive separate versioned specifications rather than having semantics invented ad hoc inside the `.mg8` repository.
