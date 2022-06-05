from turtle import Turtle
import time
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_player_score = 0
        self.left_player_score = 0
        self.color("white")
        self.pu()
        self.update_scoreboard()
        self.hideturtle()

    def left_goal(self):
        self.goto(0, 0)
        self.write("Player 1 scored !", font=FONT, align=ALIGNMENT)
        time.sleep(2)
        self.left_player_score += 1
        self.clear()

    def right_goal(self):
        self.goto(0, 0)
        self.write("Player 2 scored !", font=FONT, align=ALIGNMENT)
        time.sleep(2)
        self.right_player_score += 1
        self.clear()

    def update_scoreboard(self):
        self.goto(0, 260)
        self.write(f"{self.left_player_score} | {self.right_player_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        if self.right_player_score > self.left_player_score:
            self.write("Player 2 wins !", font=FONT, align=ALIGNMENT)
        else:
            self.write("Player 1 wins !", font=FONT, align=ALIGNMENT)
