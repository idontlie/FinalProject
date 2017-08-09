def betterLine(canvas,x,y,x0,y0, fill = "green", width = 1):
    #Just in case things rendered to far offscreen glitch out
    #Commented for more performance?
    #x = max(min(x,data.width+1), -1)
    #y = max(min(y,data.height+1), -1)
    #x0= max(min(x0,data.width+1), -1)
    #y0= max(min(y0,data.height+1), -1)
    canvas.create_line(x,y,x0,y0, fill = fill, width = width)

def betterCircle(canvas, x, y, radius, fill):
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius,
     fill = fill)

def betterSquare(canvas, x, y, radius, fill):
    canvas.create_rectangle(x-radius, y-radius, x+radius, y+radius,
     fill = fill)

def betterRect(canvas, x, y, xSize,ySize, fill, stipple, width = 1):
    canvas.create_rectangle(x,y, x + xSize, y + ySize,
     fill = fill, stipple = stipple, width = width, outline = "white")

def betterText(canvas, x,y, text, fill, size):
    canvas.create_text(x,y, text = text,
    font = ('fixedsys',str(size)),
    fill = fill, anchor = "nw")

def betterTextTitle(canvas, x,y, text, fill, size):
    canvas.create_text(x,y, text = text,
    font = ('system',str(size)),
    fill = "white", anchor = "nw")

class Colors(object):
    red = "#ff0000"
    green = "#00ff00"
    blue = "#0000ff"
