from turtle import Turtle, Screen
from snake import Snake
from food import Food
import score_board
import time
import game_result

body_parts = []
game_is_started = True
score = 0

my_screen = Screen()
my_screen.title("Snake Game")
my_screen.setup(600, 600)
my_screen.bgcolor("black")
score_text = score_board.Score()
score_text.show_score(score)

snake = Snake(body_parts)
snake.create_base_body()
food = Food()


my_screen.onkey(snake.up_head, "Up")
my_screen.onkey(snake.left_head, "Left")
my_screen.onkey(snake.down_head, "Down")
my_screen.onkey(snake.right_head, "Right")
my_screen.listen()

while game_is_started:
    my_screen.update()
    time.sleep(0.1)
    snake.movement()
    snake.detect_wall()
    snake.detect_tail()
    if snake.detect_wall() or snake.detect_tail():
        score_text.update_high_score()
        snake.explode()
        game_over = game_result.GameOver(score)
        score_text.clear()
        game_over.show_result(score_text.high_score)
        game_is_started = False
    if body_parts[0].distance(food) <= 15.0:
        snake.get_bigger()
        food.goto_new_position()
        score += 1
        score_text.show_score(score)

my_screen.exitonclick()