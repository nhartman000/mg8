# MG8 / `.mg8`

**MG8** is Nicholas Hartman / American Milestone Inc.'s bounded intelligence-unit and deterministic execution-container architecture.

The `.mg8` file/unit binds structured state, constraints, orchestration, conditional transform eligibility, and an auditable transformation ledger into a discrete composable unit.

## Canonical compatibility and repository authority

Use the [pinned compatibility matrix](docs/COMPATIBILITY.md) and [repository authority map](docs/REPOSITORY_AUTHORITY.md) before selecting an implementation. They distinguish current format authorities, named executable profiles, prompt-only/historical adapters and unsupported grammar. The machine registries live in [`registry/`](registry/), with positive and expected-negative schema fixtures checked in CI.

## File family

```text
.mg8pk   package / distribution container for one or more .mg8 units
.mg8     bounded execution unit / container
.ork     orchestration: order, dependencies, branches, loops, entry flow
.gst     structured state, context, constraints, and state-detection data
.g8son   bounded conditional gate/operator definitions
.qson    immutable execution / transformation trace records
```

The intended execution relationship is:

```text
.mg8pk
  ↓ system.ork
.mg8
  ↓ flow.ork
.gst state/context
  ↓
.g8son gate / transform eligibility
  ↓
.qson trace / realized transformation record
```

At unit scope, `flow.ork` selects and orders the `.gst` and `.g8son` resources used by the `.mg8` unit and defines when execution events are written to `.qson`.

## Core distinction

MG8 is **not** a Boolean-gate language. `AND`, `OR`, `NAND`, etc. may be representable as particular gate behaviors, but they do not define the `.mg8` architecture.

The core model is:

```text
structured state
    ↓
constraint / context resolution
    ↓
conditional transform eligibility
    ↓
ordered execution
    ↓
realized state transition
    ↓
immutable trace
```

## Identity and trace semantics

File identity, gate identity, and execution identity are distinct.

A `.g8son` file may contain multiple gates. Every gate execution attempt receives its own event-level `trace_id`, so repeated execution of the same gate produces distinct trace events.

## `.gst` state role

`.gst` is the state/context layer. It carries the structured state against which gates are evaluated. The broader MG8 state model includes current-state and prior-state continuity, with state-detection semantics kept distinct from the gate/operator layer.

## Repository structure

- [`spec/mg8_v1.md`](spec/mg8_v1.md) — canonical `.mg8` specification
- [`schema/mg8.schema.json`](schema/mg8.schema.json) — current `.mg8` manifest/schema contract
- [`examples/basic.mg8`](examples/basic.mg8) — minimal `.mg8` unit example
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — unit/runtime architecture
- [`docs/FILE_FAMILY.md`](docs/FILE_FAMILY.md) — cross-repository file-family registry and authority map
- [`spec/ork_reference_profile.md`](spec/ork_reference_profile.md) — interim `.ork` orchestration reference profile
- [`spec/mg8pk_v1.md`](spec/mg8pk_v1.md) — baseline `.mg8pk` package-role specification
- [`docs/PROVENANCE.md`](docs/PROVENANCE.md) — provenance and scope boundary

Dedicated current format repositories:

- GST: https://github.com/nhartman000/gst
- G8SON: https://github.com/nhartman000/g8son
- QSON: https://github.com/nhartman000/qson
- Reference runtime: https://github.com/nhartman000/mg8-engine

## Response-contract examples and measured repeatability

The opt-in [response-contract profile](docs/RESPONSE_CONTRACTS.md) binds GST globals/facts and G8SON atomic requirements into a model-facing response contract. The [simple, ordered and grammar examples](examples/response-contracts/) preserve the tested conditions.

[Published live evidence](experiments/response-contracts/README.md) retains both the original divergent batch and the revised batch: each revised contract produced three byte-identical responses in three fresh calls, without temperature, seed or answer reuse. This is a finite observed result, not a guarantee of deterministic inference. The existing canonical format contracts are unchanged.

## Packed single-file units and packages

The opt-in [packed container profile 1.0](spec/packed_containers_v1.md) defines a single physical `.mg8` containing its GST, bounded G8SON files, ORK and QSON, and a `.mg8pk` containing complete units plus `system.ork`. It uses uncompressed ZIP storage, explicit profile identity and per-member integrity. The [envelope schema](schema/packed-container.schema.json) is additive; the existing JSON manifest schema is unchanged.

This is a physical packaging and authoring profile, not a claim that legacy loaders execute these archives or that a composed chain improves reasoning. Import is copy-only and execution remains separately authorized.

## Specification status

This repository is the authority for the `.mg8` unit and the current cross-file family registry.

The roles of `.ork` and `.mg8pk` are established, but standalone repositories/full grammars for them are not yet present in the connected GitHub account. Their documents here are therefore explicitly versioned as interim/baseline specifications rather than silently inventing a finished universal grammar.
