import copy
from fractions import Fraction as F
import unittest
from metrics import score, compare, invented_examples


class OfferedDenominators(unittest.TestCase):
    def setUp(self):
        self.offered = [{'id': 'a1', 'truth': 'affected', 'cluster': 'one'},
                        {'id': 'a2', 'truth': 'affected', 'cluster': 'one'},
                        {'id': 'u1', 'truth': 'unaffected', 'cluster': 'two'},
                        {'id': 'u2', 'truth': 'unaffected', 'cluster': 'two'}]
        self.policy = dict(minimum_stale_reduction=F(1, 2), minimum_control_acceptance=F(1, 2),
                           maximum_false_invalidation=F(1, 4), maximum_control_loss=0)
        self.baseline = [{'id': i['id'], 'decision': 'accept'} for i in self.offered]

    def test_missing_outcomes_remain_in_offered_denominator(self):
        r = score(self.offered, [{'id': 'a1', 'decision': 'accept'}])
        self.assertEqual(r['rates']['stale_acceptance'], F(1, 2))
        self.assertEqual(r['rates']['all_unresolved'], F(3, 4))
        self.assertEqual(r['counts']['missing'], 3)
        self.assertEqual(r['counts']['clusters'], 2)

    def test_confusion_and_unresolved_cells_partition_each_truth_stratum(self):
        r = score(self.offered, [{'id': 'a1', 'decision': 'invalidate'},
            {'id': 'a2', 'decision': 'timeout'}, {'id': 'u1', 'decision': 'invalidate'},
            {'id': 'u2', 'decision': 'abstain'}])
        self.assertEqual(r['rates']['affected_invalidation_sensitivity'], F(1, 2))
        self.assertEqual(r['rates']['false_invalidation'], F(1, 2))
        for keys in [('stale_acceptance', 'affected_invalidation_sensitivity', 'affected_unresolved'),
                     ('control_acceptance', 'false_invalidation', 'unaffected_unresolved')]:
            self.assertEqual(sum(r['rates'][k] for k in keys), 1)

    def test_refusing_abstaining_invalidating_or_omitting_everything_cannot_win(self):
        cs = invented_examples()['comparisons']
        for name in ('refuse', 'abstain', 'invalidate', 'missing_everything'):
            with self.subTest(name=name):
                self.assertFalse(cs[name]['descriptive_success'])
                self.assertFalse(cs[name]['gates']['absolute_control_acceptance'])
        self.assertTrue(cs['oracle_toy']['descriptive_success'])

    def test_identical_outcomes_do_not_count_as_improvement(self):
        r = compare(self.offered, self.baseline, self.baseline, **self.policy)
        self.assertFalse(r['descriptive_success'])
        self.assertFalse(r['gates']['stale_reduction'])

    def test_no_unaffected_controls_makes_comparison_unassessable(self):
        r = compare(self.offered[:2], [], [], **self.policy)
        self.assertFalse(r['assessable'])
        self.assertFalse(r['descriptive_success'])

    def test_empty_denominators_are_undefined_not_zero_error(self):
        r = score([], [])
        self.assertTrue(all(v is None for v in r['rates'].values()))
        self.assertFalse(compare([], [], [], **self.policy)['assessable'])

    def test_reject_duplicate_unknown_or_extra_records(self):
        bad = [[{'id': 'a1', 'decision': 'accept'}] * 2,
               [{'id': 'unknown', 'decision': 'accept'}],
               [{'id': 'a1', 'decision': 'pass'}],
               [{'id': 'a1', 'decision': 'accept', 'truth': 'affected'}]]
        for records in bad:
            with self.assertRaises(ValueError):
                score(self.offered, records)
        with self.assertRaises(ValueError):
            score(self.offered + [self.offered[0]], [])

    def test_no_zero_floor_no_float_or_out_of_range_threshold(self):
        for key, value in [('minimum_control_acceptance', 0), ('minimum_stale_reduction', 0),
                           ('minimum_control_acceptance', .5), ('maximum_control_loss', True),
                           ('maximum_false_invalidation', 2)]:
            p = dict(self.policy, **{key: value})
            with self.assertRaises(ValueError):
                compare(self.offered, [], [], **p)

    def test_absolute_floor_does_not_replace_relative_control_loss(self):
        candidate = [{'id': 'a1', 'decision': 'invalidate'}, {'id': 'a2', 'decision': 'invalidate'},
                     {'id': 'u1', 'decision': 'accept'}, {'id': 'u2', 'decision': 'abstain'}]
        r = compare(self.offered, self.baseline, candidate, **self.policy)
        self.assertTrue(r['gates']['absolute_control_acceptance'])
        self.assertFalse(r['gates']['control_noninferiority'])
        self.assertFalse(r['descriptive_success'])

    def test_unadjudicated_truth_cannot_be_silently_reclassified(self):
        bad = copy.deepcopy(self.offered)
        bad[0]['truth'] = 'unknown'
        with self.assertRaises(ValueError):
            score(bad, [])


if __name__ == '__main__':
    unittest.main()
