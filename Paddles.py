from turtle import Turtle

PADDLE_MOVE_DISTANCE = 20
UP = 90


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.pu()
        self.setheading(UP)
        self.starting_x = x_pos
        self.starting_y = y_pos
        self.reset_paddle()

    def up(self):
        self.forward(PADDLE_MOVE_DISTANCE)

    def down(self):
        self.backward(PADDLE_MOVE_DISTANCE)

    def reset_paddle(self):
        self.setpos(self.starting_x, self.starting_y)
