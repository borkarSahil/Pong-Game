# TODO : Border and middle line
# TODO : Score Card
# TODO : 2 Turtle which will move
# TODO : 1 ball

# TODO : CREATE THE SCREEN
# TODO : CREATE AND MOVE A PADDLE
# TODO : CREATE ANOTHER PADDLE
# TODO : CREATE THE BALL AND MAKE IT MOVE
# TODO : DETECT COLLISION WITH WALL AND BOUNCE
# TODO : DETECT COLLISION WITH PADDLE
# TODO : DETECT WHEN PADDLE MISSES
# TODO : KEEP SCORE

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorecard import ScoreCard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Paddle
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.listen()
# Right paddle Movements
screen.onkey(key="Up", fun=r_paddle.move_Up)
screen.onkey(key="Down", fun=r_paddle.move_Down)

# Left paddle Movements
screen.onkey(key="w", fun=l_paddle.move_Up)
screen.onkey(key="s", fun=l_paddle.move_Down)

# Ball
ball = Ball()

# Score Board
scoreboard = ScoreCard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#     Detect the collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

#     Detect collision with r_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        # print("Made Contact")
        # ball.speed()
        ball.bounce_x()

#      When ball passes the paddle
    if ball.xcor() > 380:
        scoreboard.increaseScoreA()
        ball.reset_position()
    elif ball.xcor() < -380:
        scoreboard.increaseScoreB()
        ball.reset_position()

    if scoreboard.scoreB >= 5 or scoreboard.scoreA >= 5:
        game_is_on = False

scoreboard.game_end()




screen.exitonclick()