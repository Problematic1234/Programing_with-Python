# DATE =  19 JANUARY 2023

# Turtle To Print Your Name

import turtle as t

t.pen()
t.bgcolor('black')

colors = ["red", "green", "yellow", "blue", "gray", "purple", "aqua", "brown", "pink", "magenta", "light blue", "light green", "white", "light red", "golden", "silver", "orange", "cyan", "Light Brown", "indigo"]
name = t.textinput("Enter your name Please", "Enter your name Please")
s = int(t.numinput("Number Of Sides", "How Many Sides You Want(1-20)", 10, 1, 20))

for i in range(1000):
    t.pencolor(colors[i % s % 10])
    t.penup()
    t.forward(i * 4)
    t.pendown()
    t.write(name, font=("Gill Sans Ultra Bold",
                        int((i * 2 + 4) / 4), "bold"))
    t.left(360 / s + 4)
