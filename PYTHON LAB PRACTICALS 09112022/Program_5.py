print("***** PYTHON PROGRAM TO FIND THE FACTORIAL OF A NUMBER USING RECURSION *****")
def recursive_factorial(n):
   if n == 1:
       return n
   else:
       return n*recursive_factorial(n-1)

num=int(input("Enter The Number --> "))

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recursive_factorial(num))