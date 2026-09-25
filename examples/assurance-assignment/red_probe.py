"""Independent internal counterexamples derived from manuscript Section 6."""
from dataclasses import replace
from itertools import product
from assurance import S1,S2,S3,Outcome,Rule,Policy,fixture,assign,aggregate


def mutate(a,name,**changes):
    return replace(a,outcomes=tuple(replace(o,**changes) if o.predicate==name else o for o in a.outcomes))


def run():
    p,a=fixture(); checks=0
    def require(condition):
        nonlocal checks
        assert condition
        checks+=1
    def rejected(fn):
        nonlocal checks
        try:fn()
        except ValueError:checks+=1
        else:raise AssertionError('expected rejection')
    inventory=((a.context.claim,a.context.scope),)
    def agg(records,inv=inventory):return aggregate(records,p,inv,a.context.release,a.context.at)
    require(assign(a,p).current_level==3)
    for name in ('external_admission','human_scientific_disposition','non_author_reconstruction','execution','comparison','independent_challenge'):
        rejected(lambda name=name:replace(p,rules=tuple(replace(r,approvers=('author',)) if r.predicate==name else r for r in p.rules)))
    for actors in (('author',),('domain-steward','author')):
        rejected(lambda actors=actors:replace(p,coverage_approvers=actors))
        for name in ('platform:alternative','sensitivity:calibration'):
            rejected(lambda actors=actors,name=name:replace(p,rules=tuple(replace(r,exemption_approvers=actors) if r.predicate==name else r for r in p.rules)))
    require(assign(type(a)(a.context,a.mode,a.coverage,a.outcomes),p).current_level is None)
    o=a.outcomes[0]
    no_status=Outcome(o.predicate,o.state,o.binding,o.evidence,o.actor,o.role,o.rationale)
    require(assign(replace(a,outcomes=(no_status,)+a.outcomes[1:]),p).current_level is None)
    require(agg((a,)).accepted)
    # Every gate independently degraded, without importing author tests.
    for name in S3:
        ceiling=0 if name in S1 else 1 if name in S2 else 2
        for state in ('fail','unknown','not-applicable'):
            result=assign(mutate(a,name,state=state),p)
            require(result.current_level is not None and result.current_level<=ceiling)
        require(assign(replace(a,outcomes=tuple(o for o in a.outcomes if o.predicate!=name)),p).current_level<=ceiling)
        for field in ('evidence','role','rationale','actor'):
            require(assign(mutate(a,name,**{field:''}),p).current_level<=ceiling)
    # Separate lower-tier failures cannot be rescued by higher-tier successes.
    samples=('external_admission','execution','independent_challenge')
    for states in product(('pass','fail','unknown'),repeat=3):
        trial=a
        for name,state in zip(samples,states):trial=mutate(trial,name,state=state)
        expected=3
        for tier,state in enumerate(states):
            if state!='pass':expected=tier;break
        require(assign(trial,p).current_level==expected)
    zero=replace(a,outcomes=())
    require(assign(zero,p).current_level==0)
    require(not agg((zero,)).accepted)
    for status in ('stale','expired','withdrawn','pending','disputed'):
        require(assign(replace(a,freshness=status),p).current_level is None)
        require(assign(mutate(a,'independent_challenge',freshness=status),p).current_level is None)
    for expiry in (0,a.context.at-1,a.context.at):
        require(assign(mutate(a,'content_identity',expires_at=expiry),p).current_level is None)
    require(assign(mutate(a,'content_identity',expires_at=a.context.at+1),p).current_level==3)
    # Authorized N/A retains3 only for explicitly exemptible subcases.
    for name,ruleid in (('platform:alternative','no-relevant-alternative'),('sensitivity:calibration','no-material-calibration-choice')):
        trial=mutate(a,name,state='not-applicable',exemption_rule=ruleid,exemption_actor='domain-steward')
        require(assign(trial,p).current_level==3)
        require(assign(mutate(trial,name,exemption_actor='outsider'),p).current_level==2)
        require(assign(mutate(trial,name,exemption_rule='invented'),p).current_level==2)
    for core in S3:
        rejected(lambda core=core:Rule(core,('reviewer',),'forgive-difficulty',('steward',)))
    for coverage in ('partial','audit-only','unassessed'):
        trial=replace(a,coverage=coverage)
        require(agg((trial,)).current_level is None)
        if coverage!='partial':require(assign(trial,p).current_level<=1)
    for mode in ('slice','checkpoint'):
        trial=replace(a,mode=mode)
        require(assign(trial,p).current_level is None)
        full=replace(trial,coverage_evidence='argument',coverage_actor='domain-steward',coverage_rationale='explicit full-scope justification')
        require(assign(full,p).current_level==3)
    require(assign(replace(a,mode='witness'),p).current_level<=1)
    require(agg(()).current_level is None)
    rejected(lambda:agg((a,a)))
    rejected(lambda:agg((a,),()))
    rejected(lambda:agg((a,),inventory+inventory))
    for field,value in (('release','different'),('policy','different'),('at',11)):
        c=replace(a.context,**{field:value})
        changed=replace(a,context=c,outcomes=tuple(replace(o,binding=c) for o in a.outcomes))
        rejected(lambda changed=changed:agg((changed,)))
    c=replace(a.context,claim='claim-2')
    second=replace(a,context=c,outcomes=tuple(replace(o,binding=c) for o in a.outcomes))
    inv=inventory+((c.claim,c.scope),)
    for name,expected in (('external_admission',0),('execution',1),('independent_challenge',2)):
        low=mutate(second,name,state='fail')
        require(agg((a,low),inv).current_level==expected)
    require(a.outcomes[0].state=='pass' and assign(a,p).current_level==3)
    return checks

if __name__=='__main__':print('Independent assertion probes passed:',run())
