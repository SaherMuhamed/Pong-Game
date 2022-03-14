import time
from turtle import Screen, Turtle
from paddle import Paddle
from bounce import Bounce
from scoreboard import Scoreboard


def dash_lines():
    lines = Turtle()
    lines.width(5)
    lines.speed("fastest")
    lines.setheading(90)
    lines.hideturtle()
    lines.color("white")
    lines.penup()
    lines.goto(x=0, y=-230)
    for _ in range(12):
        lines.pendown()
        lines.forward(20)
        lines.penup()
        lines.forward(20)


# TODO 1: Create the screen, Setup the screen.
screen = Screen()
screen.title("Pong Game")
screen.tracer(0)
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.listen()
dash_lines()


# TODO 2: Create and move the left paddle.
left_paddle = Paddle((-390, 0))
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

# TODO 3: Create and move the right paddle.
right_paddle = Paddle((380, 0))
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

# TODO 4: Create the ball and make it move.
ball = Bounce()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    print(ball.move_speed)
    screen.update()
    ball.move_ball()

    # TODO 5: Detect collision with wall and bounce.
    if ball.ycor() > 235 or ball.ycor() < -235:
        ball.bounce_y()

    # TODO 6: Detect collision with another paddle.
    if ball.distance(right_paddle) < 15 and ball.xcor() > 365:
        ball.bounce_x()
        scoreboard.r_point()

    if ball.distance(left_paddle) < 15 and ball.xcor() < -360:
        ball.bounce_x()
        scoreboard.l_point()

    # TODO 7: Detect when paddle missed.
    if ball.xcor() > 400:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()
