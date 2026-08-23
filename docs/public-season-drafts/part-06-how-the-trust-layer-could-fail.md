---
artifact_role: outward-facing-blog-draft
authors: [Codex, junior]
status: mature-private-draft
date: 2026-08-23
series: Making Computational Review Version-Specific
series_part: 6
publication_status: private-not-approved
audience:
  - security and privacy reviewers
  - scholarly-infrastructure decision-makers
  - research-methods evaluators
  - funders and protocol designers
reader_utility: derive bounded experiments and stop conditions from trust-layer threats before investing in scale
operational_artifact: threat-to-test decision matrix
evidence_status: prospective threat model and evaluation plan; no demonstrated mitigation effectiveness
source_drafts: [part-11-how-the-trust-layer-fails, part-12-how-we-would-know-this-helps]
future_cross_list_slot: internal web/iOS MCRP protocol prototype; unscheduled and not evidence for this post
---

# How this trust layer could fail—and how we would test it

_Making Computational Review Version-Specific, 6 of 6_  
_By Codex and junior_

Decentralization can distribute failure as readily as authority.

A signed review can come from a conflicted reviewer. Three apparent registries can share one controller. A transparent relationship graph can expose a vulnerable critic. An append-only log can preserve misinformation perfectly. None of these is a corner case; each follows from mistaking cryptographic integrity for scientific trust.

MCRP is therefore not ready to claim that a distributed review network improves science. The responsible next step is to turn its most dangerous assumptions into bounded tests with baselines, measurable harms, and stop rules.

Automation remains useful within that boundary. Agents can verify signatures, traverse dependencies, execute declared workflows, route notices, and produce discrepancy reports. They cannot silently decide that a reviewer is independent, a challenge is resolved, or a scientific claim is warranted.

## Three failures to design for first

### 1. The review ring

Six accounts repeatedly endorse one another. Every signature is valid and each profile looks plausible. A routing policy observes three favorable “independent” reviews and advances a release. In reality, several accounts share an employer, two share an operator, and all reports rely on the same unverified output.

Possible controls include conflict and control-principal disclosures, quorums across declared trust domains rather than raw keys, reciprocal-review alerts, and qualified-human escalation. None proves independence. Small specialties may have legitimately dense collaboration graphs, so anomaly detection can also punish the communities it is meant to protect.

### 2. The captured registry

A community recognizes reviewer credentials from three registries. One vendor operates all three and changes eligibility rules after a dispute. Revocations are selectively delayed, old credentials remain replayable, and dominant discovery interfaces hide challenges.

Possible controls include ownership metadata, signed policy versions, exportable records, independent witnesses, short-lived credentials, competing discovery services, and fork rights. Technical exit does not guarantee social visibility. A community may be able to export its records and still be unable to carry its recognition elsewhere.

### 3. Retaliation by disclosure

An early-career researcher challenges a senior collaborator’s data-handling claim. Publishing the challenger’s identity, affiliation, timing, and relationship graph enables retaliation even if the scientific challenge is sound.

Possible controls include selective disclosure, accountable pseudonyms, delayed publication, access-controlled evidence, redacted public views, and an appeal route. Re-identification may still be possible through writing style, timing, specialist knowledge, or a small candidate pool. More transparency is not always safer.

## Operational artifact: threat-to-test decision matrix

The values below are categories and decision rules, not validated effect sizes.

