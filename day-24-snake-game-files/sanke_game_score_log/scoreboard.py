from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")
FILE_NAME = "score.log"


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.score = 0
        self.highest_score = self.read_score(FILE_NAME)
        self.update_score()

    def update_score(self) -> None:
        self.clear()
        self.write(
            f"Score : {self.score}, Highest Score: {self.highest_score}",
            False, align=ALIGNMENT, font=FONT
        )

    def increase_score(self) -> None:
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score

        self.save_score(FILE_NAME)
        self.score = 0
        self.update_score()

    def save_score(self, file_name):
        with open(file=file_name, mode="w") as snake_file:
            snake_file.write(str(self.highest_score))

    def read_score(self, file_name):
        try:
            with open(file=file_name, mode="r") as snake_file:
                return int(snake_file.read())
        except FileNotFoundError:
            return self.score
        except Exception:
            return self.score
