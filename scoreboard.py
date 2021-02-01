from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.setposition(0, 260)
        self.hideturtle()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over", align="center", font=FONT)