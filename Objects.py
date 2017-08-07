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
            l.render(canvas, data, angle, self.pos, gameCube)
    def setAngle(self,angle):
        self.angle = angle

class Character(Lines):
    jumpHeight = -20
    def __init__(self, pos, size, color, width = 1):
        super().__init__(pos, False, width)
        #Creates all lines in a rectangular prism...
        #Probably a better way to do this, but, I'm not quite sure how.
        s = size
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
        self.addLine(Line(Point( -s,s, s),Point(-s,s,-s), color))
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
        self.addLine(Line(Point( -s,s, s),Point(-s,s,-s), color))
    def isInside(self,point):
        size = self.size + 1
        if(point.x < -size + self.pos.x): return True
        if(point.x >  size + self.pos.x): return True
        if(point.y < -size + self.pos.y): return True
        if(point.y >  size + self.pos.y): return True
        if(point.z < -size + self.pos.z): return True
        if(point.z >  size + self.pos.z): return True
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
            l.render(canvas, data, angle, self.pos, GameCube(self.size+1,""))

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
        for i in range(-divisions-1,divisions+1):
            self.addLine(Line(
                Point(z, i*div, -size),
                Point(z, (i+1)*div, -size), color2)
                )
            self.addLine(Line(
                Point(z, i*div, size),
                Point(z, (i+1)*div, size), color2)
                )
        for i in range(-divisions-1,divisions+1):
            for j in range(-divisions-1,divisions+1):
                self.addLine(
                    Line(Point(z, j*div, i*div),
                    Point(z, (j+1)*div, i*div), color1)
                    )
                self.addLine(
                    Line(Point(z, i*div, j*div),
                    Point(z, i*div, (j+4)*div), color2)
                    )
    def move(self, vector, gameCube):
        for i in range((self.divisions*2)+16,len(self.linesList)):
            if(i%2==0):
                self.linesList[i].move(vector) #add axis to this as well
                if(self.linesList[i].isCollision(gameCube)):
                    self.linesList[i].keepIn(gameCube.size, "z")
