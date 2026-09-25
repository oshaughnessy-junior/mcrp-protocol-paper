# Response to review 1586: lightweight revision semantics

**Revision proposal, 25 September 2026.** This note answers the request for formal
review-graph, carry-forward, and invalidation semantics. It defines a candidate
profile and a new finite executable model. It does not assert that the historical
v0.1.2 implementation implemented these definitions. Its 16 new tests are not the
historical thirteen tests reported in the submitted manuscript.

## A. Review graph and edge direction

An SRR is represented for this purpose by a finite tuple

$$S=(r,V,\nu,C,D,R,N),$$

where $r$ is its immutable release identity, $V$ a set of stable logical object
identifiers, $\nu:V\to\mathcal I$ their exact version identities, $C\subseteq V$
the material claims, and $D,R,N$ typed directed edge sets. Version identities bind
all semantically material fields; for a claim these include text, scope,
assumptions, acceptance predicates, and required reviewer roles, not just its
prose. The finite toy uses version tokens supplied by the caller and does not
hash these fields or resolve artifacts. Real content hashing and version
resolution remain separate implementation duties.

All dependency edges point **upstream object → dependent object**. $D$ contains
computational `derives` relations and must be acyclic. For example, input data →
execution → output is an allowed derivation path. Iterative computation is
represented by distinct time/version-indexed executions or one bounded execution
object, not by a cyclic derivation between the same immutable objects.

$R$ contains declared review dependencies: `requires-evidence`,
`requires-authority`, and `requires-freshness`. These indicate that a change to the
upstream object requires reconsideration of the dependent object or decision.
Unlike $D$, these edges may form cycles. A mutually dependent set of review
obligations is traversable by a finite fixed-point computation; it is not a
proof of valid evidential support. $N$ contains `cites`, `contextualizes`, and
`contradicts` in this toy vocabulary. These edges are recorded but do not
propagate revision impact automatically. If a particular contextual citation or
counterargument is a material premise of a decision, the profile must additionally
record the corresponding edge in $R$. A typed contradiction edge alone does not
prove its target false.

Let $E=D\cup R$. Unknown edge types fail validation in the executable profile;
otherwise silently guessing whether an unknown relation propagates would make
implementations disagree. This is a proposed minimal relation profile, not a
finished mapping to every PROV or EVI predicate. A release must record any richer
propagation policy as a versioned dependency of the affected decisions.

## B. Delta roots and conservative reachability

Consider old and new releases $S,S'$ with $r\ne r'$, compared through stable logical
IDs. Define the version-change roots

