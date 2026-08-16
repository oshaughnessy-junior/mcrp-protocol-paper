# MCRP review-attestation federation — v0.1 working draft

This document sketches the next MCRP protocol components. It is not a frozen specification, implementation commitment, or validated governance model.

## 1. Design target

Enable independently governed reviewers, verification services, archives, communities, and discovery systems to make, register, exchange, challenge, and evaluate statements about the same immutable Scientific Record Release (SRR).

The protocol MUST preserve the distinction among:

- identity and attribution;
- mechanical observations;
- scientific judgment;
- process completion;
- community endorsement;
- current policy-derived standing.

No one of these implies the others.

The protocol distinguishes four outcomes: a **release-local lifecycle state** records a historical MCRP transition under an exact contract and authority; a **community endorsement** records a community's recommendation; a **current trust view** derives a time-bound interpretation from a frozen event snapshot; and a **user reliance decision** remains outside the protocol. There is no global acceptance state.

## 2. Core objects

### Review request

A review request MUST bind:

- exact SRR and claim versions;
- review questions and requested disposition types;
- required roles, competencies, independence, and conflicts policy;
- expected review or execution method;
- accepted assessment modes and evidence-access boundary;
- completion, expiry, compensation, confidentiality, and appeals terms;
- requesting actor, policy identifier, and signature.

The request MUST identify whether it is author-requested, community-commissioned, or unsolicited. A later community endorsement MUST apply the community's independently published policy; requester-selected scope and completion terms are not sufficient. Omitted review dimensions and uncovered claims remain visible.

### Review report

A review report MUST state:

- target and actual scope;
- record fragments and external evidence inspected;
- methods and tools used;
- observations, inferences, dispositions, caveats, and unresolved questions;
- changes made or requested;
- author, agent, delegation, and execution provenance where material;
- report identity and signature.

### Review attestation

A review attestation MUST strictly extend MCRP's existing signed tuple `(claim version, acceptance-contract version, evidence-set digest, release digest, role, decision)`. It MUST include:

- immutable subject identity;
- exact acceptance-contract identity and evidence-set digest;
- attestation type and exact predicate;
- claim scope and exclusions;
- decision, uncertainty, and limitations;
- assessment mode, outcome vector, and exact review-report digest;
- issuer, role, competency or authority basis, and conflicts;
- governing policy;
- issuance, expiry, and freshness conditions;
- supersession, challenge, withdrawal, and revocation links;
- signature.

A signature MUST NOT be interpreted as proof of competence, independence, correctness, or truth.

Predicates MUST declare their authority class. Tools and agents MAY issue mechanically observable predicates under recorded delegation. Under current MCRP governance, scientific-disposition predicates require a qualified human issuer. An agent recommendation MUST use a distinct predicate and MUST NOT satisfy a human-disposition guard. Human adoption MUST identify the agent report reviewed and state the human's independent scope of responsibility.

### Contribution assertion

A contribution assertion MUST bind an actor and role to an exact object or change; describe provenance and delegated agent participation; distinguish claimed credit from author adoption; and support challenge, correction, withdrawal, or supersession. Contribution credit MUST NOT imply scientific endorsement, reviewer competence, or trustworthiness.

### Challenge and adjudication

A challenge MUST identify its exact target, grounds, evidence, requested consequence, author, scope, and signature. Its presence MUST NOT automatically erase or reverse the challenged attestation.

An adjudication MUST preserve both the challenged record and challenge, identify the governing policy and adjudicator authority, and append a disposition such as `upheld`, `partly-upheld`, `rejected`, `unresolved`, or `out-of-scope`.

Authority is scoped: an issuer may withdraw or supersede its own attestation; a credential issuer may revoke its own credential; a node may correct or withdraw its own receipt; a policy authority may exclude an event only from its own derived view; and an adjudicator may issue a contrary disposition under its policy. No actor may erase or rewrite another actor's signed statement.

### Trust-node receipt

A receipt MUST establish only that a named trust node registered a named signed object under a stated registration policy and log state. It MUST NOT imply that the node endorses the object's scientific content unless it issues a separate endorsement attestation.

### Trust view

A trust view MUST identify:

