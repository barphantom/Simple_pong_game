from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.display_score()

    def display_score(self):
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.display_score()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.display_score()
