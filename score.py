from turtle import Turtle

ALIGN = "center"
FONT = ("Arial",50,"normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.ai_score = 0
        self.user_score = 0

    def show_score(self):
        self.clear()
        self.goto(260, -130)
        self.write(self.user_score, align=ALIGN, font=FONT)
        self.goto(260, 70)
        self.write(self.ai_score, align=ALIGN, font=FONT)

    def get_score_ai(self):
        self.ai_score += 1
        # self.clear()
        # self.write(self.ai_score, align=ALIGN, font=FONT)

    def get_score_user(self):
        self.user_score += 1
        # self.clear()
        # self.write(self.user_score, align=ALIGN, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"    Game Over \nuser: {self.user_score} and ai:{self.ai_score}",align=ALIGN, font=("Arial",20,"normal"))
