---
artifact_role: adversarial-publication-utility-review
authors: [Codex]
status: complete
date: 2026-08-22
publication_status: private-not-approved
scope: MCRP distributed-review drafts Parts 2-12
review_posture: skeptical-time-poor-reader
---

# Adversarial utility review: MCRP Parts 2–12

## Bottom line

The eleven drafts are mature technical notes, but they are not yet an effective eleven-post public sequence. A skeptical reader will perceive one idea being repeatedly decomposed: bind review to exact scientific objects, separate machine observations from human decisions, preserve changes and disagreements as events, and test whether the resulting network helps. Repeating the authority boundary and prior-art catalogue in every post protects the claims but makes the series feel defensive and slow.

The public value is concentrated in five practical questions:

1. What exact evidence supports a claim, and what happens when it changes?
2. Which parts of review can agents do, and who remains accountable?
3. How can independent review products travel across institutions?
4. How could a living review network update without erasing history or disagreement?
5. How could this system fail, and what evidence would justify continuing?

Recommendation: keep the eleven drafts as a private design corpus and source material. Publish a shorter five-post arc after the existing Part 1. Merge aggressively, defer the standalone reputation post, replace recurring standards catalogues with one stable “foundations” box or landing page, and give every public post one operational artifact a reader can use.

## Utility test

A post earns a public slot only if a time-poor reader can answer, within the opening screen:

- Is this for me?
- What costly mistake does it prevent?
- What can I do differently after reading it?
- What does this add beyond the position paper and technical architecture supplement?
- Why should I care before MCRP has a working distributed implementation?

“It completes the conceptual architecture” is not sufficient. The reader needs a decision rule, checklist, worked failure, or testable design constraint.

## Per-post findings

### Part 2 — From claims to evidence

**Target reader:** Computational researchers, reproducibility reviewers, research-software engineers, and agents assembling evidence packets.  
**Concrete problem solved:** Prevents a successful rerun or rerender from being mistaken for support of the paper’s actual claim.  
**Actionable takeaway:** Maintain separate derivation and claim paths; declare evidence relations and acceptance conditions; when a dependency is unresolved, report the exact boundary rather than failing or blessing the whole paper.  
**Value beyond the supplements:** The claim/derivation distinction is already present in the position paper, but the calibration and negative-result examples make it teachable and usable. This is pedagogical value, not a new technical contribution.  
**Reason to read now:** Agents increasingly produce “reproducibility succeeded” reports; teams need a vocabulary for preventing a machine success from laundering an unsupported scientific claim.  
**Redundancy:** Overlaps Part 4 on dependency changes, Part 9 on review scope, and the position paper’s SRR/claim graph.  
**Likely drop-off:** The object vocabulary, tuple, diagram, and long prior-art paragraph arrive before the reader has extracted a lightweight method.  
**Recommendation:** **Merge with Part 4.** Keep the opening, one calibration example, a compact claim/evidence checklist, and the rule for changed dependencies.

### Part 3 — Who is allowed to say it passed?

**Target reader:** Teams using agents or automated checks in peer review; editors, methods reviewers, and workflow designers.  
**Concrete problem solved:** Prevents execution status, policy conformance, reviewer authority, and scientific acceptance from collapsing into one green check.  
**Actionable takeaway:** Type every output as an observation, agent report, policy projection, or human disposition; record who adopts agent work and for what scope.  
**Value beyond the supplements:** The authority boundary is already central to the position paper. The useful addition is the four-layer table and the three-claim example, which turn a principle into an interface and governance rule.  
**Reason to read now:** Agent-assisted review is being operationalized before institutions have stable language for accountability. This post can provide that language immediately.  
**Redundancy:** Strong overlap with Part 9’s automation boundary and repeated passages across all later posts.  
**Likely drop-off:** Readers may feel the thesis is settled after the table; the remaining identity and standards discussion becomes repetitive.  
**Recommendation:** **Merge with Part 9.** Lead with “please review this paper is an underspecified work order,” use the four-layer table, then show work decomposition and explicit human adoption.

### Part 4 — What happens after acceptance?

**Target reader:** Maintainers of published computational work, repositories, journals, review services, and dependency-monitoring systems.  
**Concrete problem solved:** Prevents old approval from silently surviving corrections, successor releases, dependency drift, withdrawal, or revocation.  
**Actionable takeaway:** Treat acceptance as an immutable historical event; compute current standing separately; never carry approval forward solely because a label or digest is unchanged.  
**Value beyond the supplements:** It expands the position paper’s freshness and supersession sections with a precise state vocabulary and a useful release-to-successor timeline.  
**Reason to read now:** Software, data, and calibration dependencies change continuously, while review badges and citations usually do not expose the resulting scope change.  
**Redundancy:** Part 2 already motivates forward dependency traversal; Part 8 repeats the update loop.  
**Likely drop-off:** The stale/superseded/withdrawn/revoked taxonomy is valuable but reads like protocol documentation when detached from a reader workflow.  
**Recommendation:** **Merge with Part 2.** Make “approval has a history, not a halo” the second half of one high-utility claim-lifecycle post.

