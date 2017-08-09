from BasicObjects import *
from Objects import Cube
from random import randint
class TitleScreen(object):
    def __init__(self):
        self.particles = []
        self.angle = Angle(0,0,0)
        self.startRad = 100
        self.startCount = 20
        self.cube = Cube(Point(0), 300, "green")

    def update(self):
        if(randint(0,10)<3 and self.startCount > 0 ):
            self.startCount -= 1
            self.newParticle()

        self.angle.rx+= 1/100
        self.angle.ry+=.4/100
        self.angle.rz+=.7/100
        for i in range(len(self.particles)):
            self.particles[i].update(self.cube)

    def newParticle(self):
        rx = randint(-10,10)/3
        ry = randint(-10,10)/3
        rz = randint(-10,10)/3
        self.particles.insert( 0,
            Particle(Point(0),Vector(rx,ry,rz), self.startRad)
        )
    def render(self, canvas, data):
        self.cube.render(canvas, data, self.angle)
        #check the distance between each particle and draw lines when apropriate
        for i in self.particles:
            i.pos.render(canvas, data, self.angle, 4)
            for j in self.particles:

                dis = i.pos.disTo(j.pos)
                #draw white line if distance is small
                if dis <i.rad+j.rad:
                    Line(i.pos,j.pos,"white").render(
                        canvas, data, self.angle,
                        Point(0)
                    )
                #red if larger
                elif dis<(i.rad+j.rad)*1.5:
                    Line(i.pos,j.pos,"red").render(
                        canvas, data, self.angle,
                        Point(0)
                    )
                #blue if large
                elif dis<(i.rad+j.rad)*2:
                    Line(i.pos,j.pos,"blue").render(
                        canvas, data, self.angle,
                        Point(0), .5
                    )

class Particle(object):
    def __init__(self, point, vector, radius):
        self.pos = point
        self.vel = vector
        self.rad = radius
        self.age = 0
    def update(self, cube):
        self.pos.keepIn(cube.size,"xyz")
        self.pos+=self.vel
        self.age += 1
