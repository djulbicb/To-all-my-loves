from turtle import *
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.color("red")
turtle.setx(0)

screen = Screen()
screen.setworldcoordinates(-1, -1, screen.window_width(), screen.window_height())

for i in range(20):
    turtle.penup()
    turtle.forward(random.randint(10,50))
    turtle.pendown()
    turtle.forward(random.randint(10,50))


screen.exitonclick()
