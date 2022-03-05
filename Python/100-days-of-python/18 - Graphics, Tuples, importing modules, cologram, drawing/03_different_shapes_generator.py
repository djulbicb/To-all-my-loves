from turtle import *
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

turtle = Turtle()
turtle.shape("turtle")
turtle.setx(0)
turtle.pensize(15)
turtle.speed("fastest")

screen = Screen()

for shapeSide in range(3, 11):
    turtle.color(random.choice(colours))
    angle = 360 / shapeSide
    for i in range(shapeSide):
        turtle.forward(100)
        turtle.right(angle)
        turtle.forward(100)

screen.exitonclick()




directions = [0, 90, 180, 270]
