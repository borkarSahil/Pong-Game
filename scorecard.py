from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 15, 'normal')

class ScoreCard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(x=0,y=250)
        self.scoreA = 0
        self.scoreB = 0
        self.display()

    def display(self):
        self.write(arg =f"Player 1 : {self.scoreA}  Player 2 : {self.scoreB}" , move=False, align=ALIGNMENT, font=FONT)
    #
    def increaseScoreA(self):
        self.scoreA += 1
        self.clear()
        self.display()

    def increaseScoreB(self):
        self.scoreB += 1
        self.clear()
        self.display()

    def game_end(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game End !", move=False, align=ALIGNMENT, font=FONT)
        self.goto(0, -50)
        self.write(arg=f"Player 1 : {self.scoreA}  Player 2 : {self.scoreB}", move=False, align=ALIGNMENT, font=FONT)