from turtle import Screen, Turtle

SIZE = 20
STARTING_POSITIONS = [(0, 0), (-SIZE, 0), (-SIZE * 2, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.to_initial_pos()


    def to_initial_pos(self):
        self.segments = []
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

        self.head = self.segments[0]


    def restart(self):
        for seg in self.segments:
            seg.hideturtle()

        self.to_initial_pos()


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(SIZE)


    def add_segment(self, pos):
        seg = Turtle('square')
        seg.penup()
        seg.color('#c6c8d1')
        seg.goto(pos)
        self.segments.append(seg)


    def extend(self):
        new_seg_pos = self.segments[-1].position()
        self.add_segment(new_seg_pos)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
