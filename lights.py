from structures import *
from intersect import hit, intersectworld
from ray import prepare_computations
class pointlight:

    def __init__(self, position: point = point(-10, 10, -10),
        intensity: vector = vector(1,1,1)):
        self.intensity = intensity
        self.position = position


def lightning(material, light, point, eyev, normalv: vector):
    effective_color = material.color * light.intensity
    lightv = normalize(light.position - point)
    ambient = effective_color * material.ambient
    light_dot_normal = dot(lightv, normalv)
    if light_dot_normal < 0:
        diffuse = vector(0,0,0)
        specular = vector(0,0,0)
    else:
        diffuse = effective_color * material.diffuse * light_dot_normal
        reflectv = reflect(-lightv, normalv)
        reflect_dot_eye = dot(reflectv, eyev)
        if reflect_dot_eye <= 0:
            specular = vector(0,0,0)
        else:
            factor = reflect_dot_eye ** material.shiness
            specular = light.intensity * material.specular * factor
    
    return ambient + diffuse + specular


def shade_hit(w: 'world', comps: 'prepare_computations'):
    '''
    for supporting multiple light sources iterate through all off them
    and sum results
    '''
    return lightning(comps.object.material, w.light, comps.point,
    comps.eyev, comps.normalv)

def color_at(w: 'world', r: 'ray') -> 'color':
    if h := hit(intersectworld(w, r)):
        comps = prepare_computations(h, r)
        return shade_hit(w, comps)
    else:
        return vector(0,0,0)