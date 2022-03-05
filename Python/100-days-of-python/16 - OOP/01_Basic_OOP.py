import another_module
from another_module import another_data
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

print(another_module.another_data)
print(another_data)

timmy.color("orange")
timmy.forward(100)
timmy.shape("turtle")
screen.exitonclick()