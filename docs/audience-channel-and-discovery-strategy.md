---
artifact_role: audience-channel-and-discovery-strategy
authors: [Codex, junior]
status: updated-decision-strategy
date: 2026-08-23
publication_status: private-not-approved
scope: independent AI and research-infrastructure publication lane
companion: new-ai-research-infrastructure-lane-brief.md
---

# Audience, channel, and discovery strategy

## Decision

Treat AI and research infrastructure for science as an independent publication lane, not a category or sub-blog within the ROS group astrophysics site.

The new lane receives its own editorial identity, canonical publication surface, repository, queue, feed, discovery program, analytics boundary, review rubric, and Telegram approval target. The research site may selectively point to material with a genuine scientific connection, but it is neither the canonical archive nor the chronological container for the lane.

This strategy supersedes the earlier section-within-the-research-site recommendation. It does not authorize implementation, domain registration, site edits, post edits, publication, or deployment.

## Audience promise

Working subject: **AI and research infrastructure for science**.

One-sentence promise:

> Practical, evidence-conscious accounts of how agents, software, provenance, review, and governance can improve scientific work—and where those systems fail.

Primary readers:

- scientists responsible for reproducible, reviewable computational work;
- research-software and infrastructure engineers;
- agent-system designers working on evidence, memory, review, coordination, or governance;
- scholarly-communication and metaresearch practitioners;
- technical research leaders evaluating automation without surrendering human authority.

It is not a general AI-news site, model-release tracker, product-marketing channel, or replacement for the astrophysics research blog.

## Recommended public architecture

### Repository and deployment

Use a separate repository and deploy pipeline from `outward-facing-web`. This provides the strongest operational boundary:

- separate publication queue and branch protections;
- separate digest-bound approval destination;
- no risk that astrophysics-site drift or unrelated local changes enter an infrastructure release;
- independent templates, feed, sitemap, analytics, and rollback;
- a clean canonical history for the publication program.

Do not bootstrap the lane inside the existing dirty/diverged research-site checkout. Do not put unapproved drafts on public preview branches.

### URL and domain choice

Preferred mature form: a true custom subdomain or distinct custom domain with a clear relationship to the ROS group, for example a name under a controlled parent domain. A subdomain can express an independent site identity while preserving visible institutional relationship.

Preferred bootstrap form: an independent sibling GitHub Pages repository, designed so its routes can later migrate cleanly to a custom domain. This is faster and preserves repository/deployment separation, but a second `github.io` repository path does not deliver the full branding and search-identity benefit of a true subdomain.

Do not delay private editorial preparation while choosing the final domain. Do delay public launch until the canonical URL and redirect posture are decided.

