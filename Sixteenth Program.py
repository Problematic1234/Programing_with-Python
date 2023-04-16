# DATE = 8 JANUARY 2022

# TURTLE3

import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.pensize(5)
h = 6
for i in range(2000):
    c = colorsys.hls_to_rgb(h, 0.5, 1)
    t.pencolor(c)
    h += 0.005
    t.circle(i/2, 280)
    t.rt(40)

    for j in range(4):
        t.right(48)

t.hideturtle()
turtle.done()
