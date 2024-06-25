import math as m

num = int(input("Enter Value of N: "))
print("\n")
print("O(C): ",1)
print("\n")
print("O(log(log(n))): ",m.log2(m.log2(num)))
print("\n")

print("O(log2(num)): ",m.log2(num))
print("\n")

print("O(pow(num,(1/2))): ",pow(num,(1/2)))
print("\n")

print("O(num): ",num)
print("\n")

print("O(m.log2(num)): ",num*(m.log2(num)))
print("\n")

print("O(num^2): ",num*num)
print("\n")

print("O(num^3): ",num*num*num)
print("\n")

print("O(pow(2,num)): ",2^num)
print("\n")

print("O(pow(num,num)): ",num^num)
print("\n")

print("O(pow(2,pow(2,num))): ",pow(2,pow(2,num)))
print("\n")
