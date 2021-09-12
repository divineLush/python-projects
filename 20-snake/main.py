from turtle import Screen
from time import sleep
from snake import Snake


snake = Snake()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('#161821')
screen.title('snake')
screen.tracer(0)

is_game_on = True
while is_game_on:
    screen.update()
    sleep(0.1)

    snake.move()


screen.exitonclick()
