---
artifact_role: bounded-research-note
authors:
  - Codex
  - junior
status: working-draft
date: 2026-08-16
question: Which existing standards and systems should an MCRP federated review-trust layer reuse, and what integration gap may remain?
claim_posture: source-facts-separated-from-design-inference
---

# Trust-layer landscape for distributed MCRP review

## Research judgment

A federated attestation layer is a coherent extension of MCRP, but almost none of its constituent mechanisms are new. The plausible integration contribution is narrower:

> Bind an exact scientific object to a typed account of what was checked, a signed and scoped judgment, a transparent registration history, and plural policies for deciding whether that judgment is sufficient.

This proposition still requires formal crosswalks, implementation, security review, and comparative trials.

## Reusable foundations

| Need | Primary source and established capability | Candidate MCRP use; this column is inference |
|---|---|---|
| Signed claims | [W3C Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/) defines issuer–holder–verifier credentials, proofs, evidence, schemas, and status hooks. | Profile scientific review, competency, contribution, and authorization attestations; do not treat credential verification as proof that a claim is true. |
| Credential status | [W3C Bitstring Status List 1.0](https://www.w3.org/TR/vc-bitstring-status-list/) provides a privacy-conscious mechanism for suspension or revocation status. | Reuse status machinery where appropriate, while keeping key compromise, withdrawal, supersession, expiry, and scientific retraction semantically distinct. |
| Portable identifiers | [W3C DID Core](https://www.w3.org/TR/did-core/) defines controller-managed identifiers and verification methods without requiring one central registry. | Use only where key portability or non-institutional identity adds value; a DID does not establish uniqueness, expertise, independence, or conduct. |
| Signed statement transparency | [IETF SCITT, RFC 9943](https://www.rfc-editor.org/rfc/rfc9943.html) defines signed statements, transparency services, receipts, and auditability; one statement can be registered independently with multiple services. SCITT does not define scholarly discovery, reputation, server-to-server federation, or inter-node replication. | Treat scientific review statements as domain-specific signed statements registered with multiple independent services, then specify scholarly exchange and discovery separately. |
| Append-only log precedent | [Sigstore Rekor](https://docs.sigstore.dev/logging/overview/) records signed metadata in an auditable, append-only transparency log with inclusion and consistency verification. | Reuse transparency-log patterns, monitors, witnesses, and identity monitoring; log inclusion means registered, not scientifically endorsed. |
| Attestation envelope | The developing [in-toto Attestation Framework v1](https://github.com/in-toto/attestation/tree/main/spec/v1) binds typed predicates to digest-identified subjects in signed envelopes. | Evaluate it as a candidate envelope for scientific review predicates rather than assuming it is the final choice. |
| Federation bootstrap and trust marks | [OpenID Federation 1.0](https://openid.net/specs/openid-federation-1_0.html) defines signed entity statements, trust chains, trust marks, delegated trust-mark issuers, status, and discovery. | Reuse selected machinery for node and community recognition; do not adopt one hierarchical trust anchor as universal scientific authority. |
| Review workflow federation | [COAR Notify](https://coar-repositories.org/tools-and-resources/notify/) supports decentralized communication between repositories, peer-review services, and overlay journals, including requests and announcements. | Profile review request, report, endorsement, correction, and undo messages with exact MCRP release identities and signatures. |
| Review-event representation | [DocMaps](https://docmaps.knowledgefutures.org/) proposes and pilots a machine-readable, extensible, discoverable framework for editorial and peer-review events in publish–review–curate workflows. | Experimentally map MCRP review objects to its vocabulary, adding claim-level scope and execution/evidence digests only where absent. |
| Registered peer-review metadata | [Crossref's peer-review record type](https://www.crossref.org/documentation/schema-library/markup-guide-record-types/peer-reviews/) supports referee reports, editor reports, community comments, recommendations, revision rounds, conflicts, and `isReviewOf` relations. | Register citable review objects and link them to immutable releases; Crossref metadata alone does not establish exact computational state or signer authority. |
| Researcher identity and review activity | [ORCID peer reviews](https://support.orcid.org/hc/en-us/articles/360006971333-Peer-Reviews) can be added by trusted organizations with reviewer permission; [ORCID trust markers](https://info.orcid.org/interpreting-the-trustworthiness-of-an-orcid-record/) expose assertion provenance. Visibility remains researcher-controlled and permission-dependent. | Reference ORCID before creating a new identity system, but do not use it as the sole durable ledger of review decisions. |
| Organization identity | [ROR](https://ror.org/about/) supplies an open, community-led registry of persistent research-organization identifiers. | Identify affiliations, credential issuers, review communities, archives, and server operators. |
| Contribution roles | [ANSI/NISO CRediT](https://credit.niso.org/) defines 14 research contribution roles and is intended to improve attribution and accountability. | Represent research contributions using existing roles; define review-specific roles separately rather than stretching authorship categories. |
| Review terminology | [ANSI/NISO Z39.106-2023](https://www.niso.org/publications/z39106-2023-peerreview) standardizes terminology for peer-review identities and processes. | Reuse vocabulary in review-community profiles and disclosure rather than inventing new labels. |
| Decentralized atomic assertions | [Nanopublications](https://nanopub.net/) combine assertion, provenance, and publication-information graphs; their [architecture](https://nanopub.net/docs/architecture/) supports decentralized services, and [Trusty URIs](https://trustyuri.net/) provide content-addressed identifiers. | Treat signed, immutable, distributed assertion publishing as close prior art; test whether MCRP needs only a scientific-review profile and lifecycle binding. |
| Claim and provenance packaging | [PROV-O](https://www.w3.org/TR/prov-o/) covers entities, activities, agents, and responsibility; [RO-Crate](https://www.researchobject.org/ro-crate/specification.html) packages research objects; [Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/) represents workflow execution; [Micropublications](https://doi.org/10.1186/2041-1480-5-28) represent claims, evidence, support, challenge, and attribution. | Keep MCRP-specific work focused on prospective contracts, scoped authority, invalidation, and exact binding of review events to releases. |
| Discovery and relationship indexes | [Signposting](https://signposting.org/) supports machine discovery of scholarly resources and constituents; the [Crossref Research Nexus](https://crossref.org/documentation/research-nexus/) and [DataCite Event Data](https://support.datacite.org/docs/eventdata-guide) index relationships among research objects and events. | Separate crawling, notifications, relationship indexing, and trust evaluation rather than asking one trust node to perform all four. |

## Closest social and institutional systems

### Publish–review–curate and overlay review

[COAR describes publish–review–curate](https://coar-repositories.org/what-we-do/repositories-and-publishing/) as a family of workflows connecting repositories with review and curation services rather than requiring a conventional journal container. [Peer Community In](https://peercommunityin.org/faq/) already has disciplinary communities whose recommenders select reviewers, manage evaluation, make editorial decisions, and publish citable recommendations.

**Inference:** MCRP should not claim to invent distributed or overlay review. It can contribute exact computational-release binding, claim-scoped attestations, and dependency-sensitive status to this ecosystem if those features survive interoperability tests.

### Review and contributor recognition

ORCID records peer-review activity and its source, while Crossref can register reviews and recommendations as citable records. CRediT formalizes contributor roles.

**Inference:** A future reviewer/contributor history should link to these infrastructures rather than replace them. MCRP may add evidence-bearing scope: what exact claim or release was reviewed, by which method, under which policy, with what later challenges.

### Decentralized review and reputation proposals

Decentralized peer-review, blockchain review, token incentive, and reviewer-reputation designs have a substantial literature. Examples include [DecSci](https://doi.org/10.1016/j.ipm.2021.102724), [PRINCIPIA](https://arxiv.org/abs/2008.09011), [Ants-Review](https://arxiv.org/abs/2101.09378), and a [2024 mechanism proposal](https://arxiv.org/abs/2404.18148). These works already discuss community governance, transparent review, reviewer certificates, incentives, and reputation.

**Inference:** “Decentralized journals,” voting, reputation, tokens, and blockchain are not defensible novelty claims for MCRP. A blockchain is not required for the core design. Transparency logs and replicated archives can test the architectural hypothesis with fewer governance commitments.

### Agent-native publication

[Traxia](https://arxiv.org/abs/2606.08256v1) is especially close on signed agent identities, immutable contribution histories, tiered review, reputation, and contradiction detection. It reports architectural foundations and a partial prototype rather than empirical validation.

**Inference:** The differentiator cannot be “agents can sign and review.” It must remain the standards-compatible connection between prospectively fixed claim contracts, exact execution evidence, externally enforced transitions, portable review attestations, and scoped invalidation—and this remains unvalidated.

## Proposed MCRP design inference: trust is not one kind of edge

The framework should distinguish:

- **epistemic:** supports, bounds, contradicts, fails to reproduce, narrows, leaves unassessed;
- **procedural:** completed a declared review, executed under reviewer control, satisfied a mechanical policy;
- **authority:** controls an identity, holds an affiliation, has recognized competence, received a delegation;
- **social/governance:** admitted by a community, subject to a conflict rule, sanctioned, appealed, or reinstated;
- **operational:** preserved, resolvable, fresh, revoked, superseded, unavailable.

A trust view is a policy-bound query over these edges. It is not a global property stored on a person or release.

Example query:

> Show exact releases endorsed by two institutionally independent domain reviewers, with one reviewer-controlled execution, registered by two separately governed nodes, and with no unresolved material challenge newer than the endorsements.

The query's roots, definitions of independence, accepted credentials, thresholds, time window, and treatment of missing evidence must themselves be versioned and visible.

## Proposed MCRP design inference: Sybil and capture posture

Keys do not create unique humans or independent institutions. The classic [Sybil attack](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/) result is a warning against treating a permissionless population of identifiers as a reliable population of actors.

MCRP should use layered resistance:

- authenticated ORCID and institutional assertions when appropriate;
- multiple independent identity and competency attestations;
- community-specific reviewer eligibility;
- quorums based on trust domains and conflicts, not raw key count;
- collaboration and conflict-graph checks;
- limits on correlated endorsements;
- transparent selection rules, audits, and appeals;
- rate limits and moderation against spam or coordinated abuse;
- explicit newcomer routes that do not require inherited prestige;
- export and fork paths when a node or community is captured;
- no token balance, citation count, institutional prestige, or scalar reputation as sole authority.

These measures mitigate; they do not prove independence or prevent capture.

## Gap statement and stop conditions

The narrow candidate gap is the bridge among:

1. an exact scientific release and claim graph;
2. a typed statement of what was checked;
3. a signed, scoped human or machine disposition;
4. an auditable, multi-node registration history plus a separately specified exchange and discovery layer;
5. plural, reproducible policies that derive current standing.

Stop or narrow this program if a closest system already implements this end-to-end with prospective contracts, exact execution binding, independent authority, challenges, revocation, freshness, and plural policy views; if crosswalks require incompatible reinvention of existing standards; or if trials show no meaningful benefit over a repository plus open peer-review records.

## Evidence required before stronger claims

- Round-trip mappings for SRRs, reviews, credentials, status, and notifications
- Two independently implemented nodes exchanging the same event set
- Replay, revocation, equivocation, conflict, Sybil, and capture fixtures
- Reviewer studies testing whether views improve or damage comprehension
- A real distributed review with claim-level division of labor
- Comparisons against repository-plus-open-review and publish–review–curate baselines
- Measures of defect detection, false acceptance, disagreement visibility, review effort, privacy cost, recovery after change, and governance failures

Until those exist, describe this as an architecture and evaluation agenda, not a working replacement for journals or an evidence-backed improvement to peer review.
