import turtle
import math
import time

turtle.tracer(0,0)
t = turtle.Turtle()
turtle.bgcolor('black')
turtle.setup(1900,1040,0,0)
t.hideturtle()

for j in range(10000):
    t.color(abs(math.sin(j/100)),abs(math.sin((j+1000)/100)),abs(math.sin((j+2000)/100)))
    for i in range(3000):
        t.rt(45 + j/200)
        t.fd(i)
        
        width = (turtle.window_width() / 2) + 200
        abs_x = abs(t.xcor())
        if abs_x > width:
            break
        
    turtle.update()
    t.reset()
    t.hideturtle()
    turtle.tracer(0,0)