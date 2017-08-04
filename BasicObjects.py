import math
import copy
from betterGraphics import *
class Angle(object):
    def __init__(self, rx,ry,rz):
        self.rx= rx
        self.ry= ry
        self.rz= rz

    def rot(rx,ry,rz):
        self.rx+=rx
        self.ry+=ry
        self.rz+=rz

#stores XYZ coords. When instantiated with no params, defaults to 0,0,0
#For more readability, call Point(0)
class Point(object):
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def rotateAboutCenter(self, angle, center):
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

    def rotateAboutCamera(self, camera):
        cx,cy,cz = camera.x, camera.y, camera.z
        x, y, z = self.x+cx, self.y+cy, self.z+cz
        a = camera.getAngle()
        rx,ry,rz = a.rx,a.ry,a.rz
        xrot = Point.compRot(x, y, rz, "x")
        yrot = Point.compRot(x, y, rz, "y")
        zrot = z

        xrotx = xrot
        yrotx = Point.compRot(yrot, zrot, rx, "y")
        zrotx = Point.compRot(yrot, zrot, rx, "z")

        yroty = yrotx
        xroty = Point.compRot(xrot, zrotx, ry, "y")
        zroty = Point.compRot(xrot, zrotx, ry, "x")
        camDis = math.sqrt(x**2 + y**2 + z**2)
        fov = 10
        self.x,self.y,self.z = xroty/(zroty/fov), (yroty/(zroty/fov)), zroty
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
    def rotateAboutCenter(self, angle):
        p1 = Point(self.x,self.y,self.z)
        p2 = Point(self.x1,self.y1,self.z1)
        p1.rotateAboutCenter(angle,center)
        p2.rotateAboutCenter(angle,center)
        self.x0, self.y0, self.z0 = p1.x, p1.y, p1.z
        self.x1, self.y1, self.z1 = p2.x, p2.y, p2.z

    def rotateAboutCamera(self, camera):
        p1 = Point(self.x,self.y,self.z)
        p2 = Point(self.x1,self.y1,self.z1)
        p1.rotateAboutCamera(camera)
        p2.rotateAboutCamera(camera)
        self.x0, self.y0, self.z0 = p1.x, p1.y, p1.z
        self.x1, self.y1, self.z1 = p2.x, p2.y, p2.z

    def render(self, canvas, data, camera):
        scale = 10
        s = scale
        p1 = Point(self.x0,self.y0,self.z0)
        p2 = Point(self.x1,self.y1,self.z1)
        p1.rotateAboutCamera(camera)
        p2.rotateAboutCamera(camera)
        betterLine(canvas, data,
        (p1.x*s) + data.CX,
         (p1.y*s) + data.CY,
          (p2.x*s) + data.CX,
           (p2.y*s) + data.CY,
           fill = self.color
           )

    def oldrender(self, canvas, data, angle, center):
        scale = 10
        s = scale
        p1 = Point(self.x0,self.y0,self.z0)
        p2 = Point(self.x1,self.y1,self.z1)
        p1.rotateAboutCenter(angle,center)
        p2.rotateAboutCenter(angle,center)
        print(type(p1),type(p1.y),type(data.CX))
        canvas.create_line(
        (p1.x*s) + data.CX,
         (p1.y*s) + data.CY,
          (p2.x*s) + data.CX,
           (p2.y*s) + data.CY,
           fill = self.color
           )



class Camera(object):
    def __init__(self, point, angle):
        self.x = point.x
        self.y = point.y
        self.z = point.z
        self.rx = angle.rx
        self.ry = angle.ry
        self.rz = angle.rz
    def move(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z
    def rotate(self, rx, ry ,rz):
        self.rx += rx
        self.ry += ry
        self.rz += rz
    def getPos(self):
        return Point(self.x, self.y, self.z)
    def getAngle(self):
        return Angle(self.rx, self.ry, self.rz)