### Part 5 — A review need not belong to a journal

**Target reader:** Editors, scholarly-infrastructure builders, review communities, repositories, funders, and societies.  
**Concrete problem solved:** Shows how review functions can be allocated across accountable parties without requiring one platform to own the object, workflow, and endorsement.  
**Actionable takeaway:** Separate preservation, discovery, technical checking, scientific judgment, curation, appeals, and sanctions; identify the institution accountable for each.  
**Value beyond the supplements:** The function-allocation table is an accessible version of the distributed-architecture supplement’s “journal analogue.” The substantive architecture is largely the same.  
**Reason to read now:** Publish–review–curate systems and independent review services exist now, but their outputs remain hard to combine or interpret across institutions.  
**Redundancy:** Parts 6 and 7 supply the missing exchange and standing mechanisms; alone, Part 5 risks being a conceptual reallocation exercise.  
**Likely drop-off:** The title attracts journal-reform readers but may repel editors or imply a journal-replacement thesis that the body disclaims. The long function table may feel descriptive rather than actionable.  
**Recommendation:** **Reframe and merge with Part 6.** Title around portable review products, not the absence of journals. Use one multi-party example and one responsibility matrix.

### Part 6 — Who said what about which release?

**Target reader:** Protocol designers, repository and identity-service engineers, scholarly-communications technologists, and review-platform architects.  
**Concrete problem solved:** Makes independently issued review observations and decisions discoverable against exact releases without turning registry inclusion into endorsement.  
**Actionable takeaway:** Separate registration, scientific activity, discovery, and federation; bind each attestation to an exact target, issuer, scope, policy, evidence set, and status.  
**Value beyond the supplements:** Almost all architecture appears in the distributed-review supplement. The worked event path is clearer than the supplement but does not add much new design.  
**Reason to read now:** Interoperability discussions can otherwise jump prematurely to “trust servers” without defining what a receipt, registry, or policy view actually means.  
**Redundancy:** High overlap with Parts 5 and 8 and the supplement’s trust-node, attestation, and event-loop sections.  
**Likely drop-off:** The third paragraph is an acronym wall; a general scientific reader may stop before reaching the useful four-operation distinction.  
**Recommendation:** **Merge with Part 5 and radically compress.** Put standards in a linked foundations box. Show one portable review bundle and its accountable parties.

### Part 7 — Reputation and credit without a universal score

**Target reader:** Reviewer-routing designers, research societies, platform governance teams, and contributors concerned about credit or exclusion.  
**Concrete problem solved:** Prevents reviewer selection and recognition from collapsing expertise, conflict, diligence, prestige, agreement, and correctness into one score.  
**Actionable takeaway:** Keep credit, competency, authorization, and current reliability evidence separate; route under a published local policy; preserve newcomer and dissent pathways.  
**Value beyond the supplements:** The worked newcomer/dissenter routing example adds concreteness, but the underlying faceted-standing model is already in the architecture supplement.  
**Reason to read now:** Automated reviewer routing and reputation features can quickly harden into opaque prestige systems. The warning is timely even before MCRP exists.  
**Redundancy:** Parts 3, 5, 6, and 11 already cover identity, authority, institutions, registries, Sybils, and capture.  
**Likely drop-off:** The hypothetical candidate list feels like governance design for infrastructure that has not been prototyped. Readers may debate reputation policy instead of the narrower MCRP contribution.  
**Recommendation:** **Defer as a standalone post.** Preserve a short “no universal score” rule in the portable-review post. Revisit only after a prototype or reviewer-routing experiment supplies evidence and a concrete interface.

### Part 8 — A scientific network that keeps updating

**Target reader:** Research-infrastructure architects, dependency-monitoring teams, repositories, review networks, and technically inclined scientific leaders.  
**Concrete problem solved:** Connects corrections, reviews, and dependency changes to downstream claims so each reader or journal need not manually rediscover impact.  
**Actionable takeaway:** Model current state as a reproducible projection over append-only events; emit bounded impact candidates; expose completeness and partition states; reserve decisions for qualified humans.  
**Value beyond the supplements:** The nine-step loop closely follows the architecture supplement. The calibration partition/recovery case is the unique public value because it makes “living” and “self-updating” precise.  
**Reason to read now:** Research records are increasingly distributed and machine-consumed, but correction propagation remains document-centric and lossy.  
**Redundancy:** Part 4 covers freshness; Part 6 covers event exchange; Part 10 covers preserved disagreement.  
**Likely drop-off:** Nine numbered protocol steps are too many for a blog post, especially after another standards inventory. The central concept is buried.  
**Recommendation:** **Keep but reframe.** Open with the correction-propagation failure, define “self-updating” in one sentence, use the partition example, and collapse nine steps into publish → detect → route → decide → propagate.

