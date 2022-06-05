from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.width(3)
tim.speed(1)

# Challenge 2 - Draw dashed line - 10 on 10 off. 200 long

for _ in range(10):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)

tim.hideturtle()

screen = Screen()
screen.exitonclick()