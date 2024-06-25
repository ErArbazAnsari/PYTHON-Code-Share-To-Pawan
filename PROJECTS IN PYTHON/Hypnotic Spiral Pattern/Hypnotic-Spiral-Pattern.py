import turtle
colors={"red","orange","yellow","green","blue","purple"}
speed(0)
bgcolor("black")
for x in range(1200):
    color(colors[x%6])
    forward(x*.5)
    left(149)

