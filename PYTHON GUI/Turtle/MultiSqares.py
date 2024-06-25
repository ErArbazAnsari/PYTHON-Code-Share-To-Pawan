import turtle
wh=turtle.Screen()
wh.bgcolor("lightblue")
t=turtle.Turtle("square")
t.color("red")
t.speed(5)
t.begin_fill()

for i in range(1,5):
        t.forward(200)
        t.left(90)
        for i in range(1,5):
            t.forward(175)
            t.left(90)
            for i in range(1, 5):
                t.forward(200)
                t.left(90)
                for i in range(1, 5):
                    t.forward(175)
                    t.left(90)

# t.done()
