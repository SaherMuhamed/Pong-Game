from turtle import Turtle

FONT = ('Courier', 50, 'bold')


class Scoreboard(Turtle):
    # TODO 8: Keep score.
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-150, y=170)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(x=150, y=170)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
