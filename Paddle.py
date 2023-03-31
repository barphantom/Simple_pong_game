from turtle import Turtle


class paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.coordinates = coordinates
        self.build_paddles()

    def build_paddles(self):
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.coordinates)

    def go_up(self):
        new_y = self.ycor() + 45
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 45
        self.goto(self.xcor(), new_y)
