from Objects import *
class GameObject(object):
    def __init__(data):
        self.visibleItems = []
        self.camera = Camera(Point(0,3,10),Angle(0,0,0))
        self.visibleItems.append(
            Terrain(data, Point(0,0,0), 50,50, 100, 100, 0, "green")
        )
    def addCube(self, x,y,z, size, color, width = 1):
        self.visibleItems.append(Cube(x,y,z,size,color,width))
