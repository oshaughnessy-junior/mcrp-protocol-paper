# Prospective claim lifecycle — v0.2 working draft

This document isolates the candidate contribution that must survive comparison with prior work. It is not yet a frozen MCRP release.

## Claim acceptance contract

Before a claim-bearing execution, each material claim version MUST bind:

- exact claim text, scope, units, population, and qualifiers;
- admissible evidence types and required evidence relations;
- claim-bearing outputs or output selectors;
- comparison metrics, tolerances, and scientific invariants;
- stopping and failure rules;
- required reviewer roles and independence constraints;
- dependencies whose change makes the contract or its decisions stale; and
- the digest of this contract.

Changing one of these fields after an execution produces a new claim-contract version. An earlier execution MAY be considered as evidence for the new version only through an explicit, reviewable carry-forward decision; it MUST NOT inherit acceptance automatically.

## States

The minimum claim lifecycle is:

`draft -> registered -> executed -> evidence-complete -> independently-checked -> human-approved | rejected`

Any state after `registered` MAY transition to `superseded`, `stale`, or `revoked` when its scoped conditions are met. `human-approved` is not terminal with respect to freshness.

## External enforcement

The component evaluating a transition guard MUST be outside the authority boundary of the agent or process requesting the transition. The requester MAY supply evidence but MUST NOT write an authoritative successor state directly.

Every accepted transition MUST record:

- prior and successor state;
- claim and contract version;
- exact Scientific Record Release digest;
- evidence-set digest;
- guard and policy versions;
- requesting and deciding agent identities and roles;
- timestamp and, where required, expiry; and
- reason, limitations, and unresolved findings.

## Attestations

An attestation applies only to the tuple `(claim version, acceptance-contract version, evidence-set digest, release digest, role, decision)`. It MUST NOT be replayable onto a different tuple. A signature establishes attribution and integrity, not scientific correctness or independence.

Revocation MUST preserve the original attestation and append a scoped revocation record with identity, authority, reason, and effective time.

## Dependency invalidation

The authoritative controller MUST traverse declared dependency edges after a change. A changed code, data, environment, service, model, acceptance rule, evidence object, or upstream claim marks every reachable dependent decision `stale` unless a versioned rule proves that the change is immaterial to that decision.

Invalidation MUST be monotone within a release history: it adds a dated stale or revoked disposition and never rewrites a previously passing historical record. Re-establishing a decision creates new evidence and a new attestation.

## Interoperability constraint

MCRP SHOULD profile established objects rather than duplicate them: PROV-O for entities, activities, agents, responsibility, and derivation; Workflow Run RO-Crate for execution packages; and a nanopublication- or Micropublication-compatible claim assertion/provenance record. MCRP-specific fields SHOULD be limited to prospective acceptance contracts, transition guards, scoped decisions, invalidation, and assurance policy.

## Unresolved gates

- Formal machine-readable state and transition schemas.
- Competency questions and counterexamples against EVI/PROV-only records.
- Round-trip mapping tests for PROV-O and Workflow Run RO-Crate.
- Attestation replay and revocation tests.
- Independent exercise against an immutable sanitized release.
- Comparative evidence that the lifecycle improves any review outcome.

