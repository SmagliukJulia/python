import turtle
from random import *
turtle.shape("turtle")
turtle.speed(10)


for i in range(50):
    step=randint(1,30)
    angle=randint(0,360)
    side=randint(1,2)
    turtle.forward(step)
    if side==1:
        turtle.left(angle)
        turtle.forward(step)
    else:
        turtle.right(angle)
        turtle.forward(step)

turtle.hideturtle()
turtle.done()
