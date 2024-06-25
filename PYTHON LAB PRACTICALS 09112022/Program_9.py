import math
print("***** WRITE A PYTHON PROGRAM THAT ACCEPTS THE RADIUS OF A CIRCLE \nFROM THE USER AND COMPUTES THE AREA. *****")

#Input
radiusOfCircle=float(input("Enter the Radius of Circle --> "))

areaOfCircle=math.pi*radiusOfCircle*radiusOfCircle
areaOfCircle=round(areaOfCircle,2)
#Output
print("This Area of the Circle is :",areaOfCircle)