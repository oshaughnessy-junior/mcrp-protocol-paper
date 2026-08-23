---
artifact_role: outward-facing-blog-draft
authors: [Codex, junior]
status: mature-private-draft
date: 2026-08-23
series: Making Computational Review Version-Specific
series_part: 4
publication_status: private-not-approved
audience:
  - journal and society editors
  - repositories and review services
  - scholarly-infrastructure builders
  - research funders and curators
reader_utility: design portable scoped review products without assigning scientific authority to a registry or universal platform
operational_artifact: responsibility matrix and minimum portable-review record
evidence_status: interoperability proposal grounded in deployed standards and review models; cross-system operation untested
source_drafts: [part-05-review-need-not-belong-to-a-journal, part-06-attestation-registries, part-07-reputation-without-a-universal-score]
future_cross_list_slot: internal web/iOS MCRP protocol prototype; unscheduled and not evidence for this post
---

# Portable review without a universal platform

_Making Computational Review Version-Specific, 4 of 6_  
_By Codex and junior_

A compute center can verify an execution. A methods society can assess an estimator. A domain group can challenge an interpretation. Today, their reports are difficult to combine without flattening them into one badge—or trapping them inside one platform.

The problem is not that journals, repositories, societies, and review services perform different functions. The problem is that their products rarely point to the same exact scientific objects with enough structure to travel, remain scoped, and change status without losing their history.

MCRP proposes **portable review records**: attributable statements about exact claim and release versions, carrying their method, evidence, scope, exclusions, policy, and current status. A registry can store or index such a record. Registration is not endorsement. Discovery is not acceptance. A cryptographic signature is not evidence that its signer is competent or independent.

The goal is plural infrastructure with explicit responsibility, not a universal trust server.

## The functions can separate; accountability cannot

Journals commonly bundle preservation, discovery, reviewer selection, workflow control, judgment, endorsement, correction, reputation, appeals, and sanctions. A distributed system can allocate those functions differently, but it cannot wish them away.

## Operational artifact 1: responsibility matrix

| Function | Possible responsible party | Portable output | Authority boundary |
|---|---|---|---|
| Preserve release | Repository or archive | Immutable release identifier and custody record | Preservation does not endorse contents |
| Execute workflow | Compute center or reviewer-controlled service | Scoped execution observation | Execution does not approve method or claim |
| Assess method | Methods community | Review report and scientific disposition | Decision applies only to named scope and policy |
| Assess interpretation | Disciplinary reviewers | Domain report, challenge, or disposition | Does not inherit methods authority automatically |
| Curate or recommend | Journal, society, or community | Curation decision under a versioned policy | Recommendation is local, not universal |
| Register and discover | Registry, index, or observatory | Receipt, index entry, and status events | Hosting and indexing are not endorsement |
| Handle appeals and sanctions | Accountable institution | Policy-bound adjudication or moderation record | Infrastructure cannot substitute for due process |

One organization may perform several rows. The design requirement is that readers can still distinguish them.

## Worked example: one release, three review products

Suppose release `R3` contains claim `C17-v2`: a measured excess is inconsistent with a specified background model under analysis procedure `A9`. The release identifies data `D4`, software environment `E8`, and its acceptance conditions.

A compute center reconstructs the workflow in a reviewer-controlled environment. Its report says the numerical table was reproduced within declared tolerances. It expressly excludes the appropriateness of the background model.

A statistical methods society reviews the claim and evidence. Its reviewers conclude that a nuisance parameter was constrained using information not justified by the released method. The society issues “major revision” under policy `MS-v6`.

After the authors publish `C17-v3` in successor release `R4`, a disciplinary curation group considers whether the earlier compute report and methods objection still apply. Software can compare the releases and flag the changed assumption. It cannot silently convert the earlier objection into “satisfied.” The curation group records its own decision and cites the earlier products.

A reader can now see three different acts: reconstruction, methods judgment, and curation. Another community may reach a different scoped decision. The records remain compatible without being averaged.

## Operational artifact 2: minimum portable-review record

A public interchange record should identify at least:

```text
Record
  identifier, schema, type, issue time, current status

Target
  exact release and claim versions; acceptance-condition version

Finding
  observation, report, challenge, adjudication, or disposition
  decision or relation; scope; exclusions; uncertainty

Basis
  evidence-set digest; review-report digest; method or profile used

Issuer
  actor identity; role; signing key; delegation when applicable
  competency or authorization basis; conflicts and affiliations

Policy
  governing community and policy version

Lifecycle
  expiry or freshness conditions; supersession, challenge,
  withdrawal, or revocation targets

Integrity and discovery
  signature; zero or more registry receipts; resolvable references
```

This is a minimum design target, not a proposed new universal schema. Existing formats should be profiled or cross-walked rather than replaced where possible.

## Registries perform four different operations

**Registration** verifies an envelope and signature, records or references the bytes, and returns a receipt under stated rules. **Review or replication** occurs elsewhere and produces a report. **Discovery** helps people and agents find reports about a release. **Federation** exchanges selected records or notifications among independently governed nodes.

Conflating these operations creates accidental authority. An inclusion receipt proves that a service registered bytes; it does not prove that the reported work occurred or the claim is true. A discovery ranking expresses a policy and visible event set; it is not protocol truth.

Reviewer standing should be equally explicit. “Trustworthy reviewer” is not a scalar property. Credit for work, scoped competency evidence, current authorization, conflicts, and later reliability-relevant events should remain separate. Communities may route work under published local policies, but MCRP should not define a universal reviewer score. Newcomer routes and useful dissent must survive.

## What is established, proposed, and evidenced

**Established prior art.** The [COAR publish–review–curate model](https://coar-repositories.org/what-we-do/repositories-and-publishing/) separates publication, review, and curation; [Peer Community In](https://peercommunityin.org/faq/) evaluates deposited preprints. [Crossref peer-review records](https://www.crossref.org/documentation/schema-library/markup-guide-record-types/peer-reviews/) and [DocMaps](https://docmaps.knowledgefutures.org/) describe review and editorial events. [W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model-2.0/) and [SCITT RFC 9943](https://www.rfc-editor.org/rfc/rfc9943.html) provide relevant signed-statement and transparency architecture. [OpenID Federation](https://openid.net/specs/openid-federation-1_0.html) addresses entity relationships and trust-chain metadata. These are guiding foundations, not MCRP inventions.

**MCRP proposal.** MCRP proposes a scientific profile that binds exact releases, claims, evidence, roles, decisions, changes, and community policies while keeping hosting, discovery, and endorsement distinct.

**Current evidence.** We have not demonstrated a cross-system round trip, community adoption, compatible policy interpretation, reliable revocation, or operation at scale. The matrix and record above are design artifacts.

## What remains open

Portability can be technical but not social: a record may be exportable while dominant interfaces ignore it. Registries can share one controller. Review rings can manufacture apparent activity. Confidential review may limit public verification. Policies can encode exclusion, and transparent ranking can still reward prestige. Appeals, legal accountability, financing, reviewer protection, and long-term stewardship remain institutional responsibilities.

The useful near-term target is therefore modest: make one review product independently resolvable, scoped to an immutable release, and understandable outside its home platform. Then test whether a second system can preserve its meaning.

The next post follows those records through corrections, partitions, and disagreement to define what a living scientific network can—and cannot—update automatically.

