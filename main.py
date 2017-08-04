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
    data.gameData = GameObject()
    data.gameData.addCube(Point(0),4,"blue")

#controller
def mouseMoved(event, data):
    data.gameData.camera.rx = (event.y-(data.width//2))/100
    data.gameData.camera.ry = (event.x-(data.height//2))/100
    #pass #TODO: Create main menu screen as well as a paused screen

def keyPressed(event, data):
    if(event.char == "w"):
        data.gameData.camera.z-= 10
    if(event.char == "s"):
        data.gameData.camera.z+= 10
    #pass #TODO: Implement character motion

def timerFired(data):
    data.time += .01


#view
def redrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width, data.height, fill = "black")
    time = data.time
    data.gameData.render(canvas, data, time)





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
    def mouseMovedWrapper(event, canvas, data):
        mouseMoved(event, data)
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
    root.bind("<Motion>", lambda event:
                            mouseMovedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(700, 700)
