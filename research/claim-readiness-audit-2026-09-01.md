---
artifact_id: evidence:science-writer:mcrp-claim-readiness-2026-09-01
artifact_type: evidence
agent: science-writer
activity: activities/2026-06-01-ScienceWriterTraining
issue: 9
parent: paper/position-paper.md
session: cron:3ebaecd5-eb97-418e-bb77-f51909603ccc
status: done
updated: 2026-09-01T14:05:00-04:00
---

# MCRP position-paper claim-readiness audit

## Scope and disposition

This close read compares `paper/position-paper.md` at `ff49fc3` with
`research/novelty-claim-ledger.md`, `research/closest-work-matrix.md`,
`protocol/prospective-lifecycle-v0.2-draft.md`, and the repository's existing
adjudication records. It does not re-review the entire literature or authorize
publication.

**Disposition:** the manuscript is reviewable as a bounded technical
supplement and is unusually explicit about its limitations. It is not ready to
support a scholarly novelty claim, a conformance claim, or a claim of improved
review outcomes. The closest-work matrix leaves only a conditional design
hypothesis: a prospective, externally enforced, claim-versioned lifecycle with
scoped decisions and dependency-sensitive staleness. That hypothesis remains
unvalidated.

## Claim-level findings

| ID | Location | Claim or claim block | Support and novelty assessment | Logic gap | Action |
|---|---|---|---|---|---|
| CR-01 | lines 5, 13--17 | Conventional publication materials do not by themselves expose all claim-to-execution, transformation, trust, and judgment links. | The cited standards and review systems support the narrower point that their scopes are partial and distinct. The universal wording at line 5 is stronger than the local evidence packet. | Absence of a required field from a standard does not prove that an individual repository never records it. | **Narrow** to “do not necessarily” or “may not,” and retain the scoped prior-art citations. |
| CR-02 | lines 7, 19 | MCRP uses versioned review objects, externally enforced verification, and re-establishment after material change. | Supported as a design in `prospective-lifecycle-v0.2-draft.md`. Novelty ledger N-03, N-04, N-07, and N-09 are conditional. No external controller or independent exercise is present here. | The prose shifts from “we propose” to present-tense behavior, which can read as implemented conformance. | **Narrow** to “Under the proposed protocol…” and “would require…” until external enforcement is exercised. |
| CR-03 | lines 9, 101--103 | Version 0.1.2 passed schema, replay, adversarial, unit, scientific-check, and corruption fixtures. | The paper labels the detailed counts author-reported, but this repository contains no itemized mapping from the counts to named fixtures, commands, logs, or an exact implementation digest. | The abstract omits the “author-reported” qualifier that appears at line 103. A reader cannot independently audit the result from this repository. | **Source or narrow.** Add a versioned validation record and exact implementation/fixture identity, or say “author-reported fixture checks.” |
| CR-04 | lines 25--33 | Claim/evidence graphs, provenance, workflow packaging, external execution, agent provenance, and staged agent-native review are prior art. | Strongly supported by the closest-work matrix and novelty ledger N-01, N-02, N-05, N-06, and N-08. All 14 DOI/arXiv identifiers extracted from `refs.bib` passed deterministic identity verification in this audit. | Source identity is verified; this turn relied on the existing 2026-08-16 matrix for semantic source locators rather than re-reading every primary source. | **Keep.** This is the manuscript's strongest and most important novelty boundary. |
| CR-05 | line 35 | The residual MCRP proposal is a prospective, externally enforced, claim-versioned lifecycle. | This accurately matches the matrix's **CONDITIONAL** gate and does not claim priority. Paper-replication, EVI, FAIRSCAPE, PROV-AGENT, RO-Crate, and Traxia leave little room for a broad systems claim. | A residual gap is not itself novelty; it becomes a contribution only after a precise semantic delta and evidence show that the delta matters. | **Keep as a design hypothesis.** Do not call it novel or first without a direct feature/behavior comparison and evaluation. |
| CR-06 | lines 45--53 | The SRR has required fields, typed evidence relations, bidirectional traversal, and blocking semantics. | Supported as normative protocol content, not as a calibrated common profile. The manuscript correctly disclaims graph novelty and cross-domain sufficiency. | “Must” statements define the proposal; they do not show that the fields are sufficient, usable, or interoperable. | **Keep**, with the existing proposed-profile caveat. Link a future machine-readable schema and conformance suite before stronger wording. |
| CR-07 | lines 57--75 | Verification authority is distinct from author production; a non-author verifier runs the workflow; scientific disposition remains human. | Supported as policy design and by the manuscript's role separation. The novelty matrix treats independent enforcement and role-scoped authorization as conditional. | Separately recorded authority is not necessarily independent authority. Line 71 acknowledges that a new model/session is insufficient, but independence criteria remain undefined. | **Frame as a requirement, not an achieved property.** Define operational independence criteria and test them in at least one real review setting. |
| CR-08 | lines 79--85 | Material revisions invalidate affected decisions; freshness failures append scoped states without rewriting history. | Supported by the v0.2 protocol draft and novelty ledger N-07/N-09 as intended semantics. No authoritative controller, closure proof, mutation suite, or false-staleness analysis is supplied. | The manuscript sometimes describes automatic behavior that has not been implemented or independently exercised. | **Narrow to proposed semantics** until mutation-driven invalidation and carry-forward tests exist. |
| CR-09 | lines 89--97 | MCRP assurance levels, the `RRP[C,D,P,X,H,A]` profile, and full/slice/checkpoint/witness modes provide a claim-scoped disclosure taxonomy. | The manuscript appropriately says these are proposed, uncalibrated disclosure fields. However, the novelty ledger does not explicitly classify the taxonomy, while ACM artifact levels and Traxia tiered review create adjacent overlap. | Contribution lists can make the taxonomy sound original even though no novelty comparison or reviewer-comprehension evidence exists. | **Add a ledger row** classifying the taxonomy as supporting/design-only unless a dedicated closest-work comparison establishes a residual contribution. |
| CR-10 | lines 107--111 | MCRP should profile existing standards and can be adopted incrementally. | This is a well-supported recommendation and aligns with novelty ledger N-12. No actual crosswalk or round-trip result exists. | Standards-compatible design intent is not demonstrated interoperability. | **Keep “should.”** Reserve “compatible/interoperable” for valid profiles and round-trip tests against independent implementations. |
| CR-11 | lines 115--121 | MCRP remains untested on real workflows, independent reconstruction, human review, cross-domain calibration, cost, and change recovery. | Directly supported by repository state and the evaluation agenda. | None; these limitations correctly prevent inference from synthetic fixtures to scientific utility. | **Keep.** These caveats are readiness gates, not optional future-work polish. |
| CR-12 | lines 125--127 | Future scholarly reconsideration should follow archived protocol, independent review, interoperability tests, and real-workflow comparison. | Fully consistent with the novelty ledger's five-part required package and the closest-work matrix. | The conclusion omits the need for an exact public validation map for the existing synthetic claims. | **Keep and add** the itemized validation artifact to the near-term gate list. |

