from math import sqrt, ceil
from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape('turtle')
turtle.color('#c6c8d1')
turtle.speed(0)

def draw_square(size=100):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)


square_size = 250
angle = 15

squares_count = int(360 / angle)
radius = int(ceil(square_size * sqrt(2) / 2))

for i in range(squares_count):
    draw_square(square_size)
    turtle.circle(radius)
    turtle.right(angle)

screen = Screen()
screen.bgcolor('#161821')
screen.exitonclick()
