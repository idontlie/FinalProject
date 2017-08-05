from Objects import *
class GameObject(object):
    def __init__(self):
        size = 200
        devisions = 20
        self.visibleItems = []
        self.angle = Angle(0,0,0)
        self.rotVels = Angle(0,0,0) #velocity of rotation for each axis
        self.rotFriction = .85 #friction coefficient
        self.pos = Point(0,0)
        #Build the main game Cube
        #The entire game is rendered inside of this cube
        self.addCube(Point(0),size,"green")
        self.addTerrain(size, size, size-(size/5), devisions, "green")
    def addCube(self, center, size, color, width = 1):
        self.visibleItems.append(Cube(center, size,color,width))

    def addTerrain(self, xSize, ySize, lowerCoord,
     gridDevisions, color, width = 1):
        self.visibleItems.append(
            Terrain(xSize, ySize, lowerCoord, gridDevisions, color, width)
        )
    #CAMERA FUNCTIONS
    def movCam(self, angle):
        self.rotVels += angle

    #MODEL FUNCTIONS:
    def update(self):
        self.angle += self.rotVels/90
        self.rotVels *= self.rotFriction

    #VIEW FUNCTIONS:
    def render(self, canvas, data):
        for obj in self.visibleItems:
            obj.render(canvas,data, self.angle)
