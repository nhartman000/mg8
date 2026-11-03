# Packed-profile verification

The envelope schema tests are structural tests, not a packed-runtime implementation.
They require Python 3 and `jsonschema>=4.20,<5`:

```sh
python -m unittest discover -s tests -p test_packed_envelope.py -v
python tools/check_compatibility.py
```

The independent Python and JavaScript implementations live in the TEXporT app and
browser-extension repositories. When the feature revisions are checked out as
siblings, run this opt-in interoperability suite from the MG8 repository:

```sh
TEXPORT_APP_ROOT="../TEXporT" \
TEXPORT_EXTENSION_ROOT="../Texport-browser-extension" \
python -m unittest discover -s tests -p test_packed_interop.py -v
```

Requirements: Node.js and the same Python `jsonschema` dependency. No Qt, browser,
provider keys, model calls or network requests are needed for these interop tests.
The selected product revisions must contain their packed-authoring APIs and example
fixtures; ordinary upstream revisions without this feature are not interchangeable.

The suite uses the real extension writer to generate fresh fixtures in a temporary
directory. It verifies:

- Python unit/package archives are accepted by the JavaScript reader.
- JavaScript units and 4-, 6-, 8-, and 12-unit packages are accepted by Python.
- Both writers' manifests, G8SON and QSON satisfy the pinned canonical member schemas.
- Cross-language gate import preserves original gate and GST bytes, source files
  and existing QSON events, appending a real review event rather than a fake gate PASS.

Without both environment variables the interop tests explicitly **skip**. Schema-only
CI passing therefore does not imply that cross-repository interoperability ran.
Each product also owns its full suite and actual UI interaction tests. Package UI
order does not establish executable state handoff, gate evaluation or reasoning quality.

Publish the exact tested revisions together with the versioned profile. Never infer
compatibility merely from a `.mg8` suffix or promote an unsupported loader to a packed
runtime. The existing canonical JSON manifest schema and historical profiles remain
unchanged by this additive serialization profile.
