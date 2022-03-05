from turtle import Turtle

ALIGN = "center"
FONT = ("Ariel", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update()

    def increase(self):
        self.score += 1
        self.clear()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

