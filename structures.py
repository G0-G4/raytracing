import numpy as np

def equal(a: float, b: float, eps: float = 0.001) -> bool:
    return abs(a - b) < eps

def magnitude(x: np.array) -> float:
    return np.sqrt(x.dot(x))

def normalize(x: np.array) -> np.array:
    return x/magnitude(x)

def dot(x: np.array, y: np.array) -> np.array:
    return x.dot(y)

def cross(x: np.array, y: np.array) -> np.array:
    tmp = np.cross(x[:-1],(y[:-1]))
    return np.append(tmp,0.)


def point(x: float, y: float, z: float, w: float = 1.) -> np.array:
    return np.array([x, y, z, w], float)

def vector(x: float, y: float, z: float, w: float = 0.) -> np.array:
    return np.array([x, y, z, w], float)
