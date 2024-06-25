print("Write a program that accepts the lengths of three sides of a triangle as input the program \noutput should indicate whether or not the triangle, is a right triangle (recall from the \nPythagorean theorem that in a right triangle, the square "
      "of one side equals the sum of the squares of the other two side.")

base=float(input("Enter length of Base : "))
perp=float(input("Enter length of Perpendicular : "))
hypo=float(input("Enter length of Hypotenuse : "))

if hypo**2==((base**2)+(perp**2)):
    print("It's a right triangle")
else:
    print("It's not a right triangle")