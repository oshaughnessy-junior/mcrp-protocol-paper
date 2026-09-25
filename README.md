# MCRP technical supplement

Working repository for an outward-facing, literature-grounded technical supplement on the Minimum Credible Reproducibility Protocol (MCRP), authored by Codex and junior. The supplement records a bounded design proposal and its evaluation gaps; it is not presented as a journal article, conference paper, priority claim, or validated intervention.

## Bounded design focus

The residual design question is whether a prospective, externally enforced, claim-versioned verification lifecycle is useful for agent-assisted computational science. The graph representation and its constituent review mechanisms are not claimed as novel. MCRP composes existing claim, provenance, workflow-run, archival, and attestation standards and proposes operational lifecycle constraints that remain to be evaluated.

## Public research source

On 25 September 2026 the maintainer authorized public access to this repository
after review of reachable history and publication surfaces. The technical
supplement remains a bounded research proposal; opening its source does not
change the scientific maturity decisions below. Older private/draft handling
notes describe preparation status and do not imply that restricted data should
be contributed here. Preserve each artifact's existing rights and provenance.

The newer [agent-first prototype](https://oshaughnessy-junior.github.io/trust-and-review-papers/)
provides runnable local contracts, mathematical models and adversarial examples.
Its [source repository](https://github.com/oshaughnessy-junior/trust-and-review-papers)
is the initial implementation and reproducible-contribution surface.

## Current status

- Publication: public aiXiv research prototype [aixiv.260925.000008](https://aixiv.science/abs/aixiv.260925.000008); revision responds to Official Agent review 1586. No validated effectiveness or priority claim.
- Submission status: no journal, conference, or arXiv submission is planned.
- Artifact route: retain the literature-grounded PDF as an outward-facing technical supplement authored by Codex and junior.
- Evidence status: closest-work comparison and claim ledger remain part of the technical record.
- Validation: historical matched-filter test counts withdrawn as supporting evidence because the itemized public mapping could not be recovered. A separate public prototype rerun and new revision-semantics tests provide narrowly scoped synthetic evidence; no comparative benefit claim is permitted.
- Release status: the reviewed technical supplement and companion post are public; any revision or additional outward-facing post requires fresh editorial, privacy, licensing, and artifact checks.
- Architecture status: a working sketch extends MCRP toward distributed-review compatibility through portable review attestations, federated trust nodes, and plural policy views. Trust-node concepts and component standards are guiding prior art, not an originality claim. The framework's main target is automation at scale: a living event network whose indexes, impact assessments, review queues, notifications, and derived views update as signed evidence arrives. This direction is unimplemented and unvalidated.

## Review revision

The revised manuscript is `paper/position-paper.md`. The point-by-point response, evidence inventory, mathematical specification, and internal red-team reports are in `paper/revisions/`. The new runnable model is `examples/revision-semantics/`; run its unittest suite from the repository root. These proposed semantics are not a claim that every earlier protocol draft or implementation already conforms.

## Executable work following the revision

The aiXiv [version1.1](https://aixiv.science/abs/aixiv.260925.000008v1.1) PDF was downloaded and verified against the released bytes. The author response is posted beneath the original version's review1586. The `aixiv-review-1586` tag preserves that submission snapshot.

Further source development adds two separate, synthetic tools:

- [Assurance assignment](examples/assurance-assignment/README.md) computes the proposed Section6 gates from supplied evidence assertions, preserving missing, expired, partial-scope and nonconforming states. It is not an authenticated review service.
- [Lifecycle benchmark](evaluation/lifecycle-benchmark/DESIGN.md) supplies exact offered-denominator metrics and a preregistration scaffold. Blanket refusal cannot win its descriptive gate; no real trial or statistical inference is claimed.

Both are standard-library Python examples. Their documentation gives commands and trust boundaries. These additions are not retroactively counted as evidence in the frozen aiXiv1.1 PDF.

## Source material

The starting protocol and validation artifacts were prepared in an internal assistant activity. Only the reviewed research derivatives belong in this repository. This public source history does not include or authorize publication of private correspondence, credentials or unrelated operational records. Current and future additions require appropriate provenance and rights; the prototype packet in the companion repository has its own explicit scoped licenses.

## Repository map

- `paper/`: technical supplement and bibliography
- `protocol/`: normative protocol revision and terminology
- `research/`: closest-work matrix, claim ledger, writing packet, and audits
- `evaluation/`: declared research questions, baselines, and validation records
- `docs/`: publication-defer, privacy, authorship, availability, and outward-release guidance
- `docs/distributed-review-architecture.md`: proposed record, attestation, federation, policy, and trust-view layers
- `docs/series-roadmap-distributed-review.md`: posts 2–4 and the proposed second outward-facing arc
- `research/trust-layer-landscape.md`: bounded standards and closest-system map for the trust layer
- `research/distributed-review-architecture-review-2026-08-16.md`: adversarial architecture, source, and narrative review with adjudication
- `protocol/review-attestation-federation-v0.1-draft.md`: non-normative next-component protocol sketch
- `review/`: independent scientific and reproducibility review records

## Non-negotiable limits

MCRP conformance records what was checked and by whom. It does not prove a scientific claim true, turn an agent into a scientific author or reviewer of record, or establish independence by signature alone.
