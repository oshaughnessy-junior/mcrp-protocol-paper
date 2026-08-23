---
artifact_role: publication-prototype-evidence-exchange-contract
authors: [Codex, junior]
status: proposed-v0.1
date: 2026-08-23
publication_status: private-not-approved
applies_to:
  - independent AI and research-infrastructure publication lane
  - internal web/iOS MCRP protocol prototype
---

# Publication–prototype evidence exchange contract, v0.1

## Purpose

This contract defines how an independently operated AI/research-infrastructure publication lane may refer to a separately developed internal web/iOS MCRP prototype, and how bounded prototype observations may inform public writing.

The contract prevents three common collapses:

1. a working interface being described as validation of the protocol;
2. a public essay silently becoming authority to expose or change an internal system;
3. a post continuing to imply support after the prototype artifact it cited has changed.

The publication lane and prototype remain separate systems of record, queues, approval targets, and release authorities. Cross-listing creates a typed reference between them. It does not merge their lifecycle or permissions.

## Non-negotiable boundaries

- The prototype is internal by default.
- A prototype build, screenshot, test, or observation is not public merely because a post refers to it.
- Publication approval does not authorize prototype deployment, data access, telemetry collection, App Store/TestFlight distribution, repository release, or source disclosure.
- Prototype approval does not authorize a website post, social adaptation, or public validation claim.
- A successful synthetic demonstration establishes only that the tested path completed under the recorded fixture and environment.
- “Validated,” “robust,” “scalable,” “usable,” “adopted,” and “review-compatible” require separately designed evidence; they may not be inferred from implementation maturity.

## Two independent maturity ladders

### Prototype maturity

| Level | Name | Minimum evidence | Public-use boundary |
|---|---|---|---|
| P0 | Concept | wireframe, architecture note, or non-executable schema | May support design explanation only; label as proposed |
| P1 | Executable skeleton | versioned build, deterministic fixture, basic schema checks | May support “implemented a path” only; no behavioral or utility claim |
| P2 | Synthetic canary | end-to-end run on synthetic data, exact build and fixture digests, expected/observed result, failure record | May support a bounded demonstration claim tied to the exact canary |
| P3 | Internal observational pilot | approved internal scope, privacy review, predefined observation fields, multiple bounded runs, incident/failure accounting | May support labeled operational observations; not general validation or user evidence |
| P4 | Evaluated pilot | preregistered questions, comparison or baseline, sampling plan, measures, stop rules, complete adverse outcomes, analysis record | May support the exact evaluated claims within the study's limitations |
| P5 | Public release candidate | P4 evidence where relevant, public-safe artifact manifest, security/privacy review, reproducible build or inspectable release, release approval | May be directly linked or cross-listed after independent publication approval |

Progress is not monotonic. A material schema change, build drift, privacy incident, or invalidated fixture can return an artifact to an earlier level or mark it stale.

### Publication maturity

| Level | Name | Minimum evidence | Cross-list boundary |
|---|---|---|---|
| W0 | Editorial concept | audience, problem, claim posture | No prototype reference beyond a clearly labeled future example |
| W1 | Source-backed outline | prior-art ledger and proposed claims | May cite standards and design artifacts; no prototype-result claim |
| W2 | Reviewable draft | mature prose, limitations, claim/source map | May quote an accepted exchange packet using its required wording |
| W3 | Verified preview | claim, link, privacy, authorship, and rendering checks; exact preview digest | Eligible for owner review; still private |
| W4 | Approved exact revision | owner approval bound to source, render, destination, and base digests | Eligible for deterministic publication execution |
| W5 | Live and verified | canonical URL, feed/sitemap inclusion, live render and metadata receipts | May be cross-listed from a public prototype surface if separately approved |

A post may not inherit the prototype's maturity. Both sides must independently satisfy the relevant gate.

## Evidence categories and permitted language

Every exchanged item must use at least one of these categories:

