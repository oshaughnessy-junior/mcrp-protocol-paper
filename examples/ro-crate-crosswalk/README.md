# Bounded RO-Crate 1.2 crosswalk

Run from the repository root:

```sh
python3 -m unittest discover -s examples/ro-crate-crosswalk -v
python3 examples/ro-crate-crosswalk/crosswalk.py
```

Python standard library only. No network, external JSON-LD processor, RO-Crate
validator, authentication, or scientific execution is used. The official context
URI is emitted as metadata but is not fetched by the code.

The fixture maps a **closed SRR subset** to flattened, RO-Crate-shaped JSON-LD,
using core Dataset/File/CreativeWork metadata and explicit namespaced MCRP
extensions. The attached `example-crate/` contains a real small payload and local
human-readable profile. `profile.html` specifies the deliberately strict subset;
`../../paper/revisions/review1587-crosswalk.md` supplies the source mapping,
preservation/loss table and primary specification references.

`import_crate` is an inverse for this exporter, not a general RO-Crate importer.
Unknown fields, contexts or entities are rejected; so are critical-field removal,
dangling links and unsupported shapes. Equivalent JSON-LD using a different
serialization may be rejected. `verify_payloads` separately checks actual local
bytes of listed artifact payloads; import alone preserves claimed hashes but does
not verify them. The verifier checks that the bundled profile description exists,
but does not hash or authenticate that description or the metadata document. It
is not an integrity verifier for the entire crate.

`extension-unaware-projection.json` is an intentionally destructive generic
consumer example. It emits `loss-manifest.json` and withdraws the local profile
claim. Its missing MCRP fields must not be interpreted as valid defaults. The
reserved example.org namespace and local profile are not registered persistent
vocabulary/profile identifiers.

**Results:** exact self-roundtrip, nine entities, matching payload hash/size,
22 explicitly discarded semantic paths in the unaware projection, and fourteen
passing named tests. This is internal transport evidence, not independent
consumer interoperability, full standards conformance, full SRR transport,
scientific review, or qualified human sign-off. The example disposition is pending.

Original prose and example data are CC BY 4.0; code is MIT licensed (LICENSE).
The RO-Crate specification and other cited works retain their own rights.
