from turtle import Screen
import random
import time
from snake import Snake
from scoreboard import scoreboard
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("yellow green")
screen.title("SNAKE GAME")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score = 0

    #detect collision from food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_on = False
        scoreboard.game_over()

    #detect collision with tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game_on = False
            scoreboard.game_over()






screen.exitonclick()