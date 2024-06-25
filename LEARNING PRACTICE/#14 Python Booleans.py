# Boolean Values
# In programming you often need to know if an expression is True or False.
#
# You can evaluate any expression in Python, and get one of two answers, True or False.
#
# When you compare two values, the expression is evaluated and Python returns the Boolean answer:
# #
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# Example
# Print a message based on whether the condition is True or False:
#
#
# var1=int(input("Enter 1st Number :- "))
# var2=int(input("Enter 2nd Number :- "))
#
# if var1>var2:
#     print("The Biggest Value is A.")
# else:
#     print("The Smallest Value is B.")

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,
# #
# print(bool("Hello"))
# print(bool(15))

def myFunction() :
  return True

print(myFunction())

x = 200
print(isinstance(x, int))