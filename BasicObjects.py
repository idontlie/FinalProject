import math
import copy
from random import randint
from betterGraphics import *
class Vector(object):
    def __init__(self, x= 0,y =0 ,z = 0):
        self.x = x
        self.y = y
        self.z = z
    def add(x,y,z):
        self.x+=x
        self.z+=z
    def __iadd__(self,other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self
    def __add__(self,other):
        if(isinstance(self,Point)):
            return Point(self.x + other.x,
            self.y + other.y,
            self.z + other.z)
        else:
            return Vector(self.x + other.x,
            self.y + other.y,
            self.z + other.z)
    def __imul__(self,other):
        self.x *= other
        self.y *= other
        self.z *= other
        return self
    def __mul__(self,other):
        if(isinstance(self,Point)):
            return Point(self.x * other.x,
            self.y * other.y,
            self.z * other.z)
        if(isinstance(other, int)):
            return Vector(self.x * other,
            self.y * other,
            self.z * other)
        else:
            return Vector(self.x * other.x,
            self.y * other.y,
            self.z * other.z)
        return self
    def __truediv__(self, other):
        return Vector(self.x / other,
        self.y / other,
        self.z / other)
class Angle(object):
    def __init__(self, rx,ry,rz):
        self.rx= rx
        self.ry= ry
        self.rz= rz
    def sum(self):
        return self.rx + self.ry + self.rz
    def rot(rx,ry,rz):
        self.rx+=rx
        self.ry+=ry
        self.rz+=rz
    def __iadd__(self,other):
        self.rx += other.rx
        self.ry += other.ry
        self.rz += other.rz
        return self
    def __add__(self,other):
        return Angle(
        self.rx + other.rx,
        self.ry + other.ry,
        self.rz + other.rz)
    def __imul__(self,other):
        self.rx *= other
        self.ry *= other
        self.rz *= other
        return self
    def __truediv__(self, other):
        return Angle(
        self.rx / other,
        self.ry / other,
        self.rz / other)

#creating an empty point defaults to 0,0,0
#for added readibilty, use Point(0) instead though
class Point(Vector):
    def __init__(self, x = 0, y = 0, z = 0):
        super().__init__(x,y,z)
    def disTo(self, point):
        return math.sqrt((self.x-point.x)**2+(self.y-point.y)**2+(self.z-point.z)**2)
    def rotate(self, angle, center):
        rx, ry, rz = angle.rx, angle.ry, angle.rz
        cx,cy,cz = center.x, center.y, center.z
        x, y, z = self.x+cx, self.y+cy, self.z+cz
        xrot = Point.compRot(x, y, rz, "x")
        yrot = Point.compRot(x, y, rz, "y")
        zrot = z

        xrotx = xrot
        yrotx = Point.compRot(yrot, zrot, rx, "y")
        zrotx = Point.compRot(yrot, zrot, rx, "z")

        yroty = yrotx
        xroty = Point.compRot(xrot, zrotx, ry, "y")
        zroty = Point.compRot(xrot, zrotx, ry, "x")
        s= Point(0,0,600)
        #dis = math.sqrt((xroty-s.x)**2+(yroty-s.y)**2+(zroty-s.z)**2)
        s= 600
        #self.x,self.y,self.z = xroty/(dis/s), yroty/(dis/s), zroty*(dis/s)
        self.x,self.y,self.z = xroty/(1+(zroty+400)/500), yroty/(1+(zroty+400)/500), zroty
        #self.x,self.y,self.z = xroty, yroty, zroty #without perspective
    def compRot(ymag, xmag, r, type):
        if (type == "y"):
            return (ymag * math.cos(r)) - (xmag * math.sin(r))
        else:
            return (ymag * math.sin(r)) + (xmag * math.cos(r))
    def isCollision(self, obj):
        return obj.isInside(self)
    #axis is a string that contains x, y, z , or any combination of those
    def keepIn(self, bounds, axis):
        if "x" in axis:
            self.x = ((self.x+bounds)%(2*bounds))-bounds
        if "y" in axis:
            self.y = ((self.y+bounds)%(2*bounds))-bounds
        if "z" in axis:
            self.z = ((self.z+bounds)%(2*bounds))-bounds
    def render(self, canvas, data, angle, radius, fill = "white"):
        p = copy.copy(self)
        p.rotate(angle, Point(0))

        betterSquare(canvas, p.x + data.CX, p.y + data.CY, radius, fill)
class Line(object):
    def __init__(self, p1, p2, color):
        self.p1 = p1
        self.p2 = p2
        self.color = color
    #Only use the move function to move individual lines
    #To move a whole shape, modify the self.pos of any instance of the "Lines" object
    def move(self, vector):
        self.p1 += vector
        self.p2 += vector
    #TODO: add static rotate function
    def render(self, canvas, data, angle, pos, width = 1):
        p1 = copy.copy(self.p1)
        p2 = copy.copy(self.p2)
        p1 += pos
        p2 += pos
        p1.rotate(angle,Point(0))
        p2.rotate(angle,Point(0))
        betterLine(canvas,
            (p1.x) + data.CX, (p1.y) + data.CY,
            (p2.x) + data.CX, (p2.y) + data.CY,
            fill = self.color,
            width = width
           )
    #Randomly chooses between anyCollision or isCollision
    #also adds a bit of jitter to the line position
    #Looks *dope AF*
    def isRandCollision(self, obj, pos = Point(0)):
        jitter = Vector(randint(-10,10),randint(-10,10),randint(-10,10))
        if(randint(0,1)==1):
            return self.isAnyCollision(obj, pos + jitter)
        else:
            return self.isCollision(obj, pos + jitter)
    #If any part of the line is colliding return true
    def isAnyCollision(self, obj, pos = Point(0)):
        if((self.p1+pos).isCollision(obj)): return True
        if((self.p2+pos).isCollision(obj)): return True
        return False

    #Only returns true if both parts of the line are colliding
    def isCollision(self, obj, pos = Point(0)):
        if(not (self.p1+pos).isCollision(obj)): return False
        if(not (self.p2+pos).isCollision(obj)): return False
        return True

    def keepIn(self, bounds, axis):
        self.p1.keepIn(bounds, axis)
        self.p2.keepIn(bounds, axis)
