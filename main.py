from ray import *
from sphere import Sphere
from intersect import *
from lights import *
from world import *
import pygame as pg
import timeit
from camera import Camera


w = World()


floor = Sphere(transform=scaling(10,0.01,10))
floor.material = Material(Vector(1, 0.9, 0.9), specular=0)

left_wall = Sphere(transform=mult(translation(0,0,5),
    mult(rotationY(-np.pi/4), mult(rotationX(np.pi/2), scaling(10,0.01,10)))))

left_wall.material = floor.material


right_wall = Sphere(transform=mult(translation(0,0,5),
    mult(rotationY(np.pi/4), mult(rotationX(np.pi/2), scaling(10,0.01,10)))))

right_wall.material = floor.material


middle = Sphere(transform = mult(translation(1.5,0.5, -0.5),
    scaling(0.5,.5,.5)))
middle.material = Material(Vector(0.5,0.9, 0.75), diffuse=0.5)

w.objects.extend([floor, left_wall, right_wall, middle])

c = Camera(1280, 720, np.pi / 3)
c.transform = view_transform(Point(0,1.5,-5), Point(0,1,0),Vector(0,1,0))


start = timeit.default_timer()
c.render(w)
stop = timeit.default_timer()
print('Time: ', stop - start) 
print("READY!!!!!!!!!")