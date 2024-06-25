import turtle

windows=turtle.Screen()
windows.bgcolor("yellow")
t=turtle.Turtle()
t.shape('circle')
t.pensize(2)
t.color("red")
t.fillcolor("green")
t.begin_fill()
for i in range(0,4):
    t.forward(200)
    t.left(90)

t.circle(120,360)
t.dot(50,"blue")

t.end_fill()
turtle.done()