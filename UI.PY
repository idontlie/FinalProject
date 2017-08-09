from betterGraphics import *
def renderHUD(canvas, data, health, score):
    w, h = data.width, data.height
    center =  (w/2)-50
    bottom = h-60
    betterText(
        canvas, 40, bottom, "HEALTH: " + str(health), 30
    )
    betterText(
        canvas, data.width-300, bottom, "SCORE: " + str(score), 30
    )
    canvas.create_rectangle(0,0,w,70, fill = "green", stipple = "gray12")
    betterText(
        canvas, center, 7, "MENU", 40
    )
