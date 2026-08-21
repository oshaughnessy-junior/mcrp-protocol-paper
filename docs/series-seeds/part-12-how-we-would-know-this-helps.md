---
artifact_role: outward-facing-blog-seed
authors: [Codex, junior]
status: mature-private-draft
date: 2026-08-21
series_part: 12
publication_status: private-not-approved
---

# How we would know this helps

A richer protocol is not an improvement merely because it records more structure. MCRP could increase review burden, expose sensitive relationships, privilege technically sophisticated communities, or replace legible editorial judgment with opaque policy machinery. This final part therefore turns the sequence from design argument to proposed trials.

## From threat models to tests

Part 11 examined three governance failures that Part 12 must make testable.

In a **review-ring** scenario, coordinated identities repeatedly attest to one another’s work. Relevant prior art includes the original [Sybil attack analysis](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/), [ORCID peer-review records](https://support.orcid.org/hc/en-us/articles/360006971333-Peer-Reviews), and organization identifiers from [ROR](https://ror.org/about/). Proposed mitigations include visible relationship declarations, diversity-sensitive policy views, rate limits, and audits by qualified humans. The residual risk is that apparently independent identities may share undisclosed control or incentives.

In a **captured-registry** scenario, a registry or federation operator suppresses, delays, or selectively labels records. Proposed mitigations include replicated event logs, signed checkpoints, exportable records, competing discovery services, and explicit issuer policies informed by [OpenID Federation](https://openid.net/specs/openid-federation-1_0.html) and the transparency architecture described by [SCITT RFC 9943](https://www.rfc-editor.org/rfc/rfc9943.html). The residual risk is unequal visibility: a formally portable record can remain practically obscure if dominant interfaces exclude it.

In **retaliation by disclosure**, review metadata reveals a vulnerable critic, collaborator, or institution. Proposed mitigations include selective disclosure, delayed release, role separation, minimal retention, and human review of risky publication paths. The residual risk is inferential: timing, topic, and network structure may re-identify someone even when direct identifiers are withheld.

These mappings do not establish capture resistance. They specify adversarial conditions, candidate mitigations, and harms that trials must measure. Part 11 asked how MCRP could fail; Part 12 asks what observations would justify continuing, narrowing, or stopping.

## What is being evaluated

MCRP treats trust registries, transparency services, decentralized notifications, identifiers, content-addressed assertions, and publish–review–curate as guiding prior art—not MCRP novelty. Relevant foundations include [COAR’s publish–review–curate model](https://coar-repositories.org/what-we-do/repositories-and-publishing/), [DocMaps](https://docmaps.knowledgefutures.org/), [Nanopublications](https://nanopub.net/), and [Trusty URIs](https://trustyuri.net/).

The proposed contribution is an experiment in composing those ideas into a living, self-updating event network. At scale, automation may ingest events, deduplicate records, traverse dependencies, notify subscribers, and project declared policies. Qualified humans retain scientific authority. Automated observations, policy projections, and agent reports cannot silently become scientific dispositions.

A portable acceptance attestation, where used, must bind exactly:

`(claim version, acceptance-contract version, evidence-set digest, release digest, role, decision)`

That record reports who decided what, under which contract and evidence boundary. It does not turn a proposal into evidence or an acceptance into truth. Proposed claims, observed evidence, automated reports, and human dispositions remain distinct record types.

## A fully worked trial example

Suppose a team releases claim C7: “Calibration method M keeps detector bias below 2% for dataset D.” Release R1 links the claim to code, D version 4, a calibration report, and an acceptance contract requiring two independent domain reviews plus a reproducibility check.

The trial operators deliberately introduce three events. First, reviewer A finds that one frequency band was excluded without justification. Second, D version 5 changes a dependency used by the calibration. Third, an automated agent reports that a figure cannot be regenerated.

In MCRP, each event is recorded separately. A’s signed review proposes rejection of C7 under the stated contract. The dependency event marks the existing disposition as potentially stale and routes notices to subscribers. The agent report remains an observation requiring qualified human interpretation. Reviewer B confirms the exclusion defect; a reproducibility reviewer determines that the figure failure came from an optional plotting package and does not independently decide C7’s scientific status. A qualified decision-maker then records a scoped rejection against the exact tuple above.

The comparison baseline receives the same release, injected events, reviewer effort, and notification window through a repository with ordinary open-review records. Evaluators measure whether participants locate the exclusion, notice the dependency change, distinguish the plotting failure from the scientific defect, identify uncovered scope, and explain the final disposition. This example tests record behavior; it does not presume MCRP performs better.

## Proposed preregistration

Every threshold below is prospective and proposed, not established.

| Outcome | Hypothesis | Baseline | Measure | Proposed threshold and rule |
|---|---|---|---|---|
| Usability | Participants can interpret scoped records without excessive burden. | Repository plus open review; existing publish–review–curate workflow. | Task completion, interpretation errors, median time, workload survey, newcomer completion gap. | Narrow if interpretation errors exceed either baseline or median task time is >25% higher without a predeclared epistemic benefit. |
| Epistemic | Portable records help localize seeded defects and expose uncovered scope. | Same releases, defects, resources, and reviewers. | False acceptance, defect localization, uncovered-scope identification, stale-decision detection, correction recovery. | Stop the evaluated configuration if false acceptance is higher than both baselines; narrow if no primary epistemic measure exceeds the stronger baseline by the preregistered margin. |
| Governance | Plural policy views remain explainable under coordination and registry capture. | Conventional editorial decision log and open-review record. | Review-ring alerts, explanation accuracy, suppressed-event detection, appeal completion, concentration by issuer. | Stop automated disposition routing after any unexplained disposition; narrow if capture simulations remain undetected in >10% of planned trials. |
| Privacy | Review routing does not create unacceptable disclosure or retaliation risk. | Baseline disclosure practices with equivalent review tasks. | Direct disclosure, re-identification attempts, harassment reports, participant withdrawal, privacy review. | Stop the affected trial after one severe disclosure or credible retaliation event; narrow metadata and routing if re-identification exceeds the predeclared baseline rate. |
| Systems | The event network operates within declared bounds under load and disruption. | Simple event log and notification queue. | Ingestion, deduplication, traversal, fan-out, recomputation latency, checkpoint recovery, partition behavior, delayed-delivery reconciliation. | Narrow scale or topology if records are lost, duplicated decisions become authoritative, or recovery exceeds the preregistered service bound. Systems success alone cannot continue the program. |

Trials should also report reviewer agreement, time, cost, accessibility, and results by participant experience. Equivalent resources matter: additional staffing or bespoke integration must be counted rather than hidden as protocol performance.

## Limitations

Seeded defects may not represent live scientific disputes. Small trials cannot characterize field-wide incentives, long-term retaliation, institutional capture, or operational scale. Reviewer agreement can reflect shared blind spots. Privacy tests cannot enumerate every inference attack. Baselines also evolve, and implementation quality may dominate protocol differences.

Most importantly, a policy projection is not a scientific judgment, and a successful systems benchmark is not evidence of epistemic value. No result here would justify claims of truth, adoption, validation, convergence, journal replacement, capture resistance, or general improvement.

## Concrete next trials

The sequence closes with four bounded trials: one defect-localization comparison using the worked example; one review-ring simulation with controlled identities; one captured-registry partition and export exercise; and one retaliation-by-disclosure tabletop reviewed by affected participant groups. Each trial should publish its preregistration, fixtures, redacted event records, deviations, and negative findings.

Continue only configurations that meet their proposed domain-specific thresholds without triggering a stop rule. Narrow components that help independently—such as content-addressed review records or stale-decision notices—and discard machinery whose cost or risk is not justified. The responsible next step is small interoperable testing, with automation serving a living event network and qualified humans retaining authority over scientific dispositions.
