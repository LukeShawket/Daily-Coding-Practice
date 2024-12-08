from random import randint
from turtle import Turtle
import random

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self, body):
        self.body_parts = body
        self.base_poses = [(0, 0), (-20, 0), (-40, 0)]

    def create_base_body(self):
        for pose in self.base_poses:
            body_part = Turtle("circle")
            body_part.speed("fastest")
            body_part.penup()
            body_part.color("orange")
            body_part.goto(pose)
            self.body_parts.append(body_part)

    def movement(self):
        for i in range(len(self.body_parts) - 1, 0, -1):
            x = self.body_parts[i - 1].xcor()
            y = self.body_parts[i - 1].ycor()
            self.body_parts[i].goto(x, y)
        self.body_parts[0].forward(20)

    def up_head(self):
        if self.body_parts[0].heading() != DOWN:
            self.body_parts[0].setheading(UP)

    def left_head(self):
        if self.body_parts[0].heading() != RIGHT:
            self.body_parts[0].setheading(LEFT)

    def down_head(self):
        if self.body_parts[0].heading() != UP:
            self.body_parts[0].setheading(DOWN)

    def right_head(self):
        if self.body_parts[0].heading() != LEFT:
            self.body_parts[0].setheading(RIGHT)

    def get_bigger(self):
        part = Turtle("circle")
        part.speed("fastest")
        part.hideturtle()
        part.color("orange")
        part.penup()
        part.setposition(self.body_parts[len(self.body_parts)-1].xcor(),
                         self.body_parts[len(self.body_parts)-1].ycor())
        self.body_parts.append(part)
        part.showturtle()

    def detect_wall(self):
        if -285 >= self.body_parts[0].xcor() or self.body_parts[0].xcor() >= 285:
            return True
        if -285 >= self.body_parts[0].ycor() or self.body_parts[0].ycor() >= 285:
            return True

    def detect_tail(self):
        for part in self.body_parts[2:]:
            if self.body_parts[0].distance(part) < 10:
                return True

    def explode(self):
        for part in self.body_parts:
            random_dir = randint(0, 360)
            part.speed("fastest")
            part.setheading(random_dir)
            part.forward(50)
