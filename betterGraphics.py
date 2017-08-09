def betterLine(canvas,x,y,x0,y0, fill = "green"):
    #Just in case things rendered to far offscreen glitch out
    #Commented for more performance?
    #x = max(min(x,data.width+1), -1)
    #y = max(min(y,data.height+1), -1)
    #x0= max(min(x0,data.width+1), -1)
    #y0= max(min(y0,data.height+1), -1)
    canvas.create_line(x,y,x0,y0, fill = fill)

def betterCircle(canvas, x, y, radius, fill):
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill = fill)

def betterText(canvas, x,y, text, size):
    canvas.create_text(x,y, text = text,
    font = ('fixedsys',str(size)),
    fill = "white", anchor = "nw")
