from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as file:
            high_score = int(file.read())
        self.high_score = high_score
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}\tHigh Score : {self.high_score}", align="center", font=("Arial", 16, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}\tHigh Score : {self.high_score}", align="center", font=("Arial", 16, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER!", align="center", font=("Arial", 16, "normal"))
    #

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as file:
                file.write(f"{self.score}")
            print("working")
        self.score = 0
        with open("score.txt") as file:
            high_score = int(file.read())
        self.clear()
        self.write(f"Score: {self.score}\tHigh Score : {high_score}", align="center", font=("Arial", 16, "normal"))


