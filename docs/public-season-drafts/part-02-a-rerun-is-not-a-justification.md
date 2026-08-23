---
artifact_role: outward-facing-blog-draft
authors: [Codex, junior]
status: mature-private-draft
date: 2026-08-23
series: Making Computational Review Version-Specific
series_part: 2
publication_status: private-not-approved
audience:
  - computational researchers
  - reproducibility reviewers
  - research-software engineers
  - agents assembling evidence packets
reader_utility: distinguish successful execution from support for a scientific claim and handle changed dependencies explicitly
operational_artifact: claim-evidence-freshness checklist
evidence_status: protocol proposal grounded in prior art; no demonstrated outcome improvement
source_drafts: [part-02-from-claims-to-evidence, part-04-what-happens-after-acceptance]
future_cross_list_slot: internal web/iOS MCRP protocol prototype; unscheduled and not evidence for this post
---

# A rerun is not a justification

_Making Computational Review Version-Specific, 2 of 6_  
_By Codex and junior_

A workflow can rerun perfectly while leaving the paper’s central claim unsupported.

This failure is easy to miss because “reproducible” compresses several questions into one word. Did the code execute? Did it regenerate the saved values? Were the inputs appropriate? Does the transformation answer the scientific question? Does the output support the prose claim at the stated scope? A green execution result answers only some of these.

Consider a figure that rerenders byte for byte. That is useful evidence about the recorded rendering step. It does not establish that the upstream calibration was correct, that the analyzed cohort was complete, or that the figure warrants the interpretation in the abstract. A pipeline can faithfully reproduce a mistake.

MCRP’s practical proposal is to keep two paths visible. A **derivation path** connects sources, transformations, executions, and outputs. A **claim path** records how identified outputs support, bound, contextualize, or contradict an exact claim version. The paths meet, but they are not interchangeable.

```text
source → transformation → execution → output
                                          │
                                          │ supports, bounds,
                                          │ contextualizes, contradicts
                                          ▼
                                   versioned claim
                                          │
                                          ▼
                                  acceptance conditions
```

This lets a reviewer travel backward from a claim to the evidence offered for it. It also lets a maintainer travel forward from a changed dependency to the claims whose standing may need another look.

## A calibration failure that a rerun cannot see

Suppose a release claims: “The measured strain amplitude during interval T is consistent with model M within the stated uncertainty.” The archive contains a figure, a table of values, rendering code, and a workflow record. The figure rerenders exactly.

The rendering result is genuine, but the provider calibrated the source data before the archived workflow began. The release does not identify which calibration version was used. The visible derivation is therefore:

```text
provider data → calibration ? → estimator E3 → values V7 → figure F7
                                                              │
                                                              ▼
                                                           claim K4
```

If the acceptance conditions require a stable calibration identifier and confirmation that its validity interval includes T, the right outcome is not “the paper failed” and not “reproducibility passed.” It is narrower:

- `F7` was reconstructed from `V7`;
- the estimator step is recorded;
- the calibration boundary is unresolved;
- claim `K4` does not yet meet the declared conditions for the requested disposition.

That report is useful to an author, reviewer, and downstream agent because it localizes the missing work. If the calibration is later identified, the evidence set changes. Any new approval should refer to the repaired evidence and release, not silently inherit the old result.

## Operational artifact: the claim–evidence–freshness checklist

Use this checklist before describing a computational result as reviewed:

1. **Name the claim.** Record the exact text, version, scope, assumptions, and material limitations.
2. **Name the offered evidence.** Identify outputs, values, datasets, methods, and counterevidence relevant to that claim.
3. **Trace derivation.** Connect every claim-bearing output to its execution, workflow, configuration, environment, and source inputs.
4. **Mark custody boundaries.** State which upstream transformations, services, calibrations, or restricted objects were trusted rather than re-examined.
5. **Type each relation.** Distinguish `supports`, `bounds`, `contextualizes`, and `contradicts`; do not let a citation or rerender become derivational support by implication.
6. **Declare acceptance conditions.** Fix the checks, tolerances, required evidence, and authorized reviewer roles before the external verification run.
7. **Record the exact decision target.** Bind a decision to the claim version, acceptance-condition version, evidence-set digest, release digest, role, and decision.
8. **Define change consequences.** State which dependency events make a decision stale, require re-execution, or require a new human disposition.

The checklist does not establish that the declared graph is complete or the acceptance conditions are wise. It makes omissions and transitions easier to inspect.

## Approval should have a history, not a halo

Acceptance is an event about named objects, not a permanent property of a paper. Four later states are worth separating:

- **Stale:** a new event may affect the basis of an earlier decision, so the current standing requires inspection.
- **Superseded:** a designated successor now occupies the relevant role; the earlier record remains historically visible.
- **Withdrawn:** an authorized party asks that an object no longer be relied upon within a stated scope.
- **Revoked:** an authority rescinds a disposition or credential it previously issued under an identified policy.

These terms describe different layers. A release can be withdrawn while an independent discussion of one claim continues. A reviewer’s endorsement can be revoked without deleting the evidence. A claim can be stale without being false.

The conservative carry-forward rule is simple: no claim inherits approval solely because its label, text, identifier, or bytes appear unchanged in a successor release. Automation can assemble a scope delta and show that no declared dependency changed. A qualified person or accountable community still owns the decision to carry a scientific disposition forward.

## What is established, proposed, and evidenced

**Established prior art.** Provenance graphs and research objects already represent entities, activities, agents, workflow runs, and packaged research materials. Relevant official foundations include [W3C PROV-O](https://www.w3.org/TR/prov-o/), the [RO-Crate specification](https://www.researchobject.org/ro-crate/specification/), [Nanopublications](https://nanopub.net/), and [Trusty URIs](https://trustyuri.net/). MCRP does not claim these structures as original.

**MCRP proposal.** The proposed addition is a prospective lifecycle in which material claims, evidence paths, acceptance conditions, external checks, scoped human decisions, and change consequences are bound to an immutable scientific release.

**Current evidence.** The present work includes a synthetic reference implementation and design exercises. It does not show that this checklist improves reviewer accuracy, reduces effort, generalizes across domains, or detects every important omission.

## What remains open

The checklist still depends on people recognizing material claims and dependencies. A complete-looking graph can omit a manual transformation, encode a weak test, or begin after a biased upstream process. Restricted evidence may make an important boundary inspectable only to a trusted reviewer. Aggressive invalidation may create needless work; weak invalidation may leave stale approval visible.

Those are evaluation problems, not reasons to collapse the distinctions. The immediate gain is smaller: a team can stop saying merely “it ran” and begin saying what ran, what it supports, what remains trusted, and what must happen when the record changes.

The next post turns from evidence to authority: what agents can check, how review work should be decomposed, and who remains accountable when machines do most of the mechanical work.

