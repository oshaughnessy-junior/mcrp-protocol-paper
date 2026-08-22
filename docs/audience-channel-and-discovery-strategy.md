---
artifact_role: audience-channel-and-discovery-strategy
authors:
  - Codex
  - junior
status: recommendation-for-human-review
date: 2026-08-22
publication_status: private-not-approved
scope: MCRP and adjacent research-infrastructure and agent-systems writing
---

# Audience, channel, and discovery strategy for MCRP

## Recommendation

Publish MCRP and closely related material on the existing ROS group web property, but not as undifferentiated entries in the astrophysics news stream. Establish a first-class **Research Infrastructure & Agent Systems** section within the same site, with its own landing page, category feed, series hubs, descriptive metadata, and subscription route. Treat MCRP as the anchor sequence for that section.

Do not create a separate AI-infrastructure site or subdomain yet. Reconsider that choice only after the section demonstrates a sustained body of work beyond MCRP, a distinct returning audience, an independent editorial identity, and enough publication cadence to justify separate operations.

This is a channel and information-architecture recommendation only. It does not authorize site edits, publication, deployment, social posting, or a domain change.

## Why MCRP belongs on the research property

MCRP is not primarily a product-development diary or generic commentary about AI. Its central subject is scientific review: how claims refer to exact evidence, how review authority is scoped, how decisions become stale, and how distributed records might support a living review network. Agent automation is an enabling mechanism and an important audience, but the intended consequence is research infrastructure.

The existing site is publicly framed as a research-group presence focused on gravitational waves and astrophysics. It already carries a small agent-systems lane, including OpenClaw workflow posts and the agent-meetings/self-improvement post. MCRP therefore does not introduce the first cross-disciplinary material; it exposes that the current taxonomy and navigation are too weak to explain the relationship among the site's subjects.

Keeping the canonical MCRP sequence on the research property has three immediate advantages:

1. It connects the proposal to concrete scientific practice rather than presenting it as abstract AI governance.
2. It retains one accumulated link, search, analytics, and maintenance surface.
3. It lets astrophysics readers encounter the infrastructure argument while letting systems readers subscribe to a narrower lane.

The required correction is not a new domain. It is a visible editorial partition.

## Option comparison

| Criterion | Mixed main blog with no partition | Section on the main site | Separate AI site or subdomain |
|---|---|---|---|
| Audience clarity | Poor: readers cannot predict whether a post is astrophysics, lab news, or agent infrastructure | Strong if the section has a distinct name, landing page, feed, and visual label | Strongest subject separation |
| Scientific positioning | Strong association with active research, but agent posts may appear incidental | Strong association while making infrastructure an explicit research program | Risk that MCRP reads as generic AI commentary rather than science infrastructure |
| Discoverability at launch | Benefits from existing internal links and site history | Same benefit, with better topical clustering | Starts with a thinner link graph and a new discovery surface |
| Brand risk | High: unexplained topic switching dilutes the site's astrophysics promise | Manageable: one publisher, two clearly named editorial lanes | High initial risk of an unestablished second brand and unclear relationship to ROS group |
| Subscription control | One noisy feed | Global feed plus section- and series-specific feeds | Clean separate feed, but readers and mailing lists fragment |
| Search identity | One site identity | One site identity; section pages cannot obtain a distinct Google site name | A subdomain can support a distinct site name, but must earn its own identity |
| Cross-posting risk | Low if there is one canonical page | Low; one canonical page plus short adaptations | Higher temptation to duplicate articles across two sites; canonical handling becomes mandatory |
| Maintenance | Lowest, but editorial quality suffers | Modest incremental templates, taxonomy, and feed maintenance | Highest: separate navigation, analytics, Search Console, deploys, security, archives, and redirects |
| Future extensibility | Weak | Strong enough for MCRP and adjacent sequences | Best only if a durable independent publication actually emerges |

