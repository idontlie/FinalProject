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
class Point(object):
    def __init__(self, x, y, z):
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
        self.x,self.y,self.z = xroty, yroty, zroty

    def compRot(ymag, xmag, r, type):
        if (type == "y"):
            return (ymag * math.cos(r)) - (xmag * math.sin(r))
        else:
            return (ymag * math.sin(r)) + (xmag * math.cos(r))
class Line(object):
    def __init__(self, p1, p2, color):
        self.x0 = p1.x
        self.y0 = p1.y
        self.z0 = p1.z
        self.x1 = p2.x
        self.y1 = p2.y
        self.z1 = p2.z
        self.color = color
    def rotate(self, angle):
        p1 = Point(self.x,self.y,self.z)
        p2 = Point(self.x1,self.y1,self.z1)
        p1.rotate(angle,center)
        p2.rotate(angle,center)
        self.x0 = p1.x
        self.y0 = p1.y
        self.z0 = p1.z
        self.x1 = p2.x
        self.y1 = p2.y
        self.z1 = p2.z
    def render(self, canvas, data, angle, center):
        scale = 10
        s = scale
        p1 = Point(self.x0,self.y0,self.z0)
        p2 = Point(self.x1,self.y1,self.z1)
        p1.rotate(angle,center)
        p2.rotate(angle,center)
        print(type(p1),type(p1.y),type(data.CX))
        canvas.create_line(
        (p1.x*s) + data.CX,
         (p1.y*s) + data.CY,
          (p2.x*s) + data.CX,
           (p2.y*s) + data.CY,
           fill = self.color
           )
