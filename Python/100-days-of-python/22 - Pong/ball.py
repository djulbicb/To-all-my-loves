from turtle import Turtle

class Ball(Turtle):

    MOVE_SPEED = 0.1

    def __init__(self):
        super(Ball, self).__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        pass

    def bounce_y(self):
        self.y_move *= -1
        pass

    def bounce_x(self):
        self.x_move *= -1
        self.MOVE_SPEED += 0.9
        pass

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1
        pass