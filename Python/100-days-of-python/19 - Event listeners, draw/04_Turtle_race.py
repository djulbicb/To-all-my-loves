# Moze biti vise kornjaca, vise instanci
# svaka instanca moze imati razlicite attribute, i da radi razlicite stvari, u programiranju se zove state

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

turtles = []
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

for index in range(0, 6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[index])
    t.goto(x=-230, y=y_positions[index])
    t.speed("fastest")
    turtles.append(t)

keep_running = True
win_color = ""
while (keep_running):
    for turtle in turtles:
        x = turtle.pos()[0]
        print(x)
        if (x >= 230 and win_color == ""):
            # turtle.color() vraca array pen i fill color
            win_color = turtle.pencolor()
            keep_running = False

        turtle.forward(random.randint(0, 10))

print(win_color)
screen.exitonclick()
