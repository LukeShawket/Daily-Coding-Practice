from turtle import Turtle

FONT = ("Arial", 22, "bold")
class GameOver:
    def __init__(self, score):
        self.game_over = Turtle()
        self.game_over.speed("slowest")
        self.game_over.penup()
        self.game_over.hideturtle()
        self.game_over.color("white")
        self.final_score = score

    def show_result(self,high_score):
        self.game_over.write(f"      Game Over!\nYour final score is {self.final_score}\n"
                             f"Your high score is {high_score}", True, "center", FONT)