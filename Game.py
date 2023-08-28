import turtle
import random
from random import randint

game_over = False

db = turtle.Screen()
db.screensize(1000, 1000)
db.bgcolor("#FF4D00")
db.title("Catch the Turtle")

max_hight = db.window_height() / 2

fo_nt = ("subway", "20", "normal")

score = 0

all_turtles = []

recorder = turtle.Turtle()
recorder.hideturtle()
recorder.color("#05F3E3")
recorder.penup()
y_recorder = max_hight * 0.9
recorder.setpos(0, y_recorder)
recorder.write(arg=f"Score: {score}", move=False, align="center", font=fo_nt)

timer_turtle = turtle.Turtle()


def turtle_creator():
    if not game_over:
        def clicker(x, y):
            global score
            score += 1
            recorder.clear()
            recorder.write(arg=f"Score: {score}", move=False, align="center", font=fo_nt)

        t1 = turtle.Turtle()
        t1.onclick(clicker)
        t1.penup()
        t1.hideturtle()
        t1.shape("turtle")
        t1.shapesize(1.75)
        t1.color("#246B00")
        t1.setpos(randint(-500, 500), randint(-200, 200))
        t1.hideturtle()
        all_turtles.append(t1)


def blanket():
    for tt in all_turtles:
        tt.hideturtle()


def show_rand():
    if not game_over:
        blanket()
        random.choice(all_turtles).showturtle()
        db.ontimer(show_rand, 500)


def time_counter(time):
    timer_turtle.hideturtle()
    timer_turtle.color("#05F3E3")
    timer_turtle.penup()
    y_timer = (max_hight * 0.9) - (35)
    timer_turtle.setpos(0, y_timer)
    timer_turtle.clear()
    if time > 0:
        timer_turtle.write(arg=f"Time: {time}", move=False, align="center", font=fo_nt)
        db.ontimer(lambda: time_counter(time - 1), 500)
    else:
        global game_over
        game_over = True
        timer_turtle.clear()
        blanket()
        timer_turtle.write(arg="Game Over", move=False, align="center", font=fo_nt)


turtle.tracer(0)

if not game_over:
    time_counter(10)
    turtle_creator()
    turtle_creator()
    turtle_creator()
    turtle_creator()
    turtle_creator()
    turtle_creator()
    turtle_creator()
    turtle_creator()
    turtle_creator()
    turtle_creator()
    turtle_creator()
    turtle_creator()
    turtle_creator()
    turtle_creator()
    turtle_creator()
    turtle_creator()
    turtle_creator()
    turtle_creator()
    turtle_creator()
    turtle_creator()
    turtle_creator()
    show_rand()
if game_over:
    blanket()

turtle.tracer(1)

turtle.done()
