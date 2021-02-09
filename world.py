from lights import *
class World:

    def __init__(self, light = Pointlight(), objects = []):
        self.light = light
        self.objects = objects