$$\Delta_V=\{v\in V\cup V':v\notin V\cap V'\text{ or }\nu(v)\ne\nu'(v)\}.$$

Added, removed, and retyped propagating edges also change their target's declared
support contract. Define

$$\Delta_E=\{v:(u,v,t)\in E\mathbin{\triangle} E'\},\qquad
\Delta=\Delta_V\cup\Delta_E\cup(C\mathbin{\triangle}C')\cup\Delta_{event}.$$

The symmetric difference of material-claim sets is also dirty, so retiring a claim
cannot hide a scope change merely by preserving its object bytes.
Here $\Delta_{event}$ contains explicitly identified event roots even when bytes
are unchanged: a withdrawn authority, discovered calibration problem, freshness
expiry, or changed interpretation of an evidence object. An event root must name
an object in the comparison universe. Completeness of event detection is not
assumed or implemented. Claim split/merge mappings require separate treatment;
they are not automatically equated with an unchanged stable ID.

Define $A$ by the least fixed point

$$A_0=\Delta,\qquad
A_{k+1}=A_k\cup\{v:(u,v,t)\in E\cup E',\ u\in A_k\},\qquad
A=\bigcup_{k\ge0}A_k.$$

Affected claims are $A\cap(C\cup C')$. Traversing the union is deliberate:
deleting an old dependency must not erase the route through which an old decision
was supported. Added dependencies must likewise be reconsidered. Cycles can occur
in the union of two separately acyclic derivation graphs, even when neither graph
has review cycles; this closure does not require a topological ordering.

**Proposition S1 (termination and declared coverage).** For finite graphs the
closure reaches a fixed point after at most $|V\cup V'|$ strict expansions. It is
exactly the set of vertices reachable from $\Delta$ by zero or more edges of
$E\cup E'$. In particular every declared dependency path from a dirty root to a
claim causes that claim to be marked for reassessment.

*Proof.* Each strict expansion adds at least one previously absent vertex; there
are finitely many. By induction, every vertex added at step $k$ has a path of
length at most $k$ from a root, and each path of length $k$ has its final vertex
added by that step. The stable set is therefore the reachability set. $\square$

Adding roots or propagating edges cannot shrink $A$, by the same path argument.
The union may conservatively mark a path assembled from old and new edges that
never coexisted in either complete release. This is intentional overapproximation,
not a claim of minimal scientifically necessary rework.

The state implied by membership in $A$ is **needs reassessment for current use**.
It neither deletes a dated historical decision nor assigns scientific falsity.
Changing a compiler, losing data access, or revising calibration can affect the
available justification while leaving a conclusion true. Even the intended new
version of a claim can remain mathematically equivalent, which must be established
through a new decision rather than silently inferred from reachability.

## C. Eligibility is not automatic authorization

For an old decision $d$ on claim $c$, let $\operatorname{Approved}(d,r,c,\nu(c))$ mean a recorded
approved disposition bound to that exact old claim contract. This is historical
approval, so it is not enough for current carry-forward. For assessment time $t$
and policy identity $p$, define

$$\operatorname{Current}(d,t,p)\iff p_d=p\land t_{issue}\le t<t_{expire}\land
(t_{revoke}=\bot\text{ or }t<t_{revoke})\land
\neg\operatorname{pending}(d)\land\neg\operatorname{disputed}(d).$$

The fixture compares explicit integer times, a policy identity, and supplied
revocation/pending/dispute records. The expiry boundary is exclusive. A missing
assessment time or policy fails closed. This evaluates the provided status facts;
it cannot authenticate a clock, discover an undisclosed revocation, or guarantee
that a latest-status feed is complete. Production users must record the policy,
assessment time, status evidence, and monitoring boundary. Re-establishing approval
under a changed policy requires a new decision rather than treating old approval
as current by default. A successor mapping
$m(c)=\mathrm{unchanged}$ is necessary but must agree with exact contract identity.
Let $\sigma$ be a separately authorized scope-delta disposition naming
$(r,r',c)$, concluding `unaffected`, and covering claim scope, custody boundary,
plausible undeclared dependencies, and missing graph edges. Define

$$\operatorname{Eligible}(d,c,S,S',\sigma;t,p)\iff
\operatorname{Approved}(d,r,c,\nu(c))\land \operatorname{Current}(d,t,p)\land c\in C\cap C'\land
m(c)=\mathrm{unchanged}\land\nu(c)=\nu'(c)\land
c\notin A\land \operatorname{AuthorizedUnaffected}(\sigma;r,r',c).$$

**Proposition S2 (carry-forward barrier).** Under this predicate, no decision on a
declared reachable changed claim is eligible for direct carry-forward. Neither a
missing scope-delta disposition, an unbound disposition, nor a non-unchanged claim
mapping can independently be rescued by a quiet graph. A known expired, revoked,
pending, disputed, or wrong-policy prior approval is also ineligible, even when
no event root was supplied.

*Proof.* Each of those conditions falsifies an explicit conjunct. $\square$

The distinction between “necessary” and “sufficient” matters. The formula is
sufficient only for **eligibility under this declared policy and its trusted
inputs**. It is not sufficient for truth or real-world unaffectedness. A separately
authorized actor must still issue a new successor-bound carry-forward record that
references the old disposition and the delta decision. The toy returns eligibility
and never performs that transition. Original dated records remain intact. Role
qualification, authentic signatures, genuinely separate authority, trustworthy
contract hashes, and validity of the supplied scope-delta conclusion are external
premises. The fixture's allow-list tests a declared actor string; it does not
implement identity verification or prove independence.

## D. Counterexamples that implementations must retain

1. **Removed-edge laundering.** Old data → run → claim; the successor removes the
   data edge. A new-graph-only traversal misses the old support relationship.
   Dirty edge targets plus union traversal mark the claim for reassessment even
   when all remaining object version tokens are unchanged.
2. **Unchanged words, changed contract.** Claim text is identical but scope or
   acceptance tolerance changes. A mapping string `unchanged` is insufficient;
   the exact claim contract version changes and blocks direct carry-forward.
3. **Missing dependency.** Data also actually supports claim B, but that edge is
   absent in both declarations. A data change marks claim A and misses B. Requiring
   a delta disposition creates an explicit review obligation; an incorrect
   `unaffected` disposition can still allow B. The negative test preserves this
   failure instead of implying the graph discovered missing science.
4. **Context versus premise.** A contextual citation change does not automatically
   propagate. When it actually affects interpretation, the authorized delta review
   must identify it or the declared graph must promote it to a review dependency.
5. **Change is not refutation.** An obsolete calibration marks dependent use for
   reassessment, while the historical observation and historical decision remain.
   No Boolean truth field is produced by the algorithm.
6. **Review cycle.** Two review obligations reference each other. The fixed-point
   closure terminates, while the separate computational derivation DAG still
   rejects a data/run self-justification cycle.

## E. New executable evidence and response wording

`examples/revision-semantics/semantics.py` implements these finite graph and
eligibility operations. `test_semantics.py` contains **16 named new tests**,
including independent path enumeration of all 512 directed graphs on three
vertices, removed-edge and removed-node cases, scoped authority binding, unchanged
byte events, claim-contract changes, clock/policy/revocation guards, and deliberately
undetected hidden lineage.
It checks immutable in-memory snapshots but does not implement an archive.
`results.json` records two synthetic revisions and retains the no-truth-verdict
interpretation. From the repository root:

```sh
python3 -m unittest discover -s examples/revision-semantics -v
python3 examples/revision-semantics/semantics.py
```

These fixtures were added in response to review 1586. They are author-side internal
implementation evidence, not an independent scientific rerun, not the missing
historical v0.1.2 fixture mapping, and not a version-specific persistent archive.
The revision should state that distinction next to any new test count. This
appendix supplies explicit semantics for a lifecycle policy, not a claim to invent
reachability algorithms, graph-based provenance, or immutable review records.
