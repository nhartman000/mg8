# ORK Reference Profile v0.3

**Status:** interim reference profile, not a universal final grammar
**Author:** Nicholas Hartman / American Milestone Inc.

## Purpose

`.ork` carries orchestration: which step a process is on, how nested loops are
bounded, and who last wrote this revision. As of v0.3, `.ork` carries **only**
this invariant control shape. Everything domain-specific — who the actors are,
what each step does, what validation rules apply — lives in a separate file,
adopted by `.ork` via a `BONIT` reference, never inline.

This split exists because `.ork` is used across genuinely different
processes (e.g. the T.O.T.E.-loops database-population mesh run, and the
nych-encoder → LLM → mg8-engine pipeline). A single invariant header can
serve every use only if it contains nothing that could conflict between
uses. Step position and loop-control shape never conflict; a concrete
workflow of named actors and actions would.

## The `.bonit` file type

`.bonit` ("boot-init") holds the domain-specific ruleset a given `.ork`
instance adopts: authority/roles, workflow steps, validation rules, and
anything else specific to one process. `.ork` never embeds this content
directly — it only names which `.bonit` applies via the `BONIT` field.

Current known `.bonit` files:

- `TOTElibrary.bonit` (in `T.O.T.E-loops`) — the database-population mesh
  protocol, migrated out of `tote_population_mesh.ork` verbatim.
- `nych/nych.bonit` and `mg8-engine/mg8.bonit` now exist as authored
  block-syntax workflow specifications for encoder/mapping and engine
  congruence/gate-authoring stages. Some stages are implemented directly
  by pipeline code; the presence of these files does not establish a
  general executable BONIT parser. Implementation support must be declared
  per named profile, not inferred from a filename or a historical comment.

No standalone repository exists yet for `.bonit`, same status as `.ork`
itself — defined here, interim, until it earns its own repository.

## Reference representation (v0.3)

```
ORK/1.0
NAME <run-id>
MODE LIVE_INSTANCE
BONIT "<path-or-id of the adopted .bonit>"

POSITION {
  PATH [
    {STEP <int>, LABEL "<string>", ITER <int|null>, MAX_ITERATIONS <int|null>,
     EXIT_PREDICATE_REF "<string>|null", ON_BOUND_EXCEEDED "UNRESOLVED"|null}
    ...
  ]
  LAST_WRITER "<role>"
  WRITTEN_AT <iso8601|null>
  MARKER <int>
}
```

Field notes:

- `PATH` is an ordered stack, outermost to innermost. A flat sequential step
  (no loop) carries `null` for all four loop-control fields. A bounded loop —
  nested at any depth — carries its own `MAX_ITERATIONS`, `EXIT_PREDICATE_REF`,
  and `ON_BOUND_EXCEEDED`, independent of any other level's loop state. This
  is how multiple concurrent/nested loops each keep their own identifying
  marker rather than sharing one flat counter.
- `ON_BOUND_EXCEEDED` is fixed to the literal `"UNRESOLVED"` whenever a bound
  is declared — never free text, never a writer-invented failure mode. This
  is the fail-closed guarantee: a loop that exhausts its iteration bound
  without satisfying its exit predicate reports `UNRESOLVED`, it does not
  guess, and it does not silently continue.
- `WRITTEN_AT` is `null` whenever the writer (typically an LLM call) cannot
  produce a reliable timestamp. `MARKER` is a monotonic integer, incremented
  on every rewrite of this file regardless of whether `WRITTEN_AT` is
  populated — so chronological order is always recoverable even with no
  timestamp.
- `LAST_WRITER` names whichever actor (as defined in the adopted `.bonit`'s
  own authority/role block) produced this revision.

This JSON-like block shape is a reference profile only, same as v0.1/v0.2.
The canonical requirement is the invariant/domain split and the per-level
loop-control shape, not this exact serialization.

## Deterministic requirements

An ORK profile intended for reproducible execution must define any semantics
it uses for:

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

Unspecified ordering should not be relied on when deterministic execution is
claimed. As of v0.3, items 6–8 (loop bounds, retry policy, failure/
indeterminate handling) are carried structurally in every `.ork` instance's
`POSITION.PATH` entries rather than left to each implementation to define
ad hoc.

## Separation of responsibility

`.ork` should not become a second state store, a second audit ledger, or a
second home for domain-specific protocol content.

```text
.gst    = what state/context exists
.g8son  = what conditional gate/operator is evaluated
.ork    = when/where execution proceeds (position + loop control only)
.bonit  = which rules/actors/workflow this instance is running
.qson   = what actually occurred
```

## Package scope

At package scope, `system.ork` may order or connect multiple `.mg8` units.
Exact package-graph serialization remains an open versioned-specification
task; the invariant header shape above applies at every scope.

## Status boundary

This document exists because the role of `.ork` is established but a
standalone canonical `.ork` repository/complete grammar has not yet been
published — same for `.bonit`. Implementations should declare the ORK/BONIT
profile/version they support rather than assuming this minimal form is
universal.

## Change log

- v0.1 — initial minimal reference profile (`{"ork_version", "flow": [...]}`)
- v0.2 — superseded draft, never published; replaced before adoption
- v0.3 — invariant/domain split: `.ork` carries only `POSITION` (step +
  nested loop-control stack) and provenance (`LAST_WRITER`/`WRITTEN_AT`/
  `MARKER`); all protocol-specific content moved to the new `.bonit` file
  type, referenced via `BONIT`. Reconciled against the one real existing
  `.ork` instance, `T.O.T.E-loops/orchestration/tote_population_mesh.ork`
  (ORK/1.0 block syntax), which is the actual syntax adopted here —
  superseding the earlier JSON-only sketch.
