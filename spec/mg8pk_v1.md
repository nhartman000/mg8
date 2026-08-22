# MG8PK Package Specification v1 — Baseline

**Author:** Nicholas Hartman / American Milestone Inc.  
**Status:** baseline package-role specification; detailed archive/serialization rules remain open

## Purpose

`.mg8pk` is the package/composition layer for distributing or composing one or more bounded `.mg8` execution units together with package-level orchestration and supporting resources.

The established hierarchy is:

```text
.mg8pk
  ↓
system.ork
  ↓
one or more .mg8 units
```

## Required conceptual contents

An MG8 package must be capable of identifying:

- a package identity/version;
- one or more `.mg8` units;
- package-level entry/orchestration (`system.ork` or an explicitly declared equivalent profile);
- any resources required to resolve the packaged units without ambiguous external paths;
- integrity/provenance metadata where the package profile defines it.

## Package boundary

`.mg8pk` is **not** the execution unit itself. The contained `.mg8` units remain individually bounded and auditable.

Package composition therefore does not erase:

- unit identity;
- state identity;
- gate identity;
- run identity;
- event-level `trace_id`.

## Path safety

A deterministic/self-contained package profile should use relative internal references and define how resource traversal is constrained. Package extraction or resolution must not implicitly authorize arbitrary filesystem access outside the package destination.

## Minimal conceptual manifest

The following illustrates the established role without freezing a final serialization grammar:

```json
{
  "mg8pk_version": "1.0",
  "package_id": "example.package.001",
  "entry": "system.ork",
  "units": [
    "units/unit-a.mg8",
    "units/unit-b.mg8"
  ]
}
```

This is a baseline representation, not a claim that every future `.mg8pk` package must be a plain JSON file rather than an archive/container format.

## Relationship to historical formats

Earlier MGate implementations used names such as `.zipson` for package/domain composition. The current canonical package role is `.mg8pk`. Historical `.zipson` artifacts should be preserved for provenance rather than silently renamed without semantic validation.

## Open specification items

The following remain intentionally unresolved until separately versioned:

- physical archive/container encoding;
- compression rules;
- canonical ordering;
- hash/signature manifest requirements;
- dependency embedding versus external references;
- package-level multi-unit branch/join grammar;
- content-addressing rules.

These gaps should be documented rather than filled by implementation-specific assumptions.
