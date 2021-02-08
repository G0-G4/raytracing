from lights import *
class world:

    def __init__(self, light = pointlight(), objects = []):
        self.light = light
        self.objects = objects
    