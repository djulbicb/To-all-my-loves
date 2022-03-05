# colorgram - biblioteka koja izvlaci paletu iz slike
import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract("dots.jpg", 30);
# jos jedna varijanta extrakcije
colorPack = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colorPack.append((r, g, b))

turtle = Turtle()
screen = Screen()
screen.colormode(255)

dimension = 10
forward = 20
radius = 5

turtle.speed("fastest")
for i in range(1, dimension):
    for j in range(1, dimension):
        color = colors[random.randint(0, len(colors) - 1)]
        turtle.color(color.rgb)

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(forward)
    turtle.back(100 * forward)
    turtle.goto(0, -forward * i)

screen.exitonclick()

