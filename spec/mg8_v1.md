# MG8 `.mg8` File / Unit Specification v1

**Author:** Nicholas Hartman / American Milestone Inc.  
**Scope:** canonical `.mg8` bounded execution-unit/container semantics

## 1. Purpose

A `.mg8` unit is the bounded engineering realization of an intelligence/execution unit. It binds the state required for an operation with the constraints, orchestration, conditional operators, and trace semantics required to execute and audit that operation deterministically.

A `.mg8` unit is not defined by Boolean logic gates. Boolean operators may appear inside a gate implementation, but the `.mg8` abstraction is broader: it is a container for bounded stateful execution.

## 2. File Family

The MG8 family is:

```text
.mg8pk   package / composition container
.mg8     bounded execution unit
.ork     orchestration script / topology
.gst     structured state and contextual constraints
.g8son   bounded conditional gate/operator definitions
.qson    immutable execution / transformation trace
```

## 3. Package and Unit Scope

At package scope:

```text
.mg8pk
  └── system.ork
        └── one or more .mg8 units
```

At unit scope:

```text
.mg8
  └── flow.ork
        ├── loads/selects .gst state
        ├── loads/selects .g8son gates
        ├── defines execution order / branches / loops
        └── emits .qson trace events
```

`system.ork` orchestrates package-level topology. `flow.ork` controls execution inside one `.mg8` unit.

## 4. Structured State — `.gst`

`.gst` carries the structured state and contextual constraints consumed by the unit.

The state layer is conceptually prior to gate evaluation. Gates do not define the state; they evaluate or transform state that has already been instantiated.

The broader state model may include:

- current state,
- prior state,
- internal state,
- external state,
- contextual constraints,
- state-detection fields,
- intent and outcome-expectation fields where the application profile defines them.

The precise `.gst` schema is defined separately from this `.mg8` unit specification.

## 5. Conditional Operators — `.g8son`

`.g8son` contains bounded conditional gate/operator definitions.

A `.g8son` file may contain one to three gates. Therefore:

```text
file identity != gate identity != execution identity
```

Each gate has its own identity independent of the file containing it.

A gate evaluates whether a transition or operation is admissible under the current state and constraints. A gate may pass, fail, remain indeterminate, or route control according to the orchestration profile.

## 6. Execution Identity

Every gate execution attempt receives a unique event-level `trace_id`.

Repeated attempts against the same gate MUST produce distinct execution identities even when:

- the same `.g8son` file is used,
- the same gate definition is used,
- the same input state is presented.

This preserves event-level auditability.

## 7. Orchestration — `.ork`

`.ork` defines execution topology and order.

At unit scope, `flow.ork` may define:

- entry node,
- state resources to load,
- gate resources to load,
- sequencing,
- dependencies,
- branches,
- loops,
- bounded retry/failure behavior,
- trace-emission points.

Deterministic execution requires that order, tie-breaking, retry behavior, failure behavior, and loop bounds be explicitly defined by the runtime/profile rather than left implicit.

## 8. Trace Ledger — `.qson`

`.qson` records realized execution/transformation events.

A trace record should be sufficient to reconstruct at minimum:

- `trace_id`,
- unit identity,
- gate identity,
- originating state reference,
- attempted operation/transform,
- outcome,
- resulting-state reference when produced,
- execution order/time index,
- relevant metadata/evidence.

The trace layer is intended to be immutable/auditable. This specification does not require a specific cryptographic ledger construction unless a profile explicitly defines one.

## 9. Minimal `.mg8` Manifest

A minimal unit manifest identifies the unit and its bound resources:

```json
{
  "mg8_version": "1.0",
  "unit_id": "example.unit.001",
  "entry": "flow.ork",
  "state": ["state/main.gst"],
  "gates": ["gates/main.g8son"],
  "trace": "trace/run.qson"
}
```

The manifest does not itself execute the gates. It binds the resources used by the runtime.

## 10. Deterministic Execution Contract

For the same canonicalized state, same gate definitions, same orchestration, and same runtime/profile rules, an MG8 execution should resolve the same admissibility and ordering decisions unless an explicitly declared external input changes.

A deterministic profile therefore needs explicit rules for:

1. canonical state encoding,
2. exact gate predicates,
3. execution ordering,
4. branch/tie resolution,
5. retry/failure behavior,
6. loop bounds,
7. trace ordering,
8. treatment of external/non-deterministic inputs.

## 11. State Transition Model

The unit-level execution model is:

```text
input / prior context
        ↓
.gst structured state
        ↓
flow.ork selects next operation
        ↓
.g8son evaluates transform eligibility
        ↓
pass / fail / indeterminate / branch
        ↓
state transition when authorized
        ↓
.qson event record
        ↓
next orchestration step
```

## 12. Relationship to `.mg8pk`

`.mg8pk` composes or distributes one or more `.mg8` units. It is a higher-level package artifact and should not be conflated with the unit itself.

The intended hierarchy is:

```text
.mg8pk
  ↓
system.ork
  ↓
.mg8
  ↓
flow.ork
  ↓
.gst + .g8son
  ↓
.qson
```

## 13. Scope Boundary

This document defines the `.mg8` unit and its place in the MG8 file family.

It does not fully specify the independent grammars for `.ork`, `.gst`, `.g8son`, `.qson`, or `.mg8pk`; those require their own versioned specifications.
