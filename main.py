from turtle import Screen
from Paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Difficulty
SCREEN_UPDATE_SPEED = 0.04
BALL_SPEED = 6
END_OF_GAME_SCORE = 5

# Controls
RIGHT_PLAYER_UP = "Up"
RIGHT_PLAYER_DOWN = "Down"
LEFT_PLAYER_UP = "w"
LEFT_PLAYER_DOWN = "s"

# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.title("Bong")
screen.setup(width=800, height=600)
screen.tracer(0)
scoreboard = Scoreboard()

# Placing Paddles
right_player = Paddle(350, 0)
left_player = Paddle(-350, 0)
# Placing Pong Ball
ball = Ball(BALL_SPEED)
# Listen for inputs
screen.listen()
screen.onkey(right_player.up, RIGHT_PLAYER_UP)
screen.onkey(right_player.down, RIGHT_PLAYER_DOWN)
screen.onkey(left_player.up, LEFT_PLAYER_UP)
screen.onkey(left_player.down, LEFT_PLAYER_DOWN)

# Game Loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SCREEN_UPDATE_SPEED)
    ball.move()

    # Checking for wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_player) < 40 and ball.xcor() > 340:
        ball.bounce_x()
        SCREEN_UPDATE_SPEED *= 0.8

    if ball.distance(left_player) < 40 and ball.xcor() < -340:
        ball.bounce_x()
        SCREEN_UPDATE_SPEED *= 0.8

    if ball.xcor() > 390:
        scoreboard.left_goal()
        scoreboard.update_scoreboard()
        SCREEN_UPDATE_SPEED = 0.04
        ball.reset()
        right_player.reset()
        left_player.reset()

    if ball.xcor() < -390:
        scoreboard.right_goal()
        scoreboard.update_scoreboard()
        SCREEN_UPDATE_SPEED = 0.04
        ball.reset()
        right_player.reset()
        left_player.reset()

    if scoreboard.left_player_score == END_OF_GAME_SCORE or scoreboard.right_player_score == END_OF_GAME_SCORE:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