## Novelty-overlap synthesis

- **Occupied territory:** claim/evidence graphs; immutable atomic claims;
  provenance and agent-action capture; workflow-run packaging; signatures and
  identities; staged review; external execution; claim-to-run-to-report paths;
  and paper/artifact-level human approval.
- **Conditional residual:** prospective acceptance predicates fixed before a
  claim-bearing run; authoritative transitions outside the generating
  process; attestations bound to claim, contract, evidence, release, role, and
  decision; and dependency-sensitive staleness/revocation with conservative
  carry-forward.
- **Not yet established:** that the residual semantics cannot be expressed by
  EVI/PROV plus policy; that they are implemented end to end; that they reduce
  unsupported completion or stale approval; or that reviewers can use the
  assurance/resource taxonomy consistently.

## Required framing changes

1. In the abstract, change present-tense enforcement claims to explicit design
   language and label the fixture result “author-reported” unless an exact
   public validation map is added.
2. Treat the line-35 residual as a **design hypothesis**, not as novelty
   established by subtraction from prior art.
3. Use normative language (“MCRP requires,” “the controller would mark”) for
   unimplemented lifecycle semantics, and reserve descriptive present tense
   for artifacts actually exercised in the named version.
4. Classify assurance levels, resource axes, and assessment modes in the
   novelty ledger; do not let a contribution list imply originality by silence.
5. Keep “standards-compatible” as an objective until profiles, validators, and
   round-trip tests exist.

## Unresolved evidence needs

1. A public, versioned validation record mapping the four claims, nine checks,
   thirteen tests, and eleven corruptions to exact fixture names, commands,
   logs, expected outcomes, implementation revision, and artifact digests.
2. Frozen machine-readable claim, state, transition, attestation, and
   invalidation schemas with fail-closed conformance tests.
3. An external validator exercised outside the generating agent's authority
   boundary, with replay, revocation, interruption/resumption, mutation, and
   false-completion fixtures.
4. Formal crosswalks and round-trip tests for PROV-O, Workflow Run RO-Crate,
   and a claim representation such as EVI, Micropublications, or
   Nanopublications.
5. A direct comparison with Paper-replication and Traxia on prospective
   acceptance, scope-bound authorization, mutation-driven invalidation, and
   stale-claim handling.
6. At least one independently reviewed real scientific workflow and a
   preregistered comparison against repository-plus-instructions and
   provenance-only baselines, including reviewer effort and adverse outcomes.

## Verification record

- Branch baseline: `ff49fc3ce63f34914005d0f499afeaeaaf1db26e`.
- Manuscript citations: 17 unique citation keys; every key is present in
  `paper/refs.bib`.
- Deterministic identity check: 14 DOI/arXiv identifiers extracted from
  `paper/refs.bib`; 14 verified, 0 mismatches, 0 not found, 0 errors.
- Claim-support boundary: prior-art support decisions use the repository's
  closest-work matrix, which records primary/official sources verified on
  2026-08-16. The validation-count claim remains blocked because the repository
  lacks an itemized public evidence map.
- No manuscript prose, bibliography, protocol, implementation, result, or
  publication surface was changed by this audit.
