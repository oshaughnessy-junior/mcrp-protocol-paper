import unittest
from dataclasses import replace
from transitions import View, target_of, submit, observe, supersede, current_at
from assurance import fixture

class TransitionTraces(unittest.TestCase):
    def setUp(self):
        self.p,self.a=fixture();self.v=View(target_of(self.a))
    def test_event_after_acceptance_preserves_history_withholds_current(self):
        accepted=submit(self.v,self.a,self.p,0)
        self.assertEqual(accepted.current,3)
        stale=observe(accepted,'calibration-withdrawn')
        self.assertIsNone(stale.current)
        self.assertEqual(stale.history,accepted.history)
        self.assertEqual(accepted.current,3)  # old immutable view unmodified
        self.assertEqual(observe(stale,'calibration-withdrawn'),stale)
    def test_late_completion_cannot_resurrect_pre_event_epoch(self):
        stale=observe(self.v,'material-update')
        with self.assertRaises(ValueError):submit(stale,self.a,self.p,0)
        # Authoritative new assertions in the current epoch, not old approval copy.
        context=replace(self.a.context,at=11)
        reassessed=replace(self.a,context=context,outcomes=tuple(replace(o,binding=context) for o in self.a.outcomes))
        self.assertEqual(submit(stale,reassessed,self.p,1).current,3)
    def test_agent_recommendation_cannot_fill_human_actor_gate(self):
        agent=replace(self.a,outcomes=tuple(replace(o,actor='agent-recommender') if o.predicate=='human_scientific_disposition' else o for o in self.a.outcomes))
        self.assertEqual(submit(self.v,agent,self.p,0).current,0)
        self.assertEqual(submit(self.v,self.a,self.p,0).current,3)
    def test_successor_no_silent_replay_even_with_matching_scope(self):
        old=submit(self.v,self.a,self.p,0)
        successor=supersede(old,(self.v.target[0],'different-release',self.v.target[2],self.v.target[3]))
        self.assertIsNone(successor.current);self.assertEqual(successor.history,old.history)
        with self.assertRaises(ValueError):submit(successor,self.a,self.p,successor.epoch)
        with self.assertRaises(ValueError):supersede(old,old.target)
    def test_missing_event_is_deliberate_limit_not_detected_change(self):
        # Undelivered real-world change cannot affect a trusted-input calculator.
        accepted=submit(self.v,self.a,self.p,0)
        self.assertEqual(accepted.current,3)
        self.assertIsNone(observe(accepted,'now-observed').current)

    def test_currentness_expires_at_query_time_without_a_new_event(self):
        expiring=replace(self.a,outcomes=tuple(replace(o,expires_at=11) for o in self.a.outcomes))
        v=submit(self.v,expiring,self.p,0)
        self.assertEqual(current_at(v,self.p,10),3)
        self.assertIsNone(current_at(v,self.p,11))
        self.assertIsNone(current_at(v,self.p,9))
        self.assertIsNone(current_at(v,replace(self.p,id='different-policy'),10))

if __name__=='__main__':unittest.main()
