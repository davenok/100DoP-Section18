# Challenge 3 - different shapes

from turtle import Turtle, Screen
from random import choice

colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]

screen = Screen()
tim = Turtle()
tim.shape("arrow")
tim.width(3)
tim.speed(8)

def draw_shape(sides):
    angle = 360/sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)

for sides in range(3, 11):
    tim.pencolor(choice(colors))
    draw_shape(sides)
    
tim.hideturtle()
screen.exitonclick()