# MG8 Architecture

**Nicholas Hartman / American Milestone Inc.**

## 1. File-family hierarchy

```text
.mg8pk
  ↓
system.ork
  ↓
.mg8 bounded unit
  ↓
flow.ork
  ├── .gst state/context
  ├── .g8son conditional gates/operators
  └── .qson execution/transformation trace
```

The levels are intentionally distinct:

- `.mg8pk` composes/distributes one or more bounded units.
- `.mg8` binds the resources for one bounded execution unit.
- `.ork` defines execution topology and ordering.
- `.gst` represents structured state and constraints.
- `.g8son` defines bounded conditional transform eligibility.
- `.qson` records realized execution events.

## 2. Unit execution

A unit executes conceptually as:

```text
load .mg8 manifest
      ↓
enter flow.ork
      ↓
load current/prior .gst state
      ↓
select .g8son gate
      ↓
evaluate admissibility
      ↓
pass / fail / indeterminate / branch
      ↓
apply authorized transition
      ↓
write event-level .qson trace
      ↓
continue flow.ork
```

## 3. State is separate from gate logic

MG8 does not collapse state, logic, and audit into one file.

`.gst` is the state/context substrate. `.g8son` operates against that substrate. `.qson` records what actually occurred. `.ork` determines when and in what order those operations happen.

This separation supports auditability and makes it possible to reason about:

- what state existed,
- what gate was evaluated,
- what decision was made,
- what transition occurred,
- what event produced the trace.

## 4. Identity layers

MG8 distinguishes three identities:

```text
file identity
    ≠
gate identity
    ≠
execution identity
```

A `.g8son` file may contain 1–3 gates. Each gate has its own stable gate identity. Every gate execution attempt receives a unique `trace_id`.

This means the same gate can be executed repeatedly without collapsing multiple execution events into one audit record.

## 5. Determinism boundary

A deterministic MG8 profile requires explicit handling of:

- canonical state representation,
- exact gate predicates,
- execution ordering,
- tie-breaking,
- branch semantics,
- failure/retry behavior,
- loop bounds,
- external input declaration,
- trace ordering.

The runtime must not rely on unspecified ordering or implicit fallbacks if reproducible execution is required.

## 6. `.gst` continuity role

The `.gst` layer is where current and historical state continuity belongs. The larger state model includes prior/current state and may distinguish internal and external state detection.

The conceptual progression is:

```text
prior state
    +
current state
    ↓
temporal continuity / memory
    ↓
state-detection context
```

Higher-order awareness/intent semantics belong to `.gst` profiles and are not treated as gate syntax.

## 7. Audit relationship

A realized transform should be traceable from state through gate decision to result:

```text
state reference
   ↓
gate identity
   ↓
trace_id
   ↓
operation / transform attempt
   ↓
outcome
   ↓
resulting state reference
```

This is the core provenance chain within one `.mg8` unit.
