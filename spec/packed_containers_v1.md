# Packed MG8 and MG8PK containers — profile 1.0

**Author:** Nicholas Hartman / American Milestone Inc.
**Status:** versioned opt-in physical serialization and authoring profile; not an extension of an existing runtime's supported execution grammar.

## Purpose and compatibility

A packed `.mg8` is **one physical file** holding its manifest, GST state, G8SON gate definitions, unit ORK script and QSON ledger. A packed `.mg8pk` holds complete packed units and package orchestration. Neither requires loose external resources.

This profile layers physical containment over the [existing unit manifest](mg8_v1.md) and [package role](mg8pk_v1.md); it does not replace their resource identities or modify the legacy JSON manifest schema. Existing plain-JSON `.mg8` files remain valid for their declared profiles. Legacy readers MUST NOT be assumed capable of reading packed files. Container readers MUST identify the profile explicitly and fail closed on unknown versions. A file extension alone never establishes compatibility.

## Archive envelope

Use ZIP with storage method **0 (STORE)**, not compression. Members retain their individual bytes. A reader does not need to decompress content, and may read entries in memory without filesystem extraction. Container size is at most 16 MiB, at most 128 file entries, and the sum of member uncompressed sizes is at most 16 MiB. Unit resource members are at most 1 MiB each; package members containing complete units may be at most 16 MiB subject to the outer total bound. A package has 1–32 units. ZIP64, encrypted archives, multipart archives, symlink/special entries and unsupported methods are rejected by this first profile. No directories need explicit archive entries.

Every archive contains UTF-8 `container.json`:

```json
{
  "profile": "mg8-packed/1.0",
  "kind": "unit",
  "manifest": "manifest.json",
  "integrity": {
    "manifest.json": "<lowercase SHA-256 of exact member bytes>",
    "flow.ork": "<lowercase SHA-256 of exact member bytes>"
  }
}
```

The illustrated hashes are placeholders, not literal valid values. The real integrity map MUST cover **every other member exactly once**, excluding `container.json` itself. No unlisted members are allowed. Verify all hashes before use. SHA-256 is integrity metadata, not a signature, trusted origin, or authorization to execute.

Packages instead declare `profile: mg8pk-packed/1.0`, `kind: package`. Other container fields are identical. [Envelope schema](../schema/packed-container.schema.json) validates the JSON envelope only; archive, resource and cross-reference checks are additional requirements.

Paths are portable ASCII slash-separated relative paths matching `[A-Za-z0-9_-][A-Za-z0-9_./-]*`. User-facing labels may remain Unicode, but internal resource names must satisfy this portable subset. Reject empty names, empty/dot/dot-dot components, leading slash, backslashes, drive/UNC names, control characters, NUL, duplicate paths and case-insensitive path collisions. Local and central ZIP records must agree on entry identity, method, sizes and CRC; reject malformed, truncated or inconsistent records. Never resolve a resource outside the archive. Imported JSON must be strict finite JSON; duplicate object keys are invalid. Readers must apply bounds before allocating or reading member payloads.

Writers should use stable entry order, consistent ZIP metadata and consistent JSON serialization for reproducible packaging when input bytes and identities are unchanged. This does not make LLM inference deterministic or imply identical archives after new audit events.

## Unit contents

```text
review.mg8
├── container.json
├── manifest.json
├── flow.ork
├── state/context.gst
├── gates/eligibility.g8son
├── gates/completion.g8son
└── trace/execution.qson
```

`manifest.json` conforms to the existing MG8 manifest schema with `mg8_version: 1.0`. Entry, state, gates and trace references MUST resolve to contained members of the expected file type. A unit has at least one GST resource and one G8SON resource. Each G8SON file has 1–3 gates; multiple bounded files may be included. Preserve source file IDs, gate IDs and exact copied bytes; reject conflicting identities instead of renaming them silently. Gate identities are unique within the unit. Different units retain their own identity scopes.

GST carries global Gestalt, context, variables and state. This first interoperable authoring subset requires `gst_version: "1.0"`, a nonblank string `state_id`, `internal` and `external` objects each containing `prior` and `current`, a `continuity` object, nonblank `intent` and `outcome_expectation` strings, and a `constraints` object. Global Gestalt/context/variables and original source snapshots are retained within this state structure; missing values remain explicitly unresolved. A `context_id` alone is not this subset's state identity. These requirements name a supported authoring subset, not a new universal GST schema.

G8SON declares conditions/conditional operators, not context storage. ORK owns ordering and bounds; putting files in an archive does not define or execute a flow. Internal paths are at most 240 ASCII characters and identifiers at most 200 characters with no control characters.

TEXporT may emit this explicitly data-only unit authoring subset:

