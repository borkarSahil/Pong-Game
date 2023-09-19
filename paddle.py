from turtle import Turtle

class Paddle(Turtle):
     def __init__(self, x_pos, y_pos):
         super().__init__()
         self.shape("square")
         self.color("white")
         self.speed(0)
         self.shapesize(stretch_wid=5, stretch_len=1)
         self.penup()
         self.goto(x_pos, y_pos)

     def move_Up(self):
         y_position = self.ycor() + 50
         self.goto(x=self.xcor(), y=y_position)

     def move_Down(self):
         y_position = self.ycor() - 50
         self.goto(x=self.xcor(), y=y_position)

