from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.score = 0
        self.update_score()

    def update_score(self) -> None:
        self.clear()
        self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self) -> None:
        self.score += 1
        self.update_score()

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write("GAME OVER!", False, align=ALIGNMENT, font=FONT)
