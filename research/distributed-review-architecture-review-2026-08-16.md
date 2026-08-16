# Distributed-review architecture review and adjudication

Date: 2026-08-16
Review target: working drafts of the distributed-review architecture, federation protocol, trust-layer landscape, and series roadmap
Authors: Codex and junior

## Review method

Three independent bounded passes examined:

- system and authority semantics;
- closest standards and primary-source accuracy;
- outward-facing sequence and claim strength.

The review was adversarial and did not assume that stable identifiers, signatures, federation, or reputation make a trustworthy scientific system.

## Blocking findings addressed

1. Restored the exact existing MCRP attestation tuple—claim version, acceptance-contract version, evidence-set digest, release digest, role, and decision—and made the new envelope a strict extension.
2. Classified predicate authority so tools and agents can issue observations while current scientific dispositions require qualified human adoption under explicit responsibility.
3. Restored external-controller separation and required control-principal, delegation, dependency, and independence evidence.
4. Distinguished historical release-local approval, community endorsement, current trust view, and user reliance.
5. Bound trust views to frozen event, node-checkpoint, credential, revocation, policy, evaluator, query, and clock snapshots.
6. Replaced free-standing mutable statuses with typed events and constrained completion to prospective policy evaluation.
7. Defined scoped withdrawal, revocation, correction, exclusion, and adjudication authority; no actor may rewrite another's signed statement.
8. Added contribution assertions and separated credit from scientific endorsement and reviewer standing.
9. Replaced cumulative RA grades with a multidimensional, tested capability vector.
10. Added policy-supply-chain, selective non-inclusion, moderation/privacy, time/partition, downgrade, long-term key, economic, and reviewing-agent threats.

## Landscape corrections addressed

- Added OpenID Federation 1.0 for trust marks, delegated issuers, status, and federation discovery while rejecting a universal hierarchy.
- Clarified that SCITT supports independently registering statements with multiple transparency services but does not supply scholarly federation or discovery.
- Elevated Nanopublications and Trusty URIs as close prior art for immutable distributed assertions.
- Separated notifications, crawling, relationship indexes, and policy evaluation.
- Marked DocMaps and in-toto maturity accurately and labelled MCRP edge and Sybil controls as design inference.
- Added direct Traxia and fuller provenance-source links.

## Narrative corrections addressed

- Distributed review is a design opportunity, not a consequence already delivered.
- A signature is not semantic portability; resolvers, schemas, target identity, evidence references, and status are also required.
- External parties may challenge or propose successors but cannot supersede another party's record automatically.
- The current series remains focused on structure, authority, and time before the second arc introduces registries.
- The second arc now ends with an explicit evaluation contract.

## Remaining evidence gaps

- No formal schema or crosswalk has been produced.
- No node, registry, evaluator, or federation prototype exists.
- No security proof, independent implementation, or attack suite exists.
- No reviewer, author, curator, or reader study has been conducted.
- No governance, privacy, moderation, compensation, or appeals model has community legitimacy.
- No comparison has shown benefit over repositories plus open review or publish–review–curate systems.

Disposition: **adequate as a conceptual architecture and outward-facing roadmap; not adequate as a standard, implementation claim, or evidence-backed peer-review intervention.**
