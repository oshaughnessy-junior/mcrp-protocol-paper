# Evaluation questions

The position paper does not claim answers to these questions. They define the empirical program required for a later research article.

1. Does a prospective MCRP contract reduce unsupported completion declarations compared with a repository plus flat run logs?
2. Does it improve localization of missing, contradictory, or stale evidence compared with PROV-only capture?
3. How much reviewer time is spent per material claim under each assurance level?
4. Which defects are caught mechanically, by reproducibility reviewers, and by domain reviewers?
5. How reliably do dependency changes invalidate affected claim states and attestations?
6. How do full, slice, checkpoint, and witness modes trade cost against claim coverage?

## Distributed-review and trust-layer questions

7. Can independently implemented trust nodes exchange the same review, challenge, revocation, and supersession events without losing scope or changing meaning?
8. Can two nodes reproduce the same current standing from the same events and policy, while producing explainably different standings under different declared policies?
9. Which identity, competence, conflict, and independence signals reduce false authority without excluding qualified newcomers or laundering institutional prestige?
10. How do faceted reviewer histories compare with scalar reputation scores under review rings, Sybil identities, minority-correct reviewers, and later-overturned consensus?
11. Can distributed division of review labor reduce omissions or reviewer burden without increasing handoff loss, duplication, or false confidence?
12. How quickly and accurately do challenges, withdrawals, key revocations, scientific retractions, and freshness events propagate across partially connected nodes?
13. Can users distinguish log inclusion, process completion, community endorsement, and scientific support in realistic interfaces?
14. Does policy-visible plural review improve disagreement localization and correction compared with repository-plus-open-review and publish–review–curate baselines?

These questions test a proposed architecture. They do not imply that trust-node federation, reviewer reputation, or distributed review improves science.

## Minimum comparison design

- Predeclare workflows, claim targets, corruptions, stopping rules, and adjudication.
- Compare at least: flat logs, provenance capture alone, and MCRP.
- Report unsupported-completion rate, material-defect detection, review time, disagreement localization, and recovery after interruption.
- Separate synthetic corruption detection from evidence about real scientific review.
- For trust-layer studies, report Sybil/collusion assumptions, identity and conflict ground truth, node governance, policy versions, privacy harms, censorship or equivocation tests, and newcomer participation.
