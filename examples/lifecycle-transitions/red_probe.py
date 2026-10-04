"""Independent finite trace enumeration; trusted identities/events, not security."""
from itertools import product
from dataclasses import replace
from transitions import View, target_of, submit, observe, supersede, current_at
from assurance import fixture


def run():
    p, a = fixture()
    count = 0
    for sequence in product(('accept', 'event', 'successor'), repeat=5):
        v = View(target_of(a))
        for i, op in enumerate(sequence):
            old = v
            if op == 'event':
                v = observe(v, 'event:'+str(i))
                assert current_at(v,p,10) is None
                assert observe(v,'event:'+str(i)) == v
            elif op == 'successor':
                v = supersede(v,(v.target[0],'release:'+str(i),v.target[2],v.target[3]))
                assert current_at(v,p,10) is None
            else:
                c = replace(a.context,release=v.target[1])
                fresh = replace(a,context=c,outcomes=tuple(replace(o,binding=c,expires_at=11) for o in a.outcomes))
                v = submit(v,fresh,p,v.epoch)
                assert current_at(v,p,10) == 3
                assert current_at(v,p,11) is None
            assert v.history[:len(old.history)] == old.history
            if v.epoch > old.epoch:
                try:
                    submit(v,a,p,old.epoch)
                except ValueError:
                    pass
                else:
                    raise AssertionError('stale epoch accepted')
            count += 1
    return {'sequences': 243, 'transitions': count}


if __name__ == '__main__':
    print(run())
