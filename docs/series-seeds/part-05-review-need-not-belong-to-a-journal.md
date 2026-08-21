---
artifact_role: outward-facing-blog-seed
authors: [Codex, junior]
status: mature-private-draft
date: 2026-08-21
series_part: 5
publication_status: private-not-approved
---

# A review need not belong to a journal

The journal of a distributed review system may be less like a container and more like a view.

A conventional journal commonly bundles preservation, discovery, reviewer selection, workflow control, editorial judgment, endorsement, correction, and reputation. Those functions are valuable, but they do not have to be performed by one institution or stored beside one mutable document. The [COAR publish–review–curate model](https://coar-repositories.org/what-we-do/repositories-and-publishing/) explicitly separates publication, review, and curation, while [Peer Community In](https://peercommunityin.org/faq/) organizes evaluation and recommendation of deposited preprints. MCRP treats these as guiding prior art, not as novelty attributable to MCRP.

MCRP asks what becomes possible when participating services refer to the same immutable release and claim versions. A compute center can report a reviewer-controlled reconstruction. A methods society can assess a statistical procedure. A disciplinary group can review an interpretation. An archive can preserve the record. A curation community can publish a recommendation under its own policy. None needs to impersonate the others, and no automated report silently acquires the authority of a scientific decision.

This separation changes the unit around which review is organized. Instead of assuming that one journal owns the whole process, a reader could encounter a bundle of related records: a released manuscript, versioned claims, evidence references, reconstruction reports, signed reviews, author responses, challenges, and curation decisions. Identifiers, content-addressed assertions, trust registries, transparency services, decentralized notifications, and publish–review–curate workflows are established design resources for such a bundle. MCRP’s proposal is narrower: specify how these resources can describe review of exact scientific objects while preserving the boundary between evidence and disposition.

## The functions do not disappear

The difference is allocation, not abolition.

| Function | Conventional journal bundle | Possible distributed bundle |
|---|---|---|
| Preservation | Journal or contracted archive preserves the article | Repository or archive preserves each named release and associated records |
| Discovery | Journal site, index, and issue structure expose the work | Multiple indexes and community views discover the same identifiers |
| Reviewer selection | Editors select reviewers under journal policy | A review community selects reviewers under a versioned community policy |
| Workflow control | Journal platform manages invitations, reports, and revisions | Interoperating services exchange notices and status records |
| Technical checking | Journal staff, reviewers, or vendors perform checks | Compute, data, or methods services issue scoped reports |
| Scientific judgment | Editors and reviewers reach a disposition | Qualified reviewers and curators reach dispositions under declared roles |
| Endorsement | Acceptance and journal branding signal endorsement | One or more communities publish scoped recommendations or decisions |
| Correction | Journal updates, retracts, or links notices | Custodians preserve versions while authorized communities issue linked notices |
| Reputation | Journal, editors, and reviewers carry accumulated standing | Communities, roles, organizations, and persistent contributor records provide context |
| Appeals and sanctions | The journal’s accountable organization administers them | An identified institution remains responsible under its published policy |

The distributed column is a proposal about possible allocation. It is not evidence that the allocation works at scale, resists capture, produces agreement, or yields better decisions. Existing journals could participate unchanged at the level of scientific authority while exposing more precisely scoped, portable records. Other communities could undertake only one function, such as methods review, without presenting themselves as full journals.

## A worked example

Suppose a collaboration releases manuscript `R3`, whose central claim `C17-v2` says that a measured excess is inconsistent with a specified background model under analysis procedure `A9`. The release points to data digest `D4` and software environment digest `E8`. These references identify the proposal and its supporting evidence; they do not establish that the claim is true.

Three independent activities follow.

First, a compute center reconstructs the analysis in an environment controlled by its assigned reviewer. Its signed report says that the published workflow completed against `D4` and produced the stated numerical table within declared tolerances. That is an automated observation plus a reviewer-scoped report. It does not decide whether the model assumptions are scientifically appropriate.

Second, a statistical methods society reviews `C17-v2`. Its reviewers conclude that one nuisance parameter was constrained using information that the released methods do not justify. The society issues a decision of “major revision” under policy `MS-Policy-v6`, citing the reconstruction report and its own analysis. Where the society binds that disposition cryptographically, the attestation covers exactly `(claim version, acceptance-contract version, evidence-set digest, release digest, role, decision)`. The decision is therefore about the named versions and evidence set, not every past or future form of the claim.

Third, a disciplinary curation group considers the revised claim `C17-v3` in manuscript `R4`. It may reuse the compute report only after determining whether that report remains applicable. It may request a new statistical review, accept a declared carry-forward rule, or decline to decide. A policy projection generated by software can flag that `C17-v3` changed an assumption covered by the earlier objection, but the projection cannot silently turn “major revision” into “satisfied.” A qualified human acting in an authorized role must issue the scientific disposition.

A reader’s interface could then show a community-specific view: the preserved releases, the compute observation, the methods decision, the author response, and the curation outcome. Another community could present a different view or reach a different scoped decision. The records remain distinguishable: observations report what a process produced; evidence supports or challenges a claim; policies state decision conditions; authorized people make scientific dispositions.

## Institutions still matter

A filtered interface cannot substitute for governance. Confidentiality, reviewer protection, conflict enforcement, research ethics, sanctions, appeals, financing, legal accountability, and long-term preservation require accountable organizations. Reviewer identity may sometimes be public, pseudonymous, confidential to an institution, or disclosed only under an appeal procedure. A technical signature can bind a statement to a credential, but it cannot determine whether the credentialing process was fair or whether an institution exercised sound judgment.

The journal analogue in MCRP is therefore a recognizable review community plus a versioned curation policy: who may review, which conflicts are prohibited, which predicates are required, how challenges and appeals work, and when a decision becomes stale. Existing journals can provide exactly this function. The architecture neither predicts nor requires their disappearance. It separates functions so that the scope, custody, and authority of each record can be represented explicitly.

Automation remains important because a living, self-updating event network may need to track many releases, claims, reviews, responses, and policy changes. Services can detect new records, verify digests, route notifications, project policy consequences, and assemble views. Qualified humans retain scientific authority. Automated observations, policy projections, and agent reports cannot silently become scientific dispositions.

## Limitations

This architectural sketch does not demonstrate adoption, validation, operational scale, community convergence, resistance to capture, or improvement over journal-centered workflows. Distributed responsibility can create gaps: no community may accept jurisdiction; policies may conflict; records may be technically available but socially illegible; confidentiality can restrict portability; and preservation obligations may be disputed. Multiple attestations can also create the appearance of consensus when they share reviewers, evidence, or institutional dependencies.

Nor does content addressing establish truth. It can help identify what was reviewed, while the adequacy of evidence, the interpretation of results, and the legitimacy of a decision remain scientific and institutional questions. MCRP must preserve those distinctions in both its data model and its interfaces.

The next numbered part turns from institutional allocation to exchange infrastructure: how established trust registries, transparency services, decentralized notification protocols, identifiers, and signed attestations might let communities discover statements about exact releases without mistaking transport or registration for scientific endorsement.
