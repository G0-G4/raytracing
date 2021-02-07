from structures import *

class pointlight:

    def __init__(self, position: point, intensity: point):
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