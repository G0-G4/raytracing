import numpy as np
from numba import njit

'''
functions for creating points and Vector ( both are np.arrays with different 4th component)
and functions for processing them

(I could have used "np.array" as a parent class, but there are some difficulties with it, so i decided to use 
"np.array" as it is, but mimmicking creation of Point and Vector by using simple factory functions)
'''

@njit()
def equal(a: float, b: float, eps: float = 0.001) -> bool:
    return abs(a - b) < eps

@njit()
def magnitude(x: np.array) -> float:
    return np.sqrt(x.dot(x))
    
@njit()
def normalize(x: np.array) -> np.array:
    return x/magnitude(x)

@njit()
def dot(x: np.array, y: np.array) -> np.array:
    return x.dot(y)

@njit()
def cross(x: np.array, y: np.array) -> np.array:
    tmp = np.cross(x[:-1],(y[:-1]))
    return np.append(tmp,0.)


def Point(x: float, y: float, z: float, w: float = 1.) -> np.array:
    # return np.array([[x, y, z, w]], float).T  # Point is a Vector column
    return np.array([x, y, z, w], float)

def Vector(x: float, y: float, z: float, w: float = 0.) -> np.array:
    # return np.array([[x, y, z, w]], float).T  # Vector is a Vector column
    return np.array([x, y, z, w], float)


def translation(x: float, y: float, z: float) -> np.array:
    tmp = np.identity(4, float)
    tmp[0][3] = x
    tmp[1][3] = y
    tmp[2][3] = z
    return tmp

@njit()
def mult(m1: np.array, m2: np.array) -> np.array:
    return m1 @ m2

def scaling(x: float, y: float, z: float) -> np.array:
    return np.diag([x, y, z, 1.])


def rotationX(r: float) -> np.array:
    tmp = np.diag([1., np.cos(r), np.cos(r), 1.])
    s = np.sin(r)
    tmp[2][1] = s
    tmp[1][2] = -s
    return tmp

def rotationY(r: float) -> np.array:
    tmp = np.diag([np.cos(r), 1., np.cos(r), 1.])
    s = np.sin(r)
    tmp[0][2] = s
    tmp[2][0] = -s
    return tmp

def rotationZ(r: float) -> np.array:
    tmp = np.diag([np.cos(r), np.cos(r), 1., 1.])
    s = np.sin(r)
    tmp[0][1] = -s
    tmp[1][0] = s
    return tmp

def shearing(xy: float, xz: float, yx: float, yz: float, zx: float, zy: float) -> np.array:
    tmp = np.identity(4)
    tmp[0][1] = xy
    tmp[0][2] = xz
    tmp[1][0] = yx
    tmp[1][2] = yz
    tmp[2][0] = zx
    tmp[2][1] = zy
    return tmp

@njit()
def inverse(arr):
    return np.linalg.inv(arr)

@njit
def transpose(arr):
    return np.transpose(arr)

@njit
def reflect(inn: Vector, n: Vector) -> Vector:
    return inn - 2 * n * dot(inn, n)


def normal_at(obj, point: Point):
    return obj.__normal_at__(point)

def view_transform(fr: np.array, to: np.array, up: np.array):
    forward = normalize(to - fr)
    left = cross(forward, normalize(up))
    true_up = cross(left, forward)
    orientation = np.array([
        [left[0],     left[1],    left[2],      0.],
        [true_up[0],  true_up[1], true_up[2],   0.],
        [-forward[0], -forward[1], -forward[2], 0.],
        [0.,          0.,          0.,          1.]
    ])
    return mult(orientation, translation(-fr[0], -fr[1], -fr[2]))


