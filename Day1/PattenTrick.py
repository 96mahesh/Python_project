import turtle

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

t = turtle.Pen()
t.speed(75)
turtle.bgcolor('white')
for i in range(180):
    t.pencolor(colors[i % 7])
    t.width(i // 100 + 1)
    turtle.begin_fill()
    t.forward(i)
    t.left(59)
turtle.end_fill()
turtle.done()
