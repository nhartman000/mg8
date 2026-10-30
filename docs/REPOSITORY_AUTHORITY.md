# Repository authority and consolidation

Source registry: [repositories.json](../registry/repositories.json). Consolidation here is explicit ownership/routing, not a destructive monorepo migration.

| Subsystem | Current repository / branch | Designation | Responsibility |
|---|---|---|---|
| encoder-and-mgate | [nhartman000/nych](https://github.com/nhartman000/nych) / `main` | current-reference | NYCH deterministic intake, symbolic context and M-Gate AtomicRequirement interfaces |
| prompt-authoring-engine | [nhartman000/mg8-engine](https://github.com/nhartman000/mg8-engine) / `main` | current-reference | Container/response contract authoring and reference execution; not trusted state/effect authority |
| enforcement-runtime | [nhartman000/mg8-runtime](https://github.com/nhartman000/mg8-runtime) / `main` | current-reference | Trusted host admission, evaluator registration, permits, state commits and QSON |
| mg8-ork-bonit-authority | [nhartman000/mg8](https://github.com/nhartman000/mg8) / `main` | canonical-format-authority | MG8 unit schema and interim ORK/BONIT role/profile registry |
| gst-authority | [nhartman000/gst](https://github.com/nhartman000/gst) / `main` | canonical-format-authority | GST conceptual state/context/continuity semantics |
| g8son-authority | [nhartman000/g8son](https://github.com/nhartman000/g8son) / `000` | canonical-format-authority | G8SON bounded-gate schema |
| qson-authority | [nhartman000/qson](https://github.com/nhartman000/qson) / `main` | canonical-format-authority | QSON events/sequence/actor trace schema |
| reproducibility-prototype | [nhartman000/mgate-keeper](https://github.com/nhartman000/mgate-keeper) / `main` | historical-experiment | Historical reproducibility surface, not trusted admission authority |
| gui-and-older-engine | [nhartman000/mgate-suite](https://github.com/nhartman000/mgate-suite) / `main` | historical-experimental | Older suite with historical format roles explicitly documented |

## Selection policy

1. For new symbolic intake use `nych/main`; for prompt/container authoring use `mg8-engine/main`; for trusted admission, effects and state commits use `mg8-runtime/main`. These are complementary roles, not three competing production runtimes.
2. Dedicated format repositories govern interchange. G8SON’s actual default branch is `000`, not an assumed `main`. ORK/BONIT roles and supported profile identities are registered in the MG8 repository.
3. `mgate-keeper` is a historical experiment surface; current repository code must not be confused with older ZIP snapshots that omitted gate/context transmission. `mgate-suite` remains the historical/experimental older suite as its own implementation-status document already states.
4. Unmerged branches, including `mg8-engine` PR3 (`codex/implementable-mg8-v0.4`), do not define current main behavior. No implicit merge, branch deletion, history rewrite, repository archival or file-identity migration is performed by this registry.
5. Private similarly named research repositories are not designated current deployment targets here; this is not a claim that their implementations were audited or archived.
6. No production-readiness or security certification is implied. A deployed application must still pin versions and enforce host/process capabilities.

The designation is a routing choice, not a moving-tip compatibility guarantee. Exact implementation baselines and pinned source links are in the [matrix source table](COMPATIBILITY.md#pinned-implementation-sources) and machine registries; unpublished fixes are not credited to those baselines.

See the [compatibility matrix](COMPATIBILITY.md) for actual supported and unsupported serialization/execution profiles and the [verified stack index](VERIFIED_STACK.md) for published revisions, actual CI and independent final-state verification.
