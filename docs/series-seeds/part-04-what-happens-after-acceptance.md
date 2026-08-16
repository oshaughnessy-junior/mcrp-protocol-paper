---
artifact_role: outward-facing-blog-seed
authors: [Codex, junior]
status: seed
date: 2026-08-16
series_part: 4
publication_status: private-not-approved
---

# What happens after acceptance?

Scientific approval should have a history, not a halo. An approval that silently outlives the evidence it reviewed is a provenance failure.

An immutable review record should preserve what happened: a qualified reviewer accepted a particular claim version, under a particular contract, using a particular evidence set. Later events should not rewrite that history. They should append a current disposition such as `stale`, `superseded`, `revoked`, or re-established after review.

Suppose a calibration dataset is corrected. The change affects two figures and one headline claim, but it does not touch a simulation claim whose inputs were independent. A dependency-aware system can mark the affected paths for inspection without withdrawing every result. The headline claim becomes stale pending a new disposition. The simulation claim retains standing only if its independence is explicit or a reviewer approves the scope delta. Automation identifies candidates; it does not make the scientific judgment.

Three questions must remain distinct. **Was this release approved then?** is historical. **Can its recorded computations be reconstructed now?** is operational. **Does a named policy presently regard this claim as supported?** is a current, policy-bound view. Collapsing them produces either amnesia—old decisions disappear—or false permanence—old approvals never age.

Once review events are bound to exact objects, other parties can publish reruns, challenges, endorsements, or narrowed dispositions without asking one publisher to own the whole history. An outside challenge does not automatically supersede an earlier decision; it becomes another visible event awaiting interpretation or adjudication.

That opens a larger institutional question. If the record, review, and curation decision can be separately preserved, must a review belong to one journal at all?

## Maturity work

- Add a release-to-successor timeline with one unaffected and one stale claim.
- Define revocation, withdrawal, supersession, and staleness without conflating them.
- Make the carry-forward rule explicit: no claim inherits approval merely because its label is unchanged.

