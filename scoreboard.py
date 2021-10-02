from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.update_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score()

    def score(self):
        self.write(arg=f"{self.update_score}", move=False, align="center", font=("Courier", 80, "normal"))
        self.update_score += 1

    def new_score(self):
        self.clear()
        self.score()

