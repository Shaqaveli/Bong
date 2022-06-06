from turtle import Turtle
import random

BALL_SPEED = 6


class Ball(Turtle):
    def __init__(self, ball_speed):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.ball_speed = ball_speed
        self.x_move = 0
        self.y_move = 0
        self.reset_ball()
        self.pu()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0, 0)
        rand_dir = random.choice([-1, 1])
        self.x_move = self.ball_speed * rand_dir
        rand_dir = random.choice([-1, 1])
        self.y_move = self.ball_speed * rand_dir
