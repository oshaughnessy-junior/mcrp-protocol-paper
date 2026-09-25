"""Conservative resource-envelope checks; no actual resource collection or billing."""
from fractions import Fraction as F
from datetime import datetime
import copy
import json

SPEC = {
    'C': {'cpu_device_hours': 'device-hour', 'gpu_device_hours': 'device-hour',
          'wall_time': 'second', 'peak_memory': 'byte'},
    'D': {'input_bytes': 'byte', 'transferred_bytes': 'byte', 'peak_storage': 'byte',
          'retained_bytes': 'byte', 'retention_duration': 'second'},
    'P': {'requirements': 'conjunctive-requirements'},
    'X': {'requirements': 'conjunctive-requirements', 'access_wait': 'second'},
    'H': {'setup': 'person-hour', 'review': 'person-hour', 'operation': 'person-hour',
          'repair': 'person-hour', 'administration': 'person-hour'},
    'A': {'requests': 'request', 'input_tokens': 'token', 'output_tokens': 'token',
          'tool_calls': 'call', 'runtime': 'second', 'billed_cost': 'USD'},
}
CONTEXT = {'workload_id', 'mode', 'interval_start', 'interval_end', 'boundary_id',
           'boundary_description', 'collector', 'currency_basis', 'requirements_vocabulary'}
FIELDS = {'status', 'unit', 'bounds', 'requirements', 'method', 'sources', 'reason', 'activity_ids'}


def rational(x):
    if not isinstance(x, str) or not x:
        raise ValueError('exact nonnegative values must be rational strings')
    try:
        r = F(x)
    except (ValueError, ZeroDivisionError):
        raise ValueError('invalid rational') from None
    if r < 0:
        raise ValueError('negative resource amount')
    return r


def nonempty_strings(x):
    return isinstance(x, list) and all(isinstance(v, str) and v for v in x) and len(set(x)) == len(x)


def validate(profile):
    if set(profile) != {'schema', 'context', 'coordinates'} or profile['schema'] != 'mcrp-resource-envelope/0.1':
        raise ValueError('unknown envelope schema or fields')
    c = profile['context']
    if set(c) != CONTEXT or any(not isinstance(v, str) or not v for v in c.values()):
        raise ValueError('complete nonempty context required')
    if c['mode'] not in {'full', 'slice', 'checkpoint', 'witness'}:
        raise ValueError('unknown assessment mode')
    start, end = [datetime.fromisoformat(c[k].replace('Z', '+00:00')) for k in ('interval_start', 'interval_end')]
    if start.tzinfo is None or end.tzinfo is None or end < start:
        raise ValueError('ordered timezone-qualified interval required')
    if set(profile['coordinates']) != set(SPEC):
        raise ValueError('all six coordinates required')
    for axis, metrics in SPEC.items():
        values = profile['coordinates'][axis]
        if set(values) != set(metrics):
            raise ValueError('missing or unexpected metric in ' + axis)
        for name, unit in metrics.items():
            item = values[name]
            if set(item) != FIELDS or item['unit'] != unit:
                raise ValueError('metric fields or unit mismatch')
            if item['status'] not in {'observed', 'estimated', 'unavailable'}:
                raise ValueError('unknown status')
            if not all(isinstance(item[k], str) for k in ('method', 'reason')):
                raise ValueError('method and reason must be strings')
            if not nonempty_strings(item['sources']) or not nonempty_strings(item['activity_ids']):
                raise ValueError('source/activity identities must be unique nonempty strings')
            if item['status'] == 'unavailable':
                if item['bounds'] is not None or item['requirements'] is not None or not item['reason']:
                    raise ValueError('unavailable requires null values and explicit reason')
                continue
            if not item['method'] or not item['sources'] or not item['activity_ids']:
                raise ValueError('known values require method, source and activity provenance')
            if unit == 'conjunctive-requirements':
                if item['status'] != 'observed' or item['bounds'] is not None or not nonempty_strings(item['requirements']):
                    raise ValueError('requirements are an observed declared set, not numeric or estimated')
            else:
                if item['requirements'] is not None or not isinstance(item['bounds'], list) or len(item['bounds']) != 2:
                    raise ValueError('numeric interval required')
                lo, hi = map(rational, item['bounds'])
                if lo > hi or (item['status'] == 'observed' and lo != hi):
                    raise ValueError('ordered bounds and observed point value required')
    return profile


