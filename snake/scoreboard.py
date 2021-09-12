from turtle import Screen, Turtle
from random import randint


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_high_score()
        self.penup()
        self.speed('fastest')
        self.to_initial_pos()
        self.hideturtle()
        self.write_score()


    def to_initial_pos(self):
        self.color('#e2a478')
        self.goto(0, 260)


    def write_score(self):
        self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=('Mono', '14', 'normal'))


    def update(self):
        self.clear()
        self.update_high_score()
        self.write_score()


    def inc(self):
        self.score += 1
        self.update()


    def update_high_score(self):
        if self.score <= self.high_score:
            return

        self.high_score = self.score
        with open('highscore.txt', mode='w') as file:
            file.write(str(self.high_score))


    def read_high_score(self):
        with open('highscore.txt') as file:
            contents = file.read()
            self.high_score = int(contents)


    def game_over(self):
        self.color('#e27878')
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Mono', '14', 'normal'))


    def restart(self):
        self.to_initial_pos()
        self.score = 0
        self.update()
