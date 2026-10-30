# Verified reference stack and execution evidence

This index records actual hosted clean-wheel results, not proposed CI. The [compatibility matrix](COMPATIBILITY.md) and [repository authority map](REPOSITORY_AUTHORITY.md) define format and repository boundaries. No production certification, universal parser, deterministic inference, or fully locked transitive dependency claim is made.

## Published revisions and hosted CI

| Component | Merged reference revision | Actual hosted result |
|---|---|---|
| NYCH | `57b81e9220069dd5ff72197b41288c9613e3343b` ([PR #3](https://github.com/nhartman000/nych/pull/3)) | [Clean-wheel CI](https://github.com/nhartman000/nych/actions/runs/40249424426): Python 3.11, 3.12, 3.14, 199 tests each; [merged-main run](https://github.com/nhartman000/nych/actions/runs/40249523197) passed. |
| MG8 Engine | `daf260dae62bd27810d84b3107e0d22f1dd30736` ([PR #5](https://github.com/nhartman000/mg8-engine/pull/5)) | [Clean-wheel CI](https://github.com/nhartman000/mg8-engine/actions/runs/40249708946): Python 3.11, 3.13, 98 tests each plus 18 recorded observation checks; [merged-main run](https://github.com/nhartman000/mg8-engine/actions/runs/40250278984) passed. |
| MG8 Runtime | `c4b2bc4ab6bc051ae7ca53e69f457eb772d28097` ([PR #1](https://github.com/nhartman000/mg8-runtime/pull/1)) | [PR clean-wheel CI](https://github.com/nhartman000/mg8-runtime/actions/runs/41044188232) and [branch-push clean-wheel CI](https://github.com/nhartman000/mg8-runtime/actions/runs/41044179769): Python 3.11–3.14, 94 tests each, no skips. Tested source head `7b8647039de33ae4aca611999b4ac30aab743b6d`; [merged-main clean-wheel run](https://github.com/nhartman000/mg8-runtime/actions/runs/41044579318) and [merged-main conformance run](https://github.com/nhartman000/mg8-runtime/actions/runs/41044579243) also passed. |

Engine and Runtime use the published NYCH revision above, not an editable/source workaround or unpublished local dependency. NYCH includes its previously omitted `nych.schemas` subpackage and declares Python >=3.11 to match its mandatory pinned TCTA dependency. Wheel jobs check installed import provenance outside source and run `pip check`; these are distinct from merely passing source-tree tests.

Runtime's separate [normal conformance matrix](https://github.com/nhartman000/mg8-runtime/actions/runs/41044188124) passed, but intentionally skips optional NYCH integration when absent. Only the clean-wheel matrix above supplies the no-skip integration claim. Its pinned caller runs on push and pull request.

## Complete offline integration

The executable profile is `nych-runtime-one-unit/1`, described in the [pinned integration contract](https://github.com/nhartman000/mg8-runtime/blob/c4b2bc4ab6bc051ae7ca53e69f457eb772d28097/docs/NYCH_INTEGRATION.md).

1. Real installed NYCH semantic encoding processes `I see a red light.` and preserves the checkpoint in runtime GST.
2. Real NYCH `AtomicRequirement.evaluate()` supplies M-Gate PASS/FAIL/UNKNOWN evidence through a host-owned mechanical evaluator.
3. A loaded MG8 unit binds GST, G8SON, explicit JSON ORK/BONIT profiles, operation arguments and bounds. The trusted runtime performs exact-operation admission.
4. A single-use effect permit authorizes `accepted.txt`; fresh file observation and a separate commit permit authorize accepted state. SQLite and canonical-schema QSON retain evidence.
5. A separate read-only verifier process re-encodes the input, reads the file and persisted SQLite/QSON/GST, checks schema/source identities, record/event inventories, lifecycle transitions, candidate/operation/permit/receipt/commit bindings, audited expiry times and the hash chain.

Observed results in each clean-wheel CI job:

| Scenario | Separate verifier result | Effect/state |
|---|---|---|
| PASS | `VERIFIED_COMPLETE` | Expected file bytes and committed state verified. |
| FAIL | `VERIFIED_BLOCKED`, outcome `FAIL` | No file dispatch or commit; version-zero state retained. |
| UNKNOWN | `VERIFIED_BLOCKED`, outcome `INTERMEDIATE` | No file dispatch or commit; version-zero state retained. |

Independent review found and regression-tested rehashed candidate/permit tampering, unaudited extra operations, contradictory lifecycle statuses and expired authority. Final review approved after fixes. Package-resource schema discovery was exercised with actual `pip --target` and `pip --user` installations; schema bytes remain unchanged. Acceptance checks remain enabled under Python optimization.

### Reproduce from installed wheels

Build/install the pinned NYCH wheel and the pinned runtime wheel with its `integration` extra, then run outside both checkouts, using new output directories:

```sh
python -m mg8_runtime.nych_demo run ./pass
python -m mg8_runtime.nych_verify ./pass
python -m mg8_runtime.nych_demo run ./fail --scenario fail
python -m mg8_runtime.nych_verify ./fail
python -m mg8_runtime.nych_demo run ./unknown --scenario unknown
python -m mg8_runtime.nych_verify ./unknown
```

Each bundle contains the authored unit/resources, encoding checkpoint, SQLite store and `execution.qson`; successful runs also retain accepted bytes and committed GST. Hosted clean-wheel workflow artifacts retain scenario bundles and wheel-hash results.

### Independence and scope

This is independent persisted-state verification, not an independently reimplemented gate engine: producer and verifier share `GateSet`, `Registry`, loader and canonical-digest semantics. The verifier does not import the producer/adapter or instantiate Runtime/Store; its mechanical comparison is separately implemented. Shared semantics retain common-mode bug risk. Hash chains and source fingerprints are not signatures or protection against a malicious trusted host rewriting every artifact and verifier.

The demonstration is a fixed mechanical offline workflow, not model inference, automatic natural-language requirement compilation, the full NYCH pipeline, a TCTA admissibility integration, full block-language ORK/BONIT, or an MG8PK package graph. Run IDs, timestamps and QSON bytes vary. The earlier 18 model observations remain separate experimental repeatability evidence, not proof of universal deterministic inference.
