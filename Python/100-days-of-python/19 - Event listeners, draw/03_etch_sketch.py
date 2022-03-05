from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
turtle.speed("fastest")
turtle.pensize(10)
screen.listen()

distance = 20
angle = 10
def backwards():
    turtle.forward(distance)
def forwards():
    turtle.backward(distance)
def turn_left():
    turtle.setheading(turtle.heading() + angle)
def turh_right():
    turtle.setheading(turtle.heading() - angle)
def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.onkeypress(key="w", fun=backwards)
screen.onkeypress(key="s", fun=forwards)
screen.onkeypress(key="d", fun=turh_right)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="c", fun=clear)



screen.exitonclick()