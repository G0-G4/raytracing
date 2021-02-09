from structures import *

'''
"point" and "Vector" are not real classes, they are functions
wich create necessary np.arrays
'''


class Ray:
    '''
    really point is not a type, it is an np.array, but it is created with "point" function
    same with Vector
    '''
    def __init__(self, origin: Point, direction: Vector) -> 'Ray':
        self.origin = origin
        self.direction = direction
    
    def position(self, t: float) -> Point:
        return self.origin + t * self.direction


    def transform(self, matr: np.array) -> 'Ray':
        return Ray(mult(matr, self.origin), mult(matr, self.direction))


class Prepare_computations:

    def __init__(self, i: 'Intersection', r: Ray):

        self.t = i.t
        self.object = i.object
        self.point = r.position(self.t)
        self.eyev = -r.direction
        self.normalv = normal_at(self.object, self.point)
        if dot(self.normalv, self.eyev) < 0:
            self.inside = True
            self.normalv *= -1
        else:
            self.inside = False

