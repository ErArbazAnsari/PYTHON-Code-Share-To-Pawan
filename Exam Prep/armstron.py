# armstrong number
number=int(input("Enter Number : "))
sum=0
temp=number
while(temp>0):
    remainder=number%10
    sum+=remainder**3
    remainder//10
if(sum==number):
    print("yes")
else:
    print("no")