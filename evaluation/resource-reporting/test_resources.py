import copy
import unittest
from resources import validate, template, invented_complete, compare, sum_disjoint

class Envelopes(unittest.TestCase):
    def test_unknown_is_not_zero_or_equal(self):
        p = template(); validate(p)
        self.assertEqual(compare(p, p)['relation'], 'incomparable')
        p['coordinates']['C']['wall_time']['bounds'] = ['0', '0']
        with self.assertRaises(ValueError): validate(p)

    def test_exact_complete_identity_and_cost_order(self):
        p = invented_complete(); q = copy.deepcopy(p)
        self.assertEqual(compare(p, q)['relation'], 'equal')
        q['coordinates']['A']['billed_cost']['bounds'] = ['2', '2']
        self.assertEqual(compare(p, q)['relation'], 'less-or-equal')

    def test_modes_and_boundaries_are_incomparable(self):
        p = invented_complete()
        for key, val in [('mode', 'slice'), ('boundary_id', 'different'), ('currency_basis', 'different')]:
            q = copy.deepcopy(p); q['context'][key] = val
            self.assertEqual(compare(p, q)['relation'], 'incomparable')

    def test_platform_requirements_are_conjunctions_not_costs(self):
        p = invented_complete(); q = copy.deepcopy(p)
        p['coordinates']['P']['requirements']['requirements'] = ['linux']
        q['coordinates']['P']['requirements']['requirements'] = ['linux', 'gpu']
        self.assertEqual(compare(p, q)['relation'], 'less-or-equal')
        q['coordinates']['P']['requirements']['requirements'] = ['macos']
        self.assertEqual(compare(p, q)['relation'], 'incomparable')

    def test_overlapping_estimates_do_not_prove_dominance(self):
        p = invented_complete(); q = copy.deepcopy(p)
        for obj, b in [(p, ['1', '3']), (q, ['2', '4'])]:
            obj['coordinates']['C']['wall_time'].update(status='estimated', bounds=b)
        self.assertEqual(compare(p, q)['relation'], 'incomparable')
        q['coordinates']['C']['wall_time']['bounds'] = ['3', '4']
        self.assertEqual(compare(p, q)['relation'], 'less-or-equal')

    def test_sum_only_disjoint_compatible_consumption(self):
        p = invented_complete()
        self.assertEqual(sum_disjoint(p, ['H.setup', 'H.review'])['bounds'], ['2', '2'])
        p['coordinates']['H']['review']['activity_ids'] = p['coordinates']['H']['setup']['activity_ids']
        with self.assertRaises(ValueError): sum_disjoint(p, ['H.setup', 'H.review'])
        for paths in [['C.wall_time', 'A.runtime'], ['C.cpu_device_hours', 'C.gpu_device_hours'], ['D.peak_storage'], ['H.setup', 'H.setup']]:
            with self.assertRaises(ValueError): sum_disjoint(p, paths)

    def test_invalid_units_ranges_and_provenance_refused(self):
        for changes in [dict(unit='minute'), dict(bounds=['2','1']), dict(bounds=['NaN','NaN']),
                        dict(bounds=[1,1]), dict(sources=[]), dict(activity_ids=[])]:
            p = invented_complete(); p['coordinates']['C']['wall_time'].update(changes)
            with self.assertRaises(ValueError): validate(p)

    def test_missing_axes_metrics_and_naive_interval_refused(self):
        p = template(); del p['coordinates']['X']
        with self.assertRaises(ValueError): validate(p)
        p = template(); del p['coordinates']['H']['review']
        with self.assertRaises(ValueError): validate(p)
        p = template(); p['context']['interval_start'] = '2026-01-01'
        with self.assertRaises(ValueError): validate(p)

if __name__ == '__main__': unittest.main()
