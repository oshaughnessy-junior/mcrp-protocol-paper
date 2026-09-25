"""Revision-only finite reference semantics, not the historical v0.1.2 verifier."""
from __future__ import annotations
from dataclasses import dataclass
from collections import deque
from types import MappingProxyType
import json

PROPAGATING = frozenset({'derives', 'requires-evidence', 'requires-authority', 'requires-freshness'})
NONPROPAGATING = frozenset({'cites', 'contextualizes', 'contradicts'})


@dataclass(frozen=True)
class Graph:
    release: str
    # Map stable logical IDs to exact version identities. They are fixture tokens,
    # not digests checked by this model.
    objects: dict
    # Edges point upstream -> dependent. Type controls propagation.
    edges: frozenset
    claims: frozenset

    def __post_init__(self):
        object.__setattr__(self,'objects',MappingProxyType(dict(self.objects)))
        object.__setattr__(self,'edges',frozenset(self.edges))
        object.__setattr__(self,'claims',frozenset(self.claims))
        if not self.release or not self.claims <= self.objects.keys():
            raise ValueError('release and resolved claim IDs required')
        if any(not isinstance(k,str) or not k or not isinstance(v,str) or not v for k,v in self.objects.items()):
            raise ValueError('nonempty string object/version IDs required')
        for source,target,kind in self.edges:
            if source not in self.objects or target not in self.objects:
                raise ValueError('unresolved endpoint')
            if kind not in PROPAGATING | NONPROPAGATING:
                raise ValueError('unknown edge semantics')
        outgoing={v:[] for v in self.objects}; indegree={v:0 for v in self.objects}
        for source,target,kind in self.edges:
            if kind=='derives':
                outgoing[source].append(target); indegree[target]+=1
        todo=deque(v for v,d in indegree.items() if not d); visited=0
        while todo:
            source=todo.popleft(); visited+=1
            for target in outgoing[source]:
                indegree[target]-=1
                if not indegree[target]:todo.append(target)
        if visited != len(self.objects):raise ValueError('cyclic derivation')

    def dependencies(self):
        return frozenset((s,t,k) for s,t,k in self.edges if k in PROPAGATING)


def reach(edges, roots):
    """Least fixed point; finite cycles do not require a topological ordering."""
    found=set(roots); todo=list(roots)
    outgoing={}
    for source,target,_ in edges:outgoing.setdefault(source,set()).add(target)
    while todo:
        for target in outgoing.get(todo.pop(),()):
            if target not in found:found.add(target); todo.append(target)
    return frozenset(found)


def revision_impact(old,new,events=()):
    """Conservative declared-record impact; caller may add material event roots."""
    if old.release==new.release:raise ValueError('successor needs new release identity')
    universe=old.objects.keys() | new.objects.keys()
    if not set(events)<=universe:raise ValueError('unknown event root')
    dirty={v for v in universe if old.objects.get(v)!=new.objects.get(v)} | set(events) | (old.claims ^ new.claims)
    # Adding/removing/retyping a dependency changes its target's support contract.
    dirty.update(target for _,target,_ in old.dependencies() ^ new.dependencies())
    affected=reach(old.dependencies() | new.dependencies(),dirty)
    return {'dirty':sorted(dirty),'affected':sorted(affected),
            'affected_claims':sorted(affected & (old.claims | new.claims)),
            'meaning':'needs-reassessment; no claim-truth verdict'}


@dataclass(frozen=True)
class PriorDecision:
    release: str
    claim: str
    contract: str
    outcome: str
    policy: str = 'policy-v1'
    issued_at: int = 0
    expires_at: int = 10
    revoked_at: int | None = None
    pending: bool = False
    disputed: bool = False

    def __post_init__(self):
        if not isinstance(self.policy,str) or not self.policy:
            raise ValueError('decision policy identity required')
        if any(type(t) is not int or t < 0 for t in (self.issued_at,self.expires_at)) or self.expires_at <= self.issued_at:
            raise ValueError('ordered nonnegative integer decision times required')
        if self.revoked_at is not None and (type(self.revoked_at) is not int or self.revoked_at < self.issued_at):
            raise ValueError('invalid revocation time')
        if type(self.pending) is not bool or type(self.disputed) is not bool:
            raise ValueError('pending/disputed must be explicit booleans')

    def current(self,as_of,policy):
        # The caller supplies an assessment clock and observed revocation/dispute
        # records. The predicate evaluates them; it cannot discover hidden events.
        if type(as_of) is not int or as_of < 0 or not isinstance(policy,str) or not policy:
            return False
        return (self.policy==policy and self.issued_at <= as_of < self.expires_at
                and (self.revoked_at is None or as_of < self.revoked_at)
                and not self.pending and not self.disputed)


@dataclass(frozen=True)
class DeltaDisposition:
    predecessor: str
    successor: str
    claim: str
    actor: str
    conclusion: str
    # Named topics checked by a separately authorized reviewer, assertions only.
    covered: frozenset

REQUIRED_DELTA_TOPICS=frozenset({'claim-scope','custody-boundary','plausible-undeclared-dependencies','missing-edges'})


def carry_eligible(old,new,claim,mapping,disposition,authorized_actors,events=(),prior_decision=None,as_of=None,policy=None):
    """Eligibility only; does not copy a decision, authenticate or execute science."""
    if claim not in old.claims or claim not in new.claims:return False,'claim-missing'
    if prior_decision is None or (prior_decision.release,prior_decision.claim,prior_decision.contract,prior_decision.outcome)!=(old.release,claim,old.objects[claim],'approved'):
        return False,'prior-approval-missing-or-unbound'
    if not prior_decision.current(as_of,policy):return False,'prior-approval-not-current'
    if mapping!='unchanged':return False,'not-unchanged'
    if old.objects[claim]!=new.objects[claim]:return False,'claim-contract-changed'
    if claim in revision_impact(old,new,events)['affected_claims']:return False,'declared-impact'
    if disposition is None:return False,'scope-delta-missing'
    if (disposition.predecessor,disposition.successor,disposition.claim)!=(old.release,new.release,claim):
        return False,'scope-delta-binding'
    if disposition.actor not in authorized_actors:return False,'scope-delta-authority'
    if disposition.conclusion!='unaffected' or not REQUIRED_DELTA_TOPICS<=disposition.covered:
        return False,'scope-delta-incomplete'
    return True,'eligible-for-explicit-carry-forward'


def fixture():
    return Graph('srr-v1',{'data':'d1','run':'r1','claim':'c1','other':'o1'},
                 frozenset({('data','run','derives'),('run','claim','requires-evidence')}),
                 frozenset({'claim','other'}))


def demo():
    old=fixture()
    changed=Graph('srr-v2',dict(old.objects,data='d2'),old.edges,old.claims)
    removed=Graph('srr-v3',dict(old.objects),frozenset(),old.claims)
    return {'data_revision':revision_impact(old,changed),
            'removed_lineage':revision_impact(old,removed),
            'historical_release_unchanged':old.release=='srr-v1' and old.objects['data']=='d1',
            'status':'Synthetic revision semantics only; not historical verifier output.'}

if __name__=='__main__':print(json.dumps(demo(),indent=2))
