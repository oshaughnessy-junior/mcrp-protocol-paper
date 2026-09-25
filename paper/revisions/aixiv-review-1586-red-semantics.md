# Collective red review: revision semantics and acceptance boundaries

25 September 2026. Internal author-directed review, not an independent scientific
review. Inspected the integrated `paper/position-paper.md`, semantics source note,
new executable example, design response draft, and evidence red report. Findings
were shared with the design and evidence agents and root integrator.

## Findings and final dispositions

**RS-1: Historical approval could be recycled after expiry or revocation.** The
initial Appendix A predicate required `Approved`, but that meant only a recorded
historical disposition. An old approval could pass carry eligibility on unchanged
objects when the caller omitted an expiry/revocation event root. Corrected in the
semantics source and implementation with `Current(d,t,p)`: exact policy match,
issued-at <= assessment time < expires-at, no effective known revocation, and no
pending or disputed status. Missing assessment time or policy fails closed. The
new test exercises exclusive expiry, future issuance, changed policy, known
revocation before/after the decision time, pending and disputed status. This is an
explicit computation over supplied clock/status evidence, not an asserted
`trusted_current` Boolean. Undiscovered status events and clock authenticity
remain external limitations. **Resolved: source, model, and integrated Appendix A now agree.**

**RS-2: A changed material-claim inventory was not explicitly dirty.** Retiring a
claim while retaining the object bytes need not change its version token in the
initial toy. Adding C symmetric-difference C' to dirty roots prevents its scope
change disappearing from impact reporting. The source definition, implementation,
and a regression test now agree. Direct carry-forward already rejected a claim
absent from the new inventory. **Resolved: source, model, and integrated Appendix A now agree.**

**RS-3: Appendix/code version mismatch.** The first integrated appendix said 14
new tests; it lacked the later membership and currentness fixes. The final source
now has **16 named tests**, all passing, and includes these stronger predicates.
Keep this count separate from the twenty publicly rerun domain tests and the
withdrawn historical thirteen-test assertion. **Resolved: integrated Appendix A states sixteen and contains both fixes.**

**RS-4: Mandatory authority and exemption ambiguity.** Agreed with collective
review: Section 6's explicit S1 list must include external admission/authority.
An open exemption mechanism must not let a policy waive material-claim mapping,
provenance paths, tests, or negative controls while awarding minimum conformance.
Use a closed, specifically justified N/A list and retain all S1/S2 gates; scientific
challenge and freshness remain mandatory at S3. Also define zero as disclosure or
pending status, not an acceptance transition with an empty predicate set. These
main-manuscript fixes are now integrated: S1/S2 predicates are non-exemptible; S3
exceptions are confined to specifically justified subcases; zero explicitly does
not authorize scientific acceptance. **Resolved.**

**RS-5: Early graph-completeness claim.** Agreed with evidence review: Section 4
must say all *declared reachable* affected outputs/claims, not every actual
scientifically affected object. The executable hidden-lineage counterexample is
valuable because it demonstrates that the graph can miss a real impact even when
the local predicate passes. It and its interpretation are preserved, and Section 4 now qualifies reachability
to declared propagating dependencies. **Resolved.**

## Checks and boundaries that hold

- Forward edge direction is fixed; computational derivation is acyclic, while
  review-dependency cycles are handled by a least fixed point.
- Reachability uses old/new edge union and changed-edge targets. Deleting lineage
  cannot erase its historical route. Conservative cross-version paths are admitted
  as overapproximation rather than misrepresented as minimal rework.
- Independent finite path enumeration checks all 512 directed graphs on three
  vertices against closure, including self-loops and cycles.
- Unchanged-claim mapping, exact contract identity, prior bound approval,
  currentness, graph non-impact, and separately authorized scope-delta disposition
  are distinct necessary conditions; none alone suffices.
- The toy computes eligibility but does not issue a carry-forward record, check
  artifact hashes, authenticate authorities, discover materiality or missing
  dependencies, perform scientific execution, or certify truth.
- An affected node receives `needs-reassessment`, while immutable historical
  snapshots remain available. It never receives a scientific false verdict.
- New revision tests are explicitly author-side internal fixtures, distinct from
  historical v0.1.2 evidence and independent scientific replication.

## Recheck instructions

After syncing Appendix A, run:

```sh
python3 -m unittest discover -s examples/revision-semantics -v
python3 examples/revision-semantics/semantics.py
```

Then verify that the rendered appendix includes `Current(d,t,p)`, the material-claim
symmetric difference, and the correct count of sixteen new tests. Verify the
mandatory S1/S2 inventory and zero-level non-acceptance semantics in Section 6.
Public readers also need source-pinned links to the evidence inventory and these
new examples; repository-relative prose alone is not a resolvable supplement.

## Final verification

Re-read the integrated manuscript after all corrections. `Current` and `Eligible`
were reformatted using aligned equations without changing their logical conjuncts.
The material-claim symmetric difference remains in the dirty-root definition.
All sixteen executable tests passed again, including expiry/policy/revocation and
retired-claim tests. S1 explicitly includes separately authorized external admission;
all S1/S2 predicates are mandatory; MCRP-0 cannot constitute scientific acceptance;
and graph impact is qualified to declared reachability. Source-tagged evidence
and example links are now present. No remaining semantic publication blocker was
found. Public resolution of the new tag URLs and rendered-page visual quality
remain release checks owned by the integrator, not claims established by this
source-level review.
