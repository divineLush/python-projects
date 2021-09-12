from turtle import Screen, Turtle
from random import randint


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('#e2a478')
        self.speed('fastest')
        self.goto(0, 260)
        self.hideturtle()
        self.write_score()


    def write_score(self):
        self.write(f'Score: {self.score}', align='center', font=('Mono', '14', 'normal'))


    def update(self):
        self.clear()
        self.write_score()


    def inc(self):
        self.score += 1
        self.update()


    def game_over(self):
        self.goto(0, 0)
        self.color('#e27878')
        self.write('GAME OVER', align='center', font=('Mono', '14', 'normal'))
