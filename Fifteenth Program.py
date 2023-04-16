# DATE = 8 JANUARY 2023

# TURTLE2

import turtle as t
t.bgcolor("black")
t.speed(0)
t.hideturtle()

Colors = ["yellow","red","yellow","red"]

for i in range(120):
    for c in Colors:
        t.color(c)
        t.circle(200-i, 100)
        t. left(90)
        t.circle(200 - i, 100)
        t.right(60)
        t.end_fill()

t.mainloop()
