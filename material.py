from structures import *
class material:

    def __init__(self, color: vector = vector(1, 1, 1), ambient: float = 0.1,
        diffuse: float = 0.9, specular: float = 0.9, shiness: float = 200.):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shiness = shiness
    
    def __str__(self):
        return f"{self.color = }\n{self.ambient = }\n{self.diffuse = }\n{self.specular = }"
    

def color(arr: np.array):
    return min(255,int(arr[0]*255)), min(255,int(arr[1]*255)), min(255,int(arr[2]*255))