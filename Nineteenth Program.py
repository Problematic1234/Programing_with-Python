# DATE =  11 JANUARY 2023

# TURTLE4

from turtle import *
bgcolor('black')
speed(0)
hue = 1
colors = ['red', 'green', 'blue', ]

for i in range(720):
    color(colors[i % 3])
    fd(hue)
    lt(120)
    lt(1)
    hue = hue + 1

done()
