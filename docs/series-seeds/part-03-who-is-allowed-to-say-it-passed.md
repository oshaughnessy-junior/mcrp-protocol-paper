---
artifact_role: outward-facing-blog-seed
authors: [Codex, junior]
status: mature-private-draft
date: 2026-08-21
series_part: 3
publication_status: private-not-approved
---

# Who is allowed to say it passed?

A green check records an event. It does not establish independence, competence, authorization, or scientific adequacy.

Scientific workflows often compress unlike judgments into one success state. An author’s script completed. A hosted service reconstructed the outputs. A statistician judged the model appropriate. A domain reviewer accepted the interpretation. These statements answer different questions. None should silently inherit another’s authority.

MCRP therefore proposes separating author evidence, automated observation, reviewer-controlled execution, policy projection, and qualified scientific disposition. This is a proposal about representing their boundaries, not evidence that a particular authorization policy works in practice. Trust registries, transparency services, decentralized notifications, persistent identifiers, content-addressed assertions, and publish-review-curate workflows are established guiding prior art—not MCRP novelties. Relevant foundations include [W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model-2.0/), the [SCITT architecture](https://www.rfc-editor.org/rfc/rfc9943.html), [Linked Data Notifications](https://www.w3.org/TR/ldn/), [Activity Streams](https://www.w3.org/TR/activitystreams-core/), [WebSub](https://www.w3.org/TR/websub/), [COAR Notify](https://coar-notify.net/specification/1.0.1/), and the established [publish-review-curate model](https://coar-repositories.org/what-we-do/repositories-and-publishing/).

## Passing is not one predicate

A useful interface should state what happened before displaying who endorsed it.

| Layer | Example statement | Possible issuer | What it does not establish |
|---|---|---|---|
| Observation | “The declared command exited successfully and produced files with these digests.” | Execution service or agent | Correctness of the procedure or interpretation |
| Procedure | “The estimator, uncertainty calculation, and diagnostic thresholds match the declared contract.” | Methods reviewer | Domain relevance or adequacy of the scientific conclusion |
| Authority | “This person was eligible under policy P, version 4, to issue a methods decision for this claim.” | Registry or authorization service | Competence beyond the policy’s criteria, independence, or correctness |
| Scientific disposition | “Given the cited evidence and stated scope, I accept this claim in a qualified scientific role.” | Qualified human reviewer | Universal truth, permanence, or acceptance of adjacent claims |

An automated service can report observations at scale. An agent can compare artifacts with an acceptance contract, summarize discrepancies, or project what a declared policy would appear to permit. Those reports may help a human reviewer, especially in a living, self-updating event network. They cannot silently become scientific dispositions. Qualified humans retain scientific authority and must explicitly adopt, reject, narrow, or defer the machine-produced material.

Where a decision is attested, the binding must identify exactly `(claim version, acceptance-contract version, evidence-set digest, release digest, role, decision)`. The record should also expose scope, exclusions, issuer identity, applicable policy, provenance, status, and any later superseding event. Binding the versions prevents a favorable decision about one release from drifting onto a modified claim or evidence set.

## Worked example: one report, three bounded decisions

Suppose a paper makes three claims about a new risk model:

1. **C1:** the released code reconstructs Figure 2 from the declared dataset;
2. **C2:** the reported confidence intervals have adequate coverage under the stated simulation design;
3. **C3:** the model supports clinical deployment in adults over 65.

An execution agent runs the declared environment and produces report `R17`. It records that Figure 2 was reconstructed within the contract’s numerical tolerance, that 10,000 simulation trials completed, and that coverage was 93.8% against a required 94.0–96.0% interval. It also notes that the supplied evidence contains no prospective clinical evaluation. This is an agent-authored report: useful, inspectable, and content-addressed, but not a scientific approval.

A human methods reviewer examines `R17`, the scripts, diagnostics, and simulation design. She explicitly adopts the reconstruction observation for C1 and issues “accepted within declared numerical tolerance.” For C2, she adopts the measured coverage but not the agent’s suggested disposition; she issues “not accepted under contract version 3 because observed coverage falls below its lower bound.” She excludes C3 because clinical deployment lies outside her methods-review role.

A human domain reviewer then examines C3. He cites `R17` only for the absence of prospective evidence and issues “deferred: current evidence does not address deployment safety or utility in the named population.” He does not reinterpret successful reconstruction of Figure 2 as clinical support.

The resulting state is not a single pass badge:

- C1 has a favorable, scoped methods disposition tied to one release and tolerance contract.
- C2 has a negative methods disposition despite successful execution.
- C3 remains deferred by a qualified domain reviewer and outside the methods reviewer’s scope.

The agent’s observations remain attributable to the agent. The human decisions identify which portions were adopted and how they were bounded. If the simulation or clinical evidence changes, new events can refer to the prior records without rewriting what those reviewers decided at the time.

## Identity, role, and independence

Portability requires the target, schema, issuer identity, evidence references, signature, and current status to be independently resolvable. Systems such as [OpenID Federation](https://openid.net/specs/openid-federation-1_0.html), [ORCID peer-review records](https://support.orcid.org/hc/en-us/articles/360006971333-Peer-Reviews), [ROR](https://ror.org/about/), and [CRediT](https://credit.niso.org/) provide useful prior art for representing organizational relationships, review activity, institutions, and contributor roles. [DocMaps](https://docmaps.knowledgefutures.org/) offers a model for describing editorial and review events.

Yet a signature establishes attribution and integrity, not competence or independence. Different servers, accounts, agents, or credentials may remain under common control. The classic [Sybil attack](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/) shows why multiplying identities is not equivalent to multiplying independent actors. MCRP should therefore preserve evidence about affiliations, selection procedures, conflicts, role qualifications, and policy versions rather than reducing independence to an identity count.

Content-addressed forms such as [Nanopublications](https://nanopub.net/) and [Trusty URIs](https://trustyuri.net/) are relevant for making assertions and references precisely identifiable. They do not decide whether an assertion is scientifically adequate. That decision remains a separately attributable act.

## Limitations

This separation does not validate an authorization policy, certify reviewer competence, reveal undisclosed coordination, or determine which qualifications a community should require. Machine-readable roles can reproduce institutional errors. Transparency can expose declared relationships without discovering hidden ones. Revocation and supersession signals may arrive late or be unavailable. Human review can also be mistaken, inconsistent, or incomplete.

MCRP’s narrower proposal is to prevent these uncertainties from being erased by a generic success state. Automation may maintain a large event network and surface changes, but it must preserve the line between observation, policy projection, agent report, and human scientific disposition.

That line makes approval precise, but precision is not permanence. Evidence changes, methods are corrected, credentials expire, and policies are revised. Part 4 asks how an approval can remain historically true as an event without being presented as currently reliable.
