#Finding the Factorial of number

number=int(input("Enter The Number : "))
factorial=1

for i in range(1,number+1):
    factorial=factorial*i
print("Your Factorial is :- ", factorial)