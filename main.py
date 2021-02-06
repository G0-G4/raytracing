from ray import *
from sphere import sphere
from intersect import *
import pygame as pg



    

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

s = sphere()
r = ray(point(0,0,-5), vector(0, 0, 1))
rorigin = point(0,0,-5)
rvec = vector(0,0,1)

for y in range(scrHEIGHT):
    worldy = half - pixelsize*y
    for x in range(scrWIDTH):
        worldx = -half + pixelsize*x
        position = point(worldx, worldy, wallz)
        r = ray(rorigin, normalize(position - rorigin))
        xs = intersect(s, r)
        if hit(xs):
            screen.set_at((x, y), (255, 0, 0))

pg.display.flip()
pg.image.save(screen, 'fstrender.bmp')
input()
