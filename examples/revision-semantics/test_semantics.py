import unittest
from itertools import product
from semantics import Graph, PriorDecision, DeltaDisposition, REQUIRED_DELTA_TOPICS, reach, revision_impact, carry_eligible as checked_carry, fixture

def carry_eligible(old,new,claim,*args):
    return checked_carry(old,new,claim,*args,prior_decision=PriorDecision(old.release,claim,old.objects[claim],'approved'),as_of=5,policy='policy-v1')

class Semantics(unittest.TestCase):
    def delta(self,successor='srr-v2',actor='reviewer'):
        return DeltaDisposition('srr-v1',successor,'other',actor,'unaffected',REQUIRED_DELTA_TOPICS)

    def test_graph_snapshot_is_immutable(self):
        objects={'a':'1'}; g=Graph('v',objects,frozenset(),frozenset({'a'}))
        objects['a']='2'
        self.assertEqual(g.objects['a'],'1')
        with self.assertRaises(TypeError):g.objects['a']='3'

    def test_derivation_cycle_rejected(self):
        with self.assertRaises(ValueError):Graph('v',{'a':'1','b':'1'},frozenset({('a','b','derives'),('b','a','derives')}),frozenset())

    def test_other_cycles_permitted(self):
        for kind in ('requires-evidence','cites','contradicts'):
            Graph('v',{'a':'1','b':'1'},frozenset({('a','b',kind),('b','a',kind)}),frozenset())

    def test_reach_independent_path_enumeration(self):
        vertices=('a','b','c'); pairs=tuple(product(vertices,repeat=2))
        for bits in product((0,1),repeat=len(pairs)):
            edges=frozenset((s,t,'requires-evidence') for (s,t),b in zip(pairs,bits) if b)
            expected={'a'}
            # Every reachable node has a simple path of at most n-1 edges.
            for length in (1,2):
                for tail in product(vertices,repeat=length):
                    path=('a',)+tail
                    if all((s,t,'requires-evidence') in edges for s,t in zip(path,path[1:])):expected.add(path[-1])
            self.assertEqual(reach(edges,{'a'}),frozenset(expected))

    def test_upstream_change_impacts_only_reached_claim(self):
        old=fixture(); new=Graph('srr-v2',dict(old.objects,data='d2'),old.edges,old.claims)
        self.assertEqual(revision_impact(old,new)['affected_claims'],['claim'])
        self.assertEqual(old.objects['data'],'d1')
        self.assertIn('no claim-truth',revision_impact(old,new)['meaning'])

    def test_deleted_edge_cannot_hide_impact(self):
        old=fixture(); new=Graph('srr-v2',dict(old.objects),frozenset(),old.claims)
        self.assertEqual(revision_impact(old,new)['affected_claims'],['claim'])

    def test_deleted_upstream_node_uses_old_graph(self):
        old=fixture(); objects=dict(old.objects); del objects['data']
        new=Graph('srr-v2',objects,frozenset(e for e in old.edges if e[0]!='data'),old.claims)
        self.assertIn('claim',revision_impact(old,new)['affected_claims'])

    def test_context_does_not_automatically_propagate(self):
        old=fixture(); edges=old.edges | {('data','other','contextualizes')}
        new=Graph('srr-v2',dict(old.objects,data='d2'),frozenset(edges),old.claims)
        self.assertNotIn('other',revision_impact(old,new)['affected_claims'])
        self.assertFalse(carry_eligible(old,new,'other','unchanged',None,{'reviewer'})[0])
        self.assertTrue(carry_eligible(old,new,'other','unchanged',self.delta(),{'reviewer'})[0])

    def test_scope_binding_and_authority(self):
        old=fixture(); new=Graph('srr-v2',dict(old.objects),old.edges,old.claims)
        for delta in (self.delta('wrong'),self.delta(actor='author'),DeltaDisposition('srr-v1','srr-v2','other','reviewer','unaffected',frozenset())):
            self.assertFalse(carry_eligible(old,new,'other','unchanged',delta,{'reviewer'})[0])
        self.assertFalse(carry_eligible(old,new,'other','narrowed',self.delta(),{'reviewer'})[0])

    def test_event_root_for_same_bytes(self):
        old=fixture(); new=Graph('srr-v2',dict(old.objects),old.edges,old.claims)
        self.assertEqual(revision_impact(old,new,['data'])['affected_claims'],['claim'])
        self.assertFalse(carry_eligible(old,new,'other','unchanged',self.delta(),{'reviewer'},['other'])[0])

    def test_changed_claim_contract_even_if_mapping_lies(self):
        old=fixture(); new=Graph('srr-v2',dict(old.objects,other='new-scope'),old.edges,old.claims)
        self.assertFalse(carry_eligible(old,new,'other','unchanged',self.delta(),{'reviewer'})[0])

    def test_missing_graph_edge_can_miss_real_impact(self):
        old=fixture(); new=Graph('srr-v2',dict(old.objects,data='d2'),old.edges,old.claims)
        # External evaluator knows an undeclared edge data->other. Model does not.
        self.assertNotIn('other',revision_impact(old,new)['affected_claims'])
        self.assertFalse(carry_eligible(old,new,'other','unchanged',None,{'reviewer'})[0])
        # Even a falsely asserted authorized disposition passes the toy predicate:
        # its content is a trust premise, not a scientific oracle.
        self.assertTrue(carry_eligible(old,new,'other','unchanged',self.delta(),{'reviewer'})[0])

    def test_prior_approval_required_and_bound(self):
        old=fixture(); new=Graph('srr-v2',dict(old.objects),old.edges,old.claims)
        for prior in (None,PriorDecision('wrong','other','o1','approved'),PriorDecision('srr-v1','other','o1','pending')):
            self.assertFalse(checked_carry(old,new,'other','unchanged',self.delta(),{'reviewer'},prior_decision=prior)[0])

    def test_material_claim_set_changes_are_dirty(self):
        old=fixture(); new=Graph('srr-v2',dict(old.objects),old.edges,frozenset({'claim'}))
        self.assertIn('other',revision_impact(old,new)['dirty'])
        self.assertIn('other',revision_impact(old,new)['affected_claims'])

    def test_currentness_clock_policy_revocation_and_pending(self):
        old=fixture(); new=Graph('srr-v2',dict(old.objects),old.edges,old.claims)
        def check(prior,as_of=5,policy='policy-v1'):
            return checked_carry(old,new,'other','unchanged',self.delta(),{'reviewer'},prior_decision=prior,as_of=as_of,policy=policy)[0]
        prior=PriorDecision('srr-v1','other','o1','approved')
        self.assertTrue(check(prior))
        for clock in (None,-1,True,10,11):self.assertFalse(check(prior,clock))
        self.assertFalse(check(prior,policy='policy-v2'))
        self.assertFalse(check(PriorDecision('srr-v1','other','o1','approved',issued_at=6)))
        for args in ({'revoked_at':3},{'pending':True},{'disputed':True}):
            self.assertFalse(check(PriorDecision('srr-v1','other','o1','approved',**args)))
        # Revocation is date-scoped, not a retrospective rewrite of historical use.
        self.assertTrue(check(PriorDecision('srr-v1','other','o1','approved',revoked_at=7)))
        self.assertFalse(check(PriorDecision('srr-v1','other','o1','approved',revoked_at=7),as_of=7))

    def test_bad_graph_and_revision_identity(self):
        with self.assertRaises(ValueError):Graph('v',{'a':'1'},frozenset({('a','b','derives')}),frozenset())
        with self.assertRaises(ValueError):Graph('v',{'a':'1'},frozenset({('a','a','unknown')}),frozenset())
        with self.assertRaises(ValueError):revision_impact(fixture(),fixture())

if __name__=='__main__':unittest.main()
