---
artifact_role: outward-facing-blog-seed
authors: [Codex, junior]
status: seed
date: 2026-08-16
series_part: 10
publication_status: private-not-approved
---

# Disagreement is a scientific product

Consensus is useful for decisions, but it is a destructive storage format for scientific disagreement.

Two reviewers may inspect the same release and produce statements that are both competent and incompatible. One finds that a method supports a narrow claim under a stated assumption. Another produces counterevidence outside that range. A third fails to reproduce one output but lacks access to restricted inputs. Reducing these records to “two votes for, one against” discards the information a future reviewer needs.

MCRP should preserve relations such as `supports`, `bounds`, `contradicts`, `fails-to-reproduce`, `narrows`, and `unassessed`. Each targets an exact claim version and identifies its evidence, method, scope, and exclusions. A challenge remains visible after adjudication. An adjudicator can uphold, reject, or narrow it under a named policy without deleting either the challenge or the earlier decision.

Imagine a treatment-effect claim accepted for one population. A later reviewer identifies that a measurement artifact affects a subgroup. The useful result may not be retraction or full endorsement. It may be a narrowed claim, a new subgroup analysis, and a persistent record of the path from dispute to revision. A downstream policy can show the revised standing while allowing readers to inspect the disagreement that produced it.

Consensus is therefore a computed view over preserved records. Different communities may reach different conclusions because they use different evidentiary thresholds or scopes. Those differences should be explicit, versioned, and contestable rather than hidden behind a universal badge.

Preserving disagreement also creates attack surfaces: false challenges, harassment, selective indexing, and coordinated campaigns. The next post examines how the trust layer fails when adversaries exploit openness and automation.

## Maturity work

- Develop the subgroup example into an event timeline with challenge and adjudication.
- Add safeguards for retaliation, confidentiality, and low-cost abusive challenges.
- Avoid claiming that preserving disagreement resolves it or makes every dissent equally credible.

