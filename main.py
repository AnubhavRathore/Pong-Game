from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
l_scoreboard = Scoreboard((-100, 200))
r_scoreboard = Scoreboard((100, 200))
screen.listen()
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")

game_is_on = True

while game_is_on:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() >= 330 or ball.xcor() <= -330:
        if ball.distance(l_paddle) < 50 or ball.distance(r_paddle) < 50:
            ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_position()
        l_scoreboard.new_score()

    if ball.xcor() < -400:
        ball.reset_position()
        r_scoreboard.new_score()

    '''below two methods are my own method to reverse the direction of ball when opponent loses.'''

    # if ball.xcor() > 400 or ball.xcor() < -400:
    #     ball = Ball()
    #     if ball.xcor() > 400:
    #         ball.bounce_y()
    #         ball.bounce_x()
    #     ball.move()

    # if ball.xcor() < -400:
    #     ball = Ball()
    #     ball.move()

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

screen.exitonclick()
