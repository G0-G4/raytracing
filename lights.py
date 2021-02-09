from structures import *
from intersect import hit, intersectworld
from ray import Prepare_computations
class Pointlight:

    def __init__(self, position: Point = Point(-10, 10, -10),
        intensity: Vector = Vector(1,1,1)):
        self.intensity = intensity
        self.position = position


def lightning(material: 'Matrerial', light, point: Point, eyev: Vector, normalv: Vector):
    effective_color = material.color * light.intensity
    lightv = normalize(light.position - point)
    ambient = effective_color * material.ambient
    light_dot_normal = dot(lightv, normalv)
    if light_dot_normal < 0:
        diffuse = Vector(0,0,0)
        specular = Vector(0,0,0)
    else:
        diffuse = effective_color * material.diffuse * light_dot_normal
        reflectv = reflect(-lightv, normalv)
        reflect_dot_eye = dot(reflectv, eyev)
        if reflect_dot_eye <= 0:
            specular = Vector(0,0,0)
        else:
            factor = reflect_dot_eye ** material.shiness
            specular = light.intensity * material.specular * factor
    
    return ambient + diffuse + specular


def shade_hit(w: 'World', comps: 'Prepare_computations'):
    '''
    for supporting multiple light sources iterate through all off them
    and sum results
    '''
    return lightning(comps.object.material, w.light, comps.point,
    comps.eyev, comps.normalv)

def color_at(w: 'World', r: 'Ray') -> 'color':
    if h := hit(intersectworld(w, r)):
        comps = Prepare_computations(h, r)
        return shade_hit(w, comps)
    else:
        return Vector(0,0,0)

def color(arr: np.array):
    return min(255,int(arr[0]*255)), min(255,int(arr[1]*255)), min(255,int(arr[2]*255))