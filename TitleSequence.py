from BasicObjects import *
from Objects import *
from random import randint
class TitleScreen(object):
    def __init__(self):
        self.time = 0
        self.stars = StarField(10000, 300)
        self.particles = []
        self.angle = Angle(0,0,0)
        self.startRad = 100
        self.startCount = 30
        self.cube = Cube(Point(0), 400, Colors.green)

    def update(self):
        if(randint(0,10)<3 and self.startCount > 0 ):
            self.startCount -= 1
            self.newParticle(self.cube.size)

        self.angle.rx+= 1/100
        self.angle.ry+=.4/100
        self.angle.rz+=.7/100
        for i in range(len(self.particles)):
            self.particles[i].update(self.cube)
        self.time +=1
    def newParticle(self, bounds):
        rx = randint(-10,10)/3
        ry = randint(-10,10)/3
        rz = randint(-10,10)/3
        x = randint(-bounds,bounds)
        y = randint(-bounds,bounds)
        z = randint(-bounds,bounds)
        self.particles.insert( 0,
            Particle(Point(x,y,z),Vector(rx,ry,rz), self.startRad)
        )
    def render(self, canvas, data):
        h = data.height
        w = data.width
        if not self.time > 100:
            time = self.time**1.7
            animation = False
        else:
            time = self.time + 2000
            animation = True
        self.stars.render(canvas, data, self.angle)
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
        betterRect(canvas,
        min(-10, time - 750), 150, 750, 140, "black", "gray75")
        betterTextTitle(canvas,
        min(100, time - 650), 150, "INSIDE_THE_BOX", "white", 100)

        if(time % 10 < 5 or not animation):
            betterRect(canvas,
            max(w - 750, w-time) , h - 410, 750, 116, "black", "gray75")
            betterText(canvas,
            max(w - 700, w-time+50), h - 400, "START_GAME","white", 60)
        else:
            betterRect(canvas,
            max(w - 750, w-time) , h - 410, 750, 116, "#303030", "gray75")
            betterText(canvas,
            max(w - 700, w-time+50), h - 400, "START_GAME", "#00ff00", 59)

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
