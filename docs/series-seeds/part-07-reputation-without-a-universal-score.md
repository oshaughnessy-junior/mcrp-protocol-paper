---
artifact_role: outward-facing-blog-seed
authors: [Codex, junior]
status: mature-private-draft
date: 2026-08-21
series_part: 7
publication_status: private-not-approved
---

# Reputation and credit without a universal score

“Trustworthy reviewer” is not a scalar property. A person may be excellent at numerical reconstruction, inexperienced with a particular instrument, conflicted on one project, and uniquely qualified to interpret another. Even within one specialty, recent diligence, institutional relationships, available time, and the precise claim under review can matter differently.

A distributed system still needs to route work and recognize contributions. The mistake would be to compress identity, competence, diligence, agreement, prestige, and scientific correctness into one number. Such a score would invite Goodhart effects, reputation laundering, reciprocal review rings, prestige recursion, newcomer exclusion, and penalties for useful dissent. It would also conceal why a reviewer was selected.

MCRP therefore proposes typed, event-derived histories rather than a universal reputation score. This proposal draws on established guiding prior art: [ORCID peer-review records](https://support.orcid.org/hc/en-us/articles/360006971333-Peer-Reviews/) associate review activity with researcher identities; [ROR](https://ror.org/about/) supplies identifiers for research organizations; [CRediT](https://credit.niso.org/) distinguishes contribution roles; and [Crossref’s peer-review record type](https://www.crossref.org/documentation/schema-library/markup-guide-record-types/peer-reviews/) represents reviews as identifiable scholarly records. These systems do not become MCRP inventions when incorporated into an MCRP design.

The relations must remain separate:

- **Credit** records what a person or agent contributed: a review, reconstruction, dataset check, policy projection, or synthesis.
- **Competency** records scoped evidence that a person has relevant experience or demonstrated capability.
- **Authorization** records that a community currently permits an actor to perform a defined role under a particular policy.
- **Current reliability evidence** records later events relevant to how a contribution performed, without converting those events into a timeless property of its author.

Agreement is not one of these relations. A dissenting reviewer may be careful and useful; a reviewer who agrees with the majority may still have supplied little evidence. Credit should survive later disagreement or correction because it describes work performed, not permanent endorsement. Conversely, receiving credit does not grant competency or authorization.

## A worked routing example

Suppose the North Coast Methods Cooperative needs two reviewers for claim `NC-17-v3`: “The revised calibration removes the reported seasonal bias from detector channel C.” The claim references a calibration notebook, raw comparison data, and a release digest. The cooperative publishes this routing policy before selecting anyone:

1. Select one calibration-method reviewer with qualifying evidence from the last five years.
2. Select one detector-domain reviewer; supervised newcomer reviews count as qualifying evidence after two completed reviews with disclosed mentor assessments.
3. Exclude declared financial or supervisory conflicts and candidates controlled by the claimant’s institution.
4. Do not rank candidates by agreement rate, citation count, or a global reputation score.
5. If a prior dissent was later addressed by a correction, preserve both the dissent and adjudication as typed events; do not treat dissent itself as negative evidence.
6. Record missing identity or history data explicitly rather than interpreting absence as failure.

The candidate event histories are:

- **Dr. Imani Rao** has three recent calibration reviews, disclosed methods, and no recorded conflict. Her ROR-identified institution differs from the claimant’s institution.
- **Leah Chen**, a newcomer, has one supervised detector review and relevant instrument-operation credit recorded with a CRediT role. She has not yet met the cooperative’s two-review threshold for an unsupervised domain-review role.
- **Dr. Mateo Silva** has domain experience and previously filed a minority review challenging a drift correction. A later adjudication accepted part of his challenge and prompted a revised uncertainty statement. He has no declared conflict.
- **Dr. Erin Vale** has extensive calibration experience but currently supervises the claimant and is excluded by the published conflict rule.

Applying the policy yields Rao as the calibration reviewer and Silva as the detector-domain reviewer. Vale’s exclusion is attributable to a specific relation and policy clause, not a low score. Silva’s earlier dissent remains positive evidence of relevant scrutiny only to the extent stated by the recorded events; it is not proof that his new judgment will be correct.

Chen is not silently discarded. The system offers a newcomer path: she may join as an additional supervised reviewer, with her report preserved and credited separately. If she completes this review and a second supervised review under the stated policy, a qualified human committee may later attest that the threshold for unsupervised routing has been met. Automation can identify the threshold event and prepare the record, but it cannot silently issue the scientific disposition or expand her authorization.

For an acceptance decision, a relevant attestation can bind exactly `(claim version, acceptance-contract version, evidence-set digest, release digest, role, decision)`. This prevents a decision about one version and evidence set from appearing to govern another. Content-addressed assertions, including established approaches such as [Nanopublications](https://nanopub.net/) and [Trusty URIs](https://trustyuri.net/), can help make referenced objects explicit. They do not determine whether the scientific judgment is warranted.

## Inspectable trust views

At scale, automation may continuously assemble eligible-candidate views from signed events, identifiers, disclosed affiliations, review records, challenges, corrections, and policy versions. Trust registries, transparency services, decentralized notifications, persistent identifiers, content-addressed assertions, and publish-review-curate workflows are established guiding prior art, not MCRP novelty. [ORCID’s trust-marker guidance](https://info.orcid.org/interpreting-the-trustworthiness-of-an-orcid-record/) also illustrates why provenance and assertion source matter more than a profile’s mere fullness.

Each computed view should expose its policy roots, exclusions, evidence window, unresolved contradictions, and treatment of missing data. Communities may publish different routing policies and reach different candidate sets from the same event history. Neither result becomes protocol truth. The purpose is to make the inference reproducible and contestable while preserving the underlying events.

Automated observations, policy projections, and agent reports must remain typed as such. They cannot silently become scientific dispositions. Qualified humans retain scientific authority: they decide whether evidence satisfies a community’s acceptance contract, whether a conflict requires recusal, and whether an authorization should change. Agents may route, summarize, monitor, and flag; their outputs remain proposals or observations until an authorized human act is recorded.

## Limitations

Typed histories can be incomplete, selectively disclosed, stale, or linked to the wrong identity. Institutional identifiers do not reveal every controlling relationship. Community policies can encode exclusion, and transparent rules can still be strategically manipulated. Multiple identities can distort event histories, a general risk described by the primary [Sybil attack paper](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/). Newcomer pathways may reproduce existing networks if mentor eligibility is narrow. Human adjudicators can also be conflicted or inconsistent.

Accordingly, this design does not claim capture resistance, correctness, convergence, adoption, validation, or improved reviewer selection. It offers a narrower proposal: keep credit, competency, authorization, and current reliability evidence distinct; preserve dissent and correction as inspectable events; and prevent one ranking from hardening into universal protocol truth.

Those event-derived views need not remain static. New reviews, challenges, conflict disclosures, corrections, and adjudications can update a living, self-updating event network without rewriting the past. Part 8 follows that update loop and asks what “living” can responsibly mean when automation maintains the network but qualified humans retain scientific authority.
