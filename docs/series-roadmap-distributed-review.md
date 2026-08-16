---
artifact_role: outward-facing-series-roadmap
authors:
  - Codex
  - junior
status: working-draft
date: 2026-08-16
claim_posture: proposed-not-validated
---

# MCRP outward-facing sequence after Part 1

## Narrative rule

The current four-part series should complete MCRP's core logic before expanding the institutional frame:

1. identify the exact object reviewed;
2. connect each claim to evidence and execution;
3. separate evidence production from authority to approve;
4. preserve and revise approvals correctly over time.

Distributed review then appears as a design opportunity enabled by portable, version-bound records—not as a capability already delivered.

Keep four layers distinct: immutable SRR archive and resolution; the MCRP claim-review lifecycle; attestation transport, indexing, and federation; and client- or community-specific trust, reputation, routing, and curation. The latter layers extend around MCRP rather than silently becoming requirements of minimum MCRP. Trust servers and their component standards are guiding prior art, not an originality claim. The framework's practical objective is automation at scale and a scientific network that updates its indexes, review queues, impact assessments, and policy views as new signed events arrive.

Use this framing consistently:

> MCRP begins as a protocol for making a review result precise. It may also supply part of the substrate for distributed review, because independent parties can refer to the same immutable scientific object without requiring one publisher to own the entire process.

## Part 2: From Claims to Evidence

**Hook:** A workflow can rerun perfectly while leaving the paper's central claim unsupported. Reproducing an output and justifying a claim are different paths.

**Core model:** Connect a derivation structure—source, transformation, execution, output—to an epistemic structure in which evidence supports, bounds, contextualizes, or contradicts a claim. Review travels backward from claim to source and forward from a changed dependency to affected decisions.

**Example:** A figure rerenders exactly from saved values, but those values came from a provider-calibrated dataset with no calibration version. The rendering passes; the calibration dependency is unresolved and the scientific claim path remains incomplete.

**Boundary:** A graph exposes declared structure, not omitted claims or the scientific adequacy of a chosen custody boundary. The MCRP-specific proposition is the lifecycle consequence: a required missing path blocks a claim transition.

**Bridge:** Even a complete path does not decide whether the claim may advance. Who is authorized to say that it passed?

## Part 3: Who Is Allowed to Say It Passed?

**Hook:** A green check records an event. It does not establish independence, competence, authorization, or scientific adequacy.

**Core model:** Separate author evidence, machine verification, reviewer-controlled execution, and qualified scientific disposition. Bind each attestation to the exact claim, contract, evidence set, release, role, and decision.

**Example:** An external execution service confirms outputs; a domain reviewer accepts two claims, narrows one, and leaves another unassessed. The result is a vector of scoped decisions, not one badge.

**Distributed-review hint:** A signed, scoped attestation can be made portable when its target, schema, issuer identity, evidence references, and revocation status are independently resolvable. The repository host, execution verifier, domain reviewer, and curator need not be the same institution.

**Boundary:** Identity is not competence; competence is not independence; signatures do not establish either. Workable authorization policies remain untested.

**Bridge:** A precise approval can still become misleading after its evidence changes.

## Part 4: What Happens After Acceptance?

Suggested subtitle: **Scientific approval should have a history, not a halo.**

**Hook:** An approval that silently outlives the evidence it reviewed is a provenance failure.

**Core model:** Preserve acceptance as a historical event while appending current `stale`, `superseded`, `revoked`, or re-established dispositions. Never rewrite an old pass. Distinguish historical review, current reproducibility, and present scientific disposition.

**Example:** Revised calibration data affects two outputs and one headline claim but not a simulation claim. The first becomes stale; the second retains standing only after an explicit scope-delta judgment.

**Expansion:** Stable identities, a shared attestation format, and resolvers could let multiple parties publish reruns, challenges, endorsements, or narrowed dispositions against the same record without requiring one publisher to control all review records. An external party may challenge or propose a successor; it does not automatically supersede another party's record.

**Bridge to the second arc:** Where do portable review decisions live, how are they found, and why should anyone trust their issuers?

## Second arc: distributed review

### Part 5: A Review Need Not Belong to a Journal

Hook: **The journal of a distributed review system may be less like a container and more like a view.** Decompose the journal bundle into preservation, content identity, review routing, signed decisions, curation, reviewer history, correction, and discovery. A journal can remain one respected policy bundle rather than the exclusive host and owner of the review record. That view still depends on archives, review coordinators, accountable institutions, confidentiality, ethics enforcement, sanctions, appeals, financing, legal accountability, and preservation services; it does not make those functions disappear.

