from ray import *
from sphere import sphere
from intersect import *
from lights import *
import pygame as pg
import timeit
import matplotlib.pyplot as plt
from material import color


scrWIDTH, scrHEIGHT = 300, 300

# change coords from (-1, 1) to screen coords
def coords(x, y, w = scrWIDTH, h = scrHEIGHT):
    return w*(x+1)/2, h*(-y+1)/2


pg.display.init()
pg.display.set_caption('raytracing')
screen = pg.display.set_mode((scrWIDTH,scrHEIGHT))


screen.fill((1,1,1))


wallz = 10.
wallsize = 7.
pixelsize = wallsize/scrWIDTH
half = wallsize/2

light = pointlight(vector(-10, 10, -10), vector(1, 1, 1))
s = sphere(material=material(vector(168/255, 228/255, 160/255)))
r = ray(point(0,0,-5), vector(0, 0, 1))
rorigin = point(0,0,-5)
rvec = vector(0,0,1)

start = timeit.default_timer()

for y in range(scrHEIGHT):
    worldy = half - pixelsize*y
    for x in range(scrWIDTH):
        worldx = -half + pixelsize*x
        position = point(worldx, worldy, wallz)
        r = ray(rorigin, normalize(position - rorigin))
        xs = intersect(s, r)
        if h:= hit(xs):
            p = r.position(h.t)
            normal = h.object.normal_at(p)
            eye = -r.direction
            col = lightning(h.object.material, light, p, eye, normal)
            screen.set_at((x, y), color(col))

pg.display.flip()
pg.image.save(screen, 'scndrender.bmp')
stop = timeit.default_timer()



print('Time: ', stop - start) 
input()