| Code | Category | Examples | Permitted claim pattern |
|---|---|---|---|
| E0 | Normative or prior-art source | standard, RFC, protocol specification, primary research paper | “The standard defines…” or “Prior work proposes…” |
| E1 | Design rationale | architecture decision, schema mapping, threat model | “The prototype is designed to…” or “We chose…” |
| E2 | Synthetic demonstration | fixture, mock workflow, deterministic UI path | “In this synthetic canary, version X completed…” |
| E3 | Implementation/conformance evidence | schema validation, compatibility test, deterministic build | “Build X passed checks Y against profile Z” |
| E4 | Internal operational observation | bounded pilot event, latency, failure mode, workflow friction | “Across N approved internal runs under conditions C, we observed…” |
| E5 | Comparative evaluation | preregistered measure against a baseline or alternative | “Under evaluation E, X differed from baseline B by…” |
| E6 | Independent external evidence | third-party replication, critique, adoption, or interoperability test | “Party Q reports…” with independence and scope stated |

E1–E3 do not justify usefulness, robustness, adoption, reviewer trust, or scientific validity. E4 is descriptive and context-bound. Only E5 or E6 can support broader empirical claims, and only within their recorded design and limitations.

## Cross-listing eligibility

### May be cross-listed

- public standards, prior art, and stable public identifiers;
- an approved public protocol or schema release;
- synthetic diagrams, fixtures, screenshots, and walkthroughs that contain no private identifiers or topology;
- exact conformance or canary receipts reduced to public-safe fields;
- an approved public prototype release, release note, or demonstration;
- aggregate failure categories and limitations when the privacy review explicitly permits them;
- a public post, position paper, protocol note, or evaluation plan with a canonical URL;
- later corrections, staleness notices, and superseding versions.

### Must not be cross-listed

- internal repository, filesystem, server, test-distribution, or dashboard locators;
- unpublished source code or binaries not explicitly released;
- credentials, tokens, device IDs, push identifiers, certificates, session IDs, or network topology;
- raw crash logs, analytics events, interaction traces, screenshots from real private workflows, or message contents;
- private scientific artifacts, reviewer identities, manuscripts, claims, results, or comments;
- internal user names, contacts, calendars, issue titles, machine names, or operational schedules;
- selective success metrics that omit failures, retries, exclusions, or denominator definitions;
- model transcripts or agent reasoning;
- any artifact whose owner, license, consent, or release authority is unresolved.

## Exchange packet

Every reference from one lane to the other must be backed by a durable packet. A minimal packet contains:

```yaml
schema: mcrp.publication-prototype-exchange.v0.1
exchange_id: opaque-stable-id
direction: prototype-to-publication | publication-to-prototype
producer: named-system-or-role
source_repository: private-logical-id
source_revision: full-commit-or-release-id
prototype_maturity: P0 | P1 | P2 | P3 | P4 | P5
publication_maturity: W0 | W1 | W2 | W3 | W4 | W5
evidence_categories: [E0, E1]
artifacts:
  - logical_name: artifact-name
    sha256: full-digest
    media_type: application/json
    privacy_class: public | export-reviewed | internal | restricted
fixture_or_dataset:
  identifier: synthetic-fixture-id
  sha256: full-digest
environment:
  build_id: exact-build-id
  configuration_digest: full-digest
observed_at: ISO-8601
expires_or_recheck_at: ISO-8601
allowed_public_claims:
  - exact bounded sentence or template
prohibited_inferences:
  - exact broader inference
limitations:
  - material limitation
supersedes: null
approval_receipts:
  privacy: receipt-id
  evidence: receipt-id
  publication: null
```

Private physical paths may appear in the internal packet store but never in the public projection. Public prose refers to the opaque exchange ID, public release identifier when present, and safe digest prefix where useful.

Any change to the source revision, fixture, configuration, artifact bytes, allowed claim, privacy classification, or limitation creates a new packet. It may supersede the prior packet; it may not mutate the historical record silently.

## Exchange workflow

1. **Register candidate.** The producing system records the exact artifact revision and requested evidence category.
2. **Classify privacy.** Apply an export allowlist; do not attempt to sanitize arbitrary raw logs after the fact.
3. **Assign maturity.** Record the independently justified P and W levels.
4. **Write allowed and prohibited claims.** These must be concrete enough for a reviewer and deterministic checker to compare with the draft.
5. **Evidence review.** Confirm the observation follows from the bound artifact and that adverse outcomes are represented.
6. **Editorial use.** The writer may use only the allowed claim or a strictly narrower paraphrase, with the maturity label and limitations visible nearby.
7. **Build private preview.** Bind the rendered post to the exchange packet digest.
8. **Owner approval.** Obtain exact publication approval through the publication lane's Telegram workflow. Prototype release, website publication, and social publication remain separate decisions.
9. **Live verification.** Confirm the canonical page points to the intended public artifact, not an internal locator.
10. **Monitor drift.** On supersession, invalidation, privacy change, or material failure, queue a post annotation, correction, or withdrawal review.

