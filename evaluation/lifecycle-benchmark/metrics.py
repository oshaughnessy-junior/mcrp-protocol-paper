"""Exact offered-denominator metrics; examples are invented, not trial results.

Ground-truth registry and outcome records must come from different processes.
This module checks record consistency, not truth, independence or timestamps.
"""
from fractions import Fraction
import json

TRUTHS = {'affected', 'unaffected'}
DECISIONS = {'accept', 'invalidate', 'abstain', 'refuse', 'timeout'}
UNRESOLVED = {'abstain', 'refuse', 'timeout', 'missing'}


def ratio(numerator, denominator):
    return Fraction(numerator, denominator) if denominator else None


def rate(value):
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise ValueError('rates require integers or exact Fractions')
    value = Fraction(value)
    if not 0 <= value <= 1:
        raise ValueError('rate must be between zero and one')
    return value


def score(offered, outcomes):
    """Score one condition at its predeclared decision horizon.

    offered: [{id, truth, cluster}] fixed by evaluator before assignment.
    outcomes: [{id, decision}] one final recorded decision per offered item.
    Missing outcomes are counted as unresolved, never removed from denominators.
    Ambiguous scientific cases need adjudication before inclusion in this binary
    benchmark; exclusions and their counts must be published separately.
    """
    registry = {}
    for item in offered:
        if set(item) != {'id', 'truth', 'cluster'}:
            raise ValueError('registry fields must be id, truth, cluster')
        if not isinstance(item['id'], str) or not item['id'] or item['id'] in registry:
            raise ValueError('offered identities must be unique nonempty strings')
        if item['truth'] not in TRUTHS:
            raise ValueError('unadjudicated truth is outside this binary scorer')
        if not isinstance(item['cluster'], str) or not item['cluster']:
            raise ValueError('cluster must identify the assignment/inference unit')
        registry[item['id']] = item
    decisions = {}
    for item in outcomes:
        if set(item) != {'id', 'decision'}:
            raise ValueError('outcome fields must be id, decision')
        ident = item['id']
        if ident not in registry or ident in decisions:
            raise ValueError('outcome identity absent from registry or duplicated')
        if item['decision'] not in DECISIONS:
            raise ValueError('unknown decision')
        decisions[ident] = item['decision']
    cells = {truth: {decision: 0 for decision in sorted(DECISIONS | {'missing'})}
             for truth in sorted(TRUTHS)}
    for ident, item in registry.items():
        cells[item['truth']][decisions.get(ident, 'missing')] += 1
    affected = sum(cells['affected'].values())
    unaffected = sum(cells['unaffected'].values())
    n = affected + unaffected
    counts = {'offered': n, 'affected': affected, 'unaffected': unaffected,
              'clusters': len({item['cluster'] for item in offered}),
              'recorded': len(decisions), 'missing': n - len(decisions)}
    unresolved = {t: sum(cells[t][d] for d in UNRESOLVED) for t in TRUTHS}
    rates = {
        'stale_acceptance': ratio(cells['affected']['accept'], affected),
        'affected_invalidation_sensitivity': ratio(cells['affected']['invalidate'], affected),
        'false_invalidation': ratio(cells['unaffected']['invalidate'], unaffected),
        'control_acceptance': ratio(cells['unaffected']['accept'], unaffected),
        'affected_unresolved': ratio(unresolved['affected'], affected),
        'unaffected_unresolved': ratio(unresolved['unaffected'], unaffected),
        'all_unresolved': ratio(sum(unresolved.values()), n),
        'decision_coverage': ratio(n - sum(unresolved.values()), n),
    }
    return {'counts': counts, 'cells': cells, 'rates': rates}


def compare(offered, baseline, candidate, *, minimum_stale_reduction,
            minimum_control_acceptance, maximum_false_invalidation,
            maximum_control_loss):
    """Descriptive candidate success gate, NOT statistical inference.

    Same offered registry is required for paired synthetic comparisons. Real
    randomized arms require a prespecified clustered analysis, not this paired
    convenience routine. At least one affected and one unaffected item are needed.
    """
    delta, floor, fpr, loss = map(rate, (minimum_stale_reduction,
        minimum_control_acceptance, maximum_false_invalidation, maximum_control_loss))
    if delta <= 0 or floor <= 0:
        raise ValueError('positive improvement and control-acceptance floor required')
    b, c = score(offered, baseline), score(offered, candidate)
    if b['counts']['affected'] == 0 or b['counts']['unaffected'] == 0:
        return {'assessable': False, 'descriptive_success': False,
                'reason': 'both affected and unaffected offered strata required',
                'baseline': b, 'candidate': c}
    br, cr = b['rates'], c['rates']
    gates = {
        'stale_reduction': br['stale_acceptance'] - cr['stale_acceptance'] >= delta,
        'absolute_control_acceptance': cr['control_acceptance'] >= floor,
        'control_noninferiority': cr['control_acceptance'] >= br['control_acceptance'] - loss,
        'false_invalidation_bound': cr['false_invalidation'] <= fpr,
    }
    return {'assessable': True, 'descriptive_success': all(gates.values()),
            'gates': gates, 'baseline': b, 'candidate': c}


def invented_examples():
    offered = [{'id': prefix + str(i), 'truth': truth, 'cluster': 'toy-workflow-' + str(i)}
               for prefix, truth in [('a', 'affected'), ('u', 'unaffected')] for i in range(2)]
    policy = dict(minimum_stale_reduction=Fraction(1, 2),
                  minimum_control_acceptance=Fraction(1, 2),
                  maximum_false_invalidation=Fraction(1, 4), maximum_control_loss=0)
    baseline = [{'id': i['id'], 'decision': 'accept'} for i in offered]
    candidates = {d: [{'id': i['id'], 'decision': d} for i in offered]
                  for d in ('refuse', 'abstain', 'invalidate')}
    candidates['missing_everything'] = []
    candidates['oracle_toy'] = [{'id': i['id'], 'decision': 'invalidate' if i['truth'] == 'affected' else 'accept'} for i in offered]
    # This oracle is an illustrative upper-bound policy with evaluator truth access;
    # no actual agent is claimed to achieve it.
    return {'status': 'invented metric counterexamples; not empirical results',
            'offered': offered, 'policy': policy,
            'comparisons': {name: compare(offered, baseline, records, **policy)
                            for name, records in candidates.items()}}


def json_default(value):
    if isinstance(value, Fraction):
        return str(value)
    raise TypeError(type(value).__name__)


if __name__ == '__main__':
    print(json.dumps(invented_examples(), indent=2, default=json_default))
