from turtle import Turtle

class Paddle(Turtle):


    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.position_x = x
        self.position_y = y
        self.goto(self.position_x, self.position_y)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        x_position = self.xcor()
        y_position = self.ycor() + 20
        self.goto(x_position, y_position)


    def move_down(self):
        x_position = self.xcor()
        y_position = self.ycor() - 20
        self.goto(x_position, y_position)

