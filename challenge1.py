from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.width(3)

# Challenge 1 - Draw 100x100 square

for _ in range(4):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()