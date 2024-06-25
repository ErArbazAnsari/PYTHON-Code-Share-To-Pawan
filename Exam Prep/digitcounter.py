counter=0
number=int(input("Enter Digit : "))
temp=number
while(number>0):
    number//=10
    counter+=1
print(counter)