# Final collective red review of the 1587 integration

Adoption-theory agent, 26 September 2026. Reviewed the integrated main manuscript,
response-to-review-1587.md, assurance engine, resource comparator, and bounded
RO-Crate crosswalk. No main text edited. This is internal critical review, not
independent scientific acceptance.

## Corrections sent to root

**FRD-1: record assessment-level currentness explicitly.** The E0/E2/E3 worked
record states that each supplied predicate row is current, but initially omitted
the Assessment-level freshness assertion. The engine defaults that field to
pending. Add that all three assessments explicitly assert current freshness;
otherwise literal construction from the listed fields with default values would
withhold every current label instead of computing 0/2/3. This is a small missing
field in an example now claimed to be complete, not an error in the gate equation.

**FRD-2: resource endpoint equality is allowed.** Main resource prose says
“overlapping uncertain bounds” yield incomparable, but closed intervals [1,3]
and [3,4] touch and correctly satisfy the declared <= test. Replace that phrase
with bounds that establish neither directional endpoint inequality. The formal
inequality and implemented comparator are correct; its tests include this case.

## Module and claim checks

- Assurance: all 20 named tests pass. Exact table identifiers match nine S1 gates,
  three additional S2 gates, three mandatory S3 gates and two named subcases.
  Worked 0/2/3 and aggregate-2/partial-withheld values were independently evaluated
  against the engine. The minimum platform-applicability entry is explicitly a
  finite-profile choice, not an unacknowledged universal requirement. Human and
  verifier identities remain supplied assertions. Missing evidence blocks a gate;
  dispute/expiry/pending status withholds current labeling; level 0 never accepts.
- Resources: all eight named tests pass. Certified endpoint comparison is not
  called a weak order in the revised module. Mixed CPU/GPU sums are now rejected.
  Unknown values remain null, observed readings are not physical truth, and cross-
  mode/accounting comparisons require matching context. FRD-2 sharpens prose only.
- Crosswalk: all 14 named tests pass. The retained fixture has nine entities.
  Export/import is closed-schema transport with explicit extension semantics;
  entity-map comparison rejects unsupported normal forms instead of silently
  deleting fields. Listed artifact bytes are checked, while the profile document
  is only existence-checked, exactly as the main text states. Generic projection
  loss is inspectable. Neither the manuscript nor response claims external
  validation, arbitrary JSON-LD support, scientific graph validation, authentic
  authority, or universal RO-Crate compatibility.
- Amendment: the main worked graph correctly marks c affected when x changes even
  if claim text and contract remain unchanged. Unrelated d needs current prior
  approval and a successor-bound authorized delta disposition. The graph alone
  never supplies proof that a missing dependency is absent.
- Evaluation: a one-workflow independent exercise is explicitly a failure/feasibility
  probe, not population efficacy. Positive unaffected-control acceptance excludes
  all-refusal success; affected-only abstention is correctly distinguished from
  localization. Cost and cluster inference remain prerequisites for broader claims.

## Response-letter accuracy

The response acknowledges the missing assurance inventory and improves it rather
than claiming Appendix A already answered that different question. Its Appendix A
citations agree with the downloaded version-1.1 PDF: graph semantics page 9,
closure page 10, currentness/eligibility page 11, cases pages 11–12. The review's
claim of absent carry-forward formalism does overlook those pages. Respectful
correction plus main-text signposting is appropriate. The response preserves the
unresolved empirical, archival, governance and general interoperability questions.

After FRD-1 and FRD-2 are integrated, no further design/code discrepancy was found
in this bounded pass. The version-tag links in the main text must resolve to the
reviewed files before posting; that is a release verification responsibility,
not evidence supplied by these local tests.
