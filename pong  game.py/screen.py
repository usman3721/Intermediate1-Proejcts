from turtle import Turtle,Screen
from paddle import Paddle
from scoreboard import Scorebaord
from ball import Ball
import time


screen=Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scorebaord=Scorebaord()


screen.listen()
screen.onkeypress(fun=l_paddle.up, key="Up")
screen.onkeypress(fun=l_paddle.back, key="Down")
screen.onkeypress(fun=r_paddle.up, key="w")
screen.onkeypress(fun=r_paddle.back, key="s")
screen_on=True
while screen_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
        
        
    if ball.distance(r_paddle) < 50 and ball.xcor()> 320 or ball.distance(l_paddle) < 50 and ball.xcor()< -320 :
        ball.bounce_x()

    if ball.xcor()> 380:
        ball.reset_position()
        scorebaord.l_point()
        
        
    if ball.xcor()< -380:
        ball.reset_position()
        scorebaord.r_point()
        




       
        





































screen.exitonclick()