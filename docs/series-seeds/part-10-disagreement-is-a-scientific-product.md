---
artifact_role: outward-facing-blog-seed
authors: [Codex, junior]
status: mature-private-draft
date: 2026-08-21
series_part: 10
publication_status: private-not-approved
---

# Disagreement is a scientific product

Consensus is useful for decisions, but it is a destructive storage format for scientific disagreement.

Two reviewers may inspect the same release and produce statements that are both competent and incompatible. One finds that a method supports a narrow claim under a stated assumption. Another produces counterevidence outside that range. A third fails to reproduce one output but lacks access to restricted inputs. Reducing these records to “two votes for, one against” discards the scopes, methods, and access conditions that a future reviewer needs.

MCRP should preserve relations such as `supports`, `bounds`, `contradicts`, `fails-to-reproduce`, `narrows`, and `unassessed`. Each disposition targets an exact claim version and identifies its evidence, method, scope, exclusions, and acceptance contract. Where a reviewer or adjudicator attests to a disposition, the binding is `(claim version, acceptance-contract version, evidence-set digest, release digest, role, decision)`. The binding does not prove that the decision is correct. It specifies what was evaluated, under which rules, by whom in a declared role, and with what result.

This proposal builds on established guiding prior art rather than claiming novelty for its components. [W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model-2.0/) describes signed, attributable claims; [SCITT](https://www.rfc-editor.org/rfc/rfc9943.html) specifies transparency services for signed statements; [Nanopublications](https://nanopub.net/) and [Trusty URIs](https://trustyuri.net/) demonstrate granular assertions and content-addressable references. [Linked Data Notifications](https://www.w3.org/TR/ldn/), [Activity Streams](https://www.w3.org/TR/activitystreams-core/), [WebSub](https://www.w3.org/TR/websub/), and [COAR Notify](https://coar-notify.net/specification/1.0.1/) provide relevant notification and event patterns. The [COAR publish-review-curate model](https://coar-repositories.org/what-we-do/repositories-and-publishing/) is likewise guiding prior art for connecting repository publication with review and curation. MCRP’s proposal is a particular scientific workflow assembled around these ideas: automation at scale maintains a living, self-updating event network, while qualified humans retain scientific authority.

## A worked disagreement timeline

Consider claim `C17-v3`: “Treatment T reduces the twelve-month event rate by at least 10% for adults with condition X.” Its acceptance contract `AC4-v2` requires a preregistered analysis, specified covariate handling, confidence-interval bounds, and subgroup checks defined before review. Release `R9` contains the manuscript, analysis code, and a public evidence subset; protected clinical records remain in a controlled environment.

1. **Publication event.** The authors publish `C17-v3`, `AC4-v2`, and `R9`. Their digests become stable targets in the event network. Publication is a proposal for assessment, not an accepted disposition.

2. **Support event.** Reviewer A executes the declared analysis against the controlled evidence and reports `supports`, limited to the aggregate population. The report cites the executable method, environment description, exclusions, and evidence-set digest.

3. **Challenge event.** Reviewer B observes that one measurement device systematically rounds values for participants over age 70. B publishes a `bounds` challenge: the aggregate estimate may remain compatible with the contract, but the claim’s unrestricted population language is not supported for that subgroup. The challenge includes a diagnostic table derived under the data-use agreement; it does not expose patient-level records.

4. **Restricted-access reproduction event.** Reviewer C cannot access the protected records and cannot reproduce the subgroup diagnostic from the public subset. C records `unassessed`, not `fails-to-reproduce`. Access limitations remain part of the event rather than being silently converted into negative evidence.

5. **Author response event.** The authors acknowledge the device issue, publish analysis release `R10`, and propose `C17-v4`: “Treatment T reduces the twelve-month event rate by at least 10% for adults aged 18–70 with condition X under the specified measurement protocol.” They also register a separate claim about participants over 70 as unresolved.

6. **Adjudication event.** A qualified adjudicator applies `AC4-v2` to the original materials and records that B’s challenge is upheld in scope. The adjudicator narrows the standing of `C17-v3`; the decision neither deletes A’s aggregate result nor represents C’s access-limited report as scientific opposition.

7. **Policy-view update.** A downstream service recomputes its display. Under one policy, `C17-v3` appears as superseded and bounded; `C17-v4` appears pending review. Another community may apply a stricter subgroup rule and leave both unaccepted. Each view identifies its policy version and source events.

The worked example preserves proposal, evidence, observation, and disposition as different objects. Automated agents may detect the rounding pattern, project how a policy would classify the event, route notifications, and update indexes. Those outputs remain observations, projections, or agent reports until a qualified human makes the relevant scientific disposition. They cannot silently become acceptance, rejection, contradiction, or adjudication.

## Safeguards for contested records

A durable disagreement layer can also become infrastructure for retaliation or harassment. Identity and role assertions may draw on systems such as [ORCID peer-review records](https://support.orcid.org/hc/en-us/articles/360006971333-Peer-Reviews), [ROR](https://ror.org/about/), [CRediT](https://credit.niso.org/), or federation metadata, but identity alone is not credibility. Conversely, compulsory public identity can endanger junior researchers, whistleblowers, patients, or reviewers challenging powerful institutions.

MCRP should therefore support confidential review identities with accountable disclosure procedures. A challenge may expose a stable pseudonymous reviewer reference while an authorized steward retains the confidential role evidence. Public records should contain the minimum information needed to inspect the scientific argument. Restricted datasets, personal information, embargoed results, and security-sensitive methods require access-controlled evidence references, redacted derivatives, and explicit statements of what an adjudicator could inspect.

Low-cost abusive challenges require procedural friction that does not erase legitimate dissent. A receiving policy can require a target claim version, a typed relation, a scope statement, a method or rationale, declared conflicts, and a rate-limited deposit or accountable sponsor. Duplicate and coordinated challenges may be clustered for triage without being counted as independent evidence. Moderators may quarantine threats, doxxing, fabricated citations, or repetitive content while retaining a content-addressed audit record accessible under appropriate governance. Appeals should be possible, and moderation actions should name their policy version and reason.

The [Sybil attack](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/) establishes why many apparent identities cannot automatically be treated as many independent participants. MCRP should not translate volume into scientific weight. Nor should it assume that transparency prevents institutional capture, selective indexing, retaliation, or coordinated abuse. Preserved dissent is not necessarily credible dissent, and adjudication does not make conflict disappear.

## Limitations

This design does not determine which scientific conclusion is true. It does not ensure fair participation, reliable adjudicators, complete evidence, safe disclosure, or consistent policies across communities. Confidentiality can limit public verification; transparency can expose vulnerable participants; anti-abuse controls can burden legitimate challengers. Human qualification and institutional standing may themselves be disputed. A living event network can preserve and route these disputes, but its records remain dependent on the quality, incentives, access, and governance of their producers.

The next numbered part turns from representational integrity to adversarial operation: Part 11 examines how trust registries, transparency services, decentralized notifications, and automated review workflows can be manipulated—and what failure containment must exist before communities rely on them.
