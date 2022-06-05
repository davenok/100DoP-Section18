from turtle import Turtle, Screen, colormode
from random import choice, randint

colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
directions = [0, 90, 180, 270]

screen = Screen()
tim = Turtle()
tim.shape("arrow")
tim.width(7)
tim.speed(10)
colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

def random_step():
    tim.setheading(choice(directions))
    tim.pencolor(random_color())
    tim.forward(15)

current = tim.position()
tim.penup()
tim.sety(350)
tim.write("Random Walk",align = "center")
tim.home()
tim.pendown()

for _ in range(250):
    random_step()

tim.hideturtle()
screen.exitonclick()