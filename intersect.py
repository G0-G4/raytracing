from structures import *
from sphere import * #delete later
from ray import *   #delete later
from numba import njit

class intersection:
    def __init__(self, t: float, fig):
        self.t = t
        self.object = fig



class intersections(list):
    pass

def intersect(fig, r: ray) -> intersections:
    r = r.transform(inverse(fig.transform))
    return intersections([intersection(i, fig) for i in fig.__intersect__(r)])


def intersectworld(w, r: ray) -> intersections:
    xs = intersections()
    for obj in w.objects:
        xs.extend(intersect(obj, r))
    return intersections(sorted(xs, key = lambda x: x.t))


def hit(inters: intersections) ->intersection:
    # сортировку можно будет убрать, тк подаются уже отсортированные
    for i in sorted(inters, key = lambda x: x.t):
        if i.t >=0:
            return i
    # return min(inters, key = lambda x: x.t)
    return None