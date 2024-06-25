import random as rnd
import time

# number = rnd.randint(0, 10)
# print(number)
start_time = time.time()
for i in range(1,1000000):
    number = rnd.randint(0, 10)
    print(number, end=' ')
print("Time taken:\n\n", time.time() - start_time, "seconds")