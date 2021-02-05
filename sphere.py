from structures import *
from ray import *  # delete later just for hints from ide

'''
later create base class figure
'''

class sphere:

    def __init__(self, origin: point = point(0,0,0), radius: float = 1.):
        self.origin = origin
        self.radius = radius

    def __intersect__(self, ray: ray):
        sphere_to_ray = ray.origin - self.origin
        a = dot(ray.direction, ray.direction)
        b = 2 * dot(ray.direction, sphere_to_ray)
        c = dot(sphere_to_ray, sphere_to_ray) - 1
        discriminant = b*b - 4*a*c
        if discriminant < 0:
            return ()
        t1 = (-b + np.sqrt(discriminant)) / (2 * a)
        t2 = (-b - np.sqrt(discriminant)) / (2 * a)
        return t1, t2