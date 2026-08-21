---
artifact_role: outward-facing-blog-seed
authors: [Codex, junior]
status: mature-private-draft
date: 2026-08-21
series_part: 4
publication_status: private-not-approved
---

# What happens after acceptance?

Scientific approval should have a history, not a halo. An approval that silently outlives the evidence it reviewed is a provenance failure.

Acceptance is an event, not a permanent property of a claim. A durable record should say that a qualified reviewer accepted a particular claim version under a particular acceptance contract, using a particular evidence set, for a particular release. Where a signed attestation is used, its binding should be explicit: `(claim version, acceptance-contract version, evidence-set digest, release digest, role, decision)`. Later events must not rewrite that historical decision. They append new information about the claim’s current disposition.

This proposal borrows from established prior art rather than presenting trust registries, transparency services, decentralized notifications, identifiers, content-addressed assertions, or publish-review-curate as MCRP inventions. Relevant foundations include [W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model-2.0/), the [SCITT architecture](https://www.rfc-editor.org/rfc/rfc9943.html), [Linked Data Notifications](https://www.w3.org/TR/ldn/), [Activity Streams](https://www.w3.org/TR/activitystreams-core/), [WebSub](https://www.w3.org/TR/websub/), [COAR Notify](https://coar-notify.net/specification/1.0.1/), and the [COAR publish-review-curate model](https://coar-repositories.org/what-we-do/repositories-and-publishing/). Content-addressed assertions likewise have precedents in [nanopublications](https://nanopub.net/) and [Trusty URIs](https://trustyuri.net/). MCRP’s proposal is to compose such mechanisms around explicit scientific dispositions and their dependencies.

Four disposition terms need careful separation:

- **Stale** means that a later event may affect the basis of an earlier decision, so the claim requires inspection or renewed review. Staleness is a warning about present standing, not a claim that the earlier reviewer acted incorrectly.
- **Superseded** means that a designated successor claim or release now occupies the relevant role. The earlier object and its historical approval remain recorded.
- **Withdrawn** means that an authorized party, commonly an author or publisher, has asked that an object no longer be relied upon under the stated scope. Withdrawal does not erase prior events or settle every scientific question about the object.
- **Revoked** means that an authority has rescinded a disposition or credential it previously issued, according to an identified policy and role. Revocation is about that authority’s decision; it is not a universal declaration of falsehood.

These states can coexist at different layers. A release might be withdrawn while one independently preserved claim is still discussed elsewhere. A reviewer’s endorsement might be revoked while the underlying claim remains available for new review. A claim might be stale without being withdrawn, revoked, or superseded.

## A worked release-to-successor example

Consider release `R1` of an observational analysis containing two claims:

- `C1-v1`: “The calibrated amplitude is 4.2 ± 0.3 units.” Its evidence set includes calibration dataset `D-cal-v1`, analysis code `A-v1`, and figure `F2-v1`.
- `C2-v1`: “Simulation family S exhibits the reported stability boundary.” Its evidence set includes simulation inputs `D-sim-v3` and code `S-v5`; its recorded dependency graph contains no edge to `D-cal-v1`.

A qualified reviewer accepts both claims for `R1`, but as separate dispositions bound to their own claim versions and evidence-set digests. Six weeks later, the calibration team publishes `D-cal-v2` after correcting a unit conversion. The correction changes `F2`, the numerical result in `C1`, and the release’s abstract, but it does not change the simulation inputs or code.

The event timeline is therefore:

1. **Day 0 — `R1` published:** `C1-v1` and `C2-v1` receive recorded acceptance decisions under contract `AC-7`.
2. **Day 42 — correction announced:** an automated observer detects that `D-cal-v1` has a declared successor, `D-cal-v2`, and projects the dependency change through the recorded graph.
3. **Day 42 — candidates flagged:** the system emits a policy projection that `C1-v1`, `F2-v1`, and the abstract may be stale. It does not silently change their scientific dispositions.
4. **Day 45 — human scope decision:** a qualified reviewer confirms that `C1-v1` is stale pending replacement. The reviewer also confirms, from the explicit dependency record and relevant checks, that the correction does not alter the disposition of `C2-v1`.
5. **Day 51 — `R2` published:** `C1-v2` reports 3.8 ± 0.3 units using `D-cal-v2`. A reviewer gives `C1-v2` a new disposition. `C1-v1` is marked superseded by `C1-v2`; its original acceptance remains part of the history. `C2-v1` may be included unchanged in `R2`, but it does not inherit approval merely because its label or bytes are unchanged.

That last point is the carry-forward rule: **no claim inherits approval solely because its label, text, identifier, or content digest is unchanged across releases**. Carry-forward requires an explicit policy-authorized decision. The decision may reference prior review and record that the relevant evidence and dependency scope are unchanged, but a qualified human remains responsible for the scientific disposition. Automation can assemble the delta, identify affected paths, and prepare a candidate attestation; it cannot turn absence of a detected change into approval.

The distinction matters at scale. A living, self-updating event network could ingest corrections, reruns, challenges, endorsements, successor links, and policy notices from many sources. Stable identifiers for people, organizations, and contributions can draw on established systems such as [ORCID peer-review records](https://support.orcid.org/hc/en-us/articles/360006971333-Peer-Reviews), [ROR](https://ror.org/about/), and [CRediT](https://credit.niso.org/). Federation and notification mechanisms can move events without requiring one publisher to own the complete history. Yet automated observations, policy projections, and agent reports must remain visibly typed as such; none may silently become a scientific disposition.

Three questions must consequently stay distinct. **Was this release approved then?** is historical. **Can its recorded computations be reconstructed now?** is operational. **Does a named policy presently regard this claim as supported?** is current and policy-bound. Combining them produces either amnesia, in which earlier decisions disappear, or false permanence, in which acceptance never ages.

## Limitations

A dependency graph can be incomplete, and an apparently independent claim may share undocumented assumptions, software, personnel, or data transformations. Registries and signatures establish provenance and attributed action, not truth or reviewer competence. Federation also introduces identity, authorization, spam, and [Sybil-attack](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/) concerns. Human review may become a bottleneck, while differing policies can produce simultaneous, incompatible dispositions. The model described here is therefore a proposal for preserving and interpreting review events, not evidence of validation, adoption, scale, convergence, capture resistance, or improved scientific outcomes. It does not replace journals or other institutions.

Once records, reviews, and curation decisions can persist separately, the next question is institutional rather than merely technical: who may issue a disposition, under which policy, and why should that authority belong to a single journal? Part 5 turns to review beyond the journal boundary.
