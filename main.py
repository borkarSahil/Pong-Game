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

game_is_on = True
while game_is_on:
    screen.update()





screen.exitonclick()