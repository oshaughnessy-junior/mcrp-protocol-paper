"""Trusted-event integration toy, not a signer, execution runner or event detector.

A serialized caller authenticates target/epoch stamps and observes material events.
This toy composes the existing assurance calculator with append-only history and
an epoch fence. Actor strings and outcomes remain assertions, not verified facts.
"""
from dataclasses import dataclass, replace
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'assurance-assignment'))
from assurance import assign

@dataclass(frozen=True)
class View:
    target: tuple  # claim, release, scope, policy; assessment time is per receipt
    epoch: int = 0
    history: tuple = ()  # (target, epoch, assessment, calculated result)
    current: object = None
    events: tuple = ()


def target_of(assessment):
    c=assessment.context
    return (c.claim,c.release,c.scope,c.policy)


def observe(view, event_id):
    """Caller classifies this event as material to this target before delivery."""
    if not isinstance(event_id,str) or not event_id:
        raise ValueError('identified material event required')
    if event_id in view.events:
        return view  # repeated delivery cannot create a new epoch
    return replace(view,epoch=view.epoch+1,current=None,events=view.events+(event_id,))


def submit(view, assessment, policy, issued_epoch):
    """Trusted issuance stamp; lock/transaction around compare+append is assumed."""
    if type(issued_epoch) is not int or issued_epoch != view.epoch:
        raise ValueError('stale assessment epoch')
    if target_of(assessment) != view.target:
        raise ValueError('wrong exact target')
    result=assign(assessment,policy)
    return replace(view,history=view.history+((view.target,view.epoch,assessment,result),),
                   current=result.current_level)


def supersede(view, successor_target):
    if (type(successor_target) is not tuple or len(successor_target)!=4 or
        any(not isinstance(x,str) or not x for x in successor_target) or
        successor_target[1]==view.target[1]):
        raise ValueError('new release identity required')
    # Conservative all-pending branch only. carry_eligible in the sibling model
    # tests the narrower carry-forward path; this function never copies approval.
    return replace(view,target=successor_target,epoch=view.epoch+1,current=None)


def current_at(view, policy, at):
    """Query-time expiry check; unseen revocations still need observe()."""
    if type(at) is not int or at<0:
        raise ValueError('nonnegative synthetic query time required')
    if view.current is None or not view.history:
        return None
    target,epoch,a,result=view.history[-1]
    if (target!=view.target or epoch!=view.epoch or policy.id!=target[3] or
        at<a.context.at or any(o.expires_at is not None and at>=o.expires_at for o in a.outcomes)):
        return None
    return result.current_level
