import turtle
windows=turtle.Screen()
windows.bgcolor("yellow")

turtle.penup()

times=int(input("Enter No. Of Sides "))
degree=360/6
for i in times:
    turtle.forward(50)
    turtle.left(degree)


turtle.done()