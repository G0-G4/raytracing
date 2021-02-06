from structures import *
from sphere import * #delete later
from ray import *   #delete later

class intersection:
    def __init__(self, t: float, fig):
        self.t = t
        self.object = fig



class intersections(list):
    pass



def intersect(fig, r: ray) -> intersections:
    r = r.transform(np.linalg.inv(fig.transform))
    return intersections([intersection(i, fig) for i in fig.__intersect__(r)])


def hit(inters: intersections):
    for i in sorted(inters, key = lambda x: x.t):
        if i.t >=0:
            return i
    # return min(inters, key = lambda x: x.t)
    return None