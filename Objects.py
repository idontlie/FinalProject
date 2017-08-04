from BasicObjects import *
#all objects in this class are subclasses of the "Lines" object
#this is because all ingame objects are really all just a collection of lines
class Lines(object):
    def __init__(self, center, color, width):
        self.center = center
        self.color = color
        self.width = width
        self.linesList = []
        #no need to include angle as a param. Should always be 0 on init
        self.angle = Angle(0,0,0)

    def addLine(self, line):
        self.linesList.append(line)
    def rotateAboutCenter():
        for l in self.linesList:
            l.rotateAboutCenter
    def oldrender(self, canvas, data):
        for l in self.linesList:
            l.oldrender(canvas, data, self.angle, self.center)
    def render(self, canvas, data, camera):
        for l in self.linesList:
            l.render(canvas, data, camera)
    def setAngle(self,angle):
        self.angle = angle


class Cube(Lines):
    def __init__(self, center, size, color,  width = 1):
        super().__init__(center, color, width)
        #Creates all lines in a cube...
        #Probably a better way to do this, but, I'm not quite sure how.
        s = size
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
class Terrain(Lines):
    def __init__(self, center, xRes, yRes, xScale, yScale, bumpyness,
    color, width = 1):
        super().__init__(center, color, width)
        for x in range(xRes):
            for y in range(yRes):
                break #WRITE THE FUCKING CAMERA SCRIPT BEFORE YOU DO THIS DUMBFUCC
