# Cross-review of the assurance insertion and transport claims

Reviewer: author-directed evidence agent. This is a second code/prose inspection,
not independent scientific sign-off.

## Assurance: no blocking mismatch found

I independently ran all 20 tests in `examples/assurance-assignment/`; all passed.
I then constructed the three table records from `fixture()` and the stated row
changes rather than relying on demonstration output: remove the human disposition
row for E0, set independent challenge unknown for E2, and authorize the platform
subcase exemption for E3. Computed current levels were exactly `[0, 2, 3]`.

The nine S1 rows, three additional S2 rows and five additional S3 rows match the
17-rule fixture. Only the named platform and sensitivity subcases permit the
listed domain-steward exemptions; overall sensitivity remains mandatory. The
currentness distinction between unknown outcome and stale/disputed authority is
faithfully described. Literal fixture actors are allow-list assertions, explicitly
not authenticated identities or proof of independence.

Minor completeness suggestion: add the exact E2 example to `run_demo.py` and its
saved results so all three main-text records have named machine-readable cases.
The table is currently sufficient to reconstruct E2, as the independent probe did.

## Transport: preserve the limit of the claim

The inspected `ro-crate-crosswalk/crosswalk.py` is a closed custom exporter/importer.
Its inverse verifies equality with its own canonical emitted graph; this proves
self-round-trip preservation on the supported subset. It does not prove acceptance
by a generic JSON-LD processor, RO-Crate validator or independent importer.

The code itself correctly states these limits, rejects unhandled fields instead
of silently dropping them, records extension-unaware loss paths, and marks the
external validator and independent consumer as untested. Keep those distinctions
in the manuscript and response letter. A standards-targeted transport demonstration
is supportable; comprehensive standard conformance or broad interoperability is
not established by exporter/importer self-consistency. Additional validation
conducted after this inspection should be named with its exact version and scope.
