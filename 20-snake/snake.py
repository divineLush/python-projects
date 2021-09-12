from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        for pos in STARTING_POSITIONS:
            seg = Turtle('square')
            seg.penup()
            seg.color('#c6c8d1')
            seg.goto(pos)
            self.segments.append(seg)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(20)
        self.segments[0].left(90)
