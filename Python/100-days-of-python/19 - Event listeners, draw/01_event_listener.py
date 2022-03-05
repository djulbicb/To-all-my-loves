from turtle import Turtle, Screen

t = Turtle()
t.speed("fastest")
s = Screen()
s.listen()

def up():
    t.setheading(90)
    t.forward(100)
def down():
    t.setheading(270)
    t.forward(100)
def left():
    t.setheading(180)
    t.forward(100)
def right():
    t.setheading(0)
    t.forward(100)
def move_forwards():
    t.forward(100)

s.onkey(key="space", fun=move_forwards)
s.onkey(key="Up", fun=up)
s.onkey(key="Down", fun=down)
s.onkey(key="Left", fun=left)
s.onkey(key="Right", fun=right)

s.exitonclick()