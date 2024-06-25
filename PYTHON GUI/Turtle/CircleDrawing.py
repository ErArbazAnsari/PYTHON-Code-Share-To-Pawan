import turtle
wh=turtle.Screen()
wh.bgcolor("lightblue")
t=turtle.Turtle("square")
t.color("red")
t.speed(0)
t.begin_fill()
for i in range(0,360):
    t.forward(2)
    t.left(1)
t.end_fill()

t.color("green")
t.begin_fill()
for i in range(0,360):
    t.forward(1.5)
    t.left(1)
t.end_fill()

t.color("white")
t.begin_fill()
for i in range(0,360):
    t.forward(1)
    t.left(1)
t.end_fill()
t.done()
