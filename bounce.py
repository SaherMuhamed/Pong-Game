from turtle import Turtle


class Bounce(Turtle):
    def __init__(self):
        super().__init__()
        self.dx = 10
        self.dy = 10
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(x=0, y=0)
        self.move_speed = 0.1
        self.bounce_x()
