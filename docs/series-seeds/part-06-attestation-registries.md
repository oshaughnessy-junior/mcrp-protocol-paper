---
artifact_role: outward-facing-blog-seed
authors: [Codex, junior]
status: mature-private-draft
date: 2026-08-21
series_part: 6
publication_status: private-not-approved
---

# Who said what about which release?

A compute center records a successful replay; a methods society approves the statistical procedure; a domain group challenges the interpretation. All three statements target the same claim version and remain visible without being averaged into one badge.

A distributed review system needs interoperable places where independently produced review claims can be registered, discovered, challenged, superseded, and revoked. We call these **federated attestation registries**, or more loosely trust servers. They record typed, signed statements about exact releases and claim versions: who reports rerunning them, what was examined, what passed, what failed, what remained outside scope, and what later event changed an earlier decision’s standing.

The registry is not the novel idea here. [W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model-2.0/) specifies a model for cryptographically verifiable claims. [SCITT RFC 9943](https://www.rfc-editor.org/rfc/rfc9943.html) describes transparency-service architecture for registering signed statements and producing receipts. [Linked Data Notifications](https://www.w3.org/TR/ldn/), [Activity Streams](https://www.w3.org/TR/activitystreams-core/), [WebSub](https://www.w3.org/TR/websub/), and [COAR Notify](https://coar-notify.net/specification/1.0.1/) provide established patterns for decentralized notifications and event exchange. [Nanopublications](https://nanopub.net/) and [Trusty URIs](https://trustyuri.net/) demonstrate content-addressed assertions and identifiers. [COAR’s publish-review-curate model](https://coar-repositories.org/what-we-do/repositories-and-publishing/) and [Peer Community In](https://peercommunityin.org/faq/) are guiding prior art for separating publication, review, and curation.

MCRP’s proposal is narrower: define a scientific profile and lifecycle binding that could connect these established components. Cross-system interoperability remains proposed and untested. Nothing here establishes adoption, operational scale, or convergence on a common policy.

## Four operations, not one badge

A useful design separates registration, replication, discovery, and federation:

```text
Reviewer or replay service
          |
          | signed attestation
          v
[1. Registration service] -----> inclusion receipt
          |
          | indexed event
          v
[2. Discovery view] -----------> reader or routing agent
          ^
          |
[3. Replication activity] ------ new, independently signed result
          |
          | selected event exchange
          v
[4. Federated peer registry] ---> its own indexes and policy views
```

**Registration** checks envelope and schema conformance, verifies the presented signature, records or references the statement, and returns an inclusion receipt. The receipt says that a particular service registered particular bytes under stated rules. It does not say the scientific claim is true, the reviewer is competent, or the reported work occurred as described.

**Replication** is scientific activity performed outside the registry. A replay service or qualified human may execute procedures and then issue an attestation. The registry records that report; it does not perform the experiment merely by receiving it.

**Discovery** indexes events so that people and software agents can find relevant reviews, challenges, withdrawals, or superseding releases. Automated observations, policy projections, and agent reports must retain their types and provenance. They cannot silently become scientific dispositions.

**Federation** exchanges selected records or notifications among independently governed nodes. [OpenID Federation](https://openid.net/specs/openid-federation-1_0.html) offers relevant prior art for establishing entity relationships, publishing metadata, and evaluating trust chains or trust marks during node bootstrap. A trust mark can report that an authority made a statement under a policy; it is not a universal endorsement.

Review events also need a portable representation. [DocMaps](https://docmaps.knowledgefutures.org/) supplies prior art for describing editorial and review processes as structured event histories. MCRP could profile such events while preserving identifiers for the claim, release, evidence set, actor, policy, and decision.

## A worked example

Suppose release `R7` contains claim version `C3`: “Pipeline P estimates parameter θ with the uncertainty procedure specified in contract `A2`.” Its evidence bundle hashes to `E9`.

A university compute center reruns the archived workflow on a declared environment. The numerical output matches the released tolerances, but the center does not assess whether the uncertainty procedure is scientifically appropriate. It signs a **replay observation** whose scope says “execution and numerical comparison only.”

A statistical methods society separately examines `C3`, `A2`, and `E9`. Two qualified reviewers declare conflicts, inspect the procedure, and issue a **scientific disposition** accepting the method within a stated population and model class. The binding is recorded exactly as `(claim version, acceptance-contract version, evidence-set digest, release digest, role, decision)`.

A domain consortium then reports that the sampled population excludes a relevant physical regime. It signs a **challenge** against the same claim version but does not dispute the replay observation. Its event links the challenged disposition, supplies a new evidence digest, and requests reconsideration.

The registration service issues separate receipts for all three signed records. A discovery view can show:

- replay observed, with limited scope;
- methods acceptance, under society policy version `S4`;
- domain challenge pending qualified-human review.

A routing agent may notify the society and locate reviewers with appropriate domain roles. It may project “contested under policy S4” as a machine-generated status. It may not rewrite that projection into “rejected,” nor may the replay result become an acceptance decision. If qualified humans later revise the disposition, they issue a new signed event linked to the earlier one; the earlier record remains inspectable.

Identity and contribution metadata can help readers interpret this history without becoming scientific authority. [ORCID peer-review records](https://support.orcid.org/hc/en-us/articles/360006971333-Peer-Reviews/) and [ORCID trust markers](https://info.orcid.org/interpreting-the-trustworthiness-of-an-orcid-record/) provide relevant identity context; [ROR](https://ror.org/about/) identifies research organizations; [CRediT](https://credit.niso.org/) describes contributor roles; and [Crossref’s peer-review record type](https://www.crossref.org/documentation/schema-library/markup-guide-record-types/peer-reviews/) provides publication metadata prior art. These records can support routing and credit, but no identifier or accumulated history settles a scientific question.

## Automation without silent authority

At scale, a living, self-updating event network could ingest signed review events, follow release links, update indexes, notify affected communities, and surface policy-specific views. Agents could detect missing bindings, stale reviews, conflicting attestations, or releases affected by a withdrawn dependency. Such outputs remain observations or projections until the relevant acceptance contract assigns a qualified human role the authority to decide.

Registries may apply different admission and display policies. A methods society might accept dispositions only from credentialed statisticians with declared conflicts, while a replication community might display every signature-verifiable rerun. Hosting is not endorsement, and plurality should not be collapsed into a universal score. The classic [Sybil attack analysis](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/) is a reminder that multiplying apparent identities can distort decentralized reputation. Organizational affiliations, trust marks, and histories can inform local policy, but they do not eliminate that governance problem.

## Limitations

This proposal does not demonstrate that independent registries will exchange compatible records, that communities will agree on roles or contracts, or that the resulting network will resist capture. Content addressing and transparency receipts expose particular changes and registrations; they do not establish truth or fair governance. Persistent identifiers may still refer to incomplete, misleading, or compromised assertions. Notifications can be delayed or ignored. Revocation and supersession rules may conflict across jurisdictions and disciplines.

Reviewer-history routing can also reproduce prestige and exclusion. Policy views therefore need inspectable criteria, appeal paths, conflict declarations, and room for communities to maintain distinct judgments. MCRP does not replace journals, societies, repositories, or qualified scientific review. It proposes a way to preserve and connect their explicit events without allowing infrastructure or automation to inherit authority by accident.

The next part turns from where attestations live to the harder social problem they create: how reviewer histories can support routing and credit without becoming a single prestige score.
