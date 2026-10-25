# Response-contract profile v1

Status: opt-in model-facing prompt profile and bounded reference implementation. It does not amend the canonical MG8 manifest schema or establish deterministic LLM inference.

## Role and order

Natural-language prompt → canonical NYCH intake → MG8 resource binding → GST/G8SON response contract → fresh model call → recorded observation and optional byte-repeatability comparison.

MG8 has uses beyond this profile. Here it binds a response-oriented contract; NYCH does not become a gate evaluator, GST remains state/context, G8SON carries requirements, ORK declares bounded generation behavior, and QSON records observations. A model's self-reported PASS is not independent semantic evidence.

## Resources

The [examples](../examples/response-contracts/) contain three independently selectable units. Each `response.mg8` points to one `context.gst`, one `conditions.g8son`, `flow.ork`, and a relative `.qson` trace reference. Example paths remain within the unit directory.

GST preserves global audience/voice/tense/format/whitespace rules and facts. G8SON preserves requirement IDs and natural-language `atomic_requirements`. This is the explicitly named requirement profile; it is not presented as a migration of the dedicated G8SON schema. All fields are supplied to the model rather than printed locally and silently omitted from the request.

The selected ORK subset declares one generation per trial, no automatic repair and no answer reuse. A repeatability experiment repeats independent trials; it does not reinterpret the per-trial bound as permission for arbitrary retries. Unsupported controls must be rejected rather than ignored. This profile is not a universal ORK interpreter or the general state-commit/effect-authority runtime.

## Contract alternatives

- `simple`: one active-voice, present-tense sentence, 16–24 words, plain-language intent and explicit formatting globals. Most phrasing remains open.
- `ordered`: fixed subject, finite verb, scientific term spellings and energy/input/output order, while some phrasing remains open.
- `grammar`: a single syntactic production with fixed lexical connectors. It deliberately approaches serialization of facts rather than open-ended prose generation.

No complete answer or historical matching output is included as an example inside these model-facing resources. The facts supplied to GST do substantially narrow the task; that must be counted when assessing results.

## Execution and evidence

The engine implementation and operational documentation are in [mg8-engine](https://github.com/nhartman000/mg8-engine/blob/main/docs/response-contracts.md). Existing engine profiles and sampling defaults are not silently changed. This new profile omits temperature and seed instead of sending null/default values. Providers and caller-supplied transports must preserve that choice.

The [live evidence](../experiments/response-contracts/README.md) retains the original divergent batch as well as the revised matches. Each revised unit matched byte-for-byte across three fresh calls under the tested model and context. No cached answer, prior-output injection, trimming or repair was used. This is observed finite repeatability, not a universal guarantee or certification of ninth-grade readability/scientific accuracy. Provider input caching is distinct from answer reuse and is reported separately.

Response hashes, request identity, semantic requirement satisfaction and runtime authorization are separate properties. Reproducibility records must not be relabeled as proof that all semantic G8SON requirements passed. Published experimental `.qson` ledgers name their serialization profile; independent canonical-QSON conformance is not claimed.
