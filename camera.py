from structures import *
from ray import Ray
import pygame as pg
from lights import color_at, color
class Camera:

    def __init__(self, hsize: int, vsize: int, fov: float, transform: np.array = np.identity(4)):
        self.hsize = hsize
        self.vsize = vsize
        self.fov = fov
        self.transform = transform

        self.half_view = np.tan(self.fov / 2)
        aspect = self.hsize/ self.vsize
        if aspect >= 1:
            self.half_width = self.half_view
            self.half_height = self.half_view / aspect
        else:
            self.half_height = self.half_view
            self.half_width = self.half_view * aspect
        
        self.pixelsize = (self.half_width * 2) / self.hsize

    def ray_to_pixel(self,px, py) -> Ray:
        xoffset = (px + 0.5) * self.pixelsize
        yoffset = (py + 0.5) * self.pixelsize
        world_x = self.half_width - xoffset
        world_y = self.half_height - yoffset
        invtr = inverse(self.transform)
        pixel = mult(invtr, Point(world_x, world_y, -1))
        origin = mult(invtr, Point(0,0,0)) # дальше видимо будут изменения
        direction = normalize(pixel - origin)
        return Ray(origin, direction)

    def render(self, world: 'World'):
        pg.display.init()
        pg.display.set_caption('raytracing')
        screen = pg.display.set_mode((self.hsize,self.vsize))
        screen.fill((1,1,1))
        for y in range(self.vsize):
            for x in range(self.hsize):
                ray = self.ray_to_pixel(x, y)
                col = color_at(world, ray)
                screen.set_at((x,y), color(col))
        pg.display.flip()

        pg.image.save(screen, 'render.bmp')
        
