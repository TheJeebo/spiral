import turtle
import math
import time

#sets up the window and main turtle t
turtle.tracer(0,0)
t = turtle.Turtle()
turtle.bgcolor('black')
turtle.setup(1900,1040,0,0)
t.hideturtle()

#will run for 10,000 frames
for j in range(10000):
    #this handles the color shift giving a rainbow effect using sin waves
    t.color(abs(math.sin(j/100)),abs(math.sin((j+1000)/100)),abs(math.sin((j+2000)/100)))
    
    #turtle extends out to 3000 but breaks when outside of window boundaries, this varies depending on the rotation
    for i in range(3000):
        t.rt(45 + j/200)
        t.fd(i)
        
        width = (turtle.window_width() / 2) + 200
        abs_x = abs(t.xcor())
        #checks if turtle is drawing outside window width and breaks
        if abs_x > width:
            break
        
    turtle.update()
    t.reset()
    t.hideturtle()
    turtle.tracer(0,0)
