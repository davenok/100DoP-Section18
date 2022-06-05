from turtle import Turtle, Screen
# Turtle docs https://docs.python.org/3/library/turtle.html

# basic import
# import turtle
# obj = turtle.Turtle()
#
# from ... import ...
# from turtle import Turtle...
# obj = Turtle()
#
# from turtle import *
# imports everything
# not "good" code, but know it exists
#
# import turtle as t
# obj = t.Turtle()



timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
# https://www.tcl.tk/man/tcl/TkCmd/colors.html
# https://www.wikipython.com/tkinter-ttk-tix/summary-information/and-more-colors-psg/

#Movement
timmy.forward(100)
timmy.right(90)








screen = Screen()
screen.exitonclick()