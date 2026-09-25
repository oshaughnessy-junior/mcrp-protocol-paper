# Final internal red review: crosswalk and amendment semantics

Scope: integrated Sections 8.1 and 5.5, their executable fixtures, and
`response-to-review-1587.md`. Same author-directed team; this is not external
scientific or standards validation. Main manuscript and rendered artifacts were
not edited by this reviewer.

**Disposition: no substantive remaining blocker.**

- Section 8.1 correctly limits the result to a closed supported source subset,
  names the experimental namespace, distinguishes standard metadata from MCRP
  extension meaning, and excludes general RDF serialization handling, complete
  standards conformance, and independent-consumer interoperability.
- It accurately reports nine entities and fourteen named tests. All fourteen
  tests passed again. Listed artifact payload bytes receive the SHA-256/size check;
  the local profile description is only existence-checked. The text does not claim
  whole-crate integrity or approval authority from those operations.
- Reconstructing/reexporting and comparing entity maps matches the implemented
  strict importer. Unknown data and missing critical extensions are rejected;
  entity-list order may change without losing supported fields. The explicit
  destructive-consumer projection reports information loss rather than defaulting
  missing policy fields to success.
- Independently instantiated the main-text graph x -> e -> c and y -> d in the
  revision-semantics model. Changing x marks c affected and leaves d outside
  declared reachability. d remains ineligible without a scope-delta disposition,
  and becomes eligible with the bound disposition and current old approval.
  This agrees with Section 5.5, including its distinction between eligibility
  and an actual carry-forward act.
- Changed claim contracts, missing edges and expired/withdrawn approval are
  correctly distinguished from scientific falsity. The main example does not
  imply hidden dependencies become detectable.
- Checked the **downloaded version 1.1 PDF**, not merely its source: Appendix A.1
  starts on page 9, A.2 on page 10, A.3 on page 11, and A.4 begins on page 11 and
  continues onto page 12. The response's page references are accurate. Describing
  the new main-text example as clearer signposting, rather than claiming the
  appendix was absent, is appropriate.

**Minor consistency suggestion sent to integrator:** Table 1's inherited RO-Crate
row still says “round-trip compatibility remains unimplemented.” Qualify this as
broader or independent compatibility and reference the bounded Section 8.1
self-roundtrip, so the table cannot be mistaken as denying the new demonstration.
This does not change a result or introduce a scientific publication blocker.

Public resolution of source-tagged links and final rendered equation/table layout
remain release checks for the integrator. This review makes no claim about those
external publication states.
