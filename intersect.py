from structures import *
from sphere import * #delete later
from ray import *   #delete later
from numba import njit

class Intersection:
    def __init__(self, t: float, fig):
        self.t = t
        self.object = fig



class Intersections(list):
    pass

def intersect(fig, r: Ray) -> Intersections:
    r = r.transform(inverse(fig.transform))
    return Intersections([Intersection(i, fig) for i in fig.__intersect__(r)])


def intersectworld(w, r: Ray) -> Intersections:
    xs = Intersections()
    for obj in w.objects:
        xs.extend(intersect(obj, r))
    return Intersections(sorted(xs, key = lambda x: x.t))


def hit(inters: Intersections) -> Intersection:
    # сортировку можно будет убрать, тк подаются уже отсортированные
    # for i in sorted(inters, key = lambda x: x.t):
    for i in inters:
        if i.t >=0:
            return i
    # return min(inters, key = lambda x: x.t)
    return None