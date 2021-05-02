import turtle as t
from turtle import Screen

tim = t.Turtle()
tim.shape("turtle")

def dash_line():
    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

for _ in range(4):
    dash_line()
    tim.right(90)

screen = Screen()
screen.exitonclick()