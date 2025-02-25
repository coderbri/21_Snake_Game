import time
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)        # ? Stops constant refresh for smoother animations

snake = Snake()
food = Food()

scoreboard = Scoreboard()

# 3. Control the Snake
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()     # ? Refreshes the screen between movements
    time.sleep(0.1)     # ? Delay between movements
    snake.move()

    # Food Detection
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend() # 7. Extend Tail
        scoreboard.increase_score()

    # Game Over Logic: Collisions with Wall and Tail
    if (
            snake.head.xcor() > 280
            or snake.head.xcor() < -280
            or snake.head.ycor() > 280
            or snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
