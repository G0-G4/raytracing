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
