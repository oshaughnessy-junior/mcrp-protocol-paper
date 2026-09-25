"""Asserted-input implementation of proposed Section 6; NOT authentication/science."""
from dataclasses import dataclass
from typing import Optional

S1 = ('external_admission','content_identity','claim_mapping','provenance',
      'trust_leaves','acceptance_tests','negative_controls','archive_identity',
      'human_scientific_disposition')
S2 = S1 + ('non_author_reconstruction','execution','comparison')
S3 = S2 + ('independent_challenge','overall_sensitivity','freshness_exercised')
STATES = ('pass','fail','unknown','not-applicable')
FRESHNESS = ('current','stale','expired','withdrawn','pending','disputed')
MODES = ('full','slice','checkpoint','witness')
COVERAGE = ('full','partial','audit-only','unassessed')

def text(value):
    return isinstance(value,str) and bool(value.strip())

def tick(value):
    return type(value) is int and value >= 0

@dataclass(frozen=True)
class Context:
    claim: str
    release: str
    scope: str
    policy: str
    at: int
    def __post_init__(self):
        if not all(text(v) for v in (self.claim,self.release,self.scope,self.policy)) or not tick(self.at):
            raise ValueError('Context requires identifiers and a nonnegative synthetic time')

@dataclass(frozen=True)
class Rule:
    predicate: str
    approvers: tuple
    exemption_rule: str = ''
    exemption_approvers: tuple = ()
    def __post_init__(self):
        if not text(self.predicate) or type(self.approvers) is not tuple or not self.approvers or not all(text(v) for v in self.approvers):
            raise ValueError('Predicate requires immutable authorized-actor inventory')
        if type(self.exemption_approvers) is not tuple or not all(text(v) for v in self.exemption_approvers):
            raise ValueError('Invalid exemption authorizers')
        if 'author' in self.exemption_approvers:
            raise ValueError('Author cannot authorize its own exemption disposition')
        is_subcase=self.predicate.startswith(('platform:','sensitivity:'))
        if self.exemption_rule or self.exemption_approvers:
            if not is_subcase or not text(self.exemption_rule) or not self.exemption_approvers:
                raise ValueError('Only declared subcases can have exemption rules')

@dataclass(frozen=True)
class Policy:
    id: str
    rules: tuple
    coverage_approvers: tuple
    def __post_init__(self):
        if not text(self.id) or type(self.rules) is not tuple or not all(isinstance(r,Rule) for r in self.rules):
            raise ValueError('Immutable policy and Rule objects required')
        names=tuple(r.predicate for r in self.rules)
        if len(set(names)) != len(names) or not set(S3).issubset(names):
            raise ValueError('Every core gate exactly once is required')
        if any(n not in S3 and not n.startswith(('platform:','sensitivity:')) for n in names):
            raise ValueError('Unknown predicate family')
        if any(n.endswith(':') for n in names) or not any(n.startswith('platform:') for n in names):
            raise ValueError('At least one identified platform subcase is required')
        if type(self.coverage_approvers) is not tuple or not self.coverage_approvers or not all(text(v) for v in self.coverage_approvers):
            raise ValueError('Coverage authorizers required')
        if 'author' in self.coverage_approvers:
            raise ValueError('Author cannot authorize its own full-scope coverage disposition')
        for name in ('external_admission','human_scientific_disposition',
                     'non_author_reconstruction','execution','comparison','independent_challenge'):
            if 'author' in next(r.approvers for r in self.rules if r.predicate==name):
                raise ValueError('Author cannot fill a required independent-action fixture role')

@dataclass(frozen=True)
class Outcome:
    predicate: str
    state: str
    binding: Context
    evidence: str = ''
    actor: str = ''
    role: str = ''
    rationale: str = ''
    freshness: str = 'pending'
    expires_at: Optional[int] = None
    exemption_rule: str = ''
    exemption_actor: str = ''
    def __post_init__(self):
        if self.state not in STATES or self.freshness not in FRESHNESS or not isinstance(self.binding,Context):
            raise ValueError('Invalid outcome state or binding')
        if self.expires_at is not None and not tick(self.expires_at):
            raise ValueError('Invalid expiry')

@dataclass(frozen=True)
class Assessment:
    context: Context
    mode: str
    coverage: str
    outcomes: tuple
    freshness: str = 'pending'
    coverage_evidence: str = ''
    coverage_actor: str = ''
    coverage_rationale: str = ''
    def __post_init__(self):
        if not isinstance(self.context,Context) or self.mode not in MODES or self.coverage not in COVERAGE or self.freshness not in FRESHNESS:
            raise ValueError('Invalid assessment')
        if type(self.outcomes) is not tuple or not all(isinstance(o,Outcome) for o in self.outcomes):
            raise ValueError('Immutable outcome tuple required')

