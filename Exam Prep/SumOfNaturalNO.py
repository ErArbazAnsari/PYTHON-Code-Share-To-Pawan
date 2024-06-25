#sum of natural no.
import time
limit=int(input("Enter limit : "))
sum=0
for i in range(1,limit+1):
    print(i)
    sum=sum+i
print(sum)
print("Time Taken")
print(time.time())