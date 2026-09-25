import unittest
from dataclasses import replace
from assurance import *

class AssuranceTests(unittest.TestCase):
    def setUp(self): self.p,self.a=fixture()
    def change(self,name,**kwargs):
        return replace(self.a,outcomes=tuple(replace(o,**kwargs) if o.predicate==name else o for o in self.a.outcomes))
    def test_complete_and_accepted(self):
        self.assertEqual(assign(self.a,self.p).current_level,3)
        self.assertTrue(aggregate((self.a,),self.p,((self.a.context.claim,self.a.context.scope),),self.a.context.release,10).accepted)
    def test_each_core_gate_missing_failed_unknown_and_exempt(self):
        for name in S3:
            expected=0 if name in S1 else 1 if name in S2 else 2
            missing=replace(self.a,outcomes=tuple(o for o in self.a.outcomes if o.predicate!=name))
            self.assertEqual(assign(missing,self.p).current_level,expected,name)
            for state in ('fail','unknown','not-applicable'):
                self.assertEqual(assign(self.change(name,state=state),self.p).current_level,expected,(name,state))
    def test_absent_evidence_role_rationale_or_authority(self):
        for field in ('evidence','role','rationale','actor'):
            self.assertEqual(assign(self.change('external_admission',**{field:''}),self.p).current_level,0)
        self.assertEqual(assign(self.change('human_scientific_disposition',actor='author'),self.p).current_level,0)
    def test_no_vacuous_acceptance(self):
        empty=replace(self.a,outcomes=())
        result=aggregate((empty,),self.p,((empty.context.claim,empty.context.scope),),empty.context.release,10)
        self.assertEqual(result.current_level,0); self.assertFalse(result.accepted)
        with self.assertRaises(ValueError): aggregate((),self.p,(),self.a.context.release,10)
    def test_only_authorized_subcase_exemptions(self):
        for name,rule in [('platform:alternative','no-relevant-alternative'),('sensitivity:calibration','no-material-calibration-choice')]:
            good=self.change(name,state='not-applicable',exemption_rule=rule,exemption_actor='domain-steward')
            self.assertEqual(assign(good,self.p).current_level,3)
            for kwargs in ({'exemption_actor':'author'},{'exemption_rule':'posthoc'},{'rationale':''}):
                bad=replace(good,outcomes=tuple(replace(o,**kwargs) if o.predicate==name else o for o in good.outcomes))
                self.assertEqual(assign(bad,self.p).current_level,2)
    def test_policy_cannot_exempt_or_remove_core(self):
        with self.assertRaises(ValueError): Rule('external_admission',('external-verifier',),'waive',('domain-steward',))
        with self.assertRaises(ValueError): replace(self.p,rules=tuple(r for r in self.p.rules if r.predicate!='external_admission'))
        with self.assertRaises(ValueError): replace(self.p,rules=tuple(r for r in self.p.rules if not r.predicate.startswith('platform:')))
    def test_missing_current_assertion_defaults_pending(self):
        o=Outcome('external_admission','pass',self.a.context,'fixture','external-verifier','fixture role','reason')
        self.assertEqual(o.freshness,'pending')
        self.assertIsNone(assign(replace(self.a,outcomes=tuple(o if x.predicate==o.predicate else x for x in self.a.outcomes)),self.p).current_level)
        a=Assessment(self.a.context,'full','full',self.a.outcomes)
        self.assertIsNone(assign(a,self.p).current_level)
    def test_known_author_cannot_receive_independent_gate_authority(self):
        for name in ('external_admission','human_scientific_disposition','non_author_reconstruction','execution','comparison','independent_challenge'):
            rules=tuple(replace(r,approvers=('author',)) if r.predicate==name else r for r in self.p.rules)
            with self.assertRaises(ValueError): replace(self.p,rules=rules)
    def test_known_author_cannot_authorize_coverage_or_exemption(self):
        with self.assertRaises(ValueError): replace(self.p,coverage_approvers=('author',))
        with self.assertRaises(ValueError): replace(self.p,coverage_approvers=('domain-steward','author'))
        for name in ('platform:alternative','sensitivity:calibration'):
            rule=next(r for r in self.p.rules if r.predicate==name)
            with self.assertRaises(ValueError): replace(rule,exemption_approvers=('author',))
            with self.assertRaises(ValueError): replace(rule,exemption_approvers=('domain-steward','author'))
    def test_current_statuses_and_expiry(self):
        for state in FRESHNESS[1:]:
            self.assertIsNone(assign(replace(self.a,freshness=state),self.p).current_level)
            self.assertIsNone(assign(self.change('comparison',freshness=state),self.p).current_level)
        self.assertIsNone(assign(self.change('comparison',expires_at=10),self.p).current_level)
        self.assertEqual(assign(self.change('comparison',expires_at=11),self.p).current_level,3)
    def test_stale_high_gate_withholds_lower_current_label(self):
        self.assertIsNone(assign(self.change('independent_challenge',freshness='disputed'),self.p).current_level)
    def test_context_binding(self):
        for field,value in (('claim','other'),('release','other'),('scope','narrow'),('policy','other'),('at',11)):
            with self.assertRaises(ValueError): assign(self.change('execution',binding=replace(self.a.context,**{field:value})),self.p)
    def test_duplicates_and_unknown(self):
        with self.assertRaises(ValueError): assign(replace(self.a,outcomes=self.a.outcomes+(self.a.outcomes[0],)),self.p)
        with self.assertRaises(ValueError): assign(replace(self.a,outcomes=self.a.outcomes+(replace(self.a.outcomes[0],predicate='invented'),)),self.p)
    def test_witness_and_low_coverage_caps(self):
        for coverage in ('audit-only','unassessed'):
            self.assertEqual(assign(replace(self.a,coverage=coverage),self.p).current_level,1)
        self.assertEqual(assign(replace(self.a,mode='witness'),self.p).current_level,1)
    def test_slice_checkpoint_full_scope_argument(self):
        for mode in ('slice','checkpoint'):
            x=replace(self.a,mode=mode)
            self.assertIsNone(assign(x,self.p).current_level)
            x=replace(x,coverage_evidence='fixture:scope-proof',coverage_actor='domain-steward',coverage_rationale='asserted full scope justification')
            self.assertEqual(assign(x,self.p).current_level,3)
            self.assertIsNone(assign(replace(x,coverage_actor='author'),self.p).current_level)
    def test_partial_scope_retains_local_label_withholds_aggregate(self):
        a=replace(self.a,coverage='partial',mode='slice')
        self.assertEqual(assign(a,self.p).current_level,3)
        r=aggregate((a,),self.p,((a.context.claim,a.context.scope),),a.context.release,10)
        self.assertIsNone(r.current_level); self.assertFalse(r.accepted)
    def test_inventory_not_cherrypicked_or_duplicated(self):
        inv=((self.a.context.claim,self.a.context.scope),('missing','other scope'))
        self.assertIsNone(aggregate((self.a,),self.p,inv,self.a.context.release,10).current_level)
        with self.assertRaises(ValueError): aggregate((self.a,self.a),self.p,inv,self.a.context.release,10)
        with self.assertRaises(ValueError): aggregate((self.a,),self.p,(inv[0],inv[0]),self.a.context.release,10)
        with self.assertRaises(ValueError): aggregate((self.a,),self.p,(inv[1],),self.a.context.release,10)
    def test_release_context_and_full_scope(self):
        inv=((self.a.context.claim,'broader scope'),)
        self.assertIsNone(aggregate((self.a,),self.p,inv,self.a.context.release,10).current_level)
        for release,at in [('wrong',10),(self.a.context.release,11)]:
            with self.assertRaises(ValueError): aggregate((self.a,),self.p,((self.a.context.claim,self.a.context.scope),),release,at)
    def test_no_mutation(self):
        before=repr((self.a,self.p)); assign(self.a,self.p)
        aggregate((self.a,),self.p,((self.a.context.claim,self.a.context.scope),),self.a.context.release,10)
        self.assertEqual(repr((self.a,self.p)),before)
    def test_invalid_values(self):
        with self.assertRaises(ValueError): replace(self.a.context,at=True)
        with self.assertRaises(ValueError): self.change('execution',expires_at=-1)
        with self.assertRaises(ValueError): replace(self.a,coverage='probably-full')
        with self.assertRaises(ValueError): replace(self.p,rules=list(self.p.rules))

if __name__=='__main__': unittest.main()