```json
{
  "ork_profile": "texport-packed-authoring/1.0",
  "flow": ["eligibility", "completion"],
  "max_iterations": 1,
  "on_fail": "stop",
  "on_unknown": "review"
}
```

The flow lists gate IDs in approved order, which may differ from gate-file enumeration order. It must cover every contained gate exactly once; imported gates append without reordering the existing reviewed flow. The only allowed keys for this profile are `ork_profile`, `flow`, `max_iterations`, `on_fail`, and `on_unknown`. Unsupported fields such as branches or parallel execution are rejected, not ignored. All contained G8SON files must be listed in the manifest. This subset is not a claim that the legacy reference executor implements these routes. Runtimes must explicitly opt in and validate their supported profile before execution. Unknown outcomes never authorize acceptance or a state commit.

## QSON and container snapshots

A new exported unit contains a real authoring/review event, **not fabricated execution evidence**. QSON resource fields must satisfy the current canonical QSON schema. This subset further requires event sequences contiguous from 1 and each event's `run_id` equal to the ledger `run_id`. Trace IDs must be unique in the ledger; actor type/id are nonblank strings; optional timestamps must be valid timezone-qualified RFC 3339 values; optional results, references and metadata retain their declared schema types. For QSON schemas requiring a nonempty ledger, record `event_type: review`, its actual actor, run/event identities and ordered sequence, with a reason identifying assembly/export. Do not manufacture a successful gate attempt or state commit to initialize the ledger. Event-level `trace_id` and run identity remain distinct from file and gate identity.

A saved archive is a snapshot. Editing containment or authoring flow produces a new snapshot and may append an appropriate real review event. Existing ledger events and their identities must remain unchanged; rewriting the ZIP envelope is not permission to rewrite history. Runtime trace updates require a separately declared writable snapshot/lifecycle policy; this packaging profile does not implement execution, concurrency control, signatures or a trusted append-only store.

## Non-destructive gate import

Dropping one or more G8SON files onto a unit is an authoring action:

1. Validate the original unit, bounded imported files, IDs and destination paths.
2. Copy exact source bytes inside the unit; never delete or modify the original external gate files.
3. Preview the changed membership and explicit flow order. Reject collisions or unsupported orchestration; do not guess branch placement.
4. Update manifest membership and approved flow, retain existing resources, append a real review event, and recalculate envelope integrity.
5. Save a new `.mg8` file. Filesystem implementations must avoid unintended overwrite/partial publication; browser downloads follow browser destination policy.

Importing content never executes it, grants permissions or establishes that its conditions passed. Captured text and imported definitions remain untrusted data until explicitly approved for authoring, and runtime authority is still separate.

## Package contents and ordered composition

```text
reasoning.mg8pk
├── container.json
├── manifest.json
├── system.ork
└── units/
    ├── research.mg8
    ├── analysis.mg8
    ├── critique.mg8
    └── synthesis.mg8
```

Package `manifest.json` contains `mg8pk_version: 1.0`, a stable `package_id`, `entry: system.ork`, and an ordered `units` array. Each entry resolves to a complete packed unit; validate the nested container and its resource references. Reject duplicate unit identities in one package. Package-within-package nesting is unsupported. Do not extract or flatten unit identities into the package scope.

The first data-only package authoring profile is:

```json
{
  "ork_profile": "mg8pk-sequential/1.0",
  "flow": ["units/research.mg8", "units/analysis.mg8", "units/critique.mg8", "units/synthesis.mg8"],
  "max_steps": 4,
  "on_fail": "stop",
  "on_unknown": "review"
}
```

Flow matches the manifest unit order exactly and `max_steps` equals that finite count. Only `ork_profile`, `flow`, `max_steps`, `on_fail`, and `on_unknown` are accepted in this package ORK subset. The package manifest accepts only `mg8pk_version`, `package_id`, `entry`, `units`, and optional object `metadata`. All contained `.mg8` units must participate in the manifest and flow; unlisted execution units and nested packages are rejected. This supports explicit chains of 4, 6, 8, 12 or other bounded counts without treating those numbers as special file-format variants. Actual state handoff, evaluation, branching, joins and multi-unit runtime execution require a separately implemented compatible runtime. Packaging alone does not prove improved reasoning, successful execution or determinism of model output.

## ICM workspace relationship

ICM organizes surrounding source, themed text and navigation. A thematic folder may contain labelled `.txt` files, editable companion resources and the corresponding packed `.mg8` alongside them. The packed file must independently contain all declared unit resources; nearby files are authoring sources, not hidden runtime dependencies. Groups lacking approved gates can remain ordinary text folders without manufactured MG8 units. MG8PK composes selected units, not arbitrary ICM folders.

AI organization must propose source-linked groups and conditions for review, preserve original markers/notes/provenance, retain unresolved information and distinguish proposal from execution. Automatic categorization does not itself authorize agent actions.