- frozen event-set manifest and digest;
- trust roots and recognized credential issuers;
- policy and evaluator versions;
- exact node checkpoints, query and query-language versions, credential and revocation snapshots, and evaluator artifact digest;
- evaluation time and freshness cut;
- clock semantics and declared completeness boundary;
- outputs at claim and release scope;
- uncovered requirements, excluded events, conflicts, and unresolved disagreement.

A trust view is mechanically reproducible only given that snapshot. It MUST NOT modify its input records or claim that the snapshot is globally complete.

## 3. Suggested event vocabulary

Observation and execution:

- `artifact-resolved`;
- `workflow-executed`;
- `outputs-match`;
- `negative-control-passed`;
- `dependency-change-observed`.

Scientific disposition:

- `supports-within-scope`;
- `bounds`;
- `contradicts`;
- `methods-adequate`;
- `uncertainty-adequate`;
- `claim-too-broad`;
- `material-limitation`;
- `unassessed`.

Review and governance:

- `review-requested`;
- `review-accepted`;
- `process-recorded-completion`;
- `competency-recognized`;
- `role-delegated`;
- `conflict-disclosed`;
- `community-endorsed`;
- `challenge-raised`;
- `challenge-adjudicated`.

Status and history:

- `expired`;
- `stale`;
- `superseded`;
- `withdrawn`;
- `revoked`;
- `retracted`;
- `unavailable`.

These types MUST use one event envelope that records target, scope, issuer and authority, cause, prior event or state, effective time, observed-log time, policy and guard versions, and reason. Status is derived from events rather than stored as a mutable field. Types MUST NOT be collapsed without an explicit, signed, versioned, loss-aware mapping policy.

Process completion MUST be computed from the review request's prospective completion rule and required dispositions. A `process-recorded-completion` receipt cannot independently establish MCRP completion or scientific approval.

## 4. Trust-node semantic operations

A minimal node SHOULD support:

- `register(signed_object) -> receipt | rejection`;
- `resolve(object_id) -> object | unavailable`;
- `query(subject, claim, issuer, type, policy, time) -> event_set`;
- `status(object_or_credential_id) -> dated_status_history`;
- `checkpoint() -> signed_log_checkpoint`;
- `prove_inclusion(object_id, checkpoint) -> proof`;
- `follow(subject_or_query) -> notification_stream`;
- `federate(peer, selection_policy) -> replicated_events_and_receipts`.

An implementation MAY separate these operations among archive, log, index, notification, and policy-evaluation services.

Any authoritative transition or policy result MUST disclose the requester, issuer, node, credential issuer, policy authority, and their control principals; delegation paths; material shared dependencies; and the independence rule evaluated. A different service account, agent, model, hostname, or corporate subsidiary MUST NOT establish independence by itself.

## 5. Federation rules

- The same signed object MAY be registered at multiple independently governed nodes.
- Nodes MUST publish identity, keys, registration policy, moderation policy, retention policy, supported schemas, and checkpoint mechanism.
- Replication MUST preserve the original signed bytes, issuer, subject, and receipts.
- A node MUST NOT present a mirrored statement as its own endorsement.
- Conflicting statements MUST remain independently addressable.
- Nodes SHOULD expose equivocation or fork evidence and support cross-node checkpoint monitoring.
- Submission receipts and maximum-publication-delay policies SHOULD make selective non-inclusion observable within a declared boundary; no node can prove global event completeness.
- A federation policy MAY exclude content from discovery. Moderation evidence MAY require opaque or privacy-preserving tombstones, delayed disclosure, or private audit; a public reason or target digest MUST NOT be required when it would violate privacy, safety, or law.
- Replication and schema mapping MUST retain the signed original. Mapping artifacts MUST identify their schema and mapping versions and MUST fail rather than discard decision scope, exclusions, or limitations.

## 6. Reviewer and contributor histories

Histories SHOULD be event-derived and faceted by:

- domain, method, instrument, and role;
- review scope and assessment mode;
- competency and identity assurance;
- conflicts and independence evidence;
- challenges, adjudications, corrections, and withdrawals;
- timeliness and follow-through;
- underlying evidence accessibility and reproduction status.

The base protocol MUST NOT define a global scalar reputation score. A ranking provider MAY compute one, but it MUST identify its inputs, weights, policy, time window, uncertainty, exclusions, and maximum trust-inference depth.

