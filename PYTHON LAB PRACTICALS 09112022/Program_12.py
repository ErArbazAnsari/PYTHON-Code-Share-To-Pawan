print("***** CREATE A TUPLE AND PERFORM THE FOLLOWING METHODS *****")
'''
(1) Add items 
(2) len() 
(3) check for the item in the tuple 
(4)Access items.'''

#Creating Tuple.
myTuple=(1,2,3,4,5)
#Printing MyTuple
print("Here is My Tuple.")
print(myTuple)

print("\nAdd items in tuple.")
myTuple=myTuple+(6,7,8,9,10)
print(myTuple)

print("\nlength of tuple by using len() method.")
print(len(myTuple))

#Checking the item present in tuple or not.
print("The first tuple is : ")
print(myTuple)
item=int(input("Enter item : "))
print("The value of item has been initialized")

myresult = False
for elem in myTuple :
   if item == elem :
      myresult = True
      break
print("Does the tuple contain the value mentioned ?")
print(myresult)

#Data Accessing in Tupe
print("Here is my Typle")
print(myTuple)
print((myTuple[5]))