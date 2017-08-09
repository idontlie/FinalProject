from Objects import *
from random import randint
from betterGraphics import Colors
class GameObject(object):
    def __init__(self):
        #Game Stats:
        self.health = 3
        self.score = 0

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
        self.size = 300 #gameCube size constant
        size = self.size
        self.gameCube = GameCube(size, Colors.green)
        self.visibleItems.append(StarField(10000,400))
        self.ground = size-(size/5) #how far the terrain is from the cube
        devisions = 5 #terrain devisions
        self.addTerrain(size, self.ground, devisions, Colors.red,Colors.red)
        charSize = 20

        self.char = Character(
            Point(self.ground-charSize,0,-200),charSize,"White"
        )
    def reset(self):
        del self.visibleItems
        self.__init__()
    def addCube(self, center, size, color, width = 1):
        self.visibleItems.append(Cube(center, size,color,width))

    def addTerrain(self, size, lowerCoord,
     gridDevisions, color, width = 1):
        self.visibleItems.append(
            Terrain(size, lowerCoord, gridDevisions, color, width)
        )
    def createEnemy(self):
        s = randint(10,50)
        self.visibleItems.append(
            Enemy(
                Point(
                    self.ground-s,
                    randint(-self.size,self.size),
                    self.size+2*s
                ),
             s, "motion", color = "snow")
             #TODO: MAKE MOTION SOMETHING OTHER THAN A PLACEHOLDER
        )
    #CAMERA FUNCTIONS
    def movCam(self, angle):
        #increase speed as score increases
        angle *= (1+(self.score/10000))
        self.rotVels += angle

    #MODEL FUNCTIONS:
    def moveChar(self, vector):
        self.vel += vector
    def jumpChar(self):
        self.char.jump()

    def update(self):
        #do physics:
        self.pos += self.vel/100
        self.vel *= self.friction
        #angle physics
        self.angle += self.rotVels/300
        self.rotVels *= self.rotFriction

        #spawn enemies:
        if(randint(0,100)<(2+self.score/1000)):
            self.createEnemy()
        #do character physics:
        self.char.update()
        for i in reversed(range(len(self.visibleItems))):
            #move movable items
            if(self.visibleItems[i].isMovable == True):
                self.visibleItems[i].move(self.vel, self.gameCube)
                #Check for collisions
                self.visibleItems[i].pos.keepIn(self.gameCube.size, "y")
                if isinstance(self.visibleItems[i], Enemy):
                    if(self.visibleItems[i].isCubeCollision(self.char)):
                        del self.visibleItems[i]
                        self.health-= 1
                        self.score-= 1
                    elif(self.visibleItems[i].pos.z + 10 < -self.gameCube.size):
                        del self.visibleItems[i]
                        self.score +=  int(100*((self.rotVels.sum()/10)+.5))

    #VIEW FUNCTIONS:
    def render(self, canvas, data):
        #render game cube seperately
        self.gameCube.render(canvas, data, self.angle, self.gameCube)
        #render visible items
        for obj in self.visibleItems:
            obj.render(canvas, data, self.angle, self.gameCube)
        #render character on top of everything
        self.char.render(canvas, data, self.angle, self.gameCube)
