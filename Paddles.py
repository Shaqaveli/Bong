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
        self.setpos(x_pos, y_pos)


    def up(self):
        self.forward(PADDLE_MOVE_DISTANCE)

    def down(self):
        self.backward(PADDLE_MOVE_DISTANCE)
