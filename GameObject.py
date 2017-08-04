from Objects import *
class GameObject(object):
    def __init__(self):
        self.visibleItems = []
        self.camera = Camera(Point(0,0,-10),Angle(0,0,0))
        #self.visibleItems.append(
        #    Terrain(Point(0,0,0), 50,50, 100, 100, 0, "green")
        #)

    def addCube(self, center, size, color, width = 1):
        self.visibleItems.append(Cube(center, size, color, width))

    def render(self, canvas, data, time):
        for obj in self.visibleItems:
            obj.render(canvas, data, self.camera)
