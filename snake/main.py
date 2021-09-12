from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard


snake = Snake()
food = Food()
scoreboard= Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('#161821')
screen.title('snake')
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

is_game_on = True

def game_over():
    global is_game_on
    is_game_on = False
    scoreboard.game_over()


def start_game():
    global is_game_on
    while is_game_on:
        screen.update()
        sleep(0.1)
        snake.move()

        # detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.inc()

        # detect collision with wall
        is_wall_right = snake.head.xcor() > 295
        is_wall_left = snake.head.xcor() < -295
        is_wall_top = snake.head.ycor() > 295
        is_wall_bottom = snake.head.ycor() < -295
        if is_wall_right or is_wall_left or is_wall_top or is_wall_bottom:
            game_over()

        # detect collision with tail
        for seg in snake.segments[1:]:
            if snake.head.distance(seg) < 10:
                game_over()


start_game()


def restart_game():
    print('restart')
    scoreboard.restart()
    food.refresh()
    snake.restart()

    global is_game_on
    is_game_on = True

    start_game()


screen.onkey(restart_game, 'space')

screen.exitonclick()
