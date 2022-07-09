from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()


screen.tracer(0)

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "q")
screen.onkey(left_paddle.move_down, "a")


end_of_game = False
while not end_of_game:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_to_right_edge()
    # detect collision between the up or bottom wall and the ball

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with paddle and make the ball bounce
    if (ball.distance(right_paddle) < 50 and ball.xcor()) > 320 or (ball.distance(left_paddle)<50 and ball.xcor() < \
            -320):
        ball.bounce_x()

    # when the right paddle misses a game and restarting
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_points()
    # when the left paddle misses a ball, the ball should move over to the centre
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_points()



screen.exitonclick()
