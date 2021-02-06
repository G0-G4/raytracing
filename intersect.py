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


@njit()
def inverse(arr):
    return np.linalg.inv(arr)

def intersect(fig, r: ray) -> intersections:
    r = r.transform(inverse(fig.transform))
    return intersections([intersection(i, fig) for i in fig.__intersect__(r)])


def hit(inters: intersections):
    for i in sorted(inters, key = lambda x: x.t):
        if i.t >=0:
            return i
    # return min(inters, key = lambda x: x.t)
    return None