### Part 6: Attestation Registries—Who Said What About Which Release?

Introduce federated attestation registries—“trust servers” in shorthand—that index signed, scoped assertions about exact SRRs and claim versions. Explain inclusion receipts, auditable history, policies, server replication of records, discovery, revocation, and why hosting is not endorsement. The registry records and discovers attestations; it does not manufacture trust. Trust is a policy-specific view computed from typed records, issuer histories, declared roots, and exclusions. Federated registries need not agree on one status.

Heavily ground this post in Verifiable Credentials, SCITT and transparency logs, Linked Data Notifications, Activity Streams, WebSub, COAR Notify, DocMaps, Nanopublications, ORCID, and existing publish–review–curate communities. MCRP is proposing a scientific profile and automation loop across them, not the registry concept itself.

Short introduction:

> A distributed review system needs more than immutable scientific releases. It needs interoperable places where independently produced review claims can be published, discovered, challenged, and revoked. We call these federated attestation registries—or, more loosely, trust servers. They record typed, signed statements about exact release and claim versions: who reports rerunning them, what was examined, what passed, what failed, what remained outside scope, and what later event made an earlier decision stale. The registry does not decide what is true, and inclusion is not endorsement. It makes “who said what about which version, under what policy, on what evidence?” available so communities and readers can construct explicit trust views of their own.

Sharper hook:

> A compute center records a successful replay; a methods society approves the statistical procedure; a domain group challenges the interpretation. All three statements target the same claim version and remain visible without being averaged into one badge.

### Part 7: Reputation and Credit Without a Universal Score

Show why reviewer standing must remain domain-, method-, role-, conflict-, evidence-, and time-specific. Keep credit for what a contributor produced separate from later evidence about whether it worked or warranted scientific trust. Preserve inspectable event histories and let communities publish reproducible policy views. Cover Goodhart effects, prestige recursion, newcomer exclusion, dissent penalties, review rings, and bounded trust inference for the registries themselves.

### Part 8: A Scientific Network That Keeps Updating

**Hook:** Publication should add a version to the network, not freeze the network's understanding of it.

Trace one event loop: a dependency changes; monitors emit a scoped impact candidate; registries update indexes; policy views mark affected claims `pending` or `stale`; routing services create review work; agents rerun bounded checks; qualified reviewers append new dispositions; subscribers receive the result. Historical approval remains immutable while current views update.

Stress idempotency, checkpoints, causal references, delayed delivery, partitions, recomputation latency, and `unknown` states. “Self-updating” means automatic records and projections, not automatic scientific authority.

### Part 9: Review as a Distributed Workflow

Make review requests explicit and decomposable. Route execution, statistics, data, methods, interpretation, and adversarial challenge to qualified parties. Agents can inventory, execute, compare, monitor, and draft reports; humans retain scoped scientific authority under the present protocol.

### Part 10: Disagreement Is a Scientific Product

Preserve `supports`, `bounds`, `contradicts`, `fails-to-reproduce`, `narrows`, and `unassessed` as distinct records. Consensus is a computed view, never destructive aggregation.

### Part 11: How the Trust Layer Fails

Cover Sybil farms, reciprocal endorsement, server capture, key compromise, selective revocation, replay, reputation laundering, denial of discovery, privacy, retaliation, and coordinated false challenges. The answer is defence in depth, not “decentralization” as a cure.

### Part 12: How We Would Know This Helps

End the numbered arc with a preregistered evaluation contract. Compare against repository-plus-open-review and publish–review–curate baselines; measure false acceptance, defect localization, review time, reviewer agreement, stale-decision detection, attack resistance, cost, privacy harm, and newcomer participation.

## Later focused posts

- Review beyond executable science: instruments, samples, physical custody, tacit observations, and restricted data
- The economics of independent review: compensation, compute, incentives, and public goods
- Migration without a new platform: profiles over PROV, RO-Crate, Workflow Run RO-Crate, nanopublications, COAR Notify, Crossref, and existing archives

## Public-claim gates

Do not say MCRP has delivered a distributed science framework. Until interoperability and adversarial trials exist, use:

- “targets compatibility with distributed review”;
- “could provide a substrate”;
- “proposes a federated trust layer”;
- “treats journal functions as separable services.”

Avoid:

- “replaces journals”;
- “solves trust”;
- “prevents capture”;
- “proves reviewer reputation”;
- “achieves decentralization”;
- “establishes scientific truth.”
