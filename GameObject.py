from Objects import *
class GameObject(object):
    def __init__(self):
        self.visibleItems = []
        self.angle = Angle(0,0,0)
        self.rotVels = Angle(0,0,0) #velocity of rotation for each axis
        self.rotFriction = .98 #friction coefficient

        #Build the main game Cube
        #The entire game is rendered inside of this cube
        self.addCube(Point(0),1,"green")
    def addCube(self, center, size, color, width = 1):
        self.visibleItems.append(Cube(center, size,color,width))
    def render(self, canvas, data):
        for obj in self.visibleItems:
            obj.render(canvas,data)
