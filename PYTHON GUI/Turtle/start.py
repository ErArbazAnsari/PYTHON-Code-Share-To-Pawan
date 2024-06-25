import turtle

window=turtle.Screen()
t=turtle.Turtle()
t.pensize(6)
for i in range(1):
    for j in ["red","blue","black","green","yellow"]:
        t.pencolor(j)
        t.forward(200)
        t.right(144)
turtle.done()