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
    def rotate():
        for l in self.linesList:
            l.rotateAboutCenter
    def render(self, canvas, data, angle):
        for l in self.linesList:
            l.render(canvas, data, angle, self.angle, self.center)
    def setAngle(self,angle):
        self.angle = angle


class Cube(Lines):
    def __init__(self, center, size, color, width = 1):
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
    def __init__(self, xSize, ySize, zCoord, devisions, color, width = 1):
        super().__init__( Point(0,0,0), color, width)
        z = zCoord; x = xSize; y = ySize
        xDiv, yDiv = (x/devisions), (y/devisions)
        for ix in range(-devisions,devisions):
            self.addLine(
                Line(
                    Point(z, y, ix*xDiv), Point(z, -y, ix*xDiv), color
                )
            )
        for iy in range(-devisions,devisions):
            self.addLine(
                Line(
                    Point(z, iy*yDiv, x), Point(z,iy*yDiv, -x), color
                )
            )
