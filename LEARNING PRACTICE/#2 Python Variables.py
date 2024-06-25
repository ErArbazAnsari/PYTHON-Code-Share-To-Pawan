#Variables are containers for storing data values.

#How to create variable in python
"""var="arbaz"
print(var)

num=input("Enter the number")
print(num)

var1=int(input("Enter Any number : "))
print(var1)
print(type(var1))

x, y, z= "Arbaz", "Arman", "Ashfaq"
print(x)
print(y)
print(z)

x1=y1=z1= "Arbaz"
print(x1)
print(y1)
print(z1)
"""

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)
# print(fruits)


#Output Variables
# x = "Python is awesome"
# print(x)

# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)
#
# var1=5
# var2='arbaz'
# print(type(var2))
# print(var1+var2)


# Python - Global Variables

var5='My is arbaz'
def fun1():
    print("What is your name ")
    print(var5)
fun1()


x = "awesome"

def myfunc():
    global x
    x = "fantastic"
    print("Python is ",  x)

myfunc()

print("Python is " , x)