### Part 9 — Review as a distributed workflow

**Target reader:** Editors, review coordinators, agent-workflow builders, data custodians, and teams commissioning computational review.  
**Concrete problem solved:** Converts “please review this paper” from an ambiguous request into bounded work objects with coverage, competency, conflict, access, resource, deadline, and completion conditions.  
**Actionable takeaway:** Write a versioned review request; decompose it by expertise and access; require explicit reports or unable-to-complete states; never treat workflow completion as consensus.  
**Value beyond the supplements:** The work-object concept is in the architecture supplement, but the detector example is an immediately reusable review-request template and handles restricted evidence better than the position paper.  
**Reason to read now:** Multi-agent and multi-specialist review fails at handoffs and hidden scope; teams can adopt this decomposition before implementing MCRP infrastructure.  
**Redundancy:** Part 3 supplies the authority taxonomy; Part 10 supplies disagreement outcomes.  
**Likely drop-off:** The complete request and four work objects are long. Readers need a downloadable template or compact schema to reward the effort.  
**Recommendation:** **Keep, merged with Part 3.** Make this the practical centerpiece: authority types plus a one-page review-request template.

### Part 10 — Disagreement is a scientific product

**Target reader:** Editors, review communities, dispute-resolution designers, open-review platforms, and scientific readers frustrated by flattened review outcomes.  
**Concrete problem solved:** Prevents incompatible, scoped findings from being destroyed by majority votes or a single final badge.  
**Actionable takeaway:** Store support, bounds, contradiction, failed reproduction, narrowing, and unassessed states separately; preserve access conditions, appeals, and adjudication history.  
**Value beyond the supplements:** The clinical timeline and explicit distinction between access failure and reproduction failure add meaningful explanatory value beyond the supplement’s invariants.  
**Reason to read now:** Agentic synthesis and ranking systems are especially prone to flattening dissent into scores or consensus summaries.  
**Redundancy:** Part 11 repeats retaliation, Sybil, confidentiality, moderation, and capture concerns.  
**Likely drop-off:** The long clinical example and safeguards section turn one sharp thesis into two posts. Some readers will leave once the typed-relations principle is clear.  
**Recommendation:** **Merge with Part 8 for the main sequence.** Preserve a shorter disagreement example in the living-network post; retain the full draft as a later focused essay if audience response warrants it.

### Part 11 — How the trust layer fails

**Target reader:** Security, privacy, governance, and scholarly-infrastructure decision-makers; skeptics deciding whether MCRP deserves experimentation.  
**Concrete problem solved:** Prevents signatures, logs, federation, or decentralization from being mistaken for independence, legitimacy, capture resistance, or safety.  
**Actionable takeaway:** Threat-model review rings, registry control, and retaliation separately; expose residual risk; use “unknown” and human escalation rather than automated acceptance or accusation.  
**Value beyond the supplements:** The threats are listed in the architecture supplement, but the three scenarios and bounded dispositions make them legible and operational. This is one of the series’ strongest additions.  
**Reason to read now:** Trust infrastructure can become socially consequential before it is technically mature; failure constraints should shape prototypes, not follow them.  
**Redundancy:** Part 7 addresses prestige/Sybils, Part 10 addresses retaliation and abuse, and Part 12 maps the same threats into trials.  
**Likely drop-off:** Each scenario repeats mitigation-plus-residual-risk structure; without a compact threat table or explicit prototype gate, the post may feel cautionary rather than decision-relevant.  
**Recommendation:** **Merge with Part 12.** Use three threats to derive three stop conditions and one minimal experimental program.

### Part 12 — How we would know this helps

**Target reader:** Research-methods evaluators, funders, protocol designers, and leaders deciding whether to build or trial MCRP.  
**Concrete problem solved:** Prevents architectural richness from being presented as demonstrated improvement; converts claims into comparative trials and stop/narrow rules.  
**Actionable takeaway:** Compare against credible baselines; measure burden, epistemic performance, governance, privacy, and systems behavior; stop or narrow on harm or unexplained dispositions.  
**Value beyond the supplements:** The position paper names an evaluation agenda and the architecture supplement lists experiments. This draft adds prospective measures and thresholds, but the numerical margins are not yet justified.  
**Reason to read now:** It offers a disciplined answer to “why should anyone invest in this?” and can keep prototyping falsifiable.  
**Redundancy:** Part 11 supplies the threats; the technical documents already contain an evaluation agenda.  
**Likely drop-off:** The large preregistration table is dense, and arbitrary-looking thresholds can reduce confidence. A skeptical reader may mistake speculative numbers for protocol theater.  
**Recommendation:** **Merge with Part 11 and reframe.** Publish hypotheses, baselines, harms, and decision rules; defer numerical thresholds until domain and study-design review.