Google states that it has no general indexing or ranking preference between subfolders and subdomains; the choice should follow organizational needs. A meaningful distinction is branding: Google can show a separate site name for a subdomain, but not for a subdirectory-level home page. That branding advantage is real, but it is not sufficient reason to split a young publication. See [Google's crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq) and [site-name guidance](https://developers.google.com/search/docs/appearance/site-names).

## Proposed information architecture

### Publisher level

Keep the publisher identity as the ROS group web presence. Its top-level navigation should make the two relevant editorial lanes legible:

- **Astrophysics & Group Research**
- **Research Infrastructure & Agent Systems**

The second label is preferable to “AI blog.” It describes the durable problem domain and leaves room for non-agent infrastructure, reproducibility, review protocols, research software, provenance, and evaluation. “AI” alone invites an audience expecting model news, tutorials, or product commentary that the MCRP sequence does not provide.

### Section level

The Research Infrastructure & Agent Systems landing page should contain:

- a two-sentence statement connecting automation to scientific accountability;
- three topic clusters: **agent-team operations**, **research provenance and review**, and **distributed scientific infrastructure**;
- a featured-series panel for MCRP;
- the latest posts in the section;
- a section-specific Atom/RSS subscription link;
- a link back to the astrophysics/research context that motivates the work.

Use a stable descriptive route such as `/research-infrastructure/`. Do not lead the URL with the internal acronym `mcrp`; descriptive URLs are more intelligible to new readers. Google's URL guidance recommends simple, readable words that match the audience's language: [URL structure best practices](https://developers.google.com/search/docs/crawling-indexing/url-structure).

### Series level

Give MCRP one canonical series hub under that section. The hub should answer four questions before listing posts:

1. What is the practical problem?
2. What does MCRP propose?
3. What has and has not been demonstrated?
4. Where should a reader start?

Offer three reading paths:

- **Five-minute orientation:** position-post introduction and one architecture diagram.
- **Core protocol:** Parts 2–4, from claims and evidence through authority and revision.
- **Distributed-review arc:** Parts 5–12, including registries, reputation, event-driven updating, failure modes, and evaluation.

Every installment should expose the series title, part number, previous/next links, hub link, authors, publication/update dates, and a compact “claim posture” box. The title should lead with the reader's problem rather than the acronym—for example, “Why scientific approval needs a version history — MCRP, Part 4.”

The PDF and protocol repository should be companion artifacts linked from the hub, not competing canonical copies of the blog prose.

### Metadata and authorship

Normalize front matter across the lane:

- `section: research-infrastructure`
- `series: mcrp`
- `series_part: N`
- `authors: [Codex, junior]`
- `description:` one search- and feed-appropriate summary
- `canonical_url:` the single canonical article location
- `claim_posture:` proposal, prototype, evaluated, or retrospective
- topic tags drawn from a controlled vocabulary rather than ad hoc synonyms

The current site disables Open Graph and Schema.org output and uses inconsistent author/category metadata across posts. Before the sequence is promoted, the publication packet should verify social-card metadata and `BlogPosting`/`Article` author representation. Google's Article guidance recommends representing multiple authors separately and linking each to a stable author identity page rather than combining names into one author string: [Article structured-data guidance](https://developers.google.com/search/docs/appearance/structured-data/article).

The byline remains **Codex and junior**, as already specified for the sequence. The publisher and authors should be distinct metadata fields. The series hub should also explain, briefly and plainly, what those author identities mean and where human editorial approval enters the process.

## Feeds, subscriptions, and internal discovery

Retain one global feed for readers who want the whole research-group publication stream, but add:

- a Research Infrastructure & Agent Systems category feed;
- an MCRP series feed;
- feed-discovery links in the relevant landing-page HTML;
- visible subscription choices labeled by scope.

Jekyll has first-class categories and tags, and `jekyll-feed` supports category feeds. This is a small conceptual extension of the present stack rather than a second publishing system. See the [Jekyll post taxonomy documentation](https://jekyllrb.com/docs/posts/) and [jekyll-feed documentation](https://github.com/jekyll/jekyll-feed).

Use both the sitemap and recent-update feeds. Google describes sitemaps as the broad URL inventory and RSS/Atom as a timely update signal; both should carry canonical, fetchable URLs and correct modification times: [sitemap and feed practices](https://developers.google.com/search/blog/2014/10/best-practices-for-xml-sitemaps-rssatom).

Internal discovery should not rely on chronology alone. Add contextual links:

- astrophysics or simulation posts can link to relevant MCRP posts when provenance or review is genuinely involved;
- agent-team posts can link forward to the MCRP hub as the scientific-accountability arc;
- MCRP posts should link to concrete scientific examples without implying those projects adopted the protocol;
- the position-paper landing page should link to the public series hub and repository;
- repository READMEs should point back to the canonical public explanation.

## Social and cross-posting strategy

The website remains canonical. LinkedIn and similar channels are discovery surfaces, not duplicate archives.

For the MCRP sequence:

- announce the series once with the hub and its central thesis;
- adapt only anchor installments for LinkedIn: Parts 2, 5, 8, 11, and 12 are the strongest candidates;
- use short platform-native summaries that link to the canonical article;
- do not publish eleven near-identical “new part” announcements in rapid succession;
- package Parts 2–4 and Parts 5–12 as recognizable arcs with recap posts or threads;
- require separate approval for each website publication and each social adaptation.

If a full article is ever syndicated, set the original website URL as canonical when the destination supports it. Canonicalization consolidates signals and avoids competing copies; Google documents redirects and `rel="canonical"` as strong signals: [canonical URL guidance](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls).

## Release cadence

Publish the series as a bounded editorial season rather than an undifferentiated backlog dump.

Recommended pattern:

1. Series hub plus the short position introduction.
2. Parts 2–4 at roughly one post per week.
3. A brief synthesis and explicit opening of the distributed-review arc.
4. Parts 5–12 at one post every one to two weeks, with grouping and recap links.
5. Evaluation and protocol updates only when new evidence exists; do not manufacture cadence after the numbered arc.

This cadence gives each argument time to be discovered and discussed, while maintaining enough continuity for the sequence to remain legible.

## Elevation and approval workflow

Audience/channel review should become a mandatory stage before the existing publication gate.

For each mature post, the producing agent should prepare a small channel packet containing:

- exact draft and rendered-preview digests;
- recommended canonical section and series position;
- primary audience and excluded audience;
- search-facing title, description, and intended query vocabulary;
- internal links in and out;
- feed/category metadata;
- proposed social adaptations, if any;
- risks: brand confusion, unsupported scientific implication, privacy, or authorship ambiguity;
- explicit choices for Richard: approve website publication, revise, defer, or reject.

The agent then builds an owner-visible private preview and sends a Telegram approval request bound to the exact packet. A button tap is a decision signal, not a memory substitute: the executor must revalidate the stored packet, source digest, preview digest, destination, and current site base before publishing.

Sequence-level oversight and per-post authority should remain separate:

- **Sequence approval** confirms the information architecture, order, cadence, and shared framing.
- **Post approval** authorizes one exact website revision.
- **Channel approval** separately authorizes each LinkedIn or other social adaptation.
- **Deployment verification** records the live URL, canonical metadata, feed inclusion, and rendered result.

The escalation invariant should be: once a post reaches `verified-for-human-review`, the workflow must deliver one durable owner-visible request and record its Telegram message ID. A local review-request file is not evidence that oversight occurred.

## When a separate site becomes justified

Reassess a dedicated site or true subdomain when most of the following are true:

- the infrastructure lane contains at least two substantial programs beyond MCRP;
- it sustains publication for at least six months rather than one finite sequence;
- analytics show a distinct returning audience with limited overlap with the astrophysics stream;
- readers request an independent subscription or community identity;
- contributors or editorial governance differ materially from the research-group blog;
- the section needs its own homepage promise, newsletter, event calendar, or participation model;
- operating a separate deploy, accessibility check, analytics property, Search Console property, archive, and redirect policy has a named owner.

If those conditions emerge, prefer a true subdomain with a clear relationship to the ROS group publisher. Move canonical URLs once, issue redirects, preserve feed continuity where possible, and avoid maintaining duplicate full-text copies. A separate repository served only as another `github.io` path would split operations without delivering the full branding benefit of a subdomain.

## Near-term editorial decisions for Richard

1. Approve or revise the section name **Research Infrastructure & Agent Systems**.
2. Confirm the existing ROS group site as the canonical publication property for the first MCRP season.
3. Approve the three-path series hub and the staged cadence.
4. Select the first three posts for exact publication review; Parts 2, 3, and 4 are the coherent starting arc.
5. Decide whether LinkedIn adaptations should use the Codex/junior byline explicitly or a publisher-prefaced form such as “From the ROS group agent team.”

Until those decisions are recorded, the MCRP drafts remain private and no channel is authorized.
