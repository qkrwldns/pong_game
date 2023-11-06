from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from score import Score
import time

window = Screen()
window.setup(width=600, height=700)
window.bgcolor("black")
window.title("Pong Game")
window.tracer(0)


something = Ball()
user_paddle = Paddle((0,-325))
ai_paddle = Paddle((0,325))

scores =Score()


window.listen()
window.onkeypress(user_paddle.move_right, "Right")
window.onkeypress(user_paddle.move_left, "Left")

user_num = 0
ai_num = 0

game = True
while game:
    if ai_num == 10 or user_num == 10:
        something.home()
        game = False

    scores.show_score()
    time.sleep(something.move_speed)
    window.update()  # 얘가 움직일때마다 계속 업데이트 해줘야함 얘를 루프문에 포함 안시키면 안움직임
    something.move_ball()
    ai_paddle.move_r_ai_paddle()
    if ai_paddle.xcor() == 280:
        ai_paddle.move_l_ai_paddle()

    if ai_paddle.xcor() == - 280:
        ai_paddle.move_l_ai_paddle()

    # detect collision with wall
    if something.xcor() > 280 or something.xcor() < -280:
        # needs to bounce
        something.reverse_ball()

    # detect collision with user_paddle

    if something.ycor() < -300 and something.distance(user_paddle) < 50 or something.ycor() > 300 and something.distance(ai_paddle) < 50:
        something.paddle_reverse_ball()

    # miss ball

    if something.ycor() < -330:
        something.reset_ball_user()
        scores.get_score_ai()
        ai_num += 1

    if something.ycor() > 330:
        something.reset_ball_ai()
        scores.get_score_user()
        user_num += 1

scores.game_over()
something.hideturtle()
window.update()
window.exitonclick()
