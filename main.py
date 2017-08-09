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
    data.mousePressed = False
    data.mouseX, data.mouseY = 0,0
    data.mouseTime = 0
    data.isTitleScreen = True
    data.isPaused = False
    data.isHelp = False
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
    data.mousePressed = True
def mouseReleased(event, data):
    data.mousePressed = False
def mouseMoved(event, data):
    data.mouseTime = 0
    data.mouseX = event.x
    data.mouseY = event.y
def keyPressed(event, data):
    #All keyboard data stored in data.chars dictionary
    char = event.char.lower()
    data.chars[char] = True
    if(char == " "):
        data.game.jumpChar()
    if(char == "z"):
        data.game.createEnemy()
    if(char == "p"):
        data.isPaused = not data.isPaused
    if(char == "h"):
        data.isHelp = not data.isHelp

def keyRelease(event, data):
    data.chars[event.char.lower()] = False

def keyActions(data):

    #CHARACTER MOTION INPUT
    if(data.chars['a']):
        data.game.moveChar(Vector(0,2,0))
    if(data.chars['d']):
        data.game.moveChar(Vector(0,-2,0))

    #CAMERA MOTION KEYBOARD INPUT
    if(data.chars['i']):
        data.game.movCam(Angle(0,0,1))
    if(data.chars['j']):
        data.game.movCam(Angle(0,1,0))
    if(data.chars['k']):
        data.game.movCam(Angle(0,0,-1))
    if(data.chars['l']):
        data.game.movCam(Angle(0,-1,0))

    #RESET GAME INPUT
    if(data.chars['r']):
        data.game.reset()
        data.game.moveChar(Vector(0,-2,0))
        data.isGameOver = False
def timerFired(data):
    data.mouseTime += 1
    data.time += 1
    keyActions(data)
    if(data.isTitleScreen):
        w = data.width
        h = data.height
        data.titleScreen.update()
        if(data.mousePressed and data.mouseX > w-750 and\
                data.mouseY > h - 410 and data.mouseY < (h - 410) + 116):
            data.isTitleScreen = False
    if(not data.isGameOver and not data.isTitleScreen and not data.isPaused and not data.isHelp):
        data.game.moveChar(Vector(0,0,-2))
        data.game.update()
        if(data.game.health<0):
            data.isGameOver = True


#view
def redrawAll(canvas, data):
    clear(canvas, data)
    if(data.isTitleScreen and not data.isHelp):
        data.titleScreen.render(canvas, data)
    elif(data.isGameOver):
        UI.renderGameOVR(canvas, data, data.game.score)
    elif(data.isPaused):
        UI.renderPaused(canvas, data)
    elif(data.isHelp):
        UI.renderHelp(canvas, data)
    else:
        #render game
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

    def mouseReleasedWrapper(event, canvas, data):
        mouseReleased(event, data)
    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
    def mouseMovedWrapper(event, canvas, data):
        mouseMoved(event, data)
        #redrawAllWrapper(canvas, data)
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
    data.timerDelay = 10 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<ButtonRelease-1>", lambda event:
                            mouseReleasedWrapper(event, canvas, data))
    root.bind("<Motion>", lambda event:
                            mouseMovedWrapper(event, canvas, data))
    root.bind("<KeyPress>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind("<KeyRelease>", lambda event:
                            keyReleaseWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1024, 768)
