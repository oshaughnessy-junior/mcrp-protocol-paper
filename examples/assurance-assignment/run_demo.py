"""Print deterministic synthetic cases; does not execute a scientific workflow."""
from dataclasses import replace, asdict
import json
from assurance import fixture, assign, aggregate

p,a=fixture()
examples={
 'all_asserted_pass':a,
 'no_scientific_disposition':replace(a,outcomes=tuple(o for o in a.outcomes if o.predicate!='human_scientific_disposition')),
 'author_self_admission':replace(a,outcomes=tuple(replace(o,actor='author') if o.predicate=='external_admission' else o for o in a.outcomes)),
 'expired_comparison':replace(a,outcomes=tuple(replace(o,expires_at=10) if o.predicate=='comparison' else o for o in a.outcomes)),
 'narrow_slice':replace(a,mode='slice',coverage='partial'),
 'unjustified_full_slice':replace(a,mode='slice'),
 'authorized_platform_nonapplicability':replace(a,outcomes=tuple(replace(o,state='not-applicable',exemption_rule='no-relevant-alternative',exemption_actor='domain-steward') if o.predicate=='platform:alternative' else o for o in a.outcomes)),
 'unlawful_core_exemption':replace(a,outcomes=tuple(replace(o,state='not-applicable',exemption_rule='waive-controls',exemption_actor='domain-steward') if o.predicate=='negative_controls' else o for o in a.outcomes)),
}
print(json.dumps({'synthetic_asserted_inputs_only':True,'cases':{
 name:{'claim_result':asdict(assign(x,p)), 'release_result':asdict(aggregate((x,),p,((a.context.claim,a.context.scope),),a.context.release,10))}
 for name,x in examples.items()}},indent=2))
