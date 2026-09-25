# Review 1587: one bounded RO-Crate crosswalk

This revision adds an inspectable **SRR-subset → RO-Crate-profile JSON-LD →
SRR-subset** transport example. It addresses the request for one concrete mapping,
while preserving the distinction between self-round-trip evidence, standard
conformance, and independent interoperability. The result does not establish the
latter two properties.

## Standard target and declared extension

The example deliberately targets **RO-Crate 1.2**, the manuscript's cited version;
it does not imply that 1.2 is the newest release. The official
[metadata rules](https://www.researchobject.org/ro-crate/specification/1.2/metadata.html)
permit additional vocabulary terms and describe flattened JSON-LD entities with
identifiers, types, and references. We use ordinary Dataset, File and CreativeWork
metadata where those terms suffice, and a visibly separate experimental namespace
for MCRP-specific meaning.

The [root/descriptor specification](https://www.researchobject.org/ro-crate/specification/1.2/root-data-entity.html)
guides our metadata descriptor, root Dataset, title, description, publication date,
and license reference. `ro-crate-metadata.json` identifies its root through `about`
and declares the versioned RO-Crate target. Those conventional structural fields
are checked by tests independently of the export/import equality assertion.
This local subset checker is not an implementation of all requirements of the
RO-Crate specification.

The [profile rules](https://www.researchobject.org/ro-crate/specification/1.2/profiles.html)
separate a whole-crate profile declaration from the metadata descriptor's base
specification declaration. We therefore reference a bundled human-readable
`profile.html` from the root and include its profile entity. This local profile
URI resolves within the attached example directory; it is not a registered or
persistent profile identifier. The reserved example-domain namespace
`https://example.org/mcrp/toy-crosswalk/0.1#` makes the experiment explicit and is
not claimed to be an operational ontology resolver. A production profile would
need durable publication, broader documentation, independent tooling, and a
supported conformance process.

## Exact domain and preservation rule

The accepted SRR subset consists of release identity, title, description, date,
license, file identity/metadata, claim text and scope, declared requirements,
scoped decisions, and typed graph edges. Decisions include the claim reference,
declared actor, outcome, policy and synthetic validity tick. This example omits
full execution/environment manifests, authentic signatures, archive deposition,
resource envelopes, real authority verification, and the complete lifecycle.
It must not be described as transporting every possible SRR.

Let $X$ be the closed set of supported source records; let $E$ be the exporter and
$I$ the strict extension-aware importer. The intended bounded preservation property
is $I(E(x))=x$ for $x\in X$. Each source field maps to one explicit entity/property
or specified reference collection, and the inverse reads those fields back.
The importer reconstructs and reexports the source and checks equality of the
resulting entity map with the input entity map. This rejects unknown properties,
unknown entities, stripped extensions, and unsupported shapes rather than
silently dropping meaning. Graph entity order is irrelevant; broader RDF/JSON-LD
serialization equivalence is not implemented. This is a field-preservation
argument for a closed representation, not a general standards theorem.

| Source meaning | Export representation | Profile-aware recovery | Deliberately extension-unaware projection |
|---|---|---|---|
| Title, description, date, license | Root Dataset core properties and license contextual entity | Exact supported strings/references | Available as generic metadata |
| File identity, label, media type, byte count | File entity and core properties | Exact supported values | Available; no automatic scientific interpretation |
| Declared SHA-256 | `mcrp:sha256` on each file | Exact digest; optional local byte/hash check | Discarded by the demonstration consumer |
| Claim text | CreativeWork text; additional `mcrp:Claim` type | Exact text and claim ID | Text remains in graph, but claim semantics and root discovery links are lost |
| Scope and declared requirements | `mcrp:scope`, `mcrp:requires` references | Exact supported fields | Lost; a generic text display is not scoped reliance |
| Decision claim/actor/outcome/policy/validity | CreativeWork about plus explicit `mcrp:*` fields | Exact values, including pending/rejected outcomes | Decision meaning, authority assertions and validity lost |
| Typed dependency/interpretation relations | `mcrp:Edge` entities with source, target and kind | Exact typed relation list | Lost; no invalidation reachability can be inferred |
| Release identity and semantic object inventories | Root `mcrp:*` properties | Exact fields | Lost; root becomes generic discovery metadata |
| Unsupported richer SRR fields | No silent fallback | Export rejects them | Not assessed |

An unaware consumer may retain or ignore extensions in real software. Our
projection is explicitly a **chosen destructive consumer**: it strips them,
records every discarded path, and withdraws the local profile conformance
assertion. The importer then refuses to reconstruct MCRP semantics from that
projection. It does not assume that ordinary RO-Crate consumers interpret a
custom approval field correctly.

## Worked fixture and executable results

The source contains one twelve-byte text file with values 1.0, 2.0 and 3.0; a claim
restricted to their mean; a **pending** review disposition; and two typed evidence
relations. Export produces nine graph entities and a physical attached example
crate with the payload and local profile description. Reimport equals the exact
supported source record. The listed artifact payload's SHA-256 and byte count match. The verifier checks
that the local profile description exists but does not hash or authenticate it
or the metadata document; this is not whole-crate integrity verification. The
extension-unaware projection reports **22 discarded paths**, including semantic
types; these are field-loss paths, not 22 scientific failures.

Fourteen named tests check the round trip, standard-inspired descriptor/root
structure, entity-order tolerance, meaningful scope/outcome changes, unknown
source and crate fields, stripped scope/context, duplicate or alien entities,
dangling references, descriptor tampering, nested reference extras, explicit
extension loss, payload tampering, path restrictions, missing local profile, and
input nonmutation. Tests are internal author-side evidence. **No external
RO-Crate validator, general JSON-LD processor, or independently implemented
consumer was run.** Thus this demonstrates a concrete transport route and its
loss boundary, not universal RO-Crate conformance, round-trip conformance with
an arbitrary consumer, or scientific validation.

From the repository root:

```sh
python3 -m unittest discover -s examples/ro-crate-crosswalk -v
python3 examples/ro-crate-crosswalk/crosswalk.py
```

The source, `srr-input.json`, `example-crate/ro-crate-metadata.json`, actual payload,
`extension-unaware-projection.json`, `loss-manifest.json`, and `results.json` are
retained together. A useful independent next test is to ingest this crate in an
existing third-party RO-Crate tool, identify the fields it retains or drops, and
then build a separate extension-aware reader that reproduces the bounded source
and the same refusal cases. Until performed, that interoperability remains an
open task rather than a claimed result.
