import math
import copy
from Objects import *
from GameObject import *
from tkinter import * 

#model
def init(data):
    data.CX = data.width//2
    data.CY = data.height//2
    data.time = 0
    data.c = Cube(data,Point(0,0,0),"blue",4)
    data.c0 = Cube(data,Point(4,4,0),"white",4)
    data.c1 = Cube(data,Point(4,0,4),"white",4)

#controller
def mousePressed(event, data):
    pass #TODO: Create main menu screen as well as a paused screen

def keyPressed(event, data):
    pass #TODO: Implement character motion

def timerFired(data):
    data.time += .01


#view
def redrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width, data.height, fill = "black")
    time = data.time
    data.c.setAngle(Angle(time, time/2, time))
    data.c0.setAngle(Angle(time, time/2, time))
    data.c1.setAngle(Angle(time, time/2, time))
    data.c.render(canvas,data)
    data.c0.render(canvas,data)
    data.c1.render(canvas,data)





###################################
####################################
# use the run function as-is
####################################
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 10 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(700, 700)
