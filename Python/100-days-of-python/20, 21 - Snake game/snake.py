from turtle import Turtle

STARTING_POSITIONS = start_position = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



    def move(self):
        # for seq_num in range(start=2, stop=0, step=-1): range functions doesnt have keyword arguments
        for seq_num in range(len(self.segments) - 1, 0, -1):
            segment = self.segments[seq_num - 1]
            new_x = segment.xcor()
            new_y = segment.ycor()
            self.segments[seq_num].goto(new_x, new_y)

            segment.forward(MOVE_DISTANCE)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle(shape="square")
        t.penup()
        t.color("white")
        t.goto(position)
        t.speed("fastest")
        self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())



