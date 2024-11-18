import turtle

colors = ["yellow", "red", "yellow", "red"]
for i in range(120):
    for c in colors:
        turtle.color(c)
        turtle.circle(200 - i, 100 - 1)
        turtle.lt(90)
        turtle.circle(200 - i, 100 - 1)
        turtle.rt(60)
        turtle.end_fill()
turtle.mainloop()
