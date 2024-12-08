from importlib.metadata import files
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.goto(0, 250)
        self.hideturtle()
        self.color("white")
        with open("D:\PyhtonLearn\SnakeGame\data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0

    def show_score(self, score):
        self.clear()
        self.score = score
        self.write(f"Score : {score}  High Score: {self.high_score}", False, "center", ("Arial", 18, "bold"))

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.score}")
