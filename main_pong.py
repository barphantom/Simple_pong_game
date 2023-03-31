from turtle import Screen
from Paddle import paddle
from Ball import Ball
from Score_board_file import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)


pap_R = paddle((350, 0))
pap_L = paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(pap_R.go_up, "Up")
screen.onkeypress(pap_R.go_down, "Down")

screen.onkeypress(pap_L.go_up, "w")
screen.onkeypress(pap_L.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move_ball()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #need to bounce the ball
        ball.bounce_ball_y()

    if ball.distance(pap_R) < 50 and ball.xcor() > 320:
        print(f"Made contact")
        ball.bounce_ball_x()

    if ball.distance(pap_L) < 50 and ball.xcor() < -320:
        print(f"Made contact")
        ball.bounce_ball_x()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.whose_point = -1
        ball.reset_game()
    elif ball.xcor() < -380:
        scoreboard.r_point()
        ball.whose_point = 1
        ball.reset_game()



screen.exitonclick()