def compare(left, right):
    """Return a certified bound comparison only when every dimension proves it.

    For interval estimates, left<=right requires every left upper<=right lower
    (except identical observed point values). Overlapping uncertain intervals are
    incomparable. This checks declared envelopes, not actual measurement accuracy.
    """
    validate(left); validate(right)
    for key in CONTEXT - {'collector'}:
        if left['context'][key] != right['context'][key]:
            return {'relation': 'incomparable', 'reason': 'different context: ' + key}
    le = ge = True
    for axis in SPEC:
        for name, unit in SPEC[axis].items():
            a, b = left['coordinates'][axis][name], right['coordinates'][axis][name]
            if 'unavailable' in {a['status'], b['status']}:
                return {'relation': 'incomparable', 'reason': 'unavailable: ' + axis + '.' + name}
            if unit == 'conjunctive-requirements':
                aa, bb = set(a['requirements']), set(b['requirements'])
                le &= aa <= bb; ge &= bb <= aa
            else:
                alo, ahi = map(rational, a['bounds']); blo, bhi = map(rational, b['bounds'])
                le &= ahi <= blo; ge &= bhi <= alo
    return {'relation': 'equal' if le and ge else 'less-or-equal' if le else 'greater-or-equal' if ge else 'incomparable',
            'reason': 'componentwise declared constraints; no scalar resource or assurance score'}


def sum_disjoint(profile, paths):
    """Only numeric additive consumption, same units and disjoint activities.

    Peak, wall/elapsed time, requirements and retained state cannot be added here.
    Cross-axis sums are forbidden even if units coincide. This does not prove the
    supplied activity identifiers capture all physical overlap.
    """
    validate(profile)
    allowed = {'C': {'cpu_device_hours', 'gpu_device_hours'},
               'D': {'transferred_bytes'}, 'H': set(SPEC['H']),
               'A': {'requests', 'input_tokens', 'output_tokens', 'tool_calls', 'billed_cost'}}
    if not paths or len(set(paths)) != len(paths):
        raise ValueError('nonempty unique metric paths required')
    if sum(path.startswith('C.') for path in paths) > 1:
        raise ValueError('heterogeneous CPU/GPU device-hours are not equivalent compute')
    items, seen, axis0, unit0 = [], set(), None, None
    for path in paths:
        axis, name = path.split('.')
        if axis not in allowed or name not in allowed[axis]:
            raise ValueError('metric is not additive consumption')
        item = profile['coordinates'][axis][name]
        if item['status'] == 'unavailable' or (axis0 and axis != axis0) or (unit0 and item['unit'] != unit0):
            raise ValueError('unknown or incompatible sum')
        if seen.intersection(item['activity_ids']):
            raise ValueError('overlapping activity identities cannot be added')
        seen.update(item['activity_ids']); axis0, unit0 = axis, item['unit']; items.append(item)
    return {'unit': unit0, 'bounds': [str(sum((rational(i['bounds'][n]) for i in items), F(0))) for n in (0, 1)],
            'activity_ids': sorted(seen)}


def template():
    return {'schema': 'mcrp-resource-envelope/0.1', 'context': {
        'workload_id': 'REPLACE: exact claim/release/scope/workload identity', 'mode': 'full',
        'interval_start': '2026-01-01T00:00:00Z', 'interval_end': '2026-01-01T00:00:00Z',
        'boundary_id': 'REPLACE: versioned accounting manifest identity',
        'boundary_description': 'REPLACE: included hosts/runs/roles and exclusions; include failed runs',
        'collector': 'REPLACE: accountable recorder and instrument versions',
        'currency_basis': 'REPLACE: USD price date, taxes, exchange-rate source and billing interval',
        'requirements_vocabulary': 'REPLACE: versioned conjunction-only predicate definitions'},
        'coordinates': {a: {n: {'status': 'unavailable', 'unit': u, 'bounds': None,
            'requirements': None, 'method': '', 'sources': [], 'reason': 'Template only; no measurements collected',
            'activity_ids': []} for n, u in ns.items()} for a, ns in SPEC.items()}}


def invented_complete():
    p = template()
    for a, ns in p['coordinates'].items():
        for n, i in ns.items():
            i.update(status='observed', method='Invented test point; not observed real use',
                sources=['toy-source:' + a + '.' + n], activity_ids=['toy-activity:' + a + '.' + n], reason='')
            if i['unit'] == 'conjunctive-requirements':
                i['requirements'] = []
            else:
                i['bounds'] = ['1', '1']
    return p


if __name__ == '__main__':
    print(json.dumps(template(), indent=2))
