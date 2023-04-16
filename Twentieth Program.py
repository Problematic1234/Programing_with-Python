# DATE =  19 JANUARY 2023

# TURTLE5

import turtle as t
import colorsys as cs

t.speed(0)
t.bgcolor("black")
for i in range(1000):
    t.color(cs.hsv_to_rgb(i/300,0.5,1))
    t.fd(i)
    t.lt(59)

t.hideturtle()
t.done()
