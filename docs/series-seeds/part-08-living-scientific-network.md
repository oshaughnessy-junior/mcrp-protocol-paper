---
artifact_role: outward-facing-blog-seed
authors: [Codex, junior]
status: mature-private-draft
date: 2026-08-21
series_part: 8
publication_status: private-not-approved
---

# A scientific network that keeps updating

Publication should add a version to the network, not freeze the network’s understanding of it.

Today, a corrected dataset or withdrawn method may be discoverable yet remain disconnected from the downstream claims that used it. Every reader, lab, and editor must reconstruct the impact manually. MCRP proposes a living, self-updating event network in which releases, dependencies, reviews, challenges, and corrections are machine-addressable enough for new events to trigger bounded follow-up work. “Self-updating” applies to records, indexes, and policy projections—not to scientific authority.

This proposal builds on established prior art rather than claiming these mechanisms as MCRP inventions. [W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model-2.0/) describes credential and proof structures; [SCITT RFC 9943](https://www.rfc-editor.org/rfc/rfc9943.html) specifies transparency services for signed statements; [Linked Data Notifications](https://www.w3.org/TR/ldn/), [Activity Streams](https://www.w3.org/TR/activitystreams-core/), [WebSub](https://www.w3.org/TR/websub/), and [COAR Notify](https://coar-notify.net/specification/1.0.1/) provide relevant notification patterns. [Nanopublications](https://nanopub.net/) and [Trusty URIs](https://trustyuri.net/) demonstrate approaches to small assertions and content-addressable references. COAR’s [publish-review-curate](https://coar-repositories.org/what-we-do/repositories-and-publishing/) model is also guiding prior art. MCRP’s work is to propose how such ideas might be combined under explicit scientific-governance constraints.

## The proposed nine-step event loop

The proposed federation protocol would advertise a capability vector for each participant: which event types it can emit or consume, identifier schemes it resolves, verification methods it supports, policies it can project, computations it can execute, confidentiality classes it can handle, and human decisions it is authorized to record. That vector describes operational capability, not scientific credibility.

1. **Publish.** A source emits a signed, stably identified event for a new release, correction, retraction, or review. Its advertised capability must include the event type, identifier method, and signing method.

2. **Register.** A registry verifies the envelope, records its receipt, and indexes declared relationships. This requires signature-verification and indexing capabilities; it does not endorse the contents.

3. **Notify.** A transparency or notification service sends the event to declared subscribers using its supported delivery protocols and confidentiality class.

4. **Match.** A dependency monitor compares declared references against the new event and emits scoped impact candidates. Its capability vector must identify the relationship types it can traverse. A match is an automated observation, not a scientific disposition.

5. **Project policy.** A policy evaluator computes administrative states such as `pending-review`, `stale-under-policy-v3`, or `unknown`. It must name the policy version it implements. This projection neither approves nor rejects a claim.

6. **Route work.** A routing service opens bounded review requests for eligible reviewers or agents. Its capabilities must cover the required subject scope, confidentiality class, and jurisdictional constraints.

7. **Recompute.** Authorized agents resolve named inputs, reconstruct declared environments, rerun permitted checks, and produce signed reports. Their vectors must state supported environments, evidence access, and execution limits. Agent reports remain evidence proposals.

8. **Decide.** A qualified human reviews the evidence and records a scoped disposition. Where the decision is attested, its binding is exactly `(claim version, acceptance-contract version, evidence-set digest, release digest, role, decision)`. Automation may check that this tuple is complete, but may not choose the decision.

9. **Propagate.** The signed human decision becomes another event. Registries update projections and notify downstream subscribers, beginning another bounded loop without rewriting historical records.

## Worked example: calibration update during a partition

Suppose release `R17` claims a measured amplitude of 4.2 units and declares dependency on calibration dataset `C5`. The calibration provider publishes successor `C6`, stating that one frequency band in `C5` used an incorrect transfer coefficient. A registry accepts the signed correction event and assigns receipt `E900`. A dependency monitor finds the explicit `R17 → C5` reference and emits impact candidate `I31`, limited to the affected band.

A policy evaluator using acceptance contract `A3` projects the relevant claim as `pending-review`; it does not mark the claim false. A router creates work item `W44`. An authorized execution agent reruns the declared analysis with `C6`, producing release digest `D6`. The output changes from 4.2 to 3.8 units, while an independent control band remains unchanged. The agent reports those observations, its environment digest, and one missing auxiliary file. It does not recommend acceptance.

A qualified calibration reviewer examines the correction, rerun, missing file, and contract. The reviewer decides that the numerical claim must be revised but that the method need not be withdrawn. The signed disposition binds the relevant versions, evidence digest, release digest, reviewer role, and decision. Registries then project `R17` as `superseded-by-R18` once the authors publish the revision. Historical views still show what was known at each named snapshot.

Now add a network partition. During the review, Registry East receives `E900`, but Registry West does not. East shows `pending-review`; West still shows `current-at-snapshot-E870`. Neither may claim a globally current state. West instead exposes its checkpoint, trust-root set, and completeness boundary, plus `pending-convergence` if it knows delivery is incomplete.

When connectivity returns, West receives `E900`, `I31`, the agent report, and the signed human disposition. Stable event identities allow duplicate deliveries to be ignored. Causal references prevent the disposition from being applied before its evidence and contract are resolvable. West replays from its last signed checkpoint, recomputes its local projection, and reaches the same recorded sequence for the shared event set. This is recovery of a view from named inputs—not proof of universal convergence, truth, or scientific correctness.

## Limitations

A dependency graph is only as complete as its declarations. Undeclared reuse, inaccessible software, restricted evidence, ambiguous identifiers, compromised trust roots, and incompatible policy versions can leave impact unknown. Content addressing can establish byte-level identity without establishing meaning or quality. Transparency can expose an event history while still leaking sensitive relationships, so confidentiality-aware routing and minimized metadata are necessary.

Automation at scale may generate more candidates than humans can responsibly assess. Sybil behavior remains relevant to open federations, as framed by the original [Sybil attack paper](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/), but identity and reputation controls must not be described as capture resistance. Most importantly, automated observations, policy projections, and agent reports cannot silently become scientific dispositions. Qualified humans retain scientific authority under explicit roles and scopes.

A living event network therefore creates structured work; it does not complete that work by itself. Part 9 turns one review request from this loop into four routable work objects, including separate handling for confidentiality and restricted data, so that automation can assist without collapsing distinct responsibilities into a single opaque review task.
