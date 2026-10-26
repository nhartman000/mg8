# MG8 family compatibility matrix

Authoritative machine registry: [compatibility.json](../registry/compatibility.json). This is a compatibility registry of named profiles, not a promise that every implementation accepts every file with a shared extension.

Registry SHA-256: `8b6a81739efa8925a468ae4e58e0d8573b60440f05a11da5dff4b96b00b44cae`

## Format authorities

| Format | Repository / branch | Pinned authority | Scope |
|---|---|---|---|
| MG8 | `nhartman000/mg8` / `main` | [175106883c0c](https://github.com/nhartman000/mg8/blob/175106883c0c3fc6b14894c4fbdd4cbd51e2b9b6/schema/mg8.schema.json) | Canonical resource-binding envelope 1.0. |
| ORK | `nhartman000/mg8` / `main` | [2f900083c9f2](https://github.com/nhartman000/mg8/blob/2f900083c9f275366885599623ddb6a7f4db910d/spec/ork_reference_profile.md) | Interim v0.3 block header: invariant position/bounds, BONIT reference; not a universal executable grammar. |
| BONIT | `nhartman000/mg8` / `main` | [2f900083c9f2](https://github.com/nhartman000/mg8/blob/2f900083c9f275366885599623ddb6a7f4db910d/spec/ork_reference_profile.md) | Interim domain-authority/workflow role; block language and named runtime JSON are different profiles. |
| GST | `nhartman000/gst` / `main` | [0d8aefbede38](https://github.com/nhartman000/gst/blob/0d8aefbede38a6e9e8ec671ef9a135d491147ff2/spec/gst_v1.md) | Conceptual v1 state/context/continuity contract; no universal payload JSON Schema published. |
| G8SON | `nhartman000/g8son` / `000` | [ecb193d90189](https://github.com/nhartman000/g8son/blob/ecb193d90189c8bfdb2d0e7cebb00432a1d0e260/schema/g8son.schema.json) | Canonical envelope with 1–3 gates; runtime/operator semantics require an explicit evaluator profile. |
| QSON | `nhartman000/qson` / `main` | [92e6e3e8f9f0](https://github.com/nhartman000/qson/blob/92e6e3e8f9f0fa4f501db21228116417d71df998/schema/qson.schema.json) | Canonical events envelope; event identity/sequence/type/structured actor. |

## Implementations and profiles

A profile listed below is not silently converted into another one. “Loaded” or “transmitted” does not mean “independently enforced.”

### nych-intake

Current deterministic encoder reference; M-Gate rule/evaluator interfaces. Repository: `nhartman000/nych`.

| Format | Actual support and boundary |
|---|---|
| MG8 | Legacy local container adapter; not canonical manifest export. |
| ORK | Workflow emission described in BONIT; not a full ORK v0.3 interpreter. |
| BONIT | nych.bonit describes staged workflow; not an executable language parser. |
| GST | build_gst emits canonical-concept-compatible pretext with unresolved findings. |
| G8SON | nych.schemas.g8son local transform-result profile is not dedicated canonical schema. |
| QSON | nych.schemas.qson local audit events/actor-string profile is not dedicated canonical schema. |

### mg8-engine-reference-1

Current prompt/container authoring and historical/reference executor; not trusted enforcement runtime. Repository: `nhartman000/mg8-engine`.

| Format | Actual support and boundary |
|---|---|
| MG8 | Canonical resource-binding envelope plus explicitly retained embedded legacy units. |
| ORK | Flat JSON flow/ork_flow/steps gate order; pinned loader does not validate profile identity or reject foreign BONIT/control fields. Do not use it for policy enforcement. |
| BONIT | Block mg8.bonit is a specification; fixed mapping/congruence checks implemented in pipeline code, not a generic parser. |
| GST | Pydantic state/context model; profile-specific merge/projection, not universal temporal advancement. |
| G8SON | Canonical-style 1–3 gate array loading and permissive legacy single-gate models; not full dedicated-schema validation, and generic executor trusts callback outcomes. |
| QSON | Legacy entries/step/actor-string reference-model serialization; NOT canonical events schema. |

### response-contract-v1

Opt-in NYCH-first model-facing contract and fresh response byte comparison. Repository: `nhartman000/mg8-engine`.

| Format | Actual support and boundary |
|---|---|
| MG8 | Resource-binding envelope, one GST. |
| ORK | Exact named repeatability-experiment-v1 generate_once subset; no repair/reuse, unsupported controls rejected. |
| BONIT | Not consumed by this profile; no implied BONIT execution. |
| GST | Full authored globals/facts/context supplied to model. |
| G8SON | Explicit historical atomic_requirements profile, preserved text/IDs; semantic requirements not independently certified. |
| QSON | Same engine entries reference-model export; comparison result separate from semantic gate result. |

### mg8-runtime-sequential/0.1

Current enforced-admission/permit/commit reference runtime; initial profile, not certified production deployment. Repository: `nhartman000/mg8-runtime`.

| Format | Actual support and boundary |
|---|---|
| MG8 | Strict 1.0 resource envelope, exactly one GST, confined source snapshots. |
| ORK | Only JSON ork_profile=mg8-runtime-sequential/0.1 with bonit and complete sequential flow. |
| BONIT | Only JSON bonit_profile=mg8-runtime/0.1 actors/scopes/budgets/bindings; rejects other grammar. |
| GST | Requires gst_version=1.0 and explicit state object; no automatic full internal/external chronology merge. |
| G8SON | Canonical schema/AND OR NAND NOR ternary evaluator; historical requirements only with explicit reviewed bindings. |
| QSON | Canonical schema events export; authoritative append-only SQLite and verified per-run hash chain. |

### historical-mgate-keeper

Maintained historical experiment/reproduction surface, not canonical format authority or enforcement runtime. Repository: `nhartman000/mgate-keeper`.

| Format | Actual support and boundary |
|---|---|
| MG8 | Earlier experiment/project configuration. |
| ORK | No current block-language execution claim. |
| BONIT | No generic interpreter. |
| GST | Context plus constraints transmitted in current repository; old ZIP implementations may omit them. |
| G8SON | Prompt requirements; does not establish independent domain evaluation. |
| QSON | Experiment audit response-pair profile; do not relabel canonical ledger. |

### historical-mgate-suite

Historical/experimental GUI/engine implementation; existing status document identifies role drift. Repository: `nhartman000/mgate-suite`.

| Format | Actual support and boundary |
|---|---|
| MG8 | Historical project/orchestration meaning, not current unit envelope. |
| ORK | Historical graph/flow behavior, not current v0.3 parser. |
| BONIT | No current universal interpreter claim. |
| GST | Historical context modifiers. |
| G8SON | Historical Boolean/graph behavior; use its own schemas only. |
| QSON | Historical trace format; no implicit canonical conversion. |

## Pinned implementation sources

These inspected baselines, not unpublished sibling-worktree changes or moving branch tips, define the cells above. Each named profile has the same revision and source paths in the machine registry. Authority correction `2f900083c9f275366885599623ddb6a7f4db910d` is included in this publication branch; it is not a claim that `main` already contains it.

| Profile | Inspected revision | Source boundaries |
|---|---|---|
| `nych-intake` | `cee3610723ffe4877c424591711fed29717ab655` | [nych/gst_export.py](https://github.com/nhartman000/nych/blob/cee3610723ffe4877c424591711fed29717ab655/nych/gst_export.py), [nych/schemas/mg8.py](https://github.com/nhartman000/nych/blob/cee3610723ffe4877c424591711fed29717ab655/nych/schemas/mg8.py), [nych/schemas/g8son.py](https://github.com/nhartman000/nych/blob/cee3610723ffe4877c424591711fed29717ab655/nych/schemas/g8son.py), [nych/schemas/qson.py](https://github.com/nhartman000/nych/blob/cee3610723ffe4877c424591711fed29717ab655/nych/schemas/qson.py), [nych/gates.py](https://github.com/nhartman000/nych/blob/cee3610723ffe4877c424591711fed29717ab655/nych/gates.py), [nych.bonit](https://github.com/nhartman000/nych/blob/cee3610723ffe4877c424591711fed29717ab655/nych.bonit) |
| `mg8-engine-reference-1` | `72b954d78e8168d0e4f7862085ececf3cd97a80a` | [src/mg8_engine/core.py](https://github.com/nhartman000/mg8-engine/blob/72b954d78e8168d0e4f7862085ececf3cd97a80a/src/mg8_engine/core.py), [src/mg8_engine/ork.py](https://github.com/nhartman000/mg8-engine/blob/72b954d78e8168d0e4f7862085ececf3cd97a80a/src/mg8_engine/ork.py), [src/mg8_engine/models.py](https://github.com/nhartman000/mg8-engine/blob/72b954d78e8168d0e4f7862085ececf3cd97a80a/src/mg8_engine/models.py), [src/mg8_engine/pipeline.py](https://github.com/nhartman000/mg8-engine/blob/72b954d78e8168d0e4f7862085ececf3cd97a80a/src/mg8_engine/pipeline.py), [mg8.bonit](https://github.com/nhartman000/mg8-engine/blob/72b954d78e8168d0e4f7862085ececf3cd97a80a/mg8.bonit) |
| `response-contract-v1` | `72b954d78e8168d0e4f7862085ececf3cd97a80a` | [src/mg8_engine/response_contract.py](https://github.com/nhartman000/mg8-engine/blob/72b954d78e8168d0e4f7862085ececf3cd97a80a/src/mg8_engine/response_contract.py), [docs/response-contracts.md](https://github.com/nhartman000/mg8-engine/blob/72b954d78e8168d0e4f7862085ececf3cd97a80a/docs/response-contracts.md) |
| `mg8-runtime-sequential/0.1` | `514cc3e0eb2146ee4156450e76b705d67de05f14` | [src/mg8_runtime/loader.py](https://github.com/nhartman000/mg8-runtime/blob/514cc3e0eb2146ee4156450e76b705d67de05f14/src/mg8_runtime/loader.py), [src/mg8_runtime/gates.py](https://github.com/nhartman000/mg8-runtime/blob/514cc3e0eb2146ee4156450e76b705d67de05f14/src/mg8_runtime/gates.py), [src/mg8_runtime/store.py](https://github.com/nhartman000/mg8-runtime/blob/514cc3e0eb2146ee4156450e76b705d67de05f14/src/mg8_runtime/store.py), [docs/IMPLEMENTATION.md](https://github.com/nhartman000/mg8-runtime/blob/514cc3e0eb2146ee4156450e76b705d67de05f14/docs/IMPLEMENTATION.md) |
| `historical-mgate-keeper` | `02036d7b58790df98984c5c0d0f0b10feba45a33` | [mgate_keeper/__init__.py](https://github.com/nhartman000/mgate-keeper/blob/02036d7b58790df98984c5c0d0f0b10feba45a33/mgate_keeper/__init__.py) |
| `historical-mgate-suite` | `b5bac36447f50f438d780e678cff3c73da5deaa9` | [IMPLEMENTATION_STATUS.md](https://github.com/nhartman000/mgate-suite/blob/b5bac36447f50f438d780e678cff3c73da5deaa9/IMPLEMENTATION_STATUS.md), [spec/version_matrix.json](https://github.com/nhartman000/mgate-suite/blob/b5bac36447f50f438d780e678cff3c73da5deaa9/spec/version_matrix.json) |

## Outcomes and historical adapters

- NYCH evaluator results are PASS / FAIL / UNKNOWN. Canonical gate traces use PASS / FAIL / INTERMEDIATE; UNKNOWN maps to INTERMEDIATE, never PASS.
- Controller exhaustion is UNRESOLVED. It is not globally redefined as a predicate FAIL; any mapping in a historical BONIT profile is local to that profile.
- A model-returned transformed/PASS flag is not trusted state-commit authority. Use the enforcement runtime when permits and independent postconditions are required.
- G8SON atomic requirements and engine/NYCH local QSON ledgers remain explicit legacy/reference profiles, not canonical schema exports.
- MG8 Runtime’s JSON ORK/BONIT subset is not the block-syntax v0.3 language. At the pinned engine baseline, the generic loader may read the flow while ignoring foreign policy/control fields; it does not provide fail-closed profile rejection. Later hardening is not credited until its published revision is explicitly pinned.
- Full MG8PK package graphs, universal BONIT execution and full GST chronology advancement are not implied.

## Verification

Run `python tools/check_compatibility.py` after installing `jsonschema`. It verifies pinned schema bytes, canonical examples and expected legacy-profile mismatches. The clean-install and end-to-end evidence index is published separately; source claims alone do not establish execution.

No repository is certified production-ready by this document. [Repository authority and consolidation](REPOSITORY_AUTHORITY.md) defines the current reference entry points without deleting or merging historical branches.
