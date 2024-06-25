mysum=0
number=296
temp=number
while(number):
    i=1
    fact=1
    remainder=number%10
    while(i<=remainder):
        fact=fact*i
        i=i+1
    mysum=mysum+fact
    mysum=mysum//10
if(mysum==temp):
    print("Te number is strong number")
else:
    print("Number is not strong number")# Variable to store sum of the numbers  
sum=0  
# Ask user to enter the number  
num=int(input("Enter a number:"))  
# temporary variable  store copy of the original number  
temp=num  
# Using while loop  
while(num):  
    # intialize with 1  
    i=1  
    # fact variable with 1  
    fact=1  
    rem=num%10  
    while(i<=rem):  
        fact=fact*i   # Find factorial of each number  
        i=i+1  
    sum=sum+fact  
    num=num//10  
if(sum==temp):  
    print("Given number is a strong number")  
else:  
    print("Given number is not a strong number")  