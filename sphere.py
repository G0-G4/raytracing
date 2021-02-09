from structures import *
from ray import *  # delete later just for hints from ide
from numba import njit
from material import *
'''
later create base class figure
'''

class Sphere:

    def __init__(self, origin: Point = Point(0,0,0), radius: float = 1.,
        transform = np.identity(4), material: Material = Material() ) ->'Sphere':
        self.origin = origin
        self.radius = radius
        self.transform = transform
        self.material = material

    def __intersect__(self, ray: Ray) -> tuple:
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

    def __normal_at__(self, world_point: Point) -> Vector:
        obj_point = mult(inverse(self.transform), world_point)
        obj_normal = obj_point - self.origin
        world_normal = mult(transpose(inverse(self.transform)), obj_normal)
        return normalize(world_normal)