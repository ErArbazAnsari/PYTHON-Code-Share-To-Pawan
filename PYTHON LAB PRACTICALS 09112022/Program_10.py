print("***** CREATE A LIST AND PERFORM THE FOLLOWING METHODS.")

#Creating List.
list1=[2,4,6,8,10,12,14,16,18,20]
#Printing List.
print("Our List")
print(list1)

#(a) insert() (b) remove() (c) append()
#(d) len() (e) pop() (f) clear()
print("\nUsing insert()")
list1.insert(10,22)
print(list1)

print("\nUsing remove()")
list1.remove(2)
print(list1)

print("\nUsing append()")
list1.append([1,2,3])
print(list1)

print("\nUsing len()")
print(len(list1))

print("\nUsing pop()")
list1.pop(10)
print(list1)

print("\nUsing clear()")
list1.clear()
print(list1)
print(len(list1))
