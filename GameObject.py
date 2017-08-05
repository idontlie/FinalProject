from Objects import *
class GameObject(object):
    def __init__(self):
        self.visibleItems = []
        self.angle = Angle(0,0,0)
        self.rotVels = Angle(0,0,0) #velocity of rotation for each axis
        self.rotFriction = .8 #friction coefficient

        #Build the main game Cube
        #The entire game is rendered inside of this cube
        self.addCube(Point(0),100,"green")
    def addCube(self, center, size, color, width = 1):
        self.visibleItems.append(Cube(center, size,color,width))
    def movCam(self, angle):
        self.rotVels += angle
    def update(self):
        self.angle += self.rotVels/100
        self.rotVels *= self.rotFriction
    def render(self, canvas, data):
        for obj in self.visibleItems:
            obj.render(canvas,data, self.angle)
