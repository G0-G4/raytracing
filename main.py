from ray import *
from sphere import sphere
import pygame as pg



    

scrWIDTH, scrHEIGHT = 720,720

# change coords from (-1, 1) to screen coords
def coords(x, y, w = scrWIDTH, h = scrHEIGHT):
    return w*(x+1)/2, h*(-y+1)/2


# pg.display.init()
# pg.display.set_caption('raytracing')
# screen = pg.display.set_mode((scrWIDTH,scrHEIGHT))

# pos = point(0,scrHEIGHT//2,0)
# vel = vector(0.1,-0.1,0)



# screen.fill((1,1,1))
# p = point(0, 0.5, 0)
# for i in range(12):
#     pg.draw.circle(screen, (255,255,255), coords(p[0], p[1]), 10)
#     p = mult(rotationZ(2*np.pi/12),p)
# pg.display.flip()


r = ray(point(0,0,5), vector(0,0,1))
s = sphere()
print(s.origin)
xs = intersect(s, r)
print(xs)


# input()