from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self) -> None:
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", False, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", False, align=ALIGNMENT, font=FONT)

    def l_point(self) -> None:
        self.l_score += 1
        self.update_score()

    def r_point(self) -> None:
        self.r_score += 1
        self.update_score()