## How observations may inform posts

Prototype observations are most useful when they sharpen examples, reveal missing states, expose operational costs, or falsify an assumed workflow. They should influence public writing through a bounded observation ledger rather than informal recollection.

Acceptable examples:

- “A synthetic iOS-to-web canary exposed an unmodeled `unknown` state between delivery and ingestion; the protocol draft now represents that state explicitly.”
- “Version 0.3 passed the listed schema-conformance checks on fixture F. This demonstrates the tested serialization path, not interoperability with independent implementations.”
- “Across eight approved internal trials, reviewers repeatedly needed the evidence-scope field before acting. This is an operational observation from one workflow, not a usability study.”

Unacceptable transformations:

- “The app validates MCRP.”
- “Reviewers found the protocol usable” when no designed user study exists.
- “The network is robust” because retries completed in one environment.
- “The system scales” from local latency or throughput observations.
- “The prototype proves distributed review works.”

When a prototype observation changes the conceptual framework, the post should say what was learned and what remains untested. Do not retrofit the observation into a claim that the prototype had already been designed to prove.

## Privacy and mobile-specific constraints

Web and iOS artifacts require explicit checks for information that is easy to expose incidentally:

- notification bodies and badge counts;
- device, vendor, advertising, installation, and push-token identifiers;
- account names, avatars, contact data, and message history;
- crash reports, analytics payloads, timestamps, IP addresses, and location hints;
- screenshots containing OS status bars, calendars, networks, or real documents;
- test-distribution invitations, signing identities, provisioning profiles, and bundle-management details;
- internal hostnames, API routes, authentication states, and trust-store contents.

Public demonstrations use synthetic accounts, synthetic records, fixed clocks when possible, sanitized status bars, and a public-safe build or recording generated expressly for export. A screen recording of an internal system is not made safe by cropping alone.

## Update cadence and staleness

Do not continuously mirror prototype state into public posts.

- Generate exchange candidates at versioned prototype releases, completed synthetic canaries, evaluation checkpoints, and material failure/correction events.
- Review ordinary candidates in a weekly editorial batch.
- Elevate privacy, security, retraction, or invalidation events immediately.
- Recheck active prototype-linked posts at least monthly during the launch season and at every referenced artifact supersession.
- Preserve publication history. Apply dated annotations or successor posts rather than silently rewriting what an earlier prototype version supported.

The prototype may maintain a living internal projection. The public lane publishes reviewed snapshots and corrections, not a live operational dashboard.

## Queue and authority separation

Maintain two linked queues:

- **Prototype evidence queue:** artifact, build, fixture, observation, privacy class, maturity, and technical reviewer.
- **Publication queue:** argument, audience, canonical destination, source/claim map, preview, authorship, and owner decision.

The shared key is `exchange_id`; neither queue may directly advance the other. A technical reviewer can accept an E3 receipt without approving prose. An editor can reject a post without invalidating the prototype receipt. Richard's publication approval applies only to the exact destination and rendered revision named in its packet.

## Minimum launch rule

Before the new publication lane publicly mentions the internal prototype as evidence, require:

- at least P2 prototype maturity;
- a complete exchange packet with E2 or E3 evidence;
- synthetic-only public assets;
- explicit limitations and prohibited inferences;
- W3 verified preview maturity;
- digest-bound owner approval for the exact public revision.

P0–P1 material may still appear as clearly labeled design illustration without implying observed behavior. No internal prototype link, build, or locator is exposed until a separately approved P5 public release exists.

## Review of this contract

Treat v0.1 as a design control, not a validated protocol. Revisit it after the first three exchange packets or the first material near-miss, whichever occurs first. Record which fields were missing, which claims were difficult to classify, and whether the two-queue boundary prevented or merely delayed ambiguity.
