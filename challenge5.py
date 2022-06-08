from turtle import Turtle, Screen, circle, colormode
from random import choice, randint

#colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
#directions = [0, 90, 180, 270]

screen = Screen()
tim = Turtle()
tim.shape("arrow")
tim_width = 11
tim.speed("fastest")
colormode(255)
tim_heading = 0
valid_divisors_360 = [12, 18, 24, 36, 45, 72, 90]

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

def draw_circle(heading):
    tim.pencolor(random_color())
    tim.setheading(heading)
    tim.circle(100 + tim.width()*2.5)


current = tim.position()
tim.penup()
tim.sety(350)
tim.write("Spirograph",align = "center")
tim.home()
tim.pendown()

for divisor in valid_divisors_360:
    divisor = int(360/divisor)
    for _ in range(divisor):
        tim.width(tim_width)
        draw_circle(tim_heading)
        tim_heading += 360/divisor
    tim_width -= 1


tim.hideturtle()
screen.exitonclick()