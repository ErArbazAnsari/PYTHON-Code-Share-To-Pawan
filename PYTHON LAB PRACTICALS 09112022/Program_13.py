print("**** CREATE A DICTIONARY AND APPLY THE FOLLOWING METHODS *****")
'''(1) Print the dictionary items 
(2) access items 
(3) use get() 
(4) change values 
(5) use len().'''
mydict={'A':1,'B':5,'C':3}
print(mydict)

print("Printing Dictionary Values.")
print(mydict.values())

print("\nAccessing items.")
print(mydict)
print(mydict['A'])
print(mydict['B'])
print(mydict['C'])

values=mydict.values()
values=list(values)
print(values)

#Using Get()
print(mydict.get("A"))
print(mydict.get("B"))
print(mydict.get("C"))

print("\n\nLength of Dictionary.")
print(len(mydict))

#changing the values of key present in dictionary.
mydict['A']=24018
mydict['B']=24000
mydict['C']=20000
print(mydict)