| Threat | Proposed mitigation to test | Comparison | Measure | Stop or narrow rule |
|---|---|---|---|---|
| Review ring or Sybil identities | Relationship declarations, domain-diverse quorum, reciprocal-review alerts, human escalation | Raw signature count and conventional reviewer log | False authorization, ring detection, false accusation, newcomer exclusion, explanation accuracy | Stop automated disposition routing after any unexplained authoritative transition; narrow controls that increase false accusations or exclusion without detecting seeded rings |
| Captured registry or selective federation | Signed policies and checkpoints, ownership disclosure, export, competing discovery, witness comparison | Single registry and ordinary editorial record | Suppressed-event detection, revocation latency, export fidelity, view reproducibility, recovery after partition | Stop if a valid challenge or revocation can be silently omitted from an allegedly complete view; narrow any topology that cannot state its completeness boundary |
| Retaliation or deanonymization | Selective disclosure, accountable pseudonymity, metadata minimization, human privacy review | Existing disclosure practice for equivalent tasks | Direct disclosure, re-identification, withdrawal, reported intimidation, auditability loss | Stop the affected exercise after a severe disclosure or credible retaliation event; reduce metadata and access before resuming |
| Review burden and opacity | Typed work requests, compact views, explicit exclusions, accessibility support | Repository plus open review or current local workflow | Completion, interpretation error, time, workload, uncovered scope, newcomer gap | Narrow if burden rises without a preregistered epistemic or governance benefit; stop configurations users cannot explain |
| Dependency and event failure | Stable identities, idempotent ingestion, checkpoints, explicit unknown/stale states | Simple event log and notification queue | Lost events, duplicate authority, impact precision, recovery, reconciliation latency | Stop if records are lost or duplicates become authoritative; reduce scope if recovery cannot meet a declared service bound |

Each experiment needs preregistered fixtures, equivalent resources, credible baselines, severity definitions, and an independent safety review. Numerical margins and sample sizes should be set with domain and study-design expertise. They should not be invented to make the architecture look testable.

## A bounded comparative exercise

Consider claim C7: “Calibration method M keeps detector bias below 2% for dataset D.” The release links the claim to code, data version 4, a calibration report, and acceptance conditions requiring independent domain reviews plus a reconstruction check.

Trial operators introduce three events: a reviewer finds that one frequency band was excluded without justification; data version 5 changes a calibration dependency; and an agent reports that a figure cannot be regenerated.

The protocol must keep them separate. The reviewer’s finding is a scoped scientific challenge. The dependency event marks existing standing as potentially stale. The agent’s failure is an observation requiring interpretation. A second reviewer may confirm the exclusion while an execution reviewer determines that the plotting failure came from an optional package and does not decide the calibration claim.

Compare this workflow with a repository plus ordinary open-review records using the same release, defects, reviewers, resources, and notification window. Measure whether participants locate the exclusion, notice the dependency change, distinguish presentation failure from scientific defect, identify uncovered scope, and explain the final disposition. Also measure time, burden, accessibility, privacy, and handoff loss.

The trial should be allowed to show that MCRP adds cost without benefit.

## What is established, proposed, and evidenced

**Established prior art.** The original [Sybil attack analysis](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/) explains why apparent identity count does not establish independent participation. [SCITT RFC 9943](https://www.rfc-editor.org/rfc/rfc9943.html) and [OpenID Federation](https://openid.net/specs/openid-federation-1_0.html) provide relevant transparency and federation foundations. [ORCID](https://support.orcid.org/hc/en-us/articles/360006971333-Peer-Reviews) and [ROR](https://ror.org/about/) supply identity and organization context. None of these systems guarantees competence, independence, fair governance, or scientific truth.

**MCRP proposal.** The proposed contribution is to compose exact scientific releases, prospective acceptance conditions, scoped review attestations, dependency-sensitive freshness, plural policy views, and event-driven automation under conservative authority rules.

**Current evidence.** No evaluation demonstrates that this composition improves review, operates at web scale, converges across institutions, resists capture, protects vulnerable reviewers, or outperforms simpler alternatives. The matrix is an evaluation agenda.

## What remains open

The largest unknowns are social and empirical. Communities may not agree on roles, evidence, or independence. Security controls can centralize power. Privacy protections can reduce accountability. Review work may become more bureaucratic. Small trials cannot reproduce long-term prestige, coercion, retaliation, or institutional capture. Systems performance cannot substitute for epistemic value.

The series should therefore end with a choice, not a promise: build the smallest interoperable exercise, publish negative findings, retain components that help independently, and discard machinery whose cost or risk is not justified.

## Future cross-list slot: a separate prototype

A separate internal web/iOS MCRP protocol prototype may later provide an interface for exercising record binding, review requests, event exchange, and policy views. That work has its own scope and release timeline. It is not a dependency of this series, has not produced results cited here, and should be cross-listed only after an independent review confirms what it actually implements and tests.

Until then, the claims remain deliberately modest: exact review objects may make important boundaries more inspectable; automation may help maintain a living event network; and qualified humans must remain accountable for scientific dispositions.

