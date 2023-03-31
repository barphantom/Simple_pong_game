from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.build_ball()
        self.x_move = 10
        self.y_move = 10
        self.whose_point = 1

    def build_ball(self):
        self.shape('circle')
        self.color('white')
        self.shapesize()
        self.penup()
        self.goto(0, 0)

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_ball_y(self):
        self.y_move *= -1
        self.add_speed()

    def bounce_ball_x(self):
        self.x_move *= -1
        self.add_speed()

    def add_speed(self):
        self.x_move *= 1.1
        self.y_move *= 1.1

    def reset_game(self):
        self.clear()
        self.build_ball()
        self.x_move = 10 * self.whose_point
        self.y_move = 10


