---
artifact_role: outward-facing-blog-seed
authors: [Codex, junior]
status: seed
date: 2026-08-16
series_part: 6
publication_status: private-not-approved
---

# Who said what about which release?

A compute center records a successful replay; a methods society approves the statistical procedure; a domain group challenges the interpretation. All three statements target the same claim version and remain visible without being averaged into one badge.

A distributed review system needs interoperable places where independently produced review claims can be registered, discovered, challenged, and revoked. We call these **federated attestation registries**, or more loosely trust servers. They record typed, signed statements about exact release and claim versions: who reports rerunning them, what was examined, what passed, what failed, what remained outside scope, and what later event changed an earlier decision's status.

The registry is not the novel idea here. [Verifiable Credentials](https://www.w3.org/TR/vc-data-model-2.0/) provide a model for signed claims; [SCITT](https://www.rfc-editor.org/rfc/rfc9943.html) and transparency logs provide registration receipts and auditable histories; [Linked Data Notifications](https://www.w3.org/TR/ldn/), [Activity Streams](https://www.w3.org/TR/activitystreams-core/), [WebSub](https://www.w3.org/TR/websub/), and [COAR Notify](https://coar-notify.net/specification/1.0.1/) provide patterns for exchanging events; [Nanopublications](https://nanopub.net/) demonstrate decentralized, content-addressed assertions. These systems are guiding infrastructure. MCRP proposes a scientific profile and lifecycle binding across them.

A useful registry can validate schemas and signatures, issue an inclusion receipt, preserve or reference an append-only history, index statements, exchange selected records, and notify subscribers. Hosting is not endorsement. A registry receipt proves neither scientific truth nor reviewer competence. Different registries may admit different records and compute different policy views while preserving the signed originals.

For example, a methods society may accept a review only from credentialed statisticians with declared conflicts, while a replication community may show every verifiable rerun. A reader can inspect both views and their policies. The network gains plural discovery without manufacturing one universal authority.

That leaves the hard social question: how can a system use reviewer histories for routing and credit without turning status into a single score that entrenches prestige?

## Maturity work

- Add a registry receipt/event diagram and explicitly separate registration, replication, discovery, and federation.
- Cite OpenID Federation for node bootstrap and trust marks; cite DocMaps for review-event representation.
- Preserve the claim boundary: established components motivate the design; cross-system interoperability is proposed and untested.

