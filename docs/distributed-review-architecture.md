---
artifact_role: architecture-sketch
authors:
  - Codex
  - junior
status: working-draft
date: 2026-08-16
scope: distributed-review-compatible MCRP and federated trust layer
claim_posture: proposed-not-validated
---

# From version-specific review to distributed scientific trust

## Executive judgment

MCRP's natural next step is not a larger provenance graph or an original trust-server design. Existing work on signed claims, transparency services, decentralized notifications, review-event exchange, scholarly identifiers, and distributed assertions supplies the guiding infrastructure and motivation. MCRP's role is to make the Scientific Record Release (SRR) and every review event precise enough that those systems can automate scientific review coordination at scale.

The immediate guides include [W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model-2.0/) for signed claims, [IETF SCITT](https://www.rfc-editor.org/rfc/rfc9943.html) and [Sigstore Rekor](https://docs.sigstore.dev/logging/overview/) for transparent statement registration, [Linked Data Notifications](https://www.w3.org/TR/ldn/), [Activity Streams 2.0](https://www.w3.org/TR/activitystreams-core/), [WebSub](https://www.w3.org/TR/websub/), and [COAR Notify](https://coar-notify.net/specification/1.0.1/) for decentralized event delivery, and [Nanopublications](https://nanopub.net/) for content-addressed distributed assertions. MCRP should profile and connect these systems, not claim to originate them.

The larger target is a **distributed-review-compatible science framework** with four separable planes:

1. **Scientific records:** immutable releases containing versioned claims, evidence, executions, dependencies, and prospective acceptance contracts.
2. **Attestations:** typed, scoped, signed statements about exact records, claims, reviews, contributions, identities, and conflicts.
3. **Trust nodes:** federated services that may register, resolve, archive, replicate, index, or help users discover those statements while advertising which capabilities and retention commitments they actually provide.
4. **Trust views:** transparent, community- or user-specific policies that compute a current interpretation without rewriting the underlying history.

The target is a **living, self-updating network**: new releases, executions, reviews, challenges, corrections, dependency changes, and credential events automatically trigger bounded validation, indexing, impact analysis, policy recomputation, notifications, and new review tasks. “Self-updating” means the network updates its records and derived views from signed events; it does not mean that software silently grants scientific authority or rewrites human judgments.

This is an architectural hypothesis, not a demonstrated system. MCRP has not yet shown interoperability, web-scale automation, convergence, security, usable governance, improved review, or resistance to institutional capture.

## The central invariant

There is no globally authoritative `accepted=true`. A release can still have a historical MCRP lifecycle transition such as `human-approved` under one exact acceptance contract and authority boundary. That is distinct from a community endorsement, a current derived trust view, and a user's decision to rely on the result.

The strongest valid form is:

> Under policy P, trust roots T, visible event set E, and observation time t, this exact release satisfies these requirements for these claims.

A signature establishes attribution and integrity. A registry receipt establishes that a statement was registered. A credential can establish that an issuer made an identity or competency claim. None of these establishes scientific truth, adequate review, independence, or legitimacy by itself.

## System layers

### 1. Immutable scientific objects

The current MCRP core remains stable:

- claim and acceptance-contract versions;
- evidence and counterevidence;
- artifacts and manifests;
- executions, environments, configurations, and provenance;
- SRRs and successor manifests;
- claim mappings such as `unchanged`, `revised`, `split`, `merged`, `narrowed`, `broadened`, and `retired`.

Objects are content-identified and may be hosted or mirrored anywhere. A trust node does not own their scientific meaning.

### 2. Review work objects

Review must itself become an inspectable product. Candidate objects are:

- **review request:** target SRR, claims, questions, required competencies, method, conflict policy, confidentiality, resources, deadline, and completion rule;
- **review scope:** the claims, evidence paths, executions, methods, or scientific questions actually covered;
- **review report:** findings, method, evidence inspected, limitations, exclusions, and unresolved questions;
- **verification report:** machine checks or reviewer-controlled executions and their exact observations;
- **challenge:** counterevidence or a scoped objection to a record or earlier attestation;
- **adjudication:** a policy-bound response that may uphold, reject, or narrow a challenge without deleting either side;
- **receipt:** evidence that a named review process received or registered a particular object.

A review report should be a citable, immutable research object, not prose floating next to a mutable manuscript.

A separate **contribution assertion** should bind an actor and role to an exact object or change, record provenance and delegated agent participation, and permit adoption, challenge, correction, or withdrawal. Contribution credit and scientific trustworthiness remain separate derived views.

### 3. Typed attestations

An attestation must strictly extend, not weaken, MCRP's existing binding to `(claim version, acceptance-contract version, evidence-set digest, release digest, role, decision)`. It should additionally name:

- identifier, schema, and type;
- exact SRR and optional claim versions;
- assertion or decision, scope, exclusions, and uncertainty;
- review profile or method used;
- assessment mode, outcome vector, and exact review-report digest;
- issuer identity, role, and signing key;
- competency or authorization basis;
- conflict and independence disclosures;
- governing policy and software version where material;
- issue time, expiry, and freshness conditions;
- supersession, challenge, withdrawal, or revocation targets;
- signature and zero or more node receipts.

Predicate authority is typed. Tools or agents may issue mechanically observable predicates under recorded delegation. Under current MCRP governance, scientific dispositions require a qualified human issuer; an agent recommendation is a separate predicate and cannot satisfy a human-disposition guard. Human adoption must identify the agent report examined and state the human's independent scope of responsibility.

Initial predicates may include:

- `executed-under-reviewer-control`;
- `outputs-match-declared-predicate`;
- `methods-adequate-for-claim`;
- `data-fit-for-declared-use`;
- `uncertainty-treatment-adequate`;
- `claim-supported-within-scope`;
- `claim-not-supported`;
- `material-limitation-present`;
- `independent-replication-reported`;
- `reviewer-competency-recognized`;
- `conflict-disclosed`;
- `attestation-challenged`, `superseded`, `withdrawn`, or `revoked`.

An undifferentiated vote is a lossy special case. MCRP should preserve the issuer's role, basis, scope, method, and limitations rather than turn every judgment into an up/down count.

### 4. Federated trust nodes

“Trust server” is accessible working language; **review trust registry**, **trust node**, or **review observatory** better describes the role. A node may:

1. validate signatures, schemas, target identities, scope, replay protection, and status;
2. apply a published admission and moderation policy;
3. append or reference attestations in an auditable history;
4. issue an independently verifiable inclusion receipt;
5. index releases, claims, reports, reviewers, contributors, challenges, and policies;
6. exchange notifications and selected public records with peer nodes;
7. publish signed checkpoints or equivalent audit evidence;
8. notify subscribers of challenges, staleness, supersession, and revocation;
9. compute optional, clearly labelled policy-specific views.

It must not imply that hosting equals endorsement, declare scientific truth, erase disagreement, require a blockchain, or produce a normative global reputation score.

Hosting, indexing, reviewer selection, process management, policy evaluation, curation, and scientific endorsement should remain distinguishable roles even when one organization performs several.

The original MCRP authority boundary remains mandatory for authoritative transitions. A policy result must expose the requester, issuer, node, credential issuer, policy authority, and their control principals; delegation paths; material shared dependencies; and the independence rule evaluated. Different accounts, agents, models, hostnames, or subsidiaries do not establish independence by themselves.

### 5. Community policy

A review community publishes a versioned policy defining:

- accepted identity-assurance and competency evidence;
- required reviewer roles and prohibited conflicts;
- independence and diversity constraints;
- mandatory review predicates and assessment modes;
- treatment of restricted or unavailable evidence;
- quorum or threshold logic;
- freshness windows and invalidation rules;
- challenge, correction, appeal, and abuse procedures;
- carry-forward rules for successor releases.

This policy bundle is the closest analogue to a journal's editorial standard. Mechanical portions can be executable; scientific judgments remain signed human dispositions under current MCRP rules.

### 6. Discovery and presentation

Clients may show:

- the exact record and claim scope;
- observations from verification and execution;
- supporting, limiting, and contradicting reviews;
- unresolved disputes and uncovered claims;
- contributor and reviewer histories;
- current freshness and availability;
- the trust roots, policy, inputs, and time used to compute the displayed view.

No free-floating green badge should appear without its release identity, scope, date, policy, and underlying outcomes.

## The journal analogue

Journals currently bundle archiving, discovery, review commissioning, reviewer selection, workflow control, editorial judgment, endorsement, reputation, indexing, preservation, and correction. A distributed architecture can separate these functions.

A future journal-like entity could be a recognizable review community that publishes:

- governance and membership rules;
- reviewer eligibility and conflict rules;
- named review profiles;
- signed editorial recommendations;
- curated collections of exact SRRs;
- review histories, appeals, and corrections;
- contributor and reviewer attestations;
- a durable trust-node log.

The work may remain in any compatible archive. A compute center may attest to reconstruction, a methods community to analysis quality, a disciplinary society to interpretation, and another laboratory to independent challenge. Each refers to the same immutable SRR. Existing journals can participate as respected policy authorities and curators; the architecture does not require their disappearance. Confidentiality, ethics enforcement, sanctions, appeals, legal accountability, editorial synthesis, financing, and long-term stewardship remain institutional functions that a filtered trust view does not make disappear.

The useful formula is:

> The record is preserved wherever it can remain resolvable; review may be contributed by parties whose claimed competence and independence are inspectable under a named policy; recommendations come from identifiable communities; and the underlying review evidence can be made portable.

## Trust accumulation without trust collapse

“Trustworthy reviewer” is not a scalar property. Standing is contextual across domain, method, instrument, role, time, conflict, and evidence quality. A reviewer may be excellent at numerical reconstruction and unqualified to judge clinical interpretation.

Trust nodes should preserve faceted, event-derived histories:

- identity and affiliation assurance;
- declared and independently recognized competencies;
- exact scopes reviewed;
- review method, specificity, and evidence coverage;
- challenges raised and later adjudication;
- corrections and self-withdrawals;
- conflicts and independence evidence;
- timeliness and follow-through;
- reproducibility of reviewer-generated verification;
- policy violations and credential revocations.

Applications may rank or route reviewers, but must disclose the inputs, formula, time window, exclusions, and uncertainty. Protocol objects should never contain one universal reviewer or paper score.

Trust edges should be typed—for example, `recognizes-identity`, `recognizes-competency-in`, `delegates-review-role`, `endorses-process`, `accepts-under-policy`, `challenges`, and `revokes`. Trust is not automatically transitive.

## Distributed lifecycle

1. Authors freeze and register a candidate SRR with prospective claim contracts.
2. One or more nodes index a version-specific review request.
3. The work is decomposed by claim, evidence path, execution, method, dataset, or risk.
4. Services route work using competencies, conflicts, availability, resources, and policy constraints.
5. verifiers, reviewers, and challengers issue independent reports and attestations.
6. A client or node evaluates the visible event set under a named policy.
7. A community may issue a curation attestation for that release and policy.
8. Other communities can independently endorse, narrow, challenge, or ignore the same record.
9. New evidence and procedural objections append challenges and adjudications.
10. Dependency events trigger scoped freshness and invalidation checks.
11. A successor SRR carries decisions forward only through an explicit scope-delta disposition.
12. Passing, failing, disputed, stale, superseded, and revoked histories remain inspectable.

Review products are **mergeable but not averaged**. Several reports can form a coverage view, but disagreement and uncovered scope must survive aggregation.

## Trust vocabulary

The architecture uses “trust” only as shorthand. Implementations should name the actual relation:

- **cryptographic trust anchor:** accepted basis for verifying a key or statement;
- **identity recognition:** evidence connecting an identifier to an actor;
- **authorization:** permission to exercise a role under a policy;
- **competency recognition:** a scoped claim about relevant expertise;
- **process conformance:** evidence that declared procedural requirements were met;
- **scientific disposition:** a qualified judgment about evidence and claim scope;
- **community recommendation:** a curation decision under a named policy;
- **user reliance:** a decision outside the protocol by a reader or downstream system.

These relations are not interchangeable and should not inherit one another silently.

## Automation and the living network

The primary engineering goal is to turn scientific review from a sequence of disconnected documents into an event-driven network that can remain current without requiring every reader or journal to rediscover every change manually.

A candidate loop is:

1. An archive publishes or supersedes an exact SRR.
2. Registries validate the signed event, issue receipts, index its claims and dependencies, and notify subscribers.
3. Automated consumers resolve the record, perform schema, signature, reachability, freshness, and policy checks, and publish scoped observation events.
4. Dependency and citation monitors identify potentially affected claims and emit impact candidates rather than silently changing scientific state.
5. Policy evaluators recompute frozen, reproducible trust views from the new event snapshot.
6. Routing services create review requests for uncovered, stale, disputed, or policy-required work.
7. Agents may retrieve evidence, reconstruct environments, execute workflows, compare outputs, and draft reports under recorded delegation.
8. Qualified reviewers append scientific dispositions, challenges, or adjudications where human authority is required.
9. Nodes distribute the new events and downstream views update again.

This loop is incremental and idempotent. Consumers should process an event more than once without duplicating its meaning, resume from signed checkpoints, state their completeness boundary, and tolerate partitions or delayed delivery. Derived views should expose `unknown`, `stale`, or `pending-convergence` rather than pretend that every node has seen the same world.

The network is “living” because its state is a reproducible projection over an accumulating event history. Historical records remain immutable; current interpretations update as new evidence arrives.

### Automate aggressively, authorize conservatively

Good automation targets include:

- object resolution, signatures, schemas, and receipts;
- claim–evidence and dependency traversal;
- change detection and candidate invalidation;
- notification, deduplication, indexing, and subscription matching;
- review coverage and policy requirement checks;
- environment reconstruction, bounded execution, and output comparison;
- reviewer discovery and conflict candidates;
- generation of review queues, discrepancy packets, and status summaries.

Automation should not silently decide that all material claims were declared, a custody boundary is scientifically adequate, a reviewer is genuinely independent, an interpretation is warranted, or a challenge is scientifically resolved. Those boundaries are represented as explicit tasks and dispositions so that increasing automation does not launder judgment into infrastructure.

## Threat model

The design must anticipate:

- Sybil reviewers and review rings;
- forged competence, hidden conflicts, and author-controlled “independent” reviewers;
- stolen keys, replay, over-broad delegation, and delayed revocation;
- omitted claims, scope laundering, strategic claim splitting, and meaningless tests;
- correlated human or model errors and agent monoculture;
- server equivocation, selective federation, censorship, and ranking manipulation;
- prestige capture, newcomer exclusion, retaliation, harassment, and defamation;
- deanonymization through review histories or conflict graphs;
- malicious artifacts, resource exhaustion, archive decay, and policy drift.
- compromised policy packages, evaluators, schemas, default trust roots, and client software;
- selective non-inclusion of challenges despite valid inclusion proofs for favored records;
- compensation, bribery, financial dependence, coercion, and coordinated challenge campaigns;
- clock disagreement, partitions, federation downgrade, and lossy schema mapping;
- prompt injection, poisoned metadata, and malicious documents targeting reviewing agents.

Defence must be layered: exact subject binding; identity-assurance tiers; multiple identity and competence issuers; institutional and collaboration diversity constraints; conflict graphs; signed policy and evaluator releases; submission receipts and maximum-publication-delay policies; signed checkpoints and cross-node witnesses; local trust roots; visible policy; lossless original-object retention; mirroring and export; appeals; compensation disclosure; scoped privacy or accountable pseudonymity; sandboxed execution and untrusted-content handling; and explicit `unknown` or `pending-convergence` states.

Decentralization is not itself a defence. If every client trusts the same default node or reputation projection, the result is centralized in practice.

## Protocol invariants to formalize

1. An authoritative decision never refers to a mutable subject.
2. Every disposition states exact scope and exclusions.
3. Every derived standing states policy, trust roots, visible events, and time.
4. Signature, credential, log inclusion, and server hosting never imply scientific adequacy.
5. Absence of challenge never implies support.
6. Conflicting attestations remain visible after adjudication.
7. Revocation and staleness append history rather than rewriting it.
8. Carry-forward requires an explicit scope-delta decision.
9. Aggregation preserves uncovered claims and unresolved disagreement.
10. Restricted evidence remains distinct from missing evidence.
11. Reviewer standing resolves to underlying, role- and domain-scoped events.
12. Agent actions disclose their operator, delegation, and material execution identity.
13. A node's trust view is reproducible from its published inputs and policy.
14. Federation failure does not make locally retained valid objects unverifiable.

## Minimal experiments

### A. Two-node semantic round trip

Two independently implemented nodes ingest one SRR, exchange review and revocation events, and reproduce the same view under the same policy. Different policies should yield different but fully explainable views.

### B. Attestation abuse suite

Exercise replay onto a successor release, unauthorized roles, expired credentials, hidden relationships, over-broad scope, post-review mutation, delayed revocation, server equivocation, missing restricted evidence, and Sybil endorsements. Measure false acceptance and localization.

### C. Distributed review of one public workflow

Split one modest study across execution, data, methods, uncertainty, and adversarial reviewers. Measure coverage, effort, duplicated work, handoff loss, disagreement localization, defects found, and reconstruction of the final policy view.

### D. Change and freshness exercise

Mutate presentation, numerical dependency, calibration data, claim interpretation, and acceptance predicates. Measure under- and over-invalidation of claims and attestations.

### E. Trust-policy diversity

Apply execution-oriented, domain-oriented, rapid-preliminary, and high-assurance policies to the same event set. Test whether differences remain intelligible and no interface presents one view as universal.

### F. Reputation robustness

Compare scalar ranking, faceted event histories, and policy thresholds under simulated review rings, Sybils, newcomers, minority-correct reviewers, and overturned consensus.

## Smallest credible prototype boundary

The first prototype needs content-addressed SRRs; signed review-event envelopes; immutable reports and challenges; a versioned policy format; a client evaluator; publish, retrieve, query, follow, and checkpoint interfaces; one auditable log; one replication path; claim-level discovery; faceted reviewer histories; and revocation, freshness, and supersession fixtures.

It does not need tokens, payment, blockchain consensus, a universal identity provider, automatic reviewer assignment, journal submission management, a global social network, or a universal reputation score.

## Non-goals

- Replacing scientific judgment with consensus computation
- Claiming novelty for provenance, signatures, identity, federation, or reputation
- Defining one global meaning of “accepted”
- Turning journal prestige into a server score
- Assigning agents human scientific authority by default
- Requiring public disclosure of restricted evidence
- Erasing dissent after adjudication
- Treating a declared graph as complete merely because it validates
- Claiming that a protocol prevents fraud or institutional capture
- Presenting this architecture as validated before interoperability, review, and attack experiments exist
