print("***** PYTHON PROGRAM TO PRINT TRY, EXCEPT, AND FINALLY BLOCK STATEMENTS *****")

# The 'try' block lets you test a block of code for errors.
# The 'except' block lets you handle the error.
# The 'else' block lets you execute code when there is no error.
# The 'finally' block lets you execute code, regardless of the result of the try- and except blocks.

#The finally block gets executed no matter
#if the try block raises any errors or not:
#Code:
try:
  print(x)
except:
  print("X is Not Defined Please Check.")
finally:
  print("The 'try except and finally' is finished.")