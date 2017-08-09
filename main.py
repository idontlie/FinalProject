import math
import copy
import string
import time
from Objects import *
from GameObject import *
from TitleSequence import*
from tkinter import *
import UI
#tkinter MVC framework stolen from 15112 course website

#model
def init(data):
    data.isTitleScreen = True
    data.isPaused = False
    data.isGameOver = False
    data.titleScreen = TitleScreen()
    data.CX = data.width//2
    data.CY = data.height//2
    data.time = 0
    data.game = GameObject()
    data.chars = {"a":False,"d":False}
    for i in string.printable:
        data.chars[i] = False
#controller
def mousePressed(event, data):
    pass #TODO: Create mai n menu screen as well as a paused screen

def keyPressed(event, data):
    #All keyboard data stored in data.chars dictionary
    data.chars[event.char.lower()] = True
    if(event.char == " "):
        data.game.jumpChar()
    if(event.char == "z"):
        data.game.createEnemy()

def keyRelease(event, data):
    data.chars[event.char.lower()] = False

def keyActions(data):

    if(data.chars['w']):
        #data.game.movCam(Angle(1,0,0))
        pass
    if(data.chars['a']):
        #data.game.movCam(Angle(0,1,0))
        data.game.moveChar(Vector(0,2,0))
    if(data.chars['s']):
        data.game.movCam(Angle(0,1,0))
    if(data.chars['d']):
        data.game.moveChar(Vector(0,-2,0))

def timerFired(data):
    keyActions(data)
    if(data.isTitleScreen):
        data.titleScreen.update()
    if(not data.isGameOver and not data.isTitleScreen and not data.isPaused):
        data.game.moveChar(Vector(0,0,-2))
        data.game.update()


#view
def redrawAll(canvas, data):
    clear(canvas, data)
    if(data.isTitleScreen):
        data.titleScreen.render(canvas, data)
    if(not data.isGameOver and not data.isTitleScreen):
        data.game.render(canvas, data)
        UI.renderHUD( #Heads up display for score, health, etc
            canvas, data,
            data.game.health, data.game.score
        )
def clear(canvas,data):
    canvas.create_rectangle(0,0,data.width, data.height, fill = "black")


###################################
####################################
# use the run function as-is
###############################
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
        #redrawAllWrapper(canvas, data) Don't uncomment this. It crashes
    def keyReleaseWrapper(event, canvas, data):
        keyRelease(event, data)
        #redrawAllWrapper(canvas, data)

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
    data.timerDelay = 0 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<KeyPress>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind("<KeyRelease>", lambda event:
                            keyReleaseWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1024, 768)
