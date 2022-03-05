from turtle import Turtle, Screen
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

screen = Screen()
screen.colormode(255)

turtle = Turtle()
turtle.speed("fastest")

r = 150

def draw_spirograph(size_of_gap):
    for _ in range(0, int(360 / size_of_gap)):
        turtle.circle(r)
        turtle.color(random_color())
        turtle.setheading(turtle.heading() + size_of_gap)

draw_spirograph(10)
screen.exitonclick()