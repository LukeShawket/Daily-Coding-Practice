from random import randint
from time import sleep
from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
        self.showturtle()


    def goto_new_position(self):
        self.hideturtle()
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
        self.showturtle()