import turtle
turtle.shape("turtle")


def draw_star(size,color):
       count = 0
       angle = 144
       for _ in range(5):
           turtle.forward(size)
           turtle.right(angle)
       turtle.end_fill()

draw_star(100,"purple")
