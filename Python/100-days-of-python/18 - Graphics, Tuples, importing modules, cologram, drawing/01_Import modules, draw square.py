# Ucitavanje modula na razlicite nacine
import turtle
from turtle import Turtle, Screen
# da sve ucita, ali se ne preporucuje
from turtle import *
import turtle as t

timmy = turtle.Turtle()
timmy = t.Turtle()

turtle = Turtle()
turtle.shape("turtle")
turtle.color("red")

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

screen = Screen()
screen.exitonclick()