@dataclass(frozen=True)
class Result:
    context: Context
    current_level: Optional[int]
    predicate_level: int
    mode: str
    coverage: str
    reasons: tuple


def assign(assessment, policy):
    """No IO; absent evidence blocks gates. None means current label withheld."""
    if assessment.context.policy != policy.id:
        raise ValueError('Wrong policy context')
    rules={r.predicate:r for r in policy.rules}
    outcomes={}
    for o in assessment.outcomes:
        if o.predicate in outcomes or o.predicate not in rules:
            raise ValueError('Duplicate or unknown outcome')
        if o.binding != assessment.context:
            raise ValueError('Evidence assertion bound to wrong assessment context')
        outcomes[o.predicate]=o
    reasons=[]; current=assessment.freshness=='current'; satisfied=set()
    if not current: reasons.append('assessment:'+assessment.freshness)
    for name,rule in rules.items():
        o=outcomes.get(name)
        if o is None:
            reasons.append(name+':missing'); continue
        if o.freshness!='current' or (o.expires_at is not None and o.expires_at<=assessment.context.at):
            current=False; reasons.append(name+':not-current'); continue
        if not all(text(v) for v in (o.evidence,o.role,o.rationale)) or o.actor not in rule.approvers:
            reasons.append(name+':missing-evidence-or-authority'); continue
        if o.state=='pass':
            satisfied.add(name)
        elif (o.state=='not-applicable' and rule.exemption_rule and
              o.exemption_rule==rule.exemption_rule and
              o.exemption_actor in rule.exemption_approvers):
            satisfied.add(name)
        else: reasons.append(name+':'+o.state)
    level=0
    for index, gates in ((1,S1),(2,S2),(3,tuple(rules))):
        if set(gates).issubset(satisfied): level=index
    if assessment.coverage in ('audit-only','unassessed') or assessment.mode=='witness':
        level=min(level,1)
        reasons.append('coverage-or-witness:capped-at-1')
    if assessment.coverage=='full' and assessment.mode in ('slice','checkpoint'):
        if not (text(assessment.coverage_evidence) and text(assessment.coverage_rationale)
                and assessment.coverage_actor in policy.coverage_approvers):
            current=False; reasons.append('full-scope:missing-validated-coverage-argument')
    return Result(assessment.context,level if current else None,level,
                  assessment.mode,assessment.coverage,tuple(reasons))

@dataclass(frozen=True)
class ReleaseResult:
    current_level: Optional[int]
    accepted: bool
    reasons: tuple


def aggregate(assessments, policy, inventory, release, at):
    """Inventory is a separately fixed tuple of (claim, full scope) pairs."""
    if type(inventory) is not tuple or not inventory or not tick(at) or not text(release):
        raise ValueError('Nonempty prospective inventory/release/time required')
    if any(type(row) is not tuple or len(row)!=2 or not all(text(v) for v in row) for row in inventory):
        raise ValueError('Invalid inventory row')
    claims=dict(inventory)
    if len(claims)!=len(inventory): raise ValueError('Duplicate material claim')
    if type(assessments) is not tuple: raise ValueError('Immutable assessments required')
    seen=set(); results=[]; reasons=[]
    for a in assessments:
        c=a.context
        if c.claim in seen: raise ValueError('Multiple assessments for one material claim')
        seen.add(c.claim)
        if c.claim not in claims: raise ValueError('Assessment outside inventory')
        if (c.release,c.policy,c.at)!=(release,policy.id,at):
            raise ValueError('Mixed release/policy/time context')
        result=assign(a,policy); results.append(result)
        if c.scope!=claims[c.claim] or a.coverage!='full': reasons.append(c.claim+':partial-scope')
        if result.current_level is None: reasons.append(c.claim+':withheld')
    if seen!=set(claims): reasons.append('missing-material-claim')
    if reasons: return ReleaseResult(None,False,tuple(reasons))
    level=min(r.current_level for r in results)
    return ReleaseResult(level,level>=1,())


def fixture():
    rules=tuple(Rule(n,('human-reviewer',) if n=='human_scientific_disposition' else ('external-verifier',)) for n in S3)
    rules+=(Rule('platform:alternative',('external-verifier',),'no-relevant-alternative',('domain-steward',)),
            Rule('sensitivity:calibration',('external-verifier',),'no-material-calibration-choice',('domain-steward',)))
    policy=Policy('synthetic-policy-v1',rules,('domain-steward',))
    context=Context('claim-1','sha256:synthetic-release','full toy claim',policy.id,10)
    outcomes=tuple(Outcome(r.predicate,'pass',context,'fixture:'+r.predicate,r.approvers[0],
                           'fixture role','synthetic evaluator assertion',freshness='current') for r in rules)
    return policy,Assessment(context,'full','full',outcomes,freshness='current')
