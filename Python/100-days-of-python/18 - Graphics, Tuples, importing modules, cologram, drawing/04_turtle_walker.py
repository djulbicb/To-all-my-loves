from turtle import *
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0,90,180,270]
distance = 30

turtle = Turtle()
turtle.pensize(15)
turtle.speed("fastest")

screen = Screen();
screen.colormode(255)

for i in range(500):
    turtle.setheading(random.choice(directions)) # umesto right, left
    # turtle.color(random.choice(colours))
    turtle.color(random_color())
    turtle.forward(distance)