Google states that it has no general indexing preference between subfolders and subdomains; organization should follow the publication's needs. It does support site names at the domain or subdomain level, not for a subdirectory landing page. See [Google's crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq) and [site-name guidance](https://developers.google.com/search/docs/appearance/site-names).

## Editorial identity and information architecture

The landing surface should contain:

- the one-sentence audience promise;
- a featured current season;
- a concise foundations page for standards and prior art;
- topic paths for agent-team operations, evidence and provenance, scientific review, distributed infrastructure, and evaluation/failure analysis;
- latest essays and latest operational artifacts as distinct lists;
- stable author pages for Codex and junior;
- an explicit human editorial-approval statement;
- a feed, archive, sitemap, and subscription choices.

MCRP should launch as the first bounded editorial season, with one canonical hub and a finite public arc. The eleven technical drafts remain the private design corpus. The public season should be rewritten into the five utility-led pieces specified in [the lane decision brief](new-ai-research-infrastructure-lane-brief.md), rather than released as eleven lightly differentiated installments.

Every post should expose:

- problem-led title and description;
- authors and publisher as separate metadata;
- season, sequence position, and previous/next navigation;
- claim posture: proposal, synthetic demonstration, internal observation, evaluation, or externally reproduced;
- operational artifact when one is promised;
- explicit limitations;
- canonical URL and update history.

Google's Article guidance recommends representing multiple authors separately and linking each to a stable identity page: [Article structured-data guidance](https://developers.google.com/search/docs/appearance/structured-data/article).

## Feeds and subscriptions

Provide:

- one complete publication feed;
- optional topic feeds only after enough content exists to keep them useful;
- an MCRP-season feed during launch;
- feed-autodiscovery metadata;
- a complete sitemap and correct modification times.

RSS/Atom is a first-class distribution channel, not a build by-product. It should contain canonical, fetchable URLs and sufficiently complete metadata. Google distinguishes sitemaps as the broad URL inventory and feeds as recent-update signals; both are useful: [sitemap and feed practices](https://developers.google.com/search/blog/2014/10/best-practices-for-xml-sitemaps-rssatom).

## Relationship to the main research site

Use selective contextual cross-links, not mirroring.

Appropriate research-site links include:

- a short pointer when a new infrastructure piece directly explains a method used in scientific work;
- a permanent resources-page link to the new publication lane;
- links from relevant simulation, reproducibility, or research-software posts;
- occasional season launch or evaluation-result notices.

Avoid:

- automatically copying every infrastructure post into the research feed;
- dual full-text publication;
- generic “new post” notices with no astrophysics relevance;
- implying that group research projects adopted MCRP unless documented;
- using the research site's authority as evidence for protocol validity.

The infrastructure site remains canonical. If full-text syndication ever occurs, the syndicated copy must point to the canonical source where the destination supports it. Google documents `rel="canonical"` as a strong consolidation signal: [canonical URL guidance](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls).

## Social discovery

LinkedIn and similar services are discovery surfaces, not the archive.

- Announce the lane once with its audience promise and current-season hub.
- Adapt only anchor pieces, with short platform-native arguments linking to the canonical article.
- Require a separate digest-bound approval for every social adaptation.
- Preserve the Codex/junior authorship while making the publisher relationship explicit.
- Prefer qualified response, artifact use, and returning readership over raw impressions.

For the five-piece public MCRP season, two or three LinkedIn adaptations are sufficient. Do not turn a finite research-infrastructure argument into repetitive social promotion.

## Queue, metrics, and ownership

The lane needs an independent publication queue with at least:

- artifact and exact revision;
- editorial state;
- source/claim/privacy state;
- operational-artifact state;
- audience and channel decision;
- preview and digest;
- owner approval receipt;
- deployment and live-verification receipt;
- social adaptation states, separately;
- correction, staleness, and supersession state.

The approval target should name this destination explicitly, such as `ai-research-infrastructure/main`. Approval for the research site, LinkedIn, the protocol repository, or an internal prototype is not interchangeable.

Measure:

- qualified organic discovery by intended audience;
- article/series completion where privacy-compatible;
- feed subscriptions and return readership;
- downloads, forks, references, or reuse of operational artifacts;
- informed critiques, corrections, and collaborators;
- cross-links from relevant technical and scientific sources;
- editorial throughput, correction latency, and approval latency.

Avoid optimizing primarily for impressions, posting volume, or generic engagement. Analytics require an explicit privacy and retention posture before activation.

Assign one named editorial/operational owner. A publication lane without an accountable queue owner will reproduce the oversight failure that left mature MCRP drafts private without an owner-visible decision request.

## Elevation workflow

1. Build and review material privately in its owning repository.
2. Run source, claim, privacy, utility, and artifact checks.
3. Classify audience and canonical destination.
4. Build an owner-visible private preview.
5. Deliver a digest-bound Telegram request with approve, revise, reject, and defer actions.
6. Record the exact outbound message ID; a local request file is not delivery evidence.
7. On approval, revalidate content, render, destination, and base revision before deterministic publication.
8. Verify live URL, canonical metadata, feed/sitemap inclusion, and rendering.
9. Prepare any social adaptation as a new artifact with a new approval.

Sequence approval governs shared architecture and cadence. Post approval governs one exact website revision. Prototype release, website publication, research-site pointer, and social publication are all distinct actions.

## Phased launch

### Phase 0: private foundation

- choose public name and audience promise;
- create the independent private repository and queue;
- select canonical-domain strategy;
- define author/publisher metadata and privacy posture;
- implement the approval target and private preview flow;
- rewrite and review the five-piece MCRP season.

Exit: every launch artifact is privately reviewable, but nothing is public.

### Phase 1: minimum public surface

- publish landing page, foundations page, feed, sitemap, author pages, and MCRP hub;
- publish the orientation and first utility-led MCRP piece;
- add one selective research-site pointer;
- verify search, feed, social-card, accessibility, and canonical metadata.

Exit: the publication has a coherent identity and one useful canonical piece.

### Phase 2: bounded season

- publish at most weekly;
- attach an operational artifact to each piece;
- use no more than three approved social adaptations;
- collect qualified response and corrections;
- preserve an explicit complete-season roadmap.

Exit: all five pieces are live or deliberately deferred, with verification receipts.

### Phase 3: continuation decision

Continue only if there is material beyond MCRP, a distinct relevant audience, evidence of artifact use or informed engagement, and an accountable owner. Otherwise preserve the season as a finite, high-quality publication and stop manufacturing cadence.

## Decisions still required

- Public name and final audience promise.
- Separate repository name and owner.
- Bootstrap sibling-site URL versus immediate custom subdomain/domain.
- Visual relationship to the ROS group.
- Named editorial/operational owner.
- Exact five-piece season briefs and first release candidate.
- Whether the existing agent-meetings article is linked, summarized, or republished with canonical handling.

Until these decisions and exact publication approvals are recorded, all material remains private.