## Recommended shorter public sequence

The existing public Part 1 remains the entry point. Replace planned Parts 2–12 with five posts:

### Public Part 2 — A rerun is not a justification

**Source material:** Current Parts 2 and 4.  
**Promise:** Show readers how to connect a claim to its actual evidence and how that standing changes when a dependency changes.  
**Utility artifact:** A compact claim–evidence–freshness checklist with one calibration example.  
**Cut:** Most standards inventory, duplicate authority language, and the full state taxonomy unless needed in the example.

### Public Part 3 — What agents can check—and who remains accountable

**Source material:** Current Parts 3 and 9.  
**Promise:** Turn an underspecified review request into bounded machine and human work.  
**Utility artifact:** A one-page review-request template plus the observation/report/projection/disposition table.  
**Cut:** Repeated general defenses of human authority after the rule has been made explicit.

### Public Part 4 — Portable review without a universal platform

**Source material:** Current Parts 5 and 6, with one paragraph from Part 7.  
**Promise:** Explain how a compute center, methods society, archive, journal, and curation group can publish compatible, scoped review products without giving a registry scientific authority.  
**Utility artifact:** A responsibility matrix and the minimum fields of a portable review record.  
**Cut:** The provocative anti-journal title, acronym catalogue, speculative reviewer-ranking design, and standalone reputation post.

### Public Part 5 — A scientific record that can change without rewriting history

**Source material:** Current Parts 8 and 10.  
**Promise:** Define a living network as append-only events plus recomputed views, including corrections, partitions, disagreement, and access limits.  
**Utility artifact:** A five-step event loop and one correction/disagreement timeline.  
**Cut:** Nine-step protocol enumeration and duplicate standards material.

### Public Part 6 — How this trust layer could fail—and how we would test it

**Source material:** Current Parts 11 and 12.  
**Promise:** Make the case for a bounded prototype by deriving tests and stop conditions from review rings, captured registries, and retaliation risk.  
**Utility artifact:** Threat → mitigation → residual risk → experiment → stop rule table.  
**Cut:** Unreviewed numerical effect margins; retain them in the private study-design packet until justified.

## Proposed release cadence

Publish no faster than one post per week. The public sequence is conceptual and cumulative, not news-driven. Between posts, use reader questions and observed confusion to revise later installments. Announce the complete five-post roadmap at Part 2, but approve and release each post separately.

A useful progression is:

1. Part 2: immediate reproducibility practice;
2. Part 3: agent workflow and accountability;
3. Part 4: institutional interoperability;
4. Part 5: living-network architecture;
5. Part 6: adversarial tests and decision to proceed.

This creates an escalation from a problem readers already have to infrastructure they may eventually choose to build.

## Cross-series revisions that would materially increase utility

1. **One public foundations page.** Cite trust registries, transparency, notification, identity, content-addressing, and publish–review–curate once in a maintained page. Each post should link to it and cite only the two or three sources necessary for its argument.
2. **One operational artifact per post.** Checklist, template, record schema, event diagram, or threat/test table. Without these, the series remains commentary on its own architecture.
3. **Lead with the failure, not MCRP.** The first screen should name the reader’s current costly mistake. Introduce MCRP only after the problem is concrete.
4. **State the delta from the supplement.** Each post should say what it contributes: a worked example, practical template, interface rule, or evaluation decision—not another restatement of the architecture.
5. **Use a single authority box.** Reuse a compact visual legend for proposal, evidence, observation, agent report, policy projection, and human disposition. Do not restate the full boundary in every section.
6. **Separate design rules from evidence.** Mark what is proposed, what follows from prior art, what has been synthetically exercised, and what remains untested.
7. **End with a reader action.** Ask the reader to apply the checklist, critique the work-order template, identify an interoperability partner, or challenge an experiment—not merely continue to the next post.

## Publication disposition

- **Keep as public cores after merging:** current Parts 2, 3, 4, 8, 9, 11, and 12.
- **Reframe and merge:** current Parts 5, 6, and 10.
- **Defer as a standalone public post:** current Part 7.
- **Keep all eleven privately:** they remain useful as the detailed design corpus, reference material, and source text for the five-post public arc.

No post in the current eleven-part form should be automatically released merely because it meets the private maturity rubric. The next gate should assess the merged five-post arc for reader utility, source accuracy, privacy, and explicit management approval.

