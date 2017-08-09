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
    betterRect(canvas,0,0,w,70, Colors.green, "gray12")
    betterText(
        canvas, center, 7, "MENU", "white", 40
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
