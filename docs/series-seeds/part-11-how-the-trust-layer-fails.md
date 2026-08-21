---
artifact_role: outward-facing-blog-seed
authors: [Codex, junior]
status: mature-private-draft
date: 2026-08-21
series_part: 11
publication_status: private-not-approved
---

# How the trust layer fails

Decentralization does not cure social power. It can distribute failure as readily as authority.

MCRP imagines automation at scale: a living, self-updating event network in which proposals, evidence, reviews, challenges, releases, and curatorial decisions remain linked as they change. That network can support discovery and coordination, but qualified humans retain scientific authority. Automated observations, policy projections, and agent reports are typed inputs. They cannot silently become scientific dispositions.

This distinction matters because cryptographic integrity is narrower than scientific trust. No signature proves that its signer is unique, independent, competent, or honest. No append-only log proves that its contents are scientifically sound. No federation prevents nominally independent services from sharing one controller. The classic [Sybil analysis](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/) explains why counting identities cannot by itself establish independent participation.

MCRP therefore treats trust registries, transparency services, decentralized notifications, persistent identifiers, content-addressed assertions, and publish-review-curate workflows as guiding prior art—not as MCRP inventions. Relevant examples include [SCITT’s transparency-service architecture](https://www.rfc-editor.org/rfc/rfc9943.html), [OpenID Federation](https://openid.net/specs/openid-federation-1_0.html), [DocMaps](https://docmaps.knowledgefutures.org/), [ORCID peer-review records](https://support.orcid.org/hc/en-us/articles/360006971333-Peer-Reviews), [ROR organization identifiers](https://ror.org/about/), [Nanopublications](https://nanopub.net/), [Trusty URIs](https://trustyuri.net/), and COAR’s [publish-review-curate model](https://coar-repositories.org/what-we-do/repositories-and-publishing/). MCRP’s proposal is to test how such ingredients might be composed while keeping proposal, evidence, and disposition visibly distinct.

## Scenario 1: the review ring

Suppose six accounts repeatedly endorse one another’s computational claims. Each has a valid key, a plausible profile, and a record containing signed reviews. An automated policy projects “three positive independent reviews” and routes a manuscript toward release. The signatures are authentic, but four accounts share one employer, two are operated by the same person, and every review cites the same unverified output.

A mitigation stack could require typed identity and competency claims, disclose control principals and conflicts, calculate quorums across declared trust domains rather than raw keys, and preserve newcomer routes that do not depend on inherited prestige. Rate limits and anomaly reports could flag unusually reciprocal reviewing. The routing policy and its inputs should be reproducible, while any anomaly score remains an automated observation—not a misconduct finding.

Residual risk remains substantial. Undeclared coordination can cross institutions; competency credentials can encode incumbent advantage; and anomaly detection can burden small specialties whose legitimate collaboration graphs are dense. The safe disposition may be `unknown independence`, followed by human review, rather than automatic rejection or acceptance.

## Scenario 2: the captured registry

Imagine that a community accepts reviewer-role credentials from three registries. The interfaces look independent, but one vendor operates all three and quietly changes eligibility rules after a dispute. Old credentials remain replayable, revocations are selectively delayed, and the projected policy view still labels affected reviews “authorized.”

Mitigations include explicit registry ownership metadata, versioned acceptance contracts, independent monitors or witnesses, exportable signed records, fork rights, short-lived credentials where appropriate, and public evidence of policy or revocation changes. Transparency practice such as [SCITT](https://www.rfc-editor.org/rfc/rfc9943.html) informs the logging model, but logging is not adjudication. Where a disposition depends on an attestation, its binding must be recorded exactly as `(claim version, acceptance-contract version, evidence-set digest, release digest, role, decision)`.

The residual risks are controller collusion, witness concentration, discovery denial, key compromise, and communities lacking resources to operate a fork. Export rights can preserve technical exit while leaving social recognition concentrated. The framework must therefore avoid describing these controls as capture resistance.

## Scenario 3: retaliation by disclosure

Transparency can itself become an attack. Consider an early-career researcher who privately challenges a senior collaborator’s data-handling claim. If the event network publishes the challenger’s identity, institutional affiliation, timestamps, and relationship graph, the signed record may enable professional retaliation even when the challenge is scientifically appropriate.

Possible mitigations include role-separated pseudonyms, delayed or selective disclosure, private conflict declarations, access-controlled evidence, redacted public projections, and an appeal path handled by qualified humans. The system can publish that an authorized challenge exists without publishing every relationship needed to verify authorization. Disclosure policies should be versioned and inspectable.

Residual risk cannot be removed. Writing style, timing, specialist knowledge, or a small candidate pool may re-identify the challenger. Restricted reviewers may abuse privileged access. Redaction can also make accountability harder. Privacy and auditability are competing outcomes to measure, not a single dial that architecture can optimize universally.

## A worked disposition example

A simulation report proposes that parameter set P should become the default for a shared analysis. The report is a proposal, not evidence that P is scientifically preferable. Two automated replication agents rerun the supplied workflow. One reproduces the headline value; the other reports a dependency mismatch. Those reports are evidence-bearing observations, not votes.

A policy projection finds one favorable domain-qualified review, one unresolved technical challenge, and no demonstrated independence between the author and favorable reviewer. It outputs `not ready: independence unknown; challenge unresolved`. A qualified human panel inspects the signed artifacts, records the evidence-set digest, and decides to request a new independent run rather than accept or reject P. The event network then links the proposal, both agent reports, the challenge, the policy projection, and the human decision without rewriting any one of them into another type. If the acceptance contract later changes, the earlier disposition remains bound to its original contract version rather than being silently reinterpreted.

## Limitations

These scenarios do not demonstrate that the proposed mitigations work, scale, or improve scientific practice. They omit jurisdictional differences, labor costs, accessibility, long-term key custody, coercion, informal prestige, and the unequal capacity of communities to monitor infrastructure. Content addressing can expose tampering without establishing truth. Identifiers can reduce ambiguity without proving identity or independence. Transparency can reveal rule changes while also creating privacy hazards.

MCRP is not a journal replacement, and a living event network must not become an automated court. Its useful boundary is narrower: preserve typed, inspectable relationships among proposals, evidence, reviews, challenges, and human dispositions while making uncertainty and policy provenance harder to hide.

Part 12 closes the sequence by turning these architectural concerns into concrete, preregistered trials. It will specify proposed hypotheses, baselines, measures, thresholds, and stop rules across usability, epistemic, governance, privacy, and systems outcomes. The next trials should include a synthetic review-ring exercise, a registry-control and revocation simulation, and a disclosure-red-team study. Results that cross a proposed harm threshold will stop or narrow the corresponding mechanism; they will not be reframed as evidence that the larger vision has already been validated.
