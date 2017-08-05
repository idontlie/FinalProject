import math
import copy

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
class Point(object):
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
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

    def compRot(ymag, xmag, r, type):
        if (type == "y"):
            return (ymag * math.cos(r)) - (xmag * math.sin(r))
        else:
            return (ymag * math.sin(r)) + (xmag * math.cos(r))
class Line(object):
    def __init__(self, p1, p2, color):
        self.x0, self.y0, self.z0 = p1.x, p1.y, p1.z
        self.x1, self.y1, self.z1 = p2.x, p2.y, p2.z
        self.color = color
    def rotate(self, angle):
        p1 = Point(self.x,self.y,self.z)
        p2 = Point(self.x1,self.y1,self.z1)
        p1.rotate(angle,center)
        p2.rotate(angle,center)
        self.x0, self.y0, self.z0 = p1.x, p1.y, p1.z
        self.x1, self.y1, self.z1 = p2.x, p2.y, p2.z
    def render(self, canvas, data,cAngle, angle, center):
        p1 = Point(self.x0,self.y0,self.z0)
        p2 = Point(self.x1,self.y1,self.z1)
        #p1.rotate(angle,center)
        #p2.rotate(angle,center)
        p1.rotate(cAngle,Point(0))
        p2.rotate(cAngle,Point(0))
        canvas.create_line(
        (p1.x) + data.CX,
         (p1.y) + data.CY,
          (p2.x) + data.CX,
           (p2.y) + data.CY,
           fill = self.color
           )

#Testing
a = Angle(0,0,0)
b = Angle(1,2,3)
assert(a.rx == 0)
a+=b
assert(a.rx==b.rx)
