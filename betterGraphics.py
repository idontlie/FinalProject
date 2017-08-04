def betterLine(canvas,data,x,y,x0,y0, fill = "green"):
    x = max(min(x,data.width+1), -1)
    y = max(min(y,data.height+1), -1)
    x0= max(min(x0,data.width+1), -1)
    y0= max(min(y0,data.height+1), -1)
    canvas.create_line(x,y,x0,y0, fill = fill)
