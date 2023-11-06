from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.03

    def move_ball(self):
        x = self.xcor() - self.x_move
        y = self.ycor() - self.y_move
        self.goto(x, y)

    def reverse_ball(self):
        self.x_move *= -1  # -1 을 곱하면 방향이 반대로됨 -10이 돼서 클래스로 들어아고 move_ball은 - 된 방향에 숫자를 더해줘서 반대로!

    def paddle_reverse_ball(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def reset_ball_ai(self):
        self.home()
        self.paddle_reverse_ball()
        self.move_speed = 0.03

    def reset_ball_user(self):
        self.home()
        self.paddle_reverse_ball()
        self.move_speed = 0.03