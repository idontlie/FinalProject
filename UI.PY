from betterGraphics import *
def renderHUD(canvas, data, health, score):
    w, h = data.width, data.height
    center =  (w/2)-50
    bottom = h-60
    betterText(
        canvas, 40, bottom, "HEALTH: " + str(health), "white", 30
    )
    betterText(
        canvas, w-300, bottom, "SCORE: " + str(score),"white", 30
    )
    lim = 20
    if(data.mouseTime > lim):
        if(data.mouseTime < 40):
            betterRect(canvas, 0, 0, w, 70-(data.mouseTime-lim)**2, Colors.green, "gray12")
            betterText(
                canvas, 40, 10-(data.mouseTime-lim)**2, "Press 'p' to pause or 'h' for help", "white", 30
            )
    else:
        betterRect(canvas, 0, 0, w, 70, Colors.green, "gray12")
        betterText(
            canvas, 40, 10, "Press 'p' to pause or 'h' for help", "white", 30
            )

def renderPaused(canvas, data):
    w, h = data.width, data.height
    betterText(
        canvas, 325, (h/2)-50, "GAME_PAUSED", "white", 100
        )
    betterText(
        canvas, 175, 600, "  PRESS P TO UNPAUSE\n(or press r to restart)", "white", 40
    )
def renderHelp(canvas, data):
    betterText(
        canvas,  20, 20, """\


tl;dr:
\t 'A' and 'D' keys move the _Character™
\t 'IJKL' keys rotate the camera to get more points




Inside_The_Box_™ is a game about dodging obstacles
Use the 'a' and 'd' keys to move the _Character™
Each time you crash into an _Obstacle™, you lose
one health and one point

The goal of the game is to earn as many points as possible
The player earns points whenever obstacles make
it behind the _Character™ without a collision.
To earn more points for each obstacle, you can use the
'IJKL' keys to rotate the camera. This multiplies the points
per _Obstacle™ by the speed at which the camera is moving
The faster you rotate the camera, the more points you can get
However as you get more points, the rate of _Obstacle™ spawn
increases and so does the camera rotation speed

""", "white", 24
    )
def renderGameOVR(canvas, data, score):
    w, h = data.width, data.height
    if(data.time%20>2):
        betterText(
            canvas, 325, (h/2)-50, "GAME_OVER", "white", 100
            )
    else:
        betterText(
            canvas, 325, (h/2)-50, "GAME_OVER", Colors.red, 100
            )
    betterText(
        canvas, 400, 150, "SCORE: " + str(score),"white", 30
    )
    betterText(
        canvas, 200, 600, "PRESS R TO TRY AGAIN", "white", 40
    )
