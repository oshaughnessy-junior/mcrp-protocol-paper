---
artifact_role: outward-facing-blog-seed
authors: [Codex, junior]
status: seed
date: 2026-08-16
series_part: 11
publication_status: private-not-approved
---

# How the trust layer fails

Decentralization does not cure social power. It can distribute failure as readily as authority.

A trust layer can be attacked through Sybil identities, reciprocal endorsements, captured registries, compromised keys, replayed attestations, selective revocation, hidden conflicts, reputation laundering, denial of discovery, and coordinated false challenges. Honest transparency can expose private relationships or enable retaliation. Automated routing can amplify biased credentials and make a locally chosen policy look objective.

No signature proves that its signer is unique, independent, competent, or honest. No append-only log proves that its contents are scientifically sound. No federation prevents several nominally independent services from sharing one controller. These limits should shape the protocol before its most convenient affordances harden into governance.

Defence therefore has several layers: typed identity and competency claims; explicit control principals and conflicts; quorums based on trust domains rather than key counts; independent monitors and witnesses; short-lived credentials where appropriate; challenge and appeal paths; rate limits and moderation; privacy-preserving disclosure; export and fork rights; and reproducible policy views that reveal their inputs. Newcomer routes matter too, because a system that requires inherited prestige can resist Sybils while entrenching incumbents.

These measures mitigate risk; they do not establish capture resistance. The framework should preserve enough raw signed material to let a community recompute a view after a node or policy fails. It should also make `unknown` an acceptable answer when independence or evidence cannot be established.

Architecture arguments are easy to make and hard to falsify. The final numbered post specifies what evidence would justify continuing—and what results should cause MCRP to narrow or stop.

## Maturity work

- Add three concrete threat scenarios: review ring, captured registry, and retaliation through disclosure.
- Map mitigations to residual risks rather than presenting a checklist as a solution.
- Ground the identity-count warning in Sybil prior art and the registry controls in transparency-log practice.

