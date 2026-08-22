---
artifact_role: editorial-lane-decision-brief
authors: [Codex, junior]
status: recommendation-for-human-review
date: 2026-08-22
publication_status: private-not-approved
supersedes: audience-channel-and-discovery-strategy.md section-only recommendation
---

# A distinct AI and research-infrastructure publication lane

## Decision

Treat this work as a new editorial and operational lane, not a category added to the astrophysics blog. The lane should have its own audience promise, publication queue, review rubric, approval target, landing surface, feed, distribution plan, metrics, and named operator. The research site may feature selected links, but it should not be the canonical chronological container for the program.

Working scope: **AI and research infrastructure for science**. The durable subject is how agents, software, provenance, review, and governance change scientific work—not general model news and not another stream of group announcements.

## What the lane publishes

The lane is broader than a blog:

- concise problem-led essays;
- protocols and position notes;
- reusable checklists, schemas, templates, and reference implementations;
- worked scientific examples;
- adversarial reviews and failure analyses;
- evaluation plans and, later, empirical results;
- versioned technical supplements and change notes.

MCRP can be its first bounded editorial season, but the lane should also accommodate agent-team coordination, research-librarian infrastructure, evidence workflows, scientific-writing controls, and evaluated automation patterns.

## Launch architecture

1. Create an independent repository and deployment target for the lane. Do not reuse the dirty or diverged `outward-facing-web` checkout as its production surface.
2. Give the lane a dedicated landing page, archive, MCRP hub, RSS/Atom feed, sitemap, social metadata, structured article metadata, and stable author pages for Codex and junior.
3. Keep one canonical copy of every article in the new lane. The astrophysics site should carry short, selective pointer posts only when the scientific connection is genuine.
4. Use the digest-bound Telegram approval workflow with a distinct destination such as `research-infrastructure-lane/main`. Approval for the astrophysics site, this lane, LinkedIn, or any other channel is never interchangeable.
5. Launch with a short manifesto/orientation, the existing agent-meetings essay where appropriate, and a five-post utility-focused MCRP season—not the eleven current technical drafts.

A custom subdomain would give the cleanest public identity, but domain selection is a separate human decision. An independent sibling GitHub Pages repository can bootstrap the lane while preserving operational separation; if used, choose URLs and redirects with a later custom-domain migration in mind.

## MCRP launch season

Keep Parts 2–12 as the private design corpus. Rewrite them into five public pieces:

1. **A rerun is not a justification** — claim, evidence, and freshness checklist.
2. **What agents can check—and who remains accountable** — typed authority and review-request template.
3. **Portable review without a universal platform** — responsibility matrix and minimum portable record.
4. **A scientific record that can change without rewriting history** — event loop and disagreement timeline.
5. **How this trust layer could fail—and how we would test it** — threat/test/stop-rule table.

Release at most weekly. Every piece must ship with an operational artifact and pass a reader-utility review before the source/claim/privacy/publication gates.

## Discovery and elevation

- Lead titles and descriptions with the reader's problem, not “MCRP Part N.”
- Maintain a foundations page for standards and prior art so each essay does not repeat an acronym catalogue.
- Use the main research site and relevant repositories for contextual inbound links.
- Adapt only anchor pieces for LinkedIn; each adaptation gets a separate digest-bound approval.
- Announce a bounded season with a stable hub and complete roadmap.
- Add Search Console/analytics only with an explicit privacy posture; measure discovery, completion, artifact use, qualified responses, and return readership—not raw impressions alone.
- Elevate mature artifacts automatically to Richard for oversight; silence is neither approval nor successful delivery.

## Success and stop criteria

Review after the first season. Continue if the lane attracts a distinct relevant audience, produces reuse of its operational artifacts, generates informed collaborators or critiques, and can sustain material beyond MCRP. Narrow or stop if it becomes repeated position-paper summary, cannot maintain an independent cadence, fragments attention without useful engagement, or lacks an accountable operator.

## Decisions still required

- Public name and one-sentence audience promise.
- Repository and URL/subdomain.
- Visual identity and relationship to the ROS group publisher.
- Named editorial/operational owner.
- Whether the existing agent-meetings post is republished, summarized with a canonical pointer, or simply linked.
- Approval to rewrite the five-post MCRP public season; no current draft is authorized for publication.
