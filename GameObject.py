from Objects import *
class GameObject(object):
    def __init__(self):
        #angle vars
        self.angle = Angle(0,0,0)
        self.rotVels = Angle(0,0,0) #velocity of rotation for each axis
        self.rotFriction = .85 #friction coefficient
        #position vars
        self.pos = Point(0,0)
        self.vel = Vector(0,0)
        self.friction = .85

        self.visibleItems = []
        #Build the main game Cube
        #The entire game is rendered inside of this cube
        size = 300 #gameCube size constant
        self.gameCube = Cube(Point(0),size,"green")
        self.ground = size-(size/5) #how far the terrain is from the cube
        self.visibleItems.append(
            Character(Point(self.ground,0,-200),20,"White")
            )
        devisions = 7 #terrain devisions (/2)

        self.addTerrain(size, self.ground, devisions, "green")

    def addCube(self, center, size, color, width = 1):
        self.visibleItems.append(Cube(center, size,color,width))

    def addTerrain(self, size, lowerCoord,
     gridDevisions, color, width = 1):
        self.visibleItems.append(
            Terrain(size, lowerCoord, gridDevisions, color, width)
        )
    #CAMERA FUNCTIONS
    def movCam(self, angle):
        self.rotVels += angle

    #MODEL FUNCTIONS:
    def moveChar(self, vector):
        self.pos += vector
    def update(self):
        self.angle += self.rotVels/200
        self.rotVels *= self.rotFriction
        for i in range(len(self.visibleItems)):
            if(self.visibleItems[i].isMovable == True):
                self.visibleItems[i].move(self.vel, self.gameCube)



    #VIEW FUNCTIONS:
    def render(self, canvas, data):
        self.gameCube.render(canvas, data, self.angle, self.gameCube)
        for obj in self.visibleItems:
            obj.render(canvas,data, self.angle, self.gameCube )
