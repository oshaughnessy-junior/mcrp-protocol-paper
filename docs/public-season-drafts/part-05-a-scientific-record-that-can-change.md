---
artifact_role: outward-facing-blog-draft
authors: [Codex, junior]
status: mature-private-draft
date: 2026-08-23
series: Making Computational Review Version-Specific
series_part: 5
publication_status: private-not-approved
audience:
  - research-infrastructure architects
  - repositories and review networks
  - dependency-monitoring teams
  - editors and open-review platforms
reader_utility: propagate corrections and preserve scoped disagreement without rewriting history or automating scientific authority
operational_artifact: five-step living-record loop and disagreement timeline
evidence_status: event-network proposal grounded in notification and transparency standards; convergence and utility untested
source_drafts: [part-08-living-scientific-network, part-10-disagreement-is-a-scientific-product]
future_cross_list_slot: internal web/iOS MCRP protocol prototype; unscheduled and not evidence for this post
---

# A scientific record that can change without rewriting history

_Making Computational Review Version-Specific, 5 of 6_  
_By Codex and junior_

A corrected dataset can be public and still remain disconnected from every downstream claim that used it.

The correction may live on a provider page. The paper may keep its original badge. An editor, reader, or laboratory must rediscover the dependency, infer which results are affected, and decide whether the old review still applies. At scale, that is not a document problem. It is an event-routing problem.

MCRP proposes a living scientific record built from append-only events and recomputed views. Releases, dependencies, observations, reviews, challenges, corrections, and decisions retain stable identities. New events can trigger bounded follow-up work without rewriting what earlier actors knew or decided.

“Self-updating” has a strict boundary here. Records, indexes, notifications, dependency matches, and policy projections may update automatically. Scientific acceptance, rejection, narrowing, withdrawal, or adjudication remains an attributable human act under an explicit policy.

## Operational artifact: the five-step living-record loop

```text
1. PUBLISH
   Emit a signed event for an exact release, correction, review, or challenge.

2. DETECT
   Resolve identifiers, verify envelopes, and match changed dependencies
   to potentially affected claims. Emit impact candidates, not verdicts.

3. ROUTE
   Notify subscribers and open bounded work for execution, methods,
   custody, domain, or adjudication review.

4. DECIDE
   Agents produce observations and reports. Qualified humans record
   scoped scientific dispositions where authority is required.

5. PROPAGATE
   Append the new decision or challenge as another event. Recompute
   policy-specific views while preserving prior records and disagreement.
```

A useful implementation must make these operations incremental and idempotent: receiving an event twice cannot create two authoritative decisions. Nodes should expose the event snapshot, policy, trust roots, and completeness boundary behind any displayed state.

## Worked example: a correction during a partition

Release `R17` reports a measured amplitude of 4.2 units and declares calibration dataset `C5` as a dependency. The calibration provider publishes successor `C6`, reporting an incorrect transfer coefficient in one frequency band.

A registry records the correction. A dependency monitor finds the explicit `R17 → C5` reference and emits an impact candidate limited to the affected band. Under acceptance conditions `A3`, a policy evaluator displays `pending review`; it does not declare the claim false.

An authorized execution agent reruns the analysis with `C6`. The result changes from 4.2 to 3.8 units, while a control band remains unchanged. The agent reports the outputs, environment, and one missing auxiliary file. A calibration reviewer examines the correction and rerun, then decides that the numerical claim must be revised while the method need not be withdrawn. When the authors publish `R18`, the old claim is recorded as superseded.

Now suppose Registry East received the correction before Registry West. East shows `pending review`. West should not present its older state as globally current. It can say `current at checkpoint E870` and expose its completeness boundary. After connectivity returns, West receives the correction, reports, and disposition, then recomputes its view.

That is recovery from a shared event set. It is not proof of universal convergence, scientific truth, or correct governance.

## Disagreement must survive the update

Consensus helps institutions decide, but it is a destructive storage format for scientific disagreement. “Two reviewers for, one against” discards what each reviewer examined, which assumptions held, and whether access was limited.

The record should preserve typed relations such as:

- `supports` within a named scope;
- `bounds` or narrows a claim;
- `contradicts` using named counterevidence;
- `fails-to-reproduce` after a specified attempt;
- `unassessed` because evidence or expertise was unavailable;
- `supersedes`, `withdraws`, or `revokes` a prior object or decision.

These relations are not votes. A failed reproduction under incomplete access is not automatically a contradiction. A later adjudication can settle what one community will do without deleting the dissent.

### A compact disagreement timeline

Suppose claim `C17-v3` says treatment T reduces a twelve-month event rate by at least 10% for adults with condition X.

1. Reviewer A reports support for the aggregate population after examining controlled data.
2. Reviewer B identifies systematic measurement rounding for participants over 70 and issues a bounded challenge.
3. Reviewer C lacks access to the protected records and records `unassessed`, not `fails-to-reproduce`.
4. The authors publish `C17-v4`, narrowing the age range and leaving the older subgroup unresolved.
5. A qualified adjudicator upholds B’s challenge in scope. A’s aggregate finding and C’s access limitation remain visible.
6. Different communities recompute different policy views from the same events, each naming its rules.

Automation can route the challenge, update indexes, and project how a named policy treats the event. It cannot silently convert B’s challenge into scientific rejection or C’s access limitation into negative evidence.

## What is established, proposed, and evidenced

**Established prior art.** Decentralized event and notification patterns already exist in [Linked Data Notifications](https://www.w3.org/TR/ldn/), [Activity Streams 2.0](https://www.w3.org/TR/activitystreams-core/), [WebSub](https://www.w3.org/TR/websub/), and [COAR Notify](https://coar-notify.net/specification/1.0.1/). [SCITT RFC 9943](https://www.rfc-editor.org/rfc/rfc9943.html) supplies relevant transparency-service concepts. [Nanopublications](https://nanopub.net/) and [Trusty URIs](https://trustyuri.net/) show granular, content-addressed assertions. MCRP does not claim originality for these components.

**MCRP proposal.** The proposed integration connects those mechanisms to exact scientific releases, typed disagreement, dependency-sensitive freshness, bounded work routing, and human-authorized dispositions.

**Current evidence.** The architecture has not demonstrated lossless federation, reliable operation under partitions, accurate dependency impact, manageable human workload, or improved correction uptake. The examples above specify desired behavior.

## What remains open

A dependency graph is only as complete as its declarations. Restricted evidence and ambiguous identifiers can leave impact unknown. Automated monitors may create more review candidates than humans can assess. Transparency can expose sensitive relationships. Moderation can suppress legitimate dissent or fail to contain harassment. Different nodes may see different events indefinitely.

Interfaces must therefore expose `unknown`, `stale`, `unassessed`, and `pending convergence` rather than manufacturing certainty. Confidential challenges may require accountable pseudonymity, selective disclosure, and an appeal process. Those are governance choices, not consequences of content addressing.

The near-term test is deliberately small: can two independently governed systems exchange one correction, one scoped challenge, and one human disposition while preserving the targets, types, history, and policy differences? A future prototype may help exercise that question, but no prototype result is claimed here and its timeline is separate from this publication sequence.

The final post asks how this trust layer could fail—and which experiments and stop conditions should determine whether it deserves to grow.

