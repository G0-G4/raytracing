from structures import *

'''
"point" and "vector" are not real classes, they are functions
wich create necessary np.arrays
'''


class ray:
    '''
    really point is not a type, it is an np.array, but it is created with "point" function
    same with vector
    '''
    def __init__(self, origin: point, direction: vector) -> 'ray':
        self.origin = origin
        self.direction = direction
    
    def position(self, t: float) -> point:
        return self.origin + t*self.direction


    def transform(self, matr: np.array) -> 'ray':
        return ray(mult(matr, self.origin), mult(matr, self.direction))


class prepare_computations:

    def __init__(self, i: 'intersection', r: ray):

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

