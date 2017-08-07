from BasicObjects import *
#all objects in this class are subclasses of the "Lines" object
#this is because all ingame objects are really all just a collection of lines
class Lines(object):
    def __init__(self, center, color, isMovable, width):
        self.center = center
        self.color = color
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
            l.render(canvas, data, angle, self.center, gameCube)
    def setAngle(self,angle):
        self.angle = angle

class Character(Lines):
    def __init__(self, pos, size, color, width = 1):
        super().__init__(pos, color, False, width)
        #Creates all lines in a rectangular prism...
        #Probably a better way to do this, but, I'm not quite sure how.
        s = size
        x, y, z = pos.x-s, pos.y, pos.z
        self.addLine(Line(Point(s+x,s+y,s+z),    Point(-s+x,s+y,s+z), color))
        self.addLine(Line(Point(s+x,s+y,s+z),   Point( s+x,-s+y,s+z), color))
        self.addLine(Line(Point(s+x,s+y,s+z),   Point( s+x,s+y,-s+z), color))
        self.addLine(Line(Point(-s+x,-s+y,-s+z),Point(-s+x,-s+y,s+z), color))
        self.addLine(Line(Point(-s+x,-s+y,-s+z),Point(-s+x,s+y,-s+z), color))
        self.addLine(Line(Point(-s+x,-s+y,-s+z),Point(s+x,-s+y,-s+z), color))
        self.addLine(Line(Point(-s+x,-s+y, s+z), Point(-s+x,s+y,s+z), color))
        self.addLine(Line(Point(-s+x,-s+y, s+z), Point(s+x,-s+y,s+z), color))
        self.addLine(Line(Point( s+x,-s+y, -s+z),Point(s+x,s+y,-s+z), color))
        self.addLine(Line(Point( s+x,-s+y, -s+z),Point(s+x,-s+y,s+z), color))
        self.addLine(Line(Point( s+x,s+y, -s+z),Point(-s+x,s+y,-s+z), color))
        self.addLine(Line(Point( -s+x,s+y, s+z),Point(-s+x,s+y,-s+z), color))
class Cube(Lines):
    def __init__(self, center, size, color = "green", width = 1):
        super().__init__(center, color, True, width)
        #Creates all lines in a cube...
        #Probably a better way to do this, but, I'm not quite sure how.
        s = size
        self.size = s
        x, y, z = center.x, center.y, center.z
        self.addLine(Line(Point(s+x,s+y,s+z),    Point(-s+x,s+y,s+z), color))
        self.addLine(Line(Point(s+x,s+y,s+z),   Point( s+x,-s+y,s+z), color))
        self.addLine(Line(Point(s+x,s+y,s+z),   Point( s+x,s+y,-s+z), color))
        self.addLine(Line(Point(-s+x,-s+y,-s+z),Point(-s+x,-s+y,s+z), color))
        self.addLine(Line(Point(-s+x,-s+y,-s+z),Point(-s+x,s+y,-s+z), color))
        self.addLine(Line(Point(-s+x,-s+y,-s+z),Point(s+x,-s+y,-s+z), color))
        self.addLine(Line(Point(-s+x,-s+y, s+z), Point(-s+x,s+y,s+z), color))
        self.addLine(Line(Point(-s+x,-s+y, s+z), Point(s+x,-s+y,s+z), color))
        self.addLine(Line(Point( s+x,-s+y, -s+z),Point(s+x,s+y,-s+z), color))
        self.addLine(Line(Point( s+x,-s+y, -s+z),Point(s+x,-s+y,s+z), color))
        self.addLine(Line(Point( s+x,s+y, -s+z),Point(-s+x,s+y,-s+z), color))
        self.addLine(Line(Point( -s+x,s+y, s+z),Point(-s+x,s+y,-s+z), color))
    def isInside(self,point):
        size = self.size + 1
        if(point.x < -size + self.center.x): return True
        if(point.x >  size + self.center.x): return True
        if(point.y < -size + self.center.y): return True
        if(point.y >  size + self.center.y): return True
        if(point.z < -size + self.center.z): return True
        if(point.z >  size + self.center.z): return True
        return False
    def move(self,vector, gameCube):
        for i in range(len(self.linesList)):
            self.linesList[i].move(vector)
class Enemy(Cube):
    def __init__(self, startLoc, size, motion, color = "red"):
        super().__init__(startLoc, size, color)
        self.motion = motion

    def update(self):
        for i in range(len(self.linesList)):
            motion.move(self.linesList[i])

class GameCube(Cube):
    def __init__(self, size, color, width = 1):
        super().__init__(Point(0), size, color, width)
    def render(self, canvas, data, angle, gameCube):
        for l in self.linesList:
            l.render(canvas, data, angle, self.center, GameCube(self.size+1,""))

#creates the ground beneath the character
class Terrain(Lines):
    def __init__(self, size, zCoord, devisions, color, width = 1):
        super().__init__(Point(0,0,0), color, True, width)
        s = size
        z = zCoord
        self.size = size
        self.zCoord = zCoord
        div = (s/devisions)
        for i in range(-devisions-1,devisions+1):
            self.addLine(Line(Point(z, j*div, i*div),
                Point(z, (j+1)*div, i*div), color)
                )
        for i in range(-devisions-1,devisions+1):
            for j in range(-devisions-1,devisions+1):
                self.addLine(
                    Line(Point(z, j*div, i*div),
                    Point(z, (j+1)*div, i*div), color)
                    )
                self.addLine(
                    Line(Point(z, i*div, j*div),
                    Point(z, i*div, (j+1)*div), color)
                    )
    def move(self,vector, gameCube):
        for i in range(2,len(self.linesList)):
            if(i%2==0):
                self.linesList[i].move(vector) #add axis to this as well
                if(self.linesList[i].isCollision(gameCube)):
                    self.linesList[i].keepIn(gameCube.size, "z")
            else:
