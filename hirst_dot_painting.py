from turtle import Turtle, Screen, colormode
from random import choice
import turtle

w = Screen()
tim = Turtle()
tim.hideturtle()
tim.penup()
colormode(255)

color_list = [(205, 163, 100),
 (230, 211, 87),
 (206, 90, 130),
 (122, 94, 77),
 (192, 134, 173),
 (103, 174, 210),
 (212, 95, 83),
 (71, 114, 158),
 (67, 123, 87),
 (61, 170, 90),
 (125, 188, 163),
 (223, 173, 191),
 (159, 72, 106),
 (81, 98, 187),
 (155, 210, 205),
 (154, 210, 212),
 (164, 180, 48),
 (223, 178, 173),
 (183, 187, 209),
 (60, 60, 59),
 (88, 145, 156),
 (80, 56, 57),
 (83, 58, 53),
 (74, 48, 51)]

def get_random_color():
    return choice(color_list)

# Draw 10x10 grid of dots
# dot size 10px
# spacing 20px

for x in range(11):
    for y in range(11):
        tim.setx(20*x)
        tim.sety(20*y)
        tim.dot(10, get_random_color())

w.exitonclick()