Review quality MUST NOT be equated with agreement with later majority opinion. Qualified dissent and correct early challenges are first-class events.

## 7. Identity, privacy, and restricted review

- Scholarly identifiers such as ORCID and ROR SHOULD be reused where adequate.
- Agent identity MUST remain distinct from the authorizing human or institution.
- A human adoption of an agent-generated disposition MUST be a separate attestation.
- Anonymous or pseudonymous review MAY use an accountable intermediary that issues a scoped credential or receipt without publishing the reviewer identity.
- Public logs MUST NOT contain protected evidence, unnecessary personal data, secret conflicts, or material that enables retaliation.
- Material compensation, sponsorship, and financial dependence for review or curation MUST be disclosed to the governing policy, with public visibility governed by safety and confidentiality constraints.
- A commitment to restricted evidence MUST remain distinguishable from evidence that is absent or was never inspected.
- Withdrawal from public display does not necessarily permit deletion from an audit record; governance, safety, and legal requirements remain unresolved.

## 8. Candidate capability vector

Avoid a cumulative badge ladder. A deployment reports independently tested capabilities and their observation windows:

- `attestation-portability`: canonical serialization, signature envelope, key resolution, algorithm agility, and exact MCRP tuple binding;
- `transparent-registration`: receipt verification, signed checkpoints, bounded status history, and submission-delay monitoring;
- `record-discovery`: structured query, notifications, and declared index coverage;
- `cross-node-exchange`: lossless exchange or replication across separately identified nodes, with governance-independence evidence reported separately;
- `revocation-convergence`: observed propagation time and partitions under a declared SLA, including `unknown` or `pending-convergence` states;
- `policy-reproducibility`: identical results from a frozen event, credential, revocation, policy, evaluator, and clock snapshot;
- `disagreement-preservation`: uncovered claims, conflicting dispositions, challenges, and appeals remain inspectable;
- `privacy-controls`: tested disclosure, pseudonymity, restricted-evidence, and moderation behavior.

These are infrastructure capabilities, not levels of scientific truth or reviewer quality.

## 9. Time, keys, and long-lived records

- Events SHOULD record signed issue time, log-observed time, causal references, and allowed clock skew.
- Policies MUST define behavior under partitions and uncertain ordering; they SHOULD prefer `unknown` or `pending-convergence` to a falsely current result.
- Registration SHOULD preserve key-validity evidence, issuer status, and checkpoints sufficient for later historical validation.
- Key rotation, compromise, algorithm migration, and countersignature history MUST be append-only. Later compromise MUST NOT silently invalidate every historical statement or leave them silently trusted.
- Policies, evaluators, schemas, and default trust-root releases MUST themselves be signed, versioned, rollback-resistant, and covered by reproducible fixtures.

## 10. Required test suite before stabilization

- exact subject and claim binding;
- replay onto successor releases;
- unauthorized role and over-broad delegation;
- expired, compromised, or revoked credentials;
- challenge, withdrawal, supersession, and retraction semantics;
- identical-policy cross-node round trip;
- different-policy explainability;
- node equivocation and inconsistent checkpoints;
- delayed or partitioned revocation propagation;
- conflict and correlated-review fixtures;
- privacy and anonymous-review leakage tests;
- policy, evaluator, schema, and trust-root supply-chain compromise;
- selective non-inclusion, moderation privacy, partition, ordering, and downgrade attacks;
- prompt injection, poisoned metadata, and malicious review packets targeting agents;
- uncovered-claim and unresolved-disagreement preservation;
- export to established scholarly review and provenance standards.

## 11. Open governance questions

- Who may issue competency attestations, and how can newcomers enter?
- Which combinations of identity, affiliation, collaboration, and funding create a disqualifying conflict?
- When may an unresolved challenge suspend a community endorsement?
- How should defamatory, harassing, illegal, or privacy-invasive statements be moderated without enabling silent scientific censorship?
- What economic model supports independent review, preservation, and monitoring?
- When is public identity required, and when is accountable pseudonymity safer?
- How are captured or defunct trust nodes exited without losing history?
- Which authorities can revoke credentials, reports, community standing, or only their own earlier statements?

These are scientific-institutional design questions. A schema or cryptographic primitive cannot settle them.
