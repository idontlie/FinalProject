from BasicObjects import *
#all objects in this class are subclasses of the "Lines" object
#this is because all ingame objects are really all just a collection of lines
class Lines(object):
    def __init__(self, pos, isMovable, width):
        self.pos = pos
        self.width = width
        self.linesList = []
        #no need to include angle as a param. Should always be 0 on init
        self.angle = Angle(0,0,0)
        self.isMovable = isMovable

    def addLine(self, line):
        self.linesList.append(line)
    def rotate():
        for l in self.linesList:
            l.rotateAboutCenter
    def render(self, canvas, data, angle, gameCube):
        for l in self.linesList:
            l.render(canvas, data, angle, self.pos)
    def setAngle(self,angle):
        self.angle = angle


class Cube(Lines):
    def __init__(self, pos, size, color = "green", width = 1):
        super().__init__(pos, True, width)
        #Creates all lines in a cube...
        #Probably a better way to do this, but, I'm not quite sure how.
        s = size
        self.size = s
        self.addLine(Line(Point(s,s,s),    Point(-s,s,s), color))
        self.addLine(Line(Point(s,s,s),   Point( s,-s,s), color))
        self.addLine(Line(Point(s,s,s),   Point( s,s,-s), color))
        self.addLine(Line(Point(-s,-s,-s),Point(-s,-s,s), color))
        self.addLine(Line(Point(-s,-s,-s),Point(-s,s,-s), color))
        self.addLine(Line(Point(-s,-s,-s),Point(s,-s,-s), color))
        self.addLine(Line(Point(-s,-s, s), Point(-s,s,s), color))
        self.addLine(Line(Point(-s,-s, s), Point(s,-s,s), color))
        self.addLine(Line(Point( s,-s, -s),Point(s,s,-s), color))
        self.addLine(Line(Point( s,-s, -s),Point(s,-s,s), color))
        self.addLine(Line(Point( s,s, -s),Point(-s,s,-s), color))
        self.addLine(Line(Point(-s,s, s),Point(-s,s,-s), color))
    #Point collisions:
    def isInside(self,point):
        size = self.size + 1
        #print(point.x, point.y, point.z)
        if(point.x < -size + self.pos.x): return False
        if(point.x >  size + self.pos.x): return False

        if(point.y < -size + self.pos.y): return False
        if(point.y >  size + self.pos.y): return False

        if(point.z < -size + self.pos.z): return False
        if(point.z >  size + self.pos.z): return False
        return True
    #Use spherical hitboxes to give the user a bit more leeway when dodging
    def isCubeCollision(self,cube):
        return (cube.pos.disTo(self.pos))<self.size+cube.size
    def move(self,vector, gameCube):
        self.pos += vector
class Character(Cube):
    jumpHeight = -15
    def __init__(self, pos, size, color, width = 1):
        super().__init__(pos, size, color, width)
        self.isMovable = False
        self.vel = 0
        self.minPos = pos.x# + (size*2)
        self.gravity = 1
        self.canJump = True
    def update(self):
        self.pos.x += self.vel
        self.vel += self.gravity
        if(self.pos.x > self.minPos):
            self.canJump = True
            self.pos.x = self.minPos
    def jump(self):
        self.vel = Character.jumpHeight
class Enemy(Cube):
    def __init__(self, startLoc, size, motion, color = "red"):
        super().__init__(startLoc, size, color)
        self.motion = motion
    def render(self, canvas, data, angle, gameCube):
        #print (len(self.linesList))
        for l in self.linesList:
            if(l.isRandCollision(gameCube, self.pos)):
                l.render(canvas, data, angle, self.pos)

class GameCube(Cube):
    def __init__(self, size, color, width = 1):
        super().__init__(Point(0), size, color, width)
    def render(self, canvas, data, angle, gameCube):
        for l in self.linesList:
            l.render(canvas, data, angle, self.pos)

#creates the ground beneath the character
class Terrain(Lines):
    def __init__(self, size, zCoord, divisions, color1, color2, width = 1):
        super().__init__(Point(0,0,0), True, width)
        s = size
        z = zCoord
        self.size = size
        self.zCoord = zCoord
        self.divisions = divisions
        div = (s/divisions)
        for i in range(-divisions,divisions+1):
            for j in range(-divisions,divisions):
                self.addLine(
                    Line(Point(z, j*div, i*div),
                    Point(z, (j+1)*div, i*div), color1)
                    )
                self.addLine(
                    Line(Point(z, i*div, j*div),
                    Point(z, i*div, (j+1)*div), color2)
                    )
    def move(self, vector, gameCube):
        for i in range(len(self.linesList)):
            if(i%2==0): #only move the horizontal lines forward
                self.linesList[i].move(Vector(0,0,vector.z))
                if(not self.linesList[i].isCollision(gameCube)):
                    self.linesList[i].keepIn(gameCube.size, "z")
            else: #only move the verticle lines left and right
                self.linesList[i].move(Vector(0,vector.y,0))
                if(not self.linesList[i].isCollision(gameCube)):
                    self.linesList[i].keepIn(gameCube.size, "y")
