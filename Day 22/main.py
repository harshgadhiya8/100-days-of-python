from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreborard import Score
import time
paddles=[]
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((370,0))
l_paddle = Paddle((-370,0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detecting collision with wall
    if ball.ycor()> 280 or ball.ycor()< -280:
        ball.bounce_y()

    #detecting with collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    #detecting when the paddle misses
    if ball.xcor() > 380: #right paddle
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380: #left paddle
        ball.reset_position()
        score.r_point()

screen.exitonclick()