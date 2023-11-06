from turtle import Turtle

user_paddle = (0,-325)
ai_paddle = (0,325)
paddles = [user_paddle,ai_paddle]


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(1, 4)
        self.goto(position)
        self.r_move = 20

    def move_right(self):
        if self.xcor() <= 250:
            new_x = self.xcor() + 20  # Move the paddle 10 units to the right // fd로 움직 X 위치 변경임!
            self.goto(new_x, self.ycor())

    def move_left(self):
        if self.xcor() >= -250:
            new_x = self.xcor() - 20  # Move the paddle 10 units to the right
            self.goto(new_x, self.ycor())

    def move_r_ai_paddle(self):
        new_x = self.xcor() + self.r_move
        self.goto(new_x, self.ycor())


    def move_l_ai_paddle(self):
        self.r_move *= -1