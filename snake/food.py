from turtle import Screen, Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        # food size is 10x10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('#84a0c6')
        self.speed('fastest')
        self.refresh()


    def refresh(self):
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)
