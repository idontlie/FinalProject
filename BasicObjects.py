import math
import copy

class Vector(object):
    def __init__(self, x= 0,y =0 ,z = 0):
        self.x= x
        self.y= y
        self.z= z
    def add(x,y,z):
        self.x+=x
        self.y+=y
        self.z+=z
    def __iadd__(self,other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self
    def __add__(self,other):
        return Vector(self.x + other.x,
        self.y + other.y,
        self.y + other.y)
    def __imul__(self,other):
        self.x *= other
        self.y *= other
        self.z *= other
        return self
    def __truediv__(self, other):
        return Vector(self.x / other,
        self.y / other,
        self.y / other)
class Angle(object):
    def __init__(self, rx,ry,rz):
        self.rx= rx
        self.ry= ry
        self.rz= rz
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
        return Angle(self.rx + other.rx,
        self.ry + other.ry,
        self.rz + other.rz)
    def __imul__(self,other):
        self.rx *= other
        self.ry *= other
        self.rz *= other
        return self
    def __truediv__(self, other):
        return Angle(self.rx / other,
        self.ry / other,
        self.rz / other)

#creating an empty point defaults to 0,0,0
#for added readibilty, use Point(0) instead though
class Point(Vector):
    def __init__(self, x = 0, y = 0, z = 0):
        super().__init__(x,y,z)
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
        s= Point(0,0,1000)
        dis = math.sqrt((xroty-s.x)**2+(yroty-s.y)**2+(zroty-s.z)**2)
        s= 1000
        self.x,self.y,self.z = xroty*(dis/s), yroty*(dis/s), zroty*(dis/s)
        #self.x,self.y,self.z = xroty*(zroty+600)/600, yroty*(zroty+600)/600, zroty
        #self.x,self.y,self.z = xroty, yroty, zroty without perspective
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

class Line(object):
    def __init__(self, p1, p2, color):
        self.p1 = p1
        self.p2 = p2
        self.color = color
    def move(self, vector):
        self.p1 += vector
        self.p2 += vector
    def rotate(self, angle):
        self.p1.rotate(angle, center)
        self.p2.rotate(angle, center)

    def render(self, canvas, data, angle, center, gameCube):
        if (self.p1.isCollision(gameCube) or self.p2.isCollision(gameCube)):
            return
        p1 = copy.copy(self.p1)
        p2 = copy.copy(self.p2)
        p1.rotate(angle,Point(0))
        p2.rotate(angle,Point(0))
        canvas.create_line(
        (p1.x) + data.CX,
         (p1.y) + data.CY,
          (p2.x) + data.CX,
           (p2.y) + data.CY,
           fill = self.color
           )
    def isCollision(self, obj):
        if(self.p1.isCollision(obj)): return True
        if(self.p2.isCollision(obj)): return True
        return False
    def keepIn(self, bounds, axis):
        self.p1.keepIn(bounds, axis)
        self.p2.keepIn(bounds, axis)
#Testing
a = Angle(0,0,0)
b = Angle(1,2,3)
assert(a.rx == 0)
a+=b
assert(a.rx==b.rx)
